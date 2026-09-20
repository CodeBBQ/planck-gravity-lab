# Repository Instructions for Coding Agents

## Existing authority

Read the top-level `README.md` first and follow the repository's research, provenance, orchestration, independence, and issue-specific protocols. For bootstrap issue #6, the documented multi-session acceptance protocol remains authoritative. Project Cockpit integration must never weaken or bypass those rules.

## Project Cockpit integration

This repository is tracked in `CodeBBQ/ProjectCockpit` as **Planck Gravity Lab** (`projects/planck-gravity-lab.md`). This source repository remains authoritative for scientific/process state; Project Cockpit is only the management-level summary.

On the first meaningful interaction in a fresh working context, assess the current project state after reading the authoritative repository startup path, relevant durable audit/orchestration state, issues, current branch, recent work, and available validation evidence. Do not use an old cockpit snapshot as a substitute for repository-first startup.

Express cockpit-facing state in project-management language. Produce or refresh a Project State Assessment with: `project`, `objective`, `status` (`ACTIVE|READY|BLOCKED|PARKED|DONE`), `phase`, `current_milestone`, `progress_summary`, `recent_achievement`, exactly one `next_action`, `blockers`, `risks`, `dependencies`, `decisions_required`, `validation_status`, `relevant_issues`, `confidence` (`HIGH|MEDIUM|LOW`), and `assessed_at`.

Never invent progress, validation, blockers, GO/NO-GO state, or milestone completion. In particular, do not infer research readiness from cockpit metadata and do not begin substantive Planck-gravity research unless the repository's acceptance protocol permits it.

When the user says **"Update Project Cockpit for the current project"**, create an updated assessment. If `CodeBBQ/ProjectCockpit` is writable, update its snapshot, `PROJECTS.md`, and `CHANGELOG.md`; otherwise return the complete assessment as a handoff without pretending the cockpit was changed.

## Trello project canvas

This repository is also tracked on the project-specific Trello board **GRPlanckScale**. The repository and current GitHub issues/pull requests remain authoritative; Trello is only the operational project-management view and must not become a second source of truth.

Keep the Trello lists `Now`, `Next`, `Parallel`, `Waiting / Validation`, `Later / Backlog`, and `Done` consistent with verified repository state. After any new verified result that materially changes active work, the immediate next step, a blocker, validation state, issue/PR state, or roadmap priority, update the corresponding Trello card/list in the same working session. Do not synchronize after every commit when the management state has not materially changed.

Do not copy speculative or unverified states into Trello as facts. Trello cards should not duplicate GitHub specifications; keep only concise management context, one concrete next action, and links to authoritative repository/GitHub sources. Card titles must use plain, immediately understandable language. Keep relevant issue/PR numbers in titles when they exist, but never use a number or repository-internal shorthand as the only explanation.

Repository-specific orchestration and scientific rules remain higher authority. In particular, Trello must never be used to bypass the issue-6 acceptance protocol, worker/moderator independence, provenance requirements, or the research-start gate.
