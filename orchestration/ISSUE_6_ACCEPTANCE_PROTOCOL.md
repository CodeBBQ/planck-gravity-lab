# Issue #6 Multi-Session Acceptance Protocol

This protocol defines the executable acceptance procedure for bootstrap issue #6. It exists because a single chat/session cannot truthfully satisfy acceptance requirements that explicitly require genuinely separate fresh worker and moderator sessions.

The protocol does **not** weaken independence. Instead, it turns the audit into a finite graph of separate sessions whose only shared memory is durable repository state.

No substantive Planck-gravity research may be performed. Use only the isolated non-scientific fixture under `orchestration/audit-fixtures/issue-6/`.

## 1. Authority and scope

For issue #6 acceptance, the authoritative inputs are:

1. accepted `main`;
2. issue #6;
3. this protocol;
4. durable audit-run records created under `orchestration/audit-runs/issue-6/`;
5. the isolated issue-6 dummy fixture.

Chat history is never an input to another session.

The user acts only as a **launcher**: copy the exact prompt named by the current audit-run state into a new fresh chat/session. The user must not design workers, dependencies, role assignments, contamination controls, or stopping conditions.

## 2. Session classes

A valid audit run uses the following distinct fresh sessions.

### S0 — Audit initializer

Purpose:
- bootstrap from `README.md` and issue #6;
- pin the accepted `main` SHA being audited;
- inspect repository consistency and the dummy fixture;
- create the durable audit-run manifest;
- create the exact prompts for the first worker batch;
- make no final GO/NO-GO decision.

S0 may perform the repository/static parts of Phases 1-3 and 10, but it may not substitute for later live cross-session tests.

### S1-LIT — Literature-scout worker

Fresh worker session using only its generated prompt and repository access.

### S1-APP — Approach-researcher worker

Fresh worker session using only its generated prompt and repository access.

### S1-FND — Foundations-researcher worker

Fresh worker session using only its generated prompt and repository access.

### S1-NV-A and S1-NV-B — Independent numerical-replication workers

Two separate fresh worker sessions addressing the same decisive dummy arithmetic.

They are deliberate independent replications. Each must exclude the other replication worker's branch, result, arithmetic, and conclusion until both first-pass handoffs are durable.

### S2-MOD — Replacement moderator

A genuinely fresh moderator session with repository access only. It must reconstruct the audit state from durable records, ingest completed worker handoffs, verify that completed work is not repeated, classify any failures, and create the next `MOD-*`-style audit decision for the fixture.

The expected next enabled live role is the adversarial reviewer when the decisive dummy result is sufficiently available. The moderator decides this from repository state; the user does not.

### S3-REV — Adversarial-review worker

A genuinely fresh adversarial-review worker session launched only if S2-MOD marks it ready and emits its exact prompt.

The original author(s) and numerical replicators may not serve as this reviewer.

### S3-SYN — Synthesis bootstrap worker

A genuinely fresh synthesis worker session launched only after the moderator marks the synthesis node ready. Its task is limited to the dummy fixture and verifies that the synthesis role resolves its dependencies, accepted inputs, unresolved evidence, and handoff correctly.

If the synthesis node remains blocked because review or verification has not passed, the protocol records that fact instead of launching S3-SYN early.

### S4-FINAL — Final acceptance adjudicator

A final fresh session, distinct from S0, every worker, and S2-MOD.

It reads accepted repository state plus the complete durable audit-run record and determines final GO/NO-GO for issue #6.

Only S4-FINAL may write the final issue-6 acceptance verdict to `RESEARCH_READINESS.md`.

## 3. Required order and allowed parallelism

The session graph is:

```text
S0 initializer
   |
   +--> S1-LIT ----+
   +--> S1-APP ----+
   +--> S1-FND ----+----> S2-MOD replacement moderator
   +--> S1-NV-A --+
   +--> S1-NV-B --+
                         |
                         +--> S3-REV (when ready)
                         |
                         +--> S3-SYN (only when synthesis prerequisites are ready)
                         |
                         +--> any explicitly justified failure/re-scope worker required by the fixture
                         |
                         +--> S4-FINAL adjudicator
```

`S1-LIT`, `S1-APP`, `S1-FND`, `S1-NV-A`, and `S1-NV-B` may run in parallel after S0 has created their durable records and prompts.

No S1 worker may depend on another S1 worker's fresh-session output.

S2-MOD must not start until the S1 batch has reached durable terminal states sufficient for re-entry evaluation. A failed worker may be terminal if the failure itself is the intended audit input and is durably classified.

S3-REV is sequential because it depends on the decisive dummy output and verification state.

S3-SYN is sequential and may run only after its fixture dependencies are satisfied.

S4-FINAL runs last.

## 4. Audit-run durable state

S0 creates one directory:

```text
orchestration/audit-runs/issue-6/<RUN-ID>/
```

Use a collision-resistant human-readable run ID such as:

```text
RUN-2026-08-28-A
```

The run directory contains at minimum:

```text
manifest.md
sessions/
  S0-initializer.md
  S1-LIT.md
  S1-APP.md
  S1-FND.md
  S1-NV-A.md
  S1-NV-B.md
  S2-MOD.md
  S3-REV.md
  S3-SYN.md
  S4-FINAL.md
prompts/
  S1-LIT.txt
  S1-APP.txt
  S1-FND.txt
  S1-NV-A.txt
  S1-NV-B.txt
  S2-MOD.txt
  S3-REV.txt        # created when/if enabled
  S3-SYN.txt        # created when/if enabled
  S4-FINAL.txt      # created only after live protocol prerequisites are complete
results/
  ...
```

The audit-run records are process-validation artifacts only. They do not consume or modify production `CMP-*`, `WRK-*`, or `MOD-*` IDs and must not enter the production registry.

### `manifest.md` minimum fields

- run ID;
- issue number;
- audited `main` SHA;
- protocol version/source commit;
- fixture path;
- overall state: `initialized | worker_batch_running | moderator_reentry_ready | followup_running | final_adjudication_ready | GO | NO-GO | BLOCKED`;
- required sessions and their state;
- allowed parallelism;
- contamination restrictions;
- explicit next launcher action;
- termination condition;
- links/paths to all session records and prompts.

### Session-state vocabulary

Each session record uses:

```text
planned -> ready -> launched -> completed
                       \-> failed
                       \-> blocked
                       \-> invalid
                       \-> superseded
```

`invalid` means the session violated an acceptance constraint, for example by using prohibited sibling context or by simulating another required fresh session inside itself.

## 5. Prompt rule

Every prompt given to the user must be stored verbatim under the active audit-run `prompts/` directory before the user is told to launch it.

The user should never have to construct or edit a role prompt.

A minimal prompt may reference the repository and one durable session record. Global rules should be discovered through repository startup rather than duplicated into chat text.

## 6. Exact minimal prompt templates

S0 must instantiate these templates with the current `<RUN-ID>` and branch/write target.

### First batch: S1-LIT

```text
Work on issue #6 in the CodeBBQ/planck-gravity-lab repository as the fresh audit session identified by `orchestration/audit-runs/issue-6/<RUN-ID>/sessions/S1-LIT.md`.

Use only the repository, issue #6, and that durable session record as context. Follow the repository startup and worker instructions. Execute only the non-scientific issue-6 dummy fixture task assigned there, persist the required result and handoff, commit your changes on the branch specified by the session record, and do not perform substantive Planck-gravity research.
```

### First batch: S1-APP

```text
Work on issue #6 in the CodeBBQ/planck-gravity-lab repository as the fresh audit session identified by `orchestration/audit-runs/issue-6/<RUN-ID>/sessions/S1-APP.md`.

Use only the repository, issue #6, and that durable session record as context. Follow the repository startup and worker instructions. Execute only the non-scientific issue-6 dummy fixture task assigned there, persist the required result and handoff, commit your changes on the branch specified by the session record, and do not perform substantive Planck-gravity research.
```

### First batch: S1-FND

```text
Work on issue #6 in the CodeBBQ/planck-gravity-lab repository as the fresh audit session identified by `orchestration/audit-runs/issue-6/<RUN-ID>/sessions/S1-FND.md`.

Use only the repository, issue #6, and that durable session record as context. Follow the repository startup and worker instructions. Execute only the non-scientific issue-6 dummy fixture task assigned there, persist the required result and handoff, commit your changes on the branch specified by the session record, and do not perform substantive Planck-gravity research.
```

### First batch: S1-NV-A

```text
Work on issue #6 in the CodeBBQ/planck-gravity-lab repository as the fresh audit session identified by `orchestration/audit-runs/issue-6/<RUN-ID>/sessions/S1-NV-A.md`.

Use only the repository, issue #6, and that durable session record as context. Follow the repository startup and worker instructions. Execute only the non-scientific issue-6 dummy fixture task assigned there, preserve the stated replication/contamination exclusions, persist the required result and handoff, commit your changes on the branch specified by the session record, and do not perform substantive Planck-gravity research.
```

### First batch: S1-NV-B

```text
Work on issue #6 in the CodeBBQ/planck-gravity-lab repository as the fresh audit session identified by `orchestration/audit-runs/issue-6/<RUN-ID>/sessions/S1-NV-B.md`.

Use only the repository, issue #6, and that durable session record as context. Follow the repository startup and worker instructions. Execute only the non-scientific issue-6 dummy fixture task assigned there, preserve the stated replication/contamination exclusions, persist the required result and handoff, commit your changes on the branch specified by the session record, and do not perform substantive Planck-gravity research.
```

### Replacement moderator: S2-MOD

```text
Work on issue #6 in the CodeBBQ/planck-gravity-lab repository as the fresh replacement-moderator audit session identified by `orchestration/audit-runs/issue-6/<RUN-ID>/sessions/S2-MOD.md`.

Use only the repository, issue #6, and that durable session record as context. Follow the repository moderator startup path. Reconstruct the audit/fixture state from durable repository records, perform the assigned re-entry and scheduling checks, persist the next audit decision and any newly enabled exact worker prompt(s), commit changes on the branch specified by the session record, and do not perform substantive Planck-gravity research.
```

### Adversarial reviewer: S3-REV

S2-MOD writes the exact prompt using this minimal form only if the reviewer is ready:

```text
Work on issue #6 in the CodeBBQ/planck-gravity-lab repository as the fresh audit session identified by `orchestration/audit-runs/issue-6/<RUN-ID>/sessions/S3-REV.md`.

Use only the repository, issue #6, and that durable session record as context. Follow the repository startup and worker instructions. Execute only the non-scientific issue-6 dummy fixture review assigned there, preserve all independence restrictions, persist the required result and handoff, commit changes on the branch specified by the session record, and do not perform substantive Planck-gravity research.
```

### Synthesis bootstrap: S3-SYN

S2-MOD or a later valid moderator decision writes the exact prompt only when ready:

```text
Work on issue #6 in the CodeBBQ/planck-gravity-lab repository as the fresh audit session identified by `orchestration/audit-runs/issue-6/<RUN-ID>/sessions/S3-SYN.md`.

Use only the repository, issue #6, and that durable session record as context. Follow the repository startup and worker instructions. Execute only the non-scientific issue-6 dummy fixture synthesis/bootstrap task assigned there, use only dependency-approved durable inputs, persist the required result and handoff, commit changes on the branch specified by the session record, and do not perform substantive Planck-gravity research.
```

### Final adjudicator: S4-FINAL

The exact prompt is emitted only after the run reaches `final_adjudication_ready`:

```text
Work on issue #6 in the CodeBBQ/planck-gravity-lab repository as the fresh final acceptance session identified by `orchestration/audit-runs/issue-6/<RUN-ID>/sessions/S4-FINAL.md`.

Use only the repository, issue #6, and that durable session record as context. Follow the repository startup path, inspect the complete durable multi-session audit run, determine whether every required acceptance condition was actually executed with the required independence, update `RESEARCH_READINESS.md` with the audited main SHA and final GO/NO-GO, commit the result on the branch specified by the session record, and do not perform substantive Planck-gravity research.
```

## 7. Branch and incorporation rule

Each live fresh session must write to its own audit branch unless its session record explicitly declares an isolated shared integration branch safe for that task.

Default branch names:

```text
review/issue-6-<RUN-ID>-s1-lit
review/issue-6-<RUN-ID>-s1-app
review/issue-6-<RUN-ID>-s1-fnd
review/issue-6-<RUN-ID>-s1-nv-a
review/issue-6-<RUN-ID>-s1-nv-b
review/issue-6-<RUN-ID>-s2-mod
review/issue-6-<RUN-ID>-s3-rev
review/issue-6-<RUN-ID>-s3-syn
review/issue-6-<RUN-ID>-s4-final
```

The session record must define what accepted baseline to start from and how its result is incorporated.

A moderator/adjudicator must not infer a completed live test from an unmerged branch it cannot trace. Before a dependent session is marked `ready`, the prerequisite result must be durably incorporated into the audit integration state by merge/cherry-pick-equivalent accepted repository history or by another repository-native mechanism explicitly recorded in the manifest.

The incorporation step is process bookkeeping, not scientific acceptance.

## 8. Independence requirements

The following are mandatory:

1. Every listed session is a genuinely separate fresh chat/session.
2. No session receives prior-chat summaries as hidden context.
3. The user copies only the exact repository-generated prompt for that session.
4. S1-NV-A and S1-NV-B do not inspect each other's first-pass work before both are durably complete.
5. S2-MOD is not one of the S1 workers and must reconstruct state from Git.
6. S3-REV is not an author or numerical replicator of the decisive dummy output.
7. S4-FINAL is not S0, S2-MOD, or any worker session.
8. Same-session simulation of any required fresh session is invalid and cannot be marked PASS.
9. A session that violates contamination rules is marked `invalid`; the affected acceptance test must be rerun in a new fresh session after correcting durable protocol state.

## 9. Phase mapping

The original acceptance intent is preserved as follows.

- Phase 1: S0 live fresh bootstrap.
- Phase 2: S0 creates/validates the dummy audit campaign state and first decision in the isolated fixture/run.
- Phase 3: S0 proves the initial batch contains orthogonal parallelism, deliberate replication, a blocked dependency, and duplicate suppression.
- Phase 4: S1-LIT, S1-APP, S1-NV-A/B, S3-REV are live fresh worker executions; S1-FND and S3-SYN provide live foundations/synthesis bootstrap coverage.
- Phase 5: S2-MOD is the live fresh replacement-moderator re-entry test.
- Phase 6: S2-MOD classifies any intentionally injected failed/re-scoped dummy case; if a replacement worker must be executed to prove the path, it emits a new fresh-session prompt and the run waits for it.
- Phase 7: S1-NV-A/B plus S3-REV demonstrate verification/review independence.
- Phase 8: S2-MOD and S4-FINAL verify stopping/convergence from durable state; the fixture must exercise both completed and blocked terminal scenarios.
- Phase 9: live workers/verifier/reviewer/synthesis demonstrate that process records point to but do not substitute for dummy scientific-provenance placeholders.
- Phase 10: S0 and S4-FINAL perform cross-system consistency checks against the pinned accepted baseline and the completed audit run.

## 10. Failure, retry, and rerun rules

A live session can end in `failed`, `blocked`, or `invalid` without making the audit loop indefinitely.

- Environment/process failure: S2-MOD or S4-FINAL records whether a retry is justified and exactly what changed.
- Missing dependency: do not retry; wait for the dependency or terminate `BLOCKED` if the dependency cannot be satisfied.
- Ambiguous/over-broad session contract: fix the durable protocol/session record, supersede the bad session, and rerun only the affected acceptance node in a new fresh session.
- Unavailable dummy input: terminate the affected fixture path as `BLOCKED` if that is the intended stopping test.
- Valid negative dummy result: preserve it as completed; do not rerun seeking a preferred outcome.
- Independence violation: mark the session `invalid` and rerun the affected node in a genuinely new fresh session.

A corrected rerun receives a new session attempt suffix, for example `S1-NV-A.2`; prior attempts remain preserved.

## 11. Termination and anti-loop rule

The audit must never return NO-GO merely because the current chat cannot create another chat.

Instead, a session that has completed its assigned node must leave one of these durable outcomes:

- `NEXT_SESSION_REQUIRED` — with exactly one or more repository-generated prompt files that the user can launch now;
- `WAITING_FOR_INCORPORATION` — prerequisite branch/result must be merged/incorporated before launching the next prompt;
- `FINAL_ADJUDICATION_READY` — all live prerequisites complete; launch S4-FINAL;
- `TERMINAL_NO_GO` — a repository/protocol defect or unsatisfied independence requirement remains after permitted targeted rerun;
- `TERMINAL_GO` — written only by S4-FINAL.

The user-facing response from any non-final session should therefore end with the exact next prompt(s), not with a generic NO-GO caused by inability to instantiate child chats.

The run terminates when S4-FINAL records `GO` or `NO-GO` in both the audit manifest and `RESEARCH_READINESS.md`.

## 12. GO criterion

S4-FINAL may declare **GO** only if all of the following are true:

- S0 successfully bootstrapped from repository + issue #6 without hidden context;
- the audit run pinned an accepted `main` SHA;
- the initial worker batch was repository-generated and justified;
- the required fresh worker sessions actually ran;
- independent replication contamination controls were preserved;
- a genuinely fresh replacement moderator reconstructed durable state and scheduled the next justified work without user DAG design;
- the fresh adversarial-review path ran with author independence;
- foundations and synthesis bootstrap were live-tested sufficiently to resolve their worker contracts;
- failure/re-scope, duplicate suppression, blocked dependency, convergence, and stopping behavior were demonstrated through durable fixture state;
- process/scientific provenance separation remained intact;
- no required session needed old chat context;
- no required independence test was replaced by same-session simulation;
- the user acted only as launcher of exact prompts generated by repository state.

Otherwise S4-FINAL records a specific **NO-GO** reason and identifies the smallest affected node that must be corrected/rerun.

## 13. User launcher experience

At any point, the user should need to do only this:

1. open the current audit-run manifest;
2. copy the exact prompt(s) listed under `Next launcher action`;
3. start each in a genuinely fresh chat;
4. after those sessions commit their durable outputs, return to the manifest or the repository-generated next prompt.

The user must never be asked to decide which research/audit role should run next.
