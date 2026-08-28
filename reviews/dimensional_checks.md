# Dimensional Checks

This file records dimensional analysis of key equations used in the project.

## Purpose

Every equation that appears in an approach template or candidate experiment must
be dimensionally correct. Dimensional errors are a common source of order-of-magnitude
mistakes.

## Format

```
## Check [ID]: [Equation label]

- Equation: (LaTeX or ASCII)
- Source file:
- LHS dimensions: [M L T ...]
- RHS dimensions: [M L T ...]
- Result: pass / fail
- Notes:
```

---

## Checks

> **TODO (numerical verifier):** Record dimensional checks here as equations are
> added to approach templates and candidate experiments.

### Priority equations

The following equations should be checked first:

1. Planck length: `l_P = sqrt(ħ G / c³)` — dimensions [L]
2. Planck time: `t_P = sqrt(ħ G / c⁵)` — dimensions [T]
3. Planck mass: `m_P = sqrt(ħ c / G)` — dimensions [M]
4. Planck energy: `E_P = sqrt(ħ c⁵ / G)` — dimensions [M L² T⁻²]

> **TODO:** Verify each of the above and record the result.
