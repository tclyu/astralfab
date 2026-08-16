# Analysis: estate facts and scenarios

**Status:** closed dated record, written under documentation convention v0 (`docs/documentation/convention-v0.md`) and the analysis/design convention v0 (`docs/estate/design-convention-v0.md`). A later analysis supersedes this one by new file; this one is never edited into a different claim. Envelope: the `Estate` issue.

## Subject

What are the facts, operating scenarios, and standing constraints of this estate as of the date below, stated so that design work can derive decisions from them by reference?

## Sources

1. **The estate's committed files** — governance doctrine under `docs/governance/`, conventions under `docs/documentation/` and `docs/estate/`, the record under `bootstrap/`, protection and settings stated as data in `bootstrap/terraform/`. Re-findable at those paths on the `integration` line.
2. **The live tracker** — the issue tree on the tracker repository, read 2026-08-17.
3. **The bootstrap record** — `bootstrap/estate.md` and `bootstrap/operations.md`, the closed account of how the estate was built.

## Facts

Each verified against the named source on the date below.

- **F1. Two repositories, one owner.** `tclyu/astralfab` (platform and the family's only tracker) and `tclyu/astralfab-artifacts` (issues off, otherwise configured identically); both public, both personal-account repositories, so organization-level roles and permissions are unavailable (sources 1, 3).
- **F2. Two accounts, many agents.** The owner account decides, merges, accepts, and applies configuration; one automation account performs every agent write, shared by multiple agent products on one machine. Authorship is therefore carried by signature blocks in the work, not by the login (source 1, `docs/governance/attribution.md`).
- **F3. Protected line.** Every change to `integration` arrives by reviewed, squash-merged pull request; the automation account cannot merge or push protected refs; only the owner can merge, and only through a pull request. Values live once in `bootstrap/terraform/` (source 1).
- **F4. Conventions in force.** Persistence classes govern what any committed file may contain; delegation tiering governs how work is dispatched; attribution governs how authorship is recorded; documentation convention v0 governs research files provisionally; the analysis/design convention v0 governs analysis and design files provisionally (source 1).
- **F5. Working practice.** Development happens in per-task git worktrees; scratch lives in git-ignored `.staging/` under a committed law; running documents never land; pull requests park open until a concrete act relies on them (sources 1, 3).
- **F6. The tracker is thin by design.** One tree, one hierarchy dimension (domain of work), substance in files, issue bodies holding only scope and current decision; facets are labels; new subjects get issues when work begins, not before (sources 1, 2).
- **F7. Undesigned surface.** The artifacts repository's role — what it supplies, in what format, to whom — is a stated open design question, deliberately not decided at bootstrap (sources 1, 2).
- **F8. No automation in the lane.** There are no CI checks on pull requests; every gate is currently a human or agent act (sources 1, 3).

## Scenarios

The situations this estate is built to serve; each is an observed or committed-to pattern, not speculation.

- **S1. Multi-agent parallel authoring.** Several agent products (Codex, Cursor, Claude) work concurrently on one machine against the same repositories, isolated by worktrees and branch namespacing, identified by signature blocks, coordinated by the tracker.
- **S2. Owner gating sessions.** The owner is the only merge and acceptance authority and is not continuously present; work therefore accumulates as parked, signed, self-contained acts (open pull requests, local drafts, acceptance queues) that a single owner sitting can dispatch in dependency order.
- **S3. The derivation pipeline.** Generic research lands first; estate analysis states local facts; design derives decisions from both by reference; deliverables (skills, code, release machinery) get envelopes under `Delivery` as design produces them.
- **S4. Scaffolding replay.** The estate's configuration and seeding exist as executable data (`bootstrap/terraform/`, `bootstrap/seed/`) so that a future estate can be stood up by rerunning them; the record (`bootstrap/estate.md`, `bootstrap/operations.md`) is the readable form of the same intent.
- **S5. Supply.** The artifacts repository will supply something to consumers — the scenario exists, its design does not (F7). Design under this envelope decides it.

## The chicken-egg census (closed facts of this build)

Circular dependencies met so far and the mechanism that broke each; recorded because the pattern recurs and the breaks are reusable.

| Loop | Break |
| --- | --- |
| Research needs a documentation convention; the convention needs research | Deliberately minimal provisional convention (v0) with declared authority and declared expiry; research written under it supersedes it |
| Research about research needs an envelope defined by that research | Envelope drafted locally, created and accepted in the same owner sitting that lands the research |
| Design needs a design convention; writing one is a design act | Same v0 pattern: minimal provisional analysis/design convention, superseded by a standard evidenced by the first real design acts |
| Estate analysis needs the committed record as fact base; the record lands by the same lane | Merge ordering inside one owner sitting: record merges before analysis lands |
| The attribution convention's own pull request needs a signature | The convention's PR signs itself per the convention it lands |
| Editing an accepted doctrine invalidates its acceptance | Batch edits paired with fresh digests and re-acceptance in the same sitting |
| Permissions cannot be enforced before they exist | Configuration applied in value flips: permissive first, tightened once the dependent structure exists |

The general form: break a loop with the smallest provisional artifact that has declared authority and declared expiry, then let the work it enables supersede it.

## Constraints on design

- **D1.** Personal-account GitHub: no custom roles, no organization rulesets, no environments — protection is built from rulesets and two accounts only (F1, F3).
- **D2.** Persistence law: no design may require a committed file to track a live surface; live facts stay on their surfaces, records close (F4).
- **D3.** Owner bandwidth: every design that adds owner acts must batch them into sittings (S2); a design demanding continuous owner presence is wrong for this estate.
- **D4.** No CI yet (F8): any design relying on automated checks must include landing them; until then its gates are procedural.

## Confidence

High for the facts and constraints: each is verified against committed files, stated configuration data, or the live tracker as of the date below. Medium for the scenario framing: S1–S4 are observed practice, S5 is a commitment whose shape is the open question. The census rows are closed facts of this build.

## Date

Facts and tracker state verified 2026-08-17. A later analysis supersedes this file; it is not updated in place.
