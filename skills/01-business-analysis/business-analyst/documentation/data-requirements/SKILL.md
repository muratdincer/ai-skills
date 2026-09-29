---
name: data-requirements
description: "Defines data requirements from a business perspective: entities and relationships, attributes with meaning, type, format, mandatory rules, validations and allowed values, identifiers, data ownership, sources and consumers, sensitivity classification, quality expectations, retention and deletion. Use when a feature or system introduces or changes data, when a data dictionary is needed for development or migration, or when asked to 'define the data' or 'what fields do we need'."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: documentation
  title: "Define data requirements"
  related: "conceptual-data-model, data-classification, data-quality-rules, retention-policy, frd-writing"
  prompt: "Define the data requirements for the supplier onboarding feature: supplier, contacts, bank details and documents."
---

# Define Data Requirements

## Purpose
Specify what data the business needs, what it means, who owns it, how good it must be and how long it may be kept, so that design, integration, migration and privacy decisions rest on an agreed data definition.

## When to use
- A new feature or system creates, changes or consumes business data.
- Developers, integrators or a migration team need a business-level data dictionary.
- Personal or sensitive data is involved and handling rules must be decided early.

## When not to use
- A conceptual or logical model for a whole domain is needed. Use `conceptual-data-model` or `logical-data-model`.
- Only measurable data quality rules are needed for an existing dataset. Use `data-quality-rules`.
- Field-to-field mapping between two systems is needed. Use `field-mapping` or `source-to-target-mapping`.

## Inputs
Required:
- The feature, process or system scope and the information it handles (in any form: forms, reports, notes).

Optional, improves quality:
- Existing data dictionary or schema, glossary, business rules, regulations (KVKK/GDPR, sector retention rules), data owners, sample records (masked).

If the scope is missing, ask for it. Never ask for real personal data; work with field names and masked samples.

## Process
1. List the business entities from the input (nouns that have identity and lifecycle), and the relationships with cardinality ("a supplier has 1..n contacts").
2. For each entity, define its business meaning in one sentence using glossary terms, its identifier (natural and/or system) and its lifecycle states.
3. List attributes per entity with business definition, data type, format/length, mandatory (always, conditional with condition, optional), default, allowed values or reference list, and unit or currency.
4. Write validation rules per attribute and across attributes (e.g. end date ≥ start date); reference business rule IDs where they exist.
5. Identify the source of each attribute (user entry, system, external interface, derived with formula) and its consumers (screens, reports, interfaces).
6. Assign data ownership: business owner (defines meaning and quality) and data steward; mark unknown owners `[UNKNOWN]`.
7. Classify sensitivity per attribute (public, internal, confidential, personal, special category personal) and note masking, access and minimization needs under KVKK/GDPR.
8. State quality expectations: completeness, uniqueness, accuracy source, timeliness; and the behavior on bad data.
9. State retention, archiving and deletion or anonymization rules with their legal or business basis; unknown periods are `[TBD]`, never guessed.
10. Note migration or history needs (existing data to load, audit trail, versioning), and list assumptions and open questions with owners.
11. If the goal continues, suggest `data-classification` for detailed classification, `data-quality-rules` for measurable checks, or `retention-policy` for retention decisions.

## Output format
```markdown
# Data Requirements: <feature / system>
## Entities and Relationships
| Entity | Definition | Identifier | Lifecycle states | Relationships |
## Attributes: <Entity>
| Attribute | Definition | Type / format | Mandatory | Allowed values / default | Validation | Source | Consumers | Sensitivity |
## Ownership
| Entity | Business owner | Data steward |
## Quality Expectations
## Retention and Deletion
| Entity / attribute | Retention | Basis | End-of-life action |
## Migration and History Needs
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every entity has a business definition, identifier and relationships with cardinality.
- [ ] Every attribute has definition, type, mandatory rule and source.
- [ ] Sensitivity is classified per attribute, with privacy handling for personal data.
- [ ] Retention and deletion are stated with basis or marked `[TBD]`.
- [ ] Every entity has a business owner or an open question naming who decides.
- [ ] No real personal data appears; no values or periods were invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Copying database columns as requirements. Start from business meaning; physical design follows.
- Leaving "mandatory" unconditional when it depends on type or status. Write the condition ("mandatory if supplier type = foreign").
- Collecting data "just in case". Each personal attribute needs a purpose; otherwise drop it (data minimization).

## Example
Input: "Supplier onboarding: company info, contacts, bank account, certificates."

Excerpt of output:
| Attribute | Definition | Type / format | Mandatory | Validation | Source | Sensitivity |
|---|---|---|---|---|---|---|
| Tax number | Tax identifier of the supplier company | Text, 10 digits `[ASSUMPTION: domestic]` | Yes, if supplier type = domestic | Checksum per tax authority rule `[TBD]` | Supplier entry | Internal |
| IBAN | Bank account for payments | Text, IBAN format | Yes | Valid IBAN; account holder = company name | Supplier entry, verified by Finance | Confidential |
| Contact phone | Business phone of the contact person | Text, E.164 | Optional | Valid format | Supplier entry | Personal |

Retention: supplier records kept for `[TBD – legal basis from Legal]` after the relationship ends, then anonymized.
