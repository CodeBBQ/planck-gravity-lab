# QuantumGravity — Planck-Scale Gravity Lab

> **Scientific goal:**  
> *What is the closest physically realizable experiment, using established physics and current demonstrated technology, to probing gravitational physics associated with the Planck scale?*

This is a multi-session collaborative research project. The Git repository is the shared scientific memory; chat history is not authoritative.

> **Bootstrap status:** architecture, collaboration, per-agent instructions, and provenance mechanics are defined. Substantive research remains **NO-GO** only until the fresh-agent readiness audit (#6) returns GO.

## Authoritative project documents

- `PROJECT_RULES.md` — scientific/mathematical constraints.
- `LITERATURE_RULES.md` — source access and evidence classification.
- `REPOSITORY_ARCHITECTURE.md` — repository authority/readiness model.
- `COLLABORATION_WORKFLOW.md` — roles, handoffs, independence, reviews and branch ownership.
- `PROVENANCE_WORKFLOW.md` — stable IDs, claim lifecycle, cross-links, contradiction handling.
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

## Evidence and provenance

| Code | Meaning | Final design? |
|---|---|---|
| E1 | Directly demonstrated experimental result | Yes |
| E2 | Established physical theory / derivation | Yes |
| E3 | Proposed but not demonstrated technique | Investigation only |
| E4 | Speculative / model-dependent physics | Context only |

Evidence code is separate from project verification status: `unverified`, `verified`, `challenged`, `superseded`, or `rejected`.

Stable IDs use `CLM-*` for claims, `CAL-*` for calculations, `REV-*` for reviews/disputes, and `CAN-*` for candidates.

```text
open source → verified CLM → CAL → approach/candidate → independent verification/review → synthesis
```

See `PROVENANCE_WORKFLOW.md` for the exact conventions. Decisive final-design statements require verified E1/E2 inputs and a complete traceable chain.

## Collaboration

The roles are foundations researcher, literature scout, experimental-approach researcher, numerical verifier, adversarial reviewer, and synthesis researcher. See `COLLABORATION_WORKFLOW.md` and `agents/README.md`.

For decisive scientific results, the original researcher must not also be the independent numerical verifier or final adversarial reviewer of that same result. Negative and rejected results are valid preserved outputs.

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

The canonical startup protocol is `agents/README.md`. Before work:

1. read this README;
2. read `PROJECT_RULES.md` and `LITERATURE_RULES.md`;
3. read `REPOSITORY_ARCHITECTURE.md`, `COLLABORATION_WORKFLOW.md`, and `PROVENANCE_WORKFLOW.md`;
4. select the assigned primary role and read its `agents/<role>.md` file;
5. read relevant accepted definitions;
6. inspect the assigned issue/task, branch/base, and existing files in your write area;
7. perform only the assigned role and leave a repository-based handoff.

Do not rely on previous chat history. Do **not** begin substantive Planck-gravity research until bootstrap issue #6 returns GO.

## What this project does not do

- choose a winning experiment prematurely;
- fabricate citations;
- equate quantum sensitivity with sensitivity to quantum gravity;
- equate sub-Planck parameter/displacement sensitivity with probing Planck-scale physics;
- treat publication/arXiv presence as proof of assumptions;
- call a signal "too small" without quantifying the gap;
- allow speculative physics or undemonstrated technology to support final experimental designs.