# Common Metrics for "Proximity to the Planck Scale"

## Status: TEMPLATE — to be filled by foundations researcher and numerical verifier

---

## 1. Why a single universal metric is wrong

There is no single dimensionless number that captures "how close an experiment is
to the Planck scale". Different experiments probe different physical quantities,
and these quantities relate to Planck-scale physics through different combinations
of fundamental constants.

Providing only one metric invites false comparisons between physically dissimilar
approaches.

---

## 2. Framework: four distinct dimensionless ratios

The following ratios characterise proximity in different senses.
They are **not** directly comparable to each other.

### Metric 1: Energy ratio

```
ε_E = E / E_P
```

- `E` = characteristic energy of the experiment (e.g., beam energy, phonon energy)
- `E_P` = Planck energy ≈ 1.22 × 10¹⁹ GeV (TODO: exact value from constants.py)

**Physical meaning:** How close is the experiment's energy scale to the Planck
energy? Relevant when the signal is proportional to (E/E_P)^n.

**Note:** Currently demonstrated particle accelerator energies give ε_E ~ 10⁻¹⁵.
The exact value must be computed in `calculations/scaling_relations.py`.

### Metric 2: Length ratio

```
ε_L = l_P / L
```

- `L` = characteristic length scale of the experiment
- `l_P` = Planck length ≈ 1.62 × 10⁻³⁵ m (TODO: exact value from constants.py)

**Physical meaning:** How many Planck lengths fit in the experiment's length scale?
Relevant when the signal is proportional to (l_P/L)^n.

**Warning:** A small ε_L does not mean the experiment probes Planck-scale physics
unless a physical effect proportional to (l_P/L)^n appears in the governing equation.

### Metric 3: Momentum-times-length ratio

```
ε_q = q l_P / ħ
```

- `q` = momentum transfer in the experiment
- Dimensionless: = q / (ħ / l_P) = q / m_P c

**Physical meaning:** Relevant for scattering experiments and probes of
short-distance structure. Related to the de Broglie wavelength vs. l_P.

### Metric 4: Signal-to-noise ratio for Planck effect

```
ε_SNR = δ_P / σ_exp
```

- `δ_P` = predicted signal magnitude arising from Planck-scale physics
  (model-dependent — must state which model and label E4 if speculative)
- `σ_exp` = best demonstrated experimental uncertainty for that observable

**Physical meaning:** The most direct measure of experimental reach. If ε_SNR ≪ 1,
the experiment cannot detect the predicted effect.

**Critical note:** This metric requires a specific theoretical prediction δ_P.
Every such prediction must be labelled with its evidence code (usually E3 or E4).

---

## 3. Comparison across approaches

When comparing approaches, use all applicable metrics. Do not reduce to a single
number.

A table comparing approaches should report:

| Approach | ε_E | ε_L | ε_q | ε_SNR (model) | Gap (orders of magnitude) |
|----------|-----|-----|-----|---------------|--------------------------|
| TODO     |     |     |     |               |                          |

See `synthesis/comparison_table.md` for the evolving comparison.

---

## 4. Orders-of-magnitude gap

For every approach, compute:

```
gap = -log₁₀(most favourable applicable metric)
```

A gap of N means the experiment falls N orders of magnitude short of the
Planck scale on that metric.

Report the gap for every metric that applies; do not pick the most favourable
one without justification.

---

## 5. Reproducible calculation

All metric computations must be reproducible by running:

```
python calculations/scaling_relations.py
```

---

## 6. Open questions

> **TODO (foundations researcher):** Are there physical scenarios where ε_SNR can
> be large (experimentally accessible) even though ε_E and ε_L are extremely small?
> If so, under what assumptions, and what is the evidence code?
