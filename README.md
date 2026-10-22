# MinBridge Benchmark Research

This repository tracks publicly obtainable datasets and a reproducible data plan for evaluating relational hallucination, evidence sufficiency, and abstention in financial numerical reasoning.

## Research brief

The attached MinBridge proposal requires three distinct kinds of evidence:

1. Answerable financial numerical QA with contexts, executable gold reasoning, and answer checks.
2. Controlled unanswerable twins with a clear missing fact or invalid relation, plus minimal missing-data certificates.
3. Independent real-analyst questions with answerability labels and expert-reviewed reasoning evidence.

The first category is available now. The second can be built from public answerable datasets, but requires proof-based filtering and human review. The third is only partly available: FinDER provides authentic financial search queries with answerability-like `reasoning` labels and filing evidence, but its tasks are mostly open-book RAG and not tied to numeric gold programs or minimal certificates. No public dataset located directly provides all requested annotations.

## Access-checked sources

| Source | What it contributes | Access result | License / caveat | Link |
|---|---|---|---|---|
| FinQA | Financial report/table questions, answers, gold programs and supporting facts | Official GitHub files download directly; 1,147 test examples | Repo code has MIT; benchmark site states data CC BY 4.0. Underlying report content remains third-party SEC filings; retain attribution and review redistribution scope | [Repo](https://github.com/czyssrs/FinQA), [test.json](https://raw.githubusercontent.com/czyssrs/FinQA/main/dataset/test.json) |
| TAT-QA | Hybrid table/text financial QA, derivation, answer type and report context | Official JSON splits download directly; test gold file available in GBFR repo | Repo MIT; report material is third-party. Preserve original split and attribution | [Repo](https://github.com/NExTplusplus/TAT-QA), [test gold](https://raw.githubusercontent.com/NExTplusplus/TAT-QA/master/dataset_raw/tatqa_dataset_test_gold.json) |
| FinanceReasoning | 2,238 financial numerical QA examples, Python solution, context and ground truth | Official repo splits and files directly downloadable | Data CC BY-NC-SA 4.0 and intended for noncommercial research; source documents may carry third-party restrictions | [Repo](https://github.com/BUPT-Reasoning/FinanceReasoning), [Easy](https://raw.githubusercontent.com/BUPT-Reasoning/FinanceReasoning/master/data/FinanceReasoning/easy.json), [Medium](https://raw.githubusercontent.com/BUPT-Reasoning/FinanceReasoning/master/data/FinanceReasoning/medium.json), [Hard](https://raw.githubusercontent.com/BUPT-Reasoning/FinanceReasoning/master/data/FinanceReasoning/hard.json) |
| FinanceBench | 150 open evaluation cases with question, answer, justification, evidence; referenced filing PDFs | Direct JSONL download tested (150 rows); document metadata JSONL (361 rows) direct | No GitHub license declared; do not redistribute files in a new benchmark until terms are confirmed. Excellent independent external test | [Repo](https://github.com/patronus-ai/financebench), [150 cases](https://raw.githubusercontent.com/patronus-ai/financebench/main/data/financebench_open_source.jsonl), [document metadata](https://raw.githubusercontent.com/patronus-ai/financebench/main/data/financebench_document_information.jsonl) |
| FinDER | 5,703 real-world financial query / evidence / answer triplets; boolean `reasoning`, query and source context | Hugging Face viewer and Parquet access; publicly downloadable | Dataset card says CC BY-NC 4.0. Realistic analyst-style questions, but mostly qualitative and not an exact fit for numerical relation hallucination | [Dataset](https://huggingface.co/datasets/Linq-AI-Research/FinDER), [paper](https://arxiv.org/abs/2504.15800) |
| GBFR released counterfactuals | Directly relevant negative financial twins and modification type | All three JSON files download from the paper's official repo; counts checked: FinQA 97, TAT-QA 151, FinanceReasoning 412 | Repo has no declared license. File is usable for inspection/reproduction, but legal permission for republishing/adapting is unresolved. Does not supply bridge-relation labels, MSS, certificates, or proof scans | [Paper repo](https://github.com/aolaoban/Graph-Bounded_Financial_Reasoning), [FinQA negatives](https://raw.githubusercontent.com/aolaoban/Graph-Bounded_Financial_Reasoning/main/data/FinQA/finqa_nsdata.json), [TAT-QA negatives](https://raw.githubusercontent.com/aolaoban/Graph-Bounded_Financial_Reasoning/main/data/TAT-QA/tatqa_nsdata.json), [FinanceReasoning negatives](https://raw.githubusercontent.com/aolaoban/Graph-Bounded_Financial_Reasoning/main/data/FinanceReasoning/financereasoning_nsdata.json) |
| CFBenchmark | Chinese financial text-processing dataset, some numerical calculation subset | Official repo and Hugging Face page exist; repo data paths differ from the numerical set mentioned by GBFR | Public repo's main benchmark targets text tasks; GBFR's copied numerical files have unclear redistribution terms. Do not count as a ready source until exact subset provenance is verified | [Repo](https://github.com/TongjiFinLab/CFBenchmark), [HF](https://huggingface.co/datasets/TongjiFinLab/CFBenchmark) |
| UMWP / AbstentionBench | General-domain answerable/unanswerable math twins; pairs and answerability labels | Direct JSONL URL tested; official loader and subset index provided | UMWP dataset repo has no license declared; useful as cross-domain prototype, not a financial benchmark | [Data repo](https://github.com/Yuki-Asuuna/UMWP), [AbstentionBench loader](https://github.com/facebookresearch/AbstentionBench/blob/main/recipe/abstention_datasets/umwp.py) |
| SEC EDGAR / XBRL | Official source for filing documents, company facts and structured financial facts | Official JSON APIs; per-company facts and filing indices are directly accessible | Use SEC fair-access rules and include identifying User-Agent; suitable for future independently authored examples, not ready QA annotations | [Developer resources](https://www.sec.gov/about/developer-resources), [API docs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) |
| FinTextQA | Financial long-form QA | Dataset is not released: upstream repository explicitly says textbook subset lacks permission to open source | Not obtainable as a complete public dataset; exclude from direct data plan | [Repo](https://github.com/AlexJJJChen/FinTextQA), [paper](https://aclanthology.org/2024.acl-long.328/) |

The GBFR paper itself is ACL 2026 Long Paper 1273: [Anthology page](https://aclanthology.org/2026.acl-long.1273/). Its artifact files are accessible, but neither the GitHub repository nor its data files declare an explicit license. Access does not imply permission to redistribute derivatives.

## What must be created or annotated

| Proposed step | Existing direct data? | Feasibility and work needed |
|---|---|---|
| FinQA answerable baseline and 150-question pilot | Yes | Use the official test split and gold program; avoid mixing train/dev/test across twins |
| PoT/CoT response runs and numeric-vs-relational error labels | No model outputs are supplied for the study's model matrix | Generate outputs under fixed prompts/settings; blind two annotators to method; calculate agreement and adjudicate |
| Answerable/unanswerable financial twin set | Partial | GBFR supplies a small set of entity/time/metric perturbations; construct new twins by removing gold-used facts and related-but-unused facts from FinQA, TAT-QA and FinanceReasoning |
| Proof that a question is truly unanswerable | No | Enumerate numeric facts and bounded arithmetic closure; formalize permitted transformations and units; reject a negative if target remains derivable. Then manually inspect all benchmark negatives and audit a random 200 with two annotators |
| Minimal missing-data certificate | No | Derive from the gold program's leaf operands, then minimize against alternative valid paths and available context. A single gold program is insufficient to prove global minimality when alternate derivations exist |
| Relation provenance tiers T0-T4 | No | Publish a sourced, frozen formula/definition inventory. Use primary standards where accessible and separately sourced textbooks. Mark definitions with source, jurisdiction, date and permitted scope; sensitivity-test contested T3/T4 boundaries |
| Minimal sufficient sets and counterfactual relation credit for SCPO | No | Generate from annotated formula hypergraphs and exhaustive/minimal-set search on small examples; manual validation required. Ensure the target's identifiability matches the operational solver semantics |
| Independent real analyst test, about 300 questions | Closest: FinDER (5,703 real queries), FinanceBench (150 questions) | FinDER is best query-style source but not numeric-program aligned; FinanceBench is numerical and evidence rich but small and unlicensed for redistribution. Use FinDER/FinanceBench under their own terms for evaluation only, then obtain permission or collect original questions via a documented analyst study |
| Cross-domain abstention generalization | Partial | UMWP is available and paired but is general math; another source such as NeoQA tests evidence sufficiency but fictional non-numeric news and has a non-derivative license. Use only as a separate external task, not as direct MinBridge training data |

## Recommended benchmark construction

1. Start with FinQA test (1,147), TAT-QA test-gold, and selected FinanceReasoning examples. Keep the original source ID and split in every derived row. FinanceReasoning redistribution is noncommercial/share-alike; treat those examples as a separately licensed component.
2. Make two controlled twins per eligible answerable item: (a) remove one or more gold-program leaf facts; (b) remove a relevant-looking fact unused by every valid derivation. Preserve the original question wording and context otherwise, and record exact context spans removed.
3. Construct a fact inventory as typed tuples `(metric, entity, period, unit, value, span)` and a relation inventory with formula, source, jurisdiction, definition tier and declaration status. Include common unit conversions explicitly.
4. Run a bounded derivability checker over admissible relations. Enumerate one- and two-step arithmetic combinations as the proposal states, but avoid treating arbitrary arithmetic as an accepted relation. Detect alternative derivations and duplicate numeric values. Drop ambiguous negatives.
5. Calculate missing certificates by finding the smallest set of facts whose addition restores derivability, allowing all accepted formula paths. Validate “all certificate facts restore answerability” and “removing any one does not” mechanically, then have annotators check the semantic interpretation.
6. Independently annotate an initial 200 items and report Cohen's kappa or Krippendorff's alpha by label. Double-annotate every disputed example and all test-set examples. Keep rationale, evidence spans, adjudication, annotator guide version and provenance.
7. Split by report/document/company and source dataset before generating twins, so an original and all its variants remain in one split. Deduplicate near-identical contexts across datasets. Keep a locked test set and hash every source file and generated release.
8. For the independent analyst set, ask two finance practitioners to write or contribute de-identified questions against publicly cited filings. Record consent and rights to publish question text, answerability labels, evidence spans and corrections. If these rights are unavailable, report FinDER and FinanceBench strictly as external evaluations with their current provenance.

## Download verification

The following upstream files were fetched over HTTPS and parsed successfully during the audit:

- GBFR `finqa_nsdata.json`: 97 records, fields include context, table, question, answer, steps and negative sample details.
- GBFR `tatqa_nsdata.json`: 151 records, includes answer type, derivation and negative sample details.
- GBFR `financereasoning_nsdata.json`: 412 records, includes Python solution, ground truth and negative sample details.
- FinanceBench open JSONL: 150 records, with question, answer, justification and evidence.
- FinanceBench document JSONL: 361 metadata rows with linked filing PDFs.
- FinQA official `test.json`: 1,147 records.
- FinanceReasoning official `easy.json`: 1,000 records.
- UMWP JSONL URL: available; the AbstentionBench loader confirms paired answerable/unanswerable structure.
- FinTextQA repository README: available; states part of the actual dataset cannot be open sourced.

This audit establishes download and parse availability, not the right to redistribute each source's content.

## Immediate decision

The benchmark is feasible from public inputs if MinBridge is presented as a new, carefully annotated derived benchmark. FinQA/FinanceReasoning/TAT-QA supply answerable program-based sources; GBFR's released negatives give a useful seed; FinDER and FinanceBench provide independent realistic financial query evaluations. No public source provides the complete benchmark as specified. The essential original work is negative-set verification, relation provenance, minimal certificates, and a rights-cleared real-analyst set.
