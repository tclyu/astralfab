title: Repositories
parent: AstralFab
labels: -
milestone: bootstrap
---
Container for the configuration of the family's repositories. Children: one issue per repository (`astralfab`, `astralfab-artifacts`), each holding everything about that repository's configuration until bloat forces a split.

The configuration itself is code: `bootstrap/terraform/` (owned by `Scaffolding`) is the executable form, `bootstrap/estate.md` (owned by `Record`) the readable form. The issues in this container carry the decisions and their history — what was chosen, what had to transit a wrong value and why — not the values themselves; a value stated in two places would be a second source of truth.
