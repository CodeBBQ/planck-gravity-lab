# Approach: Astrophysical and Cosmological Baselines

## Status: TEMPLATE — to be filled by experimental approach researcher

---

## Research question

> **TODO:** What specific aspect of Planck-scale gravitational physics could this
> approach probe? State a falsifiable question.

---

## Observable

> **TODO:** What physical quantity is measured?  
> Units, typical range, and measurement method.

---

## Governing physics

> **TODO:** State the relevant physical laws.  
> Cite governing equations with sources and evidence codes (E1–E4).  
> Derive, do not merely assert.

---

## Relevant Planck-scale quantity

> **TODO:** Which Planck-scale quantity (l_P, t_P, m_P, E_P, or combination)
> appears in the governing equation, and in what combination?  
> If none appears naturally, state that explicitly.

---

## Dimensionless control parameter

> **TODO:** Identify the small dimensionless ratio that controls the Planck-scale
> correction. Derive it. Express it numerically using values from
> `calculations/constants.py`.

---

## Current demonstrated technology

> **TODO (literature scout + approach researcher):** What is the state of the art
> for this approach?  
> Record each performance number as a structured claim in `literature/claims/`
> with evidence code E1 and an accessible source.

| Parameter | Best demonstrated value | Source | Evidence code |
|-----------|------------------------|--------|---------------|
| TODO | TODO | TODO | TODO |

---

## Best realistic configuration

> **TODO:** Describe the most favourable experimental configuration using only
> demonstrated technology (E1/E2 only).  
> Do not invoke undemonstrated techniques (E3) here — list them separately below.

---

## Signal estimate

> **TODO (numerical verifier):** Derive the predicted signal for the best realistic
> configuration. Show the derivation step by step. Implement in
> `calculations/scaling_relations.py`.

---

## Noise and backgrounds

> **TODO:** List all relevant noise sources. Quantify each.  
> Identify which is dominant.

| Noise source | Magnitude | Reducible? |
|-------------|-----------|-----------|
| TODO | TODO | TODO |

---

## Systematics

> **TODO:** Identify systematic errors that could mimic or mask the Planck-scale signal.

---

## Scaling analysis

> **TODO (numerical verifier):** How does the signal-to-noise ratio scale with
> experimental parameters (size, mass, temperature, integration time, etc.)?  
> Derive the scaling. Implement in `calculations/scaling_relations.py`.

---

## Orders-of-magnitude gap

> **TODO:** Compute ε_SNR = predicted signal / experimental uncertainty using the
> metrics in `definitions/common_metrics.md`.  
> Express as orders of magnitude (log₁₀).  
> Do not write "too small" — give the number.

---

## Potential amplification mechanisms

> **TODO:** Are there physical or technical mechanisms that could improve the reach?
> For each:
> - State the mechanism.
> - Derive the amplification factor quantitatively.
> - Assign evidence code (E1/E2 if established, E3 if proposed but undemonstrated).

---

## Possible loopholes

> **TODO:** Under what circumstances could the approach produce a signal without
> probing Planck-scale physics?

---

## Failure modes

> **TODO:** What would cause the approach to be physically impossible or
> experimentally infeasible?

---

## Best surviving configuration

> **TODO (after analysis):** Summary of the strongest configuration that survives
> the analysis above, with all assumptions stated and labelled.

---

## Open questions

> **TODO:** List unresolved questions that require further research sessions.

---

## Evidence

| Claim | Code | Source | arXiv/DOI | Verified? |
|-------|------|--------|-----------|-----------|
| TODO | TODO | TODO | TODO | No |

---

## Confidence

> **TODO (adversarial reviewer):** After adversarial review, assign a confidence
> level and justify it.
