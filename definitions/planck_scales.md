# Planck Scales — Definitions and Numerical Values

## Status: TEMPLATE — to be filled by foundations researcher

---

## 1. Fundamental constants required

The Planck units are derived from three fundamental constants:

| Symbol | Quantity | Value (CODATA 2018) | Source |
|--------|----------|---------------------|--------|
| G | Newtonian gravitational constant | TODO | TODO |
| ħ | Reduced Planck constant | TODO | TODO |
| c | Speed of light in vacuum | TODO | TODO |

> **TODO (literature scout):** Record exact CODATA 2018 values with full
> uncertainty, arXiv/DOI references, and evidence codes.

---

## 2. Planck unit definitions

The following definitions are standard (E2 — derived consequence of established
dimensional analysis):

### Planck length

```
l_P = sqrt(ħ G / c³)
```

**Derivation:** The unique combination of G, ħ, c with dimensions of length.

**Numerical value:** TODO (see `calculations/constants.py`)

### Planck time

```
t_P = sqrt(ħ G / c⁵) = l_P / c
```

**Numerical value:** TODO

### Planck mass

```
m_P = sqrt(ħ c / G)
```

**Numerical value:** TODO

### Planck energy

```
E_P = m_P c² = sqrt(ħ c⁵ / G)
```

**Numerical value:** TODO

### Planck temperature

```
T_P = E_P / k_B = sqrt(ħ c⁵ / G) / k_B
```

**Numerical value:** TODO

---

## 3. Physical interpretation

> **TODO (foundations researcher):** Write a concise paragraph explaining the
> physical significance of each Planck unit, being careful not to overstate what
> is established vs. what is model-dependent.

Key distinction to address:  
The Planck length is a *dimensional combination* of G, ħ, c. Its appearance as a
"minimum length" in various theories of quantum gravity is **model-dependent (E4)**
and must not be assumed as established fact.

---

## 4. Reproducible values

All numerical values must be computable by running:

```
python calculations/constants.py
```

See `calculations/constants.py` for the implementation.

---

## 5. Evidence

| Claim | Code | Source | Verified? |
|-------|------|--------|-----------|
| Definition of l_P via dimensional analysis | E2 | TODO | No |
| Numerical value of G | E1 | TODO | No |
| Numerical value of ħ | E1 | TODO | No |
| Numerical value of c | E1 | TODO | No |
