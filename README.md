# QuantumGravity — Planck-Scale Gravity Lab

> **Scientific goal:**  
> *What is the closest physically realizable experiment, using established physics and current demonstrated technology, to probing gravitational physics associated with the Planck scale?*

This is a multi-session collaborative research project. The Git repository is the shared scientific memory; chat history is not authoritative.

> **Bootstrap status:** repository architecture, collaboration, agent roles, provenance, worker/campaign memory, and moderator scheduling are implemented. Substantive research remains **NO-GO** until the final fresh-system readiness audit (#6) returns GO.

## Authoritative project documents

- `PROJECT_RULES.md` — scientific/mathematical constraints.
- `LITERATURE_RULES.md` — source access and evidence classification.
- `REPOSITORY_ARCHITECTURE.md` — repository authority/readiness model.
- `COLLABORATION_WORKFLOW.md` — roles, handoffs, independence, reviews and branch ownership.
- `PROVENANCE_WORKFLOW.md` — stable scientific IDs, claim lifecycle, cross-links, contradiction handling.
- `ORCHESTRATION_MODEL.md` — campaigns, workers, moderator authority, dependencies, concurrency, and stopping rules.
- `orchestration/README.md` — durable campaign/worker/decision memory and IDs.
- `orchestration/MODERATOR_PROTOCOL.md` — how a fresh moderator decides which workers to start next and generates their prompts.
- `agents/README.md` — canonical worker-role bootstrap and role selection.
- `agents/<role>.md` — role-specific operating instructions.

## Research areas

```text
definitions/     shared definitions and metrics
literature/      bibliography and assessed claims
calculations/    reproducible calculations and verification
approaches/      experimental-route research state
candidates/      developed surviving proposals
reviews/         adversarial reviews and disputes
synthesis/       comparison and final assessment
agents/          reusable worker-role instructions
orchestration/   campaigns, workers, moderator decisions and prompts
prompts/         reusable non-authoritative prompt material
papers/          local git-ignored full-text cache
```

## Evidence and provenance

| Code | Meaning | Final design? |
|---|---|---|
| E1 | Directly demonstrated experimental result | Yes |
| E2 | Established physical theory / derivation | Yes |
| E3 | Proposed but not demonstrated technique | Investigation only |
| E4 | Speculative / model-dependent physics | Context only |

Evidence code is separate from project verification status: `unverified`, `verified`, `challenged`, `superseded`, or `rejected`.

Stable scientific IDs use `CLM-*` for claims, `CAL-*` for calculations, `REV-*` for reviews/disputes, and `CAN-*` for candidates. Process IDs use `CMP-*`, `WRK-*`, and `MOD-*`.

```text
open source → verified CLM → CAL → approach/candidate → independent verification/review → synthesis
```

Worker/campaign/decision records point into this scientific provenance chain but are not scientific evidence themselves.

## Collaboration and orchestration

The research roles are foundations researcher, literature scout, experimental-approach researcher, numerical verifier, adversarial reviewer, and synthesis researcher. `COLLABORATION_WORKFLOW.md` defines role interaction.

The user-facing research loop is:

```text
user asks what to run next
  → moderator reads repository state
  → moderator allocates justified WRK IDs and copy-ready prompts
  → user starts those fresh worker chats
  → workers commit durable outputs + handoffs
  → moderator re-reads repository state
  → next workers / verification / review / campaign stop
```

An **agent** is a reusable role. A **worker** is one concrete execution of that role. A **campaign** is a bounded research objective. The **moderator** controls process progression but is not a scientific authority.

For decisive scientific results, the original researcher must not also be the independent numerical verifier or final adversarial reviewer of that result. Parallelism must be justified as orthogonal work or deliberate independent replication.

## Git workflow

```text
main                 accepted shared research/process state
research/<topic>     approach/foundations exploratory work
literature/<topic>   source discovery and claim assessment
review/<topic>       verification, adversarial review, governance
synthesis/<topic>    integration of reviewed outputs
```

One scoped worker/task normally owns one branch. Parallel branches may disagree. `main` is conservative accepted state.

## Start here

### If you are the moderator / coordinator

1. Read this README.
2. Read `PROJECT_RULES.md`, `LITERATURE_RULES.md`, `REPOSITORY_ARCHITECTURE.md`, `COLLABORATION_WORKFLOW.md`, `PROVENANCE_WORKFLOW.md`, and `ORCHESTRATION_MODEL.md`.
3. Read `orchestration/README.md`, `orchestration/MODERATOR_PROTOCOL.md`, and `orchestration/registry.yaml`.
4. Read the relevant campaign, worker, decision, and accepted scientific records.
5. Decide what workers are justified next, persist process records, and give the user copy-ready prompts.

### If you are executing a worker

1. Read this README and the files required by your `WRK-*` record/prompt.
2. Read `agents/README.md` and the assigned `agents/<role>.md`.
3. Respect the worker's scope, dependencies, independence restrictions, branch/write scope, completion criteria, and handoff.
4. Write durable outputs; do not rely on previous chat history.

Do **not** begin substantive Planck-gravity research until bootstrap issue #6 returns GO.

## What this project does not do

- choose a winning experiment prematurely;
- fabricate citations;
- equate quantum sensitivity with sensitivity to quantum gravity;
- equate sub-Planck parameter/displacement sensitivity with probing Planck-scale physics;
- treat publication/arXiv presence as proof of assumptions;
- call a signal "too small" without quantifying the gap;
- allow speculative physics or undemonstrated technology to support final experimental designs;
- spawn workers merely to increase parallelism or worker count.