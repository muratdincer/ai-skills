---
name: benefits-realization
description: "Tracks benefits realization after delivery by turning planned benefits into measurable indicators with baselines, targets, owners and measurement dates, comparing planned versus actual values, attributing the change, and recommending corrective actions or re-forecasts. Use after a project or program goes live, at a post-implementation or benefits review, when a business case needs to be checked against results, or when someone asks \"did we get the value we promised\"."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: program-pmo
  area: portfolio
  title: "Track benefits realization"
  related: "kpi-definition, cost-benefit-analysis, feature-adoption-review, project-closure-report, portfolio-prioritization"
  prompt: "Check benefits realization for our self-service portal six months after go-live; the business case promised 30% fewer call-center contacts and faster onboarding."
---

# Track Benefits Realization

## Purpose
Show honestly whether the value promised in the business case is arriving, how much can be attributed to the delivered change, and what the benefit owners must do to close the gap, so the portfolio learns from results and funding decisions rest on evidence.

## When to use
- A project or program has gone live and its benefits are due to be measured.
- A scheduled post-implementation or benefits review is coming up.
- A portfolio board wants planned versus actual value before funding the next phase.
- A benefits register needs to be created or repaired because the business case had vague benefits.

## When not to use
- The benefits have not been estimated yet (pre-investment). Use `cost-benefit-analysis`.
- The question is usage of a single product feature. Use `feature-adoption-review`.
- The goal is closing the project formally. Use `project-closure-report`, feeding it this review.

## Inputs
Required:
- The planned benefits (business case, charter or stated promises).
- Any actual data available after delivery, or confirmation that none exists yet.

Optional, improves quality:
- Baselines measured before delivery, measurement definitions, data sources.
- Benefit owners in the business, go-live date and adoption data.
- Other initiatives or external factors affecting the same indicators.
- Costs incurred (for net benefit and return comparison).

If the planned benefits are missing, ask. Never fill actual values that were not provided; mark them `[UNKNOWN]` and plan how to measure them.

## Process
1. List each planned benefit and classify it: financial cash-releasing, financial non-cash (capacity freed), non-financial measurable (quality, speed, satisfaction), compliance or risk reduction. Note any disbenefits.
2. Make each benefit measurable: indicator, formula, data source, baseline (value and date), target, target date and benefit owner (a business role, not the project manager). Mark baselines reconstructed after the fact `[ASSUMPTION]`.
3. Map each benefit to its enabling change and the adoption it depends on (e.g. portal use rate), because benefits lag adoption.
4. Collect actuals per indicator and period; state source and date for each value.
5. Compare planned versus actual: variance, trend, and whether the target date has passed. Rate each benefit: On track, Behind, At risk, Achieved, Not measurable.
6. Attribute: estimate how much of the change comes from this initiative versus seasonality, other initiatives or external factors. Use control groups, before-after with trend, or owner judgement, and label the method and confidence.
7. For each benefit behind or at risk, find the cause (adoption gap, process not changed, baseline wrong, target unrealistic, external) and propose a corrective action with owner and date, or a formal re-forecast.
8. Summarize total realized versus planned value where financial; do not add non-cash and cash benefits into one figure without saying so. Identify unplanned benefits and disbenefits.
9. Define the next measurement points and when tracking stops (benefit sustained or closed).
10. Capture lessons for future business cases (which estimates were optimistic, which indicators were hard to measure).
11. If the goal continues, suggest `kpi-definition` to fix weak indicators, `project-closure-report` to record the outcome, or `portfolio-prioritization` to feed results into the next funding round.

## Output format
```markdown
# Benefits Realization Review: <initiative> — <review date>
Go-live: <date> · Review point: <e.g. +6 months> · Overall: <RAG>

## Benefits Register
| ID | Benefit | Type | Indicator (formula) | Baseline (date) | Target (date) | Actual (date, source) | Variance | Status | Owner |
|---|---|---|---|---|---|---|---|---|---|

## Adoption Drivers
| Enabler | Expected adoption | Actual | Impact on benefits |
|---|---|---|---|

## Attribution
| Benefit | Method | Attributed share | Confidence |
|---|---|---|---|

## Gaps and Corrective Actions
| Benefit | Cause | Action / re-forecast | Owner | Due |
|---|---|---|---|---|

## Unplanned Benefits and Disbenefits
## Next Measurement Points
## Lessons for Future Business Cases
## Assumptions and Data Gaps
- [ASSUMPTION] / [UNKNOWN] ...
```

## Quality checklist
- [ ] Every benefit has an indicator, formula, baseline, target, date and a business owner.
- [ ] Every actual value has a source and date; missing actuals are `[UNKNOWN]`, not estimated.
- [ ] Attribution method and confidence are stated for each benefit.
- [ ] Benefits behind target have a cause and a corrective action or re-forecast.
- [ ] Cash and non-cash benefits are not silently summed; disbenefits are listed.
- [ ] Inferences and reconstructed baselines are labeled.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Assigning benefit ownership to the project manager. Benefits are realized in the business after the project ends; the owner must be a business role.
- Claiming the whole movement of a KPI. Other initiatives and seasonality move the same numbers; state attribution and confidence.
- Measuring once at go-live. Benefits lag adoption; schedule several measurement points.

## Example
Input: "Self-service portal, 6 months after go-live; business case: 30% fewer call-center contacts, faster onboarding."

Excerpt of output:
| ID | Benefit | Baseline | Target | Actual | Status |
|---|---|---|---|---|---|
| B1 | Contact volume reduction | `[UNKNOWN]` monthly contacts before go-live | −30% by +12 months | −12% at +6 months (call-center report) | Behind |
| B2 | Faster onboarding | `[UNKNOWN]` | `[TBD]` days | not measured | Not measurable |

- B1 cause: portal adoption 35% vs 60% expected; action: add portal link to IVR and confirmation emails — owner: customer-service manager `[TBD: name]`.
- B2: define indicator "days from application to active account" and reconstruct baseline from CRM `[ASSUMPTION]`.
