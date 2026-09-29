---
description: Analyzes an A/B or multivariate test end to end - validity checks (sample ratio mismatch, exposure, duration), primary metric effect with confidence interval, guardrail metrics, segments and a ship / iterate / stop recommendation. Use when experiment results are in and a decision is needed, or when someone asks whether a test result is significant or trustworthy.
related: experiment-design, hypothesis-statement, metric-definition, insight-summary, analysis-plan
prompt: Analyze this A/B test: control 48,210 users 2.31% conversion, variant 48,950 users 2.52% conversion, ran 14 days; guardrail is refund rate.
---

# Analyze an A/B Test

## Purpose
Decide from experiment data whether a change should ship, based on a valid test, an honest effect estimate and guardrails, rather than on a single p-value or a promising-looking chart.

## When to use
- An experiment has ended (or reached its planned sample) and a decision is due.
- Stakeholders are reading interim results and want to stop early.
- A result looks surprisingly large or contradicts other evidence.

## When not to use
- The test has not been designed yet. Use `experiment-design`.
- There is no randomized control (before/after, rollout by region). Use `analysis-plan` with a quasi-experimental method.
- Only communication of an already agreed result is needed. Use `insight-summary`.

## Inputs
Required:
- Per variant: units assigned, units analyzed, and primary metric values (counts or mean and standard deviation).

Optional, improves quality:
- Pre-registered hypothesis, minimum detectable effect, planned duration and sample size.
- Guardrail and secondary metrics, segment breakdowns, daily data.

If the per-variant numbers are missing, ask. Do not compute statistics from assumed values.

## Process
1. Restate the hypothesis, primary metric, unit of randomization and planned sample/duration. Mark unknown pre-registration `[UNKNOWN]`.
2. Validity checks: sample ratio mismatch (chi-square on assignment counts against the planned split), exposure/triggering correctness, full business cycles covered (at least whole weeks), no mid-test changes, novelty or primacy effects in daily trend.
3. If randomization unit differs from analysis unit (e.g. user vs session), note the variance issue and prefer the delta method or aggregation to the randomization unit.
4. Compute the primary effect: absolute and relative difference, confidence interval and p-value with the appropriate test (two-proportion z-test for rates, Welch's t-test for means; for heavy-tailed metrics consider trimming or bootstrap). Show the calculation inputs.
5. Compare against the minimum detectable / practically significant effect, not only against zero. Report power if the result is not significant.
6. Evaluate guardrails with a non-inferiority lens; any breached guardrail blocks shipping regardless of the primary result.
7. Review pre-specified segments only; treat unplanned segment findings as hypotheses and correct for multiple comparisons (e.g. Holm or Benjamini-Hochberg).
8. If peeking occurred without a sequential design, state that the error rate is inflated.
9. Recommend: ship, ship to a subset, iterate, extend (if underpowered and justified), or stop. Tie the recommendation to the thresholds.
10. Record learnings for the experiment log.

## Output format
```markdown
# A/B Test Readout: <test name>
| Field | Value |
|---|---|
| Hypothesis | ... |
| Primary metric | ... |
| Randomization unit / split | ... |
| Dates / duration | ... |
| Decision | Ship / Ship subset / Iterate / Extend / Stop |

## Validity
| Check | Result | Status |
|---|---|---|
| Sample ratio mismatch | p = ... | OK / FAIL |
| Full weekly cycles | ... | ... |

## Primary Result
| Variant | n | Metric | Abs. diff | Rel. diff | 95% CI | p |
|---|---|---|---|---|---|---|

## Guardrails
| Metric | Control | Variant | Threshold | Status |
|---|---|---|---|---|

## Segments (pre-specified)
- ...

## Recommendation and Rationale
...

## Caveats and Learnings
- ...
```

## Quality checklist
- [ ] SRM and exposure checks are done before interpreting the effect.
- [ ] Effect is reported with a confidence interval, both absolute and relative.
- [ ] The test chosen matches the metric type and randomization unit.
- [ ] Guardrails are evaluated and can veto the decision.
- [ ] Segment findings are labeled pre-specified or exploratory.
- [ ] All numbers are computed from the input; unknown values are marked.

## Common pitfalls
- Declaring a winner at the first significant peek. Use the planned sample or a sequential method.
- Ignoring SRM; a failed SRM invalidates the result regardless of p-value.
- Reporting "no effect" when the test was underpowered. Say "inconclusive" and give the detectable effect.

## Example
Input: Control 48,210 users, 2.31% conversion; variant 48,950 users, 2.52%; 14 days; planned 50/50 split; guardrail refund rate.

Excerpt of output:
- SRM: 48,210 vs 48,950 on a 50/50 plan, chi-square p ≈ 0.018 – FAIL; investigate assignment before trusting the effect.
- Primary (for reference only): +0.21 pts absolute, +9.1% relative; 95% CI approx. +0.02 to +0.40 pts.
- Recommendation: Do not ship yet; fix the assignment issue and rerun. Refund rate guardrail `[data not provided]`.
