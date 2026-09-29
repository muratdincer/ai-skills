---
name: customer-outage-notice
description: "Writes customer-facing outage notices for each stage of a service disruption (investigating, identified, monitoring, resolved) and planned maintenance: plain-language impact, affected services and regions, status, workaround and next update time, without speculation or blame. Use when customers are affected by an outage or degradation, when a status page or email update is due, or when planned maintenance must be announced."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 11-support-ops
  role: support-engineer
  area: tickets
  title: "Write a customer outage notice"
  related: "incident-communication, incident-response, ticket-response, postmortem, known-error-article"
  prompt: "Write the first status page notice: payments via card fail for about 30% of customers in Turkey since 14:05, cause unknown, team investigating."
---

# Write a Customer Outage Notice

## Purpose
Tell affected customers quickly and honestly what is not working, what they can do meanwhile and when they will hear more, so trust is kept and support queues are not flooded with the same question.

## When to use
- An incident or degradation affects customers and needs a status page, email, in-app or social update.
- The incident moves to a new stage (identified, monitoring, resolved) and the notice must be updated.
- Planned maintenance with expected downtime must be announced in advance.

## When not to use
- The audience is internal stakeholders or executives. Use `incident-communication`.
- A written analysis after resolution is needed. Use `postmortem`.
- A single customer's individual issue. Use `ticket-response`.

## Inputs
Required:
- What customers experience (symptom), which service is affected, and the start time.
- The current stage of the incident.

Optional, improves quality:
- Affected regions, customer segments, percentage or count affected; workaround.
- Next update interval, communication policy, channels and approvers.
- Contractual or regulatory notification duties (SLA credits, regulator, KVKK/GDPR if personal data may be involved).

If the symptom, service or start time is missing, ask for it in one message. If personal data may be exposed, stop and route to the security and privacy team: breach notices follow a separate, legally reviewed process and must not be improvised in an outage notice.

## Process
1. Confirm the facts and their confidence with the incident lead; anything unconfirmed is not published. Keep an internal list of `[ASSUMPTION]` items to verify.
2. Choose the stage label: Investigating, Identified, Monitoring, Resolved, or Scheduled maintenance. Use the same labels across all channels.
3. Describe impact from the customer's point of view: which action fails or is slow, for whom, since when (with time zone). Avoid internal component names and jargon.
4. Quantify only with verified numbers ("some customers" is acceptable when the share is unknown); never minimize ("minor glitch") or dramatize.
5. Give a workaround if one is safe and verified; otherwise say none is available yet.
6. State what the team is doing in one sentence, without speculating on cause or blaming a vendor or individual.
7. Commit to the next update time (for example, within 30 minutes), not to a resolution time unless the incident lead confirms an ETA.
8. For Resolved: state end time, total duration, whether any action is needed from customers (retry failed transactions, re-login), data impact if known, and whether a postmortem summary will follow.
9. For scheduled maintenance: window with time zone and duration, affected functions, expected customer impact, preparation steps, and a contact channel.
10. Adapt length per channel (status page, email, in-app banner, SMS) from the same facts, and route for approval if the policy requires it.
11. Hand off: suggest `incident-communication` for internal stakeholders, `postmortem` once resolved, or `known-error-article` if a lasting workaround remains.

## Output format
```markdown
**[<Stage>] <Service> – <customer-visible symptom>**
Posted: <date time, time zone>

**Impact:** <what customers cannot do or see, who, since when>
**Current status:** <one sentence on what the team is doing>
**Workaround:** <steps, or "No workaround is available yet.">
**Next update:** <time, time zone> or sooner if the situation changes.

<Resolved only>
**Resolved at:** <time> (duration <h:mm>)
**Action needed from you:** <none / retry / re-login / ...>
**Follow-up:** <summary of cause will be shared by <date> / [TBD]>

---
Internal only (do not publish): facts to verify – [ASSUMPTION] ...; approver: <name/role>
```

## Quality checklist
- [ ] Every published statement is confirmed by the incident lead; nothing speculative about cause.
- [ ] Impact is written in customer terms with start time and time zone.
- [ ] A next update time is given; a resolution time appears only if confirmed.
- [ ] No blame on vendors or individuals and no internal hostnames or security details.
- [ ] Possible personal data exposure is routed to security/privacy, not described in the notice.
- [ ] Stage label and facts are consistent across channels.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Waiting for the cause before posting. Post "Investigating" early; silence drives ticket volume.
- Giving an ETA to calm customers and then missing it. Promise update times, not fix times.
- Using "some users may experience issues" for a full outage. Understating damages trust more than the outage.
- Forgetting to post "Resolved" or to tell customers to retry failed actions.

## Example
Input: "Card payments fail for about 30% of customers in Turkey since 14:05, cause unknown, team investigating."

Weak: "We are experiencing minor technical issues due to our payment provider. Fixed soon."

Strong:
**[Investigating] Payments – some card payments are failing**
Posted: 14:25 TRT
**Impact:** Since 14:05 TRT, some customers in Turkey see an error when paying by card. Other payment methods are not affected [ASSUMPTION: confirm with incident lead].
**Current status:** Our team is investigating the cause.
**Workaround:** If available on your account, bank transfer can be used meanwhile.
**Next update:** 14:55 TRT or sooner.
