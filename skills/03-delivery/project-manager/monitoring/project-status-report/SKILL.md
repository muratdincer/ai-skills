---
description: Writes a periodic project status report covering overall and per-dimension RAG status (schedule, cost, scope, quality, resources), progress against milestones, variance explanations, top risks and issues, and decisions needed from sponsors. Use for weekly or monthly reporting to sponsors or steering bodies, or when project health must be summarized objectively from plan and actual data.
related: status-update, steering-committee-pack, earned-value-analysis, raid-log, executive-summary
prompt: Write this month's status report for the HR system project from these milestone updates, budget actuals and the RAID log.
---

# Write a Project Status Report

## Purpose
Give sponsors an honest, evidence-based view of project health against the baseline and a clear list of decisions they must make, in a format they can read in two minutes.

## When to use
- Regular reporting cycle to sponsor, steering committee or PMO.
- Before a governance meeting where decisions are required.
- When status must be reconstructed from scattered updates and data.

## When not to use
- A short team or cross-functional update not tied to a baseline. Use `status-update`.
- A full steering meeting pack with financials and options. Use `steering-committee-pack`.
- Reporting to an external client with value narrative. Use `client-steering-report`.

## Inputs
Required:
- Reporting period and baseline (milestones, budget) or last report.
- Progress data: milestone status, completed work, actual costs or effort.

Optional, improves quality:
- RAID log, change requests, earned value metrics, team updates, organizational RAG definitions.

If progress data is missing, ask for it. Do not infer status from silence.

## Process
1. Define RAG thresholds, using organizational rules if given; otherwise: Green within tolerance, Amber tolerance at risk but recoverable by the PM, Red tolerance breached or needs sponsor action. State them.
2. Assess each dimension (schedule, cost, scope, quality, resources) against the baseline with evidence (dates, amounts, counts).
3. Set overall status: not better than the worst dimension that affects objectives; explain if different.
4. Show trend versus last period (improving, stable, declining).
5. List milestones: baseline date, forecast date, variance, status.
6. Summarize achievements of the period and plan for the next period (outcomes, not activities).
7. Pull top 3-5 risks and issues with owner, action and due date.
8. Formulate decisions needed as explicit asks with options, recommendation and deadline.
9. Write a 3-sentence executive summary last.
10. Mark missing data `[UNKNOWN]` and avoid softening language that hides Red status.
11. Label every inferred element `[ASSUMPTION]` and move it to assumptions or open questions. If the user's goal continues, suggest the next skill: `raid-log` to update the underlying items, `earned-value-analysis` when cost and schedule indices are needed, or `steering-committee-pack` for a decision forum.

## Output format
```markdown
# Project Status Report: <project> – <period>
Overall: <RAG> (trend <↑/→/↓>) | PM <name> | Date <date>
## Executive Summary
## Status by Dimension
| Dimension | RAG | Trend | Evidence / variance | Recovery action |
## Milestones
| Milestone | Baseline | Forecast | Variance | Status |
## Achievements This Period
## Plan for Next Period
## Top Risks and Issues
| ID | Description | Owner | Action | Due |
## Decisions Needed
| Decision | Options | Recommendation | Needed by |
## RAG Definitions
```

## Quality checklist
- [ ] Every RAG rating is backed by evidence against the baseline.
- [ ] Overall status is consistent with dimension statuses.
- [ ] Decisions are phrased as explicit asks with a deadline.
- [ ] No watermelon reporting: problems visible, not buried in text.
- [ ] Missing data is marked, not assumed Green.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Green until suddenly Red. Report Amber early with a recovery plan.
- Activity lists instead of outcomes ("had meetings with vendor"). Report what changed.
- Decisions hidden in risk text. Put asks in their own section.

## Example
Input: "UAT start slipped from 1 Mar to 15 Mar; budget 62% spent at 55% complete; vendor resource replaced."

Excerpt of output:
| Schedule | Amber | ↓ | UAT start +2 weeks; go-live still achievable using buffer | Parallel test data preparation |
| Cost | Amber | → | 62% spent vs 55% complete `[confirm EV method]` | Review vendor burn rate |
- Decision needed: Approve use of 1 week of project buffer for UAT — needed by 5 Mar.
