title: Identity
parent: Governance
labels: -
milestone: bootstrap
---
Doctrine: which account performs which act, and how that is proven. Binds once
accepted.

**Two accounts.** `tclyu` (owner, admin) performs owner-walled acts: acceptance,
approvals, merges, settings, applies. `tclyu-automation` (write) performs every
agent write: branches, pull requests, issues, comments. All agents on all
machines share the one automation identity; no agent ever writes as the owner.

**Prove before writing.** Immediately before every mutation batch, the acting
session verifies its login (`gh api user`) and stops on any mismatch. A write
and its read-back are one unit: a mutation is not done until it has been read
back and matches.

**Credentials by name.** Tokens are fetched per account by name
(`gh auth token -u <login>`). `gh auth switch` is forbidden: it mutates a shared
active-account file that every concurrent process on the machine reads.

**Never blind-retry.** A write whose outcome is unknown (timeout, ambiguous
error) is never repeated blind. Discover first — list by title, check state —
and re-create only what is provably absent.

**Single lane.** Mutations are serialized per surface; parallel agents work only
on disjoint issues and disjoint worktrees.
