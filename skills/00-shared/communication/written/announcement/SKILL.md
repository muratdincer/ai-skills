---
name: announcement
description: "Writes an announcement of a change, release, policy, process or decision structured as what is changing, why, who is affected and how, when it takes effect, what readers must do, and where to get help. Use when a team, department or user base must be informed of something new or different through email, chat channel, intranet post or newsletter."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: communication
  area: written
  title: "Write an announcement"
  related: "release-announcement, org-change-communication, communication-plan, faq-builder, stakeholder-email"
  prompt: "Announce to all engineering teams that from 1 March every production deployment must pass the new security scan gate, and what they need to do before then."
---

# Write an Announcement

## Purpose
Make sure every affected reader understands what is changing, whether it affects them and what they must do by when, so adoption happens on time and support channels are not flooded with the same questions.

## When to use
- A new process, policy, tool, standard or deadline applies to a group.
- A decision has been made and needs to be broadcast.
- An internal release, launch or milestone should be shared.

## When not to use
- Customer-facing release content with feature detail. Use `release-announcement` or `release-notes`.
- Reorganizations, reporting line or role changes. Use `org-change-communication`.
- The change is a delay, cancellation or failure. Use `bad-news-delivery`.

## Inputs
Required:
- What is changing or being announced.
- Effective date or timing.

Optional:
- Reason, audience segments, required actions, owner/contact, links, exceptions, previous state.

If the audience or the effective date is missing, ask. Do not invent a rationale: if the reason is unknown, leave `[TBD – reason]` and flag it, because announcements without a "why" drive resistance.

## Process
1. Segment the audience by impact: must act, affected but no action, informed only. If segments need different actions, give each a clearly labeled section or separate message.
2. Write a headline that states the change and the date in plain words ("Security scan gate required for production deployments from 1 March").
3. Open with the TL;DR: what, who, when, what you must do, in 2-3 lines.
4. Explain why in one to three sentences, tied to a problem or benefit readers recognize; say what decision it came from if relevant.
5. Describe what changes and what does not change; the "does not change" list prevents rumors.
6. List required actions with deadlines per segment as numbered steps.
7. Add the timeline if phased: dates for pilot, grace period, enforcement.
8. Give help channels: owner, contact, documentation, office hours; anticipate the top 3 questions as a mini FAQ.
9. Check for exceptions, accessibility (no information only in an image), and sensitive data before posting.
10. Label anything not provided by the user (dates, owners, reasons) as `[TBD]` or `[ASSUMPTION]` in a note to the sender.
11. If the user's goal continues, suggest `faq-builder` for a full FAQ or `communication-plan` when the change needs a sequence of messages across channels.

## Output format
```markdown
# <Change> – effective <date>

**TL;DR:** <what, who, when, action in 2-3 lines>

## Why
<1-3 sentences>

## What changes / what does not
- Changes: ...
- Stays the same: ...

## What you need to do
1. <action> – by <date> – <who: segment>

## Timeline
| Date | Milestone |
|---|---|

## Questions
- **<likely question>?** <answer>
Help: <owner/channel/link>

<!-- Notes for sender: [TBD] fields, assumptions -->
```

## Quality checklist
- [ ] Headline and TL;DR alone tell readers whether they are affected and what to do by when.
- [ ] The "why" is present or explicitly flagged `[TBD]`.
- [ ] "What does not change" is stated where confusion is likely.
- [ ] Actions are numbered, dated and assigned to a segment.
- [ ] A named owner or help channel is given.
- [ ] No invented dates, owners or reasons.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Leading with background and history; readers stop before the action. Lead with the TL;DR.
- One message for all segments, so everyone assumes the action is for someone else. Label actions by segment.
- Announcing the change without a help channel, which routes all questions to whoever posted it.

## Example
Input: from 1 March every production deployment must pass the new security scan gate.

Weak: "Hi all, as part of our ongoing efforts to improve security, the security team has been evaluating options for some time and has decided to introduce a new process..."

Strong (excerpt):
# Security scan gate required for production deployments – effective 1 March
**TL;DR:** From 1 March, pipelines without a passing security scan cannot deploy to production. Team leads: add the scan step to your pipelines by 22 February. Help: `[#security-gate channel – TBD]`.
