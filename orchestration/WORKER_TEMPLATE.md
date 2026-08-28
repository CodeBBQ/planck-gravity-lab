# Worker Record Template

```yaml
id: WRK-0000
campaign: CMP-0000
agent: literature_scout
status: proposed
reason: TODO exact unresolved campaign node
task: TODO exact scoped question
spawned_by: TODO moderator decision / issue / PR
starting_context:
  required:
    - README.md
    - PROJECT_RULES.md
    - LITERATURE_RULES.md
    - REPOSITORY_ARCHITECTURE.md
    - COLLABORATION_WORKFLOW.md
    - PROVENANCE_WORKFLOW.md
    - ORCHESTRATION_MODEL.md
    - agents/README.md
    - agents/<role>.md
  include: []
  exclude_for_independence: []
depends_on: []
blocked_by: []
concurrency:
  mode: sequential # orthogonal | replication | sequential
  peers: []
branch: TODO
write_scope: []
required_outputs: []
completion_criteria: []
handoff_to: TODO
scientific_inputs: []
scientific_outputs: []
result_refs: []
followups_enabled: []
notes: null
```

## Copy-ready worker prompt

Every ready worker must have a prompt equivalent to:

```text
Worker ID: WRK-XXXX
Campaign ID: CMP-XXXX
Assigned agent: <agent>

You are executing one worker instance in CodeBBQ/planck-gravity-lab.

Bootstrap:
Follow the canonical repository startup protocol. Read the files listed in this worker record, including agents/<agent>.md and ORCHESTRATION_MODEL.md. Repository state is authoritative; do not rely on prior chat history.

Task:
<exact scoped question>

Why this worker exists:
<exact unresolved node/gap>

Scope:
<what is included>

Non-goals:
<what must not be done>

Starting context:
<accepted files/IDs deliberately supplied>

Independence constraints:
<files/conclusions deliberately excluded, or "none">

Dependencies:
<completed prerequisites>

Branch/write scope:
<branch expectation and files/directories allowed>

Required outputs:
<durable repository artifacts and scientific IDs if applicable>

Completion criteria:
<explicit test for done>

Handoff:
<next role/process and required summary>

Do not expand the task merely because adjacent questions are interesting. If a required dependency/evidence item is missing, record the blocker instead of silently changing scope.
```

A prompt must be specific enough that a fresh chat can execute the worker without additional verbal context.