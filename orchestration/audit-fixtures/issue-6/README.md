# Issue #6 isolated orchestration fixture

This directory is deliberately **non-scientific** and is not part of the production `orchestration/registry.yaml`. It exercises the process contracts without creating real research workers. IDs below are fixture-only examples and must never be interpreted as scientific evidence or production allocations.

## Dummy campaign

```yaml
id: CMP-9001
title: Fictional measurement-widget evaluation
status: active
objective: Determine whether three fictional widget families satisfy a made-up acceptance contract and whether a decisive dummy score is reproducible and reviewable.
scope:
  - fictional widget documentation
  - arbitrary-unit arithmetic
non_goals:
  - physics
  - real experimental capability
  - Planck-gravity research
required_nodes:
  - node-A: catalogue fictional widget inputs
  - node-B: evaluate fictional widget geometry
  - node-C: evaluate fictional widget logging behavior
  - node-D: independently reproduce decisive dummy score twice
  - node-E: adversarially review decisive dummy result
  - node-F: synthesize only after required gates
verification_gates:
  - two independent reproductions of node-D agree within fixture tolerance
review_gates:
  - node-E resolved
exit_criteria:
  - nodes A-E resolved
  - verification and review gates satisfied
  - no unresolved decisive dummy input
known_blockers:
  - node-F blocked until D and E complete
```

## First moderator decision

```yaml
id: MOD-9001
campaign: CMP-9001
unresolved_nodes: [node-A, node-B, node-C, node-D, node-E, node-F]
workers_recommended: [WRK-9001, WRK-9002, WRK-9003, WRK-9004, WRK-9005]
workers_withheld: [WRK-9006, duplicate-proposal]
withheld_reasons:
  - WRK-9006 depends on decisive dummy score and review
  - duplicate-proposal repeats WRK-9001 with no replication purpose
concurrency:
  mode: orthogonal-plus-replication
  rationale: WRK-9001/2/3 answer independent subquestions; WRK-9004/5 deliberately reproduce the same decisive dummy arithmetic from identical accepted inputs while excluding each other's work.
stopping_assessment: continue
next_inspection_trigger: durable outputs and handoffs from WRK-9001 through WRK-9005
```

## Worker matrix

| Worker | Agent | Node | Concurrency | Independence | State in scenario |
|---|---|---|---|---|---|
| WRK-9001 | literature_scout | A | orthogonal | none | ready/completed |
| WRK-9002 | approach_researcher | B | orthogonal | none | ready/completed |
| WRK-9003 | foundations_researcher | C | orthogonal | none | ready/completed |
| WRK-9004 | numerical_verifier | D | replication | exclude WRK-9005 conclusion/arithmetic | ready/completed |
| WRK-9005 | numerical_verifier | D | replication | exclude WRK-9004 conclusion/arithmetic | ready/completed |
| WRK-9006 | synthesis_researcher | F | sequential | none | blocked until D/E |
| WRK-9007 | adversarial_reviewer | E | sequential | original authors excluded as reviewer | enabled after D |
| WRK-9008 | literature_scout | failure test | sequential replacement | references failed WRK-9001 variant | failed/re-scoped |

Each fixture worker uses the durable fields required by `WORKER_TEMPLATE.md`: task, reason, `scope`, `non_goals`, starting context, exclusions, dependencies, concurrency, branch/write scope, outputs, completion criteria, and handoff contract.

## Copy-ready prompt smoke test

Representative prompt skeleton used for each role:

```text
Worker ID: <WRK fixture ID>
Campaign ID: CMP-9001
Assigned agent: <role>

You are executing one non-scientific audit worker instance in CodeBBQ/planck-gravity-lab.
Follow the canonical repository startup protocol and the worker record. Repository state is authoritative; do not rely on prior chat history.

Task: <exact node question>
Why this worker exists: <unresolved node>
Scope: fictional widget fixture only.
Non-goals: no physics, no Planck-gravity research, no adjacent task expansion.
Starting context: README, global rules, orchestration model, agents/README, assigned agent file, this fixture.
Independence constraints: <explicit exclusions or none>.
Dependencies: <explicit prerequisites>.
Branch/write scope: audit fixture output only.
Required outputs: durable result + handoff.
Completion criteria: node-specific binary test.
Handoff: moderator; include result, files, unresolved items, and next enabled gate.
```

Role-path smoke checks cover `literature_scout`, `approach_researcher`, `numerical_verifier`, `adversarial_reviewer`, `foundations_researcher`, and `synthesis_researcher`.

## Re-entry scenario

After simulated durable completion, a replacement moderator sees:

- WRK-9001/2/3 completed;
- WRK-9004/5 completed with independent dummy reproductions;
- WRK-9007 ready for adversarial review;
- WRK-9006 still blocked until review resolves;
- WRK-9008 failed because its task was intentionally over-broad, then replaced by a narrower worker rather than automatically retried;
- the duplicate WRK-9001 proposal remains suppressed.

The next decision must schedule WRK-9007, not repeat completed work.

## Failure classification fixture

The fixture distinguishes:

- environmental/process failure -> retry may be justified only with recorded change;
- missing dependency -> remain blocked;
- over-broad/ambiguous task -> re-scope and reference predecessor;
- unavailable input -> campaign blocked/paused if decisive;
- valid negative dummy result -> preserve as completed result, do not retry for a preferred answer.

## Independence fixture

A decisive arbitrary-unit result is authored by a dummy approach worker, independently reconstructed by WRK-9004 and WRK-9005, and reviewed by WRK-9007. The original author is not eligible to be the independent verifier or reviewer. Replication workers exclude each other's intermediate arithmetic and conclusions.

## Convergence fixture

Successful ending: all mandatory nodes/gates resolve, moderator marks `completed`, and no further worker is justified.

Blocked ending: a required fictional input is declared unavailable; moderator marks the campaign `blocked` rather than spawning exploratory duplicates.

Every proposed extra worker must identify the unmet exit criterion, unresolved node, insufficiency of existing work, appropriate role, readiness, state-changing output, and following gate. Otherwise it is suppressed.

## Process/scientific provenance separation smoke test

Fixture-only process IDs (`CMP/MOD/WRK`) may point to placeholder scientific IDs such as `CLM-example-001`, `CAL-example-001`, and `REV-example-001`, but never substitute for them. No real claim, evidence, calculation, approach, candidate, or synthesis record is created by this fixture.
