# Orchestration Registry

This directory stores durable process memory for campaigns and worker instances. Read `ORCHESTRATION_MODEL.md` before using it.

## Structure

```text
orchestration/
├── README.md
├── registry.yaml
├── WORKER_TEMPLATE.md
├── CAMPAIGN_TEMPLATE.md
├── workers/
└── campaigns/
```

## Stable IDs

- Workers: `WRK-0001`, `WRK-0002`, ...
- Campaigns: `CMP-0001`, `CMP-0002`, ...

IDs are never reused.

## Allocation

The canonical next IDs live in `registry.yaml`. A moderator allocating IDs must update the registry and create the corresponding durable record in the same branch/task before recommending those workers to the user.

If multiple moderators could allocate concurrently, only one allocation branch may be merged as authoritative. On conflict, rebase/refresh against the latest registry and allocate new unused IDs. Never resolve collisions by reusing an already-recorded ID.

## Worker lifecycle

```text
proposed -> ready -> running -> completed
                         \-> blocked
                         \-> failed
                         \-> cancelled
                         \-> superseded
```

`ready` means prerequisites are satisfied and the worker may be launched. `running` means the user has actually started it. Terminal states must preserve the record.

## Campaign lifecycle

Campaign records follow `ORCHESTRATION_MODEL.md`: proposed, active, review_pending, completed, blocked, rejected, or paused.

## Registry rule

Every launched worker must appear in `registry.yaml` and have a file under `workers/`. The registry is an index; the worker file is the detailed durable record.

A fresh moderator must be able to determine what has already been attempted without reading old chat history.

## Prompt contract

Each worker record contains or generates a copy-ready prompt following `WORKER_TEMPLATE.md`. The prompt references authoritative repository files rather than duplicating global rules.

## Process provenance vs scientific provenance

`WRK-*` and `CMP-*` identify process executions. Scientific evidence continues to use `CLM-*`, `CAL-*`, `REV-*`, and `CAN-*`. Worker records should point to those IDs and files when they create or use them.