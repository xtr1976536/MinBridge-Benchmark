# Dataset decisions and source evidence

All counts below refer to released files checked on 2026-10-22, unless explicitly described as paper claims. A usable source is not a completed MinBridge label set.

## Core financial numerical sources

| Source | Verified release | Provenance and task fit | Terms and decision |
|---|---|---|---|
| [FinQA](https://github.com/czyssrs/FinQA) | Test 1,147 rows; no missing `qa.program` | Expert-written report QA, table/text facts, DSL gold programs. Strong E1 and twin-construction input | [Dataset site CC BY 4.0](https://finqasite.github.io/about.html); code MIT. Retain attribution and source IDs |
| [TAT-QA](https://github.com/NExTplusplus/TAT-QA) | 277 test contexts, 1,663 nested questions: 699 arithmetic, 40 count, 714 span, 210 multi-span | Use 699 arithmetic questions for the strict calculation subset; all have derivations. Derivations need parsing and operand alignment; not all 1,663 are numerical | [Dataset site CC BY 4.0](https://nextplusplus.github.io/TAT-QA/); code MIT |
| [FinanceReasoning](https://huggingface.co/datasets/BUPT-Reasoning-Lab/FinanceReasoning) | Easy 1,000, medium 1,000, hard 238; all include Python solution | 795 source IDs begin CodeFinQA; 288 begin CodeTAT-QA; 908 begin FinanceReasoning; remainder FinanceMath/FinCode. Treat as related source families, not independent datasets | Official HF card CC BY 4.0. GitHub lacks a LICENSE. Earlier CC BY-NC-SA assertion was wrong and referred to Tongji FinReasoning, a distinct project |
| [GBFR counterfactuals](https://github.com/aolaoban/Graph-Bounded_Financial_Reasoning) | 97 FinQA + 151 TAT-QA + 412 FinanceReasoning = 660 negatives | Exact mutation types: FinQA Entity 35, Time 27, Term 35; TAT-QA Entity 55, Time 41, Term 55; FinanceReasoning Entity 163, Time 91, Term 158. No minimal missing certificates or support tiers. In 2 FinanceReasoning rows top-level question differs from `negative_question` | No declared repository license. Link as reproduction seed; skip default download. Upstream CC BY license does not automatically license GBFR's additional transformations |

## Independent observed-query sources

See [analyst_questions.md](analyst_questions.md) for detailed provenance.

| Source | Verified release | Fit and caveat | Decision |
|---|---|---|---|
| [FinDER](https://huggingface.co/datasets/Linq-AI-Research/FinDER) | All 5,703 rows fetched; 883 operation-type candidates | Observed professional service queries and evidence; published corpus removed questions lacking 10-K evidence. `reasoning` is not answerability | Priority E2 candidate, CC BY-NC 4.0. Need a verified 300-row numerical subset, fixed contexts and independent annotations |
| [CFQA](https://github.com/ygan/CFQA) | Company split 7,250/961/2,100 = 10,311. Year split 7,199/1,028/2,084 = 10,311; these are alternative partitions, not distinct datasets | Paper sources questions from China Investor Forum, but also substitutes company names to reuse intents. Investor identity does not establish professional-analyst status. Source PDFs not bundled | New external candidate only, repository MIT. Paper says 13,643 rows; do not use that number as released count. Empty answer/page fields and “not found” statements are separate categories |
| [STRUX](https://huggingface.co/datasets/BUILDERlym/STRUX-Transcripts) | API sample accessible; dataset card full split 11,411, test 587; site reports collection 11,950 | Actual analyst speech, names/positions, ticker/date. Collection total and released split differ. Much is forward-looking/qualitative; no numerical gold program | Source-linked research candidate. No dataset license found; Motley Fool transcript source requires separate rights review |
| [EvasionBench](https://huggingface.co/datasets/FutureMa/EvasionBench) | Public HF parquet about 16.7k; official project links this dataset. GitHub includes only six example CSV cases | Actual call Q&A, but released labels are model evasion labels; paper's 84k train/1k human test claim is not the downloaded public file's schema | Secondary candidate only. Card Apache-2.0; S&P Capital IQ source rights and original transcript links need review |

CFQA's company split has 2,069 answers containing the exact phrase “无法在年报中找到” and 423 empty answers. This is not a clean 2,492-item unanswerable test: “not found by annotator”, a missing answer and a structural impossibility are different. The [paper](https://link.springer.com/article/10.1140/epjds/s13688-025-00601-6) says 2,065 questions without report answers and 1,000 unavailable reports; do not conflate those claims with released rows.

## External tasks and missing-premise alternatives

| Source | Actual accessible release | Decision |
|---|---|---|
| [RealFin official](https://github.com/xnlp-lab/RealFin) | 367 English and 175 Chinese CSV items; repository Apache 2.0 | New E4-related missing-premise contrast. Exam-style multiple choice; not a cross-domain non-finance test and not analyst QA. Use the paper-linked xnlp-lab repo rather than an unlicensed mirror |
| [UMWP](https://github.com/Yuki-Asuuna/UMWP) | JSONL link publicly available; [AbstentionBench adapter](https://github.com/facebookresearch/AbstentionBench/blob/main/recipe/abstention_datasets/umwp.py) specifies 2,600 answerable + 2,600 unanswerable paired rows | General math E4 candidate. No dataset license found in repo; not admitted to default fetch |
| [NeoQA](https://github.com/amazon-science/NeoQA) | Encrypted files and a public decryption key; fictional-event evidence sufficiency task | Separate evaluation only; non-derivative release instruction, no plaintext mirroring. Not numerical finance |
| [FinSearchComp](https://github.com/randomtutu/FinSearchComp) | 635 full JSON records; AkShare variant 594 (not an additional corpus) | CC BY 4.0; expert-authored search tasks. Select static filing questions only if adapting to bounded-document MinBridge; no natural unanswerable labels |
| [FinanceBench](https://github.com/patronus-ai/financebench) | 150 public JSONL, 361 document-metadata rows; paper total 10,231 | External test candidate, not 10,231 public samples. No repository license found; do not mirror |
| [Vals v1 public](https://huggingface.co/datasets/vals-ai/finance_agent_benchmark) | 50 CSV rows of a 537-item reported benchmark | CC BY 4.0; expert-authored, not observed requests. Do not count private 150 validation or held-out test |
| [BigFinanceBench](https://github.com/Rogo-Technologies/big-finance-benchmark) | 50 JSONL rows of 928 reported; reference single-number answer plus rubrics | Public data CC BY 4.0, marked evaluation-only/do-not-train. Not SCPO training input |
| [FinanceQA](https://huggingface.co/datasets/AfterQuery/FinanceQA) | 148 CSV rows; dataset card Apache 2.0 | Useful assumption/definition examples, but benchmark-authored and not a verified 300 natural question pool |
| [FinRAG-QA](https://github.com/Lsilotto/FinRAG-QA) | XLSX 46,903 bytes, 999 data rows | Template questions and directly reported values, not derivational questions. No license declared. Exclude from primary relation evaluation |
| [FinanceGym](https://financegym.github.io/) | Provider describes 400 public questions and withheld rubrics | Search lead evaluated for fit, not admitted as a checked raw dataset. Cited-report/forecast evaluation differs from deterministic numeric answerability and authentic query provenance |
| [FinRank](https://github.com/datanxt/FinRank) | Provider reports 1,185 records with curated negative passages | Retrieval negatives are not unanswerable questions. Exclude as a substitute for E2/E3; can inform retrieval robustness |

## Rejected substitutes

- [FinTextQA](https://github.com/AlexJJJChen/FinTextQA): official README says the textbook part cannot be open sourced. Code access does not establish complete dataset access.
- [Lamini earnings-calls-qa](https://github.com/lamini-ai/lamini-earnings-calls): large synthetic question-generation output, not observed analyst speech.
- [nsmofficial finrag-bench](https://github.com/nsmofficial/finrag-bench): checked full `questions.jsonl` is a single placeholder. Do not count its claimed 500 as public data.
- CFBenchmark/GBFR copied Chinese subsets: exact official subset provenance not resolved; not in primary list.
- Forum questions with unverifiable occupations: genuine investor text is not sufficient evidence of analyst identity.

## Search outcome

The expanded search supplies strong raw inputs, including two newly checked sources, CFQA and RealFin. It does **not** remove the need to construct MinBridge's original annotations. No discovered source has all of: 300 verified natural professional numerical questions, both answerable and naturally insufficient contexts, expert support-tier labels, alternate derivation checks, and minimal missing-data certificates. Missing annotations must be produced and audited; adding more superficially related datasets cannot establish that requirement.
