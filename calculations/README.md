# Calculations

This directory contains reproducible numerical calculations for the project.

## Files

| File | Purpose |
|------|---------|
| `constants.py` | Planck units computed from CODATA fundamental constants |
| `scaling_relations.py` | Scaling laws and orders-of-magnitude metrics |
| `test_calculations.py` | Automated tests verifying constants and scaling relations |

## Running the calculations

```bash
python calculations/constants.py
python calculations/scaling_relations.py
```

## Running the tests

```bash
python -m pytest calculations/test_calculations.py -v
# or, without pytest:
python calculations/test_calculations.py
```

## Principles

1. Use `scipy.constants` for CODATA fundamental constants wherever possible.
2. Every result printed to stdout must include units.
3. Important numerical results must be reproducible here — they must not exist
   only as prose in Markdown files.
4. Do not build a complex software system. Keep calculations simple and readable.

## Adding a new calculation

1. Add the function to the appropriate file.
2. Add a test in `test_calculations.py`.
3. Record the result in the relevant approach or candidate file with a reference
   to this directory.
