# QuantumGravity — Planck-Scale Gravity Lab

> **Scientific goal:**  
> *What is the closest physically realizable experiment, using established physics
> and current demonstrated technology, to probing gravitational physics associated
> with the Planck scale?*

This is a **multi-session collaborative research project**.  
The Git repository is the shared scientific memory.  
No chat history is preserved between sessions — everything authoritative must live here.

> **Bootstrap status:** repository architecture is accepted, but substantive research is **NO-GO** until the collaboration model, per-agent instructions, provenance workflow, and fresh-agent readiness audit are complete. See `REPOSITORY_ARCHITECTURE.md`.

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
├── PROJECT_RULES.md           ← mandatory rules for every session
├── LITERATURE_RULES.md        ← source and citation rules
├── REPOSITORY_ARCHITECTURE.md ← audited structure, authority and readiness state
│
├── definitions/               ← shared vocabulary and mathematical definitions
│   ├── README.md
│   ├── planck_scales.md       ← Planck units: derivations and numerical values
│   ├── what_counts_as_probe.md← what does "probing Planck-scale physics" mean?
│   └── common_metrics.md      ← how to quantify "proximity to Planck scale"
│
├── literature/                ← bibliography and assessed claims
│   ├── README.md
│   ├── library.bib            ← BibTeX database
│   ├── reading_queue.md       ← papers to be read and assessed
│   └── claims/                ← structured claim records
│       └── README.md
│
├── approaches/                ← research templates for experimental approaches
│   ├── README.md
│   ├── accelerators.md
│   ├── atom_interferometry.md
│   ├── optical_interferometry.md
│   ├── short_range_gravity.md
│   ├── mechanical_sensors.md
│   ├── clocks.md
│   ├── quantum_gravity_experiments.md
│   ├── astrophysical_baselines.md
│   └── strong_gravity.md
│
├── candidates/                ← fully developed experimental proposals
│   ├── README.md
│   └── TEMPLATE.md            ← required structure for a candidate experiment
│
├── reviews/                   ← adversarial reviews and checks
│   ├── README.md
│   ├── adversarial_review.md
│   └── dimensional_checks.md
│
├── calculations/              ← reproducible numerical calculations
│   ├── README.md
│   ├── constants.py
│   ├── scaling_relations.py
│   └── test_calculations.py
│
├── synthesis/                 ← comparison and final assessment
│   ├── README.md
│   ├── comparison_table.md
│   └── final_assessment.md
│
├── prompts/                   ← reusable prompts; not authoritative research memory
│   └── README.md
│
└── papers/                    ← local PDF storage (git-ignored; use arXiv/DOI)
```

The planned `agents/` area is intentionally not created by the architecture audit; bootstrap issue #4 defines it after the collaboration model is settled.

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
approach template          (approaches/)
  ↓
candidate experiment       (candidates/)
  ↓
synthesis                  (synthesis/)
```

Every quantitative number in a candidate experiment must be traceable back
up this chain to a primary source. Bootstrap issue #5 will harden identifiers, verification states, and cross-links.

---

## Collaboration workflow

### Roles

| Role | Primary files |
|------|--------------|
| Foundations researcher | `definitions/`, `PROJECT_RULES.md` |
| Literature scout | `literature/` |
| Experimental approach researcher | `approaches/` |
| Numerical verifier | `calculations/` |
| Adversarial reviewer | `reviews/` |
| Synthesis researcher | `synthesis/` |

These role names are provisional architecture only. Bootstrap issues #3 and #4 define authoritative handoffs and per-agent instructions before research starts.

### Session protocol during bootstrap

1. Read the startup checklist below.
2. Identify the assigned bootstrap task.
3. Work in a task branch.
4. Record durable decisions in the repository, not only in issue/chat text.
5. Do not silently overwrite a conflicting result or rule.
6. Do not begin substantive Planck-gravity research while the repository status is NO-GO.

---

## Git workflow

### Branch naming

```text
main                    ← accepted shared research state
research/<topic>        ← exploratory research
literature/<topic>      ← literature survey or source assessment
review/<topic>          ← adversarial review or governance audit
synthesis/<topic>       ← integration and comparison
```

Do not create all branches now. Create a branch when starting a task.

### Merging into main

For substantive scientific work, a branch may be merged into `main` when:

- All claims carry evidence codes and accessible sources.
- All important quantitative claims are independently verified or flagged as
  unverified with a TODO.
- No E3/E4 assumption appears in a final experimental design without explicit
  labelling.
- No fabricated citations are present.
- Dimensional checks pass for all new equations.
- Any conflict with existing content has a review item in `reviews/`.
- The numerical verifier has run `calculations/test_calculations.py` and it passes.

Bootstrap issues #3–#5 may refine these criteria before research begins.

---

## Start here if you are an AI research session

During the bootstrap phase, read these files **before** doing any assigned work:

1. `README.md` (this file)
2. `PROJECT_RULES.md`
3. `LITERATURE_RULES.md`
4. `REPOSITORY_ARCHITECTURE.md`
5. `definitions/README.md`
6. all currently accepted files in `definitions/`
7. the GitHub issue defining your task
8. all existing files in the repository area your task may modify

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
