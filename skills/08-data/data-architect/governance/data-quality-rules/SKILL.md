---
description: "Defines testable data quality rules for a dataset or data product across completeness, validity, uniqueness, consistency, referential integrity, timeliness and volume, each with a threshold, severity, on-failure action and owner. Use when a dataset needs quality checks, a data contract needs its quality section, recurring data issues must be prevented, or someone asks which checks to put on a table or pipeline."
related: "data-contract, data-catalog-entry, pipeline-spec, business-rules-catalog, pipeline-failure-analysis"
prompt: "Define data quality rules for the customer and orders tables that feed our monthly revenue report."
---

# Define Data Quality Rules

## Purpose
Turn vague "the data must be correct" expectations into a small set of executable, owned checks with clear thresholds and actions, so bad data is stopped or flagged before it reaches decisions.

## When to use
- A new dataset, pipeline or data product is going to production.
- Consumers repeatedly find wrong, missing, duplicated or late data.
- A data contract or certification requires explicit quality expectations.

## When not to use
- The full producer-consumer agreement (SLAs, versioning) is needed. Use `data-contract`.
- A specific incident with bad data must be diagnosed. Use `pipeline-failure-analysis`.
- Business rules of an application (not data checks) are being catalogued. Use `business-rules-catalog`.

## Inputs
Required:
- The dataset(s) with schema or field list, and at least one consumer use case the data must serve.

Optional:
- Known issues and past incidents, data volume and load pattern, business rules, reference data, existing checks, sensitivity classification.

If neither schema nor use case is given, ask for them; rules without a use case cannot be prioritized.

## Process
1. Establish the grain and key of each dataset and the critical data elements (CDEs): fields whose errors change a decision, a financial number or a regulatory report.
2. Derive failure modes from the use case and history: what wrong data would look like and what it would cost. Mark failure modes you infer, not observed, as `[ASSUMPTION]`.
3. Write rules per dimension, starting with CDEs: completeness (not null, required populations), validity (type, range, pattern, allowed values), uniqueness (key and business key), consistency (cross-field and cross-dataset, e.g. line totals equal header total), referential integrity (orphans), timeliness (freshness lag), volume (row count vs. baseline, distribution drift).
4. Express each rule as a precise, tool-neutral predicate or SQL-like expression and state the population it runs on (all rows, today's partition, changed rows).
5. Set thresholds: absolute (zero duplicates on key) or tolerance-based (null rate below x %, volume within ±y % of trailing baseline). Unknown thresholds are `[TBD]` with a proposed method to calibrate from history.
6. Assign severity and action: Critical blocks publication or quarantines the batch; Major publishes with a warning and a ticket; Minor is logged for trend. Tie severity to consumer impact, not to rule type.
7. Decide where each rule runs: at source/producer, at ingestion gate, after transformation, or as reconciliation against the source of record. Prefer the earliest point that can detect it.
8. Assign ownership: who fixes the data (producer), who is notified (consumers, steward) and the response expectation.
9. Define measurement and reporting: pass rate per rule, trend, quality score per dataset if required, and how exceptions are reviewed.
10. Prune: remove rules nobody will act on and duplicates of constraints already enforced by the database schema.
11. List assumptions and open questions. If the goal continues, suggest `data-contract` to embed the rules, `pipeline-spec` to wire them into the pipeline, or `data-catalog-entry` to publish quality status.

## Output format
```markdown
# Data Quality Rules: <dataset / product>
Grain: <...> | Key: <...> | CDEs: <list> | Owner: <producer team> | Steward: <...>

| ID | Dimension | Field(s) | Rule (predicate) | Population | Threshold | Severity | On failure | Runs at | Owner |
|---|---|---|---|---|---|---|---|---|---|
| DQ-01 | Uniqueness | order_id | count(*) = count(distinct order_id) | daily partition | 0 violations | Critical | quarantine batch | post-load | Checkout team |

## Reconciliation
- <source vs. target control totals, counts, sums>

## Reporting
- Metrics: <pass rate, trend> | Review: <cadence, forum>

## Assumptions and Open Questions
- [ASSUMPTION] ...
- [TBD] ...
```

## Quality checklist
- [ ] Every CDE has at least one rule; non-critical fields are not over-tested.
- [ ] Every rule is an unambiguous predicate with a defined population.
- [ ] Every rule has a threshold (or `[TBD]` with a calibration method), severity, action and owner.
- [ ] At least one reconciliation or volume check covers silent data loss.
- [ ] Timeliness is checked against the consumer's need, not the load schedule.
- [ ] Rules duplicating schema constraints were removed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Hundreds of generated not-null checks nobody reads. Start from CDEs and failure modes; alert fatigue kills quality programs.
- Static volume thresholds on seasonal data. Compare to a same-weekday or trailing baseline instead.
- Checks that only alert. Without a block/quarantine decision and an owner, Critical rules change nothing.
- Validating only the target. Missing rows are invisible without source-to-target reconciliation.

## Example
Input: "customers and orders feed the monthly revenue report; last quarter duplicates inflated revenue."

Excerpt of output:
- DQ-01 Uniqueness, orders.order_id, 0 duplicates per load, Critical, quarantine batch, post-load, Checkout team.
- DQ-04 Consistency, sum(order_lines.amount) = orders.total_amount per order, tolerance 0.01, Major, publish with warning.
- DQ-07 Volume, daily orders within ±30 % of same weekday over last 4 weeks `[ASSUMPTION: calibrate from history]`.
