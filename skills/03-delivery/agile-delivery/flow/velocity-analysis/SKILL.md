---
name: velocity-analysis
description: "Analyzes a team's velocity (points per iteration) or throughput (items per week/iteration) history: trend, variability, outliers and their causes, and a range-based forecast for remaining work. Use when someone shares iteration or throughput numbers and asks whether the team is speeding up or slowing down, how predictable it is, or how many iterations a backlog will take."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: agile-delivery
  area: flow
  title: "Analyze velocity/throughput"
  related: "monte-carlo-forecast, burndown-analysis, cycle-time-analysis, release-planning, engineering-metrics-review"
  prompt: "Here are our last 10 sprint velocities: 21, 34, 29, 18, 31, 33, 12, 30, 28, 32. We have 180 points left in the release. What does this tell us and when can we finish?"
---

# Analyze Velocity/Throughput

## Purpose
Turn raw velocity or throughput numbers into an honest read of the team's delivery rate and predictability, and a forecast range for remaining work that stakeholders can plan with, without turning the metric into a target.

## When to use
- Iteration velocities or weekly throughput counts are available and someone asks what they mean.
- A release or backlog needs a "how many iterations" estimate.
- Velocity dropped or jumped and the team wants to understand why.

## When not to use
- A probability-based date or scope forecast with confidence levels. Use `monte-carlo-forecast`.
- Progress within the current iteration. Use `burndown-analysis`.
- Understanding how long individual items take. Use `cycle-time-analysis`.

## Inputs
Required:
- A series of at least 5 data points (velocity per iteration or throughput per period), oldest to newest.

Optional, improves quality:
- Remaining backlog size in the same unit.
- Context per period: team changes, holidays, incidents, scope changes, estimation scale changes.
- Carry-over or partially done work rules.

If fewer than 5 points are available, say that any forecast is highly uncertain and mark it `[LOW CONFIDENCE]`. Never fill gaps with invented values.

## Process
1. Validate the data: same unit throughout, same team composition, same counting rule (only fully done items). Flag breaks (e.g. estimation scale reset) and analyze only comparable periods.
2. Compute descriptive statistics: mean, median, min, max, and the interquartile range; for 8 or more points, also the 25th and 75th percentiles. Show the arithmetic.
3. Describe variability: coefficient of variation (standard deviation / mean). As a heuristic, below ~0.2 is stable, 0.2-0.4 moderate, above ~0.4 unpredictable `[heuristic]`.
4. Identify trend with a rolling average of 3 periods; state whether the last 3-5 periods are rising, flat or falling, and avoid calling a trend from 2 points.
5. Explain outliers using supplied context; where no context exists, list candidate causes as `[INFERRED]` questions for the team.
6. Forecast remaining work as a range: remaining ÷ high rate (optimistic), ÷ median (likely), ÷ low rate (pessimistic, e.g. 25th percentile). Round up to whole iterations and state that scope growth is not included unless given.
7. If scope changes over time, note it; recommend tracking scope in a burnup rather than assuming fixed scope.
8. Add health observations: signs of metric gaming (steadily rising points with flat outcomes), large carry-over, or a mismatch between velocity and throughput.
9. Write 2-4 recommendations (e.g. reduce item size variance, stabilize team, use `monte-carlo-forecast` for dates).
10. If the user's goal continues, suggest `monte-carlo-forecast` for probability-based commitments or `release-planning` to update the plan.

## Output format
```markdown
# Velocity/Throughput Analysis – <team>, <periods>
Unit: <points/items per iteration/week> · Data points: <n> · Comparable range: <...>

## Statistics
| Mean | Median | Min | Max | P25 | P75 | CoV |
|---|---|---|---|---|---|---|
Interpretation: <stable / moderate / unpredictable>

## Trend
<rising/flat/falling> – <evidence from rolling average>

## Outliers
| Period | Value | Cause (stated / [INFERRED]) |
|---|---|---|

## Forecast for <remaining size>
| Scenario | Rate used | Iterations needed |
|---|---|---|
Caveats: <scope growth, team changes, low data>

## Recommendations
- ...
```

## Quality checklist
- [ ] Calculations are shown and reproducible from the input.
- [ ] Non-comparable periods are excluded or flagged.
- [ ] The forecast is a range, never a single number, with caveats.
- [ ] Outlier causes are either stated in the input or labeled `[INFERRED]`.
- [ ] Velocity is not used to compare teams or individuals.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Using the mean when outliers skew it. Prefer the median and percentiles.
- Treating velocity as productivity. It measures the team's own estimate scale, not value delivered.
- Forecasting with fixed scope while the backlog keeps growing. Track scope growth separately.

## Example
Input: velocities 21, 34, 29, 18, 31, 33, 12, 30, 28, 32; remaining 180 points.

Excerpt of output:
- Median 29.5, P25 ~20, P75 ~32, mean 26.8, CoV ~0.27 → moderate variability.
- Outlier: 12 in iteration 7 – cause unknown `[INFERRED: holiday or incident?]`.
- Forecast: 180 ÷ 32 ≈ 6 (optimistic), ÷ 29.5 ≈ 7 (likely), ÷ 20 = 9 (pessimistic) iterations, excluding scope growth.
