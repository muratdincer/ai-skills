---
description: "Analyzes SLA breaches over a period: validates the data and clock rules, measures breach rates by priority, category, team, time and customer, finds patterns and root causes (process, capacity, routing, dependency, measurement), and proposes prioritized improvement actions with owners and target metrics. Use when SLA performance drops, before a service review or contract discussion, when penalties or credits are at stake, or when a team wants to know why tickets miss their targets."
related: "problem-management, ticket-triage, slo-definition, kpi-definition, dashboard-spec"
prompt: "Analyze last quarter's SLA breaches: P2 resolution target is 8 business hours, we met it for 71% against a 90% target; here is the ticket export."
---

# Analyze SLA Breaches

## Purpose
Explain why service levels were missed with evidence, separate real service problems from measurement artifacts, and turn the findings into a few actions that will measurably raise attainment.

## When to use
- SLA attainment fell below target for a priority, service or customer.
- A service review, contract renewal or penalty/credit discussion is coming.
- A support team repeatedly misses response or resolution targets and the cause is disputed.

## When not to use
- Defining new service level targets or error budgets. Use `slo-definition`.
- A single ticket breached and needs escalation now. Use `ticket-escalation-summary`.
- Recurring technical incidents are the known cause. Use `problem-management`.

## Inputs
Required:
- Ticket or incident data for the period (at least ID, priority, category, created, first response, resolved, status history or pause times, assigned group) or an aggregated breach report.
- The SLA definitions: targets per priority, business hours/calendar, pause rules.

Optional, improves quality:
- Staffing and shift data, backlog trend, changes in the period (releases, reorganization, tool change).
- Customer contract terms, penalty or credit clauses.
- Previous period results for comparison.

If data or SLA definitions are missing, ask for them; do not compute rates from assumed targets. Work on aggregated or pseudonymized data: remove customer contact details and personal data from ticket text before analysis.

## Process
1. Validate the measurement: confirm clock rules (business hours, holidays, time zones, pause on "waiting for customer"), check for missing timestamps, reopened tickets, priority changes mid-life and tickets closed without resolution. Record data quality issues and their effect.
2. Compute attainment per SLA metric (response, resolution) by priority for the period and versus previous periods; show counts, not only percentages.
3. Slice breaches by category/service, assigned group, channel, customer, time of day/week and ticket age; highlight where breaches concentrate (for example, 20% of categories causing 80% of breaches).
4. Examine breached tickets' timelines: time in queue before assignment, reassignments (ping-pong), waiting on third parties, time in pause, and work time. Identify which segment consumed the clock.
5. Classify causes: demand spike, capacity/shift coverage, routing and triage errors, skill gaps, dependency on another team or vendor, process design (approvals), tooling, measurement artifacts. Label each cause as evidence-based or `[ASSUMPTION]`.
6. Check for gaming or distortion: priority downgrades near breach, premature closure, pause misuse, split tickets. Report these neutrally as measurement risks.
7. Quantify contractual exposure only from given contract terms; otherwise state `[UNKNOWN]`.
8. Propose actions ranked by expected impact and effort, each linked to a cause, with owner, due date and the metric and target that will show improvement.
9. Recommend monitoring: leading indicators (tickets approaching breach, queue age, reassignment count) and review cadence.
10. Hand off: suggest `problem-management` for technical root causes, `dashboard-spec` for a monitoring dashboard, or `slo-definition` if targets themselves appear unrealistic.

## Output format
```markdown
# SLA Breach Analysis: <service / period>
## Summary
- Attainment: <metric, priority>: <x% (n/N)> vs target <y%>; previous period <z%>
- Main drivers: 1. ... 2. ... 3. ...
- Top actions: ...
## Data and Measurement Notes
- Clock rules applied: ... Data quality issues: ... Effect: ...
## Attainment
| Metric | Priority | Met | Breached | Attainment | Target | Previous |
|---|---|---|---|---|---|---|
## Breach Concentration
| Dimension | Segment | Breaches | Share | Note |
|---|---|---|---|---|
## Where the Clock Went (breached tickets)
| Segment | Median time | Share of elapsed |
|---|---|---|
## Causes
| Cause | Evidence | Confidence (evidence / [ASSUMPTION]) |
|---|---|---|
## Contractual Exposure
<from given terms or [UNKNOWN]>
## Actions
| # | Action | Addresses cause | Owner | Due | Success metric |
|---|---|---|---|---|---|
## Open Questions
1. ...
```

## Quality checklist
- [ ] SLA clock rules and data quality issues are stated before any rate is reported.
- [ ] Rates are shown with counts, and compared with target and prior period.
- [ ] Each cause is backed by data or labeled `[ASSUMPTION]`.
- [ ] Every action links to a cause and has an owner and a success metric.
- [ ] Penalties or credits are computed only from provided contract terms.
- [ ] Personal data from ticket text is removed or pseudonymized.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Computing breaches in calendar hours when the SLA is in business hours, which inflates breach counts.
- Blaming "not enough people" without showing where the clock was spent; often queue wait or reassignments dominate.
- Reporting averages; a few very old tickets distort them. Use medians and percentiles.
- Proposing ten actions; pick the few that address the largest breach concentrations.

## Example
Input: "P2 resolution target 8 business hours; attainment 71% vs 90% target last quarter; ticket export attached."

Excerpt of output:
- Attainment: P2 resolution 71% (412/580) vs 90%; previous quarter 84% (n/N [UNKNOWN]).
- Concentration: 58% of P2 breaches in the "Integrations" category; 64% of breached tickets were reassigned 2+ times.
- Where the clock went: median 3.1 business hours in queue before first assignment.
- Cause (evidence): no routing rule for the new partner API errors introduced in month 2. Cause [ASSUMPTION]: L2 integration skill shortage on late shift.
- Action: add routing rule and triage checklist for integration errors – owner Support Lead – success: P2 integration attainment ≥ 88% next quarter.
