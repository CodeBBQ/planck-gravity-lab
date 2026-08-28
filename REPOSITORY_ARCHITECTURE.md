# Repository Architecture and Research-Readiness State

Status: **Bootstrap implementation complete; final fresh-system readiness audit (#6) remains the research-start gate.**

This document records the repository authority model and current architecture. It does not evaluate any Planck-gravity experimental approach.

## 1. Architectural assessment

The repository separates scientific rules, evidence, calculations, exploratory research, review, synthesis, worker roles, and orchestration state:

- `PROJECT_RULES.md` — authoritative scientific, mathematical, and epistemic constraints.
- `LITERATURE_RULES.md` — source-access and evidence-classification rules.
- `COLLABORATION_WORKFLOW.md` — role boundaries, handoffs, independence, branch ownership, review and rejection paths.
- `PROVENANCE_WORKFLOW.md` — stable scientific IDs and claim/calculation/review provenance.
- `ORCHESTRATION_MODEL.md` — campaigns, workers, moderator authority, dependencies, concurrency, and stopping rules.
- `agents/` — six reusable scientific worker-role specifications plus fresh-worker bootstrap.
- `orchestration/` — durable campaign, worker, moderator-decision memory, templates, registry, and moderator protocol.
- `definitions/`, `literature/`, `calculations/`, `approaches/`, `candidates/`, `reviews/`, `synthesis/` — scientific state from shared definitions through reviewed synthesis.
- `prompts/` — reusable non-authoritative prompt material.
- `papers/` — local git-ignored full-text cache.

No major directory reorganization is required before research. `main` is the conservative accepted shared state.

## 2. Authority model

1. Global scientific rules live in `PROJECT_RULES.md` and `LITERATURE_RULES.md`.
2. Collaboration and scientific-role independence live in `COLLABORATION_WORKFLOW.md`.
3. Scientific provenance semantics live in `PROVENANCE_WORKFLOW.md`.
4. Process orchestration semantics live in `ORCHESTRATION_MODEL.md`, `orchestration/README.md`, and `orchestration/MODERATOR_PROTOCOL.md`.
5. `definitions/`, verified `literature/claims/`, reproducible `calculations/`, reviewed `approaches/`/`candidates/`, and `reviews/` provide scientific state.
6. `synthesis/` is downstream and may not invent unsupported decisive facts.
7. `CMP-*`, `MOD-*`, and `WRK-*` are process provenance only; `CLM-*`, `CAL-*`, `REV-*`, and `CAN-*` are scientific provenance.
8. GitHub issues, prompts, and chat history may coordinate work but must not be the sole location of an essential scientific or process rule.

## 3. Fresh-session recoverability

A fresh session should recover the system from repository state alone:

| Required context | Current location |
|---|---|
| Scientific goal and research-start gate | `README.md` |
| Scientific constraints | `PROJECT_RULES.md` |
| Literature/evidence rules | `LITERATURE_RULES.md` |
| Collaboration independence | `COLLABORATION_WORKFLOW.md` |
| Scientific provenance | `PROVENANCE_WORKFLOW.md` |
| Orchestration semantics | `ORCHESTRATION_MODEL.md` |
| Moderator startup and scheduling | `orchestration/README.md`, `orchestration/MODERATOR_PROTOCOL.md` |
| Campaign/worker/decision state | `orchestration/registry.yaml`, `orchestration/{campaigns,workers,decisions}/` |
| Scientific worker roles | `agents/README.md`, `agents/*.md` |

## 4. Canonical startup paths

### Moderator / research coordinator

Follow `README.md` → moderator start path, then read the global rules, orchestration documents, registry, relevant process records, and accepted scientific state. The moderator controls process progression but is not a scientific authority.

### Worker

Follow `README.md`, the assigned `WRK-*` prompt/record, `agents/README.md`, and the assigned `agents/<role>.md`. Respect scope, dependencies, independence exclusions, branch/write scope, outputs, completion criteria, and handoff.

No prior chat history is authoritative.

## 5. Scientific data flow

```text
open source
  -> verified CLM
  -> CAL
  -> approach/candidate
  -> independent verification/review (REV)
  -> synthesis
```

Process records may point into this chain but never replace evidence.

## 6. Bootstrap implementation status

Completed and merged into `main` before issue #6:

- #2 repository architecture audit;
- #3 collaboration model;
- #4 per-agent files and fresh-worker bootstrap;
- #5 evidence/provenance hardening;
- #18 orchestration architecture;
- #19 worker/campaign registry and prompt contract;
- #20 moderator scheduling/convergence protocol;
- pre-audit top-level moderator navigation integration.

The remaining gate is #6: an end-to-end fresh-system readiness audit. Until #6 returns GO, substantive Planck-gravity research remains NO-GO.

## 7. Preserved architectural decisions

- Keep the current top-level research directories.
- Keep global rules centralized rather than copied into every prompt.
- Keep prompts non-authoritative.
- Keep `main` conservative.
- Preserve rejected, challenged, superseded, failed, and negative results rather than deleting history.
- Require independent verification/review for decisive scientific outputs.
- Use lightweight Markdown/YAML/BibTeX/Python/Git rather than a database unless scale later justifies one.

## 8. Readiness conclusion

**Architecture: ACCEPTED.**

**Bootstrap implementation: PRESENT.**

**Research readiness: NO-GO until issue #6 completes its required fresh-session end-to-end acceptance tests and records GO.**
