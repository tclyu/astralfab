title: Method
parent: Governance
labels: -
milestone: bootstrap
---
Doctrine: how work proceeds in this estate. Binds once accepted.

**Taxonomy.** The issue tree carries one dimension: domain of work. Names are single-concept containers; everything of a concept lives in its container. A name that carves a concept out of another ("documentation strategy" beside "documentation") is forbidden: it makes the remainder ambiguous. A child is split out only when its parent demonstrably hosts independent work streams, and the split is recorded in both bodies so the single source of truth moves atomically. Facets (repository, stage, authority) are label dimensions or body fields, each separately MECE; no label duplicates the tree's dimension.

**Envelopes, not archives.** An issue body is scope plus current decision. Substance — research, analysis, design, records — lives in files landed by pull request and linked from the owning issue. Deliberation happens in pull-request reviews against concrete files, not in comment threads.

**Worktrees.** The canonical clones are never worked in directly. One worktree per branch, named `agent/<issue>-<slug>`; the issue number in the branch name is the claim; one writer per worktree; the worktree is removed after its pull request merges.

**Staging.** Each worktree may hold a `.staging/` folder: git-ignored scratch that never ships. Files graduate into the repository only by explicit path in a reviewed pull request. `git add -A` is never used.

**Delegation.** Output-heavy execution is delegated to subagents with self-contained instruction packets carrying identity checks, exact commands, expected outputs, and stop rules; the orchestrator verifies results with read-only checks. Delegation cost is measured in `bootstrap/token-ledger.md`.
