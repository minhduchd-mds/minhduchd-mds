# Release and Push Policy

## Batch discipline

Default working cadence is **10 internal work sessions/checkpoints per push batch** when practical. Internal work may include planning, implementation, tests, refactor, UX review, security review and final verification.

The purpose is to avoid noisy history, not to hide risky changes. Emergency security fixes and changes requiring isolated review may be pushed separately.

## Preferred Git history

- One coherent batch → one squash/curated commit when possible.
- Do not create one commit per trivial file edit.
- Do not combine unrelated product changes solely to reduce commit count.
- Commit message states product outcome, not tool activity.
- Main/default branch should represent an understandable product state.

## Release evidence

Before tagging/releasing, record: build/test result, migration notes, known risks, provenance changes and rollback path.
