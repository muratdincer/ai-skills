---
name: issue-management
description: "Manages a single project issue from logging to closure: states it precisely, assesses impact and urgency, finds the cause, sets a resolution plan with owner and dates, defines escalation triggers and closure criteria, and tracks it until verified resolved. Use when something is already going wrong and affecting scope, schedule, cost or quality, such as a blocked team, a failed dependency, a vendor slip or a realized risk."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: project-manager
  area: monitoring
  title: "Manage an issue"
  related: "raid-log, escalation-message, five-whys, change-control, decision-log"
  prompt: "Our test environment has been down for 4 days and the vendor keeps postponing. Help me log and manage this as an issue with an escalation path."
---

# Manage an Issue

## Purpose
Turn a live problem into a clearly owned, time-bound resolution path with visible impact and escalation rules, so that it is fixed or decided before it quietly damages the project.

## When to use
- A risk has materialized or an unexpected problem is blocking work now.
- An issue has been open too long, keeps bouncing between teams or has no owner.
- A sponsor asks "what exactly is the problem and what are we doing about it?".

## When not to use
- Tracking many risks, assumptions, issues and dependencies together. Use `raid-log`.
- Something that may happen but has not. Use `risk-register`.
- A production incident affecting live users. Use `incident-response`.

## Inputs
Required:
- A description of what is happening and since when.

Optional, improves quality:
- Affected deliverables, milestones or teams; actions already tried.
- Escalation matrix, contract or SLA terms, RAID log IDs.

If the description is missing, ask for it. Ask at most one focused question at a time for anything that blocks the impact assessment.

## Process
1. Write the issue statement as observable facts: what is happening, where, since when, evidence. Keep interpretations separate and mark them `[ASSUMPTION]`.
2. Assess impact on scope, schedule (critical path or not), cost, quality and people; quantify only with given data, otherwise use qualitative levels.
3. Set priority from impact and urgency, and state the "cost of each day of delay" in words or numbers if given.
4. Identify the cause: separate symptom, direct cause and root cause; if unknown, plan a short diagnosis (e.g. five whys with the people involved) instead of guessing.
5. Assign a single accountable owner who has the authority to act; list contributors separately.
6. Define containment (stop the damage now) and resolution actions (fix the cause), each with owner and due date.
7. Define escalation triggers: time without progress, impact threshold or missed action date, and the next escalation level and channel.
8. Define closure criteria that are verifiable (e.g. "environment stable for 3 working days"), not "resolved".
9. Link consequences: raise a change request if the baseline is affected, update RAID entries and record decisions.
10. Track status updates with date, what changed and next check; close with a short closure note and lessons.
11. If the user's goal continues, suggest `escalation-message` to escalate, `change-control` when a baseline must change or `raid-log` to keep it in the wider log.

## Output format
```markdown
# Issue I-<id>: <short title>
| Field | Value |
|---|---|
| Raised by / date | <...> |
| Owner (accountable) | <name/role or [UNKNOWN]> |
| Priority | <Critical/High/Medium/Low> – <reason> |
| Status | Open / In progress / Escalated / Resolved / Closed |
| Linked items | <risk, dependency, CR IDs> |

## Issue Statement (facts)
## Impact
| Dimension | Impact | Evidence |
## Cause
- Symptom / direct cause / root cause (or diagnosis plan)
## Actions
| # | Type (containment/resolution) | Action | Owner | Due | Status |
## Escalation Triggers
- If <condition> by <date> → escalate to <level> via <channel>
## Closure Criteria
## Status History
| Date | Update | Next check |
```

## Quality checklist
- [ ] The statement contains facts and evidence, not blame or solutions.
- [ ] One accountable owner with authority is named or marked `[UNKNOWN]`.
- [ ] Containment and resolution are separated, each with owner and date.
- [ ] Escalation triggers are concrete and time-bound.
- [ ] Closure criteria are verifiable.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Naming a team or "vendor" as owner; nobody acts. Name a person or role with authority.
- Closing on a workaround while the cause remains. Keep a resolution action or log the residual risk.
- Escalating late because escalation feels like failure. Agree triggers upfront so escalation is routine.

## Example
Input: "Test environment down for 4 days; vendor keeps postponing the fix."

Excerpt of output:
- Statement: Integration test environment unavailable since `[date]` (4 working days); 2 vendor fix dates missed.
- Impact: System test blocked; on critical path; each day delays UAT start by one day `[ASSUMPTION: no float]`.
- Containment: run API tests against mocks – Owner QA lead – Due `[date]`.
- Escalation: if not restored by `[date]`, escalate to vendor account manager, then contract owner per SLA.
