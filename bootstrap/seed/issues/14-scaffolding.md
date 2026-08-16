title: Scaffolding
parent: Delivery
labels: -
milestone: bootstrap
---
The reusable mechanism that builds a repository family like this one. Everything
mechanical lives here; everything that is a decision stays human and is named as
such.

**Contents, all landing under this envelope:**

- `bootstrap/terraform/` — the configuration as code: settings, working branch,
  default-branch choice, both protection rulesets, facet labels, milestone;
  parameterized by owner, automation login, and the repository map. A plan with
  zero changes is the standing drift check (owner credential required for a
  truthful one — bypass actors are invisible to non-admin readers).
- `bootstrap/seed/` — the issue templates and the seed script that files them:
  title-checked (never blind-created), hierarchy wired as sub-issues, bodies
  verified by read-back.
- `bootstrap/watch/` — the read-only digest watch: recomputes each body's
  SHA-256 so edits to accepted bodies are detected. Detection only; it reverts
  nothing.

**What it never automates:** account creation, invitation acceptance, apply
authorization, body acceptance, pull-request approval and merge. A scaffold that
performed these would be manufacturing decisions, not executing them.
