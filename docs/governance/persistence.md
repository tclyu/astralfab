# Persistence — what a committed file may contain

The test, applied to every line before it is committed: **will someone have to
edit this line because the world moved?** If yes, the line does not belong in a
committed file. A persistent file is maintenance-free by construction; a line
that needs periodic updating is a defect at the moment it is written, not when
it goes stale.

## The four classes of information

1. **Timeless statements** — decisions, rationale, law, structure, scope. The
   proper content of committed files. Commit freely.
2. **Closed records** — dated statements about completed events: "the apply on
   this date reported this result", "this measurement, taken on this date, read
   this value". True forever once true. Written once, never edited; superseded
   only by a newer dated record beside them.
3. **Live facts** — the current state of any mutable surface: issue numbers,
   counts, states; branch tips; settings values; lists of open pull requests.
   **Never written into a committed file.** Name the surface and how to query
   it; the surface is the source of truth.
4. **Derived facts** — anything computable from committed sources: the count of
   templates, the list of files a directory holds, an aggregate over a table.
   **Never restated.** Name the source; the reader derives. A restated
   derivation is a second source of truth, and every second source rots.

A restatement of another *committed* source (a readable summary of code, for
example) is tolerated only when both live in this repository, the summary names
its source, and the two change together in the same pull request. A restatement
of a *live* surface is never tolerated.

## Running documents

A document that grows as work proceeds — a tally, a log, a running ledger — is
never committed. It accumulates in the worktree's `.staging/` and dies there.
When its numbers justify a decision, what lands is a **closed record**: dated,
final, attached to the change it justifies, and never edited afterwards.

## Ephemeral references

Locations that die with a session — `.staging/` contents, worktrees, machine
paths, branch names of unmerged branches — follow the staging law (rule 5 of
`.staging/README.md`): they may be recorded as self-contained historical facts,
never cited as something a reader could follow.

## On repair

A violation found in a committed file is fixed by removing the offending
restatement and naming the source instead — not by updating the stale value,
which repairs one reading and re-arms the defect.
