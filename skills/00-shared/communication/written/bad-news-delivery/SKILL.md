---
name: bad-news-delivery
description: "Communicates a delay, cancellation, scope cut, failed delivery, rejected request or missed commitment transparently, stating the news early, the cause without blame, the impact on the reader, what is being done, options and the next update. Use when someone must tell a customer, sponsor, manager or team that something will not happen as promised or expected, in writing or as talking points for a conversation."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: communication
  area: written
  title: "Deliver bad news"
  related: "tone-rewrite, escalation-message, stakeholder-email, status-update, customer-outage-notice"
  prompt: "Help me tell the sponsor that the reporting release planned for the 20th will slip by three weeks because the data vendor's API changed, and what we propose instead."
---

# Deliver Bad News

## Purpose
Deliver unwelcome news early and plainly, with ownership, impact and a way forward, so the reader can adjust their plans and trust is kept or rebuilt instead of eroded by surprise or spin.

## When to use
- A committed date, scope or result will be missed.
- A request, proposal or budget is rejected.
- A project, feature or service is cancelled or significantly changed.
- Preparing talking points before delivering the news in person.

## When not to use
- A live incident or outage with ongoing updates. Use `incident-communication` or `customer-outage-notice`.
- You need a decision from a higher level to resolve the problem. Use `escalation-message`.
- The news is a performance issue about a person. Use `feedback-sbi`.

## Inputs
Required:
- The news itself (what will not happen as expected).
- The recipient and their stake.

Optional:
- Cause, new date or options, what is already being done, mitigation offered, relationship history, channel.

If the new date or recovery plan is unknown, do not invent one: say when a firm date will be given. Ask for the cause only if it is needed to explain the impact; unknown causes are stated as "under investigation".

## Process
1. Choose the channel: significant news for a key stakeholder goes live (call/meeting) first, then in writing; the written version must still stand alone.
2. Put the news in the first sentence, in plain words. No warm-up paragraph, no buried lead.
3. Take ownership appropriate to the sender's role: "we" for the team's commitments; do not blame vendors or individuals, even when they caused it; state causes as facts.
4. Explain the cause in one or two sentences, only as deep as the reader needs; separate what is known from what is still being investigated.
5. State the impact from the reader's perspective: what they lose, what they must change, which of their dates move.
6. Describe what is already being done and what will be done to limit the impact.
7. Offer options where possible (partial delivery, reduced scope on time, later full delivery) with trade-offs, and ask the reader to choose or confirm.
8. Commit to the next update: date and what it will contain; give a firm date only if the user supplied one.
9. Apologize once, sincerely and specifically, if a commitment was broken; no repeated or generic apologies.
10. Label every inferred cause, impact or date as `[ASSUMPTION]` or `[TBD]` and list them for the sender to confirm.
11. If the user's goal continues, suggest `tone-rewrite` to adjust register for a specific reader or `status-update` to reflect the change in regular reporting.

## Output format
```markdown
Subject: <Topic>: <the news in plain words>

<Name>, <the news in one sentence>.

**Why:** <cause in 1-2 sentences; known vs. under investigation>
**What it means for you:** <impact in reader's terms>
**What we are doing:** <actions under way>
**Options:**
1. <option> – <trade-off>
2. <option> – <trade-off>
**What we need from you:** <choice/confirmation> by <date>
**Next update:** <date> with <content>

<one specific apology if a commitment was broken>

Talking points (if delivered live): <3-5 bullets in the same order>
Notes for sender: <assumptions, [TBD] items>
```

## Quality checklist
- [ ] The bad news is in the first sentence, not after context.
- [ ] Cause is stated factually with no blame on individuals or third parties.
- [ ] Impact is described from the reader's point of view.
- [ ] There is at least one option or a concrete recovery action, and a next-update date.
- [ ] No invented dates, figures or causes; unknowns are marked.
- [ ] At most one apology, and it is specific.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Sandwiching the news between compliments; the reader misses it or feels manipulated. Lead with it.
- Over-promising a new date to soften the blow, then missing it again. Give a date only when it is credible; otherwise commit to when you will know.
- Delivering bad news late to "wait until we have a solution". Early news with an honest plan beats late news with a polished one.

## Example
Input: reporting release on the 20th slips three weeks because the data vendor's API changed.

Weak: "Hi, just a quick update. The team has been working really hard and made great progress. However, due to some external factors, there may be a slight adjustment to the timeline..."

Strong (excerpt):
Subject: Reporting release: moving from the 20th to `[new date]`
"Emre, the reporting release will not ship on the 20th; our current estimate is three weeks later.
Why: the data vendor changed its API on `[date]`; our integration must be rebuilt.
Options: 1) release the 4 reports that do not use the vendor data on the 20th; 2) release everything together three weeks later."
