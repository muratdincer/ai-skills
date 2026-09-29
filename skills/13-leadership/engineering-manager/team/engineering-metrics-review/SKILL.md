---
description: Reviews engineering delivery metrics using DORA (deployment frequency, lead time for changes, change failure rate, time to restore) and SPACE dimensions, interprets trends with context, detects gaming and data-quality issues, and proposes improvement experiments. Use when preparing a metrics review for a team or organization, when leadership asks for productivity numbers, or when metrics are being misused to compare individuals.
related: cycle-time-analysis, team-health-check, kpi-definition, metric-definition, velocity-analysis
prompt: Here are our DORA numbers for the last two quarters for four teams. Review them and tell me what to discuss with the teams.
---

# Review Engineering Metrics (DORA/SPACE)

## Purpose
Turn delivery metrics into a balanced, context-aware picture of system performance that leads to improvement experiments, without turning the numbers into targets that get gamed or into rankings of people.

## When to use
- A periodic metrics review for teams or the engineering organization.
- Leadership asks "how productive is engineering" and needs a responsible answer.
- Metrics have changed sharply, or teams suspect they are measured unfairly.

## When not to use
- Detailed flow analysis of one team's work items. Use `cycle-time-analysis`.
- Defining a new metric from scratch. Use `metric-definition` or `kpi-definition`.
- Team morale and collaboration only. Use `team-health-check`.

## Inputs
Required:
- Metric values with time periods and the teams/services they cover.

Optional, improves quality:
- Metric definitions and data sources (what counts as a deployment, failure, restore).
- Context: incidents, reorgs, release freezes, migrations, headcount changes.
- Developer experience survey results or other SPACE signals (satisfaction, collaboration).

If metric definitions are unknown, state the common definitions you assume and mark them `[ASSUMPTION]`; do not compare teams whose definitions may differ.

## Process
1. Confirm definitions and data quality for each metric (source, exclusions, sample size); flag metrics that are not comparable across teams.
2. Present the four DORA metrics together per team/service over time; never interpret throughput without stability (and vice versa).
3. Look at trends and distributions (median and p85/p90), not single averages; mark changes smaller than the normal variation as noise.
4. Add context events to the timeline and explain changes with evidence; label hypotheses as such.
5. Add at least one SPACE dimension beyond activity (satisfaction/well-being, collaboration, efficiency/flow) to balance the view.
6. Check for gaming and side effects: splitting deployments artificially, reclassifying incidents, skipping tests to reduce lead time, rising on-call load.
7. Refuse individual-level rankings: metrics describe the system; if asked for per-person numbers, explain the risk and offer team-level alternatives.
8. Identify 2-3 constraints (e.g. manual approval gate, long review wait, flaky tests) that most likely limit the metrics.
9. Propose improvement experiments with an owner role, expected effect, measure and review date.
10. Prepare discussion questions for the teams, framed as curiosity, not blame.
11. If the user's goal continues, suggest `cycle-time-analysis` to dig into a constraint or `team-health-check` for the human side.

## Output format
```markdown
# Engineering Metrics Review: <scope> – <period>

## Definitions and Data Quality
| Metric | Definition used | Source | Caveats |
|---|---|---|---|

## DORA Overview
| Team / service | Deploy frequency | Lead time (median/p85) | Change failure rate | Time to restore | Trend |
|---|---|---|---|---|---|

## Beyond Activity (SPACE)
- ...

## Interpretation
- Observation → evidence → hypothesis [label]

## Gaming / Side-Effect Check
- ...

## Likely Constraints
1. ...

## Improvement Experiments
| Experiment | Owner role | Expected effect | Measure | Review date |
|---|---|---|---|---|

## Questions for Teams
- ...
```

## Quality checklist
- [ ] Throughput and stability metrics are always shown together.
- [ ] Definitions and data caveats are stated; incomparable data is not compared.
- [ ] Trends use distributions and context, not single-point averages.
- [ ] Hypotheses are labeled and separated from evidence.
- [ ] No individual-level rankings or targets on people.
- [ ] Each improvement experiment has a measure and review date.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Turning metrics into targets ("reach daily deploys by Q3"). Target the constraints, observe the metrics.
- Comparing teams with different architectures and definitions as a league table. Compare each team with its own history.
- Ignoring the cost side: faster deployments with rising on-call pages is not an improvement.

## Example
Input: Team A lead time median 6 days → 2 days, change failure rate 8% → 21% over two quarters.

Excerpt of output:
- Observation: Lead time improved 3x while change failure rate more than doubled.
- Hypothesis [label]: The removed manual QA gate was not replaced by automated checks; test coverage on the checkout service did not change (evidence: pipeline config, coverage report).
- Weak conclusion (avoid): "Team A is now the fastest team." Strong conclusion: "Speed gain is real but not yet safe; experiment: add contract tests for top 3 failing integrations, review CFR in 6 weeks."
