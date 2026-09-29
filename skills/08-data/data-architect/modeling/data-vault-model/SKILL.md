---
description: "Designs a Data Vault 2.0 model: hubs from business keys, links for relationships and transactions, satellites split by source and rate of change, plus hash key, load date, record source and business vault constructs (PIT, bridge, effectivity). Use when building an auditable, source-integrated raw layer over many changing sources, or when asked for hubs, links and satellites."
related: "dimensional-model, logical-data-model, master-data-strategy, incremental-load-design, data-lineage-doc"
prompt: "Design a Data Vault for customer and contract data coming from CRM, core banking and a web onboarding app."
---

# Design a Data Vault Model

## Purpose
Create an integration layer that captures all source history in an insert-only, auditable form, integrates sources on shared business keys and absorbs source change with minimal rework, so downstream marts can be rebuilt at any time.

## When to use
- Many sources describe the same business concepts and change frequently.
- Full auditability and reproducibility of any past state is required (regulated industries).
- Parallel, incremental loading at scale is needed without re-modelling on each source change.

## When not to use
- A single source feeds a small reporting need. Use `dimensional-model` directly.
- The need is golden-record resolution for operations. Use `master-data-strategy`.
- An operational (OLTP) schema is being designed. Use `logical-data-model`.

## Inputs
Required:
- Source systems in scope with their entities/tables and the business keys they carry.
- The core business concepts (a conceptual model or list).

Optional:
- Change frequencies and volumes per source, CDC availability, known key collisions across sources, downstream mart requirements, privacy constraints (erasure obligations).

If business keys cannot be identified for a source, ask; guessing keys breaks integration.

## Process
1. Start from business concepts, not source tables. For each concept, identify the business key used across the enterprise (not source surrogate IDs where avoidable).
2. Resolve key collisions: when sources use different keys for the same concept, decide between a shared hub with key-mapping (same-as link) or collision codes/tenant prefix in the key.
3. Define hubs: hash key over normalized business key (trim, upper-case, fixed delimiter, collision code), business key columns, load date, record source.
4. Define links for every relationship or transaction between hubs, with hash key over all participating hub keys. Keep links many-to-many; do not encode cardinality. Use non-historized (transactional) links for immutable events.
5. Define satellites: split by source system, by rate of change and by sensitivity (put personal data in its own satellite to enable erasure/crypto-shredding). Include hash diff for change detection, load date, record source; add effectivity satellites for link validity.
6. Handle multi-active attributes (several phones per customer) with multi-active satellites and a sub-sequence key.
7. Standardize technical rules: hashing algorithm and input normalization, load date semantics (arrival timestamp vs. applied date), ghost record, zero keys for missing references.
8. Design the business vault for derived logic: computed satellites, same-as and hierarchy links, PIT tables and bridges to make downstream queries efficient.
9. Specify loading patterns: hubs and links insert-if-not-exists, satellites insert-if-hash-diff-changed; all loads idempotent and parallel within a layer.
10. Map raw vault to downstream information marts (virtualized dimensions/facts from PIT + satellites).
11. Check each source attribute lands in exactly one satellite; list unmapped attributes.

## Output format
```markdown
# Data Vault Model: <scope>
## Hubs
| Hub | Business key (normalized) | Collision handling | Sources |
|---|---|---|---|

## Links
| Link | Hubs | Type (standard / non-historized / same-as / hierarchy) | Driving key (if effectivity) |
|---|---|---|---|

## Satellites
| Satellite | Parent | Source | Change rate | Attributes | Sensitive? | Multi-active? |
|---|---|---|---|---|---|---|

## Technical Standards
- Hash: <algorithm>, input normalization: <rules>
- Load date: <semantics> | Record source: <format> | Zero/ghost keys: <...>

## Business Vault
- PIT: <hub + satellites, snapshot frequency>
- Bridge / computed satellites: <...>

## Downstream Mapping
| Mart object | Built from |
|---|---|

## Open Questions / Assumptions
- ...
```

## Quality checklist
- [ ] Every hub is based on a real business key, and key collisions are resolved explicitly.
- [ ] Links carry no descriptive attributes; relationships are not encoded in hubs.
- [ ] Satellites are split by source and change rate; personal data is isolated.
- [ ] Hashing and load-date rules are specified once and applied everywhere.
- [ ] Loads are insert-only and idempotent.
- [ ] Every source attribute is mapped to exactly one satellite.

## Common pitfalls
- Source-system vault: one hub per source table with technical IDs, which integrates nothing. Model around business concepts.
- Putting business rules in the raw vault. Keep raw vault source-faithful; apply rules in the business vault.
- Querying the raw vault directly for BI. Provide PIT/bridge structures and marts.
- Ignoring erasure obligations in an insert-only model. Isolate personal data so it can be deleted or shredded.

## Example
Input: "Customer from CRM (CRM_ID), core banking (customer number) and web onboarding (email)."

Excerpt of output:
- Hub Customer: business key = core banking customer number; same-as link maps CRM_ID and onboarding email to it.
- Satellites: Sat Customer CRM (weekly changes), Sat Customer Core (daily), Sat Customer PII (name, national ID, contact; isolated for erasure).
- Link Customer-Contract with effectivity satellite, driving key Contract.
