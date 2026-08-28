# Calculations

This directory contains reproducible numerical calculations for the project.

## Core files

| File | Purpose |
|---|---|
| `constants.py` | Planck units computed from authoritative constants |
| `scaling_relations.py` | Shared scaling laws and orders-of-magnitude metrics |
| `test_calculations.py` | Automated tests for shared calculations |

## Provenance requirement

Read `PROVENANCE_WORKFLOW.md`. Every important research calculation must have a stable `CAL-<topic>-NNN` ID and identify the claim IDs used as inputs.

At the top of a script/notebook/calculation record, include something equivalent to:

```text
Calculation ID: CAL-example-001
Input claims: CLM-example-001, CLM-example-002
Outputs used by: approaches/example.md
```

A fresh numerical verifier must be able to recover the equations, units, constants, input claim IDs, and downstream output without chat history.

## Running shared calculations

```bash
python calculations/constants.py
python calculations/scaling_relations.py
python -m pytest calculations/test_calculations.py -v
```

## Principles

1. Use authoritative physical constants (`scipy.constants` where appropriate).
2. Include units and perform dimensional checks.
3. Important numerical results must be reproducible here, not only in prose.
4. Trace source-dependent inputs to `CLM-*` IDs.
5. Independently verify decisive calculations according to `agents/numerical_verifier.md` and `COLLABORATION_WORKFLOW.md`.
6. Keep calculations simple and readable; do not build unnecessary infrastructure.

## Adding a research calculation

1. Assign a new `CAL-*` ID.
2. Record input `CLM-*` IDs and assumptions.
3. Implement the calculation transparently.
4. Add tests/checks appropriate to its importance.
5. Reference the `CAL-*` ID from the approach/candidate using the result.
6. Send decisive results to an independent numerical-verifier chat.