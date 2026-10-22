#!/usr/bin/env python3
"""Check access and structure of registered datasets without mirroring them in Git."""

import argparse
import csv
import hashlib
import io
import json
import pathlib
import urllib.parse
import urllib.request
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone


ROOT = pathlib.Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "sources.json"
USER_AGENT = "MinBridgeBenchmarkAudit/1.0 (academic dataset verification)"


def fetch_bytes(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                return response.read()
        except Exception:
            if attempt == 2:
                raise
            time.sleep(1 + attempt)


def hf_page(source, offset):
    params = urllib.parse.urlencode(
        {
            "dataset": source["dataset"],
            "config": source["config"],
            "split": source["split"],
            "offset": offset,
            "length": 100,
        }
    )
    body = json.loads(fetch_bytes("https://datasets-server.huggingface.co/rows?" + params))
    return [item["row"] for item in body["rows"]], body["num_rows_total"]


def inspect_rows(source, rows):
    result = {"records": len(rows), "fields": sorted(rows[0]) if rows else []}
    if source["id"] == "tatqa-test-gold":
        questions = [q for context in rows for q in context["questions"]]
        result["nested_questions"] = len(questions)
        result["answer_types"] = dict(Counter(q.get("answer_type") for q in questions))
    elif source["family"] == "FinanceReasoning":
        result["source_families"] = dict(
            Counter(str(row.get("source", "")).split("-")[0] for row in rows)
        )
        result["missing_python_solution"] = sum(not row.get("python_solution") for row in rows)
    elif source["id"] == "finder":
        result["operation_types"] = dict(Counter(str(row.get("type")) for row in rows))
        result["reasoning_flag"] = dict(Counter(str(row.get("reasoning")) for row in rows))
        result["unique_questions"] = len({row.get("text") for row in rows})
    elif source["family"] == "CFQA":
        result["empty_answers"] = sum(not row.get("答案") for row in rows)
        result["reported_not_found_answers"] = sum(
            isinstance(row.get("答案"), str) and "无法在年报中找到" in row["答案"]
            for row in rows
        )
        result["empty_page_evidence"] = sum(not row.get("答案出自") for row in rows)
    elif source["family"] == "GBFR":
        result["mutation_types"] = dict(
            Counter(row.get("negative_sample_details", {}).get("modification_type") for row in rows)
        )
    elif source["id"] == "finqa-test":
        result["missing_gold_program"] = sum(not row.get("qa", {}).get("program") for row in rows)
    return result


def audit_source(source, output):
    fmt = source["format"]
    if fmt == "hf_rows":
        first, total = hf_page(source, 0)
        offsets = range(100, total, 100)
        with ThreadPoolExecutor(max_workers=4) as pool:
            pages = list(pool.map(lambda offset: hf_page(source, offset), offsets))
        if any(page_total != total for _, page_total in pages):
            raise ValueError("Hugging Face dataset changed during pagination")
        rows = first + [row for page, _ in pages for row in page]
        payload = json.dumps(rows, ensure_ascii=False, sort_keys=True).encode("utf-8")
        suffix = ".json"
    else:
        payload = fetch_bytes(source["url"])
        suffix = "." + fmt
        if fmt == "json":
            rows = json.loads(payload)
        elif fmt == "jsonl":
            rows = [json.loads(line) for line in payload.splitlines() if line.strip()]
        elif fmt == "csv":
            rows = list(csv.DictReader(io.StringIO(payload.decode("utf-8-sig"))))
        else:
            raise ValueError(f"Unknown format: {fmt}")

    if not isinstance(rows, list):
        raise ValueError("Expected a top-level list of records")
    destination = output / (source["id"] + suffix)
    destination.write_bytes(payload)
    detail = inspect_rows(source, rows)
    expected = source.get("expected_records")
    status = "ok" if expected is None or detail["records"] == expected else "count_mismatch"
    return {
        "id": source["id"],
        "status": status,
        "format": fmt,
        "license_status": source["license_status"],
        "sha256": hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "expected_records": expected,
        **detail,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/raw")
    parser.add_argument("--report", default="audit/access-check.json")
    parser.add_argument("--ids", nargs="*", help="Audit only these registry IDs")
    parser.add_argument("--include-unknown-license", action="store_true")
    args = parser.parse_args()

    sources = json.loads(REGISTRY.read_text(encoding="utf-8"))
    registered_ids = {source["id"] for source in sources}
    requested = set(args.ids or registered_ids)
    unknown = requested - registered_ids
    if unknown:
        parser.error("Unknown source IDs: " + ", ".join(sorted(unknown)))

    output = pathlib.Path(args.output)
    report_path = pathlib.Path(args.report)
    if not output.is_absolute():
        output = ROOT / output
    if not report_path.is_absolute():
        report_path = ROOT / report_path
    output.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    results = []
    for source in sources:
        if source["id"] not in requested:
            continue
        if source["license_status"] != "confirmed" and not args.include_unknown_license:
            results.append({"id": source["id"], "status": "skipped_unknown_license"})
            continue
        try:
            results.append(audit_source(source, output))
        except Exception as exc:
            results.append({"id": source["id"], "status": "error", "error": str(exc)})

    report = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "registry": str(REGISTRY.relative_to(ROOT)),
        "results": results,
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(Counter(item["status"] for item in results), indent=2))
    print(report_path)
    if any(item["status"] in ("error", "count_mismatch") for item in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
