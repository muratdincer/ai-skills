---
name: meeting-invite
description: "Drafts a clear meeting invitation stating purpose, expected outcome, agenda summary, attendees with the reason each is invited, and required preparation. Use when sending a calendar invite or meeting request email so recipients can decide to attend and come prepared."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: meetings
  area: before
  title: "Write a meeting invitation"
  related: "meeting-agenda, meeting-necessity-check"
  prompt: "Write a meeting invite for a 45-minute architecture review of the payment service redesign next Tuesday."
---

# Write a Meeting Invitation

## Purpose
Let recipients understand in 10 seconds why the meeting exists, why they are invited and what they must prepare, so attendance and preparation improve.

## When to use
- Sending a calendar invite or meeting request email.
- Re-sending an invite after the scope or agenda has changed.

## When not to use
- The agenda itself has not been designed yet. Use `meeting-agenda` first.

## Inputs
Required:
- Meeting topic and objective.
- Date, time, duration, location or link.

Optional:
- Agenda, attendee list with roles, pre-reads, decisions needed.

## Process
1. Write a subject line in the form `<Type>: <topic> – <outcome>` (e.g. "Decision: Payment redesign – approve target architecture").
2. Open with one sentence stating the purpose and the expected outcome.
3. Add a 3-5 bullet agenda summary.
4. State what each attendee should prepare, with links. Keep it specific ("read section 3", "bring the cost estimate").
5. Separate required and optional attendees; add one line on why key people are invited if it is not obvious.
6. Add logistics: time zone, link, dial-in, room.
7. Add a line for those who cannot attend: how to send input or who to delegate to.
8. Keep the whole invite under ~150 words.
9. If the user's goal continues and no timeboxed agenda exists yet, suggest `meeting-agenda`; if attendees may question the need for the meeting, suggest `meeting-necessity-check`.

## Output format
```markdown
Subject: <Type>: <topic> – <outcome>

Purpose: <one sentence>. By the end we will have <outcome>.

Agenda
- <item> (<minutes>)
- ...

Please prepare
- <person/everyone>: <specific action> <link>

Required: <names>   Optional: <names>
When/Where: <date, time, time zone, link/room>
Can't attend? <how to give input or delegate>
```

## Quality checklist
- [ ] Subject shows the type and outcome.
- [ ] Purpose fits in one sentence.
- [ ] Preparation is specific and linked.
- [ ] Required vs optional attendees are separated.
- [ ] Under ~150 words.
- [ ] Anything not stated in the input is labeled `[ASSUMPTION]` or listed as an open question, never presented as fact.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Invites that only contain the title; recipients cannot judge relevance.
- "Please review the attached" without saying what to look for.
- Forgetting the time zone for distributed teams.

## Example
Subject: Decision: Payment service redesign – approve target architecture
Purpose: Review the proposed architecture and decide whether to proceed to the PoC. By the end we will have a go/no-go and a list of open risks.
