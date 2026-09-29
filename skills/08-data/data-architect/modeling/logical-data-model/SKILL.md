---
description: "Turns a conceptual model or requirements into a normalized logical data model with entities, attributes, domains, primary/alternate/foreign keys, constraints and history handling, still independent of a specific database product. Use when preparing physical schema design, validating requirements against data, or when asked for an ERD, 3NF model or attribute-level model."
related: "conceptual-data-model, database-schema-design, data-requirements, business-rules-catalog, data-classification"
prompt: "Derive a logical data model in 3NF from this conceptual model and the attached field list for the claims domain."
---

# Build a Logical Data Model

## Purpose
Define exactly what data is held, at attribute level, with keys and rules that guarantee integrity, so physical design, integration mappings and quality rules can be derived without re-interpreting the business.

## When to use
- A conceptual model exists and implementation or integration design is next.
- Requirements, screens or reports must be checked for missing or conflicting data.
- An existing schema must be reverse-engineered into a clean, reviewable model.

## When not to use
- Business vocabulary and scope are not yet agreed. Use `conceptual-data-model` first.
- Engine-specific tables, indexes, partitioning and types are needed. Use `database-schema-design`.
- The model is for analytics star schemas. Use `dimensional-model`.

## Inputs
Required:
- Conceptual model or entity list for the scope, and attribute sources (requirements, field lists, screens, existing schemas).

Optional:
- Naming standards, domain (data type class) catalogue, enterprise reference data.
- Business rules catalogue, volumes, regulatory retention and privacy constraints.

If there is no entity list and no source of attributes, ask for them.

## Process
1. Carry over entities and relationships from the conceptual model; resolve business-meaningful M:N into associative entities.
2. Assign attributes to the entity whose identity they describe; reject derived or report-only values unless they are stored facts (mark derivations separately).
3. Define attribute domains (identifier, code, name, amount+currency, quantity+unit, date, timestamp with zone, flag, free text) with length/precision and allowed values.
4. Identify natural/business keys and alternate keys; propose surrogate keys only as a logical convenience and never instead of a declared business key.
5. Normalize to 3NF (BCNF where cheap): remove repeating groups, partial and transitive dependencies. Document any deliberate denormalization with its reason.
6. Apply patterns where they fit: party-role, supertype/subtype (state exclusive/inclusive, complete/incomplete), reference/code tables, hierarchies (adjacency vs. bridge).
7. Decide temporal handling per entity: current only, effective-dated (valid from/to), bitemporal (valid + transaction time), or event log. Tie each choice to a stated business or audit need.
8. Define referential integrity with optionality and delete behaviour intent (restrict, cascade, soft delete) and business constraints (uniqueness, ranges, cross-attribute rules).
9. Tag attributes with sensitivity (personal, special category, confidential) and flag candidates for masking or minimization.
10. Trace each attribute to its source requirement or field; list requirements with no attribute and attributes with no requirement.
11. Record open issues and assumptions.
12. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest the next skill: `database-schema-design` for the physical design, or `data-classification` for attributes carrying personal data.

## Output format
```markdown
# Logical Data Model: <scope> (v<x>)
## Diagram
<ERD as diagram-as-code, crow's foot notation>

## Entity: <Name>
Definition: <...> | Business key: <attrs> | Temporal: <current / effective-dated / bitemporal / event>
| Attribute | Domain | Null? | Key | Allowed values / rule | Sensitivity | Source |
|---|---|---|---|---|---|---|

## Relationships and Integrity
| Parent | Child | Cardinality | FK | On delete | Rule |
|---|---|---|---|---|---|

## Denormalization and Pattern Decisions
- <decision> — <reason>

## Traceability Gaps
- Requirements without attributes: ...
- Attributes without requirements: ...

## Open Questions / Assumptions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every entity has a declared business key, not only a surrogate.
- [ ] No transitive or partial dependencies remain unless documented as deliberate.
- [ ] Amounts carry currency, quantities carry units, timestamps state time zone semantics.
- [ ] Temporal handling is decided per entity and justified.
- [ ] Sensitive attributes are tagged.
- [ ] Every attribute traces to a source; gaps are listed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Generic EAV "attribute/value" tables to avoid modelling decisions. Model known attributes; limit EAV to truly user-defined extensions.
- Nullable foreign keys used to hide unclear cardinality. Resolve the rule or record it as an open question.
- Storing status only as current value when audits need history. Decide temporal needs explicitly.

## Example
Input: "Policy has holder, insured persons, coverages with limits; claims reference a policy and coverage."

Excerpt of output:
- Entity Coverage: business key (Policy No, Coverage Code, Valid From); Temporal: effective-dated because limits change at endorsements.
- Claim → Coverage: mandatory, N:1; on delete restrict.
- Insured Person.National ID: domain identifier, Sensitivity personal, mask outside claims handling.
- Open question: Can a claim span two coverages? If yes, add Claim Coverage associative entity.
