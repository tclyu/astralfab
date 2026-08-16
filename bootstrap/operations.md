# Operations — how the estate was reached, as a reusable sequence

Not a diary. Each operation states actor, channel, and — where a value had to transit a wrong state (chicken-and-egg) — the transitional value, the final value, and the flip condition. A scaffolding implementation replays the final-state operations and only needs the transitional notes where its target also pre-exists.

## Bootstrap window

Open from repository creation; closed when the owner accepts the three doctrine bodies (`Method`, `Authorization`, `Identity`). Acts inside the window (ungoverned by definition, enumerated here so an auditor reads design, not defect):

- W1. Repositories created by owner with auto-init (outside Terraform; adopted later by import blocks). A fresh scaffold creates them in-module instead.
- W2. Working branch `agent/bootstrap` carries no issue number — the tracker did not exist yet. All later branches are `agent/<issue>-<slug>`.
- W3. Staging law (`.gitignore` + `.staging/README.md`) authored and used before it landed; effective locally as untracked files until merged.
- W4. Seed templates and scripts run from `.staging/` before the repository could host them; landed bytes asserted identical to the bytes that ran.
- W5. The three doctrine bodies are created and filled before any doctrine exists to govern those writes; their acceptance is the act that closes this window.
- W6. The three acceptance comments were posted by an agent under the owner's explicit, recorded authorization ("overrides the no-agent-acceptance rule this once"), with the owner credential, identity-verified, read back under the automation credential. Outside the window this is forbidden by Authorization.

## Value flips (set one value, then change it)

| setting | transitional value | final value | flip condition |
| --- | --- | --- | --- |
| `default_branch` | `main` (at creation) | `integration` | the `integration` ref exists |
| branch protection | absent | two active rulesets | `integration` exists; must precede first content PR so all content passes the gate |
| automation merge ability | present (implicit in `write`) | removed (`owner-merges-only` ruleset) | rulesets active; `write` itself is retained for branches and PRs |
| repo lifecycle | created by hand | managed by Terraform | import blocks adopt them at first plan |
| documentation authority | convention v0 (provisional) | standard v1 | v1 designed from research lands; v0 re-graded, not erased |
| governance | bootstrap window open | closed | owner accepts the three doctrine bodies |

## Operations log (final working form; failed attempts omitted, deviations noted)

Worktree, branch, and staging names below are historical facts about ephemeral space: nothing in this record resolves to them, and none of them survives its pull request. Committed files must never depend on such locations (staging law, rule 5).

| # | operation | actor | channel |
| --- | --- | --- | --- |
| 1 | Create repos (auto-init, public) | tclyu | GitHub UI (pre-existing; W1) |
| 2 | Invite + accept automation collaborator (`write`) | tclyu, then tclyu-automation | gh api (pre-existing) |
| 3 | Worktree `agent/bootstrap` off canonical clone | Cursor agent | git (W2) |
| 4 | Author staging law + record skeletons | Cursor agent | files in worktree (W3) |
| 5 | Author Terraform module `bootstrap/terraform/` | Cursor agent | files in worktree |
| 6 | `terraform plan` (read-only) | subagent, automation token | terraform |
| 7 | `terraform apply` — settings, integration branch, default flip, rulesets, labels, milestone | subagent, **tclyu token, owner-authorized** | terraform |
| 8 | Verify: plan-zero, gh read-backs, negative push test | Cursor agent + subagent | terraform, gh, git |
| 9 | Seed the tracker from the templates + sub-issue wiring (title-checked, read-back) | subagent, automation token | gh api (W4) |
| 10 | Emit acceptance queue (SHA-256 over exact UTF-8 body bytes) | Cursor agent | files in worktree |
| 11 | Accept `Method`, `Authorization`, `Identity` | **tclyu (owner decision; posting delegated under W6)** | gh (closed the window 2026-08-16) |
| 12 | PR lane: Record, Scaffolding, Documentation v0 | automation authors; **tclyu approves + squash-merges (human act)** | gh |

## Discovered constraints (facts a re-implementation must know)

- **Ruleset bypass actors are invisible to non-admin readers.** The API returns `bypass_actors: null` to a write-role credential, so a Terraform drift check under the automation credential reports phantom drift on every ruleset that has bypass actors. Truthful drift checks run under the owner credential. (Measured 2026-08-16 after first apply; plan-zero under the owner-written state confirmed the live value `RepositoryRole 5, pull_request` exists.)
- **Negative probe result (2026-08-16):** an empty-commit push to `integration` as the automation account was rejected with both expected violations — "Cannot update this protected ref" (owner-merges-only) and "Changes must be made through a pull request" (protected-lines). The probe commit was reset away; nothing landed.
- **Apply result (2026-08-16):** `Apply complete! Resources: 2 imported, 11 added, 2 changed, 0 destroyed.` — exactly the reviewed plan.
- **Seed result (2026-08-16):** the tracker was seeded from the templates in `bootstrap/seed/issues/`, in template order; the sub-issue tree was wired and every body verified by read-back against its template's exact bytes. Counts and titles live in the template set, not here.

## Irreducible human acts (a scaffold must stop for these)

1. Account creation and collaborator invitation acceptance (two-party act).
2. Authorizing `terraform apply` (admin credential).
3. Accepting doctrine bodies (the decision is the artifact).
4. Approving and merging every pull request (self-approval forbidden; agents may not merge by ruleset).
