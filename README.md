# Minh Đức — Product Design & AI Engineering Portfolio

## About

This GitHub space is a portfolio of product-design, frontend, data, AI-agent and developer-tooling experiments that are being consolidated into a smaller set of maintainable products.

The current direction is not “add AI to every repository”. Each active product gets a clear domain, architecture boundary, testable core, source-provenance policy and an agent workflow that plans before it edits code.

## Active product ecosystem

| Project | Product role |
| --- | --- |
| [desygn-ai](https://github.com/minhduchd-mds/desygn-ai) | Design Intelligence Platform — audit, scoring, recommendations and agent-assisted implementation |
| [open-design](https://github.com/minhduchd-mds/open-design) | Local-first design/agent execution workspace |
| [Design-hub](https://github.com/minhduchd-mds/Design-hub) | Design knowledge, search and reusable enterprise patterns |
| [AI-design.tools](https://github.com/minhduchd-mds/AI-design.tools) | Design transformation, asset conversion and token intelligence tools |
| [Genbi](https://github.com/minhduchd-mds/Genbi) | Governed AI-assisted analytics and visualization planning |
| [Chat-hub](https://github.com/minhduchd-mds/Chat-hub) | Human/agent communication and deterministic realtime conversation core |
| [Appallinone](https://github.com/minhduchd-mds/Appallinone) | Progressive modernization of a legacy multi-page web product |
| [Dashbord-odo](https://github.com/minhduchd-mds/Dashbord-odo) | Data-first decision dashboard and explainable KPI prioritization |
| [Tracking-map-to-taxi---v.1](https://github.com/minhduchd-mds/Tracking-map-to-taxi---v.1) | Provider-neutral realtime geospatial tracking core |
| [vss-employee-experience-management-](https://github.com/minhduchd-mds/vss-employee-experience-management-) | Enterprise employee-experience product under staged Angular modernization |

## Engineering principles

- Product problem and measurable outcome before framework migration.
- Domain logic separated from rendering, vendor SDKs and infrastructure adapters.
- Deterministic algorithms and invariant tests for scoring, ranking, ordering and analytics logic.
- Progressive modernization instead of uncontrolled big-bang rewrites.
- Accessibility, responsive behavior, failure states and observability are acceptance criteria.
- External projects are used as conceptual/API references unless adaptation is explicitly documented.
- Third-party licenses, notices and source provenance are retained.

## Agent workflow

Active repositories follow the operating model documented in [`AGENT_REPOSITORY_STANDARD.md`](AGENT_REPOSITORY_STANDARD.md):

```text
Product / Domain Planner
        ↓
Task graph
        ↓
Builder agent(s)
        ↓
Independent reviewer
        ↓
Tests / evaluation
        ↓
Human merge gate
```

Agent infrastructure is intentionally not added to learning repositories, duplicates or archive candidates.

## Repository strategy

The portfolio is being cleaned into three groups:

1. **Active products** — maintained, documented and tested.
2. **Merge candidates** — useful code that should move into a canonical repository.
3. **Archive/history** — learning exercises and superseded prototypes kept for reference.

## Documentation standard

Every active repository should expose at least:

- `README.md` with an **About** section;
- architecture / product direction;
- setup and verification commands;
- roadmap or migration notes;
- security notes when credentials, auth or private data are involved;
- `docs/SOURCE_PROVENANCE.md` when external references or algorithms are relevant.

---

> Status: active portfolio modernization. Repository-specific README files are the source of truth for setup and implementation details.
