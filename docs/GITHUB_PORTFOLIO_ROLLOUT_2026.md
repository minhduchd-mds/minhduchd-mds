# Repository Portfolio Standardization — 2026-10-08

Status: **inventory and rollout plan**. No mass edits, archiving, visibility changes or auto-merges are implied.

## Inventory
GitHub connector returned **67 accessible repositories: 38 public, 29 private** on 2026-10-08. Count means accessible, not verified fully documented.

## Policies
1. Preserve existing README and accurate project history; improve, never fabricate status.
2. Each substantive repo: GitHub About (English, ~70–140 chars), 3–6 relevant topics, README, docs/ARCHITECTURE.md, docs/SETUP.md, docs/TESTING.md, SECURITY.md (for maintained projects) and license status.
3. Learning/empty/superseded repositories need concise honest README only; do not publish scaffolding presented as an active product.
4. Private projects must not leak internal architecture, credentials, user data or partner/client context into public profile summaries.
5. No empty badges and no unsupported performance/security claims. Distinguish tested, prototype, and planned features.
6. Keep current default branch (main or master); do not rename branches in bulk.
7. About changes require GitHub repository settings/API scope. Existing `scripts/sync-repo-about.py` is dry-run-first; review before `--apply`.
8. Archive/rename duplicate projects only after owner approval and replacement-link validation.

## Portfolio tiers
| Tier | Examples | Documentation |
| --- | --- | --- |
| Flagship — active | Kingmast (private), miraai, cv-template, open-design, esp32-rf-high-frequency, SM-OS-mini | Full engineering docs, reproducible tests, threat model, screenshots/demo |
| Product / tool | desygn-ai, AI-design.tools, Customer-service-bot | Purpose, quickstart, architecture, status, screenshots |
| Research / experiments | specific prototypes after individual inspection | Hypothesis, hardware, dataset, methodology, limitations |
| Historical | legacy assignments, old samples, empty repos | Short README + status; consider archival review |

## About templates
- Kingmast: `Warning-only automotive perception research: multi-camera AI, radar fusion, TTC/THW and driver-focused HMI.`
- miraai: `Multimodal AI companion research exploring voice, computer vision, gestures and cross-platform interfaces.`
- SM-OS-mini: `Minimal programmable ESP32-S3 platform researching resource management, safe runtime isolation and device I/O.`
- esp32-rf-high-frequency: `Receive-only ESP32-S3 RF observatory for signal monitoring, calibration research and reproducible experiments.`
- cv-template: `Interactive CV Studio with editable templates, PDF export and career preparation workflows.`

These are suggested copy, **not assertions that metadata was applied**.

## Rollout verification checklist
- [ ] Review existing README/description of all 67 repositories.
- [ ] Produce per-repo missing docs and About matrix.
- [ ] Flag 0-byte/legacy repos separately.
- [ ] Security and privacy review before docs changes, especially private repos.
- [ ] Edit flagships first, commit in small batches, check links and CI.
- [ ] Review dry-run output of About sync; apply only appropriate corrections.
- [ ] Report actual commits and exceptions; never claim completion without verification.
