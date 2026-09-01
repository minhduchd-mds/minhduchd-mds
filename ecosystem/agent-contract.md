# Ecosystem Agent Contract

Repository agents operate as constrained contributors, not autonomous product owners.

## Default loop

```text
Intent
  -> Product/Domain Planner
  -> Task graph
  -> Builder specialist(s)
  -> Independent reviewer/evaluator
  -> Quality gates
  -> Human-controlled release
```

## Mandatory behavior

- Read repository `README.md`, `CLAUDE.md`/`AGENTS.md`, architecture and provenance before editing.
- Determine capability ownership before creating new shared infrastructure.
- Prefer deterministic domain functions before model-driven behavior.
- Keep model/provider code behind interfaces.
- Preserve legacy behavior during progressive migrations unless a breaking change is explicit.
- Write invariant tests for ranking, ordering, scoring, migration and policy logic.
- Never expose or reproduce secrets discovered in history/configuration.
- Record external implementation provenance and licenses.
- Do not call a workflow green if CI never started or a runner was never assigned.

## Handoff envelope

Every significant agent task should be able to report: goal, changed boundaries, evidence/tests, known risks, unresolved blockers, provenance impact and recommended next action.
