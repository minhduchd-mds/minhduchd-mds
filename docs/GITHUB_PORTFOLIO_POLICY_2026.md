# MDS GitHub Portfolio Documentation Standard — 2026

**Applies to:** the repositories owned by `minhduchd-mds`.  
**Maintainer intent:** accurate presentation and low-maintenance documentation, not cosmetic claims of product completeness.

## 1. Requirements by repository category

| Category | README.md | docs/ | About description | CI / governance |
| --- | --- | --- | --- | --- |
| Active product | Required, product-specific | Architecture, ADRs, verification, security and provenance where applicable | Specific purpose and scope; <=160 chars preferred | Automated checks, supported dependency/security gates |
| Active library/tool | Required, API and examples | Contracts, compatibility, migration notes | Brief capability and target audience | Unit/contract tests, version policy |
| Hardware / AI research | Required, experimental scope | BOM, model provenance, calibration, safety/test evidence and limitations | Explicitly mark research/prototype | Hardware targets, failure scenarios, evidence integrity |
| Legacy/learning/history | Required, short and factual | Optional: only add for useful historical decisions | Mark historical/learning | Don't add heavyweight infrastructure solely for appearances |
| Duplicate/superseded | Required redirect when appropriate | Consolidation or migration record | Distinguish canonical repo | Archive after review, don't delete indiscriminately |

## 2. README minimum contract

1. **Title and maturity**: active / research / legacy; release state if known.
2. **About**: the project's actual purpose and whom it serves; don't infer claims from repo names alone.
3. **Core capabilities**: distinguish implemented, experimental and planned.
4. **Repository structure**: code-bearing top-level folders.
5. **Setup**: verified commands and explicit prerequisites, or clearly say unverified.
6. **Testing**: runnable instructions and evidence location, or explicit absence.
7. **Security/privacy**: sensitive data, network endpoints, credentials and limitations as applicable.
8. **License/provenance**: cite upstream code, datasets and model licenses.
9. **Roadmap/known limitations**: no fabricated green checks or performance claims.

## 3. GitHub About field (not the README heading)

The small description shown on GitHub's repository home page is separate from the README. This connection supports README file writes but does not expose an account/repository metadata update action. A safe, review-first GitHub CLI utility is provided at [`scripts/sync-repo-about.py`](../scripts/sync-repo-about.py).

```bash
gh auth login
python3 scripts/sync-repo-about.py
python3 scripts/sync-repo-about.py --include-private
# Inspect every proposed description before enabling write.
python3 scripts/sync-repo-about.py --apply --include-private
```

**Default safeguards:** dry-run mode, no changes to existing descriptions, no repository visibility changes, no automatic topic/homepage rewrites, archived repositories excluded. For README files without an explicit `## About` section the script uses a neutral fallback; curate those descriptions manually after the first pass.

GitHub CLI reference: https://cli.github.com/manual/gh_repo_edit

## 4. Portfolio visibility and classification

- The public profile should feature only public, verifiable projects with substantive content.
- Private customer/company files, internal endpoints and product details should **not** be copied into public READMEs or a public catalog.
- Keep historical exercises clearly labeled rather than presenting dozens of unrelated learning repositories as mature independent products.
- Consider archiving superseded/duplicate repositories **only after** confirming a canonical replacement and preserving attribution.
- Avoid creating CI/agent templates in empty or retired repos simply to increase a repository count.

## 5. Proposed recurring checks

- Audit all repositories: README existence, About description, archived/private state, last activity and ownership.
- For active projects: architecture links, live setup instructions, build/test status, dependency/license scan and threat notes.
- For hardware or AI: distinguish **vendor datasheet numbers** from measured results; document operating domain, calibration, failure handling and test logs.
- For releases: publish evidence tied to the exact commit, model hash, hardware profile and test environment.

## 6. October 2026 migration summary

- Inventory scope: 67 repositories accessible under the owner during the audit.
- Twenty-three previously missing root README files received short factual project/legacy documentation.
- Existing READMEs were preserved except the intentional portfolio profile and KINGMAST research index improvements.
- Research update: KINGMAST now has a source-backed AI Camera architecture assessment under `docs/research/`.
- **Remaining operational step:** run the About-field dry-run and apply via an authorized metadata-capable GitHub CLI session. Creating a README does not automatically fill GitHub About metadata.

The accuracy of each repository-specific README and the security of its codebase must still be verified independently; presence of documentation alone is not a software-quality gate.
