# QuantumGravity — Planck-Scale Gravity Lab

> **Scientific goal:**  
> *What is the closest physically realizable experiment, using established physics
> and current demonstrated technology, to probing gravitational physics associated
> with the Planck scale?*

This is a **multi-session collaborative research project**.  
The Git repository is the shared scientific memory.  
No chat history is preserved between sessions — everything authoritative must live here.

> **Bootstrap status:** repository architecture and the collaboration model are accepted, but substantive research is **NO-GO** until per-agent instructions, provenance workflow, and the fresh-agent readiness audit are complete. See `REPOSITORY_ARCHITECTURE.md` and `COLLABORATION_WORKFLOW.md`.

---

## Non-speculative constraint

Every conclusion in this repository must be traceable to:

- established physics (textbook or directly replicated experiment), **or**
- demonstrated experimental capability (a real instrument has achieved it).

Speculation and model-dependent assumptions may be explored but must be
**explicitly labelled** (evidence code E3 or E4) and must never appear in final
experimental designs. See `PROJECT_RULES.md` and `LITERATURE_RULES.md`.

---

## Repository architecture

See `REPOSITORY_ARCHITECTURE.md` for the audited authority model, data flow, bootstrap status, and unresolved pre-research decisions.

```text
planck-gravity-lab/
│
├── README.md                  ← you are here
├── PROJECT_RULES.md           ← mandatory scientific rules
├── LITERATURE_RULES.md        ← source and evidence rules
├── REPOSITORY_ARCHITECTURE.md ← audited structure and authority model
├── COLLABORATION_WORKFLOW.md  ← role boundaries, handoffs, independence and reviews
│
├── definitions/               ← shared vocabulary and mathematical definitions
├── literature/                ← bibliography and assessed claims
├── calculations/              ← reproducible numerical calculations
├── approaches/                ← experimental-route research state
├── candidates/                ← developed experimental proposals
├── reviews/                   ← adversarial reviews and disputes
├── synthesis/                 ← comparison and final assessment
├── prompts/                   ← reusable prompts; not authoritative research memory
└── papers/                    ← local PDF storage (git-ignored; use arXiv/DOI)
```

The planned `agents/` area is intentionally deferred to bootstrap issue #4, which converts the accepted collaboration model into role-specific startup instructions.

---

## Evidence hierarchy

| Code | Meaning | May appear in final design? |
|------|---------|----------------------------|
| E1 | Directly demonstrated experimental result | Yes |
| E2 | Established physical theory / derivation | Yes |
| E3 | Proposed but not demonstrated technique | Investigation only |
| E4 | Speculative / model-dependent physics | Context only |

See `LITERATURE_RULES.md` for the full claim record format.

---

## Provenance chain

```text
claim
  ↓  (evidence code + source)
derivation / calculation   (calculations/)
  ↓
approach                   (approaches/)
  ↓
candidate experiment       (candidates/)
  ↓
review / verification      (reviews/ + calculations/)
  ↓
synthesis                  (synthesis/)
```

Every decisive quantitative result must be traceable back to source evidence. Bootstrap issue #5 will harden identifiers, verification states, contradiction handling, and cross-links.

---

## Collaboration workflow

`COLLABORATION_WORKFLOW.md` is authoritative for how independent chats work together.

### Roles

| Role | Primary responsibility |
|------|------------------------|
| Foundations researcher | Definitions, physical distinctions, shared metrics |
| Literature scout | Open sources and assessed evidence claims |
| Experimental approach researcher | Quantitative analysis of one experimental route |
| Numerical verifier | Independent reproduction of decisive calculations |
| Adversarial reviewer | Attempts to falsify or weaken research conclusions |
| Synthesis researcher | Integrates sufficiently reviewed results |

For decisive scientific results, the original researcher must not also act as the independent numerical verifier or final adversarial reviewer of that same result.

### Default handoff flow

```text
Foundations
    ↓
Literature / evidence
    ↓
Approach research ↔ Numerical verification
    ↓
Adversarial review
    ├── rejected/unresolved → preserved in research + reviews
    ↓
Candidate experiment
    ↓
Candidate review / verification
    ↓
Synthesis
```

The flow is iterative. Negative results and rejected approaches remain valid scientific outputs.

---

## Git workflow

### Branch naming

```text
main                    ← accepted shared research state
research/<topic>        ← approach/foundations exploratory work
literature/<topic>      ← source discovery and claim assessment
review/<topic>          ← numerical/adversarial verification or governance review
synthesis/<topic>       ← integration of accepted outputs
```

One scoped task should normally own one branch. Parallel branches may disagree; `main` is not an exploration scratchpad.

### Merging into main

For substantive scientific work, merge requirements depend on work type and are defined in `COLLABORATION_WORKFLOW.md`. At minimum:

- claims must respect evidence/access rules,
- important equations must be dimensionally checked,
- decisive numerical results require independent verification before supporting a final candidate,
- unresolved disputes must remain explicit,
- E3/E4 assumptions cannot support final experimental designs,
- synthesis cannot introduce unsupported decisive facts directly.

---

## Start here if you are an AI research session

During the bootstrap phase, read these files **before** doing any assigned work:

1. `README.md` (this file)
2. `PROJECT_RULES.md`
3. `LITERATURE_RULES.md`
4. `REPOSITORY_ARCHITECTURE.md`
5. `COLLABORATION_WORKFLOW.md`
6. `definitions/README.md`
7. relevant currently accepted files in `definitions/`
8. the GitHub issue defining your task
9. all existing files in the repository area your task may modify

After bootstrap issue #4, the canonical startup list will additionally require the selected per-agent instruction file.

Do **not** begin substantive Planck-gravity research until the final fresh-agent readiness audit in bootstrap issue #6 returns GO.

---

## What this project does NOT do

- It does not choose a winning experiment prematurely.
- It does not fabricate citations or invent plausible-sounding references.
- It does not assume that quantum sensitivity implies sensitivity to quantum gravity.
- It does not treat an arXiv preprint as establishing the correctness of its own assumptions.
- It does not conclude that a signal is "too small" without quantifying the gap.
- It does not rely on previous chat history for authoritative scientific or workflow context.
