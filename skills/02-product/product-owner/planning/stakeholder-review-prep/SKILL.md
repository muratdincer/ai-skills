---
name: stakeholder-review-prep
description: "Prepares a product or stakeholder review: what was built and why, how it moves the product goal, what feedback is needed from whom, which decisions must be taken, and an agenda with demo flow and the updated outlook. Use before an iteration/sprint review, a monthly product review or a steering-style product checkpoint where stakeholders must inspect progress and give input."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-owner
  area: planning
  title: "Prepare a product review"
  related: "iteration-review-prep, demo-script, roadmap, feature-adoption-review, meeting-agenda"
  prompt: "Prepare our monthly product review with the sales and operations heads: we shipped bulk upload and the new invoice screen; I need decisions on the pricing page and feedback on the mobile beta."
---

# Prepare a Product Review

## Purpose
Turn a stakeholder review into a working session that produces feedback and decisions, not a status broadcast. The product owner leaves with validated or adjusted direction and clear owners for follow-ups.

## When to use
- Before an iteration/sprint review, monthly or quarterly product review with business stakeholders.
- Stakeholder decisions (scope, priority, budget, launch) are pending.
- A shipped feature needs structured feedback from users or business owners.

## When not to use
- The team-level demo sequence and increment summary. Use `iteration-review-prep`.
- A formal governance meeting on budget and risk across projects. Use `steering-committee-pack`.
- Only the live demo storyline is needed. Use `demo-script`.

## Inputs
Required:
- What was delivered since the last review (items, features) and the current product goal.
- The audience of the review. If missing, ask; the content depends on who decides.

Optional, improves quality:
- Usage or outcome data for delivered features.
- Pending decisions, open risks, roadmap changes.
- Feedback received so far, previous review's action items.

## Process
1. Define the review's purpose in one line and the 1-3 outcomes the product owner needs (e.g. decision on X, feedback on Y, agreement on next priorities).
2. Map the audience: who decides what, who gives which feedback, who only needs information. Invite accordingly.
3. Summarize what was built in terms of user outcomes, grouped by goal, and state what was not done and why.
4. Pull evidence: early usage, quality or support signals. If unavailable, say so rather than implying success.
5. Formulate feedback questions per feature: specific, open, and tied to a decision (e.g. "Would this replace the current Excel process for your team? What blocks it?").
6. Write each decision request as: context, options, recommendation, consequence of not deciding, needed by.
7. Update the outlook: what comes next, changes to roadmap or release plan, risks needing stakeholder help.
8. Build a timeboxed agenda: context (short) → demo/walkthrough → feedback → decisions → outlook → actions. Put decisions before the time is likely to run out.
9. Prepare a pre-read (one page) and a follow-up template for capturing feedback and decisions.
10. If the user's goal continues, suggest `demo-script` to script the walkthrough and `meeting-agenda` to send the invitation.

## Output format
```markdown
# Product Review: <product> – <date>
Purpose: <one line> · Needed outcomes: <list>
Audience: <name/role – decides / advises / informed>

## Agenda (<total> min)
| Time | Topic | Presenter | Outcome |
|---|---|---|---|

## What We Delivered
| Goal | Delivered | User outcome | Evidence |
|---|---|---|---|
Not done: <item – reason>

## Feedback We Need
- <feature>: <question> – from <who>

## Decisions Needed
### D1: <title>
Context · Options · Recommendation · If not decided · Needed by

## Outlook
- Next: ...
- Changes to plan: ...
- Risks needing help: ...

## Follow-up Template
| Feedback / decision | Owner | Due |
|---|---|---|
```

## Quality checklist
- [ ] Each decision request has options, a recommendation and a deadline.
- [ ] Feedback questions are specific and tied to a decision or next step.
- [ ] Delivered work is framed as outcomes, with evidence or an explicit "no data yet".
- [ ] Undelivered commitments are disclosed with reasons.
- [ ] The agenda reserves time for decisions and feedback, not only demo.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Running the review as a slide-based status report. Show working software or real screens and spend most time on input.
- Asking "any feedback?" at the end. Prepare targeted questions per audience.
- Burying the bad news. Disclose slips and their impact up front, with the adjusted outlook.

## Example
Input: "Shipped bulk upload and new invoice screen; need a decision on the pricing page, feedback on the mobile beta. Audience: sales and operations heads."

Excerpt of output:
- Feedback: Bulk upload – "Which customer files still fail the upload today, and who handles them?" – from Operations head.
### D1: Pricing page publication
Options: publish now with 3 tiers / wait for enterprise tier. Recommendation: publish now. If not decided by <date [TBD]>, the Q2 campaign slips.
