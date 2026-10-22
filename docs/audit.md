# Three-round audit

Date: 2026-10-22. These are three different audit passes by the same assistant, not three independent human or expert reviews.

## Round 1 Source and file integrity

- Checked official repositories, dataset cards and actual released files rather than relying on paper totals.
- Corrected FinanceReasoning license to CC BY 4.0 based on its official Hugging Face card. The former NC-SA statement belonged to Tongji FinReasoning, a distinct project.
- Corrected TAT-QA to 277 contexts / 1,663 questions / 699 arithmetic questions. All 699 have nonempty derivations; executable-program normalization is still required.
- Checked source IDs in FinanceReasoning: 795 CodeFinQA, 288 CodeTAT-QA and 908 native FinanceReasoning. They cannot be treated as independent corpora.
- Checked 660 GBFR negative records: entity/time/term changes, not deletion twins. Two FinanceReasoning rows have inconsistent top-level and nested negative-question strings.
- Replaced substring-based license gating: the earlier downloader skipped “No license declared” but missed “No repository license declared”. The new registry uses explicit status values.

## Round 2 Task fit and independence

- Applied every requirement in [requirements.md](requirements.md), separating source availability from completed annotations.
- Expanded search to CFQA, RealFin, FinRank and FinanceGym; reviewed them after discovery rather than admitting on title similarity.
- CFQA: downloaded all company and year partition files; each partition totals 10,311. Paper says 13,643. Company partition has 423 empty answers and 2,069 answers with the exact not-found phrase. The paper describes investor-forum queries plus company substitution, so rows cannot all count as original analyst queries. PDFs need separate resolution.
- RealFin: switched to paper-linked xnlp-lab official repository, which has Apache 2.0; downloaded and parsed 367 English / 175 Chinese CSV items. It covers exam-style missing premises, not document-grounded or non-finance generalization.
- FinRank's negative passages do not establish question unanswerability. FinanceGym's report/forecast task is not deterministic financial numeric identifiability. Both remain secondary search findings.
- FinDER provides 883 operation-tagged candidates, not 300 accepted numerical professional questions. It lacks independent answerability, support-tier and certificate annotations. The original release filtered out queries without filing evidence.
- Maintained explicit exclusions for generated QA, template-only datasets, placeholder releases and unclear transcript rights.

## Round 3 Reproducibility and release

- Reorganized the repository into `docs/`, `data/`, `scripts/`, and `audit/`; removed stale duplicate root documents and the faulty downloader.
- Added a standard-library audit script with explicit permission gates, CSV/JSON/JSONL/HF pagination, bounded retries, per-source failure reporting, nested question counts and SHA-256 metadata.
- Ran the registered-source access check. Thirteen licensed files passed initially; FinDER encountered a transient HTTP 502 and was retried separately. The separate FinDER retry passed with 5,703 rows, bringing confirmed-license sources to 14 passes. Four unknown-license entries were skipped as specified. Reports preserve the initial failure and successful retry with timestamps.
- Raw source data are Git-ignored. Public reports contain metadata only. The local MIT license covers original code/docs and does not relicense source datasets.
- Checked JSON validity, Python syntax, whitespace errors, document links, registry IDs, report counts and tracked-file scope before push.

## Release decision

The **source audit and clean registry** can be released. The **benchmark itself cannot be certified complete**: the 300 accepted professional numerical questions, natural insufficient contexts, intervention twins, support-tier lists, minimal certificates, human agreement and training traces remain open. Search located usable raw inputs, but no existing public dataset supplies those original MinBridge annotations. Replacing analyst questions with investor/template questions or interpreting a missing answer as structural impossibility would weaken the stated requirement.

Continue with a documented annotation/construction stage on FinDER and FinQA/TAT-QA/FinanceReasoning, keeping independent human review separate from this automated source audit. The remaining gap is annotation and validation, not an unverified claim that a larger download satisfies it.
