---
description: Writes a 30-60-90 day onboarding plan for a new hire with outcomes per phase, concrete first tasks, people to meet, access and learning milestones, and check-in points. Use when someone joins or moves into a new team or role, when a buddy or manager needs a structured ramp-up, or when an existing plan is only a list of documents to read.
related: technical-onboarding, onboarding-guide, goal-setting, one-on-one-prep, job-description
prompt: Write a 30-60-90 day plan for a mid-level backend engineer joining our payments team next month.
---

# Write a 30-60-90 Day Onboarding Plan

## Purpose
Give the new hire and the manager a shared, outcome-based ramp-up path, so that expectations for each phase are explicit, support is scheduled, and progress can be discussed with evidence instead of impressions.

## When to use
- A new hire, internal transfer or promoted person starts a new role.
- The manager or buddy needs a plan before day one.
- Past hires ramped slowly or unevenly and onboarding needs structure.

## When not to use
- The need is a technical setup and codebase walkthrough only. Use `technical-onboarding`.
- A general team handbook for everyone. Use `onboarding-guide`.
- Long-term goals after ramp-up. Use `goal-setting`.

## Inputs
Required:
- Role, level, team and start date (or "day 1" if unknown).

Optional, improves quality:
- Team mission, current priorities, systems owned, on-call model.
- Debrief notes on strengths and onboarding focus, previous role of the person.
- Available buddy, key stakeholders, mandatory trainings, access request lead times.

If role or level is missing, ask; without them phase expectations cannot be calibrated.

## Process
1. Define the end state at day 90 in 2-3 outcomes aligned with the level's expectations (e.g. independently delivers medium changes in service X, joins on-call rotation).
2. Plan pre-day-1: equipment, accounts, access requests with lead times, buddy assigned, first-week calendar.
3. Days 1-30 (learn): environment running, first small change merged in week 1-2, meet key people, understand architecture, customers and ways of working.
4. Days 31-60 (contribute): own scoped work items end to end, participate in reviews and incidents, shadow on-call if applicable.
5. Days 61-90 (own): lead a small feature or improvement, reverse-shadow on-call, propose one improvement from a fresh-eyes perspective.
6. For each phase, list 3-5 measurable signals of success and the support provided (buddy, pairing, docs, trainings).
7. Add a people map: who to meet, why, and by when.
8. Schedule check-ins: weekly 1:1s, end-of-phase reviews with two-way feedback on the onboarding itself.
9. Adjust for context without lowering the bar: part-time, remote, time zones, accessibility needs, prior domain knowledge; do not assume personal circumstances.
10. Mark team facts you inferred (systems, rotation, tools) as `[ASSUMPTION]` and list items the manager must confirm.
11. If the user's goal continues, suggest `technical-onboarding` for setup detail or `goal-setting` for goals after day 90.

## Output format
```markdown
# 30-60-90 Plan: <name or role> – <team> – start <date>
Manager: <name> · Buddy: <name or [TBD]>

## Day-90 Outcomes
1. ...

## Before Day 1
- [ ] Access / equipment / accounts – owner – lead time

## Days 1-30: Learn
| Outcome | First tasks | Success signals | Support |
|---|---|---|---|

## Days 31-60: Contribute
| Outcome | Tasks | Success signals | Support |
|---|---|---|---|

## Days 61-90: Own
| Outcome | Tasks | Success signals | Support |
|---|---|---|---|

## People to Meet
| Person / role | Why | By |
|---|---|---|

## Check-ins
- Weekly 1:1 · Day 30 / 60 / 90 reviews (two-way)

## Assumptions / To Confirm
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Each phase has outcomes, not only activities or reading lists.
- [ ] A first real contribution is planned within the first two weeks.
- [ ] Success signals are observable and calibrated to the level.
- [ ] Support (buddy, pairing, trainings) is named for each phase.
- [ ] Check-ins include feedback on the onboarding, not only on the person.
- [ ] No assumptions about personal circumstances; adjustments are framed as options.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- A month of reading documentation. Pair reading with a small, real change early.
- Uncalibrated expectations (a mid-level hire expected to own the architecture by day 60). Tie outcomes to the level definition.
- No plan for access lead times. Start requests before day 1.

## Example
Input: Mid-level backend engineer, payments team, services: payment-gateway, ledger; weekly on-call.

Excerpt of output:
- Day-90 outcome: Independently delivers medium changes in payment-gateway and completes one reverse-shadow on-call week.
- Days 1-30 first task: Fix a labeled starter issue in payment-gateway with the buddy; merged by day 10.
- Weak signal (avoid): "Understands the system." Strong signal: "Explains the refund flow across gateway and ledger in a whiteboard session with the buddy."
