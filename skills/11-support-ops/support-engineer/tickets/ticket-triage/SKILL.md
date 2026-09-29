---
name: ticket-triage
description: "Triages an incoming support ticket: classifies it (incident, service request, question, defect, security or privacy report), sets priority from impact and urgency, checks for duplicates or an ongoing outage, identifies missing information and routes it to the right queue or level. Use when a new ticket, email or chat request arrives in a support queue, when a backlog of unclassified tickets needs sorting, or when priority is disputed."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 11-support-ops
  role: support-engineer
  area: tickets
  title: "Triage a support ticket"
  related: "ticket-response, ticket-escalation-summary, known-error-article, incident-response, bug-report"
  prompt: "Triage this ticket: 'Since this morning none of our 40 branch users can print invoices from the POS, we are writing them by hand.'"
---

# Triage a Support Ticket

## Purpose
Decide within minutes what a ticket is, how urgent it is, who should handle it and what is missing, so critical issues reach the right people fast and routine requests do not clog higher support levels.

## When to use
- A new ticket, email, chat or phone note enters the support queue.
- A batch of unclassified or misrouted tickets needs sorting.
- Priority is disputed between the customer, support and engineering.

## When not to use
- The ticket is triaged and needs a customer reply. Use `ticket-response`.
- It must be handed to a higher level with full context. Use `ticket-escalation-summary`.
- A major incident is declared and needs coordination. Use `incident-response`.

## Inputs
Required:
- The ticket text (subject, description, any attachments or logs described).

Optional, improves quality:
- Customer or user identity, contract tier and SLA, affected service or product.
- The organization's priority matrix, categories and routing rules.
- Current known errors, ongoing incidents, recent changes or releases.

If the ticket text is missing, ask for it. Do not delay triage for optional inputs; mark them `[UNKNOWN]` and note which would change the priority. Mask personal data (national ID numbers, card numbers, passwords, health details) when repeating ticket content, and flag any credentials the user pasted so they can be rotated.

## Process
1. Separate what the reporter states (symptom, scope, time) from your interpretation (likely cause, affected component). Label interpretations `[ASSUMPTION]`.
2. Classify the ticket type: incident (service degraded or down), service request (standard fulfilment), question/how-to, defect (reproducible product bug without immediate outage), change request, security or privacy report, complaint.
3. Route security and privacy reports immediately to the defined channel (security team, DPO) regardless of other priority; possible personal data breaches have statutory notification clocks under KVKK and GDPR.
4. Assess impact: number of users, sites or customers affected, business process blocked, workaround available, data at risk, regulatory or financial exposure.
5. Assess urgency: is it getting worse, time-critical deadline, blocking now versus later.
6. Derive priority from the impact x urgency matrix (use the organization's matrix if provided, otherwise a 3x3 mapping to P1-P4 marked `[ASSUMPTION]`). Record the reason in one line.
7. Check for duplicates, an ongoing incident or a known error with the same symptom; if found, link rather than open a parallel investigation.
8. List the missing information that blocks diagnosis (error text, time, affected user example, environment, steps, screenshots) and ask for it in one message.
9. Route to queue or level (L1, L2, L3, vendor, product team) using routing rules; state the expected first response and resolution targets from the SLA.
10. Hand off: suggest `ticket-response` for the acknowledgement, `ticket-escalation-summary` when routing to a higher level, `incident-response` for P1, or `bug-report` for a confirmed defect.

## Output format
```markdown
# Triage: <ticket ID> – <short title>
| Field | Value |
|---|---|
| Type | incident / service request / question / defect / change / security-privacy / complaint |
| Category | <service> > <component> |
| Impact | <who and how many, workaround yes/no> |
| Urgency | <reason> |
| Priority | P1-P4 – <one-line justification> |
| Related | <incident / known error / duplicate ID or none found> |
| Route to | <queue / level / team> |
| SLA targets | first response <...>, resolution <...> or [UNKNOWN] |

## Stated vs Inferred
- Stated: ...
- [ASSUMPTION] ...
## Missing Information (ask the reporter)
1. ...
## Next Step
<acknowledge / escalate / declare incident / request info>
```

## Quality checklist
- [ ] Priority follows from stated impact and urgency, not from tone or seniority of the reporter.
- [ ] Security and privacy reports are routed to their channel regardless of priority.
- [ ] Duplicates, ongoing incidents and known errors were checked and linked.
- [ ] Missing information is asked for in a single, specific message.
- [ ] Personal data and pasted credentials are masked in the triage note.
- [ ] Inferences are labeled `[ASSUMPTION]` and SLA targets not given are `[UNKNOWN]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Setting priority by how angry or senior the reporter is. Use the matrix and write the reason.
- Treating many similar tickets as separate issues. Look for a common cause and link them to one incident.
- Downgrading because a workaround exists without checking whether the workaround is practical at scale.
- Sending a ticket back and forth between queues. Route once with a clear reason; escalate if the owner is unclear.

## Example
Input: "Since this morning none of our 40 branch users can print invoices from the POS, we are writing them by hand."

Excerpt of output:
| Type | Incident |
| Impact | 40 users at all branches [ASSUMPTION: all branches of one customer], invoicing blocked; manual workaround exists but creates tax compliance risk |
| Priority | P2 – high impact, workaround available but not sustainable; raise to P1 if more customers report |
| Related | Check release deployed last night to POS print service [ASSUMPTION] |
Missing information: exact error on screen, one affected terminal ID, time of first failure.
