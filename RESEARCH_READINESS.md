# Research Readiness Audit — Issue #6

Final status: **NO-GO**

Audited `main` commit: `c9553854ce0026bf2519cf4fba6fc55fadf20049`

This audit was performed as a fresh repository-first readiness audit. No substantive Planck-gravity research was performed. Only non-scientific fictional-widget content was used for orchestration scenarios.

## Methodology

The audit began from the top-level `README.md` and issue #6, then followed the moderator startup path discovered there. The audited baseline was the exact `main` commit above. Preconditions #2, #3, #4, #5, #18, #19, #20 and the pre-audit navigation integration were confirmed present in `main` history before proceeding.

The audit inspected the global scientific/process rules, orchestration model, moderator protocol, registry, templates, and all six agent-role paths. An isolated dummy orchestration fixture was created under `orchestration/audit-fixtures/issue-6/`; it is intentionally not production registry state.

Two repository defects were discovered during the first fresh audit and are bootstrap blockers under issue #6. They were corrected on this audit branch, but issue #6 explicitly requires affected acceptance tests to be rerun in another genuinely fresh session after fixes are merged before GO can be declared. This session therefore remains NO-GO.

In addition, the present execution environment cannot create genuinely separate fresh worker chats or a second fresh moderator chat. Static prompt/role smoke tests and repository-state simulations were performed, but they are not a valid substitute for the issue's Phase 4 and Phase 5 independence requirement. Those phases therefore remain unpassed.

## Preconditions

| Preconditions | Result |
|---|---|
| #2 repository architecture | PASS — merged before audited baseline |
| #3 collaboration workflow | PASS — merged before audited baseline |
| #4 agent protocol | PASS — merged before audited baseline |
| #5 provenance workflow | PASS — merged before audited baseline |
| #18 orchestration architecture | PASS — merge commit present in `main` history |
| #19 registry/prompt contract | PASS — merge commit present in `main` history |
| #20 moderator scheduling/convergence | PASS — merge commit present in `main` history |
| pre-audit README navigation | PASS — audited `main` is merge commit for that integration |
| audit run against `main` | PASS — baseline pinned to SHA above |

## Phase results

### Phase 1 — Entry-point and moderator bootstrap

**PASS with cross-system defect discovered later.**

Starting from `README.md`, the moderator path is discoverable without guessed filenames. It points to `ORCHESTRATION_MODEL.md`, `orchestration/README.md`, `orchestration/MODERATOR_PROTOCOL.md`, `orchestration/registry.yaml`, campaign/worker/decision records and templates. The distinction between reusable scientific agents and the moderator process role is explicit, and the moderator is explicitly not a scientific authority.

However, `REPOSITORY_ARCHITECTURE.md` was stale and still claimed that per-agent instructions and provenance mechanics remained missing. This contradicted current repository state and could mislead a fresh session. It is a cross-system consistency/bootstrap defect and contributes to the final NO-GO.

Fix on this branch: `REPOSITORY_ARCHITECTURE.md` was refreshed to the current architecture and startup paths.

### Phase 2 — Dummy campaign through moderator

**PARTIAL / NOT ACCEPTED AS END-TO-END PASS.**

The moderator contracts are sufficient to construct a bounded dummy campaign, explicit nodes/gates/exit criteria, a moderator decision, justified worker tasks, and copy-ready prompts. The isolated fixture demonstrates this structure.

A defect was found in the production `WORKER_TEMPLATE.md`: the durable worker record did not contain explicit `scope`, `non_goals`, or a substantive durable handoff contract, although the prompt contract requires those fields. That means a generated prompt could contain task boundaries that were not fully reconstructible from durable worker state after chat replacement.

Fix on this branch: `WORKER_TEMPLATE.md` now persists `scope`, `non_goals`, and a structured handoff contract, and states that prompt-only scope is not durable process memory.

Because this defect was found in the first fresh audit, the affected campaign/worker-contract test must be rerun in another fresh session after merge.

### Phase 3 — Parallelism, dependency, duplicate control

**STATIC LOGIC PASS; fresh rerun still required.**

The moderator model/protocol explicitly supports:

- three orthogonal workers on distinct independent nodes;
- deliberate independent replication with explicit contamination exclusions;
- blocked dependency withholding;
- duplicate suppression unless replication purpose is explicit.

The isolated fixture exercises all four cases. Worker count follows task structure rather than a user-specified parallelism number.

### Phase 4 — Fresh worker execution

**NOT PASSED.**

All six agent files are discoverable. Representative role instructions for literature, approach, numerical verification, adversarial review, foundations, and synthesis resolve from the canonical worker bootstrap. Static prompt smoke tests show that the repository has fields for ID, campaign, role, task/reason, scope/non-goals, dependencies, exclusions, branch/write scope, outputs, completion criteria, handoff, and provenance references after the template fix.

But issue #6 requires separate genuinely fresh worker sessions using only generated prompts and repository access. This audit environment cannot launch separate fresh chats. Therefore static inspection is insufficient and this phase remains unpassed.

### Phase 5 — Worker completion -> moderator re-entry

**NOT PASSED.**

The fixture demonstrates how durable worker states and handoffs allow a replacement moderator to distinguish completed, blocked, failed, and superseded work and choose the next gate without repeating completed work.

However, issue #6 requires a new fresh moderator session with repository-only access. This session cannot instantiate a second genuinely fresh moderator. Therefore this phase remains unpassed.

### Phase 6 — Failure and re-scoping

**STATIC LOGIC PASS.**

`MODERATOR_PROTOCOL.md` distinguishes environmental/process failure, missing dependency, over-broad/ambiguous tasks, unavailable evidence/input, and valid negative results. Retry is not automatic; replacement/re-scoped workers must reference prior work; negative results are preserved. The fixture exercises these cases.

### Phase 7 — Verification/review independence

**STATIC LOGIC PASS; live fresh-session test pending.**

The orchestration and collaboration rules require an independent numerical verifier for decisive quantitative results and adversarial review before decisive promotion. Original authors cannot serve as their own independent verifier/reviewer. Independence-sensitive workers may exclude sibling exploratory conclusions/intermediate arithmetic. The fixture exercises two independent reproductions and a separate reviewer.

A genuinely fresh verifier/reviewer execution remains part of the unpassed Phase 4 test.

### Phase 8 — Convergence and stopping

**STATIC LOGIC PASS.**

The protocol requires each new worker to map to an unmet exit criterion and unresolved node, state why existing work is insufficient, be ready, produce state-changing output, and lead to an explicit next gate. It defines completed/rejected/blocked/paused dispositions and forbids endless duplicate spawning. The fixture covers successful completion and an unresolvable blocker ending.

### Phase 9 — Scientific provenance integration

**STATIC LOGIC PASS.**

Process provenance (`CMP/MOD/WRK`) is explicitly separate from scientific provenance (`CLM/CAL/REV/CAN`). `PROVENANCE_WORKFLOW.md` provides traceable claim/calculation/review rules, preserves challenged/rejected/superseded records, and prevents unresolved/unverified decisive evidence from entering synthesis. The fixture uses non-scientific placeholder IDs only and does not create scientific evidence.

A genuinely fresh numerical verifier tracing a decisive calculation remains pending under Phase 4.

### Phase 10 — Cross-system consistency

**FAIL on audited baseline; fixes included on audit branch.**

Checks:

- README describes moderator interface and research-start gate: PASS.
- moderator startup discoverable: PASS.
- all six research-agent files discoverable: PASS.
- campaign/decision templates broadly match moderator protocol: PASS.
- worker template matched prompt contract on audited baseline: **FAIL** — scope/non-goals/handoff were prompt-only rather than fully durable.
- registry ID fields and lifecycle vocabulary: PASS at schema/document level.
- branch/write-scope conventions compatible with orchestration: PASS.
- provenance terminology: PASS.
- unresolved disputes have durable `reviews/` home: PASS.
- rejected approaches/workers are preserved: PASS.
- no essential instruction exists only in old chats: PASS for inspected contracts.
- architecture bootstrap status current: **FAIL** — `REPOSITORY_ARCHITECTURE.md` still described #4/#5 as missing.

Both identified repository defects are fixed on this branch, but their acceptance tests have not been rerun from another fresh session after merge.

## Defects found

### AUD-6-01 — stale architecture/bootstrap state

Severity: bootstrap blocker.

The audited `REPOSITORY_ARCHITECTURE.md` described role-specific instructions and provenance hardening as still missing, despite #4 and #5 being merged. This violates cross-system consistency and can force a fresh session to reconcile contradictory repository instructions.

Fix included: refresh architecture/readiness document to current startup/orchestration state.

Required rerun: Phase 1 and Phase 10 in a new fresh session after merge.

### AUD-6-02 — worker prompt boundaries not fully durable

Severity: bootstrap blocker.

The audited worker prompt required scope, non-goals, and a handoff description, but the durable YAML worker template did not persist explicit scope/non-goals and had only `handoff_to` rather than the required handoff content. A replacement moderator/worker could therefore lose prompt-only task boundaries.

Fix included: add `scope`, `non_goals`, and structured `handoff.target` / `handoff.required_summary` fields and require record/prompt equivalence.

Required rerun: Phase 2, Phase 4, Phase 5, and Phase 10 in a new fresh session after merge.

### AUD-6-03 — required genuinely fresh child sessions not executable here

Severity: audit-completion blocker, not currently demonstrated to be a repository defect.

This execution environment cannot launch separate fresh worker chats or a second fresh moderator chat. The repository contracts can be statically inspected and simulated, but issue #6 explicitly makes fresh-session replacement part of acceptance. Those tests cannot truthfully be marked PASS in this session.

Required rerun: Phase 4 and Phase 5 using actual fresh sessions after the repository fixes are merged.

## Explicit checklist

| Area | Result |
|---|---|
| repository architecture | FAIL on baseline; fix included; fresh rerun required |
| scientific rules | PASS |
| evidence/provenance | PASS statically |
| collaboration independence | PASS statically; live fresh verifier/reviewer pending |
| all research agents | PASS discoverability/static bootstrap; live fresh worker execution pending |
| moderator discoverability | PASS |
| campaign creation | PARTIAL; durable-worker defect fixed; fresh rerun required |
| worker ID/registry memory | PASS statically |
| copy-ready worker prompts | PARTIAL; record/prompt durability defect fixed; fresh rerun required |
| parallelism/replication/dependency logic | PASS statically |
| duplicate suppression | PASS statically |
| moderator replacement/re-entry | NOT PASSED — genuine fresh moderator required |
| failure/re-scoping | PASS statically |
| verification/review scheduling | PASS statically; live independence execution pending |
| convergence/stopping | PASS statically |
| process-to-scientific provenance integration | PASS statically; live verifier trace pending |

## Fixes made during this audit

1. Refreshed `REPOSITORY_ARCHITECTURE.md` so current agent/provenance/orchestration implementation and startup paths are accurately represented.
2. Hardened `orchestration/WORKER_TEMPLATE.md` so scope, non-goals, and handoff obligations are durable rather than prompt-only.
3. Added an explicitly isolated non-scientific audit fixture covering parallelism, replication, blocking, duplicate suppression, failure/re-scoping, independence, convergence, and provenance separation.

## Tests rerun after fixes

Within this same session, static consistency checks were repeated against the edited files. **No test is counted as the issue-mandated fresh-session rerun.** Issue #6 requires another genuinely fresh session after fixes before GO.

## Final decision

**NO-GO.**

The audited `main` baseline contained two bootstrap/workflow inconsistencies, and the mandatory separate fresh-worker and fresh-moderator execution tests were not executable in this session. The fixes in this branch should be merged, then issue #6 must be rerun from a new fresh audit session. Only that later session may declare GO if the repaired repository supports the complete user -> moderator -> worker -> durable handoff -> replacement moderator loop without extra explanation or old chat context.

No first real Planck-gravity campaign is suggested because issue #6 permits such suggestions only after GO.
