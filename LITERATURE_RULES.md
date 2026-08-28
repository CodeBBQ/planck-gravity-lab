# Literature Rules — QuantumGravity Research Project

These rules govern every source used in this repository.

---

## 1. Access policy

The project owner has **no institutional paywall access**.  
Every important quantitative claim must therefore have a **legally accessible
full-text source**.

A paywalled journal reference may be recorded as supplementary context but
**cannot be the sole evidence** for an important claim.

---

## 2. Source preference order

When multiple sources exist for a claim, prefer:

1. Open primary experimental paper (open-access journal)
2. arXiv manuscript corresponding to a published paper
3. Open-access journal article (DOAJ, PubMed Central, etc.)
4. Collaboration or institutional repository
5. Author manuscript on a personal/institutional webpage
6. Authoritative technical documentation (e.g., NIST, CODATA, instrument manuals)
   where appropriate for technical specifications

---

## 3. Evidence classification

Every recorded claim must carry one of the following codes:

| Code | Meaning |
|------|---------|
| **E1** | Directly demonstrated experimental result |
| **E2** | Established physical theory or derivation |
| **E3** | Proposed but not yet demonstrated technique or performance figure |
| **E4** | Speculative or model-dependent physics |

### Rules by code

- **Final experimental designs** may depend only on **E1** and **E2** evidence.
- **E3** claims may be investigated but must remain explicitly marked as
  undemonstrated.
- **E4** claims may provide motivation or context but **cannot be assumed** in any
  quantitative analysis contributing to a candidate experiment.

### Important note on arXiv

An arXiv preprint establishes that the authors *proposed or reported* something.
Its presence on arXiv **does not** establish that its assumptions are correct,
that its conclusions have been verified, or that the claimed performance has been
demonstrated. Assess arXiv papers as E1, E2, E3, or E4 based on their content,
not their existence.

---

## 4. Claim record format

For every important claim, record a structured entry in
`literature/claims/` using the template below.
Prefer machine-readable Markdown tables or YAML front-matter.

### Required fields

```
claim:          (one sentence description)
value:          (numerical value with units, if applicable)
conditions:     (experimental or theoretical conditions under which the value holds)
source:         (full bibliographic reference)
arxiv_id:       (arXiv:XXXX.XXXXX or "none")
doi:            (10.XXXX/... or "none")
location:       (equation / figure / table / section number in the source)
evidence_code:  (E1 / E2 / E3 / E4)
verified:       (yes / no / partial — did we independently check this?)
notes:          (optional — caveats, conditions of applicability, etc.)
```

---

## 5. Primary literature preference

Experimental performance numbers (noise floors, sensitivities, demonstrated
measurement precisions) must come from **primary literature** whenever possible.

Review articles may provide context and pointers but must not be the sole source
for a performance claim used in a candidate experiment.

---

## 6. Papers storage convention

Do **not** commit large PDFs to normal Git history.

- Store papers locally in a `papers/` directory (see `.gitignore` — this directory
  is excluded from Git).
- Record papers in `literature/library.bib` (BibTeX) so they can be retrieved
  reproducibly using arXiv IDs, DOIs, or institutional URLs.
- In every claim record, provide sufficient metadata (arXiv ID and/or DOI) for
  any contributor to retrieve the full text independently.

---

## 7. Reading queue

Papers that should be read but have not yet been assessed go in
`literature/reading_queue.md`.  
Move assessed papers from the queue to `literature/library.bib` and create the
corresponding claim records in `literature/claims/`.

---

## 8. Fabrication prohibition

**Never fabricate citations.**  
Never create realistic-looking placeholder references with invented author names,
journal names, volume numbers, or arXiv IDs.  
Clearly marked `TODO` placeholders are acceptable; fabricated citations are not.
