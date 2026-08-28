# Agent Instructions and Fresh-Chat Bootstrap

This directory makes each research role usable by a completely fresh chat. `PROJECT_RULES.md`, `LITERATURE_RULES.md`, and `COLLABORATION_WORKFLOW.md` remain authoritative; agent files add role-specific instructions rather than duplicating global rules.

## Mandatory fresh-chat protocol

Before changing repository files, every new research chat must:

1. Read `README.md`.
2. Read `PROJECT_RULES.md` and `LITERATURE_RULES.md`.
3. Read `REPOSITORY_ARCHITECTURE.md` and `COLLABORATION_WORKFLOW.md`.
4. Select exactly one primary role for the task and read its file in `agents/`.
5. Read `definitions/README.md` and the accepted definition files relevant to the task.
6. Read the assigned GitHub issue/task, inspect the current branch/base, and read existing files in the area the task may modify.
7. State internally the task question, role, allowed write scope, required outputs, and required handoff before doing work.
8. If the task requires decisive independent verification/review of work produced by the same chat, stop and hand that stage to a separate chat.

No prior conversation history is required or authoritative.

## Role selection

| Task | Primary role | File |
|---|---|---|
| Definitions, physical distinctions, shared metrics | Foundations researcher | `foundations_researcher.md` |
| Open literature and evidence extraction | Literature scout | `literature_scout.md` |
| Evaluate an experimental route | Experimental-approach researcher | `approach_researcher.md` |
| Independently reproduce numerical results | Numerical verifier | `numerical_verifier.md` |
| Attempt to falsify/weaken a conclusion | Adversarial reviewer | `adversarial_reviewer.md` |
| Compare reviewed outputs/project conclusion | Synthesis researcher | `synthesis_researcher.md` |

If a task spans roles, choose the role responsible for the requested deliverable. Create explicit handoffs rather than silently switching roles. Low-risk editorial/bootstrap work may combine roles; decisive scientific verification must remain independent as required by `COLLABORATION_WORKFLOW.md`.

## Task prompt minimum

A task assigned to a fresh chat should identify:

- repository and issue/task,
- primary role,
- question/deliverable,
- branch expectation if relevant,
- any deliberate independence constraint.

The task prompt should tell the chat to follow this bootstrap protocol rather than copying global rules into every prompt.

## Handoff minimum

Before completing a task, leave enough durable repository state for another fresh chat to continue: files changed, question addressed, evidence/inputs, equations/calculations where relevant, conclusion/status, unresolved items, and next role/action.

Substantive research remains subject to the repository readiness gate in `README.md`.