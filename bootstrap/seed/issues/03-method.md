title: Method
parent: Governance
labels: -
milestone: bootstrap
---
Doctrine: how work proceeds in this estate. Binds once accepted.

**Taxonomy.** The issue tree carries one dimension: domain of work. Names are single-concept containers; everything of a concept lives in its container. A name that carves a concept out of another ("documentation strategy" beside "documentation") is forbidden: it makes the remainder ambiguous. A child is split out only when its parent demonstrably hosts independent work streams, and the split is recorded in both bodies so the single source of truth moves atomically. Facets (repository, stage, authority) are label dimensions or body fields, each separately MECE; no label duplicates the tree's dimension.

**Envelopes, not archives.** An issue body is scope plus current decision. Substance — research, analysis, design, records — lives in files landed by pull request and linked from the owning issue. Deliberation happens in pull-request reviews against concrete files, not in comment threads.

**Worktrees.** The canonical clones are never worked in directly. One worktree per branch, named `agent/<issue>-<slug>`; the issue number in the branch name is the claim; one writer per worktree; the worktree is removed after its pull request merges.

**Merging.** A pull request merges only when a concrete act relies on it — a later change that must build on its files, a worktree that needs its law committed, a landing that cites its convention. Nothing merges to keep a queue tidy; an open, approved pull request parked until something depends on it is the normal state, not a backlog. When a dependent act arrives, the chain it relies on merges in dependency order and no further.

**Staging.** Each worktree may hold a `.staging/` folder: git-ignored scratch that never ships. Files graduate into the repository only by explicit path in a reviewed pull request. `git add -A` is never used.

**Persistence boundary.** A committed file contains timeless statements and closed dated records only: live facts are looked up on their surface, derived facts are derived from their source, running documents stay in staging, and ephemeral locations are never cited as followable. The test and the four classes: `docs/governance/persistence.md` (ephemeral pointers also in staging law, rule 5).

**Delegation.** Output-heavy execution is delegated to subagents with self-contained instruction packets carrying identity checks, exact commands, expected outputs, and stop rules; the orchestrator verifies results with read-only checks. Tier selection and cost measurement follow `docs/governance/delegation.md`: cheapest adequate tier for mechanical packets, premium tiers for judgment, stronger-model-only audits, running ledgers local and never committed, closed dated measurement records landing only as evidence for procedure changes.

**Attribution.** All agents share one account, so authorship is recorded in the work: every agent-authored issue body, issue comment, pull-request body, and pull-request review comment ends with a signature block (agent product, model, reasoning effort, role, task, run), per `docs/governance/attribution.md`. An audit adds the auditor's block; absence of one means no audit was performed.
