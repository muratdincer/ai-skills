---
name: report-requirements
description: "Specifies report requirements starting from the decision the report supports: audience, questions answered, fields and measures with exact calculation and grain, dimensions, filters and parameters, sorting and grouping, data sources and freshness, access and masking, delivery and format, and acceptance checks against a reconciled figure. Use when someone asks for a new report, export or list, when an existing report is disputed, or when asked to 'spec a report'."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: documentation
  title: "Specify report requirements"
  related: "dashboard-spec, metric-definition, data-requirements, kpi-definition, request-intake-document"
  prompt: "Specify the monthly overdue receivables report Finance asked for, by customer segment and aging bucket."
---

# Specify Report Requirements

## Purpose
Define a report so precisely that it answers the audience's real question, every number can be reproduced and reconciled, and developers need no guesses about calculations, filters or access.

## When to use
- A stakeholder requests a new report, export, list or scheduled extract.
- An existing report's numbers are disputed or differ from another source.
- A report is being migrated to a new platform and its logic must be made explicit.

## When not to use
- An interactive, multi-chart dashboard with layout is needed. Use `dashboard-spec`.
- Only one metric needs an agreed definition. Use `metric-definition`.
- The request itself is still raw and unqualified. Use `request-intake-document` first.

## Inputs
Required:
- The report request and its audience (who will use it).

Optional, improves quality:
- Sample of the current report or a mock-up, metric definitions, data sources, business rules, access policy, regulatory requirements.

If the audience or the purpose is missing, ask: "Which decision or action will this report drive, and who takes it?" Ask at most 5 blocking questions at a time.

## Process
1. Separate the literal ask ("an Excel list of X") from the decision or control it supports; state the report's purpose in one sentence and mark inference `[ASSUMPTION]`.
2. List the business questions the report must answer; drop fields that answer none of them.
3. Define the grain: what one row represents (one invoice, one customer per month). Most disputes come from an unclear grain.
4. Specify each field: business name, definition, source, format, and for measures the exact calculation, aggregation, unit/currency and rounding. Reference `metric-definition` IDs where they exist.
5. Specify dimensions, grouping, subtotals, sorting and the time logic (period, as-of date, time zone, fiscal vs calendar).
6. Specify filters and parameters: defaults, mandatory ones, allowed values, and how "all" and empty values behave.
7. Specify data freshness and cut-off (real-time, daily at a time, month-end close) and what happens to late or corrected data.
8. Specify access: who may see which rows and columns; mask or exclude personal data not needed for the purpose (KVKK/GDPR minimization).
9. Specify delivery: on-demand or scheduled, channel, file format, size limits, retention of generated files.
10. Define acceptance: a reconciliation figure (e.g. total equals the general ledger for the period) and sample cases to verify; list assumptions and open questions with owners.
11. If the goal continues, suggest `metric-definition` for disputed measures, `dashboard-spec` if visual exploration is needed, or `data-requirements` for new data.

## Output format
```markdown
# Report Requirements: <report name>
| Field | Value |
|---|---|
| Purpose (decision / control) | ... |
| Audience | ... |
| Grain (one row =) | ... |
| Freshness / cut-off | ... |
| Delivery | <on demand / schedule, channel, format> |

## Business Questions
## Fields and Measures
| # | Field | Definition | Source | Calculation / aggregation | Format |
## Dimensions, Grouping, Sorting, Time Logic
## Filters and Parameters
| Filter | Default | Mandatory | Allowed values | Empty/all behavior |
## Access and Masking
## Acceptance and Reconciliation
## Assumptions and Open Questions
```

## Quality checklist
- [ ] The purpose names a decision or control, not only the report content.
- [ ] The grain is stated, and every measure has an exact calculation, aggregation and unit.
- [ ] Time logic (period, as-of, time zone) and freshness are explicit.
- [ ] Every filter has a default and empty/all behavior.
- [ ] Access and masking of personal data are defined.
- [ ] Acceptance includes a reconciliation figure and source; no numbers are invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Specifying columns without the question behind them. Reports grow to 60 columns nobody reads; tie each field to a question.
- "Total sales" without saying net or gross, booked or invoiced, which currency and which date. Define every measure precisely.
- Ignoring corrections after cut-off. State whether closed periods are restated or frozen.

## Example
Input: "Finance wants a monthly overdue receivables report by segment and aging."

Excerpt of output:
- Purpose `[ASSUMPTION]`: decide which segments need collection action and provisioning at month-end close.
- Grain: one open invoice as of the last calendar day of the month `[TBD: calendar or fiscal month]`.
- Measure: Overdue amount = open invoice amount where due date < as-of date, in reporting currency at month-end rate `[TBD: rate source]`.
- Aging buckets: 1-30, 31-60, 61-90, 90+ days past due.
- Access: segment managers see only their segment; customer contact details excluded.
- Acceptance: total overdue equals the receivables sub-ledger aging total for the same as-of date.
