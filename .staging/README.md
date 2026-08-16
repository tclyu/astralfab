# `.staging/` — per-worktree scratch. Nothing in here ships.

This folder is the working space of the worktree it sits in. Every file in it except
this README is git-ignored (see the repository `.gitignore`) and must never be
committed.

Rules, for every agent and every session:

1. **Contents never ship.** A file leaves `.staging/` only by being written to its
   real repository path and landed through a reviewed pull request into
   `integration`. After it lands, delete the staging copy.
2. **Graduation is by explicit path.** Stage files for commit one path at a time.
   Never `git add -A`, never `git add .`.
3. **Per-worktree, not shared.** Each worktree has its own `.staging/`. Nothing
   outside a worktree may depend on this folder's contents — it dies with the
   worktree.
4. **What belongs here:** drafts before their destination exists, subagent
   instruction packets and raw outputs, Terraform plan/state files, working notes.
   If a file is worth keeping, give it a home in the repository through a pull
   request; if it is not, it stays here and dies here.
5. **Committed files never point here.** No committed file may cite a path under
   `.staging/`, a worktree-local path, a machine path, or any other
   non-persistent location as something a reader could follow. Recording
   self-contained facts *about* ephemeral process — digests, byte counts,
   outcomes, the name of a branch that once existed — is fine; a committed
   reference that only resolves inside someone's scratch space is a defect.
   (Naming this law file is allowed: it is committed.) The general law for what
   any committed file may contain is `docs/governance/persistence.md`.

If you are an agent and unsure whether a file belongs in `.staging/` or in the
repository: it belongs in `.staging/` until an issue envelope and a pull request
give it a home.
