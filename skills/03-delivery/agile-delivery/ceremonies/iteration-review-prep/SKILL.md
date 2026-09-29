---
name: iteration-review-prep
description: "Prepares an iteration/sprint review: summarizes the increment against the iteration goal, orders the demo around user scenarios, states what was not done and why, and drafts targeted feedback questions and backlog-impact prompts. Use when a team's iteration review, sprint review or end-of-iteration demo is coming up and someone asks for an agenda, demo order or increment summary."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: agile-delivery
  area: ceremonies
  title: "Prepare an iteration review"
  related: "stakeholder-review-prep, demo-script, iteration-goal, burndown-analysis, retrospective-facilitation"
  prompt: "Prepare our sprint review for Thursday. Goal was 'merchants can issue partial refunds'. Done: refund API, refund UI, email notice. Not done: refund report. 8 stakeholders from finance and support are coming."
---

# Prepare an Iteration Review

## Purpose
Turn the iteration review into an inspection of the increment and a conversation that changes the backlog, not a slide show: show working results in a meaningful order, be transparent about what is not done and ask the questions whose answers the team needs.

## When to use
- An iteration/sprint review or end-of-iteration demo is scheduled.
- The team tends to demo ticket by ticket and gets little useful feedback.
- New stakeholders attend and need context to give feedback.

## When not to use
- A product-level review with executives and decisions across several iterations. Use `stakeholder-review-prep`.
- Writing the step-by-step demo script itself. Use `demo-script`.
- The team's internal improvement discussion. Use `retrospective-facilitation`.

## Inputs
Required:
- The iteration goal and the list of items completed and not completed.

Optional, improves quality:
- Attendee list with roles, and time available.
- Metrics or signals related to the goal (usage, test results, performance).
- Upcoming backlog items and open product questions.
- Definition of Done, to confirm what counts as done.

If the goal or item status is missing, ask. Otherwise proceed and list gaps as open questions.

## Process
1. Restate the iteration goal and assess whether it was met, partly met or not met, with evidence. Do not claim "met" without a demonstrable signal.
2. Include only items that meet the Definition of Done in the demo; list partially done work separately without presenting it as done.
3. Group done items into 1-3 user scenarios that tell the story of the goal; order them so the most valuable or riskiest result comes first.
4. For each scenario, name the presenter candidate, the environment and data needed, and a fallback (recording or screenshots) if the environment fails. Mark unconfirmed presenters `[TBD]`.
5. Summarize not-done items with the reason (scope change, dependency, underestimation) and where they go next; avoid blame language.
6. Write 3-6 feedback questions targeted to attendees' roles, each tied to a decision or backlog item (e.g. "Is the refund limit per order or per day?").
7. Prepare a short "what's next" view: the top upcoming backlog items and any market, usage or timeline changes that attendees should react to.
8. Build a time-boxed agenda with at least a third of the time for feedback and discussion.
9. Add a capture template for feedback, new backlog items and decisions.
10. If the user's goal continues, suggest `demo-script` to script each scenario and `retrospective-facilitation` for the team's retrospective.

## Output format
```markdown
# Iteration Review: <iteration> – <date>, <duration>
**Goal:** <goal> – **Result:** Met / Partly met / Not met – <evidence>

## Agenda
| Time | Topic | Lead |
|---|---|---|

## Demo Order
1. Scenario: <user story of the result> – Items: ... – Presenter: <name/[TBD]> – Env/data: ... – Fallback: ...

## Not Done
| Item | Status | Reason | Next |
|---|---|---|---|

## Feedback Questions
1. <question> – <audience> – <decision/backlog item it informs>

## What's Next
- ...

## Capture (fill during review)
| Feedback / idea | From | Backlog impact | Decision |
|---|---|---|---|
```

## Quality checklist
- [ ] Goal result is stated with evidence, not asserted.
- [ ] Only items meeting the Definition of Done are demoed as done.
- [ ] Demo is ordered by scenario and value, not by ticket number.
- [ ] Every feedback question is tied to a decision or backlog item.
- [ ] At least a third of the time is reserved for discussion.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Demoing half-done work "because it is almost there". It inflates perceived progress; show it only as work in progress, clearly labeled.
- Asking "Any feedback?" at the end. Open questions yield silence; ask specific, role-targeted questions.
- Treating the review as a sign-off meeting. Its output is an updated backlog, not an approval.

## Example
Input: goal "merchants can issue partial refunds"; done: refund API, refund UI, email notice; not done: refund report; finance and support attend.

Excerpt of output:
- Result: Met – a partial refund is issued end to end on staging and the merchant receives the email `[confirm staging data before the review]`.
- Not done: Refund report | Not started | Underestimated API work | Top of next iteration candidates.
- Feedback question: "Should support agents be able to issue partial refunds, or only merchants?" – support lead – informs permissions item.
