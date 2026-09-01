# Ecosystem Quality Gates

A flagship/active repository is not release-ready merely because it builds.

## Required gates

1. **Build** — reproducible install/build on a supported runtime.
2. **Test** — domain invariants and changed behavior covered by automated tests.
3. **Type/lint** — typed boundaries and static checks where the stack supports them.
4. **Security** — no tracked runtime secrets; auth/input boundaries reviewed.
5. **Provenance** — borrowed/adapted code, assets, formulas and vendored dependencies documented.
6. **UX** — loading, empty, error and keyboard/focus states for changed user flows.
7. **Regression** — legacy behavior preserved or migration delta explicitly accepted.
8. **Observability** — production-critical flows expose enough evidence to diagnose failure.
9. **Rollback** — schema/deploy/high-risk migrations have a safe recovery path.
10. **Independent review** — builder is not the sole evaluator of its own change.

## AI-specific gates

- Typed/validated AI output at privileged boundaries.
- Model cannot directly become the source of business truth.
- Cost/token budget for repeated agent workflows.
- Evidence/confidence surfaced where recommendations can materially change behavior.
