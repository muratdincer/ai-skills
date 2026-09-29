---
name: workshop-plan
description: "Designs a requirements workshop: objectives, participants and roles, pre-work, a timed agenda of elicitation activities (e.g., process walk-through, story mapping, rules/exceptions round, prioritization), materials, decision rules and expected outputs, for on-site or remote formats. Use when several stakeholders must align or co-create requirements, or when asked 'plan a workshop for...'."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: elicitation
  title: "Plan a requirements workshop"
  related: "facilitation-guide, meeting-agenda, interview-question-set, story-mapping, discovery-workshop"
  prompt: "Plan a half-day remote workshop with finance, sales ops and IT to define the requirements for automated credit limit checks."
---

# Plan a Requirements Workshop

## Purpose
Design a workshop that produces agreed, usable requirements artifacts in limited time, instead of an open discussion that ends with "let's follow up".

## When to use
- Several stakeholder groups must agree on scope, flows, rules or priorities.
- Interviews revealed conflicts that need to be resolved together.
- A discovery or analysis phase needs a fast, shared starting point.

## When not to use
- You need a live facilitation script with prompts and conflict handling for an already planned session. Use `facilitation-guide`.
- Only one or two people need to be heard. Use `interview-question-set`.
- It is a client-facing, multi-day discovery engagement. Use `discovery-workshop`.

## Inputs
Required:
- The topic and the decision or output the workshop must produce.
- Participants or participant groups.

Optional, improves quality:
- Duration, format (on-site/remote/hybrid), known conflicts, prior findings, constraints on participants' time.

If the expected output is missing, ask: a workshop without a defined output is a meeting.

## Process
1. Write 1-3 workshop objectives as outputs ("agreed to-be flow for X", "prioritized list of rules for Y").
2. Choose participants for coverage and decision power; keep active participants to about 5-10; define roles: facilitator, scribe, decision owner, timekeeper, subject experts.
3. Select activities that produce the outputs, e.g.: problem framing, as-is walk-through, to-be flow sketch, story mapping, rules and exceptions round, data/report needs round, NFR quick scan, prioritization (dot voting, MoSCoW), risks and open questions.
4. Timebox each activity with buffer; place the hardest decisions when energy is highest; add breaks every 60-90 minutes.
5. Define pre-work (reading, sample data, current forms) and send it with the invitation.
6. State decision rules up front: who decides if there is no consensus, what goes to a parking lot.
7. Prepare materials: templates for each activity, board layout (physical or digital), example artifacts.
8. For remote formats, plan shorter blocks, explicit turn-taking, breakout rooms and a single shared board.
9. Plan divergence and convergence explicitly: breakout groups of 3-5 people with one task, one template and a timebox, each reporting back in 2-3 minutes; converge with note-and-vote (silent individual notes for 3-5 minutes, read-out without debate, dot vote with a fixed number of dots each, the decision owner confirms or overrides with a stated reason).
10. Define the outputs, owner and deadline for the post-workshop write-up and follow-ups. Anything you assume about participants or availability is marked `[ASSUMPTION]`.
11. If the goal continues, suggest `facilitation-guide` for the facilitator script or `meeting-agenda` for the invitation agenda.

## Output format
```markdown
# Workshop Plan: <topic>
Date/format: <...> · Duration: <...> · Decision owner: <role>

## Objectives (outputs)
1. ...

## Participants and roles
| Name/role | Why needed | Workshop role |

## Pre-work
- ...

## Agenda
| Time | Activity | Purpose / output | Method | Lead |
|---|---|---|---|---|

## Decision rules and parking lot
- ...

## Materials and board layout
- ...

## After the workshop
- Write-up by <owner> within <time>; open items tracked in <place>
```

## Quality checklist
- [ ] Every objective is an output that can be checked at the end.
- [ ] Every agenda item maps to an objective.
- [ ] The decision owner is present or the decision rule is explicit.
- [ ] Timeboxes include buffer and breaks.
- [ ] Pre-work and materials are defined.
- [ ] The remote/hybrid format is reflected in methods, not just in the invite.
- [ ] Every divergent activity has a matching convergence mechanic (e.g., note-and-vote) and a decision owner.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Inviting too many people. Split into sessions or use a sounding group for the rest.
- Starting with solution design before the problem and scope are agreed.
- No follow-up owner. Outputs decay within days if not written up and circulated.

## Example
Input: "Half-day remote workshop: finance, sales ops, IT; automated credit limit checks."

Excerpt of output:
| Time | Activity | Purpose / output | Method | Lead |
|---|---|---|---|---|
| 0:00-0:15 | Framing | Shared problem statement and scope | Draft statement review | BA |
| 0:15-1:00 | As-is walk-through | Current credit check steps and pains | Swimlane on shared board | Sales ops |
| 1:10-2:00 | Rules and exceptions | Credit limit rules, overrides, approvers | Rule table, one row per rule | Finance |
