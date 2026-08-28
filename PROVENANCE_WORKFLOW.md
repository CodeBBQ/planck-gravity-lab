# Evidence and Provenance Workflow

This document defines how sources become traceable project claims and how those claims propagate into calculations, approaches, candidates, reviews, and synthesis.

## 1. Stable identifiers

Use repository-stable IDs:

- Claim: `CLM-<topic>-NNN`
- Calculation: `CAL-<topic>-NNN`
- Review/dispute: `REV-<topic>-NNN`
- Candidate: `CAN-<topic>-NNN`

`<topic>` is a short lowercase slug such as `atomint` or `optical`. Numbers are zero-padded and unique within that topic/type. IDs are never reused, even after supersession.

## 2. Claim record

Every important claim lives in `literature/claims/` and must include:

```yaml
id: CLM-topic-001
claim: one precise sentence
value: value with units or null
conditions: scope/experimental conditions
evidence_code: E1 | E2 | E3 | E4
status: unverified | verified | challenged | superseded | rejected
source_key: BibTeX key in literature/library.bib
open_full_text: URL/arXiv/institutional location
arxiv_id: identifier or null
doi: identifier or null
location: exact section/equation/figure/table
verified_by: role/task/PR or null
used_by:
  - path or CAL/CAN/REV ID
supersedes: claim ID or null
notes: caveats
```

A claim file may contain multiple related claims, but each claim has its own stable ID.

## 3. Evidence code versus verification status

These are independent dimensions.

Evidence code answers **what kind of claim is this?**
- E1 demonstrated experiment
- E2 established theory/derivation
- E3 proposed undemonstrated technique
- E4 speculative/model-dependent

Status answers **what has this project done with the claim?**
- `unverified`: recorded but not independently checked against the source
- `verified`: source and quoted value/conditions checked by an appropriate agent
- `challenged`: a material dispute exists; decisive downstream use is blocked
- `superseded`: retained for history but replaced by another explicit claim
- `rejected`: source/interpretation does not support the recorded claim or the claim is otherwise invalid for project use

Publication or arXiv presence never implies `verified`.

## 4. Status transitions

Allowed normal transitions:

```text
unverified -> verified
unverified -> challenged
verified -> challenged
challenged -> verified
challenged -> rejected
verified -> superseded
unverified -> superseded
```

Do not delete superseded/rejected claims. Link replacements explicitly.

Only `verified` E1/E2 claims may support decisive final-design statements. A candidate may reference unverified material only when it is clearly non-decisive and flagged as pending.

## 5. Bibliography relationship

`literature/library.bib` stores bibliographic metadata once. Claim records refer to it through `source_key` and add claim-specific evidence location, value, conditions, status, and downstream usage.

Do not duplicate full bibliographic entries in every claim unless necessary for readability.

## 6. Open-access rule

A decisive quantitative claim must include a legally accessible full-text route. A paywalled DOI may be retained, but it cannot be the only evidence path. If no open full text can be checked, keep the claim `unverified` and do not use it decisively.

## 7. Calculation provenance

Each important calculation must declare its ID and input claim IDs near the top of the script/notebook/Markdown calculation record, for example:

```text
Calculation ID: CAL-optical-001
Inputs: CLM-optical-003, CLM-optical-007
Outputs used by: approaches/optical_interferometry.md
```

A decisive numerical result must be reproducible from source-backed inputs, equations, constants, and code. The numerical verifier should be able to work from these records without prior chat context.

## 8. Downstream references

Approach and candidate files should reference claim/calculation IDs next to important numerical statements rather than only citing papers indirectly.

Example:

```text
Demonstrated displacement noise: ... [CLM-optical-003]
Derived Planck-related figure of merit: ... [CAL-optical-001]
```

Review records identify the exact IDs they challenge. Synthesis references reviewed candidate/approach/calculation IDs rather than introducing new unsupported numbers.

## 9. Contradictory evidence

Contradictory claims coexist with separate IDs. Never overwrite one value with another simply because it is newer or preferred.

Record:
- both claim IDs,
- differing conditions/methods,
- whether they are actually comparable,
- a `REV-*` item when the discrepancy matters downstream.

The review may conclude that one claim is rejected, that one supersedes another, that both are valid under different conditions, or that the dispute remains unresolved.

## 10. Minimum provenance chain for a decisive number

```text
open full-text source
  -> BibTeX source_key
  -> verified CLM ID with value/units/conditions/location
  -> CAL ID with equations and source-backed inputs
  -> approach/candidate statement referencing CLM/CAL IDs
  -> independent numerical verification where decisive
  -> REV ID / adversarial disposition
  -> synthesis
```

If any decisive link is missing, the result is not ready for final synthesis.

## 11. Lightweight implementation

Use Markdown/YAML-style records, BibTeX, Python, and Git. Do not introduce a database or complex provenance service unless project scale later justifies it.

## 12. Non-scientific template rule

Templates may use placeholders such as `CLM-example-001`, `10 arbitrary_units`, and `TODO_OPEN_SOURCE`; never invent realistic authors, journals, DOIs, arXiv IDs, or experimental values for examples.