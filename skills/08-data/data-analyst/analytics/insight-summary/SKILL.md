---
description: Turns analysis results, query outputs or charts into a short "so what" insight summary - headline finding, evidence, confidence, implications and a recommended action. Use when numbers are available but the audience needs to know what they mean and what to do, e.g. after an analysis, a monthly review or a dashboard anomaly.
related: analysis-plan, executive-summary, ab-test-analysis, dashboard-spec, presentation-outline
prompt: Write an insight summary from these results: churn rose from 3.1% to 4.0% in Q3, mostly in the SMB segment on monthly plans.
---

# Write an Insight Summary

## Purpose
Convert data results into a decision-oriented narrative that states what happened, why it matters, how sure we are and what to do next, so stakeholders act on the finding instead of re-asking for the analysis.

## When to use
- An analysis is complete and must be communicated to non-analysts.
- A recurring review (weekly/monthly) needs commentary beyond the charts.
- A dashboard shows an anomaly and leadership asks "what is going on?".

## When not to use
- The analysis has not been scoped or run yet. Use `analysis-plan`.
- The results come from a controlled experiment requiring a ship decision. Use `ab-test-analysis`.
- The need is a general executive digest of non-data content. Use `executive-summary`.

## Inputs
Required:
- The results: numbers, tables, chart descriptions or analyst notes.

Optional, improves quality:
- The original question and audience.
- Metric definitions, time windows, data caveats.
- Business context (launches, incidents, seasonality).

If results are missing, ask for them. Never fill in numbers not present in the input.

## Process
1. Identify the audience and the decision they own; write for that decision.
2. Extract the single most important finding and write it as a headline sentence with direction, magnitude and scope ("SMB churn rose 0.9 pts in Q3, driving 80% of the total increase").
3. Separate observation (what the data shows) from interpretation (why) and label interpretations with their evidence level: confirmed, likely, hypothesis.
4. Check magnitude with context: absolute vs relative change, base size, normal variance, seasonality, prior-year comparison.
5. Decompose the change (mix vs rate, segment contribution) if the input supports it; otherwise note it as a follow-up.
6. State caveats that could change the conclusion: data gaps, definition changes, small samples, tracking issues.
7. Translate to implications: impact on revenue, cost, customers or risk, qualitatively unless figures are given.
8. Recommend 1-3 actions with owners, and next analyses if confidence is low.
9. Keep it to one screen; put supporting tables in an appendix.
10. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the user's goal continues, suggest `executive-summary` or `presentation-outline` to take the insight to leadership.

## Output format
```markdown
# Insight: <headline sentence>
**Audience:** <role> | **Period:** <window> | **Confidence:** High / Medium / Low

## What happened
- <observation with numbers from input>

## Why (evidence level)
- <driver> – confirmed / likely / hypothesis – <evidence>

## So what
- <implication for the decision>

## Recommended actions
1. <action> – <owner or [UNKNOWN]> – <by when>

## Caveats
- ...

## Next questions
- ...
```

## Quality checklist
- [ ] The headline states direction, magnitude and scope in one sentence.
- [ ] Every number traces to the input; nothing is estimated silently.
- [ ] Interpretations are labeled with evidence level.
- [ ] Absolute and relative changes are not confused (pts vs %).
- [ ] At least one concrete action is recommended.
- [ ] Caveats that could reverse the conclusion are visible.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Narrating every chart ("metric A went up, metric B went down"). Lead with the one finding that matters.
- Presenting correlation as cause. Use "coincides with" unless causality was tested.
- Reporting relative change on a tiny base ("+200%") without the absolute numbers.

## Example
Input: "Churn rose from 3.1% to 4.0% in Q3, mostly SMB on monthly plans. Price increase for monthly plans went live in July."

Excerpt of output:
- Headline: Q3 churn rose 0.9 pts, concentrated in SMB monthly-plan customers.
- Why: Coincides with the July monthly-plan price increase – likely – timing matches; no exit-survey data yet `[confirm]`.
- Action: Retention team to test an annual-plan migration offer for SMB monthly customers – owner `[UNKNOWN]`.
