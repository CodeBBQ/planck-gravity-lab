# Claim Record Template

Use this template only after reading `LITERATURE_RULES.md` and `PROVENANCE_WORKFLOW.md`.

```yaml
id: CLM-example-001
claim: TODO precise one-sentence claim
value: null
conditions: TODO
evidence_code: E1
status: unverified
source_key: TODO_BIBTEX_KEY
open_full_text: TODO_OPEN_SOURCE
arxiv_id: null
doi: null
location: TODO section/equation/figure/table
verified_by: null
used_by: []
supersedes: null
notes: TODO
```

## Notes

- Replace `example` with the topic slug and assign the next unused number.
- Do not reuse an ID.
- Do not mark `verified` until the source, value/claim, conditions, and exact location have been checked.
- Evidence code and verification status are different fields.
- Add downstream paths/IDs to `used_by` when the claim becomes an input.
- If a competing claim exists, create a new ID; do not overwrite the old claim.
- This template contains no scientific evidence.