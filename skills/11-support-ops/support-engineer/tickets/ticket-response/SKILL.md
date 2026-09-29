---
name: ticket-response
description: "Writes a customer-facing reply to a support ticket that acknowledges the issue, states what is known, gives a clear answer or next step with ownership and timing, and asks only for the information that is needed. Use when replying to a new or updated ticket, following up on a pending ticket, delivering a resolution, declining a request, or rewriting a draft reply that is too technical, too long or defensive."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 11-support-ops
  role: support-engineer
  area: tickets
  title: "Write a ticket response"
  related: "ticket-triage, ticket-escalation-summary, known-error-article, tone-rewrite, bad-news-delivery"
  prompt: "Write a reply to this customer: they cannot log in after the password reset, it is the second time this week and they are frustrated."
---

# Write a Ticket Response

## Purpose
Give the customer a reply they can act on in one read: they feel heard, they know what happens next and when, and the ticket moves forward instead of generating another round of questions.

## When to use
- First response or acknowledgement to a new ticket.
- Status update, request for information, or follow-up on a pending ticket.
- Delivering a resolution, a workaround or a "no" (out of scope, not supported, by design).
- Improving a drafted reply before sending.

## When not to use
- The ticket is not yet classified or prioritized. Use `ticket-triage`.
- Many customers are affected by the same outage. Use `customer-outage-notice`.
- The message is an internal handoff to another support level. Use `ticket-escalation-summary`.

## Inputs
Required:
- The customer's message (latest and relevant history).
- What support knows or has decided: the answer, the status, or the next step.

Optional, improves quality:
- Customer name, language and channel (email, portal, chat), contract tier or SLA.
- Known error or KB article, workaround, commitment dates allowed by policy.
- Company tone guidelines and signature format.

If support's position or next step is missing, ask for it; do not invent a fix, cause or date. Do not repeat sensitive data from the ticket (passwords, card numbers, national ID numbers); if the customer shared a secret, advise them to change it.

## Process
1. Identify what the customer actually needs from this reply: an answer, a fix, reassurance, a date, or permission to proceed. Note their emotional state and history (repeat contact, previous promises).
2. Choose the reply type: acknowledge, request information, update, resolve, workaround, decline, close.
3. Open with a specific acknowledgement of their situation and impact (not a generic apology), one sentence. Apologize for the experience when the company caused it; do not admit liability or speculate on cause.
4. State the key message in the first two to three sentences: the answer, the status or the decision.
5. Give next steps as a short numbered list: what the customer should do, what support will do, and when the next update will come. Use only dates allowed by policy; otherwise give an update time, not a resolution promise.
6. Ask for missing information in one batch, explaining briefly why each item is needed.
7. For a "no", explain the reason in plain language and offer an alternative (workaround, feature request channel, paid service).
8. Adapt language and depth to the audience: plain words for business users, exact commands or error codes for technical contacts. Match the customer's language (Turkish or English) and a formal address form where expected.
9. Keep it short (typically under 150 words for chat or portal, under 250 for email), remove internal jargon, ticket routing details and blame on other teams.
10. Suggest the next skill: `ticket-escalation-summary` if the ticket must go up a level, `known-error-article` if the same answer is being written repeatedly, `tone-rewrite` for sensitive cases.

## Output format
```markdown
Subject: <ticket ID> – <plain summary of the status>

Hello <name>,

<one-sentence specific acknowledgement>
<key message: answer / status / decision>

Next steps:
1. <what we do> – <when>
2. <what we need from you, if anything>

<when the next update will come or how to reopen>

<signature>

---
Internal note (not sent): reply type, promises made, open items, [ASSUMPTION]s used
```

## Quality checklist
- [ ] The key message is in the first three sentences.
- [ ] Every commitment has an owner and a time, and no resolution date is promised without authorization.
- [ ] No cause, fix or date is invented; unknowns are expressed honestly ("we are still investigating").
- [ ] Information requests are grouped and each has a reason.
- [ ] No sensitive data is repeated, and internal blame or jargon is removed.
- [ ] Length and language fit the channel and the customer.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Scripted empathy ("We apologize for any inconvenience") without addressing the real impact. Name the actual problem.
- Burying the answer after troubleshooting history. Lead with the outcome.
- Asking the customer for information already in the ticket. Read the history first.
- Closing tickets with "please let us know if the problem persists" when the fix is unverified. Confirm or schedule a check.

## Example
Input: "Customer cannot log in after password reset, second time this week, frustrated. Cause: reset emails link to the old tenant URL; fix deploying tonight; workaround: use the direct login link."

Weak: "Dear customer, we apologize for any inconvenience. Our team is working on it. Please try again later."
Strong: "Hello Ayşe, being locked out twice in one week is not acceptable, and I am sorry. The reset email currently sends you to an outdated address. Until the fix is released tonight, please log in via <direct login link> with your new password. I will update you by 10:00 tomorrow once we confirm the fix."
