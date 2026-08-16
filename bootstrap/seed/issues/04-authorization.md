title: Authorization
parent: Governance
labels: -
milestone: bootstrap
---
Doctrine: whose decision permits which act. Binds once accepted.

**Acceptance is the owner's act alone.** A body is accepted when the owner posts
a comment on its issue quoting the SHA-256 over the exact UTF-8 bytes of the
body and the byte count. No agent may post, imply, or copy an acceptance. An
accepted body that is later edited loses its acceptance until re-accepted;
`bootstrap/watch/` detects such edits and never reverts them.

**The envelope rule.** A pull request cites exactly one issue, and that issue's
accepted body is the pull request's sole envelope: the pull request may contain
nothing the envelope does not authorize. A pull request exceeding its envelope
is rejected, not trimmed in review.

**Agents never merge.** Only the owner approves and merges pull requests. This
is enforced mechanically (the `owner-merges-only` ruleset restricts protected
refs to the admin role, pull-request mode) and stated here so that it binds even
where a mechanism is absent.

**Owner-walled acts** — repository settings, rulesets, `terraform apply` — run
only under the owner's credential with the owner's explicit authorization,
each time.

**Bootstrap window.** Acts before this doctrine and its siblings (`Method`,
`Identity`) were accepted are enumerated in `bootstrap/operations.md`. They are
design, not defect, and the window closed at that acceptance.
