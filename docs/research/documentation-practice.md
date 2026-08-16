# Research: documentation practice

**Status:** provisional, written under documentation convention v0 (`docs/documentation/convention-v0.md`). To be re-graded under the documentation standard v1 that is designed from it, never erased. Envelope: the `Documentation` issue.

## The question

What practices should govern how this estate writes and maintains documentation, so that the documentation standard v1 can be designed from evidence rather than taste?

## Where this comes from

1. **This estate's committed files** — `docs/governance/persistence.md`, `docs/governance/attribution.md`, `docs/governance/delegation.md`, `docs/documentation/convention-v0.md`, `.staging/README.md`, `bootstrap/estate.md`, `bootstrap/operations.md`. Re-findable at those paths on the `integration` line.
2. **This estate's own bootstrap build** — measured events of 2026-08-16/17, recorded in `bootstrap/operations.md` and `bootstrap/token-ledger.md`.
3. **Diátaxis** — https://diataxis.fr/ (start-here and foundations pages), verified reachable and as characterized on 2026-08-17.
4. **Write the Docs, "Docs as Code"** — https://www.writethedocs.org/guide/docs-as-code/, verified reachable and as characterized on 2026-08-17.
5. **markdownlint** — https://github.com/DavidAnson/markdownlint (rule catalog in `doc/Rules.md`), verified reachable and as characterized on 2026-08-17.
6. **Google developer documentation style guide** — https://developers.google.com/style (highlights, tone, person, and voice pages), verified reachable and as characterized on 2026-08-17.
7. **The YAML "Norway problem"** — https://hitchdev.com/strictyaml/why/implicit-typing-removed/ and https://www.bram.us/2022/01/11/yaml-the-norway-problem/, verified reachable and as characterized on 2026-08-17.
8. **GitHub Docs content model** — https://docs.github.com/en/contributing/style-guide-and-content-model (about-the-content-model and about-combining-multiple-content-types pages), verified reachable and as characterized on 2026-08-17.
9. **DITA 1.3 information typing** — https://docs.oasis-open.org/dita/dita/v1.3/errata01/csprd01/complete/part1-base/archSpec/base/information-typing.html and the technical-content document types, verified reachable and as characterized on 2026-08-17.

## What was verified

I checked each point below against the named source. These are observations, not recommendations.

### What this estate already does

- Committed content already falls into four persistence classes: timeless statements, closed dated records, live facts, and derived facts. The last two are forbidden in committed files. That is in `persistence.md`. Any documentation rule has to live with this. A document in the repository is either timeless or a closed record. Anything else belongs on a live surface or in staging.
- Hard wrapping was measured as pure cost here. Thirteen prose files were unwrapped. Roughly 250 line breaks came out. The word sequence was unchanged. The wrapping carried no information. That measurement is in the bootstrap record. The formatting rule now in convention v0 closed the waste.
- The working model is substance in files and thin envelopes. Issues authorize and link. Files carry content. Pull requests carry the why. That is in `estate.md`, in the Tracker and Repository-content sections. The prior estate this family replaced accumulated megabytes of substance inside issue comments. The bootstrap record states that this model exists to prevent that.
- Byte-level assertion works and is cheap. Seeded issue bodies were checked against template bytes. Doctrine acceptance binds to a sha256 digest of the exact body. Both are in the bootstrap record. Exactness of documentation content can be enforced by script, not by care.
- Authorship cannot be inferred from the writing account here. It is recorded in the work itself, in signature blocks. That is in `attribution.md`. Documentation authorship rules have to build on that convention rather than invent a parallel one.
- This estate already satisfies the first two docs-as-code gates by construction: plain-text markup in version control, and pull-request review. It has no automated documentation checks yet. The gap is in the bootstrap record.

### What the outside sources say

- Write the Docs defines docs as code as writing documentation with the same tools and gates as code: plain-text markup in version control, pull-request review, and automated checks in CI.
- Diátaxis names four kinds of documentation: tutorials, how-to guides, reference, and explanation. The split is whether the reader is studying or working, and whether they need action or cognition. It holds that one document serving two kinds serves neither.
- markdownlint is an off-the-shelf linter with named, individually configurable rules for markdown structure. Among others it enforces a single H1 (MD025), no skipped heading levels (MD001), one unordered-list marker (MD004), blank lines around lists (MD032), and consistent code-block style (MD046). Formatting discipline is therefore enforceable without building anything.
- Google's developer documentation style guide states, as its own rules: second person, active voice, sentence-case headings, serial commas, conditions before instructions, and imperative mood for instructions. It also asks for a conversational, friendly tone throughout.
- YAML 1.1 implicit typing silently coerces unquoted scalars. `NO` becomes false. Version numbers ending in zero become floats. Date-like values become timestamps. YAML 1.2 removed most of this. Widely used parsers still apply 1.1-style behavior. The documented practical rule is defensive quoting of dates, versions, and URLs, plus safe loading in any tooling.
- GitHub's published content model uses more article types than Diátaxis's four. It says its types evolve as needs change. It permits combining conceptual, procedural, referential, and troubleshooting sections in one article when a complex task needs them together. It prefers one canonical home plus links over reusing large sections across articles.
- DITA information typing distinguishes concept ("what is"), task ("how do I"), and reference (factual lookup) topics. It defines new types by specialization of a base topic rather than a fixed list. It names the mixing of information types within one topic as a reader-focus failure.

## What I believe or infer

The rest is believed or inferred. I say how sure I am, and why, on each point.

### Say each fact once

- The same rule this estate already uses for configuration should apply to documentation: a value lives in one place, and everything else points at it. Every fact should be stated in exactly one document and referenced elsewhere by path. I am sure of this. We already paid for breaking it. Protection values restated in two files drifted apart and had to be trimmed back to a pointer. That reading comes from the bootstrap record.
- Decisions need exactly one home. Doctrine files and research files already carry a decision's status, context, reasoning, and consequences. A parallel decision-record system, such as an ADR directory, would state the same decisions twice and break the single-statement rule above. I am sure of this, for that reason.
- The derivation pipeline should reference, never copy. Generic research feeds local analysis. Analysis feeds decisions and design. Design feeds specification and implementation. Each stage cites upstream. None absorbs it. Research remains research after a consumer uses it. Converting it into policy because someone cited it is a category error. This is the single-statement rule extended along the pipeline. I am sure of this, for the same reason we already paid for restated facts.
- MECE and single-source-of-truth are diagnostics, not folder rules. Forcing naturally overlapping subjects under one exclusive parent is a misapplication. So is stripping context readers need in the name of single statement. They hold where this estate already applies them: one hierarchy dimension, and one owner per maintained fact. I am fairly sure of this. It matches how the estate already behaves, but it is still an inference about how far those diagnostics should travel.

### Dates and decay

- Undated, unowned documents decay silently. The reader cannot tell current from stale. Convention v0's date requirement generalizes: every document should carry the date it was last known true. Reading a document older than the thing it describes should be treated as a signal, not as background noise. I am sure of this. Without a date, this repo has no way to tell a live page from a leftover.
- Staleness expectations depend on what a document describes. Text about a fast-moving tool decays in months. Text about a stable standard holds for years. A single freshness threshold misfits both directions. The date requirement becomes more useful when read against the described subject's rate of change. I am only moderately sure of this. It is reasoned, not watched against staleness in this corpus.
- A document should name its invalidation triggers — which source, code, release, or estate change makes it stale — rather than rely on a date alone. Dates triage. Triggers detect. Rate of change is not metadata to estimate. It is a dependency to declare. I am fairly sure of this. It sharpens the point above, but we have not yet seen a document go stale here.

### What a script can enforce

- Structure a script can check will be checked. Structure that only a careful reader can check will drift. The wrap measurement and the byte-level assertions are both instances. The standard should prefer machine-checkable requirements — required header fields, unwrapped prose, resolvable repo-relative paths — over stylistic guidance. I am sure of this. This repo already learned it twice.
- The formatting rules worth having are the lintable ones: one H1, no skipped heading levels, one unordered-list marker, blank lines around block elements, and fenced code with a language tag. markdownlint can check all of these. Depth beyond three heading levels signals a file that should split rather than a rule that should bend. That matches this estate's split-on-bloat principle. I am sure of this. The checker already exists, and this estate already splits files that bloat.
- A normative vocabulary with fixed meaning — must, should, and may — removes a real class of ambiguity in standards documents. Adopting it costs one definitional paragraph. I am only moderately sure of this. It is ordinary standards practice, not something measured here.
- Validation layers should be ordered by cost: syntax and format linting first, structural schema checks second, human content review last. Each layer should be automated only when scale justifies it. Building schema validation before any tooling consumes the schema is machinery without a user. I am only moderately sure of this. It is cost-ordering, not a measurement from this corpus.
- The machine-checkable header could be carried as YAML frontmatter instead of the current bold-prose header. That buys tool-readability. It costs the YAML coercion hazards, which are manageable with defensive quoting and safe loading. This is an open design option for v1, not a preference. I am only moderately sure, because the hazards are documented and the payoff is untried here.

### Voice

- For an agent-authored corpus, the mechanics of the verified style guide transfer intact: active voice, sentence case, serial commas, conditions before instructions, and imperative mood for instructions. Its conversational, second-person tone does not. Different models across sessions produce tonal drift unless voice is fixed. Research files describe systems rather than instruct a reader. An impersonal, consistent-neutral voice fits better. This adaptation is this estate's inference, not the style guide's position. The verified point above states the source faithfully. I am fairly sure of the adaptation. It rests on reasoning about multi-model authorship, not on evidence from this corpus.

### How documents are shaped

- A document starts from its reader and outcome — who reads it, in what situation, and what they should understand or be able to do afterward — not from a template. Diátaxis, GitHub's content model, and DITA all organize by reader need. A template chosen before the reader's job is known produces structure without service. I am sure of this. Three independent frameworks converge on that.
- Declaring a Diátaxis mode on every document would prevent the most common structural failure, which is one file trying to be two kinds. This estate's early corpus is almost entirely reference and explanation. A full four-mode taxonomy may be more machinery than the corpus warrants until tutorials or how-to content actually exist. I am only moderately sure either way. The corpus is too small to test the question.
- Role, subject, scope, lifecycle, and authority are separate dimensions of one artifact. Role is what job the artifact does. Subject is what it is about. Scope is where it applies. Lifecycle is how mature it is. Authority is what may rely on it. Conflating them into a single type list — putting "research" beside "authentication" as peers — breaks classification. The estate's tracker already separates hierarchy from facet labels on exactly this reasoning. Documents deserve the same treatment. I am sure of this, for that reason.
- A fact record and a research synthesis are different artifacts. A fact record is a bounded assertion with its observation context. A research synthesis is a comparison and interpretation of evidence. A separate fact record is warranted only when the assertion is reused independently, changes on its own cadence, or needs its own verification. Otherwise the fact is cited at its point of use. Splitting every sentence into an addressable record adds indirection without adding trust. I am fairly sure of this. The distinction is real; the "only when" test is reasoned, not measured.
- Combining content types in one document is right when one reader needs the parts in one journey, the sections' jobs are visibly distinct, and the parts share ownership and change cadence. Splitting is right when readers, cadences, or authorities differ. The defect is never "two types present." It is competing jobs in one place. I am fairly sure of this. It is how I read the two verified models together: one permits combining when a task needs it, the other treats mixed types inside one topic as a reader-focus failure.
- Correction, update, version, supersession, and deprecation are distinct acts with distinct reader promises. A change should declare which it is. Supersession preserves the old identity with a durable pointer. This estate already practices that — v0 files are re-graded, never erased — without yet naming the vocabulary. I am only moderately sure the five-way split is the right named set. The practice is verified; the names are inferred.

## What this means for documentation standard v1

These are design inputs, not decisions. The design act still has to weigh them.

1. Build document classes from the persistence classes we already have, not a new taxonomy. A committed document is timeless doctrine, a closed record, or it does not belong in the repository.
2. Require a small header a script can check: subject, status (provisional or standing), date, and governing convention. That extends convention v0's five requirements. Scripts already proved they can enforce exact bytes. Dates stop silent decay. Checkable structure holds; taste does not.
3. Keep the real content in files and keep issue envelopes thin. The standard should say, in one sentence each, what belongs in an issue body and what belongs in a document.
4. Make the single-statement rule and the no-hard-wrap rule into requirements. Both can be checked by script.
5. Record the option to declare a Diátaxis mode on each document. Do not build that taxonomy until the corpus grows past reference and explanation.
6. Use must, should, and may in the standard itself, and in every standard after it. Spend one paragraph defining them.
7. When a pull-request lane exists, add automated documentation checks to it: header present, prose unwrapped, repo-relative paths resolvable.
8. Adopt the lintable formatting set: one H1, no skipped heading levels, one list marker, blank lines around blocks, fenced code with a language tag. Enforce it with markdownlint the day those checks exist.
9. Take the style mechanics from the verified guide: active voice, sentence-case headings, serial commas, conditions before instructions, imperative mood for instructions. Decide the tone on purpose. Either keep the guide's conversational second person, or adopt the impersonal consistent voice argued above.
10. Choose how the header is carried: bold prose as now, or YAML frontmatter with defensive quoting and safe loading. Do not build schema validation until some tool actually consumes the schema.
11. Give decisions one home: doctrine files and research files. Do not add a parallel decision-record directory.
12. Read the date on a document against how fast its subject changes. Say that freshness expectations differ by what is described. Do not invent threshold tables before anyone has seen staleness here.
13. Open every document with its reader and outcome. One line naming who this serves and what they can do afterward, next to the subject line we already require.
14. Treat role, subject, scope, lifecycle, and authority as separate header facts, never as one mixed list. Use the same dimension vocabulary as the tracker's facet labels.
15. State the derivation pipeline as reference, not copy. The analysis and design convention under the `Estate` envelope is the first consumer. The documentation standard should cite that convention, not restate it.
16. Write down the combine-versus-split tests. Name the five change acts — correction, update, version, supersession, and deprecation — so every edit declares its promise to readers.
17. For documents that describe anything that changes outside the document, require named invalidation triggers next to the date.

## How sure this file is

Fairly sure overall, not certain. What this estate already does was verified against committed files and measured events, and I am sure of those observations. The external sources were verified as sources: they say what I say they say. Whether they fit an agent-operated, single-maintainer estate is inference. Each belief above carries its own confidence.

The weakest points are the Diátaxis-mode question, where the corpus is too small to test the taxonomy either way, and the tone stance, which deliberately departs from its verified source and rests on reasoning about multi-model authorship rather than on evidence from this corpus. The later beliefs about reader-first structure, classification dimensions, fact records, the derivation pipeline, combine-versus-split, MECE and single-statement as diagnostics, change acts, and invalidation triggers generalize from three verified frameworks that agree with one another. That agreement is real evidence. None of the three was built for a two-person, many-agent estate.

## When this was current

Current as of 2026-08-17. Written by the run whose signature block is on the landing pull request.
