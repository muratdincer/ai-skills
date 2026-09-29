---
description: Produces three-point estimates (optimistic, most likely, pessimistic) per work item and aggregates them with PERT or triangular formulas into expected values, standard deviations and confidence ranges for the total. Use when effort or duration is uncertain and stakeholders need a range with a stated confidence instead of a single number.
related: wbs, schedule-plan, budget-plan, technical-estimation, monte-carlo-forecast
prompt: Give me a three-point estimate for these 12 work packages and tell me the total at 85% confidence.
---

# Estimate with Three-Point/PERT

## Purpose
Turn uncertain effort or duration into explicit ranges with confidence levels, making estimation risk visible and supporting contingency decisions.

## When to use
- Work packages with meaningful uncertainty (new technology, unclear requirements, external dependencies).
- A sponsor asks "how sure are you?" about a date or cost.
- Setting contingency reserves for a budget or schedule.

## When not to use
- Relative team estimation of backlog items. Use `estimation-session`.
- Forecasting from historical throughput. Use `monte-carlo-forecast`.
- Engineering estimate of a single technical task. Use `technical-estimation`.

## Inputs
Required:
- List of work items (ideally WBS packages) with a description.
- O/M/P values per item, or enough context for the team to provide them.

Optional, improves quality:
- Historical actuals for similar work, team capacity, unit (hours, days, cost).

Never invent O/M/P values. If they are missing, provide an elicitation template and ask the estimators to fill it; example numbers must be labeled `[EXAMPLE]`.

## Process
1. Confirm the unit (effort hours, person-days, calendar duration) and do not mix them.
2. For each item, collect O, M, P from the people doing the work. Check O ≤ M ≤ P and that P reflects realistic bad cases, not catastrophe.
3. Choose the distribution: PERT (beta) E = (O + 4M + P) / 6, SD = (P − O) / 6; or triangular E = (O + M + P) / 3 when the team distrusts the M weighting. State which one is used.
4. Compute E and SD per item.
5. Aggregate: total E = sum of E; total SD = sqrt(sum of SD²), valid only if items are independent. Flag correlated items (shared risk drivers) and widen the range if present.
6. Derive confidence values using the normal approximation: ~84% ≈ E + 1 SD, ~90% ≈ E + 1.28 SD, ~95% ≈ E + 1.645 SD.
7. Identify the items contributing most to variance (largest SD²) and note what would reduce their uncertainty.
8. Recommend contingency as the difference between the chosen confidence value and E.
9. Document assumptions per estimate and state that the result is effort, not calendar time, unless durations were estimated.
10. Label every inferred element `[ASSUMPTION]` and move it to assumptions or open questions. If the user's goal continues, suggest the next skill: `schedule-plan` to sequence the estimates, or `budget-plan` to cost them.

## Output format
```markdown
# Three-Point Estimate: <scope>
Unit: <unit> | Method: <PERT/triangular> | Estimators: <roles>
| ID | Item | O | M | P | E | SD | Key assumption |
|---|---|---|---|---|---|---|---|
| Total | | | | | ΣE | √ΣSD² | |

## Confidence Levels
| Confidence | Value |
| 50% | E |
| ~84% | E + 1 SD |
| ~95% | E + 1.645 SD |

## Top Variance Drivers
## Recommended Contingency
## Assumptions, Correlations, Open Questions
```

## Quality checklist
- [ ] O ≤ M ≤ P holds for every item.
- [ ] The formula and unit are stated.
- [ ] No O/M/P value is fabricated; examples are labeled.
- [ ] Correlations are addressed before quoting totals.
- [ ] Results are given as ranges with confidence, not a single number.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Summing pessimistic values to get a "safe" total, which overstates risk massively. Aggregate SDs instead.
- Treating the expected value as a commitment. Commit at an agreed confidence level.
- Anchoring: asking for M first and deriving O/P as ±20%. Elicit P by asking what could go wrong.

## Example
Input: "Data migration package: O=10, M=15, P=35 days."

Excerpt of output:
| WP-4 | Data migration | 10 | 15 | 35 | 17.5 | 4.17 | Source data quality as profiled |
- WP-4 contributes 46% of total variance; a data profiling spike could narrow P.
