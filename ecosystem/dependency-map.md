# Ecosystem Dependency Map

## Intended direction

```text
                 Design-hub
              knowledge / evidence
                    │
                    ▼
AI-design.tools ─▶ desygn-ai ◀─ open-design
 tools / IR         product       execution
                    │
                    ▼
              verified changes

GenBI ───────── governed analytics product
Chat-hub ────── human / agent communication
Dashbord-odo ── decision intelligence consumer
Tracking ────── geospatial domain product
VSS ─────────── employee experience domain product
Appallinone ─── progressive modernization product
```

## Boundary rules

1. Product repositories may depend on Knowledge/Tool/Execution contracts.
2. Knowledge and Tool planes must not depend on product UI implementations.
3. Deterministic domain logic stays independent of model providers.
4. AI/model adapters live at boundaries; they do not own business truth.
5. Cross-repo coupling requires an explicit contract and versioning strategy.
6. No repository reaches directly into another repository's database.
