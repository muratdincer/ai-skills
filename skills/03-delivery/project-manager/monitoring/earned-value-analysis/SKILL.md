---
name: earned-value-analysis
description: "Runs an earned value analysis from a cost-loaded baseline and progress data, computing PV, EV, AC, SV, CV, SPI, CPI, EAC, ETC, VAC and TCPI, interpreting the variances and forecasting completion cost and date with stated assumptions. Use when a project with a budget and schedule baseline needs an objective performance reading, a forecast at completion, or evidence for a status report or steering decision."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: project-manager
  area: monitoring
  title: "Run earned value analysis"
  related: "budget-plan, schedule-plan, project-status-report, change-control, monte-carlo-forecast"
  prompt: "Here is our baseline per work package and this month's actuals and percent complete. Run earned value analysis and tell me whether we will finish within budget."
---

# Run Earned Value Analysis

## Purpose
Give an objective, number-based reading of schedule and cost performance against the approved baseline, and a defensible forecast at completion, so that sponsors decide on facts rather than on percent-complete optimism.

## When to use
- Periodic control of a project with an approved cost and schedule baseline.
- Before a status report or steering meeting when cost or schedule health is questioned.
- To test whether a recovery plan is realistic (TCPI check).

## When not to use
- No cost-loaded baseline exists yet. Use `budget-plan` and `schedule-plan` first.
- Flow-based teams forecasting from throughput without a budget baseline. Use `monte-carlo-forecast`.
- Reporting overall project health to stakeholders. Use `project-status-report` and feed it these results.

## Inputs
Required:
- Baseline: budget at completion (BAC) and planned value per period or per work package.
- Progress: earned value or a measurable completion basis per work package, as of a status date.
- Actual cost (AC) to the status date, in the same currency and cost basis as the baseline.

Optional, improves quality:
- Earning rules in use (0/100, 50/50, weighted milestones, physical percent complete).
- Approved changes and management reserve movements.
- Previous periods' indices for trends.

If BAC, planned value or actual cost is missing, ask for it. Never estimate AC or EV from narrative.

## Process
1. Confirm the status date, currency, cost basis (labor only or fully loaded) and that baseline and actuals use the same basis; flag mismatches as blocking.
2. Check the baseline includes approved changes only; unapproved changes and management reserve stay outside PV.
3. Determine EV per work package using the stated earning rule. If only subjective percent complete exists, apply it but mark EV `[ASSUMPTION: subjective progress]`.
4. Compute PV, EV, AC and the variances SV = EV − PV and CV = EV − AC, cumulative and for the period.
5. Compute SPI = EV/PV and CPI = EV/AC; show both cumulative and period values and the trend over the last periods if given.
6. Forecast EAC with at least two methods and state when each fits: BAC/CPI (current efficiency persists), AC + (BAC − EV) (variance was atypical), AC + (BAC − EV)/(CPI × SPI) (schedule pressure drives cost). Derive ETC and VAC.
7. Compute TCPI = (BAC − EV)/(BAC − AC), and against EAC if a revised budget is approved; flag TCPI above about 1.1 as an unrealistic recovery assumption.
8. Estimate schedule outlook: note that SPI tends to 1.0 near the end; if the critical path is known, cross-check with it or with earned schedule (SPI(t)) when period data allows.
9. Drill into the work packages driving the largest negative CV and SV and state likely causes, labeling causes not given in the input as `[ASSUMPTION]`.
10. Recommend actions or decisions (re-plan, change request, reserve use, scope trade-off) with the owner who decides.
11. If the user's goal continues, suggest `project-status-report` to report the result or `change-control` when a baseline change is needed.

## Output format
```markdown
# Earned Value Analysis: <project> – status date <date>
Currency / cost basis: <...> | BAC: <...> | Earning rule: <...>

## Summary
<2-3 sentences: cost and schedule position, forecast, decision needed>

## Metrics
| Metric | Period | Cumulative | Trend |
|---|---|---|---|
| PV / EV / AC | | | |
| SV / CV | | | |
| SPI / CPI | | | |

## Forecast
| Method | EAC | ETC | VAC | When it applies |
|---|---|---|---|---|
TCPI (to BAC): <value> – <realistic or not>

## Variance Drivers
| Work package | SV | CV | Cause (stated or [ASSUMPTION]) |

## Recommendations and Decisions Needed
- <action> – <decision owner>

## Assumptions and Data Gaps
```

## Quality checklist
- [ ] Baseline and actuals share the same currency, cost basis and status date.
- [ ] Formulas are applied correctly and signs are interpreted consistently (negative = unfavorable).
- [ ] EAC is given with more than one method and the chosen one is justified.
- [ ] Subjective progress and inferred causes are labeled as assumptions.
- [ ] Recommendations name a decision owner.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Using spend as progress (EV = AC). EV must come from completed work, not money spent.
- Reading SPI alone late in the project; it drifts to 1.0 even when late. Check the critical path or earned schedule.
- Presenting a single EAC as certain. Show the range across methods.
- Accrual lag: invoices not yet booked make CPI look better than reality. Ask about committed but unbilled costs.

## Example
Input: "BAC 1,200k. Status month 5: PV 600k, EV 480k, AC 560k."

Excerpt of output:
- SV = −120k, SPI = 0.80; CV = −80k, CPI = 0.86.
- EAC (BAC/CPI) ≈ 1,400k; EAC (AC + BAC − EV) = 1,280k; VAC between −80k and −200k.
- TCPI (to BAC) = 720/640 = 1.13: recovering within the original budget is unrealistic without scope or funding change. Decision owner: sponsor `[confirm]`.
