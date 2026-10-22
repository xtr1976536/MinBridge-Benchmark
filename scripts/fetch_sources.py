#!/usr/bin/env python3
"""Download and validate source datasets listed in sources.json."""

import argparse
import hashlib
import json
import pathlib
import urllib.request


ROOT = pathlib.Path(__file__).resolve().parents[1]


def read_jsonl(path):
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/raw")
    parser.add_argument("--include-unlicensed", action="store_true")
    args = parser.parse_args()

    output = pathlib.Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.mkdir(parents=True, exist_ok=True)

    manifest = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
    report = []
    for source in manifest:
        if source["kind"] == "huggingface":
            continue
        if "No license declared" in source["license_note"] and not args.include_unlicensed:
            report.append({"name": source["name"], "status": "skipped_unlicensed"})
            continue

        suffix = ".jsonl" if source["kind"] == "jsonl" else ".json"
        name = source["name"].lower().replace(" ", "_").replace("/", "_")
        destination = output / f"{name}{suffix}"
        request = urllib.request.Request(
            source["url"], headers={"User-Agent": "MinBridgeBenchmarkDataAudit/0.1"}
        )
        with urllib.request.urlopen(request, timeout=120) as response:
            payload = response.read()
        destination.write_bytes(payload)

        rows = read_jsonl(destination) if source["kind"] == "jsonl" else json.loads(payload)
        count = len(rows)
        expected = source.get("expected_count")
        report.append(
            {
                "name": source["name"],
                "status": "ok" if expected is None or count == expected else "count_mismatch",
                "path": str(destination),
                "count": count,
                "expected_count": expected,
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
        )

    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
