title: astralfab
parent: Repositories
labels: repo:astralfab
milestone: bootstrap
---
Everything about the platform repository's configuration.

**Decided.** Public. Two protected branches from one root: `integration` (default, the working line — every change arrives by reviewed, squash-merged pull request) and `main` (frozen at the initial commit for this stage; never pushed). Squash is the only merge method. Issues on: this repository is the family's single tracker. Wiki, projects, discussions off. Protection is two rulesets — `protected-lines` (pull request required, one approving review, stale reviews dismissed, last push approved, threads resolved, no deletion, no force push, zero bypass) and `owner-merges-only` (updates restricted to the admin role, pull-request mode only) — so the automation account can author but never merge.

**Value flips recorded** (details in `bootstrap/operations.md`): default branch `main` → `integration` once the ref existed; protection absent → active after the ref write it would have forbidden; automation merge ability present → removed once the rulesets landed.
