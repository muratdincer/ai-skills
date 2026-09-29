---
description: "Guides the response to a suspected or confirmed security incident through triage, containment, evidence preservation, eradication, recovery and notification, including KVKK and GDPR personal data breach duties, and produces an incident log and action plan. Use when there are signs of compromise, credential leakage, malware, data exfiltration or unauthorized access and the team needs a structured, defensive response."
related: "incident-response, incident-communication, postmortem, vulnerability-triage, security-finding-report"
prompt: "We found an AWS access key of our CI user in a public GitHub repo and CloudTrail shows calls from an unknown IP. Help us respond."
---

# Respond to a Security Incident

## Purpose
Limit damage from a security incident, preserve evidence, restore trusted operation and meet legal notification duties, while keeping a clear record of decisions.

## When to use
- Indicators of compromise: suspicious logins, leaked credentials, malware alerts, unusual data transfers, defacement, ransomware notes.
- A third party (customer, researcher, vendor, authority) reports a breach or suspected breach.
- A vulnerability is found to have been exploited.

## When not to use
- An availability incident with no security cause. Use `incident-response`.
- A vulnerability with no sign of exploitation. Use `vulnerability-triage`.
- The incident is closed and needs a learning review. Use `postmortem`.

## Inputs
Required:
- What was observed, when, where (systems, accounts, data) and who detected it.

Optional, improves quality:
- Logs, alerts, timeline so far, actions already taken.
- The organization's incident response plan, severity levels, contact list, legal/privacy contacts.
- Data classification of affected systems.

If the observation is missing, ask. Do not delay containment advice for optional details; record them as open questions.

## Process
1. Triage: confirm it is a security incident, assign a severity per the organization's scale, name an incident lead and a scribe, open an incident log with UTC timestamps.
2. Scope first hypotheses: affected assets, identities, data types, entry vector, whether the attacker may still be active.
3. Preserve evidence before destructive steps: snapshot disks or instances, export logs, keep chain of custody notes; avoid rebooting or wiping compromised hosts unless required to stop harm.
4. Contain short-term: revoke or rotate exposed credentials and sessions, disable compromised accounts, isolate hosts or network segments, block indicators (IP, domain, hash), pause affected integrations.
5. Investigate: build the attack timeline from logs (identity, cloud control plane, endpoint, network, application), determine what data was accessed or exfiltrated, look for persistence (new users, keys, scheduled tasks, backdoors).
6. Eradicate: remove persistence and malware, patch the exploited weakness, rebuild from trusted images where integrity is doubtful.
7. Recover: restore services in stages with heightened monitoring, verify integrity of data and configurations, define criteria for returning to normal.
8. Assess personal data breach: if personal data may be affected, involve the data controller's privacy officer and legal. Under GDPR, notify the supervisory authority within 72 hours of becoming aware unless the breach is unlikely to result in a risk; under KVKK, notify the KVK Board as soon as possible (the Board's guidance expects within 72 hours) and inform data subjects. Legal decides; the skill only prepares facts.
9. Communicate: internal stakeholders on a fixed cadence, customers and partners as decided by leadership and legal; keep statements factual and approved.
10. Close: confirm containment and eradication, list follow-up actions with owners, schedule a postmortem.

## Output format
```markdown
# Security Incident <ID> – <short title>
| Field | Value |
|---|---|
| Severity | ... | Status | Investigating / Contained / Eradicated / Recovered / Closed |
| Detected | <UTC time> by <source> | Incident lead | ... |
| Affected assets / identities | ... |
| Personal data involved | Yes / No / [UNKNOWN] – categories, approx. subjects [UNKNOWN] |
## Timeline (UTC)
| Time | Event / action | By | Evidence ref |
## Containment Actions
- [ ] ...
## Investigation Findings
## Eradication and Recovery Plan
## Notification Assessment
- GDPR / KVKK: decision owner, deadline, status
## Communications Log
## Open Questions and Next Update
```

## Quality checklist
- [ ] Containment steps come first and are concrete (which key, which account, which host).
- [ ] Evidence preservation happens before destructive actions.
- [ ] The timeline uses one time zone and cites evidence for each entry.
- [ ] Personal data impact and notification deadlines are assessed and assigned to legal/privacy.
- [ ] Credentials, tokens and personal data are masked in the log.
- [ ] No attribution or data volumes are stated without evidence.

## Common pitfalls
- Rotating one leaked key but missing the sessions, tokens and derived credentials it created.
- Wiping a host immediately, destroying the evidence needed to know what was taken.
- Missing the regulatory clock because nobody owns the notification decision.
- Announcing root cause or attacker identity before the investigation supports it.

## Example
Input: "CI user's cloud access key found in a public repo; control-plane logs show calls from an unknown IP."

Excerpt of output:
- [ ] Deactivate the leaked key now, then create a new key for CI from the secrets manager; do not delete the old key until logs are exported.
- [ ] Query control-plane logs for all actions by this key since the commit date: new users, keys, roles, instances, storage reads.
- Notification assessment: storage buckets reachable by the key contain customer exports [ASSUMPTION: confirm]; privacy officer to decide on KVKK/GDPR notification, 72-hour clock started at <UTC time of awareness>.
