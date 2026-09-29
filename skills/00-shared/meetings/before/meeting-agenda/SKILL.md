---
name: meeting-agenda
description: "Builds a timeboxed meeting agenda with a clear objective, expected outcomes, agenda items with owners and durations, and required pre-reads. Use when planning any meeting, workshop or recurring session and you need a structured agenda that drives decisions instead of discussion."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: meetings
  area: before
  title: "Prepare a meeting agenda"
  related: "meeting-invite, meeting-necessity-check, facilitation-guide"
  prompt: "Prepare a 60-minute agenda for a meeting to decide the Q3 release scope with product, engineering and QA leads."
---

# Prepare a Meeting Agenda

## Purpose
Give every meeting a single objective, concrete outcomes and a realistic time plan so that participants arrive prepared and the meeting ends with decisions, not just talk.

## When to use
- Planning a new meeting, workshop, review or steering session.
- A recurring meeting has become unfocused and needs a reset.

## When not to use
- You are unsure the meeting is needed. Use `meeting-necessity-check` first.
- You need a detailed facilitator script. Use `facilitation-guide`.

## Inputs
Required:
- Meeting topic or goal.
- Duration.

Optional:
- Participants and their roles.
- Background material, previous meeting notes, open issues.
- Decisions that must be made.

## Process
1. State the objective in one sentence starting with a verb: decide, align, review, plan, inform, solve.
2. Define 1-3 expected outcomes (for example "approved scope list", "owner per risk").
3. List topics that serve the objective. Remove anything that does not.
4. Phrase each agenda item as a question or outcome, not a noun ("Which 5 features go into Q3?" instead of "Q3 features").
5. Assign an owner and a type to each item: Inform, Discuss, Decide.
6. Allocate time. Put decision items early while energy is high. Reserve 10% buffer and the last 5 minutes for wrap-up (decisions, actions, next steps).
7. Check the total against the duration. If it overflows, cut or move items to async.
8. List pre-reads and what participants must prepare.
9. Name the roles: facilitator, note taker, timekeeper.
10. If the user's goal continues, suggest `meeting-invite` to send the agenda or `facilitation-guide` when the session needs a run script.

## Output format
```markdown
# <Meeting title>
**Objective:** <one sentence>
**Expected outcomes:** <1-3 bullets>
**Date / Duration:** <...>  **Facilitator:** <...>  **Note taker:** <...>
**Participants:** <name – role>

| # | Time | Item (question/outcome) | Type | Owner |
|---|---|---|---|---|
| 1 | 00:00-00:05 | Objective and context | Inform | ... |
| ... | | | | |
| n | last 5 min | Wrap-up: decisions, actions, next steps | Decide | Facilitator |

**Pre-reads / preparation:** <links, what to bring>
**Parking lot:** topics raised but out of scope go here
```

## Quality checklist
- [ ] The objective is a single sentence with an action verb.
- [ ] Every item has a type, owner and duration.
- [ ] Total time is within the meeting duration including buffer.
- [ ] Decision items are explicit and placed early.
- [ ] Wrap-up is reserved at the end.
- [ ] Anything not stated in the input is labeled `[ASSUMPTION]` or listed as an open question, never presented as fact.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Agendas that are only a list of nouns; nobody knows what "done" looks like for an item.
- Too many items for the time available.
- Inviting people who are needed for only one item for the whole meeting. Suggest a timed slot instead.

## Example
Objective: Decide the Q3 release scope.
Item 2 (00:05-00:25, Decide, Product Lead): "Which of the 8 candidate features fit the Q3 capacity?"
