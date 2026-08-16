# AGENTS.md

This file is the single rulebook for agents in the astralfab family; anything `bootstrap/terraform/` already enforces is omitted.

## Family

```mermaid
flowchart LR
  family["astralfab family"] --> fab["astralfab — the tracker and everything else"]
  family --> art["astralfab-artifacts — holds what Estate design will decide"]
```

- An issue specific to one repository carries its `repo:` label; an unlabeled issue applies family-wide.

## Identity

- Codex, Cursor, and Claude Code write concurrently as `tclyu-automation`; each act as `tclyu` requires the owner's explicit permission.
- Operations no API supports: provide the owner exact steps to execute.
- Every issue and pull-request body ends with exactly one editor block, signed by the run responsible for its current state; an audit appends one auditor block beneath it. Nothing follows the block.

```text
---
Agent: Cursor                  the product name (Cursor, Codex, Claude Code), never a model
Model: claude-fable-5          the model slug exactly as the product reports it
Reasoning-Effort: xhigh        self-detected; "unreported" only if the product exposes no value
Role: editor                   "editor" or "auditor"
Task-ID: <conversation identifier issued by the product>
Run-ID: <self-issued UUIDv4, one per run>
Dispatched-By: <the dispatching run's Run-ID; subagents only>
```

## Truth

- State only current truth: replace incorrect content, never narrate the change; git and GitHub hold the history.
- Commit only durable content: no live facts, no machine paths, no tracker content. Everything else belongs in git-ignored `.staging/`, whose README states its purpose.
- Superseded content moves to `.staging/retired/` for future reuse.
- Legacy material supplies ideas only; never cite it.

## Documentation

- One paragraph per line.
- State nothing the reader can infer, unless practice shows the inference failing. Use plain language.
- Use an illustration wherever it conveys more than prose.

## Work

```mermaid
flowchart LR
  issue["Issue: scope + current decision"] --> tree["Own worktree under .worktrees/"] --> pr["One PR per purpose, into integration"] --> sitting["Owner sitting: batched approval and merge"]
```

- A record captures the final state and the operations that reproduce it, never a diary.
- Edit live tracker content only on the owner's instruction; hold pending edits as local drafts.
- When a mistake repeats, add the preventing rule to this file.

## Delegation

- An orchestrator dispatches parallel subagents and verifies their reports, consuming at most 5% of tokens; orders are self-contained and byte-exact where bytes matter.
- Subagents run on the highest Grok tier.
- Audit only when warranted, and only with a model stronger than the editor's.
- Record token usage per task in the local ledger.
