# Orchestration Registry

This directory stores durable process memory for campaigns, worker instances, and moderator decisions. Read `ORCHESTRATION_MODEL.md` first.

## Structure

```text
orchestration/
├── README.md
├── registry.yaml
├── MODERATOR_PROTOCOL.md
├── ISSUE_6_ACCEPTANCE_PROTOCOL.md
├── WORKER_TEMPLATE.md
├── CAMPAIGN_TEMPLATE.md
├── DECISION_TEMPLATE.md
├── audit-fixtures/
├── audit-runs/
├── workers/
├── campaigns/
└── decisions/
```

`ISSUE_6_ACCEPTANCE_PROTOCOL.md` is the executable multi-session bootstrap acceptance procedure. It keeps the issue-6 dummy fixture isolated from the production registry and defines how genuinely separate fresh sessions hand off through durable repository state.

## If you are the moderator

Read, in order:
1. `ORCHESTRATION_MODEL.md`;
2. this file;
3. `MODERATOR_PROTOCOL.md`;
4. `registry.yaml`;
5. relevant campaign/worker/decision records;
6. relevant accepted scientific state.

Your normal user-facing job is to answer: **what worker(s) should be started next, why, and with which complete prompt?**

For bootstrap issue #6 specifically, follow `ISSUE_6_ACCEPTANCE_PROTOCOL.md`; do not improvise a same-session substitute for its fresh-session nodes.

## Stable IDs

- Workers: `WRK-0001`, `WRK-0002`, ...
- Campaigns: `CMP-0001`, `CMP-0002`, ...
- Moderator decisions: `MOD-0001`, `MOD-0002`, ...

IDs are never reused.

## Allocation

Canonical next IDs live in `registry.yaml`. A moderator allocating IDs must update the registry and create the corresponding durable record before recommending those workers/decisions to the user.

If allocations conflict across branches, refresh against the latest accepted registry and allocate new unused IDs. Never resolve a collision by reusing an ID.

## Worker lifecycle

```text
proposed -> ready -> running -> completed
                         \-> blocked
                         \-> failed
                         \-> cancelled
                         \-> superseded
```

`ready` means prerequisites are satisfied and the worker may be launched. `running` means the user has actually started it. Terminal states remain preserved.

## Campaign lifecycle

Campaign records follow `ORCHESTRATION_MODEL.md`: proposed, active, review_pending, completed, blocked, rejected, or paused.

## Moderator decision memory

Material scheduling decisions use `MOD-*` records under `decisions/`. They preserve why workers were recommended or withheld, concurrency rationale, dependencies/blockers, stopping assessment, and the next inspection trigger.

Moderator decisions are process provenance, not scientific evidence.

## Registry rule

Every launched production worker must appear in `registry.yaml` and have a file under `workers/`. Every production campaign has a durable record under `campaigns/`. Every material production scheduling batch/stop decision has a durable `MOD-*` record.

Issue-6 audit-run session IDs and fixture IDs are deliberately separate and must not consume production IDs or enter `registry.yaml`.

A fresh moderator must be able to reconstruct what has already been attempted and why without old chat history.

## Prompt contract

Each ready worker gets a copy-ready prompt following `WORKER_TEMPLATE.md`. The prompt references authoritative repository files rather than duplicating global rules and explicitly records scope, dependencies, independence constraints, outputs, completion criteria, and handoff.

Issue-6 live-test prompts are additionally stored verbatim in the active audit-run directory before the user launches them.

## Process provenance vs scientific provenance

`WRK-*`, `CMP-*`, and `MOD-*` identify process state. Scientific evidence continues to use `CLM-*`, `CAL-*`, `REV-*`, and `CAN-*`. Process records should point to scientific IDs/files when relevant but never substitute for them.
