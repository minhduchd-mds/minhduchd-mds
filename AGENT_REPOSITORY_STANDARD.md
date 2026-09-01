# MDS Repository Agent Standard

This document defines when and how a repository in `minhduchd-mds` should be agent-enabled.

## 1. Repository classes

### A. Active product
Must have a repository-specific agent layer.

Minimum:
- `CLAUDE.md` or an existing canonical `AGENTS.md` referenced by `CLAUDE.md`;
- `.claude/agents/<domain-planner>.md`;
- `.claude/agents/change-reviewer.md`;
- `.claude/commands/plan-upgrade.md`;
- source/provenance policy;
- build/test/security gates appropriate to the stack.

### B. Active library/tool
Use the same structure, but planner/reviewer must focus on contracts, deterministic algorithms, compatibility, performance, and provenance rather than product UI.

### C. Legacy product being modernized
Add agents only after defining a behavior/regression baseline. Planner must favor vertical-slice/strangler migration over a big-bang rewrite.

### D. Learning/history/archive candidate
Do not add agent infrastructure. Keep the repository as historical evidence or archive it. Avoid spending maintenance budget on assignments, duplicate demos, and superseded templates.

### E. Duplicate repository
Choose a canonical code-bearing repository first. Do not independently evolve two copies. Preserve history, document the consolidation decision, then archive/redirect the duplicate when safe.

## 2. Required separation of roles

A builder must not be the only reviewer of its own patch.

Default flow:

`Product/Domain Planner -> Builder(s) -> Independent Change Reviewer -> Test/Eval -> Human merge gate`

Create additional specialist agents only when they own a stable domain boundary (security, data, geospatial, design transformation, analytics, etc.). Do not create agents merely to split job titles.

## 3. Planning output

For non-trivial work, the planner must produce:
- target user/job and product outcome;
- current-state repository evidence;
- affected boundaries/contracts;
- dependency-aware task graph;
- acceptance criteria and test/evaluation oracle;
- migration and rollback;
- observability/performance/security impact;
- provenance/license notes.

## 4. Command/tool permissions

Custom commands should request the minimum tools needed. Planning commands are read-only by default and should not silently edit, commit, deploy, or publish.

Write/deploy/release capabilities require an explicit user request and repository-specific gates.

## 5. Security

- Never hardcode credentials or infrastructure secrets.
- Runtime `.env` files stay untracked; examples contain placeholders only.
- A secret committed to Git history is considered exposed until rotated/revoked.
- Agent hooks/commands must not broaden shell or network permissions without a documented need.
- Untrusted repository/user content must not be interpolated into shell commands or model instructions without validation/sanitization.

## 6. Provenance and copyright

The component organization used for this standard was informed by `davila7/claude-code-templates`:
- URL: https://github.com/davila7/claude-code-templates
- reviewed upstream main commit: `618365a60f59db76dd91693996dc6d5f5b1cd86d`
- upstream license: MIT
- concepts learned: repo-local instructions, specialist agents, bounded commands, component validation/security discipline.

MDS repository prompt bodies and product/domain rules are written independently. No upstream prompt body or implementation code should be copied by default.

If any implementation is adapted in the future, record exact source URL, revision/version, license, required notices, and modifications in that repository's provenance document.

## 7. Current agent-enabled product set

Initial 2026-08 rollout:
- `open-design` — execution/runtime plane;
- `desygn-ai` — design intelligence product;
- `Design-hub` — knowledge plane;
- `Genbi` — governed analytics;
- `AI-design.tools` — design transformation/tool plane;
- `Chat-hub` — human/agent communication hub;
- `Appallinone` — progressive legacy modernization;
- `Dashbord-odo` — data-first decision dashboard;
- `Tracking-map-to-taxi---v.1` — realtime geospatial direction;
- `vss-employee-experience-management-` — enterprise employee-experience modernization.

Repositories already designated for separate exclusion, merge, consolidation, or archival should not receive this layer until their canonical product role is decided.
