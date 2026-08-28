# Moderator Scheduling and Convergence Protocol

The moderator is the user's control interface for research progression. It reads durable repository state, decides which worker instances are justified next, and produces complete copy-ready prompts. It does not establish scientific truth.

## 1. Moderator startup

Before scheduling work, read:
- `README.md`
- `PROJECT_RULES.md`
- `LITERATURE_RULES.md`
- `REPOSITORY_ARCHITECTURE.md`
- `COLLABORATION_WORKFLOW.md`
- `PROVENANCE_WORKFLOW.md`
- `ORCHESTRATION_MODEL.md`
- `orchestration/README.md`
- `orchestration/registry.yaml`
- relevant campaign and worker records
- relevant accepted scientific files/IDs

## 2. Decision cycle

For each active campaign:

1. Determine current campaign status and unmet exit criteria.
2. Map every unmet criterion to a concrete unresolved node.
3. Check whether existing workers or accepted outputs already address that node.
4. Identify prerequisites and blockers.
5. Classify candidate work as orthogonal parallel, independent replication, sequential follow-up, or redundant.
6. Reject redundant work unless a replication purpose is explicitly required.
7. Allocate worker IDs only for work that is ready or deliberately recorded as blocked/planned.
8. Generate complete worker records and copy-ready prompts.
9. Tell the user exactly which workers to start now and why.
10. After worker completion, inspect durable outputs/handoffs before scheduling further work.
11. Trigger numerical verification/adversarial review when decisive outputs require them.
12. Evaluate campaign stopping state before spawning another worker.

## 3. Ready-to-run test

A worker is `ready` only if:
- its unresolved reason is explicit;
- no existing accepted output adequately resolves the same node;
- all required dependencies are complete;
- its agent role is appropriate to the task;
- branch/write scope is known;
- completion criteria and handoff are explicit;
- independence constraints are defined where relevant.

## 4. Parallelism test

Workers may be recommended together only when one of these is true:

### Orthogonal parallelism
They answer distinct subquestions and neither requires the other's output.

### Deliberate replication
They intentionally answer the same decisive question independently. The worker records must state the replication purpose and contamination controls.

Otherwise schedule sequentially.

## 5. Duplicate detection

Before creating a worker, search:
- worker registry/tasks/reasons;
- campaign required nodes;
- relevant claim/calculation/review/candidate IDs;
- accepted approach files;
- active branches when process state matters.

If prior work already satisfies the proposed task, do not launch another worker. If prior work is incomplete, challenged, failed, or unsuitable, record exactly why a new/re-scoped worker is justified.

## 6. Failure and re-scoping

A failed or blocked worker does not automatically justify an identical retry.

Moderator must classify the failure:
- environmental/process failure: retry may be appropriate;
- missing dependency: block until dependency resolves;
- task too broad/ambiguous: re-scope into narrower worker(s);
- evidence unavailable: campaign may become blocked/paused;
- scientific result negative: preserve result; do not retry merely seeking a preferred answer.

Replacement workers must reference the previous worker and state what changes.

## 7. Verification and review triggers

The moderator must schedule an independent numerical verifier when a decisive quantitative result is produced and not yet independently reproduced.

The moderator must schedule an adversarial reviewer before a decisive approach/candidate conclusion is promoted downstream.

Original authors must not serve as their own independent verifier/reviewer for the same decisive result.

## 8. User-facing response format

Every moderator recommendation should use this compact structure:

```text
Campaign: CMP-XXXX — <title>
Current state: <short summary>

Start now:
- WRK-XXXX — <agent> — <task>
  Why now: <unresolved node + prerequisites satisfied>
- WRK-YYYY — <agent> — <task>
  Why now: ...

Can run in parallel: yes/no
Reason: orthogonal / deliberate replication / dependency relationship

Do not start yet:
- <planned task or worker> — blocked by <dependency>

After completion:
- moderator will inspect <specific outputs/gates>

Prompt for WRK-XXXX:
<copy-ready prompt>

Prompt for WRK-YYYY:
<copy-ready prompt>
```

If no worker is justified, say so and recommend completing/pausing/rejecting the campaign instead.

## 9. Decision memory

Use stable moderator decision IDs `MOD-0001`, `MOD-0002`, ... for scheduling batches or material decisions. Store one record per decision under `orchestration/decisions/` and index it in `registry.yaml` once issue #20 is merged.

A decision record must state:
- campaign;
- repository state inspected;
- unresolved nodes;
- workers spawned/recommended;
- workers withheld and why;
- concurrency classification;
- dependencies/blockers;
- campaign stopping assessment;
- next inspection trigger.

This lets a fresh moderator reconstruct why workers were or were not launched.

## 10. Convergence test

Before spawning another batch, ask:

1. Which campaign exit criterion remains unmet?
2. What exact repository node is missing/challenged?
3. Which agent role is uniquely appropriate to address it?
4. Will the proposed worker produce an output that can change campaign state?
5. Is it ready now?
6. Is equivalent adequate work already present?
7. After this worker, what explicit gate follows?

If these cannot be answered, do not spawn the worker.

## 11. Campaign dispositions

### Completed
All mandatory exit criteria and verification/review gates are satisfied.

### Rejected
Evidence/calculation/review establishes that the approach/question fails under current project constraints. Record why more workers are not expected to change that result.

### Blocked
A required node cannot currently be resolved because of unavailable evidence/capability/dependency.

### Paused
Further work is possible but presently not justified or prioritized.

## 12. Dummy validation scenarios

The final readiness audit must test at least:
- three orthogonal ready workers in parallel;
- two independent replication workers with controlled context;
- one blocked worker withheld;
- duplicate worker rejected;
- failed worker re-scoped;
- completed research output enabling verifier/reviewer;
- campaign completed because all gates pass;
- campaign blocked/paused because no resolvable next node remains.

Use explicitly non-scientific dummy data only during bootstrap validation.