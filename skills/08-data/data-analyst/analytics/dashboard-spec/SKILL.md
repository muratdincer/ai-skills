---
description: Specifies a dashboard before it is built - audience, decisions it supports, questions, KPIs with definitions, visuals, filters, drill paths, refresh and access rules. Use when someone asks for a new dashboard or report page, wants to rebuild a cluttered one, or needs a spec a BI developer can implement without guessing.
related: metric-definition, kpi-definition, report-requirements, data-requirements, insight-summary
prompt: Specify a dashboard for the customer support leadership to track ticket backlog, SLA compliance and agent workload weekly.
---

# Specify a Dashboard

## Purpose
Produce an implementable dashboard specification that starts from the audience's decisions and questions, so the result is used regularly instead of becoming another unused wall of charts.

## When to use
- A team requests a new dashboard or a new page on an existing one.
- An existing dashboard is cluttered, distrusted or unused and needs redesign.
- A BI developer needs an unambiguous spec (metrics, visuals, filters, security).

## When not to use
- The need is a one-off question. Use `analysis-plan`.
- A single metric is disputed or undefined. Use `metric-definition` first.
- The request is a formal regulatory or operational report with fixed layout. Use `report-requirements`.

## Inputs
Required:
- The audience and what they want to monitor or decide.

Optional, improves quality:
- Existing reports, screenshots, metric definitions.
- Data sources and their refresh cadence.
- BI platform constraints, corporate visual guidelines, access rules.

If the audience or purpose is missing, ask. Everything else becomes an open question.

## Process
1. Name the primary audience and its usage pattern (daily ops check, weekly review, monthly exec). One dashboard serves one primary audience.
2. List the 3-7 decisions or questions the dashboard must answer, in priority order. Drop any request that maps to no question.
3. For each question, define the KPI(s): name, formula reference, grain, target/threshold, comparison (vs target, vs prior period). Flag undefined metrics for `metric-definition`.
4. Choose visuals per question: big number with trend for status, line for time trend, bar for ranking/comparison, table for lookup, heatmap for two-dimensional density. Avoid pies beyond 3 slices and dual axes.
5. Lay out by reading order: headline KPIs top-left, trends next, diagnostic breakdowns below, detail tables last.
6. Define global and local filters, default values, and drill-down/drill-through paths.
7. Define data: sources, refresh frequency, latency tolerance, "data as of" stamp, handling of incomplete periods.
8. Define access: row-level security, who sees personal data, masking. Default to aggregated views.
9. Define alerting or conditional formatting thresholds and their colors, with non-color cues for accessibility (WCAG 2.2 contrast).
10. Define acceptance: reconciliation with source totals, performance target (load time), and a usage review date.

## Output format
```markdown
# Dashboard Spec: <name>
| Field | Value |
|---|---|
| Primary audience | <role> – <usage cadence> |
| Owner | <name or [UNKNOWN]> |
| Data refresh | <frequency, latency> |

## Questions It Answers
1. <question> → <decision it supports>

## KPIs
| KPI | Definition ref | Grain | Target / threshold | Comparison |
|---|---|---|---|---|

## Layout
| Zone | Visual | KPI / fields | Interaction |
|---|---|---|---|
| Top row | Big number + sparkline | ... | click → page 2 |

## Filters and Drill Paths
- Global: <filter> (default: ...)
- Drill: <from> → <to>

## Data and Security
- Sources: ...
- Row-level security: ...
- Personal data: <aggregated / masked / excluded>

## Acceptance Criteria
- Totals reconcile with <source> within <tolerance>.
- Loads in < <n> s with default filters.

## Open Questions
1. ...
```

## Quality checklist
- [ ] Every visual maps to a listed question.
- [ ] Every KPI has a definition reference, grain and comparison.
- [ ] Thresholds and colors are defined and not color-only.
- [ ] Incomplete current period is handled (flagged or excluded).
- [ ] Access and personal data rules are explicit.
- [ ] Nothing is invented: unknown targets are `[TBD]`.

## Common pitfalls
- Building for "everyone". Pick one primary audience; create a separate view for others.
- Showing numbers without context. Always pair a KPI with target or prior period.
- Mixing grains on one page (daily and monthly) without labeling, which causes mismatched totals.

## Example
Input: "Support leadership wants to track ticket backlog, SLA compliance and agent workload weekly."

Excerpt of output:
- Question 1: Are we meeting SLA this week? → decide whether to reallocate agents.
- KPI: SLA compliance % = tickets resolved within SLA / tickets resolved, weekly, by priority; target `[TBD]`.
- Layout: top row big numbers (open backlog, SLA %, median first response) with 12-week sparkline; middle bar chart backlog by queue; bottom table agents with open tickets (names visible only to team leads).
