# The estate — final state

Declarative: what exists once bootstrap completes. Nothing here is a step. The scaffolding module (`bootstrap/terraform/`) is the executable form of the configuration half; this file is the readable form and adds what Terraform cannot express (accounts, tracker, conventions).

## Accounts

| role | login | repository role | may |
| --- | --- | --- | --- |
| Owner | `tclyu` | `admin` on both repos | approve and merge pull requests (the only account that can), accept issue bodies, apply Terraform |
| Automation | `tclyu-automation` | `write` on both repos | every agent write: branches, pull requests, issues, comments. Never merges, never accepts |

One machine account, used by all agents (Codex, Cursor, Claude). Identity is verified (`gh api user`) before every mutation batch. Credentials are fetched by name (`gh auth token -u <login>`), never via `gh auth switch`.

## Attribution

The account name carries no authorship information — every agent writes as the one automation login — so authorship is recorded in the work itself: every agent-authored issue body, issue comment, pull-request body, and review comment ends with a signature block, and pull-request bodies aggregate one block per contributing run, which squash merges carry into protected history. Format and field vocabulary: `docs/governance/attribution.md`. Audit policy (when an audit is warranted, and at what model tier): `docs/governance/delegation.md`.

## Repositories

Two, both public, both owned by `tclyu`:

- **`tclyu/astralfab`** — the platform, and the family's single tracker (issues on here and nowhere else).
- **`tclyu/astralfab-artifacts`** — issues off; configured identically otherwise.

Branches on each: `integration` (default; the working line; every change arrives by squash-merged pull request) and `main` (frozen at the initial commit during this stage; never pushed).

## Protection and settings

The values live once, as data, in `bootstrap/terraform/`; this file restates none of them. The intent they implement: every change to a protected line arrives by reviewed, squash-merged pull request; the automation account can author branches and pull requests but can never merge or push a protected ref; only the owner can merge, and only through a pull request; the tracker repository is the only one in the family with issues enabled.

## Tracker

One tree on the tracker repository, one hierarchy dimension (domain of work), governed by the `Method` doctrine; owner acceptance of the three doctrine bodies is what closes a bootstrap window. The seeded containers and their bodies are the templates in `bootstrap/seed/issues/` — the template set is the source of truth for what bootstrap files, and the live tracker is the source of truth for what exists now (numbers, states, and everything filed since). Facet labels and the milestone are stated as data in `bootstrap/terraform/`; labels carry facet dimensions only (absence of a repo label means family-wide), and no label duplicates the hierarchy.

## Repository content

Structure, not inventory: the staging law lives at the repository root (`.gitignore`, `.staging/README.md`); `bootstrap/` holds the record and the scaffolding; `docs/` holds conventions and research. File lists are derived facts — git is the source of truth for what landed and when, the pull-request lane for why.
