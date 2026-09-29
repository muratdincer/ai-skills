---
name: stakeholder-email
description: "Writes a purpose-first email to a stakeholder with a subject line that states the action, the ask or key message in the first two lines, only the context needed, and a tone matched to the reader's role and relationship. Use when someone needs to request something, inform, align or follow up with a manager, sponsor, customer, vendor or another team by email or long chat message."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: communication
  area: written
  title: "Write a stakeholder email"
  related: "tone-rewrite, escalation-message, bad-news-delivery, stakeholder-map, meeting-follow-up"
  prompt: "Write an email to the head of finance asking her team to validate the new cost allocation rules by Friday so we can start UAT next week."
---

# Write a Stakeholder Email

## Purpose
Get the reader to understand and act on the message from the subject line and first two sentences, with a tone that fits the relationship, so the request is answered on time without follow-up clarification.

## When to use
- Asking a stakeholder for a decision, input, approval, data or time.
- Informing a stakeholder of something that affects them.
- Aligning or following up with another team, a customer or a vendor.

## When not to use
- Escalating a blocked issue to a higher level. Use `escalation-message`.
- Communicating a delay, cancellation or failure. Use `bad-news-delivery`.
- Only adjusting the tone of an existing draft. Use `tone-rewrite`.

## Inputs
Required:
- Recipient (role, relationship) and the purpose: what you want them to know or do.

Optional:
- Context, deadline and its reason, attachments, prior thread, cultural or formality expectations, sender's role.

If the purpose or the recipient is unclear, ask one question at a time. Leave unknown dates, names and figures as `[TBD]`; do not invent them.

## Process
1. Classify the email: request (decision, input, approval), inform, align, or follow-up. One email, one primary purpose; split if there are two unrelated asks.
2. Read the recipient: role, power over the outcome, what they care about (cost, risk, customers, their team's workload), formality of the relationship. Label anything you infer about them as an assumption.
3. Write the subject line as `[Action/Info] <topic> – <deadline if any>` (e.g. "Action needed: validate cost allocation rules by Fri 14 Mar").
4. Write the opening two sentences: the ask or key message, and why it matters to them.
5. Add only the context needed to act: what, why now, what happens if it slips. Three short paragraphs or bullets at most.
6. Make the ask executable: exact action, owner, format of reply, deadline with its reason, and what you will do to make it easy (attached file, 15-minute walkthrough offer).
7. Match tone to the reader: senior or external = concise and formal; peer = direct and warm; cross-cultural = explicit, no idioms. In Turkish, choose "siz" and appropriate titles (Hanım/Bey) unless the relationship is informal.
8. Close with the next step and a clear owner, not a generic "let me know".
9. Check recipients: To = who must act, Cc = who needs to know; remove sensitive data if the list is broad or external.
10. If the user's goal continues, suggest `tone-rewrite` for a different register or `escalation-message` if the ask goes unanswered past the deadline.

## Output format
```markdown
To: <who must act>   Cc: <who needs to know>
Subject: <Action needed / FYI>: <topic> – <deadline>

<Greeting>,

<Ask or key message in one sentence.> <Why it matters to the reader.>

<Context: 2-4 bullets or short sentences.>

<Ask: who does what, how to reply, by when and why that date.>
<Support offered: attachment, call, contact.>

<Next step / closing>,
<Sender>

Notes for sender: <assumptions made, [TBD] fields to fill>
```

## Quality checklist
- [ ] The subject line alone tells the reader whether to act and by when.
- [ ] The ask is in the first two sentences.
- [ ] Only one primary purpose; secondary topics are removed or clearly separated.
- [ ] Deadline has a reason; unknown values are `[TBD]`, not invented.
- [ ] Tone and formality fit the recipient and culture.
- [ ] Readable on a phone screen without scrolling past the ask.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Narrative emails that tell the history first and ask in the last line. Invert them.
- Vague asks ("any thoughts?") that get vague or no answers. Ask a closed question or a specific action.
- Cc-ing managers as pressure. It damages the relationship; escalate explicitly with `escalation-message` if needed.

## Example
Input: head of finance, validate cost allocation rules by Friday so UAT can start.

Weak: "Hi, hope you are well. As you may know we have been working on the new cost allocation module for some time... Could your team maybe have a look when they have time?"

Strong (excerpt):
Subject: Action needed: validate cost allocation rules by Fri `[date]`
"Dear Ayşe, could your team validate the attached 12 allocation rules by Friday? UAT starts Monday and cannot begin without finance sign-off on these rules."
