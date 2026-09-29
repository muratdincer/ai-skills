---
name: release-planning
description: "Plans a release: target outcome, candidate scope split into committed and stretch, forecast of when the scope can be done based on throughput or velocity ranges, dependencies, milestones, risks and a confidence level, plus the scope-versus-date trade-off options. Use when a product owner must answer what will be in a release and when, negotiate a fixed date, or prepare a release plan for stakeholders."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-owner
  area: planning
  title: "Plan a release"
  related: "roadmap, monte-carlo-forecast, velocity-analysis, release-plan, dependency-map"
  prompt: "We want to release the new onboarding flow by 15 March. Here are the 18 remaining items and our last 8 iterations' throughput. Is it feasible and what scope should we commit?"
---

# Plan a Release

## Purpose
Give stakeholders a release plan whose scope, date and confidence are based on the team's actual delivery data, with explicit trade-offs, so that commitments are realistic and surprises surface early.

## When to use
- A release, launch or milestone must be planned across several iterations/sprints or weeks of flow.
- A date is fixed externally and scope must be negotiated.
- Scope is fixed and stakeholders ask when it will be done.
- An existing release plan needs re-forecasting after scope or capacity changes.

## When not to use
- Long-term direction across quarters. Use `roadmap`.
- Technical deployment steps, cutover and rollback. Use `release-plan` or `deployment-checklist`.
- Only the statistical forecast is needed. Use `monte-carlo-forecast`.

## Inputs
Required:
- Release goal and candidate scope (items, ideally sized or countable).
- Either a target date or a question "when?".
- Historical delivery data (throughput per week/iteration or velocity). If missing, ask; without data, produce a plan only with explicit `[ASSUMPTION]` capacity and Low confidence.

Optional, improves quality:
- Team availability changes (holidays, onboarding, shared members).
- Dependencies on other teams or vendors, hardening/stabilization needs, release windows.

## Process
1. State the release goal as an outcome, not a scope list.
2. Split candidate scope into committed (must be in for the goal to be met) and stretch (nice to have). Keep committed to what the goal truly requires.
3. Make sure items are at a comparable granularity; if big items remain, estimate them in the same unit or break them down (`story-splitting`).
4. Forecast using ranges, not a single number: use the lowest, median and highest recent throughput/velocity (or a Monte Carlo result) to compute a pessimistic, likely and optimistic completion. Adjust for known capacity changes and add expected scope growth (use observed history if available, otherwise mark an assumption).
5. Answer the planning question: for a fixed date, which scope fits at 85% confidence; for fixed scope, which date is reached at 50% and 85%.
6. Lay out milestones: feature complete, stabilization, release readiness decision, release. Include dependency dates.
7. Identify risks and their effect on the forecast; propose mitigations.
8. Present trade-off options (move date, cut stretch scope, add capacity with its ramp-up cost) with consequences.
9. Define re-forecast triggers and cadence (e.g. every iteration or weekly with actual throughput).
10. If the user's goal continues, suggest `monte-carlo-forecast` for a probabilistic date or `release-plan` for the operational release and deployment plan.

## Output format
```markdown
# Release Plan: <release name>
Goal: <outcome> · Owner: <product owner> · Plan date: <date>

## Scope
| Item | Size | Committed / Stretch | Dependency |
|---|---|---|---|

## Forecast
Data used: <throughput/velocity sample, period>
| Scenario | Rate | Completion (committed) | Completion (all) |
|---|---|---|---|
| Pessimistic | | | |
| Likely | | | |
| Optimistic | | | |
Confidence for target date <date>: <High/Medium/Low> – <reason>

## Milestones
| Milestone | Target | Depends on |
|---|---|---|

## Risks and Mitigations
- <risk> – <impact on forecast> – <mitigation>

## Trade-off Options
1. <option> – <consequence>

## Re-forecast
<trigger and cadence>
```

## Quality checklist
- [ ] Forecast uses a range from real data, or its assumptions are marked and confidence is Low.
- [ ] Committed scope is smaller than the pessimistic capacity when the date is fixed.
- [ ] Scope growth and availability changes are considered.
- [ ] Every milestone and dependency has a date or `[TBD]`.
- [ ] Trade-offs are presented as options for a decision, not hidden.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Planning at 100% of average velocity. Averages are hit only half the time; commit against a pessimistic or 85th-percentile rate.
- Ignoring discovered work. Backlogs typically grow during a release; use observed growth or add an explicit buffer.
- Treating the plan as fixed. Re-forecast with actuals every cycle and communicate changes early.

## Example
Input: "18 items remaining, throughput last 8 weeks: 3, 5, 4, 2, 6, 4, 3, 5 items/week; target 15 March, 7 weeks away."

Excerpt of output:
| Pessimistic | 2/week | 14 items by target | – |
| Likely | 4/week | 18 items in ~4.5 weeks | – |
- Committed: 12 items essential to the onboarding goal; stretch: 6 items. Confidence for 15 March on committed scope: High.
- Assumption: no scope growth data; 10% growth added `[ASSUMPTION]`.
