# Analysis/design convention v0 — provisional

**Authority:** the owner's acceptance of the pull request that lands this file. **Expiry:** superseded by a design standard evidenced by the estate's first real design acts, the way the documentation standard supersedes documentation convention v0. Files written under v0 are then re-graded, never erased. Envelope: the `Estate` issue.

This convention is deliberately small. It exists to break one loop: you cannot design the documentation standard v1, the research standard, or the artifacts repository's role without a convention for analysis and design files, and writing that convention is itself a design act. The smallest provisional artifact with declared authority and declared expiry breaks the loop. This is that artifact.

## What every analysis file must state

1. **Subject** — one sentence: which part of the estate this analysis describes, and as of when.
2. **Facts with sources** — each fact checked against a named source someone else can find again (a committed path, stated configuration data, or a live surface read on a date). A statement that cannot be checked is a claim, and is marked as one.
3. **Constraints** — what any design that builds on this analysis may not break, each one traced back to a fact.
4. **Date** — an analysis is a closed dated record. A later analysis supersedes it by landing a new file. Nothing is edited into a different claim.

## What every design file must state

1. **Decision** — what is decided, in one sentence, before any justification.
2. **Derivation by reference** — the analysis files and research files this decision comes from, cited by path, never copied out. Research stays research after you cite it. Citing it in a design does not turn it into policy.
3. **Options rejected** — each alternative that was considered, with the one reason it lost. A design that records no rejected options is recording a conclusion, not a decision.
4. **Consequences** — what the decision commits the estate to, including the owner acts and follow-on envelopes it creates.
5. **Date and status** — decided, or proposed and waiting on the owner. Supersession follows the same rule as analysis: new file, durable pointer, no rewriting history.

## Form

Both kinds of file follow documentation convention v0's form rules (markdown, one file one subject, prose never hard-wrapped, a provisional header that names this convention) and land by pull request citing their envelope. Analysis and design may share one file only when one bounded decision needs both and they change on the same cadence. The default is separate files, because analysis is reusable by later designs that reject this one's conclusions.
