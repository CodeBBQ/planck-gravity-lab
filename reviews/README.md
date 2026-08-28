# Reviews

This directory contains adversarial reviews and mathematical checks.

## Purpose

Adversarial review is a mandatory step before any experimental proposal is accepted
into `synthesis/`. Reviews identify:

- Unjustified assumptions
- Dimensional errors
- Incorrect signal estimates
- Confused or missing distinctions (see `definitions/what_counts_as_probe.md`)
- E3/E4 claims disguised as E1/E2
- Amplification claims that have not been derived quantitatively

## Files

| File | Purpose |
|------|---------|
| `adversarial_review.md` | Running record of adversarial challenges and responses |
| `dimensional_checks.md` | Record of dimensional analysis checks on key equations |

## Protocol

1. When an approach or candidate is ready for review, create an entry in
   `adversarial_review.md`.
2. The adversarial reviewer must challenge every assumption and every numerical
   claim independently.
3. Conflicts must be preserved — do not silently resolve them.
4. A candidate may be promoted to synthesis only after adversarial review is closed
   with explicit resolution of all disputes.
