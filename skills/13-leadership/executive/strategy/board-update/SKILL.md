---
description: Writes a concise executive or board update on technology: what changed since last time, a few outcome metrics against targets, top risks with trend and mitigation, and explicit asks or decisions needed. Use when a CTO, CIO or technology director reports to the board, executive committee or investors, or when a long technical status must be condensed for non-technical senior readers.
related: executive-summary, status-update, technology-strategy, budget-proposal, risk-register
prompt: Write my quarterly technology update for the board; cloud migration is 60% done, we had two major outages, and I need approval for a security investment.
---

# Write an Executive/Board Update

## Purpose
Give board members or executives, in a few minutes of reading, an honest view of technology progress, risk and the decisions they need to make, in business language and with no surprises hidden in appendices.

## When to use
- Regular board, executive committee or investor technology reporting.
- A significant event (major incident, security breach, program delay) must be reported upward.
- A decision or funding approval is needed from the most senior level.

## When not to use
- Weekly or project-level status for a delivery audience. Use `status-update` or `project-status-report`.
- Summarizing a single document or analysis. Use `executive-summary`.
- Communicating an organizational change to employees. Use `org-change-communication`.

## Inputs
Required:
- The main developments since the last update and the asks or decisions needed (or confirmation that there are none).

Optional, improves quality:
- Previous update and the commitments made in it.
- Metrics with targets and trends (availability, delivery, cost, security posture, program milestones).
- Risk register, incident reports, audit findings; the board's known concerns.

If developments are missing, ask for them. Never invent metrics, trends or dates; missing values are `[UNKNOWN]`. Remind the user to remove personal data and confidential incident details not needed at this level.

## Process
1. Identify the audience (board, executive committee, investors), its known concerns and the reading time available; set the tone to business impact, not technology detail.
2. Start with the three most important messages, including bad news; a board member reading only this section must not be misled.
3. Report progress against what was committed last time: on track, at risk or off track, and why; do not change the baseline silently.
4. Select 4-6 outcome metrics tied to business goals, each with target, current value and trend; explain any metric that moved significantly in one line.
5. Present the top 3-5 risks with trend (rising/stable/falling), impact in business terms, mitigation and owner role; include security and regulatory risk explicitly.
6. Report significant incidents factually: impact on customers or revenue, root cause at a high level, what has changed; avoid blame.
7. State asks clearly: decision, approval, funding or support needed, the options, the recommendation and the deadline for the decision.
8. Remove jargon and acronyms or define them; replace technical terms with their business consequence.
9. Label anything that is an estimate or an interpretation as `[ASSUMPTION]`, and keep supporting detail in an appendix.
10. Check length: 1-2 pages or a handful of slides for the main body.
11. If the user's goal continues, suggest `budget-proposal` for a funding ask, `risk-register` for the underlying risk detail, or `executive-summary` for a condensed pre-read.

## Output format
```markdown
# Technology Update to <audience> – <period>

## Key Messages
1. ...
2. ...
3. ...

## Decisions / Asks
| Ask | Options | Recommendation | Needed by |
|---|---|---|---|

## Progress Against Commitments
| Commitment (last update) | Status | Comment |
|---|---|---|

## Outcome Metrics
| Metric | Target | Current | Trend | Note |
|---|---|---|---|---|

## Top Risks
| Risk | Business impact | Trend | Mitigation | Owner (role) |
|---|---|---|---|---|

## Significant Events
- <event> – impact – cause (high level) – what changed

## Appendix
- ...
```

## Quality checklist
- [ ] The key messages include bad news if there is any; nothing material is buried in the appendix.
- [ ] Progress is reported against previous commitments, with no silent baseline changes.
- [ ] Every metric has a target and trend and links to a business outcome.
- [ ] Every ask states options, a recommendation and a decision deadline.
- [ ] No invented metrics or dates; estimates are labeled, and no unnecessary personal or confidential data is included.
- [ ] The main body is 1-2 pages and free of unexplained jargon.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- A good-news-only report. Boards lose trust when they learn of problems elsewhere; lead with the material issue.
- Activity metrics (tickets closed, story points) instead of outcomes. Use availability, customer impact, cost and milestone delivery.
- A vague ask ("support for security"). Name the decision, the amount or option, and when it is needed.

## Example
Input: Cloud migration 60% done, two major outages, need approval for a security investment.

Excerpt of output:
- Key message 2: Two outages this quarter affected online sales for a total of `[UNKNOWN]` hours; both traced to the legacy network segment, which the migration removes by `[confirm date]`.
- Weak ask (avoid): "We need more security budget." Strong ask: "Approve option B (managed detection service, `[amount from proposal]`/year) by the next meeting; option A (in-house team) takes 9-12 months to staff `[ASSUMPTION]`."
