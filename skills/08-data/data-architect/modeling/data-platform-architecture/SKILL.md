---
description: "Designs a vendor-neutral data platform architecture: ingestion, storage and processing layers, serving patterns, governance, security, operating model and the choice between warehouse, lakehouse, mesh or hybrid, with decisions traced to requirements. Use when defining a target data platform, modernizing a legacy warehouse, or when asked for a lakehouse, data mesh or reference data architecture."
related: "target-state-architecture, technology-selection, adr, data-contract, cloud-cost-estimate"
prompt: "Design a target data platform for a manufacturer with SAP, MES and IoT sources, BI and ML consumers, and a small central data team."
---

# Design a Data Platform

## Purpose
Produce a target architecture for how data is ingested, stored, processed, governed and served, with each major decision justified by requirements and constraints, so that technology selection, roadmap and team design follow from it rather than drive it.

## When to use
- A new or target-state data platform must be defined.
- A legacy warehouse or fragmented lake is to be modernized or consolidated.
- Leadership asks whether to adopt lakehouse, data mesh or a hybrid and what it means.

## When not to use
- Only a product must be chosen among candidates. Use `technology-selection`.
- A single pipeline is being specified. Use `pipeline-spec`.
- The whole enterprise target state (not only data) is needed. Use `target-state-architecture`.

## Inputs
Required:
- Business drivers and main consumers (BI, operational analytics, ML/AI, data sharing, regulatory reporting).
- Source landscape (systems, types: OLTP, SaaS, files, events/IoT) and rough volumes/latency needs.

Optional:
- Current architecture and pain points, cloud/on-prem constraints, data residency (KVKK/GDPR), team size and skills, budget envelope, existing contracts.

If drivers or sources are missing, ask; otherwise mark design choices as `[ASSUMPTION]`.

## Process
1. Turn drivers into architecture-significant requirements: latency classes (batch, micro-batch, streaming), freshness SLAs, concurrency, retention, residency, availability, cost ceiling, self-service level.
2. Choose the organizational pattern first: centralized platform, hub-and-spoke, or domain-oriented (mesh). Mesh needs domain teams able to own data products; otherwise design for it later.
3. Define ingestion patterns per source class: CDC for OLTP, API/batch extraction for SaaS, file landing with manifest, event streaming for IoT/applications. Specify contract and schema registry use.
4. Define storage layers with clear contracts: raw/landing (immutable, source-faithful), integrated/cleansed (conformed, deduplicated), curated/serving (marts, data products, features). State formats generically (open table format, columnar) and ownership per layer.
5. Choose processing styles per layer: ELT in the platform, stream processing, and where transformation logic lives (versioned, tested code).
6. Define serving: SQL warehouse/lakehouse endpoints, semantic layer and metric definitions, APIs/reverse ETL for operational use, feature store for ML, secure sharing for external parties.
7. Design cross-cutting concerns: catalog and lineage, data quality and observability, access control (RBAC/ABAC, row/column security, masking), encryption and key management, retention and deletion, cost attribution per domain.
8. Define the operating model: platform team vs. domain teams, data product ownership, contract and change process, on-call for data incidents.
9. Assess options (e.g. warehouse-centric, lakehouse, hybrid) against requirements in a trade-off table; record key choices as ADR candidates.
10. Identify migration approach and phases if replacing a legacy platform (strangler by domain/consumer, parallel run, reconciliation).
11. List risks, open questions and non-negotiables.

## Output format
```markdown
# Data Platform Architecture: <organization/scope>
## Drivers and Architecture-Significant Requirements
| Requirement | Target | Source/assumption |
|---|---|---|

## Context and Layer Diagram
<diagram-as-code: sources → ingestion → raw → integrated → curated → serving → consumers>

## Layer Definitions
| Layer | Purpose | Format / retention | Owner | Contract/quality gate |
|---|---|---|---|---|

## Ingestion and Processing Patterns
| Source class | Pattern | Latency | Notes |
|---|---|---|---|

## Serving and Consumption
- ...

## Governance, Security and Privacy
- ...

## Operating Model
- ...

## Options and Trade-offs
| Criterion | Option A | Option B | Option C |
|---|---|---|---|

## Decisions (ADR candidates)
- ...

## Migration Phases, Risks and Open Questions
- ...
```

## Quality checklist
- [ ] Every layer has a stated contract, owner and quality gate.
- [ ] Latency and freshness targets are explicit per consumer class.
- [ ] Privacy, residency, access control and deletion are designed, not deferred.
- [ ] Organizational pattern matches team capability.
- [ ] Options are compared against requirements, not feature lists; the design stays vendor-neutral.
- [ ] Cost drivers and attribution are addressed.

## Common pitfalls
- Choosing products first and drawing the architecture around them. Derive capabilities from requirements, then select.
- Declaring a data mesh without domain ownership, funding or a self-serve platform. Name the prerequisites.
- Copying raw data into many zones without contracts, producing a swamp. Each layer must have entry criteria.
- Designing streaming everywhere when consumers need daily data. Match latency to real need.

## Example
Input: "Manufacturer, SAP ERP + MES + IoT sensors; BI and predictive maintenance; 5-person data team; on-prem ERP."

Excerpt of output:
- Pattern: centralized platform with domain-aligned curated zones; mesh deferred `[ASSUMPTION: team size too small for domain ownership]`.
- IoT: event streaming into raw with 30-day hot retention, downsampled aggregates in curated for ML features.
- Decision candidate: open table format for raw/integrated to avoid engine lock-in.
