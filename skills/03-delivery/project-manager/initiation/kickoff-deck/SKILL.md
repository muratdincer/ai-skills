---
name: kickoff-deck
description: "Prepares a project kickoff session, producing a timeboxed agenda and slide-by-slide content covering objectives, scope, team and roles, plan and milestones, ways of working, risks and immediate next steps for the team and sponsors. Use when a project is about to start or a new phase or major team change needs a shared start."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: project-manager
  area: initiation
  title: "Prepare a kickoff"
  related: "project-charter, scope-statement, stakeholder-register, communication-plan, meeting-agenda"
  prompt: "Prepare the kickoff for our data warehouse modernization project: 20 people, sponsor attends the first 30 minutes."
---

# Prepare a Kickoff

## Purpose
Align sponsors and the delivery team on why the project exists, what success looks like, who does what and how the team will work, so that the first weeks are spent executing rather than clarifying.

## When to use
- A charter is approved and the team is being assembled.
- A new phase starts with a changed team, vendor or scope.
- A troubled project is being restarted and needs a reset.

## When not to use
- The project is not yet authorized. Use `project-charter`.
- Only a routine team meeting is needed. Use `meeting-agenda`.
- A client-facing discovery session with open requirements. Use `discovery-workshop`.

## Inputs
Required:
- Charter or equivalent summary (objectives, scope, sponsor).
- Audience: who attends and the available duration.

Optional, improves quality:
- Draft plan, milestones, team roster, RACI, tools and cadences.
- Known risks, sensitive topics, sponsor expectations.

If the charter summary or the audience/duration is missing, ask for it.

## Process
1. Define 3 kickoff outcomes (e.g. shared understanding of goals, agreed roles, first 2 weeks planned).
2. Split the agenda by audience: sponsor segment first (why, success, expectations), team segment after (how).
3. Timebox each item and assign a presenter; keep at least 20% for questions and interaction.
4. Draft slide content: context and why now, objectives and success measures, scope in/out, deliverables and milestones, organization and RACI, governance and cadences, ways of working (tools, definitions, decision process), top risks and dependencies, next steps.
5. Mark every date, name and number that is not given as `[TBD]`.
6. Add an interactive element: risk brainstorm, assumptions check or expectations round.
7. Prepare a pre-read list and a follow-up message with decisions and actions.
8. List questions the PM must resolve before the session.
9. Label every inferred element `[ASSUMPTION]` and move it to assumptions or open questions. If the user's goal continues, suggest the next skill: `communication-plan` to turn the agreed cadence into a plan, or `stakeholder-register` if sponsors or key users are still unmapped.

## Output format
```markdown
# Kickoff: <project>
Date <date> | Duration <x min> | Audience <groups>
## Kickoff Outcomes
1. ...
## Agenda
| Time | Item | Presenter | Audience | Outcome |
## Slide Outline
1. Why this project, why now – <key message>
2. Objectives and success measures – ...
3. Scope in / out – ...
4. Milestones – ...
5. Team, roles and RACI – ...
6. Governance and cadences – ...
7. Ways of working – ...
8. Top risks and dependencies – ...
9. Next 2 weeks – ...
## Interactive Segment
## Pre-reads
## Open Points Before Kickoff
```

## Quality checklist
- [ ] Each slide has one key message, not a topic label.
- [ ] Sponsor time is used for why and expectations, not for tooling details.
- [ ] At least 20% of time is interactive or Q&A.
- [ ] Roles and decision rights are explicit.
- [ ] Next steps have owners and dates or `[TBD]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- A one-way presentation marathon. Build in structured interaction.
- Presenting a detailed plan as final before the team has validated it. Label it as a draft.
- Skipping ways of working; most early friction comes from unclear decision and communication rules.

## Example
Input: "DWH modernization kickoff, 20 people, 2 hours, sponsor for first 30 minutes."

Excerpt of output:
| 0:00-0:10 | Why now: licence end and reporting delays | Sponsor | All | Shared urgency |
| 0:40-1:10 | Risk and assumptions brainstorm | PM | Team | Initial RAID entries |
- Open point: Is the vendor team attending, and under which contract role?
