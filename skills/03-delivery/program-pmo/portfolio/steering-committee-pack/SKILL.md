---
description: Prepares a steering committee pack that leads with the decisions needed, then gives a concise status against baseline, key risks and issues, financials (budget, actuals, forecast) and benefits outlook, with options and a recommendation for each decision. Use before a steering committee, project board or sponsor review, when monthly program reporting must be turned into a decision-oriented pack, or when someone asks to prepare "the steerco deck" or "board update" for a project or program.
related: project-status-report, executive-summary, raid-log, decision-log, presentation-outline
prompt: Prepare the steering committee pack for next Thursday: we are 3 weeks late on integration testing, 8% over budget, and need a decision on descoping the reporting module.
---

# Prepare a Steering Committee Pack

## Purpose
Give the steering committee what it needs to steer: the decisions it must take today with options and a recommendation, and just enough status, risk, financial and benefit information to take them confidently, instead of a progress report it merely reads.

## When to use
- Before a scheduled steering committee, project board or sponsor review.
- A program's regular report must be converted into a decision-oriented pack.
- A tolerance breach (time, cost, scope, quality) needs to be brought to the board.

## When not to use
- The audience is the team or wider stakeholders who need status only. Use `project-status-report` or `status-update`.
- An external client's steering report is required. Use `client-steering-report`.
- A company-level board update across all topics is needed. Use `board-update`.

## Inputs
Required:
- Current status against plan (milestones, scope, quality) and the decisions or escalations needed.
- Financial position if the committee oversees budget (budget, actuals, forecast), or explicit confirmation that it does not.

Optional, improves quality:
- Baseline plan, tolerances agreed with the board, previous pack and its actions.
- RAID log, change requests, benefits plan.
- Committee members and their concerns.

If status or the decisions needed are missing, ask. Missing figures stay `[UNKNOWN]`; never estimate money without a stated basis.

## Process
1. Identify the committee's purpose and members, the tolerances it set, and the actions from the previous meeting. Report each prior action as done, in progress or overdue.
2. List the decisions needed. For each, write the question in one line, the options (including "do nothing"), the impact of each on time, cost, scope, risk and benefits, the recommendation with rationale, and the deadline after which the decision loses value.
3. Summarize overall status with RAG per dimension (schedule, cost, scope, quality, risk, benefits), each backed by a fact and a trend (improving, stable, worsening). Define RAG thresholds relative to tolerances.
4. Show milestones against baseline: planned, forecast, variance, and cause for each variance. Distinguish forecast from hope; state the basis of each forecast.
5. Present financials: budget, actuals to date, committed, estimate to complete, estimate at completion, variance and contingency remaining. Label derived figures and flag missing ones `[UNKNOWN]`.
6. Select the top risks and issues (no more than about five) that need committee awareness or action; give owner, impact, mitigation and what is asked of the committee.
7. Report benefits outlook: are planned benefits still achievable, and what has changed their size or timing?
8. Write the one-page executive summary last: overall status, the decisions needed, and the single most important message.
9. Keep the main pack short (about 5-8 pages or slides); move detail to an appendix.
10. Check the pack from the committee's view: can each member decide without reading the appendix? Is anything here a surprise that should have been pre-wired with the sponsor? Note who to brief before the meeting.
11. If the goal continues, suggest `decision-log` to record the outcomes, `raid-log` to update risks, or `presentation-outline` to turn the pack into slides.

## Output format
```markdown
# Steering Committee: <project / program> — <meeting date>
## 1. Executive Summary
Overall: <RAG> (<trend>) · Key message: <one sentence> · Decisions needed: <n>

## 2. Decisions Required
### D1: <question>
| Option | Time | Cost | Scope | Risk | Benefits |
|---|---|---|---|---|---|
Recommendation: <option> — <rationale> · Decide by: <date>

## 3. Status
| Dimension | RAG | Trend | Evidence |
|---|---|---|---|
## 4. Milestones vs Baseline
| Milestone | Baseline | Forecast | Variance | Cause | Forecast basis |
|---|---|---|---|---|---|
## 5. Financials
| Budget | Actual | Committed | ETC | EAC | Variance | Contingency left |
|---|---|---|---|---|---|---|
## 6. Top Risks and Issues
| ID | Description | Owner | Impact | Mitigation | Ask of committee |
|---|---|---|---|---|---|
## 7. Benefits Outlook
## 8. Previous Actions
## Appendix
## Assumptions and Data Gaps
- [ASSUMPTION] / [UNKNOWN] ...
```

## Quality checklist
- [ ] Decisions needed come first, each with options, impacts, a recommendation and a decide-by date.
- [ ] Every RAG rating has evidence, a trend and a threshold tied to the agreed tolerances.
- [ ] Milestone forecasts state their basis; variances state their cause.
- [ ] Financial figures are sourced or labeled; nothing is invented.
- [ ] Risks shown are limited to those needing committee awareness or action.
- [ ] The main pack is short enough to decide without the appendix; inferences are labeled.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Watermelon reporting (green outside, red inside). Tie RAG to tolerances and evidence, and show trend.
- Asking the committee to "note" a problem without a decision. Frame an explicit ask with options.
- Surprising the sponsor in the meeting. Pre-wire major bad news and contentious recommendations beforehand.

## Example
Input: "3 weeks late on integration testing, 8% over budget, need decision on descoping the reporting module."

Excerpt of output:
- D1: Descope the reporting module from release 1 to protect the go-live date?
  | Option | Time | Cost | Scope | Risk |
  |---|---|---|---|---|
  | A. Keep scope | +3 weeks `[ASSUMPTION]` | +`[UNKNOWN]` | Full | Regulatory date at risk |
  | B. Move reporting to release 2 | Date held | Within tolerance `[TBD: finance check]` | Reporting delayed | Interim manual reports needed |
  Recommendation: B — protects the fixed go-live date; interim reporting owner to be named. Decide by: this meeting.
- Cost: Amber, worsening — EAC 8% over budget against a 10% tolerance.
