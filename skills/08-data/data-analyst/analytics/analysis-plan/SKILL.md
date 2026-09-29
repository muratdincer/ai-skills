---
description: Writes an analysis plan that fixes the business question, hypotheses, data sources, method, validity checks and deliverable before any query is run. Use when a stakeholder asks "why did X change", "does Y work" or "should we do Z" and the analysis needs scope, method and expectations agreed up front.
related: metric-definition, data-exploration, ab-test-analysis, insight-summary, hypothesis-statement
prompt: Write an analysis plan for this question: marketing wants to know whether the new onboarding email series improved 30-day retention.
---

# Write an Analysis Plan

## Purpose
Agree on what question is being answered, how, and with which data before spending time on queries, so the result is decision-relevant, reproducible and not biased by what the analyst happened to find first.

## When to use
- A stakeholder brings an open question ("why did conversion drop?") that could take days of exploration.
- A decision depends on the result and the method must be defensible to others.
- Several analysts or teams will work on the same question and need a shared scope.

## When not to use
- The question is a controlled experiment readout. Use `ab-test-analysis`.
- The need is a recurring view, not a one-off question. Use `dashboard-spec`.
- The data is unfamiliar and must be understood first. Use `data-exploration`.

## Inputs
Required:
- The business question in the requester's words.

Optional, improves quality:
- The decision the result will inform and who makes it.
- Known data sources, tables, existing metric definitions.
- Deadline, prior analyses, suspected causes.

If the question is missing, ask for it. List every other gap as an open question in the plan.

## Process
1. Restate the question as a decision question: "Should <decision maker> do <action>, given <evidence>?" If no decision exists, say so and propose one.
2. Define the primary metric and 1-3 secondary metrics. Reference an existing definition or flag that `metric-definition` is needed.
3. Write explicit, falsifiable hypotheses (H1, H2...) including at least one competing explanation (seasonality, mix shift, tracking change, pricing, external event).
4. Specify population, unit of analysis, time window and comparison (before/after, cohort, matched control, segment). State why that comparison isolates the effect.
5. List data sources with grain, owner, freshness and known quality issues. Mark unconfirmed sources `[ASSUMPTION]`.
6. Choose the method (descriptive breakdown, cohort analysis, difference-in-differences, regression, segmentation) and note its key assumptions and threats to validity (selection bias, confounders, survivorship, Simpson's paradox).
7. Define validity checks: row counts against source of truth, metric reconciliation to the official dashboard, sensitivity to window choice.
8. Define what result would change the decision (decision thresholds) before looking at data.
9. Plan the deliverable: format, audience, level of detail, and date.
10. Note privacy: minimize personal data, aggregate or mask identifiers, respect KVKK/GDPR purpose limitation.
11. Fill the template and list open questions with owners.

## Output format
```markdown
# Analysis Plan: <title>
| Field | Value |
|---|---|
| Requester / decision maker | <name or [UNKNOWN]> |
| Decision to inform | <decision> |
| Due date | <date or [UNKNOWN]> |

## Question
<decision question>

## Metrics
- Primary: <metric> – <definition reference>
- Secondary / guardrail: ...

## Hypotheses
- H1: ... (evidence that would support / refute)
- H2 (competing explanation): ...

## Scope and Comparison
Population: ... | Unit: ... | Window: ... | Comparison: ... | Exclusions: ...

## Data Sources
| Source | Grain | Freshness | Known issues |
|---|---|---|---|

## Method and Threats to Validity
- Method: ...
- Threats and mitigations: ...

## Validity Checks
- ...

## Decision Thresholds
- If <result>, then <recommendation>.

## Deliverable
<format, audience, date>

## Open Questions
1. <question> – <owner>
```

## Quality checklist
- [ ] The question is tied to a decision, not curiosity alone.
- [ ] At least one competing explanation is listed as a hypothesis.
- [ ] Comparison group and time window are explicit and justified.
- [ ] Decision thresholds are written before any result is seen.
- [ ] Data sources are not invented; unconfirmed ones are marked.
- [ ] Personal data handling is addressed.

## Common pitfalls
- Planning a before/after comparison without accounting for seasonality or concurrent launches. Add a control group or a year-over-year baseline.
- Letting the metric definition drift during analysis. Freeze it in the plan and log any change.
- Promising causal conclusions from observational data. State the level of evidence the method supports.

## Example
Input: "Did the new onboarding email series improve 30-day retention?"

Excerpt of output:
- Question: Should CRM keep the new series as default for all sign-ups?
- H2 (competing): Retention rose because of the pricing change launched the same week.
- Comparison: Users who signed up in the 4 weeks before vs. after launch, excluding the paid-campaign cohort; difference-in-differences against the region without the series `[ASSUMPTION: rollout was regional]`.
- Decision threshold: Keep the series if the 30-day retention uplift is at least `[TBD by CRM]` points with a confidence interval excluding zero.
