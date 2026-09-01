# Capability Ownership Matrix

| Capability | Primary owner | Consumers / notes |
| --- | --- | --- |
| Design intelligence, audit and scoring | `desygn-ai` | Product-facing design analysis and evidence |
| Design knowledge, patterns and retrieval | `Design-hub` | Used by design agents/products; no duplicated knowledge store |
| Agent execution, workspace and artifacts | `open-design` | Runtime for controlled file/tool execution |
| Design transformation and token intelligence | `AI-design.tools` | Expose deterministic tools; later MCP |
| Governed metrics and analytical planning | `Genbi` | Other dashboards consume metric contracts, not raw LLM SQL |
| Conversation ordering and reconnect semantics | `Chat-hub` | Shared concepts for human/agent communication |
| KPI prioritization / decision model | `Dashbord-odo` | Domain-specific decision layer, not a generic chart engine |
| Realtime geospatial state | `Tracking-map-to-taxi---v.1` | Provider-neutral map state and plausibility |
| Progressive legacy migration patterns | `Appallinone` | Reference migration strategy, not shared runtime |
| Employee experience workflows | `vss-employee-experience-management-` | Enterprise domain owner |

## Duplication rule

If a second repository needs an owned capability, prefer one of: shared package, typed HTTP API, MCP tool, event contract or documented algorithm interface. Forking implementation is the last resort and must record why isolation is required.
