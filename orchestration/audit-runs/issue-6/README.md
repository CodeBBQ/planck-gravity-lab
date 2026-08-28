# Issue #6 live audit runs

This directory stores durable state for executable multi-session acceptance runs defined by `orchestration/ISSUE_6_ACCEPTANCE_PROTOCOL.md`.

Each run gets its own `<RUN-ID>/` directory containing a manifest, one record per required fresh session, verbatim launcher prompts, and durable results/handoffs.

These records are process-validation artifacts only:

- they use audit session IDs such as `S0`, `S1-LIT`, and `S4-FINAL` rather than production `WRK-*`/`MOD-*` allocations;
- they do not enter `orchestration/registry.yaml`;
- they do not constitute scientific evidence;
- they must contain only the non-scientific issue-6 fixture material;
- they preserve failed, invalid, blocked, and superseded attempts rather than overwriting them.

The current run manifest is the launcher-facing state machine. It must always name the exact next prompt(s) that may be launched, or a terminal state. The user should not have to infer or design the next audit worker.
