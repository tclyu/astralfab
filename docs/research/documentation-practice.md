# Research: documentation practice

**Status:** provisional, written under documentation convention v0 (`docs/documentation/convention-v0.md`). To be re-graded under the documentation standard v1 that is designed from it, never erased. Envelope: the `Documentation` issue.

## Subject

What practices should govern how this estate writes and maintains documentation, so that the documentation standard v1 can be designed from evidence rather than taste?

## Sources

1. **This estate's committed files** — `docs/governance/persistence.md`, `docs/governance/attribution.md`, `docs/governance/delegation.md`, `docs/documentation/convention-v0.md`, `.staging/README.md`, `bootstrap/estate.md`, `bootstrap/operations.md`. Re-findable at those paths on the `integration` line.
2. **This estate's own bootstrap build** — measured events of 2026-08-16/17, recorded in `bootstrap/operations.md` and `bootstrap/token-ledger.md`.
3. **Diátaxis** — https://diataxis.fr/ (start-here and foundations pages), verified reachable and as characterized on 2026-08-17.
4. **Write the Docs, "Docs as Code"** — https://www.writethedocs.org/guide/docs-as-code/, verified reachable and as characterized on 2026-08-17.
5. **markdownlint** — https://github.com/DavidAnson/markdownlint (rule catalog in `doc/Rules.md`), verified reachable and as characterized on 2026-08-17.
6. **Google developer documentation style guide** — https://developers.google.com/style (highlights, tone, person, and voice pages), verified reachable and as characterized on 2026-08-17.
7. **The YAML "Norway problem"** — https://hitchdev.com/strictyaml/why/implicit-typing-removed/ and https://www.bram.us/2022/01/11/yaml-the-norway-problem/, verified reachable and as characterized on 2026-08-17.
8. **GitHub Docs content model** — https://docs.github.com/en/contributing/style-guide-and-content-model (about-the-content-model and about-combining-multiple-content-types pages), verified reachable and as characterized on 2026-08-17.
9. **DITA 1.3 information typing** — https://docs.oasis-open.org/dita/dita/v1.3/errata01/csprd01/complete/part1-base/archSpec/base/information-typing.html and the technical-content document types, verified reachable and as characterized on 2026-08-17.

## Findings — facts

Each verified against the named source.

- **F1.** This estate already classifies committed content into four persistence classes — timeless statements, closed dated records, live facts, derived facts — and forbids the last two in committed files (source 1, `persistence.md`). Any documentation rule must be compatible: a document is either timeless or a closed record, and anything else belongs on a live surface or in staging.
- **F2.** Hard wrapping was measured as pure cost in this estate: thirteen prose files were unwrapped with roughly 250 line breaks removed and the word sequence provably unchanged, meaning the wrapping carried zero information (source 2). The formatting rule now in convention v0 (source 1) closed this.
- **F3.** Substance-in-files, envelopes-thin is the estate's working model: issues authorize and link, files carry content, pull requests carry the why (source 1, `estate.md` Tracker and Repository-content sections). The prior estate this family replaced accumulated megabytes of substance inside issue comments, which is what this model was built to prevent (source 2, recorded motivation).
- **F4.** Byte-level assertion works and is cheap: seeded issue bodies were verified against template bytes, and doctrine acceptance binds to a sha256 digest of the exact body (source 2). Exactness of documentation content is enforceable by script, not by care.
- **F5.** Authorship cannot be inferred from the writing account here, so it is recorded in the work itself via signature blocks (source 1, `attribution.md`). Documentation authorship rules must build on that convention rather than invent a parallel one.
- **F6.** Diátaxis identifies four kinds of documentation — tutorials, how-to guides, reference, explanation — distinguished by whether the reader is studying or working and whether they need action or cognition, and holds that one document serving two kinds serves neither (source 3).
- **F7.** Docs-as-code is the practice of writing documentation with the same tools and gates as code: plain-text markup in version control, pull-request review, automated checks in CI (source 4). This estate already satisfies the first two by construction; it has no automated documentation checks yet (source 2).
- **F8.** An off-the-shelf linter with named, individually configurable rules exists for markdown structure: markdownlint enforces, among others, single-H1 (MD025), no skipped heading levels (MD001), one unordered-list marker (MD004), blank lines around lists (MD032), and consistent code-block style (MD046) (source 5). Formatting discipline is therefore enforceable without building anything.
- **F9.** Google's developer documentation style guide states, as its own rules: second person, active voice, sentence-case headings, serial commas, conditions before instructions, imperative mood for instructions — and a conversational, friendly tone throughout (source 6).
- **F10.** YAML 1.1 implicit typing silently coerces unquoted scalars — `NO` to false, version numbers ending in zero to floats, date-like values to timestamps — and although YAML 1.2 removed most of this, widely used parsers still apply 1.1-style behavior, so the documented practical rule is defensive quoting of dates, versions, and URLs, plus safe loading in any tooling (source 7).
- **F11.** GitHub's published content model uses more article types than Diátaxis's four, states that its types evolve as needs change, permits combining conceptual, procedural, referential, and troubleshooting sections in one article when a complex task needs them together, and prefers one canonical home plus links over reusing large sections across articles (source 8).
- **F12.** DITA information typing distinguishes concept ("what is"), task ("how do I"), and reference (factual lookup) topics, defines new types by specialization of a base topic rather than a fixed list, and names the mixing of information types within one topic as a reader-focus failure (source 9).

## Findings — claims

Believed or inferred; each carries its own confidence.

- **C1** (high). The single-source-of-truth discipline the estate applies to configuration (values live once, prose points) applies equally to documentation: every fact stated in exactly one document, referenced elsewhere by path. The estate has already paid for violations — restated protection values in two files drifted apart and had to be trimmed back to a pointer (inference from source 2).
- **C2** (high). Undated, unowned documents decay silently; the reader cannot distinguish current from stale. v0's date requirement generalizes: every document should carry the date it was last known true, and reading a document older than the thing it describes should be treated as a signal, not background noise.
- **C3** (medium). Declaring the Diátaxis mode per document would prevent the most common structural failure (mode-mixing, F6), but this estate's early corpus is almost entirely reference and explanation; a full four-mode taxonomy may be more machinery than the corpus warrants until tutorials or how-to content actually exist.
- **C4** (high). Structure that a script can check will be checked; structure that only a careful reader can check will drift. F2 and F4 are both instances. The standard should prefer machine-checkable requirements (required header fields, unwrapped prose, resolvable repo-relative paths) over stylistic guidance.
- **C5** (medium). Normative vocabulary with fixed meaning (must / should / may) removes a real class of ambiguity in standards documents; adopting it costs one definitional paragraph.
- **C6** (high). The formatting rules worth having are the lintable ones: one H1, no skipped heading levels, one unordered-list marker, blank lines around block elements, fenced code with a language tag (all F8-checkable). Depth beyond three heading levels signals a file that should split rather than a rule that should bend — consistent with the estate's split-on-bloat principle.
- **C7** (medium-high). For an agent-authored corpus, the mechanics of the verified style guide transfer intact (active voice, sentence case, serial commas, conditions before instructions, imperative for instructions) but its conversational, second-person tone does not: different models across sessions produce tonal drift unless voice is fixed, and research files describe systems rather than instruct a reader. An impersonal, consistent-neutral voice fits better. This adaptation is this estate's inference, not the source's position (F9 states the source faithfully).
- **C8** (high). Decisions need exactly one home. Doctrine files and research files already carry a decision's status, context, reasoning, and consequences; introducing a parallel decision-record system (an ADR directory or similar) would state the same decisions twice and violate the single-statement rule (C1).
- **C9** (medium). Staleness expectations depend on what a document describes: text about a fast-moving tool decays in months, text about a stable standard holds for years. A single freshness threshold misfits both directions; the date requirement (C2) becomes more useful when read against the described subject's rate of change.
- **C10** (medium). Validation layers order by cost: syntax and format linting first, structural schema checks second, human content review last — and each layer should be automated only when scale justifies it. Building schema validation before any tooling consumes the schema is machinery without a user.
- **C11** (medium). The machine-checkable header (implication 2) could be carried as YAML frontmatter instead of prose. That buys tool-readability and costs the YAML coercion hazards, which are manageable with defensive quoting and safe loading (F10). Recorded as an open v1 design option against the current bold-prose header, not a preference.
- **C12** (high). A document starts from its reader and outcome — who reads it, in what situation, and what they should understand or be able to do afterward — not from a template. Three independent frameworks converge on organizing by reader need (F6, F11, F12); a template chosen before the reader's job is known produces structure without service.
- **C13** (high). Role (what job the artifact does), subject (what it is about), scope (where it applies), lifecycle (how mature), and authority (what may rely on it) are separate dimensions of one artifact. Conflating them into a single type list — "research" beside "authentication" as peers — breaks classification. The estate's tracker already separates hierarchy from facet labels on exactly this reasoning; documents deserve the same treatment.
- **C14** (medium-high). A fact record and a research synthesis are different artifacts: a bounded assertion with its observation context, versus a comparison and interpretation of evidence. A separate fact record is warranted only when the assertion is reused independently, changes on its own cadence, or needs its own verification; otherwise the fact is cited at its point of use. Splitting every sentence into an addressable record adds indirection without adding trust.
- **C15** (high). The derivation pipeline references, never copies: generic research feeds local analysis, analysis feeds decisions and design, design feeds specification and implementation — each stage citing upstream, none absorbing it. Research remains research after a consumer uses it; converting it into policy because someone cited it is a category error. This is the estate's single-statement rule (C1) extended along the pipeline.
- **C16** (medium-high). Combining content types in one document is right when one reader needs the parts in one journey, the sections' jobs are visibly distinct, and the parts share ownership and change cadence; splitting is right when readers, cadences, or authorities differ (F11, F12). The defect is never "two types present" — it is competing jobs in one place.
- **C17** (medium-high). MECE and SSOT are diagnostics, not folder rules. Forcing naturally overlapping subjects under one exclusive parent, or stripping context readers need in the name of single statement, are both misapplications. They hold where the estate applies them: one hierarchy dimension, one owner per maintained fact.
- **C18** (medium). Correction, update, version, supersession, and deprecation are distinct acts with distinct reader promises, and a change should declare which it is. Supersession preserves the old identity with a durable pointer — the estate already practices this (v0 files re-graded, never erased) without yet naming the vocabulary.
- **C19** (medium-high). A document should name its invalidation triggers — which source, code, release, or estate change makes it stale — rather than rely on a date alone. Dates triage; triggers detect. This sharpens C9: rate-of-change is not metadata to estimate but a dependency to declare.

## Implications for the documentation standard v1

Inferred design inputs, not decisions; the design act weighs them.

1. Define document classes in terms of the existing persistence classes (F1), not a new taxonomy: a doc is timeless doctrine, a closed record, or it does not belong in the repository.
2. Require a minimal machine-checkable header — subject, status (provisional or standing), date, governing convention — extending v0's five requirements (F4, C2, C4).
3. Keep substance in files with thin envelopes (F3); the standard should say what belongs in an issue body versus a document, in one sentence each.
4. State the single-statement rule (C1) and the no-hard-wrap rule (F2) as requirements, both scriptable.
5. Declare the document's Diátaxis mode only if the corpus grows past reference-and-explanation (C3, F6); record the option, do not build it yet.
6. Adopt must/should/may (C5) for the standard itself and all future standards.
7. Add automated documentation checks to the pull-request lane when one exists (F7): header presence, wrap check, path resolvability.
8. Adopt the lintable formatting set — one H1, no skipped levels, one list marker, blanks around blocks, fenced code with language — enforceable via markdownlint the day checks exist (F8, C6).
9. Fix the style mechanics from the verified guide (active voice, sentence-case headings, serial commas, conditions before instructions, imperative for instructions) and decide the tone stance deliberately: the source's conversational second person, or the impersonal consistent voice argued in C7.
10. Choose the header carrier — prose as now, or YAML frontmatter with defensive quoting and safe loading (C11, F10) — and defer schema validation until tooling exists to consume it (C10).
11. Declare one home for decisions: doctrine and research files; no parallel decision-record directory (C8).
12. Read the date requirement against the subject's rate of change (C9): the standard should say that freshness expectations differ by what is described, without inventing threshold tables before staleness is ever observed.
13. Open every document with its reader and outcome (C12): one line naming who this serves and what they can do afterward, alongside the existing subject requirement.
14. Define the classification dimensions — role, subject, scope, lifecycle, authority — as separate header facts, never one mixed list (C13), using the same dimension vocabulary as the tracker's facet labels.
15. State the derivation pipeline with reference-not-copy semantics (C15); the analysis/design convention under the `Estate` envelope is its first consumer, and v1 should cite rather than restate it.
16. Give the combine-versus-split tests (C16) and name the five change acts — correction, update, version, supersession, deprecation (C18) — so every edit declares its promise to readers.
17. Require named invalidation triggers next to the date (C19) for documents describing anything that changes outside the document.

## Confidence

Medium-high overall: the estate-derived facts (F1–F5) are verified against files and measured events and are high-confidence; the external sources (F6–F12) are verified as sources but their fit to an agent-operated single-maintainer estate is inference; the claims are individually rated. The weakest areas are C3, where the corpus is too small to test the taxonomy question either way, and C7, which deliberately departs from its verified source and rests on reasoning about multi-model authorship rather than on evidence from this corpus. C12–C19 generalize from three verified frameworks that agree with one another; their convergence is real evidence, but none of the three was built for a two-person, many-agent estate.

## Date

Current as of 2026-08-17. Written by the run whose signature block is on the landing pull request.
