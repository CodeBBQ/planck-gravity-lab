# Repository Architecture and Research-Readiness Audit

Status: **Bootstrap phase — structure accepted with follow-up governance work required before substantive research.**

This document records the outcome of the first repository audit. It is intentionally about structure, authority, navigation, and research readiness; it does not evaluate any Planck-gravity experimental approach.

## 1. Architectural assessment

The repository already has the right major separation of concerns:

- `PROJECT_RULES.md` — authoritative scientific, mathematical, and epistemic constraints.
- `LITERATURE_RULES.md` — authoritative source-access and evidence-classification rules.
- `definitions/` — shared vocabulary, Planck-scale definitions, and comparison concepts.
- `literature/` — bibliography, reading queue, and evidence/claim records.
- `calculations/` — reproducible numerical work and tests.
- `approaches/` — structured analysis of broad experimental routes; templates are not conclusions.
- `candidates/` — fully developed experimental proposals that survive earlier analysis.
- `reviews/` — adversarial checks, dimensional checks, and unresolved disputes.
- `synthesis/` — comparison of surviving candidates and final assessment.
- `prompts/` — reusable task prompts; prompts are not authoritative scientific memory.
- `papers/` — local, git-ignored full-text cache; retrieval metadata belongs in `literature/`.

No major directory reorganization is needed before research. The current structure supports a clean provenance path and separates exploratory analysis from accepted synthesis.

## 2. Authority model

Repository authority should be interpreted as follows:

1. `PROJECT_RULES.md` and `LITERATURE_RULES.md` are global normative rules.
2. `definitions/` contains shared scientific definitions and metrics accepted into the repository state.
3. `literature/claims/` and `calculations/` contain the evidence and reproducible derivations supporting research conclusions.
4. `approaches/` contains approach-level research state.
5. `candidates/` contains stronger proposals assembled from accepted evidence and calculations.
6. `reviews/` contains challenges, disputes, and verification records.
7. `synthesis/` is downstream of the above and must not become an independent source of unsupported facts.
8. GitHub issues, chat history, and prompts may coordinate work but must not be the only location of any rule, scientific claim, or accepted conclusion.

`main` should represent the accepted shared research state. Exploratory or disputed work belongs on task branches until merge criteria are satisfied.

## 3. Fresh-chat recoverability audit

A completely fresh chat can already recover most required context from the repository:

| Required context | Current location | Audit result |
|---|---|---|
| Scientific goal | `README.md` | Present |
| Non-speculative constraints | `PROJECT_RULES.md`, `README.md` | Present |
| Literature/access rules | `LITERATURE_RULES.md` | Present |
| Evidence classes | `LITERATURE_RULES.md`, `README.md` | Present |
| Calculation standards | `PROJECT_RULES.md`, `calculations/README.md` | Present |
| Conceptual distinctions | `PROJECT_RULES.md`, `definitions/` | Present |
| Git branch/merge model | `README.md` | Present at a basic level |
| Conflict handling | `PROJECT_RULES.md`, `reviews/README.md` | Present at a basic level |
| Provenance direction | `README.md`, `PROJECT_RULES.md` | Present at a basic level |
| Role names | `README.md`, `PROJECT_RULES.md` | Present |
| Role-specific instructions | — | **Missing; intentionally deferred to bootstrap issue #4** |
| Detailed agent handoffs | — | **Missing; intentionally deferred to bootstrap issue #3** |
| Claim lifecycle / verification states | Partial in `LITERATURE_RULES.md` | **Needs hardening in bootstrap issue #5** |
| End-to-end fresh-agent validation | — | **Deferred to bootstrap issue #6** |

Therefore the repository is structurally coherent but **not yet ready for substantive multi-agent research**. The remaining blockers are governance/context completeness rather than directory layout.

## 4. Mandatory startup path during bootstrap

Until the per-agent system is completed, a fresh chat must read in this order:

1. `README.md`
2. `PROJECT_RULES.md`
3. `LITERATURE_RULES.md`
4. `REPOSITORY_ARCHITECTURE.md`
5. `definitions/README.md`
6. all currently accepted files in `definitions/`
7. the GitHub issue defining the assigned task
8. all existing files in the repository area that task may modify

After bootstrap issue #4, this list should be superseded by the canonical per-agent startup protocol and agent file.

## 5. Data-flow architecture

The intended scientific information flow is:

```text
open literature / authoritative source
              |
              v
      literature claim record
              |
              v
 reproducible derivation/calculation
              |
              v
       experimental approach
              |
        survives review?
          /         \
        no           yes
        |             |
  preserved/rejected  v
                  candidate experiment
                        |
                  adversarial review
                        |
                        v
                     synthesis
```

This is not a mandatory linear pipeline for every exploratory idea. Work may loop backward whenever a calculation, source, or assumption is challenged.

## 6. Structural strengths

The audit found the following design choices worth preserving:

- Global scientific rules are centralized rather than duplicated across approach templates.
- The evidence hierarchy explicitly prevents E3/E4 assumptions from silently entering final designs.
- Literature access constraints are explicit and compatible with open arXiv/institutional workflows.
- `approaches/` files are clearly labelled as templates rather than accepted conclusions.
- Candidate and synthesis layers are separated, reducing premature convergence.
- Adversarial review is represented as a required repository layer.
- Reproducible calculations have a dedicated location rather than living only in prose.
- PDFs are not intended for normal Git history; source identifiers remain the reproducibility mechanism.

## 7. Gaps that should NOT be solved in this issue

The following are real blockers, but belong to the already-created bootstrap issues rather than this structural audit:

### Bootstrap issue #3 — collaboration model

Define role boundaries, handoffs, independence/contamination rules, branch ownership, rejection paths, and review responsibilities.

### Bootstrap issue #4 — per-agent files

Create one durable instruction file per role and a canonical fresh-chat startup protocol. Every new chat must be able to discover its required context from the repo alone.

### Bootstrap issue #5 — evidence/provenance hardening

Define stable claim identifiers, verification-state transitions, contradiction handling, links from claims to calculations, and downstream provenance.

### Bootstrap issue #6 — readiness dry run

Test the system with genuinely fresh agents and issue a final GO/NO-GO decision before substantive research begins.

## 8. Structural decisions resolved by this audit

- **Keep the current top-level research directories.** No restructure is justified now.
- **Keep rules centralized.** Do not copy full scientific/literature rules into every future agent file.
- **Keep prompts non-authoritative.** A prompt can direct a task but cannot substitute for repository-resident rules or accepted research state.
- **Keep `main` conservative.** Exploratory disagreement should remain visible on branches/reviews until resolved.
- **Do not add a database yet.** Markdown, BibTeX, Python, and Git are sufficient for the current scale.
- **Do not enable Git LFS by default.** Open-paper metadata plus a local ignored `papers/` cache is sufficient unless a later requirement justifies versioned PDFs.

## 9. Unresolved decisions for later bootstrap work

The following questions must be answered before the research-start gate:

- Exact mandatory-read list for each agent role.
- Whether one chat may normally hold multiple research roles or whether independent verification requires role separation for decisive results.
- Exact write scope of each agent.
- Stable naming/ID convention for claims, calculations, reviews, and candidates.
- Verification-state vocabulary and transition rules.
- Required independence for numerical verification and adversarial review.
- How rejected approaches and superseded claims remain discoverable without appearing accepted.
- Exact merge criteria for research outputs versus governance/documentation changes.

## 10. Audit conclusion

**Architecture: ACCEPTED.**

**Research readiness: NO-GO until bootstrap issues #3–#6 are completed.**

The repository already contains the necessary scientific layers. The remaining work is to make agent behavior, handoffs, provenance mechanics, and fresh-chat context recovery explicit and testable. Substantive Planck-gravity research should not begin until that bootstrap sequence passes its final readiness audit.
