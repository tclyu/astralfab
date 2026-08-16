# Token-usage ledger — delegated execution vs inline

Measures what delegation to subagents costs and saves. Provider token counts are
not exposed to agents, so all figures are byte-derived estimates (tokens ≈ bytes/4),
consistent across rows and therefore fair for comparison, approximate in absolute
terms.

Columns:

- **packet** — bytes of the instruction packet handed to the subagent (delegation
  overhead paid).
- **report** — bytes of the subagent's final report (what returned into the
  orchestrator's context).
- **observed** — bytes of command output the subagent saw (what stayed out of the
  orchestrator's context).
- **est. saved tokens** — (observed − report − packet) / 4. Negative means
  delegation cost more than inline execution.

| task | mode | packet B | report B | observed B | est. saved tokens | note |
| --- | --- | --- | --- | --- | --- | --- |
| staging-setup (worktree, law, skeletons) | inline | — | — | — | — | content-bearing: every byte must transit the orchestrator anyway; delegation would only add packet overhead |
| terraform init + validate + plan | subagent | 2412 | ~900 | ~29500 | ~6500 | output-heavy, content-light: the orchestrator needed only the action list and summary line |
| terraform apply + plan-zero | subagent | 2159 | ~1100 | ~5900 | ~700 | thin win: apply of a saved plan is quiet; the packet and report nearly offset the saved output |
| issue seeding (14 create + 13 edges + read-backs) | subagent | 1549 | ~1000 | ~2700 visible (~45000 API traffic) | ~40 visible; the real saving is the API JSON the script absorbed | the script, not the subagent, is what kept ~45 KB of issue JSON out of every context; delegation on top of a good script is nearly neutral |
| issue templates, seed + watch scripts | inline | — | — | — | — | content-bearing: authored by the orchestrator |
| acceptance comments (owner-authorized) | inline | — | — | ~600 | — | three small writes; delegation overhead would have exceeded the task |
| PR lane (graduate files, push, open PRs) | inline | — | — | — | — | content-bearing plus small git operations |

## Result

Net estimated saving ≈ 7,200 tokens across the build, almost all of it from one
row: delegating `terraform init/validate/plan` (~29.5 KB of output reduced to a
~0.9 KB report). The apply and seed rows were nearly neutral — their packets and
reports cost about what their outputs would have. The seed row shows the deeper
pattern: a purpose-built script kept ~45 KB of API JSON out of *every* context;
delegation on top of it added little. Conclusion for future builds: write scripts
that absorb output, and delegate only steps whose raw output is large and whose
report can be small.

## Model tiering (policy)

Choose the agent tier for the task before delegating, not the tier at hand:

- Mechanical, fully specified packets (run these commands, report these fields)
  go to the cheapest adequate tier (Cursor Auto class) — it costs almost nothing.
- Premium models are for judgment: authoring, diagnosis, design, and audits.
- If a cheap run shows quality problems, escalate: audit with a stronger model.
  An audit by the same model at the same effort as the editor is pointless.
- Two failure shapes, both waste: a premium model on a mechanical task (a gun on
  a chicken) burns the tier difference; an inadequate model retrying a hard task
  (a thousand bullets for a cow) burns more than one strong shot would have.

**Disclosure for this build:** all three subagent packets ran on the
orchestrator's own premium tier (fable-5) by default, not by decision — flagged
by the owner as mis-tiered. Every packet was mechanical; the Auto tier would
have sufficed at a fraction of the cost. Future builds default delegation to the
cheap tier and record the tier decision per row.

## Per-action accounting (byte-derived estimates, tokens ≈ bytes/4)

| action | actor (model) | est. tokens |
| --- | --- | --- |
| staging law + record skeletons authored | orchestrator (fable-5) | ~2,400 out |
| provider capability verification (docs read) | orchestrator (fable-5) | ~4,500 in |
| Terraform module authored (7 files) | orchestrator (fable-5) | ~2,300 out |
| terraform init/validate/plan run | subagent (fable-5; Auto would suffice) | ~7,400 absorbed; ~230 returned |
| plan inspection + repo read-backs | orchestrator (fable-5) | ~2,500 in |
| terraform apply + plan-zero run | subagent (fable-5; Auto would suffice) | ~1,500 absorbed; ~280 returned |
| ruleset visibility diagnosis + negative push probe | orchestrator (fable-5) | ~1,800 in |
| 14 issue templates authored | orchestrator (fable-5) | ~3,300 out |
| seed + digest-watch scripts authored | orchestrator (fable-5) | ~1,800 out |
| seed dry run + live seeding | subagent (fable-5; Auto would suffice) | ~700 absorbed (+~11,000 kept out by script); ~250 returned |
| graph, label, milestone verification | orchestrator (fable-5) | ~900 in |
| acceptance queue + convention v0 authored | orchestrator (fable-5) | ~1,100 out |
| acceptance comments posted + read back | orchestrator (fable-5) | ~150 |
| PR lane: graduation, commits, pushes, PR bodies | orchestrator (fable-5) | ~1,300 out |

"Absorbed" = output the subagent observed that never entered the orchestrator's
context; "returned" = the report that did. Inline "in" = command output and
documents read into the orchestrator's context; "out" = content authored by it.
These are the per-action inputs for future procedure optimization; the absolute
numbers are estimates, the ratios are the signal.

Rule of thumb this ledger exists to test: delegation pays on output-heavy,
content-light tasks (terraform runs, batch API mutations with read-backs) and
costs on content-bearing tasks (authoring files), because authored content must
transit the packet either way.
