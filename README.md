# Minh Đức — Product Design · Frontend Engineering · Applied AI

**Senior-oriented UI/UX & product-engineering portfolio** · Design systems, web applications, applied AI, edge computing and engineering quality.

I work across the product lifecycle: translating ambiguous problems into usable interfaces, defining UI systems and interaction flows, and building testable implementations. My repositories include actively developed products, research prototypes and historical learning projects. Those categories should **not** be confused with shipped, certified or production-ready software.

## Featured work

| Repository | Focus | Maturity / boundary |
| --- | --- | --- |
| [miraai](https://github.com/minhduchd-mds/miraai) | Multimodal AI companion experiments, voice, computer vision and app packaging | Active R&D; hardware/device behavior must be validated |
| [desygn-ai](https://github.com/minhduchd-mds/desygn-ai) | Design intelligence, audit workflows and AI-assisted implementation | Active product experimentation |
| [open-design](https://github.com/minhduchd-mds/open-design) | Design/agent workspace with local-first execution patterns | Active tooling |
| [AI-design.tools](https://github.com/minhduchd-mds/AI-design.tools) | Practical design transformation and asset tools | Development tooling |
| [cv-template](https://github.com/minhduchd-mds/cv-template) | CV creation, editing, templates and review experiences | Product and UI/UX experimentation |
| [esp32-rf-high-frequency](https://github.com/minhduchd-mds/esp32-rf-high-frequency) | ESP32-S3 receive-only RF observatory and instrumentation | Experimental measurement platform, not a calibrated laboratory instrument |
| [SM-OS-mini](https://github.com/minhduchd-mds/SM-OS-mini) | Minimal embedded development environment for ESP32-class devices | Research prototype |
| [Customer-service-bot](https://github.com/minhduchd-mds/Customer-service-bot) | Customer-service automation and assistant architecture | Development project |

### Private research

**KINGMAST** explores warning-only automotive perception, multi-camera/radar fusion, vehicle HMI and evidence-driven safety evaluation. It is a research prototype, **not** an autonomous-driving system or certified ADAS product. Private repositories and professional/customer materials are intentionally not published as a complete public portfolio.

## Engineering standards

- **Product / UX:** measurable user goals, realistic scenarios, accessibility, responsive layout and honest error states.
- **Architecture:** explicit domain boundaries, typed contracts, progressive migration and deterministic core logic.
- **AI:** model/data provenance, offline fallback, validation data, observable failure handling and human oversight.
- **Embedded / automotive:** hardware constraints, timestamp integrity, safe degradation, read-only vehicle integration and independent evidence.
- **Security:** least privilege, secret hygiene, dependency provenance, auditable CI and safe release processes.

## Portfolio taxonomy

| Class | Expectation |
| --- | --- |
| **Active product / library** | Specific README, architecture, setup, validation steps, security and provenance notes |
| **Research prototype** | Hypothesis, test methodology, experimental limitations and measured vs. proposed results |
| **Historical exercise** | Short factual README and maintenance status; do not claim it is production-ready |
| **Duplicate / superseded** | Choose the canonical repository before future development; archive only after verification |

Detailed working rules: [Agent Repository Standard](AGENT_REPOSITORY_STANDARD.md) and [GitHub Portfolio Documentation Policy](docs/GITHUB_PORTFOLIO_POLICY_2026.md).

## October 2026 documentation audit

An authenticated file-by-file review on **8 October 2026** found **67/67 repositories with a README.md**, across **36 public / 31 private repositories**. **31 About fields are blank** (18 public / 13 private). A README file's existence is not a claim of documentation quality, source security or passing CI.

- [Portfolio audit, public-safe summary](docs/REPOSITORY_AUDIT_2026-10-08.md)
- [Read-only repository audit script](scripts/audit_repo_portfolio.py)
- [About description dry-run / opt-in sync](scripts/sync-repo-about.py)
- [Kingmast Camera AI research (private repo)](https://github.com/minhduchd-mds/Kingmast/blob/main/docs/CAMERA_AI_RESEARCH_2026.md)

The repository About synchronization script remains **dry-run by default**. The connected file-edit workflow did not modify GitHub repository About settings.

## Repository About and README audit

The portfolio has a **dry-run-first** tool to fill missing GitHub About descriptions based on repository README sections. It preserves existing descriptions, visibility, topics and homepage settings.

```bash
# Requires Python 3.10+ and GitHub CLI logged in with permissions.
python3 scripts/sync-repo-about.py
python3 scripts/sync-repo-about.py --include-private

# Run only after reviewing dry-run output:
python3 scripts/sync-repo-about.py --apply --include-private
```

The script is optional and **does not execute automatically**. See [the script](scripts/sync-repo-about.py).

## Collaboration

The work shown here spans **product design, design systems, frontend architecture, AI prototyping and embedded exploration**. Individual repositories are the source of truth for their implementation status and licensing.

> Documentation describes the state and limits of a project. It does not substitute for passing tests, hardware qualification or user validation.
