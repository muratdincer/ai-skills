---
name: status-update
description: "Writes a concise status update with an overall RAG rating, progress against plan, risks and issues, decisions or help needed, and next steps. Use when someone must report progress on a project, workstream, initiative or incident to a manager, sponsor, steering group or team channel, or asks for a \"weekly update\", \"status report\" or \"where are we\"."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: communication
  area: written
  title: "Write a status update"
  related: "project-status-report, executive-summary, escalation-message, raid-log, steering-committee-pack"
  prompt: "Write this week's status update for the data platform migration: 3 of 5 domains moved, the finance domain is blocked on a firewall change, go-live still planned for the 30th."
---

# Write a Status Update

## Purpose
Tell readers in under a minute whether the work is on track, what changed since the last update and what they need to do, so problems surface early and decisions are not delayed by vague reporting.

## When to use
- Recurring (weekly, per iteration) updates to a sponsor, manager or steering group.
- An ad-hoc "where are we?" request on a project, workstream or migration.
- A team channel post summarizing progress for a broad audience.

## When not to use
- A full formal project report with budget, schedule baselines and RAID detail. Use `project-status-report`.
- The situation needs a decision from someone higher up now. Use `escalation-message`.
- A live incident. Use `incident-communication`.

## Inputs
Required:
- What the work is and its goal or milestone.
- Progress facts since the last update (done, in progress, blocked).

Optional:
- Plan/baseline (dates, scope, budget), previous update, RAG criteria used by the organization, risks and issues, audience.

If progress facts are missing, ask for them in one short batch. Never infer the RAG rating from tone alone; if the plan is unknown, mark the rating `[ASSUMPTION]` and say what it is based on.

## Process
1. Identify the audience and what they decide or control; this sets the level of detail and the ask.
2. Establish the baseline: milestone, target date, scope. If none is given, state "no baseline provided" instead of implying one.
3. Rate overall status with explicit criteria: Green = on track, no help needed; Amber = at risk, recoverable with the stated action; Red = target will be missed without a decision or help. Use the organization's criteria if supplied.
4. Write the headline in one sentence: RAG, the single most important fact, and the ask if any.
5. List progress as outcomes achieved, not activities ("3 of 5 domains live" not "worked on migration"), with numbers where supplied.
6. Report what changed since the last update, including RAG changes with the reason ("Amber → Red because...").
7. List the top risks and issues (maximum 3-5) each with impact, owner and mitigation; move the rest to `raid-log`.
8. State decisions or help needed with the person, the exact ask and the needed-by date.
9. List next steps for the coming period with owners.
10. Separate facts supplied by the user from your inferences; label inferences `[ASSUMPTION]` and list gaps as open questions.
11. Trim to what fits on one screen; move detail to links or an appendix.
12. If the user's goal continues, suggest `escalation-message` when a Red item needs a decision, or `executive-summary` for a senior condensed version.

## Output format
```markdown
**<Work name> – Status <date or period>**  Overall: <Green/Amber/Red> (<previous RAG>)
**Headline:** <one sentence: state + key fact + ask>

**Progress since last update**
- <outcome, with number>

**Changes / RAG movement**
- <what changed and why>

**Risks & issues**
| Item | Impact | Owner | Mitigation / next action |
|---|---|---|---|

**Decisions / help needed**
- <who>: <exact ask> by <date>

**Next steps**
- <action> – <owner> – <date>

**Assumptions / open questions**
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] The RAG rating follows stated criteria and matches the content (no "Green with a blocker").
- [ ] The headline alone tells a busy reader the state and the ask.
- [ ] Progress is expressed as outcomes, with numbers where available.
- [ ] Every risk, issue and ask has an owner; every ask has a needed-by date or `[TBD]`.
- [ ] No invented dates, percentages or names; inferences are labeled.
- [ ] Fits on one screen.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Watermelon status: green outside, red inside. If a milestone is at risk, say Amber now; late Red erodes trust more than early Amber.
- Activity lists ("meetings held, analysis ongoing") that give no signal. Report outcomes and deltas.
- Burying the ask at the end. Put it in the headline if the reader must act.

## Example
Input: "3 of 5 domains migrated, finance blocked on firewall change, go-live 30th."

Weak: "Good progress this week. We migrated some domains and are working on the rest. Some network issues. Go-live on track."

Strong (excerpt):
**Data Platform Migration – Status week 38**  Overall: Amber (was Green)
**Headline:** 3 of 5 domains live; go-live on the 30th is at risk unless the finance firewall change is approved by `[TBD – date needed from network team]`.
**Help needed:** Network lead: approve change for finance DB ports by `[TBD]`.
