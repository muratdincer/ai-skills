---
name: daily-sync-summary
description: "Turns notes or a transcript of a daily team sync (stand-up) into a short summary of progress toward the iteration goal, today's plan, blockers with owners and follow-up conversations, per person and for the team. Use when someone shares stand-up notes, a chat thread of async updates or a meeting transcript and asks for a summary, blocker list or update for absent members."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: agile-delivery
  area: ceremonies
  title: "Summarize a daily sync"
  related: "impediment-tracking, meeting-summary, action-item-extraction, burndown-analysis, iteration-goal"
  prompt: "Summarize today's stand-up from these notes and list the blockers: Emre finished the payment API mock, stuck on test env certificate; Selin reviewing Emre's PR, then starts refund flow..."
---

# Summarize a Daily Sync

## Purpose
Give the team and absent members a two-minute read of where the iteration stands against its goal, what will happen today and which blockers need someone to act, so that the sync results in coordination rather than a status log.

## When to use
- A stand-up happened and notes, a transcript or async written updates need a summary.
- Blockers mentioned in passing must be captured and routed.
- A lead or product owner missed the sync and needs the essentials.

## When not to use
- Tracking blockers over days, escalation and resolution. Use `impediment-tracking`.
- Summarizing a longer meeting with decisions and discussion. Use `meeting-summary` or `meeting-minutes`.
- Reporting status to stakeholders outside the team. Use `status-update`.

## Inputs
Required:
- Notes, transcript or written updates from the sync.

Optional, improves quality:
- Iteration goal and day number (e.g. day 6 of 10).
- Board snapshot or list of in-progress items.
- Blockers still open from previous days.

If the notes are missing, ask for them. Do not ask for optional items; note their absence.

## Process
1. Clean the input: remove small talk and duplicates, keep names as given. If the notes contain personal or health details (e.g. reason for sick leave), omit them and write only "unavailable".
2. Per person, extract: done since last sync, plan for today, blockers or help needed. Keep what was said separate from what you infer; label inferences `[INFERRED]`.
3. Classify each blocker: blocked (cannot progress), impeded (slowed), or risk (may block later). Note who can remove it and whether it has an owner.
4. Relate progress to the iteration goal: on track, at risk or off track, with the one-line reason. If the goal is unknown, say so instead of guessing.
5. Spot coordination signals: two people on the same item, items in progress for many days without movement, work not on the board, pending reviews older than a day.
6. List follow-up conversations ("after the sync") with the participants, so discussion leaves the sync.
7. Carry forward open blockers from previous days if supplied, with age in days.
8. Write the summary in the output format; keep it under about 25 lines.
9. If the user's goal continues, suggest `impediment-tracking` for blockers that need escalation or `burndown-analysis` when the goal is at risk.

## Output format
```markdown
# Daily Sync – <team>, <date> (day <n> of <m>)
**Iteration goal:** <goal or [UNKNOWN]> – **Status:** On track / At risk / Off track – <reason>

## Blockers
| Blocker | Type | Affects | Owner to resolve | Age | Next step |
|---|---|---|---|---|---|

## Per Person
- **<name>** – Done: ... · Today: ... · Needs: ...

## Coordination Signals
- ...

## Follow-up Conversations
- <topic> – <participants>

## Absent / Not Reported
- <name or none>
```

## Quality checklist
- [ ] Every blocker has a type, an affected item and an owner or `[UNKNOWN]` owner.
- [ ] Goal status is given with a reason, or the goal is marked `[UNKNOWN]`.
- [ ] Inferences are labeled; nothing is attributed to a person who did not say it.
- [ ] Personal details beyond availability are omitted.
- [ ] The summary is readable in about two minutes.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Summarizing activity ("worked on X") instead of progress toward the goal. Always tie back to the goal.
- Burying a blocker in a person's line. Lift every blocker into the table so it gets an owner.
- Treating the summary as a performance record. Keep it team-focused; do not rate individuals.

## Example
Input: "Emre finished payment API mock, stuck on test env certificate since yesterday. Selin reviewing Emre's PR then refund flow. Can was sick." Goal: customers can pay by card on staging. Day 6/10.

Excerpt of output:
- Status: At risk – card payment cannot be tested until the test environment certificate is fixed.
- Blocker: Test env certificate expired | Blocked | Payment API | `[UNKNOWN]` (platform team?) | 2 days | Raise with platform today.
- Absent: Can – unavailable.
