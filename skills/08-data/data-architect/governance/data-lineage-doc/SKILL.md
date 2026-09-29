---
name: data-lineage-doc
description: "Documents data lineage from source systems through ingestion, transformations and storage layers to reports, models and other consumers, at dataset and critical-column level, with transformation logic, owners and verification status. Use when someone asks where a number comes from, for impact analysis before a change, for audit or regulatory traceability, or when onboarding people to an unfamiliar data flow."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 08-data
  role: data-architect
  area: governance
  title: "Document data lineage"
  related: "data-catalog-entry, source-to-target-mapping, impact-analysis, data-quality-rules, diagram-as-code"
  prompt: "Document the lineage of the 'net revenue' figure on the finance dashboard back to the source systems."
---

# Document Data Lineage

## Purpose
Show, verifiably, how a dataset or metric is produced from its sources, so people can trust it, trace errors to their origin and assess the impact of changes before they break consumers.

## When to use
- A reported figure is questioned and its derivation must be explained.
- A source, table or column is about to change and downstream impact is needed.
- Audit or regulation requires traceability of reported data (e.g. financial or risk reporting).

## When not to use
- Detailed column-by-column load specification for building a pipeline. Use `source-to-target-mapping`.
- A discovery-oriented summary of one dataset. Use `data-catalog-entry`.
- Impact of a business or system change beyond data flows. Use `impact-analysis`.

## Inputs
Required:
- The lineage target (a dataset, column, metric or report) and any available evidence: SQL/transformation code, pipeline definitions, job lists, architecture notes or people's descriptions.

Optional:
- Scope direction (upstream, downstream, both), depth, owners, schedules, known issues, sensitivity of the data.

If there is no evidence at all, ask for code, pipeline names or a person who knows the flow; lineage reconstructed from guesses is worse than none.

## Process
1. Fix the target and direction: upstream (where does it come from), downstream (who uses it) or both, and the granularity (dataset-level, plus column-level for critical elements).
2. Walk the flow hop by hop from evidence: source system and object, extraction method, landing/raw layer, each transformation step, serving layer, consumer (report, model, export, API).
3. For each hop record: node name, layer, owner, run schedule, and the transformation type (pass-through, filter, join, aggregate, derive, lookup, deduplicate, manual adjustment).
4. For critical columns, write the derivation as a formula or pseudo-SQL, including filters, join keys, currency/unit conversions and hard-coded values.
5. Mark each hop's verification status: verified from code, verified from system metadata, stated by a person, or `[INFERRED]`. Never present inferred hops as verified.
6. Flag breaks and risks: manual steps (spreadsheets, uploads), undocumented logic, multiple competing sources of the same fact, fan-out points where one change hits many consumers.
7. Note control points: where data quality checks, reconciliations or approvals happen along the path.
8. Note sensitive data movement: where personal data enters, is masked, or leaves the controlled environment.
9. Draw the flow as a diagram-as-code block (left-to-right) and pair it with a hop table.
10. List gaps, open questions and the people who could close them. If the goal continues, suggest `impact-analysis` for a planned change, `data-quality-rules` for unguarded hops, or `data-catalog-entry` to publish the result.

## Output format
```markdown
# Data Lineage: <target>
Direction: <upstream/downstream/both> | Granularity: <dataset / column> | As of: <date> | Author: <...>

## Diagram
<diagram-as-code, source → ... → consumer>

## Hops
| # | From | To | Layer | Transformation | Logic (critical columns) | Owner | Schedule | Verified by |
|---|---|---|---|---|---|---|---|---|

## Control Points
- <check / reconciliation / approval at hop #>

## Risks and Breaks
- <manual step, competing source, fan-out>

## Gaps and Open Questions
- [INFERRED] ... — confirm with <role>
```

## Quality checklist
- [ ] Every hop cites its evidence type; inferred hops are labeled `[INFERRED]`.
- [ ] Critical columns have explicit derivation logic including filters and conversions.
- [ ] Manual steps and competing sources are flagged, not smoothed over.
- [ ] Personal data movement and masking points are shown.
- [ ] Diagram and hop table agree.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Stopping at the warehouse. The spreadsheet adjustment between the warehouse and the board pack is often where numbers diverge.
- Table-level lineage only. "Revenue comes from orders" hides the filter that excludes returns.
- Treating tool-harvested lineage as complete; dynamic SQL, stored procedures and manual uploads are commonly missed.

## Example
Input: "Where does 'net revenue' on the finance dashboard come from? Here is the dashboard query and the mart SQL."

Excerpt of output:
- Hop 3: stg_orders → fct_revenue, aggregate daily; net_revenue = sum(gross_amount − discount − refund) where status <> 'cancelled', converted to EUR at daily rate. Verified from code.
- Hop 5: fct_revenue → finance dashboard, filter region ≠ 'internal'. Verified from code.
- Hop 1: ERP → landing, nightly extract `[INFERRED from job name]` — confirm with ERP integration owner.
