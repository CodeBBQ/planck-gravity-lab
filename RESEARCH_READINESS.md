# Research Readiness Audit — Issue #6

Final status: **NO-GO**

Audited `main` commit: `c72b239c2b1da92f1b610f79030e556f6a618b5e`

This is a fresh repository-first rerun of issue #6 against accepted `main` after the previous audit fixes were merged. No substantive Planck-gravity research was performed. Only the existing explicitly non-scientific fictional-widget fixture was used for process validation.

## Fresh-session methodology

The audit began from the top-level `README.md` and issue #6 only, then followed the moderator startup path discovered in the repository. The session read the global scientific/process rules, orchestration model, moderator protocol, registry, campaign/worker/decision templates, agent bootstrap, all six role paths, the existing issue-6 dummy fixture, and the prior readiness record only after discovering it through repository state.

The audited baseline was pinned to the exact `main` SHA above. That commit is the merge of the prior issue-6 audit PR and therefore contains the fixes that the previous report required to be rerun from a new fresh session.

This session can inspect and mutate repository state and can simulate process records, but it cannot instantiate separate genuinely fresh child chats. Therefore issue #6 Phase 4 and Phase 5 cannot truthfully be marked PASS here. Static role/prompt/re-entry checks are recorded separately from the required live fresh-session acceptance tests.

## Preconditions

| Precondition | Result |
|---|---|
| #2 repository architecture present on `main` | PASS |
| #3 collaboration workflow present on `main` | PASS |
| #4 six-agent bootstrap present on `main` | PASS |
| #5 provenance workflow present on `main` | PASS |
| #18 orchestration architecture present on `main` | PASS |
| #19 registry/prompt contract present on `main` | PASS |
| #20 moderator scheduling/convergence protocol present on `main` | PASS |
| top-level README exposes moderator startup path | PASS |
| audit pinned to accepted `main`, not an implementation branch | PASS |

## Rerun of prior audit defects

### AUD-6-01 — stale `REPOSITORY_ARCHITECTURE.md`

**PASS on repaired `main`.**

`REPOSITORY_ARCHITECTURE.md` now describes the implemented six-agent system, provenance workflow, orchestration layer, canonical moderator/worker startup paths, and the remaining issue-6 gate. The stale #4/#5 architecture claims from the previous audited baseline are gone.

### AUD-6-02 — worker prompt boundaries not fully durable

**PASS on repaired `main`.**

`orchestration/WORKER_TEMPLATE.md` now durably stores `scope`, `non_goals`, required starting context, independence exclusions, dependencies/blockers, concurrency, branch/write scope, required outputs, completion criteria, structured handoff obligations, and scientific/process references. The template explicitly requires the durable record to contain the same task boundaries and handoff obligations as the generated prompt.

The existing isolated fixture exercises these fields and remains explicitly outside production registry state.

### AUD-6-03 — genuinely fresh child sessions unavailable in this execution environment

**STILL UNRESOLVED AS AN AUDIT-COMPLETION BLOCKER.**

This is not demonstrated to be a repository defect. It prevents truthful completion of Phase 4 and Phase 5 in this session.

## New defects found in this fresh rerun

### AUD-6-04 — stale worker-startup instruction in `PROJECT_RULES.md`

Severity: bootstrap/cross-system consistency blocker.

The audited `main` still stated that bootstrap issue #4 *will add* the mandatory role-specific agent file and referred to `README.md -> "Start here if you are an AI research session"`, a heading that no longer exists. A fresh worker reading the authoritative scientific rules therefore encounters obsolete startup guidance that contradicts the implemented role-specific system.

Fix on this branch: replace the stale issue-#4 language with the current moderator/worker startup paths and readiness gate.

Required rerun after merge: Phase 1, worker bootstrap portion of Phase 4, and Phase 10 in another genuinely fresh session.

### AUD-6-05 — stale bootstrap boundary in `COLLABORATION_WORKFLOW.md`

Severity: bootstrap/cross-system consistency blocker.

The audited `main` still said issue #4 *must now* create role files and issue #5 *must* formalize provenance mechanics, even though both are already implemented and merged. Section 8 also said those conventions were merely to be finalized by #5. This contradicts accepted repository state and can make a fresh session uncertain which workflow is authoritative.

Fix on this branch: point directly to `PROVENANCE_WORKFLOW.md`, `ORCHESTRATION_MODEL.md`, `orchestration/README.md`, and the implemented six-agent system; retain issue #6 as the only research-start bootstrap gate.

Required rerun after merge: Phase 1 and Phase 10 in another genuinely fresh session.

## Phase results

### Phase 1 — Entry-point and moderator bootstrap

**FAIL due to cross-system inconsistency; direct README discovery itself passes.**

Starting only from `README.md`, a fresh session can discover the moderator/research-coordinator interface, `ORCHESTRATION_MODEL.md`, `orchestration/README.md`, `orchestration/MODERATOR_PROTOCOL.md`, `orchestration/registry.yaml`, record/template locations, the agent/worker distinction, and the fact that the moderator is not a scientific authority.

The prior architecture defect is repaired. However, the newly found stale authoritative guidance in `PROJECT_RULES.md` and `COLLABORATION_WORKFLOW.md` means the whole bootstrap path is not internally consistent on the audited baseline. The straightforward fixes are included on this branch, but issue #6 requires a new fresh-session rerun after merge.

### Phase 2 — Create a dummy campaign through the moderator

**PASS at repository-contract/static execution level; live child-session acceptance remains downstream.**

The campaign template supports bounded objective, scope, non-goals, required nodes, verification/review gates, blockers, exit criteria, worker set, scientific references, and final disposition. The worker template now durably matches its prompt contract. The isolated fixture demonstrates a bounded fictional-widget campaign, a moderator decision, justified worker batch, blocked work, and copy-ready prompt structure without using production IDs.

The user does not need to design a worker DAG manually: the moderator protocol requires mapping unmet campaign exit criteria to unresolved nodes, checking prior work/dependencies, selecting ready roles, and explaining why each worker exists.

### Phase 3 — Parallelism, dependency, and duplicate control

**PASS statically.**

The protocol and fixture exercise three orthogonal workers, two deliberate independent replications with contamination exclusions, a withheld blocked dependency, and suppression of a duplicate worker lacking replication purpose. Parallel worker count follows task structure rather than a requested number.

### Phase 4 — Fresh worker execution

**NOT PASSED.**

All six role files are discoverable and the repaired worker record/prompt contract carries the required ID, campaign, role, task/reason, scope/non-goals, dependencies, exclusions, branch/write scope, outputs, completion criteria, handoff, and provenance requirements. Static smoke coverage exists for literature scout, approach researcher, numerical verifier, adversarial reviewer, foundations researcher, and synthesis researcher.

Issue #6 nevertheless requires separate genuinely fresh worker sessions using only generated prompts and repository access. This execution environment cannot create those sessions. In addition, the newly found `PROJECT_RULES.md` startup inconsistency must be merged and rerun before this phase could pass even in a suitable environment.

### Phase 5 — Worker completion -> moderator re-entry

**NOT PASSED.**

The isolated fixture demonstrates durable completed/blocked/failed/superseded states and a replacement-moderator decision that schedules the next enabled gate without repeating completed work. The production registry/templates are designed to preserve this state.

Issue #6 requires an actually new moderator session with repository-only access. This environment cannot instantiate that separate session, so simulation is not accepted as a live pass.

### Phase 6 — Failure and re-scoping

**PASS statically.**

The moderator protocol distinguishes environmental/process failure, missing dependency, over-broad/ambiguous work, unavailable evidence/input, and valid negative results. Retry is not automatic; replacement workers must record what changed; negative results are preserved rather than retried to obtain a preferred outcome. The fixture covers each case.

### Phase 7 — Verification/review independence

**PASS at orchestration-rule level; live fresh execution pending.**

The collaboration/orchestration rules require independent numerical verification for decisive quantitative outputs and adversarial review before decisive promotion. Original authors cannot serve as their own independent verifier/reviewer, and independence-sensitive starting context can exclude sibling intermediate conclusions. The fixture exercises independent dummy reproductions and a separate reviewer.

The live fresh verifier/reviewer execution remains unpassed under Phase 4.

### Phase 8 — Convergence and stopping

**PASS statically.**

The moderator protocol requires each proposed worker to map to an unmet exit criterion and exact unresolved node, explain why existing work is insufficient, be ready, produce a state-changing output, and lead to an explicit next gate. It supports completed/rejected/blocked/paused outcomes and suppresses further work when no justified state-changing worker exists. The fixture contains both successful and blocked endings.

### Phase 9 — Scientific provenance integration

**PASS statically.**

Process provenance (`CMP-*`, `MOD-*`, `WRK-*`) remains separate from scientific provenance (`CLM-*`, `CAL-*`, `REV-*`, `CAN-*`). The provenance workflow preserves challenged/rejected/superseded records, requires traceable calculation inputs, and prevents unresolved/unverified decisive evidence from entering final synthesis. The dummy fixture uses only explicitly non-scientific placeholder IDs and never substitutes process IDs for evidence.

A genuinely fresh numerical verifier tracing a decisive calculation remains pending under Phase 4.

### Phase 10 — Cross-system consistency

**FAIL on audited `main`; fixes included on this branch.**

| Check | Result on audited `main` |
|---|---|
| README describes current bootstrap state | PASS |
| moderator startup discoverable | PASS |
| all six research-agent files discoverable | PASS |
| repaired worker template matches prompt contract | PASS |
| campaign/decision templates match moderator protocol | PASS |
| registry fields/ID allocation align with templates | PASS |
| lifecycle/status vocabulary is usable across documents | PASS |
| branch/write-scope conventions align with orchestration | PASS |
| provenance terminology is consistent | PASS except stale #5 implementation wording in collaboration document |
| unresolved disputes have durable `reviews/` home | PASS |
| rejected approaches/workers remain preserved | PASS |
| no essential instruction depends on old chat history | PASS for implemented contracts |
| authoritative startup/bootstrap wording is current everywhere | **FAIL** — `PROJECT_RULES.md` and `COLLABORATION_WORKFLOW.md` contain stale bootstrap instructions |

Because the audited baseline itself contains these contradictions, fixes made on this branch cannot be counted as a fresh-session pass. The affected checks must be rerun after merge.

## Explicit readiness checklist

| Area | Result |
|---|---|
| repository architecture | PASS after prior fix |
| scientific rules | FAIL only for stale startup text; scientific constraints themselves consistent |
| evidence/provenance | PASS statically |
| collaboration independence | PASS statically; live verifier/reviewer pending |
| all research agents | PASS discoverability/static bootstrap; live worker execution pending |
| moderator discoverability | PASS from README |
| campaign creation | PASS statically after prior worker-template fix |
| worker ID/registry memory | PASS statically |
| copy-ready worker prompts | PASS statically after prior fix |
| parallelism/replication/dependency logic | PASS statically |
| duplicate suppression | PASS statically |
| moderator replacement/re-entry | NOT PASSED — genuine fresh moderator required |
| failure/re-scoping | PASS statically |
| verification/review scheduling | PASS statically; live independence execution pending |
| convergence/stopping | PASS statically |
| process-to-scientific provenance integration | PASS statically; live verifier trace pending |
| cross-system bootstrap consistency | FAIL on audited baseline; fixes included; fresh rerun required |

## Fixes made during this rerun

1. Updated `PROJECT_RULES.md` to remove obsolete issue-#4/fictitious-heading startup guidance and point to the current moderator/worker bootstrap paths.
2. Updated `COLLABORATION_WORKFLOW.md` to remove obsolete issue-#4/#5 implementation language and point to the implemented agent, provenance, and orchestration systems.
3. Updated this readiness report with the new audited `main` SHA, the successful fresh rerun of the prior architecture/worker-template defects, the newly discovered defects, and the remaining live-session blockers.

The existing isolated non-scientific fixture under `orchestration/audit-fixtures/issue-6/` remains sufficient for dummy process validation and is intentionally not production registry state.

## Tests rerun after fixes

Within this same session, the edited documents were checked for consistency with the top-level README, orchestration model, moderator protocol, agent bootstrap, and provenance workflow. These same-session checks are useful edit validation but **do not count as the issue-mandated fresh-session rerun** of newly discovered blockers.

No separate fresh worker sessions or replacement moderator session were executed here.

## Final decision

**NO-GO.**

This fresh rerun confirms that the two defects fixed by the previous audit are repaired on accepted `main`, but it discovered two additional stale bootstrap instructions in authoritative repository documents. Those fixes must be merged and their affected acceptance tests rerun from another genuinely fresh session. Independently, Phase 4 and Phase 5 still require actual separate fresh worker/moderator sessions rather than static simulation.

No substantive Planck-gravity research was performed, and no first real campaign is suggested because issue #6 permits that only after a valid GO.
