# The estate — final state

Declarative: what exists once bootstrap completes. Nothing here is a step. The
scaffolding module (`bootstrap/terraform/`) is the executable form of the
configuration half; this file is the readable form and adds what Terraform cannot
express (accounts, tracker, conventions).

## Accounts

| role | login | repository role | may |
| --- | --- | --- | --- |
| Owner | `tclyu` | `admin` on both repos | approve and merge pull requests (the only account that can), accept issue bodies, apply Terraform |
| Automation | `tclyu-automation` | `write` on both repos | every agent write: branches, pull requests, issues, comments. Never merges, never accepts |

One machine account, used by all agents (Codex, Cursor, Claude). Identity is
verified (`gh api user`) before every mutation batch. Credentials are fetched by
name (`gh auth token -u <login>`), never via `gh auth switch`.

## Attribution

The account name carries no authorship information — every agent writes as the
one automation login — so authorship is recorded in the work itself: every
agent-authored issue body, issue comment, pull-request body, and review comment
ends with a signature block, and pull-request bodies aggregate one block per
contributing run, which squash merges carry into protected history. Format and
field vocabulary: `docs/governance/attribution.md`. Audit policy (when an audit
is warranted, and at what model tier): `bootstrap/token-ledger.md`.

## Repositories

Two, both public, both owned by `tclyu`:

- **`tclyu/astralfab`** — the platform, and the family's single tracker (issues on
  here and nowhere else).
- **`tclyu/astralfab-artifacts`** — issues off; configured identically otherwise.

Branches on each: `integration` (default; the working line; every change arrives by
squash-merged pull request) and `main` (frozen at the initial commit during this
stage; never pushed).

## Protection (both repos, identical; stated as data in `bootstrap/terraform/`)

- Ruleset `protected-lines` on `integration` + `main`, zero bypass actors:
  no deletion, no force-push, pull request required with 1 approving review,
  stale reviews dismissed on push, last push must be approved, review threads
  resolved, squash merge only.
- Ruleset `owner-merges-only` on the same refs: updates restricted; sole bypass
  actor is the repository `admin` role, pull-request mode only. Effect: only
  `tclyu` can merge, and only via pull request; `tclyu-automation` cannot merge or
  push protected refs at all.

## Repository settings (both repos)

Squash merge only (title `PR_TITLE`, message `PR_BODY`); head branches deleted on
merge; no auto-merge; update-branch button on; wiki, projects, discussions off;
issues on for astralfab, off for artifacts.

## Tracker

One tree on the tracker repository, one hierarchy dimension (domain of work),
governed by the `Method` doctrine; owner acceptance of the three doctrine
bodies is what closes a bootstrap window. The seeded containers and their
bodies are the templates in `bootstrap/seed/issues/` — the template set is the
source of truth for what bootstrap files, and the live tracker is the source of
truth for what exists now (numbers, states, and everything filed since). Facet
labels and the milestone are stated as data in `bootstrap/terraform/`; labels
carry facet dimensions only (absence of a repo label means family-wide), and no
label duplicates the hierarchy.

## Repository content

Structure, not inventory: the staging law lives at the repository root
(`.gitignore`, `.staging/README.md`); `bootstrap/` holds the record and the
scaffolding; `docs/` holds conventions and research. File lists are derived
facts — git is the source of truth for what landed and when, the pull-request
lane for why.
