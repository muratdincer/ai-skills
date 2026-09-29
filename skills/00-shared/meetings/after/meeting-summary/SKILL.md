---
name: meeting-summary
description: "Produces a short executive summary of a meeting that leads with outcomes, lists decisions, key actions and open points, and flags what needs the reader's attention, readable in under a minute. Use when a manager, sponsor or absent stakeholder needs to know what came out of a meeting without reading full notes or a transcript."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: meetings
  area: after
  title: "Summarize a meeting"
  related: "meeting-notes, meeting-minutes, meeting-follow-up, executive-summary, action-item-extraction"
  prompt: "Summarize this 1-hour architecture review transcript for our CTO in a few lines."
---

# Summarize a Meeting

## Purpose
Tell a busy reader in under a minute what the meeting achieved, what was decided, what happens next and whether anything needs them, so they can act without attending or reading the full record.

## When to use
- A sponsor, manager or absent stakeholder needs the outcome of a meeting.
- Notes or a transcript exist but are too long for the audience.
- A series of meetings needs a consistent short record.

## When not to use
- A complete topic-by-topic record is needed. Use `meeting-notes`.
- A formal record with attendance and resolutions is required. Use `meeting-minutes`.
- The recap will be sent to attendees as a message with next steps. Use `meeting-follow-up`.

## Inputs
Required:
- Meeting notes, transcript or a description of what happened.

Optional:
- Intended reader and what they care about, meeting goal/agenda, prior decisions, preferred length.

If the source is missing, ask for it. If the reader is unknown, write for a senior stakeholder outside the team.

## Process
1. Identify the meeting goal and judge whether it was met: Achieved / Partially / Not achieved. This is the first line.
2. Extract decisions that were explicitly agreed; ignore proposals without agreement.
3. Select at most 5 actions that matter to the reader (owner and date); link or refer to the full list for the rest.
4. List open points and risks that could change a plan, cost, date or scope.
5. Identify what the reader must do: decide, approve, unblock, be aware. If nothing, say "No action needed from you".
6. Write the headline outcome in one sentence using concrete terms (what, by when, with what consequence).
7. Remove discussion history, who-said-what and jargon the reader does not share.
8. Keep facts as stated; mark anything inferred as `[ASSUMPTION]` and anything missing as `[UNKNOWN]`.
9. Check length: aim for 80-150 words, never more than half a page.
10. If the user's goal continues, suggest `meeting-follow-up` to send the recap or `action-item-extraction` when commitments need owners and dates.

## Output format
```markdown
**<Meeting> – <date>: <Achieved / Partially / Not achieved>**
<One-sentence headline outcome.>

**Decisions**
- <decision>

**Next steps**
- <action> — <owner> — <due>

**Open points / risks**
- <item> — <impact>

**Needed from you:** <decision/approval/awareness or "No action needed">
Full notes: <reference or [TBD]>
```

## Quality checklist
- [ ] The first line states whether the goal was met.
- [ ] Only explicitly agreed items are called decisions.
- [ ] Every next step has an owner and date or an `[UNKNOWN]` marker.
- [ ] The reader's required action is explicit.
- [ ] 150 words or fewer, no jargon unknown to the reader.
- [ ] Anything not stated in the input is labeled `[ASSUMPTION]` or listed as an open question, never presented as fact.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Summarizing the discussion instead of the outcome ("we talked about caching"). State what changed.
- Hiding bad news in the open points. If the goal was not achieved, say so in the first line.
- Listing every action item. Pick those the reader cares about and point to the full list.

## Example
Input: Transcript of a 1-hour review of the event-driven redesign of order processing.

Excerpt of output:
**Order processing redesign review – 12 May: Partially achieved**
Target architecture approved; migration approach still open pending a load test.
**Decisions** – Kafka-based event backbone approved for new order flows.
**Needed from you:** Approve 2 extra engineer-weeks for the load test by 16 May.
