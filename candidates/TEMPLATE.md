# Candidate Experiment Template

Copy this file and rename it when proposing a candidate experiment.  
Every section is **required**. Do not submit an incomplete candidate.

---

## Title

> (Short descriptive title)

---

## Hypothesis / Research question

> State the precise physical hypothesis being tested, or the question being answered.
> Be falsifiable. Cite the theoretical prediction with evidence code.

---

## Observable

> What physical quantity is measured?  
> State units, order of magnitude, and measurement method.

---

## Derivation

> Derive the predicted signal from first principles.  
> Show every step. Define every symbol. Check dimensions.  
> Implement numerically in \`calculations/\`.

---

## Assumptions

> List every assumption explicitly.  
> For each assumption, assign an evidence code (E1–E4) and provide a source.

| Assumption | Evidence code | Source | Verified? |
|-----------|---------------|--------|-----------|
| TODO | TODO | TODO | No |

**Final experimental designs may depend only on E1 and E2 assumptions.**

---

## Apparatus

> Describe the experimental apparatus in sufficient detail to evaluate feasibility.

---

## Demonstrated components

> For each component, cite the demonstration.

| Component | Demonstrated specification | Source | Evidence code |
|-----------|--------------------------|--------|---------------|
| TODO | TODO | TODO | E1 |

---

## Experimental parameters

| Parameter | Symbol | Value | Justification |
|-----------|--------|-------|---------------|
| TODO | TODO | TODO | TODO |

---

## Predicted signal

> State the predicted Planck-related signal magnitude.  
> Derive it, do not merely assert it.  
> If the prediction is model-dependent, label it E3 or E4 and identify the model.

---

## Noise model

> List all noise sources in order of magnitude.  
> For each, provide the relevant formula and numerical estimate.

| Noise source | Formula | Estimated magnitude | Source |
|-------------|---------|---------------------|--------|
| TODO | TODO | TODO | TODO |

---

## Systematic-error budget

> List potential systematic errors that could mimic or mask the signal.  
> For each, estimate its magnitude and describe how it would be controlled.

| Systematic | Estimated magnitude | Mitigation | Residual |
|-----------|---------------------|------------|---------|
| TODO | TODO | TODO | TODO |

---

## Integration time / repetitions

> How long must the experiment run, or how many repetitions are required, to
> achieve the stated sensitivity?  
> Derive this from the noise model — do not assert it.

---

## Planck-related figure of merit

> Compute at least one metric from \`definitions/common_metrics.md\`:
>
> - ε_E = E / E_P
> - ε_L = l_P / L
> - ε_q = q l_P / ħ
> - ε_SNR = predicted Planck signal / experimental uncertainty
>
> State which metric is most appropriate for this experiment and why.

---

## State-of-the-art comparison

> How does this proposal compare to the current best experiment of its type?  
> Cite the best demonstrated performance with evidence code E1 and an accessible source.

---

## Orders-of-magnitude gap

> Express ε_SNR (or the most appropriate metric) as a gap in orders of magnitude:
>
> ```
> gap = -log₁₀(ε_SNR)
> ```
>
> Do not write "too small" — give the number.

---

## Falsification criteria

> What experimental result would falsify the hypothesis?  
> What result would confirm a Planck-scale signal?  
> How would systematic errors be distinguished from a genuine signal?

---

## Unresolved issues

> List any open questions that must be resolved before this candidate can be
> evaluated definitively.

---

## Evidence summary

| Claim | Code | Source | arXiv/DOI | Verified? |
|-------|------|--------|-----------|-----------|
| TODO | TODO | TODO | TODO | No |
