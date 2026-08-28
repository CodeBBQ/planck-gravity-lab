# Research Orchestration Model

This document defines the process layer above research agents. It governs how campaigns are decomposed into concrete worker instances and how a moderator decides what should run next.

Scientific authority remains in `PROJECT_RULES.md`, `LITERATURE_RULES.md`, `PROVENANCE_WORKFLOW.md`, and reviewed research outputs. The moderator is never a substitute for a scientific role.

## 1. Core concepts

### Agent
A reusable research-role specification in `agents/`, such as literature scout or numerical verifier.

### Worker
One concrete execution of one agent on one scoped task. A worker is ephemeral as a chat/process but must have durable repository identity and state.

### Campaign
A bounded research objective composed of multiple workers and explicit exit criteria.

### Moderator / research coordinator
A process role that inspects campaign and repository state, identifies unresolved work, and recommends which workers should be launched next.

## 2. Relationship between layers

```text
project goal
   ↓
campaign
   ↓
moderator decision
   ↓
worker specification
   ↓
agent executes worker
   ↓
repository output + handoff
   ↓
moderator re-evaluates state
```

Agents define *how work is performed*. The moderator defines *which work exists next*.

## 3. Moderator authority

The moderator may:
- inspect accepted and exploratory repository state;
- inspect campaign/worker/dependency state;
- identify missing, unverified, challenged, blocked, or redundant nodes;
- decide which tasks are ready;
- decide which tasks may run concurrently;
- require independent replication when the workflow calls for it;
- construct worker specifications and prompts;
- recommend campaign closure, pause, or continuation based on explicit exit criteria.

The moderator must not:
- create or validate scientific claims itself;
- replace literature assessment, numerical verification, adversarial review, or synthesis;
- silently resolve scientific disagreements;
- promote E3/E4 assumptions;
- waive independence requirements;
- launch work merely to increase worker count.

## 4. Campaign lifecycle

Recommended states:

```text
proposed -> active -> review_pending -> completed
                    \-> blocked
                    \-> rejected
                    \-> paused
```

A campaign record must define:
- precise objective;
- scope/non-goals;
- required scientific nodes or deliverables;
- mandatory review/verification gates;
- candidate exit criteria;
- known blockers;
- worker set/dependency graph;
- final disposition.

## 5. Worker existence rule

Every worker must exist because of a specific unresolved campaign need.

A worker is justified only if it does at least one of the following:
- fills a missing evidence node;
- performs an uncompleted calculation;
- independently verifies a decisive result;
- adversarially reviews a material conclusion;
- resolves a concrete dispute;
- synthesizes work whose prerequisites are complete;
- replaces/re-scopes failed or invalid prior work.

A worker must not be spawned if existing repository state already resolves the same task unless the moderator explicitly records that independent replication is the purpose.

## 6. Dependency semantics

Workers may have zero or more prerequisites.

- `ready`: all prerequisites satisfied.
- `blocked`: at least one required dependency unresolved.
- `independent`: intentionally starts from the same accepted baseline without reading sibling exploratory conclusions.
- `follow-up`: depends on one or more completed workers.

The moderator must not recommend blocked workers as startable.

## 7. Concurrency classes

### Orthogonal parallelism
Workers answer different non-overlapping subquestions whose outputs can be combined later.

Example pattern:
- evidence capability,
- noise/systematics,
- foundational metric.

### Independent replication
Workers intentionally answer the same question independently to reduce anchoring or verify a decisive result.

Replication must be explicit; duplicate task text alone does not justify parallel execution.

### Sequential work
A worker needs outputs from earlier workers before its task can be defined or validly executed.

### Redundant work
A proposed worker duplicates already adequate work without a stated replication purpose. The moderator should not launch it.

## 8. Contamination control

The moderator controls which repository context is necessary for each worker.

Workers always inherit accepted global rules and definitions. For independence-sensitive work, the worker specification may deliberately exclude another exploratory worker's intermediate conclusions while still providing the source claims/equations necessary to reproduce the task.

Examples:
- a numerical verifier may receive source-backed inputs and the claimed final result but not the original intermediate arithmetic;
- parallel approach researchers may share accepted definitions/evidence but not each other's branch conclusions before their first-pass analyses.

## 9. Moderator cycle

The default orchestration loop is:

```text
1. Inspect campaign, worker registry, claims, calculations, reviews, branches
2. Determine unresolved nodes and blockers
3. Check whether existing work already resolves them
4. Build/update dependencies
5. Select ready workers
6. Classify concurrency: orthogonal / replication / sequential
7. Create worker specifications/prompts
8. User launches workers
9. Workers commit outputs and handoffs
10. Moderator ingests durable state
11. Trigger verification/review/dispute resolution as required
12. Evaluate campaign exit criteria
13. Spawn more only if a specific unresolved node remains
```

## 10. Campaign convergence and stopping

A campaign does not end because a fixed number of workers ran. It ends when its exit conditions are met.

Typical completion conditions for an experimental-approach campaign may include:
- observable defined;
- governing equations accepted;
- relevant Planck metric defined;
- demonstrated technology evidence established;
- decisive inputs verified;
- signal estimate completed;
- noise/systematics characterized sufficiently for the claim;
- scaling/gap quantified;
- decisive calculations independently verified;
- adversarial review resolved;
- strongest surviving configuration identified;
- unresolved assumptions explicitly bounded.

A campaign may also terminate as:
- `rejected`: evidence/calculation establishes the route does not survive current constraints;
- `blocked`: a decisive missing input cannot currently be obtained;
- `paused`: further work is possible but not presently justified/prioritized.

The moderator should record why additional workers are unlikely to change a completed/rejected conclusion.

## 11. Anti-infinite-spawning rules

Before proposing any new worker, the moderator must answer:
1. What exact unresolved node does this worker address?
2. Why is existing work insufficient?
3. What output will change campaign state?
4. Is this worker ready now?
5. Is parallelism/replication scientifically justified?
6. What condition will prevent another equivalent worker from being spawned afterward?

If these cannot be answered, do not spawn the worker.

## 12. User interaction model

The intended user workflow is:

```text
User: What should I run next?
Moderator: inspect repo -> recommend ready worker batch + copy-ready prompts
User launches workers
Workers finish/commit/handoff
User: Workers X-Y are done. What next?
Moderator: inspect durable state -> recommend next batch or close/pause campaign
```

The user should not need to manually manage the research dependency graph.

## 13. Integration with provenance and Git

Worker/campaign identity is process provenance, distinct from scientific provenance (`CLM-*`, `CAL-*`, `REV-*`, `CAN-*`). Worker records should point to scientific IDs and output files where relevant.

Workers should use task branches according to `COLLABORATION_WORKFLOW.md`. `main` remains accepted shared state; the moderator may inspect branch state but does not treat unmerged branch content as accepted truth.

## 14. Implementation boundary

This issue defines orchestration semantics only.

Issue #19 implements durable campaign/worker registries, IDs, lifecycle records, and prompt contracts.
Issue #20 implements the moderator scheduling protocol and user-facing next-worker recommendations.
Issue #6 validates the complete system with fresh-session dry runs.
