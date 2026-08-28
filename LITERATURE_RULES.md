# Literature Rules — QuantumGravity Research Project

These rules govern every source used in this repository. Exact IDs, verification states, and cross-link conventions are defined in `PROVENANCE_WORKFLOW.md`.

## 1. Access policy

The project owner has no institutional paywall access. Every important quantitative claim must therefore have a legally accessible full-text source.

A paywalled journal reference may be recorded as supplementary metadata but cannot be the sole evidence for an important claim.

## 2. Source preference

Prefer, in order where appropriate:
1. open primary experimental paper;
2. arXiv manuscript corresponding to a published paper;
3. open-access journal article;
4. collaboration/institutional repository;
5. author manuscript;
6. authoritative technical documentation for technical specifications.

## 3. Evidence classification

| Code | Meaning |
|---|---|
| E1 | Directly demonstrated experimental result |
| E2 | Established physical theory or derivation |
| E3 | Proposed but not yet demonstrated technique/performance |
| E4 | Speculative/model-dependent physics |

Final experimental designs may depend only on E1/E2. E3 may be investigated but remains undemonstrated. E4 is context only and cannot be assumed in decisive candidate calculations.

ArXiv presence establishes only that authors reported/proposed something. It does not establish correctness or demonstration.

## 4. Claim records

Every important claim receives a stable `CLM-*` ID and lives in `literature/claims/`. Use `literature/claims/TEMPLATE.md` and `PROVENANCE_WORKFLOW.md`.

Required information includes:
- precise claim;
- numerical value/units when applicable;
- conditions/scope;
- evidence code;
- project verification status;
- BibTeX source key;
- legally accessible full-text route;
- arXiv ID/DOI where available;
- exact section/equation/figure/table;
- verifier;
- downstream users;
- supersession/caveats.

## 5. Verification status

Claim verification status is separate from evidence class:

`unverified | verified | challenged | superseded | rejected`

Only `verified` E1/E2 claims may support decisive final-design statements. Challenged claims cannot be used decisively until resolved. Superseded/rejected claims remain preserved for provenance.

## 6. Primary-literature preference

Experimental performance numbers should come from primary literature whenever possible. Reviews may provide context/pointers but must not be the sole source for a decisive demonstrated-performance claim.

## 7. Contradictory evidence

Do not silently replace conflicting values. Create separate claim IDs, record differing conditions/methods, and create a `REV-*` record if the discrepancy matters downstream. A review may determine that both are valid under different conditions, one supersedes/rejects another, or the conflict remains unresolved.

## 8. Bibliography relationship

`literature/library.bib` stores bibliographic metadata. Claim records refer to BibTeX entries by `source_key` and store the claim-specific evidence location, value, conditions, classification, verification state, and downstream use.

## 9. Papers storage

Do not commit large PDFs to normal Git history. Keep local copies under `papers/` and record reproducible retrieval metadata in `literature/library.bib` and claim records.

## 10. Reading queue

Unassessed papers belong in `literature/reading_queue.md`. After assessment, add legitimate bibliographic metadata to `library.bib` and create claim records for evidence actually used.

## 11. Fabrication prohibition

Never fabricate citations, author names, journal data, DOIs, arXiv IDs, or realistic-looking experimental values. Clearly marked TODO/non-scientific placeholders are acceptable for templates only.