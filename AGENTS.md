# Repository Instructions for Coding Agents

## Existing authority

Read the top-level `README.md` first and follow the repository's research, provenance, orchestration, independence, and issue-specific protocols. For bootstrap issue #6, the documented multi-session acceptance protocol remains authoritative. Project Cockpit integration must never weaken or bypass those rules.

## Project Cockpit integration

This repository is tracked in `CodeBBQ/ProjectCockpit` as **Planck Gravity Lab** (`projects/planck-gravity-lab.md`). This source repository remains authoritative for scientific/process state; Project Cockpit is only the management-level summary.

On the first meaningful interaction in a fresh working context, assess the current project state after reading the authoritative repository startup path, relevant durable audit/orchestration state, issues, current branch, recent work, and available validation evidence. Do not use an old cockpit snapshot as a substitute for repository-first startup.

Express cockpit-facing state in project-management language. Produce or refresh a Project State Assessment with: `project`, `objective`, `status` (`ACTIVE|READY|BLOCKED|PARKED|DONE`), `phase`, `current_milestone`, `progress_summary`, `recent_achievement`, exactly one `next_action`, `blockers`, `risks`, `dependencies`, `decisions_required`, `validation_status`, `relevant_issues`, `confidence` (`HIGH|MEDIUM|LOW`), and `assessed_at`.

Never invent progress, validation, blockers, GO/NO-GO state, or milestone completion. In particular, do not infer research readiness from cockpit metadata and do not begin substantive Planck-gravity research unless the repository's acceptance protocol permits it.

When the user says **"Update Project Cockpit for the current project"**, create an updated assessment. If `CodeBBQ/ProjectCockpit` is writable, update its snapshot, `PROJECTS.md`, and `CHANGELOG.md`; otherwise return the complete assessment as a handoff without pretending the cockpit was changed.