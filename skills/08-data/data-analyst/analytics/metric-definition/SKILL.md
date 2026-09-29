---
description: Defines a business metric precisely enough that two analysts would compute the same number - purpose, formula, numerator/denominator, filters, grain, time logic, edge cases, source fields and owner. Use when a metric is disputed, reported differently across teams, about to be added to a dashboard or OKR, or needs to be documented in a metrics catalog.
related: kpi-definition, dashboard-spec, north-star-metric, data-quality-rules, glossary-builder
prompt: Define "active customer" precisely; finance and product report different numbers every month.
---

# Define a Metric Precisely

## Purpose
Produce an unambiguous, versioned metric definition that removes interpretation, so every report, dashboard and team computes the same number and disputes shift from "whose number is right" to "what should we do".

## When to use
- Two reports show different values for the "same" metric.
- A new KPI is being introduced to a dashboard, OKR or contract.
- A metrics catalog or semantic layer entry must be written.

## When not to use
- The need is choosing which KPIs matter for a goal. Use `kpi-definition`.
- The question is data correctness at field level. Use `data-quality-rules`.
- A single company-wide guiding metric is being chosen. Use `north-star-metric`.

## Inputs
Required:
- Metric name and the business question it should answer.

Optional, improves quality:
- Existing formulas or SQL from different teams.
- Source tables and field names.
- Known disputes or examples of mismatched numbers.

If the business question is missing, ask; otherwise mark gaps `[TBD]`.

## Process
1. Write the purpose: which decision the metric informs and what "good" direction is.
2. Define the entity and grain (per customer, per order, per day) and the population in scope.
3. Write the formula in plain language and as pseudo-SQL: numerator, denominator, aggregation (count distinct, sum, median).
4. Specify filters and exclusions explicitly: test/internal accounts, cancelled or refunded transactions, bots, currencies, tax.
5. Specify time logic: event time vs processing time, time zone, period boundaries, rolling vs calendar windows, late-arriving data and restatement policy.
6. Enumerate edge cases and their treatment: nulls, zero denominators, reactivations, merges/splits of entities, partial periods, duplicates.
7. Map to source fields and the system of record; note lineage and known quality issues.
8. If existing definitions conflict, show a reconciliation table (definition A vs B, difference driver, estimated direction of gap) and recommend one.
9. Set owner, review cadence, version and effective date; note that historic values must be restated or annotated when the definition changes.
10. Add guidance for interpretation: known seasonality, related guardrail metrics, anti-gaming notes.

## Output format
````markdown
# Metric: <name> (v<version>)
| Field | Value |
|---|---|
| Purpose / decision | ... |
| Desired direction | Up / Down / Within band |
| Owner | <name or [UNKNOWN]> |
| Grain / entity | ... |
| Effective from | <date or [TBD]> |

## Definition
Plain language: ...
```sql
-- pseudo-SQL
SELECT ... FROM ... WHERE ... GROUP BY ...
```

## Filters and Exclusions
- ...

## Time Logic
- Time stamp used: ... | Time zone: ... | Window: ... | Late data: ...

## Edge Cases
| Case | Treatment |
|---|---|

## Sources and Lineage
- ...

## Reconciliation (if conflicting definitions exist)
| Aspect | Definition A | Definition B | Effect on number |
|---|---|---|---|

## Interpretation Notes
- Guardrails: ... | Seasonality: ... | Gaming risk: ...
````

## Quality checklist
- [ ] Two analysts could implement it independently and get the same number.
- [ ] Numerator and denominator use the same population and time window.
- [ ] Time zone, period boundaries and late-data handling are stated.
- [ ] Every edge case has a stated treatment.
- [ ] Owner and version are set; unknowns are `[TBD]`, not guessed.

## Common pitfalls
- "Active" without an activity definition. Name the qualifying events and the look-back window.
- Mixing event date and booking date between numerator and denominator.
- Changing a definition silently. Version it and annotate historic charts.

## Example
Input: "Define 'active customer'; finance counts paying accounts, product counts users who logged in."

Excerpt of output:
- Purpose: Size of the engaged paying base for retention decisions.
- Definition: Distinct customer accounts with an active paid subscription on the last day of the month AND at least one qualifying product event in the trailing 28 days.
- Reconciliation: Finance count is higher because it includes paying but dormant accounts; product count includes free users.
- Edge case: Accounts merged mid-month count once under the surviving account ID.
