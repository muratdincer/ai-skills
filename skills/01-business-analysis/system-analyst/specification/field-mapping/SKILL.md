---
description: "Produces a source-to-target field mapping between two systems or messages: each target field with its source, transformation, default, validation, code-value translation, null and error handling, plus unmapped fields on both sides and open decisions. Use when building an integration, API adapter, data exchange file or system replacement, when two systems must exchange records, or when someone asks 'which field goes where and how is it converted?'."
related: "integration-requirements, api-contract, source-to-target-mapping, data-quality-rules, error-scenario-catalog"
prompt: "Map the customer fields from our CRM export to the new billing system's customer API, including code conversions."
---

# Map Fields Between Systems

## Purpose
Remove guesswork from system integration by stating, field by field, where each target value comes from, how it is converted and what happens when the source is empty or invalid. Developers build from it and testers verify against it.

## When to use
- Two systems exchange records through an API, message, file or database link.
- A system is being replaced and its data or interfaces must be re-pointed.
- An existing interface produces wrong or missing values and the mapping must be made explicit.

## When not to use
- You need column-level lineage for a data warehouse or analytics pipeline. Use `source-to-target-mapping`.
- The interface itself (protocol, frequency, SLAs) is not yet agreed. Use `integration-requirements` first.
- You need a new API design rather than a mapping to an existing one. Use `api-contract`.

## Inputs
Required:
- Source structure and target structure: field lists, schemas, sample payloads or screen fields.
- The direction and purpose of the exchange.

Optional, improves quality:
- Code lists and reference data on both sides, sample records (masked), business rules.
- Volumes, frequency, and whether the flow is create-only or create/update/delete.

If either structure is missing, ask for it. Do not invent field names; unknown ones are `[TBD]`.

## Process
1. Confirm scope: direction, entity or message, operation types (create, update, delete, upsert) and the key used to match records across systems.
2. List target fields in target order, since the target contract decides what is required. Note type, length, format, mandatory flag and allowed values for each.
3. For each target field, find the source: direct field, several fields combined, derived by rule, constant, lookup from reference data, or no source. Quote the exact source field path.
4. Define the transformation precisely: type and format conversion (date, time zone, decimal separator, currency, encoding), trimming, concatenation or splitting, unit conversion, rounding rule.
5. Build code-value translation tables for every enumerated field (status, country, product type). Every source value maps to one target value or to an explicit error; no silent defaults.
6. Define null, empty and invalid handling per field: default value, reject record, send without field, or route to manual correction. Distinguish "empty" from "not sent" on updates.
7. List unmapped fields on both sides: source data that will be lost and target fields that stay empty. Ask the data owner to confirm each loss is acceptable.
8. Mark personal and sensitive fields and state masking, minimization or encryption; do not map personal data the target does not need.
9. Label every rule not supported by the inputs `[ASSUMPTION]`, and list open decisions with the owner (usually the data owner of the target).
10. If the user wants to continue, suggest `integration-requirements` for transport and SLAs, `data-quality-rules` for validation or `error-scenario-catalog` for rejected records.

## Output format
```markdown
# Field Mapping: <source system> → <target system> (<entity / message>)
Direction: <...> · Operations: <create / update / delete> · Match key: <source key ↔ target key>

## Mapping
| # | Target field | Type / length | Mandatory | Source field(s) | Transformation / rule | Null / invalid handling | Personal data |
|---|---|---|---|---|---|---|---|

## Code Value Translations
### <field>
| Source value | Target value | Note |
|---|---|---|

## Unmapped Fields
| Side | Field | Reason | Confirmed by |
|---|---|---|---|

## Assumptions and Open Decisions
- [ASSUMPTION] ... — owner
```

## Quality checklist
- [ ] Every mandatory target field has a source, a constant or an explicit rejection rule.
- [ ] Every enumerated field has a complete translation table including an "unknown value" rule.
- [ ] Formats for dates, time zones, decimals and currencies are stated on both sides.
- [ ] Update behaviour distinguishes "clear the value" from "field not sent".
- [ ] Unmapped fields on both sides are listed and personal data not needed by the target is excluded.
- [ ] No field name, code or rule is invented; gaps are `[TBD]` or labeled `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Mapping by field name similarity. "Status" or "Type" rarely means the same thing in two systems; confirm meaning with samples.
- Ignoring time zones and local formats. A date without a zone shifts by a day on midnight records; decimal commas break parsing.
- Applying silent defaults to failed lookups. It hides data quality problems; reject or route to correction instead.

## Example
Input: "CRM customer: FullName, Phone, SegmentCode (A/B/C), CreatedAt (local time). Billing API: firstName*, lastName*, phoneE164, segment (RETAIL/SME/CORPORATE)*, createdUtc."

Excerpt of output:
| # | Target | Mandatory | Source | Transformation | Null / invalid | Personal |
|---|---|---|---|---|---|---|
| 1 | firstName | Y | FullName | Split on last space; all but last token `[ASSUMPTION]` | Reject if empty | Y |
| 3 | phoneE164 | N | Phone | Normalize to E.164 with default country `[TBD]` | Send without field if invalid, log | Y |
| 4 | segment | Y | SegmentCode | A→RETAIL, B→SME, C→CORPORATE | Unknown code → reject | N |

Open decision: how to split multi-part surnames; owner Billing data owner.
