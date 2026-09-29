---
description: Assesses whether a planned meeting is actually needed by testing its goal against async alternatives, and recommends meet, shorten, go async or cancel with a ready-to-use alternative. Use when someone plans a new or recurring meeting, asks "do we need a meeting for this?", or wants to cut meeting load.
related: meeting-agenda, meeting-invite, stakeholder-email, status-update, working-agreement
prompt: I want to set up a weekly 1-hour sync with 9 people to share progress on the data migration. Do we really need it?
---

# Decide If a Meeting Is Needed

## Purpose
Protect people's focus time by holding a meeting only when synchronous interaction is the cheapest way to reach the goal, and give a concrete async alternative when it is not.

## When to use
- A new meeting or workshop is being planned.
- A recurring meeting is up for review or people complain about meeting load.
- Someone asks whether an email, document or message would be enough.

## When not to use
- The meeting is already justified and needs structure. Use `meeting-agenda`.
- The team wants to set general meeting norms. Use `working-agreement`.

## Inputs
Required:
- The goal of the meeting (what should be different afterwards).
- Proposed attendees (count or roles) and duration/frequency.

Optional:
- Urgency, level of disagreement, sensitivity of the topic, time zones, what has already been tried async.

If the goal is missing, ask for it: without a goal the answer is always "do not meet yet".

## Process
1. Restate the goal as an outcome: decision, alignment, information sharing, problem solving, relationship/trust, or creative generation.
2. Compute the cost: attendees x duration x frequency in person-hours per month. Show the number.
3. Score the need for synchronous interaction on these signals (Yes/No each):
   - Real disagreement or trade-off that needs live negotiation.
   - High ambiguity; the problem cannot yet be written down.
   - Sensitive or emotional content (bad news, conflict, people topics).
   - Fast iteration between several people is required (design, incident).
   - Relationship building or onboarding is the explicit goal.
   - An async attempt has already failed.
4. Check disqualifiers: no clear goal, no decision maker invited, pure one-way status sharing, fewer than half the attendees contribute.
5. Decide: Meet / Meet but shorter or smaller / Go async / Cancel. Two or more sync signals and no disqualifier usually justify a meeting.
6. If meeting: propose the minimum attendee list (decision makers and contributors; others get the summary) and the shortest realistic duration.
7. If async: pick the format (written update, decision document with comment deadline, recorded walkthrough, chat thread, poll) and draft it.
8. For recurring meetings, propose a review date and a success signal to keep it.
9. Write the recommendation with the reasoning so the organizer can defend it.
10. If the user's goal continues, suggest `meeting-agenda` and `meeting-invite` when a meeting is recommended, or `stakeholder-email` / `status-update` for the async alternative.

## Output format
```markdown
# Meeting Necessity: <topic>
Goal type: <decision/alignment/info/problem solving/relationship/creative>
Cost: <n> people x <duration> x <frequency> = <person-hours/month>

| Signal | Yes/No | Note |
|---|---|---|
| Live disagreement / trade-off | | |
| High ambiguity | | |
| Sensitive content | | |
| Fast multi-person iteration | | |
| Relationship goal | | |
| Async already failed | | |

Disqualifiers: <none / list>
Recommendation: <Meet / Shorter-smaller / Async / Cancel>
Why: <2-3 sentences>

## Alternative (if async)
Format: <...>  Owner: <...>  Response deadline: <date or [TBD]>
<draft message or document skeleton>

## If meeting
Attendees (required): ...  Informed only: ...  Duration: ...  Review on: ...
```

## Quality checklist
- [ ] The goal is an outcome, not a topic.
- [ ] Cost in person-hours is shown.
- [ ] The recommendation follows from the signals, not from habit.
- [ ] An async recommendation includes a ready draft and a response deadline.
- [ ] A meeting recommendation trims attendees and duration.
- [ ] Anything not stated in the input is labeled `[ASSUMPTION]` or listed as an open question, never presented as fact.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Replacing a meeting with an async message that has no deadline or owner; nothing happens. Always set both.
- Pushing sensitive topics (re-orgs, performance, conflict) to text to save time. Those need live conversation.
- Keeping recurring meetings forever. Attach a review date and an explicit exit criterion.

## Example
Input: Weekly 1-hour sync, 9 people, to share data migration progress.

Excerpt of output:
- Cost: 9 x 1 h x 4.3 = ~39 person-hours/month.
- Signals: only "fast iteration" partly applies; goal is one-way status.
- Recommendation: Async. Weekly written update every Thursday using `status-update`, plus a 20-minute call with 3 leads only when the status is Amber or Red.
