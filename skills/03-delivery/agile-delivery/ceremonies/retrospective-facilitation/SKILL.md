---
name: retrospective-facilitation
description: "Plans and runs a team retrospective end to end: sets the stage, gathers data, generates insights, converges with note-and-vote and produces a small number of owned, verifiable improvement actions, and follows up on previous actions. Use when a retrospective is due, when someone shares retro board notes and wants actions, or when past retros produced actions that never happened."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: agile-delivery
  area: ceremonies
  title: "Facilitate a retrospective"
  related: "retrospective-format, team-health-check, working-agreement, five-whys, impediment-tracking"
  prompt: "Run our sprint retro: remote team of 7, 60 minutes. Last sprint had two production incidents and a lot of context switching. Last retro's actions: pair on reviews (not done), fix flaky tests (done)."
---

# Facilitate a Retrospective

## Purpose
Help the team inspect how it worked and leave with one to three improvement actions it will actually carry out, in a session that is safe, focused and time-boxed.

## When to use
- A regular iteration or milestone retrospective is due.
- Raw retro board notes exist and need clustering, prioritization and actions.
- Retro actions keep being forgotten and the loop needs to be closed.

## When not to use
- Designing a new or themed format only. Use `retrospective-format`.
- A project-end review for an organization-wide audience. Use `lessons-learned`.
- A blameless analysis of a specific incident. Use `postmortem`.

## Inputs
Required:
- Context: team size, remote/on-site, time available, and the period being reviewed.

Optional, improves quality:
- Notable events of the period (incidents, releases, team changes, metrics).
- Previous retro actions and their status.
- Raw notes if the retro already ran.
- Team health or mood signals.

If the context is missing, ask up to 3 questions. If raw notes are supplied, skip the planning steps that already happened.

## Process
1. Review previous actions first: done, partly done, dropped. For dropped ones, ask why; do not silently re-add them.
2. Choose a structure with five phases: set the stage, gather data, generate insights, decide what to do, close. Allocate time (e.g. 5/15/15/15/10 for 60 minutes). If a special format is needed, pick one from `retrospective-format`.
3. Set the stage: state the focus and remind the team of the prime directive or equivalent safety statement; plan a quick check-in (one word, a 1-5 scale). For remote teams, plan anonymous input.
4. Gather data: silent writing first (5-7 minutes), then read-out; add a timeline of the period's events so discussion rests on facts, not memory.
5. Generate insights: cluster notes, name each cluster, then dot-vote (3 votes per person) to pick the top 1-2 clusters. For the top cluster, dig into causes with 5 whys or a quick fishbone in small breakouts of 2-3 people for larger teams.
6. Decide actions: at most three, each specific, owned by a named person, with a due date or next iteration and a way to verify it happened. Prefer experiments ("for the next two iterations we will...") over permanent rules.
7. Separate actions the team controls from issues outside its control; the latter become escalations with an owner.
8. Close: return-on-time-invested vote or one-sentence appreciation; confirm where actions will be tracked (the backlog or board).
9. Write the record; anonymize individual quotes, avoid names in problem statements.
10. If the user's goal continues, suggest `working-agreement` when actions change team norms, `team-health-check` for broader trends, or `impediment-tracking` for escalations.

## Output format
```markdown
# Retrospective – <team>, <period>, <date>
Format: <name> · Time: <min> · Participants: <n>

## Previous Actions
| Action | Status | Note |
|---|---|---|

## Agenda
| Phase | Activity | Minutes |
|---|---|---|

## Data and Insights
- Timeline highlights: ...
- Top clusters (votes): <cluster> (<n>), <cluster> (<n>)
- Root cause of top cluster: ... [INFERRED where not stated by the team]

## Actions
| # | Action (experiment) | Owner | Due | How we verify |
|---|---|---|---|---|

## Escalations (outside team control)
- <issue> – <escalated to> – <owner>

## Check-out
- ...
```

## Quality checklist
- [ ] Previous actions were reviewed before new data was gathered.
- [ ] At most three new actions, each with an owner, due date and verification.
- [ ] Actions address the top-voted clusters, not the loudest opinion.
- [ ] Issues outside team control are escalations, not team actions.
- [ ] The record contains no blame or attributable personal quotes.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Ending with ten vague actions ("communicate better"). Pick few, make them concrete and verifiable.
- Jumping to solutions during data gathering. Keep phases separate; convergence happens after clustering and voting.
- Running the same format every time. Rotate formats when energy drops, see `retrospective-format`.
- Letting the manager dominate. Use silent writing and anonymous input so every voice is heard.

## Example
Input: "Remote team of 7, 60 min. Two production incidents, lots of context switching. Previous actions: pair on reviews (not done), fix flaky tests (done)."

Excerpt of output:
- Previous: "Pair on reviews" – not done – team says no slot was reserved; discuss, do not auto re-add.
- Weak action: "Reduce context switching."
- Strong action: "For the next 2 iterations, one rotating person handles all support requests; others ignore the support channel until 15:00. Owner: Deniz. Verify: count of interrupts logged per person in the next retro."
