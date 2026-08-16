# Research: research practice

**Status:** provisional, written under documentation convention v0 (`docs/documentation/convention-v0.md`). To be re-graded under the research standard designed from it, never erased. Envelope: the `Methodology` issue (child of `Research`).

## Subject

How should research be conducted and recorded in this estate, so that the research standard can be designed from evidence about what the estate's own first research runs actually required?

## Sources

1. **This estate's committed files** — `docs/documentation/convention-v0.md`, `docs/governance/persistence.md`, `docs/governance/delegation.md`, `bootstrap/operations.md`, `bootstrap/token-ledger.md`. Re-findable at those paths on the `integration` line.
2. **This estate's first research runs** — the writing of this file and of the documentation-practice research, 2026-08-17, both conducted under convention v0; the process itself is the primary evidence.
3. **The estate's bootstrap record** — the chicken-egg resolution and its measured outcome (source 1, `operations.md`).
4. **Diátaxis** — https://diataxis.fr/ (start-here and foundations pages), verified reachable and as characterized on 2026-08-17.
5. **Cochrane Handbook and MECIR standards** — https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current and the MECIR protocol-stage standards, verified reachable and as characterized on 2026-08-17.
6. **PRISMA 2020** — https://www.prisma-statement.org/prisma-2020-checklist, verified reachable and as characterized on 2026-08-17.
7. **Kitchenham and Charters, EBSE-2007-01** — https://ebse.webspace.durham.ac.uk/ebse-bibliography/guidelines-for-performing-systematic-literature-reviews-in-software-engineering/, verified reachable and as characterized on 2026-08-17.
8. **GRADE as applied in software engineering** — https://dl.acm.org/doi/10.1007/s10664-025-10728-9 (Empirical Software Engineering, 2025), verified reachable and as characterized on 2026-08-17.

## Findings — facts

Each verified against the named source.

- **F1.** A deliberately minimal convention with declared authority and declared expiry was sufficient to break the documentation–research circularity: v0 was written under bootstrap-window authority, and research became writable the moment it existed (sources 1, 3). No heavier method was needed to start.
- **F2.** The five v0 requirements — subject, sources, claim/fact separation, confidence, date — were each load-bearing in the first research runs: every section of both files exists because a requirement forced it, and no required section turned out to be filler (source 2).
- **F3.** The claim/fact separation is enforceable at the statement level and changes writing behavior: in the first runs it forced source verification that would not otherwise have happened — two external sources were checked live before citation specifically because unverified statements would have had to be marked as claims (source 2).
- **F4.** Research output is a closed dated record in the estate's persistence classes: once landed it states what was known as of its date, is superseded by new files, and is never edited into a different claim (source 1, `persistence.md`; v0's re-grade-never-erase matches).
- **F5.** Source re-findability is a binary the estate can test: v0 defines anything that cannot be re-found as a claim, not a source (source 1), and in the first runs this cleanly sorted inputs into estate files (paths), external documents (URLs, verified on a date), and inference (source 2).
- **F6.** Delegation economics apply to research: gathering is output-heavy and mechanical once the question is fixed, synthesis is judgment; the estate's tiering procedure (source 1, `delegation.md`) already distinguishes exactly these two shapes of work.
- **F7.** The mature evidence-synthesis discipline makes a published protocol with predefined, unambiguous eligibility criteria mandatory before the review begins, with searches motivated by the criteria — stated purpose: preventing post-hoc decisions influenced by the data found (source 5).
- **F8.** PRISMA 2020 is a 27-item reporting checklist whose stated aim is a transparent, complete account of why a review was done, what was done, and what was found — reporting is treated as a discipline separate from conducting (source 6).
- **F9.** Systematic-review methodology has been deliberately adapted from medicine to software engineering as a trustworthy, rigorous, auditable process in three phases — planning, conducting, reporting — demonstrating the method transfers across domains when adapted rather than copied (source 7).
- **F10.** In software-engineering reviews, GRADE-style certainty assessment is the most used approach but is usually misapplied as one generic grade for all findings, where the method itself calls for per-finding assessment (source 8) — external confirmation that per-claim confidence is the documented standard and file-level-only grading the documented failure.

## Findings — claims

Believed or inferred; each carries its own confidence.

- **C1** (high). The question must be fixed before gathering starts. Both first runs began from a one-sentence subject, and every source decision was made against it; research that starts from sources instead inherits the sources' scope. This is the single strongest candidate for a standard's first requirement.
- **C2** (high). Source classes deserve different verification duties: the estate's own files are checkable by reading, external documents need a reachability-and-characterization check on a date, and memory or inference must be labeled claim regardless of how confident it feels (generalization of F3, F5).
- **C3** (medium). Confidence should be stated per load-bearing claim, not only per file: a file-level grade hides the one weak claim a design decision might rest on. v0 already gestures at this; the standard should make it a requirement with a fixed vocabulary (high / medium / low plus one line of why).
- **C4** (medium-high). Negative results are results: a question investigated and closed as "no evidence" or "not worth the machinery yet" must be recorded, or the estate re-buys the investigation at full price. The first runs produced one such finding (the Diátaxis-mode question in the documentation research) and v0 had no place for it other than a rated claim.
- **C5** (medium). Gathering and synthesis should be visibly separated in the file — findings versus implications — so a reader can accept the evidence while rejecting the inference. Both first runs converged on this shape without being required to.
- **C6** (low-medium). Research files may eventually warrant a registry of recurring sources (canonical URLs, verification dates), but two files in, this is machinery without a corpus; recorded as an option, not a need.
- **C7** (medium). The section shape of a research file already maps onto Diátaxis's documentation modes (source 4): sources and findings carry reference and explanation, implications carry how-to guidance. If a mode taxonomy is ever wanted — the documentation-practice research left this open because the corpus is small — applying it at the section level of research files captures the benefit (no mode-mixing inside a section) without a document-typing regime, since the required section structure assigns modes for free.
- **C8** (medium-high). Research depth is a ladder — authoritative lookup, evidence scan, rapid review, systematic review, direct measurement, living review — and effort is calibrated to consequence and uncertainty. Calibrate up when a wrong answer is costly or hard to reverse, sources disagree, evidence is indirect or interested, or the conclusion is widely reused; calibrate down when the claim is low-consequence, stated by a stable authority, reversible, and independently checkable. Depth mismatch in either direction wastes something: rigor on a lookup wastes tokens, a lookup on a disputed effect wastes trust.
- **C9** (high). Fix the question, the eligibility of sources, and the stopping conditions before gathering starts, so inclusion rules cannot drift toward a preferred conclusion (F7 generalized). Proportional in this estate: for a lookup, one line each; for anything deeper, a short protocol note inside the research file — prospective constraint is the value, ceremony is not.
- **C10** (medium-high). Corroboration counts independent evidence paths, not URLs: several pages repeating one upstream source are one source. Verification duty for a load-bearing claim includes tracing it to its origin before counting agreement.
- **C11** (high). Reuse is by reference: a consumer cites the canonical synthesis (an exact revision when reproducibility matters), never copies it forward, and citation does not promote research into policy. Supersession produces a new file with a durable pointer to the old — matching the estate's persistence classes, where landed research is a closed dated record.

## Implications for the research standard

Inferred design inputs, not decisions; the design act weighs them.

1. Keep v0's five requirements verbatim as the core; they are all load-bearing (F2) and nothing observed argues for removal.
2. Add the question-first rule (C1): a research file opens with its question, and gathering that precedes the question is flagged as such.
3. Define the three source classes with their verification duties (C2, F5), and require the verification date for external sources.
4. Require per-claim confidence with fixed vocabulary for load-bearing claims (C3).
5. Give negative results a named place (C4) so closing a question is as recordable as answering one.
6. Require the findings/implications separation (C5) — evidence a reader can accept independently of the inference drawn from it.
7. State the lifecycle explicitly (F4): research lands as a closed dated record, supersession produces a new file, re-grading changes status metadata only.
8. Note delegation fit (F6): gathering may be delegated at the cheap tier once the question and source list are fixed; synthesis and confidence-rating stay with the tier that can be held to judgment.
9. If a documentation-mode taxonomy is ever adopted, apply it at the section level of research files (C7) — the findings/implications separation (C5) already assigns modes — rather than typing whole documents.
10. Define the depth ladder with its calibration triggers (C8) and require each research file to name the depth it claims, so a lookup is never dressed as a review nor a review billed as a lookup.
11. Require the protocol-before-search fields — question, source eligibility, stop conditions — stated in the file before gathering (C9), sized to the depth: one line each at lookup depth.
12. Count corroboration by independent evidence paths (C10): a load-bearing claim's verification traces to origins, and repeated downstream copies add zero.
13. State reuse-by-reference semantics (C11): consumers cite revisions, nothing copies research forward, and citation never converts research into policy.

## Confidence

Medium-high overall: the strongest findings are facts of the estate's own first research runs and are directly checkable (F1–F5); the main structural claims (C1, C2) are drawn from a sample of exactly two runs, which is real but thin evidence — though C1 and C9 now also carry the weight of the verified evidence-synthesis discipline (F7, F9), and C3's per-claim position gains external confirmation from F10. C6 is speculative and marked so; C7 cites a verified external framework but its section-level application is untested in this corpus; C8's ladder adapts a mature discipline's tiers to an estate that has only exercised the two cheapest rungs.

## Date

Current as of 2026-08-17. Written by the run whose signature block is on the landing pull request.
