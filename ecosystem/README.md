# MDS Ecosystem Control Plane

This directory is the machine- and human-readable control plane for the active product ecosystem. It does not contain product implementation code; it defines ownership, capabilities, dependencies, lifecycle, quality gates and release discipline shared across flagship repositories.

## Why this exists

The portfolio has evolved from independent experiments into a connected product system. A central control plane prevents duplicated capabilities, unclear ownership and agent-driven changes that optimize one repository while damaging another.

## Core rule

Each capability has one primary owner. Other repositories consume it through contracts, packages, APIs, MCP tools or documented interfaces instead of reimplementing it.

## Artifacts

- `ecosystem.manifest.json` — active product registry and relationships.
- `product-manifest.schema.json` — portable manifest contract for individual repositories.
- `capability-matrix.md` — ownership of shared capabilities.
- `dependency-map.md` — intended product/data/tool/execution relationships.
- `quality-gates.md` — minimum evidence required before release.
- `roadmap.md` — ecosystem-level delivery priorities.
- `lifecycle-policy.md` — flagship/incubator/history/archive rules.
- `release-policy.md` — batching and release discipline.
- `agent-contract.md` — constraints for repository agents.

## Product planes

```text
Product       desygn-ai / GenBI / Chat-hub / Dashbord-odo
Knowledge     Design-hub
Tool          AI-design.tools
Execution     open-design
Domain        Tracking / VSS / Appallinone
Control       this repository
```
