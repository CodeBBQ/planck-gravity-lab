# Project Rules — QuantumGravity Research Project

These rules are **mandatory** for every research session contributing to this repository.

---

## 1. Physics constraints

1. **Established physics only** for final conclusions.  
   Speculative or model-dependent physics may be explored as context but must be
   explicitly labelled and must not appear in final experimental designs.

2. **Current / demonstrated technology only** for final experimental designs.  
   Proposed-but-undemonstrated techniques must remain explicitly flagged.

3. **Never invent** particles, interactions, detector capabilities, materials, or
   technology. If something does not exist in the verified literature, say so.

---

## 2. Claim classification

Every claim must carry one of the following labels:

| Label | Meaning |
|-------|---------|
| **Established fact** | Textbook physics or a directly replicated experimental result |
| **Demonstrated experimental capability** | A real instrument has achieved this performance |
| **Derived consequence** | A calculation from established physics with no additional assumptions |
| **Proposed but undemonstrated technique** | Proposed in the literature; not yet experimentally verified |
| **Speculative / model-dependent assumption** | Depends on unconfirmed theory or unverified model |

Distinguish these explicitly in any written contribution.

---

## 3. Mathematical rigour

1. **Derive** every important scaling relation mathematically.  
   Do not quote results without derivation or a specific literature reference.

2. **Perform dimensional checks** on all equations and estimates.

3. **Quantify sensitivity and orders-of-magnitude gaps.**  
   Expressing a gap only as "too small to detect" is *not* acceptable — give the
   numerical ratio.

4. **Do not conclude merely that something is "too small".**  
   State the gap quantitatively and explain what would be needed to close it.

---

## 4. Conceptual distinctions (mandatory)

The following distinctions must be maintained at all times:

- **Measuring a displacement below the Planck length** vs.  
  **Probing physical processes occurring at the Planck scale.**  
  These are not the same thing. A measurement sensitive to sub-Planck displacements
  does not necessarily probe Planck-scale physics.

- **Quantum-mechanical sensitivity** vs.  
  **Sensitivity to gravity.**  
  An instrument that exploits quantum coherence is not automatically sensitive to
  gravitational quantum effects.

---

## 5. Amplification claims

Any claimed amplification arising from:

- integration time,
- coherence length or time,
- resonance,
- particle number or ensemble size,
- experimental repetitions,
- astronomical or cosmological baselines,

**must be quantitatively demonstrated** — show the scaling law, the applicable range,
and the resulting sensitivity. Qualitative statements alone are not acceptable.

---

## 6. Evidence and openness

1. **Negative results are valid** scientific outputs.  
   A rigorous conclusion that an approach cannot reach Planck sensitivity is
   valuable.

2. **Optimize for the strongest conclusion supported by evidence**, not the most
   exciting or publishable one.

3. Every important quantitative claim must trace to a legally accessible source
   (see `LITERATURE_RULES.md`).

---

## 7. Conflict resolution

Researchers must **not** silently overwrite disagreements.  
If two sessions reach conflicting conclusions:

- Preserve both conclusions in the relevant file with attribution.
- Create a review item in `reviews/` identifying the disputed equation, assumption,
  number, source, or interpretation.
- Resolve the dispute through the independent role defined in `COLLABORATION_WORKFLOW.md`.
- An unresolved disputed claim must not be promoted into an accepted candidate or decisive synthesis conclusion.

---

## 8. Traceability (provenance chain)

Every contribution must fit into the provenance chain:

```
claim
  ↓
source (LITERATURE_RULES evidence code)
  ↓
derivation / calculation (in calculations/ if numerical)
  ↓
approach file (in approaches/)
  ↓
candidate experiment (in candidates/)
  ↓
synthesis (in synthesis/)
```

---

## 9. Collaboration roles

| Role | Responsibility |
|------|---------------|
| **Foundations researcher** | Maintains definitions/, verifies physical assumptions |
| **Literature scout** | Populates literature/, verifies source accessibility |
| **Experimental approach researcher** | Fills approach templates in approaches/ |
| **Numerical verifier** | Independently reproduces decisive calculations |
| **Adversarial reviewer** | Attempts to falsify or weaken claims in reviews/ |
| **Synthesis researcher** | Integrates sufficiently verified/reviewed results in synthesis/ |

`COLLABORATION_WORKFLOW.md` is authoritative for role boundaries, handoffs, write scopes, independence, branch ownership, rejection paths, and merge expectations.

A single chat may perform multiple roles for low-risk bootstrap/editorial work. For decisive scientific results, the original researcher must not also serve as the independent numerical verifier or final adversarial reviewer of that same result.

---

## 10. Session startup checklist

Before beginning any work, a research session must read:

1. `README.md`
2. `PROJECT_RULES.md` (this file)
3. `LITERATURE_RULES.md`
4. `REPOSITORY_ARCHITECTURE.md`
5. `COLLABORATION_WORKFLOW.md`
6. `definitions/README.md` and relevant accepted files in `definitions/`
7. Any file in the area being investigated

Bootstrap issue #4 will add the mandatory role-specific agent file to this list. See `README.md → "Start here if you are an AI research session"` for the canonical reading order.
