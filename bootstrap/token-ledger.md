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

Rule of thumb this ledger exists to test: delegation pays on output-heavy,
content-light tasks (terraform runs, batch API mutations with read-backs) and
costs on content-bearing tasks (authoring files), because authored content must
transit the packet either way.
