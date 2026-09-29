---
name: data-contract
description: "Writes a data contract between a data producer and its consumers: schema, semantics, quality expectations, freshness and availability SLAs, ownership, access and privacy terms, versioning and change/deprecation rules, in a machine-readable-friendly form. Use when publishing a dataset, event stream or data product, onboarding a new consumer, or when asked to formalize producer-consumer expectations."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 08-data
  role: data-architect
  area: modeling
  title: "Write a data contract"
  related: "schema-evolution-plan, data-quality-rules, api-contract, data-catalog-entry, data-classification"
  prompt: "Write a data contract for the orders event stream that finance and the recommendation team consume."
---

# Write a Data Contract

## Purpose
Make the producer's promises about a dataset explicit and testable, so consumers can depend on it and producers can change it safely, turning silent breaking changes into managed versions.

## When to use
- A dataset, table, event stream or data product is exposed to other teams.
- Repeated incidents are caused by upstream schema or semantic changes.
- A new consumer is onboarded and needs guaranteed fields, freshness or quality.

## When not to use
- The interface is a synchronous service API. Use `api-contract`.
- Only the compatibility of a planned change is being assessed. Use `schema-evolution-plan`.
- Only discovery metadata is needed. Use `data-catalog-entry`.

## Inputs
Required:
- The dataset or stream (name, purpose), its schema or field list, the producer team and at least one consumer use case.

Optional:
- Existing quality issues, volume, delivery mechanism, sensitivity classification, retention needs, consumer SLAs.

If the schema or producer is unknown, ask; a contract without an accountable producer is not a contract.

## Process
1. Identify parties: producer owner (team and accountable role), consumers and their use cases, contract approver.
2. Define the interface: delivery mechanism (table, file, topic, API), location described generically, format, partitioning, primary key and event key/ordering guarantees.
3. Specify the schema per field: name, type, nullability, allowed values or ranges, unit/currency, business definition, and whether the field is part of the stable contract or experimental.
4. Specify semantics: grain, what a record represents, event-time vs. processing-time, deduplication guarantee (at-least-once, effectively-once), handling of deletes (tombstones, soft-delete flag), late data.
5. Define quality expectations as testable rules (completeness, uniqueness, validity, referential, volume thresholds) with the action on failure: block, quarantine, warn.
6. Define service levels: freshness (max lag from event), availability window, delivery schedule, support hours, incident communication path and response times.
7. Define access, privacy and usage: classification, personal data fields and legal basis, masking rules, permitted and prohibited uses, retention and deletion propagation.
8. Define versioning and change policy: semantic versioning; which changes are non-breaking (add optional field) vs. breaking (remove/rename, type narrowing, semantic change); notice period, parallel-run duration, deprecation process.
9. Define enforcement: where the contract is validated (producer CI, ingestion gate, schema registry compatibility mode) and how violations are reported.
10. Produce the contract in a structured, machine-readable-friendly layout plus a short human summary.
11. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest the next skill: `data-quality-rules` to implement the quality section, `schema-evolution-plan` for the first planned change, or `data-catalog-entry` to publish it.

## Output format
```markdown
# Data Contract: <dataset> v<MAJOR.MINOR.PATCH>
Status: <draft/active/deprecated> | Producer: <team, accountable role> | Consumers: <list>

## Interface
Mechanism: <...> | Format: <...> | Key: <...> | Ordering: <...> | Partitioning: <...>

## Schema
| Field | Type | Null | Constraint / values | Unit | Definition | Stability |
|---|---|---|---|---|---|---|

## Semantics
Grain: <...> | Time: <event/processing> | Delivery: <at-least-once/...> | Deletes: <...> | Late data: <...>

## Quality Rules
| Rule | Check | Threshold | On failure |
|---|---|---|---|

## Service Levels
Freshness: <...> | Availability: <...> | Schedule: <...> | Support: <...> | Incidents: <channel, response time>

## Access, Privacy and Usage
Classification: <...> | Personal fields: <...> | Masking: <...> | Permitted uses: <...> | Retention: <...>

## Change Policy
Breaking changes: <list> | Notice: <...> | Parallel run: <...> | Deprecation: <...>

## Enforcement
- ...
```

## Quality checklist
- [ ] Every field has a type, nullability and business definition.
- [ ] Grain, key and delivery semantics are stated.
- [ ] Quality rules are testable and each has an on-failure action.
- [ ] SLAs are numeric; unknown values are `[TBD]`, not invented.
- [ ] Breaking vs. non-breaking changes and notice periods are defined.
- [ ] Personal data, masking and retention are addressed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- A schema dump labelled as a contract. Semantics, SLAs and change policy are the valuable part.
- Contracts without enforcement. Validate in the producer pipeline and at ingestion, or they drift.
- Treating semantic changes (e.g. amount now net instead of gross) as non-breaking because the type is unchanged.

## Example
Input: "orders stream, produced by Checkout team; Finance uses it for revenue; Recommendations for purchase history."

Excerpt of output:
- Key: order_id; ordering guaranteed per order_id; delivery at-least-once, consumers deduplicate on (order_id, event_version).
- Field total_amount: decimal(18,2), not null, currency in currency_code, gross including VAT; changing to net is a MAJOR change.
- Freshness: `[TBD]` agreed max lag; Finance requires completeness by 02:00 for daily close `[confirm]`.
