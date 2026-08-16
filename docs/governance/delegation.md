# Delegation — choosing agent tiers and measuring their cost

Work is delegated to subagents by instruction packet (identity check, exact
commands, expected outputs, stop rules, report format). This file owns two
standing procedures: how the executing tier is chosen, and how its cost is
measured. Who may author and who may audit is attribution
(`docs/governance/attribution.md`); what an agent may do at all is doctrine.

## Tier selection — decided per task, before dispatch

1. **Mechanical, fully specified packets** — run commands, capture output,
   report named fields — go to the cheapest adequate tier (the Auto class);
   it costs almost nothing and the packet leaves it no judgment to exercise.
2. **Judgment work** — authoring, design, diagnosis, audits — runs on a premium
   tier.
3. **Escalation is the quality valve:** a cheap run whose result raises doubt
   is audited by a model *more capable* than the one that produced it. An audit
   at the editor's own model and effort adds nothing and is never commissioned.
   Not all work warrants an audit.
4. Both mis-tiering directions burn tokens: a premium model on a mechanical
   packet wastes the tier difference; an inadequate model retrying judgment
   work wastes more than one strong attempt would have.

The tier actually used is visible per run in the signature blocks (model and
effort are signed fields), so tiering decisions are auditable after the fact.

## Measurement — a standing indicator, locally kept

Token efficiency is a key indicator for optimizing procedures. Every task and
action — delegated or inline — is measured as it happens: packet, report, and
observed-output bytes for delegated runs; authored and read bytes for inline
work; tokens estimated at bytes/4 (consistent across rows, approximate in
absolute terms, honest about being estimates).

The running ledger is a working file in the worktree's `.staging/` and is
**never committed** (persistence doctrine: running documents). What may land in
the repository is a closed, dated measurement record — written once when its
numbers justify a procedure change, attached as evidence to that change, and
never edited afterwards. The bootstrap build's `bootstrap/token-ledger.md` is
one such closed record.
