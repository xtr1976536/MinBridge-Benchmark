# MinBridge benchmark data audit

This repository audits public data against the MinBridge research proposal. It is a source registry and construction protocol, **not a completed benchmark or an annotated 300-question test set**.

Audit date: 2026-10-22. The audit has three passes: [source and license](docs/audit.md#round-1-source-and-file-integrity), [task fit and independence](docs/audit.md#round-2-task-fit-and-independence), and [reproducibility and release](docs/audit.md#round-3-reproducibility-and-release). The exact requirements are in [requirements.md](docs/requirements.md). All investigated sources and exclusions are in [sources.md](docs/sources.md). A dedicated [real analyst question review](docs/analyst_questions.md) covers the planned 300-question set.

## Current decision

- **Answerable numerical QA:** FinQA, TAT-QA and FinanceReasoning have accessible contexts and gold answers. FinQA and FinanceReasoning include executable reasoning; TAT-QA has derivations, not a uniform executable program. FinanceReasoning reuses FinQA/TAT-QA examples and must be deduplicated before any independent comparison.
- **Unanswerable financial QA:** GBFR releases 660 negative examples across three files, but its repository has no declared license. Its mutations are entity/time/term substitutions, not MinBridge's missing-leaf and irrelevant-deletion twins. No released set includes proof of non-identifiability or minimal missing-data certificates.
- **Real analyst questions:** FinDER is the best source of observed professional queries. All 5,703 public rows were inspected by the audit; 883 carry an operation-type label, but the labels need review. No public set already supplies 300 *verified numerical* questions with MinBridge's answerability and relation-support labels. CFQA adds real investor questions in Chinese but has provenance and released-count caveats.
- **Cross-task missing premises:** RealFin has 367 English and 175 Chinese missing-condition items. It is an external missing-premise test, not a financial-document relation benchmark.

## Reproduce access checks

The machine-readable [source registry](data/sources.json) records download links, sample-count expectations, scope and explicit permission status. The standard-library auditor downloads only sources with a confirmed dataset license and writes all raw data under ignored `data/raw/`.

```bash
python3 scripts/audit_sources.py --output data/raw --report audit/access-check.json
```

To inspect a source with unknown redistribution terms locally, specify its ID and `--include-unknown-license`; this does not add its data to Git. The auditor records SHA-256, record counts, field names and source-specific checks. It does not certify semantic answerability.

## Repository layout

```text
data/sources.json          source registry and explicit permission states
docs/requirements.md       proposal-derived acceptance criteria
docs/sources.md            source-by-source research findings
docs/analyst_questions.md  focused review for authentic analyst questions
docs/audit.md              three review rounds, changes and remaining gaps
scripts/audit_sources.py   reproducible access and structure checks
audit/                    generated metadata reports, no third-party data
data/raw/                 local downloads, Git-ignored
```

The repository's MIT license covers only original audit code and documentation. Upstream datasets retain their own terms; the registry links to them rather than mirroring their contents.
