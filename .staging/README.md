# `.staging/` — local scratch. Nothing here ships except this README.

Every file under `.staging/` except this README is git-ignored and must never be committed. A file leaves staging only by being written to its real repository path and landed through a reviewed pull request into `integration`.

## Two roles

**Estate-local** (primary clone only): durable local material that must survive worktree deletion — issue-update drafts, superseded content in `retired/`, the local token ledger, seed packets, and similar. Agents write these only into the primary clone's `.staging/`, never into a worktree's.

**Task scratch** (each worktree): throwaway packets, notes, and tool outputs for that worktree's branch. It dies with the worktree. Do not keep estate drafts here.

## Rules

1. **Contents never ship.** Graduation is by explicit path into the repository via PR. Never `git add -A` or `git add .` for staging contents.
2. **Committed files never point here.** No committed file may cite a path under `.staging/`, a worktree path, or a machine path as something a reader could follow.
3. **If unsure:** put it in the primary clone's `.staging/` when it must outlive a worktree; otherwise keep it in the current worktree's `.staging/`.
