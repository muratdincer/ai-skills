---
name: project-closure-report
description: "Writes a project closure report that compares outcomes with the original objectives and baselines, explains scope, schedule, cost and quality variances, confirms acceptance and handover to operations, lists open items with owners, records lessons learned and sets up benefits tracking. Use when a project or phase is ending, when the sponsor needs a formal close-out decision, or when a project is cancelled and must be closed in an orderly way."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: project-manager
  area: closure
  title: "Write a project closure report"
  related: "acceptance-certificate, handover-document, lessons-learned, benefits-realization, earned-value-analysis"
  prompt: "Our CRM migration went live last month. Write the closure report from the charter, final status report and budget actuals."
---

# Write a Project Closure Report

## Purpose
Formally close a project or phase with an honest account of what was delivered against what was promised, what remains and who owns it, so the sponsor can release the team and budget and the organization can learn from it.

## When to use
- The final deliverables are accepted and the project or phase is ending.
- A project is cancelled or paused and needs an orderly close-out.
- The sponsor or PMO requires a closure gate decision.

## When not to use
- Only running a lessons-learned session. Use `lessons-learned`.
- Only transferring a system to support. Use `handover-document`.
- Measuring benefits long after closure. Use `benefits-realization`.

## Inputs
Required:
- Original objectives and baselines (charter, scope statement, schedule, budget) or their key figures.
- Final actuals: delivered scope, dates, costs, acceptance status.

Optional, improves quality:
- Final status report, RAID log, change log, acceptance certificates, handover records.
- Lessons-learned notes, stakeholder feedback, benefits hypotheses.

If objectives or final actuals are missing, ask for them. Never fill variances with estimates.

## Process
1. State the closure type (completed, completed with exceptions, cancelled, paused) and the closure date.
2. List each original objective and success criterion with the achieved result and evidence; mark results not yet measurable as `[TBD – measure by <date>]`.
3. Compare scope: delivered, descoped (with CR reference), added (with CR reference), and not delivered.
4. Compare schedule and cost to the original and the final approved baseline; show both so approved changes are distinguished from overruns.
5. Summarize quality: acceptance status per deliverable, open defects by severity, known limitations accepted by the business.
6. Confirm operational handover: support model, documentation, access, warranty or hypercare period and its end date.
7. List open items (issues, risks, actions, defects) with an owner outside the project team and a due date; flag orphans.
8. Close administration: contracts and POs, licenses, environments, access rights, archiving of records; mark unknown statuses.
9. Summarize lessons learned as actionable recommendations with the owner who should adopt them.
10. Define benefits tracking: which benefit, metric, baseline, target, measurement date and owner after closure.
11. Request the closure decision with sign-off lines and, if the user's goal continues, suggest `lessons-learned`, `handover-document` or `benefits-realization`.

## Output format
```markdown
# Project Closure Report: <project>
Closure type: <...> | Closure date: <...> | Sponsor: <...> | PM: <...>

## Executive Summary
## Objectives vs Outcomes
| Objective / success criterion | Target | Achieved | Evidence |
## Scope
| Item | Status (Delivered/Descoped/Added/Not delivered) | CR ref |
## Schedule and Cost
| Measure | Original baseline | Final baseline | Actual | Variance vs final | Main reasons |
## Quality and Acceptance
## Operational Handover
## Open Items Transferred
| Item | Type | New owner | Due |
## Administrative Closure
## Lessons Learned
| Lesson | Recommendation | Adopting owner |
## Benefits Tracking
| Benefit | Metric | Baseline | Target | Measure on | Owner |
## Closure Approval
| Role | Name | Decision | Date |
```

## Quality checklist
- [ ] Every original objective is reported, including missed ones.
- [ ] Variances distinguish approved changes from overruns.
- [ ] Every open item has an owner outside the dissolving project team.
- [ ] Handover and hypercare end dates are explicit or marked `[TBD]`.
- [ ] Lessons are actionable recommendations, not complaints or blame.
- [ ] No figures are invented; gaps are marked.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Comparing only to the last rebaselined plan, which hides the true story. Show the original too.
- Closing with open items owned by people who are leaving. Transfer ownership explicitly.
- Declaring success on delivery alone when business outcomes are not yet measurable. Set benefit measurement dates.

## Example
Input: "CRM migration live on 3rd. Budget 800k, actual 910k (approved CR +70k). Planned go-live 1st of previous month. 12 minor defects open."

Excerpt of output:
- Cost: Original 800k, final baseline 870k, actual 910k → +40k vs final baseline (+110k vs original, of which 70k approved).
- Schedule: go-live about one month later than original `[confirm exact days and reason]`.
- Open items: 12 minor defects → application support team `[owner name TBD]`, due in hypercare `[end date TBD]`.
