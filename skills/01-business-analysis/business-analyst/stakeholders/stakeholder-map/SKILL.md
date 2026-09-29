---
name: stakeholder-map
description: "Places stakeholders on a power/interest grid with evidence for each rating, adds current vs desired attitude, and defines an engagement strategy, channel and frequency per quadrant and per key person. Use after stakeholders are identified, before planning communication or when support for an initiative is uncertain; triggers include 'power interest grid', 'who do we manage closely?'."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: stakeholders
  title: "Map stakeholders by power/interest"
  related: "stakeholder-identification, raci-matrix, communication-plan, stakeholder-register, conflict-resolution"
  prompt: "Map these 9 stakeholders on a power/interest grid and tell me how to engage each for the CRM migration."
---

# Map Stakeholders by Power/Interest

## Purpose
Decide where to spend engagement effort by making each stakeholder's power, interest and attitude explicit, and turning that into a concrete engagement plan.

## When to use
- A stakeholder list exists and engagement effort must be prioritized.
- An initiative faces resistance or unclear support.
- Before a communication plan or a steering setup is defined.

## When not to use
- The stakeholder list does not exist yet. Use `stakeholder-identification` first.
- Tasks must be assigned to people. Use `raci-matrix`.
- A full communication calendar is needed. Use `communication-plan`.

## Inputs
Required:
- The stakeholder list with roles (names optional).
- The initiative in one or two sentences.

Optional, improves quality:
- Known attitudes, past conflicts, reporting lines, budget authority.
- Decisions coming up that need specific approvals.

If the stakeholder list is missing, ask for it or offer to run `stakeholder-identification` first.

## Process
1. Define power for this initiative: formal authority (budget, approval, veto) plus informal influence (expertise, network, control of resources or data).
2. Define interest: how much the outcome changes their work, goals or risk.
3. Rate each stakeholder High/Low on both axes and write the evidence in one clause. Mark guesses as `[ASSUMPTION]`.
4. Record current attitude (champion, supporter, neutral, sceptic, blocker, unknown) and the desired attitude by a named milestone. Attitude based on hearsay rather than direct evidence is `[ASSUMPTION]`.
5. Place them in quadrants: Manage closely (high/high), Keep satisfied (high power, low interest), Keep informed (low power, high interest), Monitor (low/low).
6. For each quadrant define strategy, channel and frequency; for each high-power stakeholder add a personal action (what message, by whom, by when).
7. Identify gaps: high-power sceptics without an owner, champions not leveraged, stakeholders with unknown attitude.
8. Note that positions move; set a review trigger (phase change, key decision, reorganization).
9. If the goal continues, suggest `communication-plan` to schedule the engagement actions or `raci-matrix` to formalize decision ownership.

## Output format
```markdown
# Stakeholder Map: <initiative>

| Stakeholder | Power (H/L) – evidence | Interest (H/L) – evidence | Attitude now → target | Quadrant |
|---|---|---|---|---|

## Grid
- Manage closely: ...
- Keep satisfied: ...
- Keep informed: ...
- Monitor: ...

## Engagement strategy
| Quadrant / person | Objective | Message | Channel | Frequency | Owner |
|---|---|---|---|---|---|

## Risks and gaps
- ...
Review trigger: <event>
```

## Quality checklist
- [ ] Every rating has a one-clause justification or is marked `[ASSUMPTION]`.
- [ ] Attitude is recorded separately from power and interest.
- [ ] Every high-power stakeholder has a named owner and action.
- [ ] Blockers and sceptics have a specific engagement action, not just "inform".
- [ ] The map is free of judgmental language about individuals.
- [ ] A review trigger is defined.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Equating hierarchy with power. A system owner or a senior specialist can block more than a director.
- Putting everyone in "manage closely". If more than a third of the list is there, re-check the ratings.
- Sharing the raw map widely. Attitude notes are sensitive; keep the working version with the core team.

## Example
Input: "CRM migration; stakeholders include Sales Director, call-center agents, IT security, DPO, marketing analysts."

Excerpt of output:
| Stakeholder | Power | Interest | Attitude now → target | Quadrant |
|---|---|---|---|---|
| Sales Director | H – budget owner | H – pipeline visibility | Supporter → Champion by kickoff | Manage closely |
| DPO | H – can stop data transfer | L – limited to data protection | Unknown → Neutral before migration design | Keep satisfied |
| Call-center agents | L | H – daily tool changes | Sceptic → Neutral by UAT | Keep informed |
