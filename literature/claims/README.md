# Literature Claims

This directory stores structured evidence records. Read `LITERATURE_RULES.md` and `PROVENANCE_WORKFLOW.md` before creating or changing claims.

## Naming

Claim files may be grouped by paper or topic, but every individual claim has a stable ID:

```text
CLM-<topic>-NNN
```

Use `TEMPLATE.md` for new records. IDs are never reused.

## Required fields

Each claim records its precise statement, optional value/units, conditions, E1/E2/E3/E4 evidence code, project verification status, BibTeX `source_key`, open full-text route, arXiv/DOI when available, exact source location, verifier, downstream uses, supersession link, and caveats.

## Status

`unverified | verified | challenged | superseded | rejected`

Evidence class and verification status are independent. Publication or arXiv presence does not make a claim verified.

Only verified E1/E2 claims may support decisive final-design statements.

## Contradictions

Preserve contradictory results as separate claim IDs. Do not overwrite a prior number. Link material conflicts to a `REV-*` review record so conditions, comparability, and resolution remain explicit.

## Bibliography

Full bibliographic metadata belongs in `literature/library.bib`. Claims reference the corresponding BibTeX key and add claim-specific provenance such as value, conditions, source location, and downstream usage.