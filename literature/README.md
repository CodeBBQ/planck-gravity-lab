# Literature

This directory contains the bibliography, reading queue, and assessed claims for
the QuantumGravity project.

## Directory structure

| Path | Contents |
|------|----------|
| `library.bib` | BibTeX database of all assessed sources |
| `reading_queue.md` | Papers to be read and assessed |
| `claims/` | Structured claim records (one file per topic or paper) |

## Workflow

1. A literature scout adds papers to `reading_queue.md`.
2. After reading and assessing, move the entry to `library.bib` and create a
   corresponding claim record in `claims/`.
3. Every claim record must include the fields specified in `LITERATURE_RULES.md`.
4. A paywalled reference may be recorded in `library.bib` but cannot be the sole
   evidence for an important claim.

## Papers storage

Local PDFs are stored in `papers/` (git-ignored).  
Use the arXiv ID or DOI in `library.bib` to retrieve a paper reproducibly.  
See `LITERATURE_RULES.md` for the full papers convention.
