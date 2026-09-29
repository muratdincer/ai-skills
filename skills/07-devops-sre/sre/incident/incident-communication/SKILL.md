---
name: incident-communication
description: "Writes incident communications for each phase (investigating, identified, monitoring, resolved) and audience: internal stakeholder updates, executive summaries and public status-page posts, with confirmed impact, customer actions, next update time and no speculation on cause. Use during or right after an incident when an update, status-page entry, customer notice or leadership briefing must be written or reviewed."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: sre
  area: incident
  title: "Write incident communications"
  related: "incident-response, customer-outage-notice, postmortem, bad-news-delivery, status-update"
  prompt: "Write the first status-page update and an internal Slack update: payments failing for about 20% of EU customers since 09:40, cause unknown, team investigating."
---

# Write Incident Communications

## Purpose
Keep every audience accurately informed during an incident, with messages that state confirmed impact and next steps, avoid speculation and blame, and arrive on a predictable cadence, so trust is preserved and responders are not interrupted with questions.

## When to use
- An incident is declared and a first or follow-up update is due.
- A status-page post, internal broadcast or executive briefing must be drafted or reviewed.
- An incident is resolved and a closing message is needed before the postmortem.

## When not to use
- The incident itself must be coordinated. Use `incident-response`.
- A formal customer notice with contractual or regulatory content is needed after the event. Use `customer-outage-notice`.
- The full analysis of what happened is the goal. Use `postmortem`.

## Inputs
Required:
- Current incident facts: affected service or function, start time, known impact, status phase.

Optional, improves quality:
- Audiences and channels in use (status page, internal channel, email, account managers).
- Organization templates, tone rules, legal or regulatory notification duties.
- Customer workarounds, ETA if genuinely known, next update time.

If impact or phase is unknown, ask one question for it. Never state a cause, ETA or number of affected customers that was not confirmed; use `[TBD]` or neutral phrasing.

## Process
1. Identify the phase (investigating, identified, monitoring, resolved) and the audiences that need a message now: internal responders' stakeholders, executives, customers (public or targeted), partners.
2. Extract confirmed facts only: what users experience, since when, scope (regions, features, share of users if measured), and what is being done; mark anything unconfirmed and keep it out of external text.
3. For external messages write in user terms: symptom, affected function, workaround if any, next update time. Exclude internal system names, speculation about cause, blame of vendors or individuals.
4. For internal messages add: severity, incident commander, channel to follow, business impact, decisions needed, and what not to do (e.g. no separate customer outreach).
5. For executives write three lines: impact in business terms, current status and risk, decision or support needed.
6. Always include the next update time and keep it even if there is no news ("no change, still investigating").
7. Check personal data and security: no customer identities, no details that aid attackers; if a data breach is suspected, route through the security and legal process before any external statement.
8. For the resolved message: time of resolution, what users may still see (e.g. delayed notifications), what users need to do, and whether a follow-up or postmortem summary will be published.
9. Review tone: plain, calm, accountable, no jargon, no minimizing ("minor glitch") and no over-promising.
10. Label inferences `[ASSUMPTION]`, list open questions, and suggest next skills: `customer-outage-notice` for formal follow-up, `postmortem` after closure.

## Output format
```markdown
# Incident Communications: <incident> · Phase: <phase> · <time, time zone>

## Status Page (public)
**<Title: function affected>**
<Symptom and scope in user terms>. <What we are doing>. <Workaround if any>. Next update by <time>.

## Internal Update
Severity: <SEVn> · IC: <name> · Channel: <link or name>
- Impact: ...
- Status: ...
- Decisions/help needed: ...
- Next update: <time>

## Executive Summary (3 lines)
## Unconfirmed Items (not for external use)
## Open Questions
```

## Quality checklist
- [ ] External text contains only confirmed facts, in user terms, with no cause speculation or internal names.
- [ ] Every message states the next update time.
- [ ] Each audience gets the content it needs (customer action, internal decisions, executive risk).
- [ ] No personal data or attack-relevant detail; suspected breaches are routed to security and legal.
- [ ] Tone is calm and accountable, without minimizing or over-promising.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Promising an ETA to calm people. Missed ETAs damage trust more than "next update at 10:30".
- Going silent because there is no news. Post the "still investigating" update on time.
- Naming a cause early ("database failure") that turns out wrong. Describe the symptom until the cause is confirmed.

## Example
Input: "Payments failing for ~20% of EU customers since 09:40, cause unknown."

Weak status-page post: "We are experiencing a minor glitch with our DB cluster in eu-west. Should be fixed in 15 minutes."

Strong status-page post:
**Card payments failing for some customers in Europe**
Since 09:40 UTC some customers in Europe cannot complete card payments. Other functions are working normally. Our team is investigating. Next update by 10:30 UTC.
