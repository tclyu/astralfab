# Attribution — signature blocks for tracker and pull-request text

One account writes for many agents and models, so the account name carries no
authorship information. Authorship is therefore recorded in the work itself:
every agent-authored text ends with a signature block. This file owns the
format; audit *policy* (when an audit is warranted and at what model tier) is
economics and lives in `bootstrap/token-ledger.md`.

## The block

A horizontal rule, then fixed fields in this order:

```
---
Agent: Cursor
Model: claude-fable-5
Reasoning-Effort: <as the product exposes it, else "unreported">
Role: editor
Task-ID: <conversation or task identifier issued by the agent product>
Run-ID: <self-issued UUIDv4, one per execution>
Parent-Run-ID: <dispatching run's Run-ID; subagents only>
```

- **`Agent`** — the agent product: `Cursor`, `Codex`, `Claude Code`, or the
  product's own name. Never a model name.
- **`Model`** — the model slug exactly as the product names it.
- **`Reasoning-Effort`** — the effort level exactly as the product exposes it;
  `unreported` only when the session genuinely cannot see its own setting.
- **`Role`** — `editor` (authored the work) or `auditor` (reviewed it with a
  more capable model). Exactly one value.
- **`Task-ID`** — the conversation or task identifier issued by the agent
  product; stable across one conversation.
- **`Run-ID`** — self-issued UUIDv4, one per execution. A subagent is its own
  run. A conversation that changes model keeps its lineage visible because the
  run, not the model, is the unit.
- **`Parent-Run-ID`** — present only on subagent blocks: the dispatching run.

All fields are stated truthfully or `unreported`; a fabricated field is an
identity violation, not a formatting error. A value someone merely told the
session is a claim, not a detection: before writing `unreported`, the session
checks whether its product records its own configuration somewhere readable
(model slug, effort, task identifier) and signs with what it finds there.

## Coverage

Every agent-authored **issue body, issue comment, pull-request body, and
pull-request review comment** ends with exactly one signature block (a
pull-request body may carry several — see aggregation). Unsigned agent text is
a defect to fix by re-signing, not deleting. The owner's human posts are
exempt: the owner account identifies itself.

## Editor and auditor

The editor's block sits on the work. An audit, when one happens, appends the
auditor's block (`Role: auditor`) beneath the editor's on the same text. The
absence of an auditor block is itself a record: no audit was performed. An
audit by the editor's own model at the same effort is pointless and is never
recorded as an audit.

## Aggregation on pull requests

A pull-request body carries one block per **contributing run** — a run whose
authored bytes are in the deliverable — in order of first contribution, keyed
by `Run-ID`. Two subagents dispatched from one conversation share `Agent`,
`Model`, and `Task-ID` yet are two contributors; only the run tells them apart.

Squash merges use the pull-request body as the commit message
(`squash_merge_commit_message = PR_BODY`), so the blocks land in protected
history automatically. One mechanism covers tracker and history; there is no
separate commit-trailer scheme to drift from it. Branch commits need no blocks
— they die with the branch on merge.
