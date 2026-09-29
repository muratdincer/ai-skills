---
name: handover-document
description: "Writes a handover document that transfers ownership of a system, project, service, workstream or role to a new owner, covering context, current state, responsibilities, contacts, access, recurring duties, risks, open items and a transition plan with an acceptance point. Use when someone leaves, changes role, goes on long leave, when a project moves from delivery to operations, when a vendor or team changes, or when asked to \"prepare a handover\"."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: knowledge
  area: capture
  title: "Write a handover document"
  related: "on-call-handover, runbook, onboarding-guide, raid-log, kb-article"
  prompt: "I'm moving to another team in two weeks. Help me write a handover for the payment reconciliation service I own."
---

# Write a Handover Document

## Purpose
Move ownership without losing knowledge, commitments or momentum. A good handover lets the new owner act alone on day one, knows what is fragile, and makes the moment of accountability transfer explicit.

## When to use
- A person leaves, changes role or takes extended leave.
- A project or product moves from a delivery team to an operations or support team.
- A vendor, contractor or team is replaced, or a workstream is reassigned.

## When not to use
- Shift-to-shift operational handover during on-call. Use `on-call-handover`.
- Step-by-step operating procedures for a specific task. Use `runbook`.
- Orienting a newcomer to the team in general, not to a specific ownership. Use `onboarding-guide`.

## Inputs
Required:
- What is being handed over (system, project, service, role) and to whom (name or role).
- The outgoing owner's knowledge: notes, brain dump or answers to questions.

Optional, improves quality:
- Handover deadline, overlap period, existing documentation, backlog, risk or RAID log.
- Architecture diagrams, runbooks, contracts, SLAs, stakeholder lists.

If the scope or the recipient is missing, ask. Then elicit the knowledge with focused questions in batches of at most 5 (responsibilities, recurring duties, fragile parts, people, open commitments), reusing anything already provided.

## Process
1. Define the handover scope precisely: what is included, what stays with someone else, and what is being retired. List explicitly anything ambiguous.
2. Write the context: why the thing exists, who it serves, key decisions and their rationale (link to decision records when they exist), and history that explains current oddities.
3. Describe the current state: status, health, recent changes, in-flight work, and known deviations from the plan or standard. Mark unconfirmed statements `[ASSUMPTION]`.
4. List responsibilities and recurring duties with frequency and trigger (daily checks, monthly reports, certificate renewals, license and contract dates, audits). Hidden calendar-driven duties are the most common loss.
5. Capture the people map: stakeholders, decision makers, users, dependent teams, vendors and escalation contacts, each with what they expect from the owner. Use roles where names are not given.
6. Inventory access and assets: systems, environments, repositories, dashboards, shared mailboxes, licenses, credentials stores. Record where access is requested, never the secrets themselves.
7. List risks, fragile areas and tribal knowledge ("do not restart X during Y", workarounds, known bugs), each with its trigger and mitigation.
8. List open items and commitments: promises made to stakeholders, pending decisions, open tickets, deadlines, with owner after handover.
9. Plan the transition: overlap activities (shadowing, reverse shadowing), knowledge-transfer sessions, a handover acceptance point (date and criteria), and how the outgoing owner can be reached afterwards and for how long.
10. Check privacy and security: no passwords, tokens or personal data beyond business contacts; flag anything that needs access revocation.
11. Fill the output template, list open questions for the outgoing owner, and suggest the next skill if the goal continues: `runbook` for procedures uncovered here, `kb-article` for reusable knowledge, or `onboarding-guide` if the new owner is also new to the team.

## Output format
```markdown
# Handover: <what> from <outgoing> to <incoming>
Handover date: <date or TBD> · Overlap: <period> · Accepted when: <criteria>

## Scope
- Included: ... · Not included (stays with): ... · Unclear: ...

## Context and Key Decisions
- ...

## Current State
- Status/health: ... · In-flight work: ... · Known deviations: ...

## Responsibilities and Recurring Duties
| Duty | Frequency / trigger | Next due | How / reference |
|---|---|---|---|

## People and Escalation
| Role / name | Relationship | What they expect | Channel |
|---|---|---|---|

## Access and Assets
| Asset | Where / how to request access | Status for new owner |
|---|---|---|

## Risks, Fragile Areas and Tribal Knowledge
- <item> — trigger — mitigation

## Open Items and Commitments
| Item | Promised to | Due | Owner after handover |
|---|---|---|---|

## Transition Plan
- Sessions: ... · Shadowing: ... · Outgoing owner reachable: <until when, how>

## Open Questions
1. ...
```

## Quality checklist
- [ ] Scope is explicit, including what is not handed over.
- [ ] Every recurring or calendar-driven duty has a frequency and next due date or `[TBD]`.
- [ ] Every open commitment has an owner after handover.
- [ ] The acceptance point (date and criteria) is stated.
- [ ] No secrets or unnecessary personal data; access is described by how to request it.
- [ ] Unconfirmed statements are marked `[ASSUMPTION]`; nothing is invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Handing over documents instead of ownership. Without an acceptance point, accountability stays ambiguous and issues fall between owners.
- Forgetting annual or quarterly duties (certificate expiry, license renewal, audit evidence). Walk through a full year's calendar.
- Recording only the happy path. The new owner most needs the workarounds and the "never do X" rules.

## Example
Input: "Moving teams in two weeks. I own the payment reconciliation service. Finance gets a daily report; the bank file format changes every January."

Excerpt of output:
- Recurring duty: bank file format update — yearly, January — next due `[TBD: confirm with bank]` — reference: `[UNKNOWN: is there a runbook?]`.
- People: Finance operations (role) — expects the daily report by 09:00 `[ASSUMPTION]` — escalation: `[UNKNOWN]`.
- Accepted when: new owner runs the daily reconciliation alone for 5 business days without help.
