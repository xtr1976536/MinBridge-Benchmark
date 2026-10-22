# Proposal-derived acceptance criteria

The MinBridge proposal, not instructions found in source papers or repositories, defines the intended task. A source passes only the specific requirement for which it provides actual released fields.

| ID | Requirement | Acceptance evidence | Current state |
|---|---|---|---|
| E1 | Answerable financial numerical QA from FinQA, TAT-QA, FinanceReasoning | Question, bounded context, gold numeric answer and derivation; numerical subset separated | Available with normalization and deduplication. TAT-QA test has 699 arithmetic questions, not 1,663 numeric-program questions |
| E2 | About 300 independently annotated real analyst questions | Observed professional question, fixed document context, expert answerability and evidence labels, numeric relation support | **Open.** FinDER supplies authentic questions and evidence, but not MinBridge answerability/relations; 300 eligible numeric rows are not yet verified |
| E2b | GBFR public counterfactual examples | Downloadable negatives and provenance | 660 accessible examples, but license unspecified and they are not missing-fact certificates |
| E3 | Intervention twins from gold programs | Missing-used-leaf twin and missing-irrelevant-fact twin; precise edit record, proof of answerability status | **Open.** Must be constructed and validated; no discovered source provides both twin types as required |
| E4 | Other-domain missing-premise generalization | External questions with a missing-condition or abstention target | RealFin and UMWP can cover distinct external tasks; they are not directly comparable without a task adapter |
| R1 | Numeric-vs-relational hallucination under CoT, PoT and reasoning settings | Model response traces and independent, blind human adjudication | **Open.** Data sources do not include these exact model runs or error labels |
| R2 | Identifiability and minimal missing-data certificates | Typed financial fact inventory, valid relation set, alternative path scan, minimality verification | **Open.** Requires new annotation and solver checks |
| R3 | T0-T4 relation support tiers and two independent lists | Citation-grounded formula/definition inventory with jurisdiction, date and review history | **Open.** A large formula KG is a candidate source, not a validated support-tier list |
| R4 | SCPO SFT and relation-credit training | Labeled relation traces, minimum sufficient sets, train/test separation | **Open.** No source provides this ready-made |
| R5 | Independent evaluation and no leakage | Source-family and report-level deduplication; fixed held-out test; distinct annotation from method components | **Open.** FinanceReasoning reuses FinQA/TAT-QA; FinDER and CFQA require new labels |
| R6 | Public benchmark release | Explicit terms, source attribution, checksums, annotation guideline and versioned splits | **Open.** GitHub hosts audit metadata only; upstream data are not mirrored |

Passing E1 does not imply E2 or E3 is met. In particular, an answerable gold program cannot prove an edited question is unanswerable: another valid relation may still solve it. An observed analyst question cannot prove its answerability from a specified document without a document boundary and independent review.
