---
description: "Builds a conceptual data model that names the core business entities, their definitions and relationships in business language, independent of any database technology. Use when starting a new domain, platform or integration, aligning stakeholders on vocabulary, or when asked for an entity map, subject-area model or business object model."
related: "logical-data-model, glossary-builder, bounded-context-map, event-storming, data-requirements"
prompt: "Create a conceptual data model for our B2B order-to-cash domain from these workshop notes."
---

# Build a Conceptual Data Model

## Purpose
Establish a shared, technology-neutral picture of what the business manages: the entities, what each one means, and how they relate. It is the anchor for logical models, integration contracts, governance ownership and the glossary.

## When to use
- A new domain, data product or platform is being scoped and terms are used inconsistently.
- Two systems or teams are to be integrated and each calls the same thing differently.
- A master data, governance or data mesh initiative needs subject areas and owners.

## When not to use
- Attributes, keys and normalization are needed. Use `logical-data-model`.
- The model is for analytical querying with facts and dimensions. Use `dimensional-model`.
- The need is a service/domain boundary map rather than data. Use `bounded-context-map`.

## Inputs
Required:
- The domain and its scope (processes or capabilities covered), plus any source material: workshop notes, process descriptions, requirements, existing screens or reports.

Optional:
- Existing glossary, enterprise data model or subject-area taxonomy.
- Known systems of record and data owners.
- Regulatory constraints (KVKK/GDPR, sector rules) affecting entity scope.

If scope is missing, ask for it; the model is meaningless without a boundary.

## Process
1. Fix the boundary: list the business processes/capabilities in and out of scope.
2. Harvest candidate entities from nouns in the sources; drop attributes, roles-as-screens, reports and system names.
3. Resolve synonyms and homonyms: one name per concept, record aliases, and split a term that means two things in different contexts (e.g. "Customer" as payer vs. ship-to party).
4. Write a one-sentence business definition per entity that states identity: what makes two instances the same one.
5. Classify entities: party/role, product/resource, event/transaction, agreement, location, reference/classification. Flag candidate master data.
6. Define relationships with business verb phrases in both directions and cardinality/optionality (1:1, 1:N, M:N; mandatory/optional). Keep M:N at this level unless the association carries business meaning, then name it as an entity.
7. Model roles explicitly (party-role pattern) when the same party plays several roles; avoid duplicating people/organizations per role.
8. Group entities into subject areas and propose a business owner per subject area as `[ASSUMPTION]` unless stated.
9. Note time and history semantics the business cares about (effective dating, versions, lifecycle states) without designing them.
10. Mark personal and special-category data at entity level for later classification.
11. Record open questions and conflicts in definitions; do not silently choose.
12. Produce the model as a diagram-as-code block plus the entity catalogue.
13. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest the next skill: `logical-data-model` to add attributes and keys, or `glossary-builder` to formalize the business terms.

## Output format
```markdown
# Conceptual Data Model: <domain>
Scope: <in> | Out of scope: <out> | Version/date: <...>

## Diagram
~~~mermaid
erDiagram
  CUSTOMER ||--o{ ORDER : places
~~~

## Entity Catalogue
| Entity | Definition (identity) | Type | Aliases | Subject area | Owner | Personal data |
|---|---|---|---|---|---|---|

## Relationships
| From | Verb phrase | To | Cardinality | Business rule / note |
|---|---|---|---|---|

## Lifecycle and History Notes
- <entity>: <states / effective dating the business needs>

## Terminology Decisions
- <term> means <...>; not to be confused with <...>

## Open Questions
1. <question> — <impact> — <who decides>
```

## Quality checklist
- [ ] No technical artefacts: no surrogate keys, data types, tables or system names as entities.
- [ ] Every entity has an identity-defining definition, not a circular one.
- [ ] Every relationship reads as a business sentence in both directions with cardinality.
- [ ] Synonyms are merged and homonyms split, with aliases recorded.
- [ ] Owners not given by the user are marked `[ASSUMPTION]`.
- [ ] Entities carrying personal data are flagged.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Modelling the current system's tables and calling it conceptual. Derive from business language, then check against systems.
- One giant "Customer" entity for every party role. Use party-role to keep identity and role separate.
- Over-detail: 60 entities for a workshop audience. Keep to the entities the business can name and defend, typically 10-30 per domain.

## Example
Input: "Sales takes orders from customers; invoices go to the head office; deliveries go to branches."

Excerpt of output:
- Party (organization) plays roles Sold-to, Bill-to, Ship-to; `[ASSUMPTION]` a branch is a Party linked to its head office via "is part of".
- Relationship: Order "is billed to" exactly one Bill-to role; a Bill-to role "is billed for" zero or many Orders.
- Open question: Can one order be delivered to several branches? — changes Order/Delivery cardinality — Sales operations.
