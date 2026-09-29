---
description: Guides a structured exploratory data analysis of an unfamiliar dataset - structure, grain, distributions, nulls, duplicates, outliers, time coverage, relationships and quality issues - and reports findings and fitness for use. Use when a new table, extract or file arrives, before building a model, metric or dashboard on it, or when someone asks "what is in this data?".
related: analysis-plan, data-quality-rules, metric-definition, feature-engineering-plan, data-catalog-entry
prompt: Explore this dataset: a CSV of 250k e-commerce orders with columns order_id, customer_id, order_ts, amount, currency, status, channel. Here is the profile output.
---

# Explore a Dataset

## Purpose
Understand what a dataset really contains, how trustworthy it is and what it can answer, before anyone builds conclusions on it, and produce a short profile others can reuse.

## When to use
- A new source, extract or file must be used for analysis or modeling.
- Numbers from a dataset look wrong and the cause is unknown.
- A data catalog entry or quality rule set needs factual input.

## When not to use
- The question and method are already clear. Use `analysis-plan`.
- Formal validation rules must be written for a pipeline. Use `data-quality-rules`.
- Features for a model are being designed. Use `feature-engineering-plan`.

## Inputs
Required:
- The dataset description: schema (column names and types) plus either a sample, profiling output or summary statistics.

Optional, improves quality:
- Business meaning of columns, source system, extraction logic.
- The intended use (analysis, dashboard, model).

If only a column list is available, produce the exploration plan with the checks to run, and mark all findings `[TBD]`. Never fabricate statistics.

## Process
1. Establish grain: what one row represents; verify the candidate key is unique and non-null.
2. Check coverage: row count, time range, gaps by day/week, sudden volume jumps (often backfills or tracking changes).
3. Profile each column by type: numeric (min, percentiles, mean vs median, zeros, negatives), categorical (cardinality, top values, rare/misspelled levels), dates (range, future dates, default dates like 1900-01-01), text/IDs (format, length).
4. Quantify missingness per column and check whether it is random or tied to a segment or period.
5. Detect duplicates (exact and on business key) and inconsistent units, currencies or time zones.
6. Identify outliers with a stated rule (IQR, percentile, domain limits) and classify: error, legitimate extreme, or unknown.
7. Examine relationships: key correlations, cross-tabs between important categoricals, referential integrity to related tables.
8. Flag personal or sensitive data columns (name, e-mail, phone, national ID, location) and recommend masking or exclusion (KVKK/GDPR).
9. Judge fitness for the intended use: usable as-is, usable with listed fixes, or not usable.
10. Record issues with severity and the next check or owner.

## Output format
```markdown
# Data Exploration: <dataset>
| Field | Value |
|---|---|
| Grain | <one row = ...> |
| Rows / time range | ... |
| Candidate key unique? | Yes / No (<n> dupes) |
| Intended use | ... |
| Fitness | Usable / Usable with fixes / Not usable |

## Column Profile
| Column | Type | Null % | Distinct | Notes (range, top values, anomalies) |
|---|---|---|---|---|

## Key Findings
1. ...

## Data Quality Issues
| Issue | Columns | Severity | Suggested fix / owner |
|---|---|---|---|

## Sensitive Data
- <column> – <category> – <mask / drop / keep with reason>

## Open Questions
1. ...
```

## Quality checklist
- [ ] Grain and key uniqueness are stated and verified.
- [ ] Every statistic comes from the provided profile or sample; missing ones are `[TBD]`.
- [ ] Missingness is checked for patterns, not only percentages.
- [ ] Outlier rule is explicit, and outliers are classified, not silently removed.
- [ ] Sensitive columns are flagged with a handling recommendation.
- [ ] A clear fitness-for-use verdict is given.

## Common pitfalls
- Trusting the mean on skewed data. Report median and percentiles.
- Treating sentinel values (0, -1, 9999, 1900-01-01) as real values.
- Ignoring the time dimension; many issues appear only as step changes over time.

## Example
Input: 250k orders, columns order_id, customer_id, order_ts, amount, currency, status, channel; profile shows 312 duplicate order_id, amount min -45.00, currency has "TRY" and "TL".

Excerpt of output:
- Candidate key unique? No – 312 duplicate order_id, likely status updates appended as rows `[confirm with source owner]`.
- Issue: Negative amounts (refunds?) mixed with sales – severity High for revenue metrics.
- Issue: Currency values "TRY" and "TL" represent the same currency – normalize.
