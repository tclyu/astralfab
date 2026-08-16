# Analysis: estate facts and scenarios

**Status:** closed dated record, written under documentation convention v0 (`docs/documentation/convention-v0.md`) and the analysis/design convention v0 (`docs/estate/design-convention-v0.md`). A later analysis supersedes this one by new file; this one is never edited into a different claim. Envelope: the `Estate` issue.

## Subject

This note records the estate's facts, the situations it is built to serve, and the constraints later design has to respect, as of the date at the bottom. Design work should point back here instead of restating these things.

## Sources

1. **The estate's committed files** — governance doctrine under `docs/governance/`, conventions under `docs/documentation/` and `docs/estate/`, the record under `bootstrap/`, and protection and settings stated as data in `bootstrap/terraform/`. Those paths on the `integration` line are where to find them again.
2. **The live tracker** — the issue tree on the tracker repository, read on 2026-08-17.
3. **The bootstrap record** — `bootstrap/estate.md` and `bootstrap/operations.md`, the closed account of how the estate was built.

## Facts

Each fact below was checked against the source named on it, on the date at the bottom.

- **Two repositories, one owner.** `tclyu/astralfab` is the platform and the family's only tracker. `tclyu/astralfab-artifacts` has issues turned off and is otherwise set up the same way. Both are public. Both sit on a personal account, so organization-level roles and permissions are unavailable. Later permission design has to work with two accounts and repository rulesets, not org features (sources 1, 3).
- **Two accounts, many agents.** The owner account decides, merges, accepts, and applies configuration. One automation account does every agent write. Several agent products share that account on one machine. Authorship is therefore carried by signature blocks in the work, not by the login. You cannot tell agents apart from the GitHub login (source 1, `docs/governance/attribution.md`).
- **Protected line.** Every change to `integration` arrives by reviewed, squash-merged pull request. The automation account cannot merge or push protected refs. Only the owner can merge, and only through a pull request. The protection values live once, in `bootstrap/terraform/`. Agents write; the owner is the only merge gate (source 1).
- **Conventions in force.** Persistence classes govern what any committed file may contain. Delegation tiering governs how work is dispatched. Attribution governs how authorship is recorded. Documentation convention v0 governs research files for now. The analysis/design convention v0 governs analysis and design files for now. New files have to fit these rules rather than invent their own (source 1).
- **Working practice.** Development happens in a git worktree per task. Scratch lives in git-ignored `.staging/`, under a committed law. Running documents never land. Pull requests stay open until a concrete act relies on them. Parked work is the normal state, not a backlog to clear (sources 1, 3).
- **The tracker is thin by design.** There is one issue tree and one hierarchy dimension: domain of work. Substance lives in files. Issue bodies hold only scope and the current decision. Facets are labels. New subjects get issues when work begins, not before. The tracker is a map, not a document store (sources 1, 2).
- **Undesigned surface.** The artifacts repository's role — what it supplies, in what format, to whom — is a stated open design question. It was deliberately not decided at bootstrap. Later design under this envelope has to decide it; nothing here pretends it is already settled (sources 1, 2).
- **No automation in the lane.** There are no CI checks on pull requests. Every gate today is a human or agent act. A design that assumes automated checks has to land those checks first, or keep its gates as procedure (sources 1, 3).

## Scenarios

These are the situations this estate is built to serve. Each one is an observed pattern or a commitment, not a guess.

- **Multi-agent parallel authoring.** Several agent products (Codex, Cursor, Claude) work at the same time on one machine, against the same repositories. They stay isolated by worktrees and branch namespacing. They identify themselves with signature blocks. They coordinate through the tracker. Concurrency is normal here, so isolation and attribution are not optional.
- **Owner gating sessions.** The owner is the only merge and acceptance authority, and is not continuously present. Work therefore accumulates as parked, signed, self-contained acts (open pull requests, local drafts, acceptance queues) that a single owner sitting can dispatch in dependency order. Designs that need the owner online all the time will fail here.
- **The derivation pipeline.** Generic research lands first. Estate analysis states local facts. Design derives decisions from both by pointing at them. Deliverables (skills, code, release machinery) get envelopes under `Delivery` as design produces them. Research stays research; design does not turn it into policy by copying it out.
- **Scaffolding replay.** The estate's configuration exists as committed data (`bootstrap/terraform/`). Seeding is a committed tool (`bootstrap/seed/seed.py`) fed by a local template packet. Issue content is never committed. A future estate can be stood up by rerunning both. The record (`bootstrap/estate.md`, `bootstrap/operations.md`) is the readable form of the same intent. The bootstrap is meant to be replayed, not treated as a one-off.
- **Supply.** The artifacts repository will supply something to consumers. The scenario exists; its design does not, because the artifacts repository's role is still the open question above. Design under this envelope decides it.

## The chicken-egg census (closed facts of this build)

These are circular dependencies this build already hit, and the mechanism that broke each. The pattern comes back, so the breaks are worth keeping.

| Loop | Break |
| --- | --- |
| Research needs a documentation convention; the convention needs research | A deliberately small provisional convention (v0) with declared authority and declared expiry; research written under it supersedes it |
| Research about research needs an envelope defined by that research | Envelope drafted locally, then created and accepted in the same owner sitting that lands the research |
| Design needs a design convention; writing one is a design act | The same v0 pattern: a small provisional analysis/design convention, superseded by a standard evidenced by the first real design acts |
| Estate analysis needs the committed record as its fact base; the record lands by the same lane | Merge ordering inside one owner sitting: the record merges before the analysis lands |
| The attribution convention's own pull request needs a signature | The convention's pull request signs itself using the convention it lands |
| Editing an accepted doctrine invalidates its acceptance | Batch the edits, pair them with fresh digests, and re-accept in the same sitting |
| Permissions cannot be enforced before they exist | Apply configuration in value flips: permissive first, then tighten once the dependent structure exists |

The general form: break a loop with the smallest provisional artifact that has declared authority and declared expiry, then let the work it enables supersede it.

## Constraints on design

- **Personal-account GitHub.** There are no custom roles, no organization rulesets, and no environments. Protection is built from rulesets and the two accounts only. This follows from two repositories, one owner, and the protected line.
- **Persistence law.** No design may require a committed file to track a live surface. Live facts stay on their surfaces. Records close. This follows from the conventions in force.
- **Owner bandwidth.** Every design that adds owner acts must batch them into sittings. A design that needs the owner present all the time is wrong for this estate. This follows from owner gating sessions.
- **No CI yet.** Any design that relies on automated checks must include landing those checks. Until then its gates are procedural. This follows from there being no automation in the lane.

## Confidence

High for the facts and constraints: each was checked against committed files, stated configuration data, or the live tracker as of the date below. Medium for how the scenarios are framed: the first four are observed practice; supply is a commitment whose shape is still the open question. The census rows are closed facts of this build.

## Date

Facts and tracker state were verified on 2026-08-17. A later analysis supersedes this file; it is not updated in place.
