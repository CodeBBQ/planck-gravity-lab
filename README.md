# QuantumGravity — Planck-Scale Gravity Lab

> **Scientific goal:**  
> *What is the closest physically realizable experiment, using established physics
> and current demonstrated technology, to probing gravitational physics associated
> with the Planck scale?*

This is a **multi-session collaborative research project**.  
The Git repository is the shared scientific memory.  
No chat history is preserved between sessions — everything lives here.

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

```
planck-gravity-lab/
│
├── README.md                  ← you are here
├── PROJECT_RULES.md           ← mandatory rules for every session
├── LITERATURE_RULES.md        ← source and citation rules
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
├── prompts/                   ← reusable prompts for AI research sessions
│   └── README.md
│
└── papers/                    ← local PDF storage (git-ignored; use arXiv/DOI)
```

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

```
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
up this chain to a primary source.

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

A single session may hold multiple roles but must record which role it is acting
in at any given point.

### Session protocol

1. Read the session startup checklist (below).
2. Identify your role(s) for this session.
3. Work in a branch (see Git workflow).
4. Record *all* equations, assumptions, sources, numerical results, uncertainties,
   and unresolved questions in the relevant files.
5. Do not silently overwrite a conflicting result — preserve it and create a review
   item in `reviews/`.
6. Open a pull request to `main` when the work satisfies the merge criteria.

---

## Git workflow

### Branch naming

```
main                    ← accepted shared research state
research/<topic>        ← exploratory research
literature/<topic>      ← literature survey or source assessment
review/<topic>          ← adversarial review
synthesis/<topic>       ← integration and comparison
```

Do not create all branches now. Create a branch when starting a task.

### Merging into main

A branch may be merged into `main` when:

- All claims carry evidence codes and accessible sources.
- All important quantitative claims are independently verified or flagged as
  unverified with a TODO.
- No E3/E4 assumption appears in a final experimental design without explicit
  labelling.
- No fabricated citations are present.
- Dimensional checks pass for all new equations.
- Any conflict with existing content has a review item in `reviews/`.
- The numerical verifier has run `calculations/test_calculations.py` and it passes.

---

## Start here if you are an AI research session

Read these files **before** beginning any research work:

1. `README.md` (this file) — project overview and workflow
2. `PROJECT_RULES.md` — mandatory scientific and mathematical rules
3. `LITERATURE_RULES.md` — source, citation, and evidence rules
4. `definitions/README.md` — vocabulary overview
5. `definitions/planck_scales.md` — Planck unit definitions and values
6. `definitions/what_counts_as_probe.md` — conceptual distinctions
7. `definitions/common_metrics.md` — how to measure "proximity to Planck scale"
8. The specific `approaches/` file for your topic (if applicable)

Do **not** begin writing conclusions before reading all of the above.

---

## What this project does NOT do

- It does not choose a winning experiment prematurely.
- It does not fabricate citations or invent plausible-sounding references.
- It does not assume that quantum sensitivity implies sensitivity to quantum gravity.
- It does not treat an arXiv preprint as establishing the correctness of its
  own assumptions.
- It does not conclude that a signal is "too small" without quantifying the gap.

