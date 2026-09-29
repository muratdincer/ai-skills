---
name: on-call-handover
description: "Writes an on-call handover for the incoming engineer from the outgoing shift's notes, alerts, incidents and change calendar: open incidents and their state, recent and upcoming changes, known risks and degraded components, noisy or silenced alerts, pending follow-ups with owners, and explicit watch items with thresholds and first actions. Use at the end of an on-call shift or rotation, before a holiday or freeze period, or whenever responsibility for a production system passes between people or teams."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: sre
  area: incident
  title: "Write an on-call handover"
  related: "incident-response, runbook, postmortem, alert-design, incident-communication"
  prompt: "My on-call week ends tomorrow. Here are my notes, the alert summary and the change calendar. Write the handover for the next on-call engineer."
---

# Write an On-Call Handover

## Purpose
Transfer operational awareness so the incoming on-call engineer knows, within minutes, what is broken, what is fragile, what is about to change and what to do if a watched signal fires. A good handover prevents rediscovering known issues at 3 a.m.

## When to use
- An on-call shift or rotation ends and responsibility passes to the next person.
- Before holidays, change freezes or large launches when context must be explicit.
- Responsibility for a service moves between teams or time zones (follow-the-sun).

## When not to use
- An incident is in progress and needs coordination. Use `incident-response`.
- A completed incident needs a formal review. Use `postmortem`.
- Recurring procedures need to be documented. Use `runbook`.

## Inputs
Required:
- The outgoing shift's material: notes, incidents and alerts during the shift, or a free-text account.

Optional, improves quality:
- Change and release calendar for the coming shift, maintenance windows, silenced alerts list.
- Open tickets and follow-ups, SLO and error budget status, escalation contacts.

If no shift material is provided, ask for it. Do not fill sections with generic content; empty sections are stated as "none reported".

## Process
1. Set the header: service scope, shift period with time zone, outgoing and incoming roles, overall status (Green/Amber/Red) with a one-line reason.
2. List open incidents and problems: current state, impact, mitigation in place, next step, owner, and links to channel or ticket. Mark anything unresolved as still open, not "probably fine".
3. List degraded or fragile components: known issues with workarounds, manual interventions done (restarts, scaled replicas, feature flags toggled, temporary config) that must be reverted or watched.
4. Summarize alert hygiene: noisy alerts and their known cause, silenced or muted alerts with expiry time, alerts that should have fired but did not.
5. List recent changes (last shift) and upcoming changes (next shift): deploys, migrations, certificate or credential expiries, maintenance windows, third-party events, traffic events.
6. Define watch items: the signal, threshold, why it matters and the first action or runbook to use if it fires.
7. List pending follow-ups with owner and due date, including action items from postmortems that affect operations.
8. Record SLO and error budget status if available, and any escalation or contact changes.
9. Keep it scannable: most urgent first, one line per item, links instead of pasted logs; mask credentials and personal data.
10. Mark every inferred status `[ASSUMPTION]` and anything unknown `[UNKNOWN]`; propose a short live handover call if status is Amber or Red. If the goal continues, suggest `runbook` for undocumented manual fixes, `alert-design` for noisy alerts, or `postmortem` for incidents that need review.

## Output format
```markdown
# On-Call Handover: <service/team> · <period, time zone>
Outgoing: <role/name> → Incoming: <role/name> · Overall status: Green/Amber/Red – <reason>

## Open Incidents and Problems
| Item | State | Impact | Mitigation in place | Next step | Owner | Link |
|---|---|---|---|---|---|---|

## Degraded Components and Manual Interventions
| Component | Issue / intervention | Revert or watch until | Workaround |
|---|---|---|---|

## Alerts
- Noisy: ...
- Silenced (until): ...
- Missed / gaps: ...

## Changes
| When | Change | Risk | Contact |
|---|---|---|---|

## Watch Items
| Signal | Threshold | Why | First action / runbook |
|---|---|---|---|

## Pending Follow-ups
| Item | Owner | Due |
|---|---|---|

## SLO / Error Budget and Escalation Notes
```

## Quality checklist
- [ ] Every open incident has a state, next step and owner; none is dropped because it is quiet.
- [ ] Temporary manual interventions and silenced alerts have a revert or expiry time.
- [ ] Each watch item has a threshold and a first action.
- [ ] Upcoming changes, expiries and maintenance windows for the next shift are listed or stated as none.
- [ ] Nothing is invented; unknown statuses are `[UNKNOWN]`, and no secrets or personal data appear.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Handover as a narrative diary. The incoming engineer needs a prioritized list, not the story of the week.
- Forgetting temporary fixes: a scaled-up replica set or a muted alert silently becomes the new normal.
- Omitting expiries (certificates, credentials, silences) that fall inside the next shift.

## Example
Input: "Checkout latency spike Tue, mitigated by adding 2 pods, root cause unknown. Muted disk alert on log node until Friday. DB minor upgrade Thursday 02:00."

Excerpt of output:
- Overall status: Amber – checkout latency cause still unknown; temporary scale-up in place.
| Component | Issue / intervention | Revert or watch until | Workaround |
|---|---|---|---|
| checkout | Scaled from 4 to 6 pods after latency spike | Keep until root cause found `[ASSUMPTION]` | Scale further if p95 > SLO |
| Signal | Threshold | Why | First action / runbook |
|---|---|---|---|
| checkout p95 latency | > SLO for 10 min | Unexplained spike recurred? | Check DB waits, follow checkout runbook |
| Log node disk alert | Mute expires Friday | Alert is muted, disk may fill | Verify disk usage before expiry |
