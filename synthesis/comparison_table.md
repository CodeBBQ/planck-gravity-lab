# Comparison Table

## Status: EMPTY — to be filled after candidate experiments are developed

---

## Instructions

When a candidate experiment passes adversarial review, add a row to this table.
Compute all metrics using `calculations/scaling_relations.py`.
Cite each metric value to the relevant claim in `literature/claims/`.

---

## Comparison

| Candidate | ε_E | ε_L | ε_q | ε_SNR (model, code) | Gap (log₁₀) | Notes |
|-----------|-----|-----|-----|---------------------|-------------|-------|
| TODO | — | — | — | — | — | |

---

## Notes on comparison

- Metrics are **not** directly comparable across rows unless they measure the same
  physical quantity. See `definitions/common_metrics.md`.
- The model column for ε_SNR must state which theoretical prediction was used and
  its evidence code.
- A smaller gap (closer to 0) is better, but only if the governing physics is
  established (E1/E2).
