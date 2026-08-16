# Scaffolding module — the family's configuration as code

This module is the executable form of the estate's repository configuration: settings, the working branch, the default-branch choice, both protection rulesets, the facet labels, and the bootstrap milestone, for every repository in the family. `bootstrap/estate.md` is the readable form; this is the one that runs.

## Usage

```sh
# Drift check (read-only, but see the caveat below):
GITHUB_TOKEN=$(gh auth token -u tclyu) terraform plan

# Converge (owner's admin credential; owner-authorized, every time):
GITHUB_TOKEN=$(gh auth token -u tclyu) terraform apply
```

A plan reporting zero changes is the standing proof that live state matches the record. State is disposable: the repositories are adopted by import blocks, so a deleted state file costs one re-import, not truth.

**Drift-check caveat (measured 2026-08-16):** GitHub returns `bypass_actors` as null to non-admin readers, so a plan run with the automation credential reports phantom drift on every ruleset that has bypass actors. A truthful drift check needs the owner credential; a plan under the automation credential is still safe (it writes nothing) but its ruleset rows are noise.

## Identity

- `terraform plan` is read-only under any credential, but only the owner credential sees the full ruleset truth (caveat above).
- `terraform apply` mutates owner-walled surfaces (settings, rulesets) and runs only with the owner's credential, only with the owner's explicit authorization.
- Fetch tokens by name (`gh auth token -u <login>`); never `gh auth switch` — the active-account file is shared by every concurrent process on the machine.

## What this module deliberately does not manage

- **Collaborators** — asserted in `checks.tf`, never written. Membership is a two-party act (grant by owner, acceptance by invitee) that no declarative tool can complete truthfully.
- **Issues, comments, pull requests** — living documents with their own writers. A declarative tool holding them would revert legitimate edits as "drift". The tracker is seeded once by `bootstrap/seed/seed.py` from a local template packet and evolves by governed acts.
- **Repository creation** — this family's repos pre-existed the module and were adopted by import (a recorded bootstrap exception). A fresh scaffold of a new family may create them in-module instead by dropping the import blocks.

## Scaffolding a new family

Set `owner`, `automation_login`, `tracker_repository`, and the `repositories` map in `terraform.tfvars`. Exactly one repository carries issues. The five acts no module can perform remain human: account creation, invitation acceptance, apply authorization, body acceptance, and pull-request approval and merge.
