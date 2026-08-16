# Analysis/design convention v0 — provisional

**Authority:** the owner's acceptance of the pull request that lands this file. **Expiry:** superseded by a design standard evidenced by the estate's first real design acts, the way the documentation standard supersedes documentation convention v0. Files written under v0 are then re-graded, never erased. Envelope: the `Estate` issue.

This convention is deliberately minimal. It exists to break one loop: designing anything — the documentation standard v1, the research standard, the artifacts repository's role — needs a convention for analysis and design files, and writing that convention is itself a design act. The smallest provisional artifact with declared authority and declared expiry breaks the loop; this is it.

## What every analysis file must state

1. **Subject** — one sentence: what part of the estate this analysis describes, as of when.
2. **Facts with sources** — each fact verified against a named, re-findable source (a committed path, stated configuration data, a live surface read on a date). An unverifiable statement is a claim and is marked as one.
3. **Constraints** — what any design deriving from this analysis may not violate, each traced to a fact.
4. **Date** — analysis is a closed dated record: a later analysis supersedes by new file; nothing is edited into a different claim.

## What every design file must state

1. **Decision** — what is decided, in one sentence, before any justification.
2. **Derivation by reference** — the analysis files and research files this decision derives from, cited by path, never restated. Research remains research after citation; a design citing it does not promote it to policy.
3. **Options rejected** — each considered alternative with the one reason it lost. A design recording no rejected options is recording a conclusion, not a decision.
4. **Consequences** — what the decision commits the estate to, including the owner acts and follow-on envelopes it creates.
5. **Date and status** — decided, or proposed awaiting the owner. Supersession follows the same rule as analysis: new file, durable pointer, no rewriting history.

## Form

Both file kinds follow documentation convention v0's form rules (markdown, one file one subject, prose never hard-wrapped, provisional header naming this convention) and land by pull request citing their envelope. Analysis and design may live in one file only when one bounded decision needs both and they share a change cadence; the default is separate files, since analysis is reusable by later designs that reject this one's conclusions.
