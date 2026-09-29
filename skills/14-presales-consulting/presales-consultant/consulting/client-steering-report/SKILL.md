---
name: client-steering-report
description: "Writes a client-facing steering committee report for a consulting or delivery engagement, covering overall status against plan with an explicit rating rule, progress on milestones, value delivered against the agreed outcomes, budget and effort burn, top risks and issues, change requests, and the decisions the client steering group must take. Use before a client steering committee or executive review, when a periodic engagement report is due, or when delivery data must be turned into a decision-oriented client update."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 14-presales-consulting
  role: presales-consultant
  area: consulting
  title: "Write a client steering report"
  related: "steering-committee-pack, project-status-report, benefits-realization, raid-log, bad-news-delivery"
  prompt: "Write the monthly steering report for our client's CRM rollout: phase 2 is two weeks late, budget is on track, we need a decision on the data migration scope."
---

# Write a Client Steering Report

## Purpose
Give the client's steering group an honest, decision-ready view of the engagement: where it stands, what value it has delivered, what threatens it, and exactly what they need to decide, so governance time goes to decisions rather than status reading.

## When to use
- A client steering committee, executive review or quarterly business review is scheduled.
- A periodic engagement report is contractually due.
- Delivery data (plan, burn, RAID, change requests) must be translated for client executives.

## When not to use
- An internal portfolio or program steering pack for your own organization. Use `steering-committee-pack`.
- A routine team-level status update. Use `project-status-report` or `status-update`.
- Measuring realized benefits after the engagement. Use `benefits-realization`.

## Inputs
Required:
- Reporting period and engagement scope.
- Current delivery data: milestone status versus plan, key risks and issues, and any decision needed.

Optional, improves quality:
- Baseline plan, budget and effort burn; change request log.
- Agreed outcomes or KPIs from the proposal or SOW.
- Previous steering report and its action items.
- Client-side dependencies and their status.

If status data or the period is missing, ask. Never invent percentages, spend or benefits; mark them `[UNKNOWN]`.

## Process
1. State the rating rule before rating (e.g. Green: on plan; Amber: deviation recoverable within the phase without steering action; Red: needs a steering decision or re-baseline) and apply it to schedule, budget, scope, quality and overall.
2. Write a three-line summary: overall status and why, the most important change since last report, and the decisions requested today.
3. Report milestone progress against the baseline: planned versus forecast dates, variance and cause. Present forecasts, not hopes; a date without a basis is `[UNKNOWN]`.
4. Report value delivered against the agreed outcomes: what users can do now, adoption or KPI movement if measured. Separate outputs (delivered) from outcomes (achieved) and do not claim outcomes without data.
5. Report budget and effort: burn to date, forecast at completion, variance, and drivers; include pending change requests' impact.
6. Present the top 3-5 risks and issues with impact, owner (supplier or client) and mitigation, including overdue client-side dependencies stated factually and without blame.
7. Frame each decision as: context, options (including do nothing) with impact on time, cost, scope and risk, your recommendation, and the deadline for the decision.
8. Review actions from the previous steering meeting: done, open, overdue.
9. Deliver bad news early and plainly: lead with the fact, impact and recovery plan; do not bury it in an appendix.
10. Keep it to what a steering group reads in ten minutes; move detail to appendices. Label inferences and forecasts `[ASSUMPTION]` or `[FORECAST]`.
11. If the goal continues, suggest `presentation-outline` for the meeting slides, `bad-news-delivery` for a difficult message, or `benefits-realization` for outcome tracking.

## Output format
```markdown
# Steering Report: <client> — <engagement> — <period>
## Summary
| Overall | Schedule | Budget | Scope | Quality |
|---|---|---|---|---|
| <RAG> | <RAG> | <RAG> | <RAG> | <RAG> |
- Why: ...  - Key change since last report: ...  - Decisions requested: ...
Rating rule: ...

## Milestones
| Milestone | Baseline | Forecast | Variance | Cause / recovery |

## Value Delivered
| Agreed outcome | Delivered so far (output) | Evidence of outcome |

## Budget and Effort
| Budget | Spent | Forecast at completion | Variance | Drivers |

## Risks and Issues
| # | Risk / issue | Impact | Owner (supplier/client) | Mitigation | Due |

## Change Requests
| CR | Description | Impact | Status |

## Decisions Required
### D1: <title>
- Context: ...  - Options: A / B / do nothing (impact)  - Recommendation: ...  - Needed by: ...

## Previous Actions
| Action | Owner | Status |

## Appendix
```

## Quality checklist
- [ ] The rating rule is stated and each RAG follows it; no "watermelon" green over red details.
- [ ] Every decision has options, impacts, a recommendation and a deadline.
- [ ] Outputs and outcomes are separated; no unmeasured benefit claims.
- [ ] Forecasts, spend and percentages come from the input or are marked `[UNKNOWN]`.
- [ ] Client-side dependencies are stated factually, with owner and impact.
- [ ] The main body can be read in about ten minutes.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Status reporting without asks. A steering report exists to get decisions; if none are needed, say so explicitly.
- Softening delays until they become crises. Report variance when first forecast, with a recovery plan.
- Listing activities as value ("40 workshops held"). Show what the client can now do or measure.

## Example
Input: "CRM rollout, phase 2 two weeks late due to delayed client test data; budget on track; need decision on migrating 10 years of history or 3."

Weak: "Status: Green overall. Some minor delays in phase 2. Data migration being discussed."

Strong:
- Overall Amber (rule: recoverable within phase). Phase 2 go-live forecast +2 weeks; cause: test data delivered after the agreed date `[confirm days]` (client dependency).
- D1: Migration scope. Options: A) 10 years history: +`[UNKNOWN]` PD, +3 weeks `[FORECAST]`; B) 3 years plus archive access: no schedule impact. Recommendation: B. Needed by: next steering meeting.
