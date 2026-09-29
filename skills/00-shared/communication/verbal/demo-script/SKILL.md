---
name: demo-script
description: "Writes a product or feature demo script with a user-story flow, click-by-click steps, talking points tied to audience value, prepared data, timing and a fallback for every risky step. Use when a team must demo software to stakeholders, customers, a review session or a sales prospect and wants a rehearsable run sheet instead of improvising."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: communication
  area: verbal
  title: "Write a demo script"
  related: "presentation-outline, iteration-review-prep, stakeholder-review-prep, uat-scenarios, elevator-pitch"
  prompt: "Write a 10-minute demo script for showing the new invoice approval workflow to the finance managers at the iteration review."
---

# Write a Demo Script

## Purpose
Produce a rehearsable run sheet that shows working software through a realistic user journey, links every step to value the audience cares about, and survives the usual demo failures, so the session ends with feedback or a decision rather than apologies.

## When to use
- Showing a finished or in-progress feature at an iteration review or stakeholder session.
- A customer, prospect or executive demo of a product capability.
- Recording a walkthrough video that must be concise and repeatable.

## When not to use
- The session is mostly argument and data, with little live software. Use `presentation-outline`.
- The goal is formal acceptance by users. Use `uat-scenarios`.
- Preparing the whole review meeting, not only the demo part. Use `iteration-review-prep` or `stakeholder-review-prep`.

## Inputs
Required:
- What will be demoed (feature, scope, environment) and to whom.
- Time available.

Optional:
- User stories or acceptance criteria, known defects, environment and data constraints, the question the audience must answer afterwards.

If the feature or audience is unknown, ask first. Do not describe screens or behaviors the user has not confirmed; mark them `[TBD: confirm UI]`.

## Process
1. Define the demo goal: the one thing the audience should believe or decide afterwards (e.g. "approve rollout to region 2", "give feedback on approval rules").
2. Pick a persona and a realistic scenario from the audience's world ("Ayşe, finance manager, approves 40 invoices on month end"), not a feature tour.
3. Order the flow as a story: trigger, main path, the "wow" moment, outcome. Put the highest-value moment in the first third, before attention drops.
4. Write the steps as a run sheet: action (what to click or type), what the audience sees, talking point in value terms ("this saves the second approval email"), not implementation details.
5. Prepare data and state: named accounts, test records, reset steps, feature flags; use synthetic or masked data, never real personal or customer data on screen.
6. Mark risk for each step (slow service, unstable integration, known defect) and write a fallback: pre-recorded clip, screenshot, pre-loaded second tab, or "narrate and move on".
7. State scope honestly: what is not done or is mocked, said out loud before someone discovers it.
8. Budget time: demo at most 60% of the slot; keep the rest for questions and the feedback or decision prompt.
9. Write 2-3 targeted feedback questions to ask at the end, closed enough to get usable answers.
10. Add a pre-demo checklist (environment up, logged in, notifications off, zoom level, data reset) and a rehearsal note.
11. If the user's goal continues, suggest `presentation-outline` for the framing slides or `iteration-review-prep` for the rest of the review session.

## Output format
```markdown
# Demo Script: <feature> for <audience>
Goal: <what the audience should decide/believe> | Slot: <min> (demo <min>, Q&A <min>)
Persona and scenario: <name, role, situation>
Not in scope / mocked: ...

## Pre-demo checklist
- [ ] Environment <name> up, build <[TBD]>   - [ ] Test data reset   - [ ] Notifications off, zoom 125%

## Run sheet
| # | Action | Audience sees | Talking point (value) | Risk | Fallback | Time |
|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | Low/Med/High | ... | 1 min |

## Closing
- Recap in one sentence: ...
- Feedback questions: 1. ... 2. ...
- Ask / next step: ...
Assumptions: [ASSUMPTION] ...
```

## Quality checklist
- [ ] The demo follows one persona's scenario, not a menu-by-menu tour.
- [ ] Every step has a value-oriented talking point.
- [ ] Every medium or high risk step has a concrete fallback.
- [ ] No real personal or customer data appears on screen.
- [ ] Unfinished or mocked parts are declared.
- [ ] Timing leaves at least 40% of the slot for questions and feedback.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Demoing the build pipeline, admin screens or code to a business audience. Show the user outcome.
- Live data entry of long forms. Pre-fill and show only the meaningful fields.
- Ending with "any questions?" and silence. Ask the specific feedback questions prepared in the script.

## Example
Input: 10 minutes, finance managers, new invoice approval workflow.

Weak step: "Open the Invoices menu, then Settings, then show the workflow configuration table."

Strong (excerpt):
| 2 | Open invoice INV-TEST-014 from the inbox | Amount over limit, routed to second approver automatically | "No more forwarding emails: over-limit invoices find the right approver themselves" | Med (routing service slow) | Pre-loaded second tab with routed invoice | 1.5 min |
Feedback question: "Is the €10k threshold `[TBD: confirm]` right for your region, or should it be configurable per cost center?"
