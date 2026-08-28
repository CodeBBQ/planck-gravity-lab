# Repository Architecture and Research-Readiness Audit

Status: **Bootstrap phase — structure and collaboration model accepted; per-agent instructions, provenance mechanics, and fresh-agent validation remain before substantive research.**

This document records the outcome of the first repository audit. It is intentionally about structure, authority, navigation, and research readiness; it does not evaluate any Planck-gravity experimental approach.

## 1. Architectural assessment

The repository already has the right major separation of concerns:

- `PROJECT_RULES.md` — authoritative scientific, mathematical, and epistemic constraints.
- `LITERATURE_RULES.md` — authoritative source-access and evidence-classification rules.
- `REPOSITORY_ARCHITECTURE.md` — authority model and bootstrap/readiness state.
- `COLLABORATION_WORKFLOW.md` — role boundaries, handoffs, independence, branch ownership, review and rejection paths.
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
2. `COLLABORATION_WORKFLOW.md` is authoritative for how independent agents collaborate and review one another.
3. `definitions/` contains shared scientific definitions and metrics accepted into repository state.
4. `literature/claims/` and `calculations/` contain evidence and reproducible derivations supporting research conclusions.
5. `approaches/` contains approach-level research state.
6. `candidates/` contains stronger proposals assembled from accepted evidence and calculations.
7. `reviews/` contains challenges, disputes, and verification records.
8. `synthesis/` is downstream of the above and must not become an independent source of unsupported facts.
9. GitHub issues, chat history, and prompts may coordinate work but must not be the only location of any rule, scientific claim, or accepted conclusion.

`main` should represent the accepted shared research state. Exploratory or disputed work belongs on task branches until merge criteria are satisfied.

## 3. Fresh-chat recoverability audit

A completely fresh chat can now recover the project-level collaboration context from the repository:

| Required context | Current location | Audit result |
|---|---|---|
| Scientific goal | `README.md` | Present |
| Non-speculative constraints | `PROJECT_RULES.md`, `README.md` | Present |
| Literature/access rules | `LITERATURE_RULES.md` | Present |
| Evidence classes | `LITERATURE_RULES.md`, `README.md` | Present |
| Calculation standards | `PROJECT_RULES.md`, `calculations/README.md` | Present |
| Conceptual distinctions | `PROJECT_RULES.md`, `definitions/` | Present |
| Git/branch model | `README.md`, `COLLABORATION_WORKFLOW.md` | Present |
| Conflict/rejection handling | `PROJECT_RULES.md`, `COLLABORATION_WORKFLOW.md`, `reviews/` | Present |
| Agent handoffs and independence | `COLLABORATION_WORKFLOW.md` | Present |
| Role-specific startup instructions | — | **Missing; deferred to bootstrap issue #4** |
| Claim lifecycle / verification states | Partial in `LITERATURE_RULES.md` | **Needs hardening in bootstrap issue #5** |
| End-to-end fresh-agent validation | — | **Deferred to bootstrap issue #6** |

The repository is structurally and collaboratively coherent but **not yet ready for substantive multi-agent research**.

## 4. Mandatory startup path during bootstrap

Until the per-agent system is completed, a fresh chat must read in this order:

1. `README.md`
2. `PROJECT_RULES.md`
3. `LITERATURE_RULES.md`
4. `REPOSITORY_ARCHITECTURE.md`
5. `COLLABORATION_WORKFLOW.md`
6. `definitions/README.md`
7. relevant currently accepted files in `definitions/`
8. the GitHub issue defining the assigned task
9. all existing files in the repository area that task may modify

After bootstrap issue #4, this list should be superseded by the canonical per-agent startup protocol and agent file.

## 5. Scientific data flow

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

The detailed role-to-role workflow, including loops, independent verification, and rejection handling, is defined in `COLLABORATION_WORKFLOW.md`.

## 6. Structural strengths

The audit found the following design choices worth preserving:

- Global scientific rules are centralized rather than duplicated across approach templates.
- The evidence hierarchy explicitly prevents E3/E4 assumptions from silently entering final designs.
- Literature access constraints are explicit and compatible with open arXiv/institutional workflows.
- `approaches/` files are clearly labelled as research state rather than accepted final conclusions.
- Candidate and synthesis layers are separated, reducing premature convergence.
- Adversarial review and independent numerical verification have explicit roles.
- Reproducible calculations have a dedicated location rather than living only in prose.
- PDFs are not intended for normal Git history; source identifiers remain the reproducibility mechanism.

## 7. Bootstrap status

### Completed

- **Issue #2 — repository architecture:** accepted.
- **Issue #3 — collaboration model:** role boundaries, handoffs, independence, branch ownership, disagreement, rejection, and merge expectations defined in `COLLABORATION_WORKFLOW.md`.

### Remaining blockers

#### Issue #4 — per-agent files
Create one durable instruction file per role and a canonical fresh-chat startup protocol. Every new chat must be able to discover its required context from the repo alone.

#### Issue #5 — evidence/provenance hardening
Define stable claim identifiers, verification-state transitions, contradiction handling, links from claims to calculations, and downstream provenance.

#### Issue #6 — readiness dry run
Test the system with genuinely fresh agents and issue a final GO/NO-GO decision before substantive research begins.

## 8. Structural decisions resolved

- **Keep the current top-level research directories.** No restructure is justified now.
- **Keep rules centralized.** Do not copy full scientific/literature rules into every future agent file.
- **Keep prompts non-authoritative.** A prompt can direct a task but cannot substitute for repository-resident rules or accepted research state.
- **Keep `main` conservative.** Exploratory disagreement should remain visible on branches/reviews until resolved.
- **Require independent verification for decisive results.** Original approach/calculation authors should not also perform their own final numerical/adversarial verification.
- **Permit negative/rejected research outputs.** They remain preserved and discoverable rather than being deleted.
- **Do not add a database yet.** Markdown, BibTeX, Python, and Git are sufficient for the current scale.
- **Do not enable Git LFS by default.** Open-paper metadata plus a local ignored `papers/` cache is sufficient unless a later requirement justifies versioned PDFs.

## 9. Unresolved decisions for later bootstrap work

The following questions remain before the research-start gate:

- Exact mandatory-read list and write scope for each agent file.
- Stable naming/ID convention for claims, calculations, reviews, and candidates.
- Verification-state vocabulary and transition rules.
- Exact machine-readable or Markdown cross-linking convention for provenance.
- How superseded claims are represented without being mistaken for accepted evidence.
- Final dry-run confirmation that fresh agents follow the intended workflow without hidden chat context.

## 10. Audit conclusion

**Architecture: ACCEPTED.**

**Collaboration model: ACCEPTED.**

**Research readiness: NO-GO until bootstrap issues #4–#6 are completed.**

The repository now contains both the necessary scientific layers and the project-level agent collaboration model. Remaining work is to instantiate role-specific instructions, formalize evidence/provenance mechanics, and validate the complete system with fresh-agent dry runs.
