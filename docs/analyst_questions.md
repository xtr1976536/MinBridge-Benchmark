# Review of the planned 300 real analyst questions

## Strict inclusion rule

Every accepted row must retain evidence that a professional actually submitted or spoke the question, the original question text or a documented transformation, a fixed disclosure set, a deterministic numerical target or a precise insufficiency reason, and independently reviewed labels. A finance expert writing a benchmark question is a different provenance class. A retail investor is not automatically a professional analyst. A generated question over a real transcript is synthetic.

## Recommended source order

1. [FinDER](https://huggingface.co/datasets/Linq-AI-Research/FinDER) is the first pool. The [paper](https://arxiv.org/html/2504.15800v2) says questions were gathered from a service used by hedge-fund analysts, portfolio managers and investment-bank analysts, then evidence/answers were annotated. The public data has 5,703 unique question strings. Its operation labels yield 883 candidates: Compositional 440, Division 128, Multiplication 121, Subtract 111, Addition 75, Subtraction 8. Do not infer answerability from `reasoning`; it is a reasoning-needs flag. Samples include incorrect operation tags and explanatory questions.
2. [STRUX](https://huggingface.co/datasets/BUILDERlym/STRUX-Transcripts) preserves analyst names/positions in earnings-call Q&A. It can provide independently observed speech, but most utterances are not ready deterministic numeric tasks. Original call/source links, fixed context, speaker authenticity and transcript reuse rights need checking.
3. [EvasionBench](https://huggingface.co/datasets/FutureMa/EvasionBench) supplies call Q&A candidates. The downloadable 16.7k file has `eva4b_label`, not independent human MinBridge answerability. It lacks filing boundaries and numeric programs. The Capital IQ transcript source requires rights verification before copied text is republished.
4. [CFQA](https://github.com/ygan/CFQA) is an external investor-question pool, not an analyst replacement. Its paper describes company-name substitution and questions from a public investor forum. Its released company partition totals 10,311, not the paper's 13,643. Numeric reasoning rows need screening, and original-vs-template provenance is not labeled per row.

## Candidate handling

The 883 FinDER operation-type rows are a screening pool, not a final 300. Record `source_id`, question provenance class, question text hash, accepted context document IDs and dates, target metric/entity/period/unit, numeric answer, operand spans, allowed relations, answerability, declaration of assumptions, and annotator/adjudicator versions.

The original FinDER released questions were filtered for available 10-K evidence. Therefore they cannot, unchanged, substantiate natural unanswerable cases. If evidence is deleted, label the result **constructed intervention** and keep it separate from the independently observed question plus natural context. A chosen retrieval excerpt that omits a fact is not proof the full filing omits it.

Only count a row as accepted after numerical eligibility, context completeness and answerability have been independently checked. No 300-row accepted set is presently released by this repository. The audit did not employ human finance annotators, so it cannot truthfully claim human agreement or adjudication.

## External benchmark tasks

FinSearchComp 635, Vals public 50, BigFinanceBench public 50 and FinanceBench public 150 offer useful expert-authored tests. Keep their provenance distinct from observed queries, retain their own scoring schemes, avoid including their test items in SCPO training, and do not sum their published full sizes as available data.
