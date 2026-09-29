---
description: Writes the post-meeting follow-up message to attendees and stakeholders with a thank-you line, outcome, decisions, action items with owners and dates, open questions, next meeting and a correction deadline. Use right after a meeting when a recap email or chat message must be sent so everyone leaves with the same understanding and commitments.
related: meeting-summary, action-item-extraction, meeting-notes, stakeholder-email, open-questions-tracker
prompt: Write a follow-up email to the attendees of today's kickoff with the vendor based on these notes.
---

# Write a Meeting Follow-Up Message

## Purpose
Lock in the shared understanding of a meeting within hours by sending a short recap that confirms decisions and commitments and invites corrections before they become the record.

## When to use
- Immediately after a meeting with decisions or commitments, especially cross-team or external.
- When attendance was partial and absentees need the outcome.
- When commitments from the meeting must be confirmed in writing (vendor, customer).

## When not to use
- The audience is a leader who needs only the outcome. Use `meeting-summary`.
- The formal record is required for governance. Use `meeting-minutes`.
- Only the action list is needed for a tracker. Use `action-item-extraction`.

## Inputs
Required:
- Meeting notes, transcript or a description of outcomes.

Optional:
- Recipient list and whether external parties are included, sender role, channel (email or chat), next meeting date, links to materials.

If external recipients are included, confirm what may be shared; do not include internal-only remarks.

## Process
1. Pick the channel and length: email for external or formal groups, chat for small internal teams. Aim for 120-250 words.
2. Write a subject line: `Follow-up: <meeting> – <date> – decisions and next steps`.
3. Open with one line of thanks and the single most important outcome.
4. List decisions as short statements, explicitly agreed only.
5. List actions as "Owner – action – due date". Put the recipient's own actions first if writing to one person.
6. List open questions with who will answer and by when.
7. Add next steps: next meeting date/time or the event that triggers it; links to notes, slides, recording.
8. Add a correction line: "If anything here does not match your understanding, reply by <date>."
9. Adjust tone for audience: external = more formal, no internal jargon or internal disagreements; internal = direct.
10. Remove sensitive details (pricing, personal data, internal positions) if recipients are external or broad.
11. If the user's goal continues, suggest `open-questions-tracker` to keep unresolved points alive or `stakeholder-email` for a separate message to people who were not in the meeting.

## Output format
```markdown
Subject: Follow-up: <meeting> – <date> – decisions and next steps

Hi all,

Thanks for your time today. Key outcome: <one sentence>.

Decisions
- <decision>

Actions
- <Owner> – <action> – <due>

Open questions
- <question> – <who> – <by when>

Next steps
- Next meeting: <date/time or trigger or [TBD]>
- Materials: <links or [TBD]>

If anything here does not match your understanding, please reply by <date>.

<Sender>
```

## Quality checklist
- [ ] Sent-ready: subject, greeting, closing and sender present.
- [ ] Decisions and actions match the source; nothing invented.
- [ ] Every action has owner and due date or `[TBD]`.
- [ ] A correction deadline is included.
- [ ] Content is appropriate for the least-trusted recipient (external, broad list).
- [ ] Anything not stated in the input is labeled `[ASSUMPTION]` or listed as an open question, never presented as fact.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Sending it days later. The value comes from speed; draft it the same day.
- Narrating the discussion. Keep only outcomes, actions, questions and next steps.
- Leaking internal notes to external recipients. Review each line for the widest audience.

## Example
Input: Kickoff with vendor; agreed weekly Tuesday status call, vendor sends staffing plan by Friday, our team shares API specs by Wednesday; data residency question open.

Excerpt of output:
Key outcome: We agreed the working model and the first two weeks of deliverables.
Actions
- <Vendor PM> – Send staffing plan – Friday `[confirm date]`
- <Our tech lead> – Share API specifications – Wednesday `[confirm date]`
Open questions
- Where will production data be hosted (data residency)? – [UNKNOWN] – before contract signature
