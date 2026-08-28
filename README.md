# QuantumGravity — Planck-Scale Gravity Lab

> **Scientific goal:**  
> *What is the closest physically realizable experiment, using established physics and current demonstrated technology, to probing gravitational physics associated with the Planck scale?*

This is a multi-session collaborative research project. The Git repository is the shared scientific memory; chat history is not authoritative.

> **Bootstrap status:** architecture, collaboration, agent roles, provenance, and orchestration semantics are defined. Substantive research remains **NO-GO** until worker-registry/prompt implementation (#19), moderator scheduling/convergence implementation (#20), and the final fresh-system readiness audit (#6) are complete.

## Authoritative project documents

- `PROJECT_RULES.md` — scientific/mathematical constraints.
- `LITERATURE_RULES.md` — source access and evidence classification.
- `REPOSITORY_ARCHITECTURE.md` — repository authority/readiness model.
- `COLLABORATION_WORKFLOW.md` — roles, handoffs, independence, reviews and branch ownership.
- `PROVENANCE_WORKFLOW.md` — stable scientific IDs, claim lifecycle, cross-links, contradiction handling.
- `ORCHESTRATION_MODEL.md` — campaigns, workers, moderator authority, dependencies, concurrency, and stopping rules.
- `agents/README.md` — canonical fresh-chat bootstrap and role selection.
- `agents/<role>.md` — role-specific operating instructions.

## Research areas

```text
definitions/   shared definitions and metrics
literature/    bibliography and assessed claims
calculations/  reproducible calculations and verification
approaches/    experimental-route research state
candidates/    developed surviving proposals
reviews/       adversarial reviews and disputes
synthesis/     comparison and final assessment
prompts/       reusable prompts; non-authoritative
papers/        local git-ignored full-text cache
agents/        fresh-chat role instructions
```

Issues #19 and #20 will add the durable `orchestration/` worker/campaign registry and moderator scheduling implementation.

## Evidence and provenance

| Code | Meaning | Final design? |
|---|---|---|
| E1 | Directly demonstrated experimental result | Yes |
| E2 | Established physical theory / derivation | Yes |
| E3 | Proposed but not demonstrated technique | Investigation only |
| E4 | Speculative / model-dependent physics | Context only |

Evidence code is separate from project verification status: `unverified`, `verified`, `challenged`, `superseded`, or `rejected`.

Stable scientific IDs use `CLM-*` for claims, `CAL-*` for calculations, `REV-*` for reviews/disputes, and `CAN-*` for candidates.

```text
open source → verified CLM → CAL → approach/candidate → independent verification/review → synthesis
```

See `PROVENANCE_WORKFLOW.md` for the exact conventions. Decisive final-design statements require verified E1/E2 inputs and a complete traceable chain.

## Collaboration and orchestration

The research roles are foundations researcher, literature scout, experimental-approach researcher, numerical verifier, adversarial reviewer, and synthesis researcher. `COLLABORATION_WORKFLOW.md` defines how those roles interact.

`ORCHESTRATION_MODEL.md` adds a process layer:

```text
campaign → moderator decision → worker specification → agent executes worker → repository handoff → moderator re-evaluates
```

An **agent** is a reusable role. A **worker** is one concrete execution of that role. A **campaign** is a bounded research objective. The **moderator** decides what worker should exist next, but is not a scientific authority.

For decisive scientific results, the original researcher must not also be the independent numerical verifier or final adversarial reviewer of that same result. Parallelism must be justified as orthogonal work or deliberate independent replication; arbitrary duplicate workers should not be launched.

## Git workflow

```text
main                 accepted shared research state
research/<topic>     approach/foundations exploratory work
literature/<topic>   source discovery and claim assessment
review/<topic>       verification, adversarial review, governance
synthesis/<topic>    integration of reviewed outputs
```

One scoped task normally owns one branch. Parallel branches may disagree. `main` is conservative accepted state.

## Start here if you are an AI research session

Before any bootstrap/research work:

1. read this README;
2. read `PROJECT_RULES.md` and `LITERATURE_RULES.md`;
3. read `REPOSITORY_ARCHITECTURE.md`, `COLLABORATION_WORKFLOW.md`, `PROVENANCE_WORKFLOW.md`, and `ORCHESTRATION_MODEL.md`;
4. if executing scientific work, select the assigned primary role and read its `agents/<role>.md` file;
5. read relevant accepted definitions;
6. inspect the assigned issue/task, branch/base, and existing files in your write area;
7. perform only the assigned role/process task and leave a repository-based handoff.

Do not rely on previous chat history. Do **not** begin substantive Planck-gravity research until bootstrap issue #6 returns GO.

## What this project does not do

- choose a winning experiment prematurely;
- fabricate citations;
- equate quantum sensitivity with sensitivity to quantum gravity;
- equate sub-Planck parameter/displacement sensitivity with probing Planck-scale physics;
- treat publication/arXiv presence as proof of assumptions;
- call a signal "too small" without quantifying the gap;
- allow speculative physics or undemonstrated technology to support final experimental designs;
- spawn workers merely to increase parallelism or worker count.