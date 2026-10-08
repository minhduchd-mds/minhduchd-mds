# GitHub Portfolio Audit — 8 October 2026

**Scope:** 67 repositories accessible from the authenticated account. This report is a snapshot, not a claim of production readiness.

## Verified overview

- **67** repositories: **36 public**, **31 private**.
- **67/67** have a `README.md` on the default branch, verified by fetching each file, including six repositories whose listing reports size 0.
- **31** repositories have blank About descriptions: **18 public** and **13 private**.
- Several non-empty descriptions are too short, promotional, or obsolete; editorial review is required beyond missing-field checks.
- This does not prove the accuracy of README text, license coverage, documentation completeness, code quality, CI success, or hardware qualification.
- Private repository names and descriptions are deliberately **not published** in this public report.

## Public repository About coverage

| Repository | README | About | Action |
| --- | --- | --- | --- |
| [quanglysinhvien](https://github.com/minhduchd-mds/quanglysinhvien) | Present | Present | Review quality |
| [student-management](https://github.com/minhduchd-mds/student-management) | Present | Present | Review quality |
| [Assignment-java](https://github.com/minhduchd-mds/Assignment-java) | Present | Present | Review quality |
| [JavaASI](https://github.com/minhduchd-mds/JavaASI) | Present | Present | Review quality |
| [youtubes](https://github.com/minhduchd-mds/youtubes) | Present | Present | Review quality |
| [template-one-page](https://github.com/minhduchd-mds/template-one-page) | Present | Present | Review quality |
| [MediaSample](https://github.com/minhduchd-mds/MediaSample) | Present | Missing | Draft and verify description |
| [Assignment](https://github.com/minhduchd-mds/Assignment) | Present | Missing | Draft and verify description |
| [Musiclove](https://github.com/minhduchd-mds/Musiclove) | Present | Present | Review quality |
| [SearchV2](https://github.com/minhduchd-mds/SearchV2) | Present | Missing | Draft and verify description |
| [Assmain](https://github.com/minhduchd-mds/Assmain) | Present | Missing | Draft and verify description |
| [Phone](https://github.com/minhduchd-mds/Phone) | Present | Missing | Draft and verify description |
| [Babyshop](https://github.com/minhduchd-mds/Babyshop) | Present | Missing | Draft and verify description |
| [JSFStruts](https://github.com/minhduchd-mds/JSFStruts) | Present | Missing | Draft and verify description |
| [JXJ](https://github.com/minhduchd-mds/JXJ) | Present | Missing | Draft and verify description |
| [Practical](https://github.com/minhduchd-mds/Practical) | Present | Missing | Draft and verify description |
| [INTXMl-ASSIAMG](https://github.com/minhduchd-mds/INTXMl-ASSIAMG) | Present | Present | Review quality |
| [quickstart-android](https://github.com/minhduchd-mds/quickstart-android) | Present | Present | Review quality |
| [identiLaxy.github.io](https://github.com/minhduchd-mds/identiLaxy.github.io) | Present | Missing | Draft and verify description |
| [cv-template-pgae](https://github.com/minhduchd-mds/cv-template-pgae) | Present | Missing | Draft and verify description |
| [homehotel](https://github.com/minhduchd-mds/homehotel) | Present | Present | Review quality |
| [Chat](https://github.com/minhduchd-mds/Chat) | Present | Present | Review quality |
| [viewpageweb.github.io](https://github.com/minhduchd-mds/viewpageweb.github.io) | Present | Present | Review quality |
| [cv-template](https://github.com/minhduchd-mds/cv-template) | Present | Missing | Draft and verify description |
| [Design-posapp](https://github.com/minhduchd-mds/Design-posapp) | Present | Missing | Draft and verify description |
| [Onepage-japan](https://github.com/minhduchd-mds/Onepage-japan) | Present | Present | Review quality |
| [angular-ivy-mxdpn7](https://github.com/minhduchd-mds/angular-ivy-mxdpn7) | Present | Present | Review quality |
| [minhduchd-mds](https://github.com/minhduchd-mds/minhduchd-mds) | Present | Present | Review quality |
| [AI-Design-Tools](https://github.com/minhduchd-mds/AI-Design-Tools) | Present | Present | Review quality |
| [AI-design.tools](https://github.com/minhduchd-mds/AI-design.tools) | Present | Missing | Draft and verify description |
| [desygn-ai](https://github.com/minhduchd-mds/desygn-ai) | Present | Present | Review quality |
| [miraai](https://github.com/minhduchd-mds/miraai) | Present | Missing | Draft and verify description |
| [open-design](https://github.com/minhduchd-mds/open-design) | Present | Present | Review quality |
| [Customer-service-bot](https://github.com/minhduchd-mds/Customer-service-bot) | Present | Missing | Draft and verify description |
| [esp32-rf-high-frequency](https://github.com/minhduchd-mds/esp32-rf-high-frequency) | Present | Missing | Draft and verify description |
| [SM-OS-mini](https://github.com/minhduchd-mds/SM-OS-mini) | Present | Missing | Draft and verify description |

## Repeatable governance

Use the scripts from the root of the public GitHub profile repository after authenticating GitHub CLI:

```bash
python3 scripts/audit_repo_portfolio.py --format markdown
python3 scripts/audit_repo_portfolio.py --include-private --format json  # keep output private
python3 scripts/sync-repo-about.py
python3 scripts/sync-repo-about.py --refresh-weak --refresh-curated
# After reviewing the exact edits:
python3 scripts/sync-repo-about.py --apply --refresh-weak --refresh-curated
```

**Policies:** no bulk archive/rename/visibility changes; no automatic invented descriptions; README state is not a passing-test badge. Do not publish a private repo audit dump or credentials. A legacy repository may have an intentionally short but factual README instead of architecture docs and production claims.

## Current implementation boundary

The connected GitHub file actions can update source files but do not expose a dedicated repository-metadata PATCH operation. Therefore this report and the synced script are committed, but **no About metadata edits have been applied** through this connection. The script is reviewed as source, not executed on the owner's authenticated machine.

See the [Kingmast Camera AI research roadmap](https://github.com/minhduchd-mds/Kingmast/blob/main/docs/CAMERA_AI_RESEARCH_2026.md) for the warning-only perception workstream.
