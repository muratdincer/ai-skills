---
name: ticket-escalation-summary
description: "Condenses a support ticket and its history into an escalation summary for the next support level, engineering or a vendor: business impact, precise symptom, environment, timeline, what was tried with results, evidence and the exact ask. Use when a ticket must move from L1 to L2/L3, to a product team or to a third party, when a long ticket thread needs a handover note, or when a customer pushes for escalation."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 11-support-ops
  role: support-engineer
  area: tickets
  title: "Summarize a ticket for escalation"
  related: "ticket-triage, ticket-response, log-analysis, bug-report, problem-management"
  prompt: "Summarize this 30-message ticket for L3: users get 'session expired' every few minutes on the web portal since Tuesday; we cleared caches and reset passwords, no change."
---

# Summarize a Ticket for Escalation

## Purpose
Give the receiving level everything it needs to act in one read, without re-asking the customer or repeating diagnostics already done, so escalations shorten resolution time instead of restarting it.

## When to use
- A ticket exceeds the current level's skills, permissions or time budget.
- A ticket moves to an engineering or product team, or to a vendor's support.
- A long, messy ticket thread needs a clean handover between shifts or owners.

## When not to use
- The ticket has not been classified or prioritized yet. Use `ticket-triage`.
- The goal is a reply to the customer. Use `ticket-response`.
- A confirmed, reproducible product defect needs a backlog item. Use `bug-report`.

## Inputs
Required:
- The ticket content and its history (messages, notes, actions taken).

Optional, improves quality:
- Priority, SLA and time remaining; customer tier and contract obligations.
- Logs, error texts, screenshots described, correlation or request IDs.
- The target team's escalation template or mandatory fields.

If the ticket history is missing, ask for it. Do not ask for optional items up front; list them under "Missing evidence". Mask personal data (names of end users, national ID numbers, card numbers, health details) and never copy passwords, tokens or session cookies into the summary; flag them for rotation if the customer pasted them.

## Process
1. Read the whole thread and extract facts with their source (customer, agent, log). Separate observed facts from agent hypotheses; label hypotheses `[ASSUMPTION]`.
2. State the symptom precisely: exact error text, where it appears, affected function, what "works" versus "fails". Replace vague words ("slow", "broken") with measurable observations or mark them `[UNKNOWN]`.
3. Quantify scope and business impact: users/sites affected, process blocked, workaround and its cost, regulatory or financial exposure, SLA time remaining.
4. Capture the environment: product/version, tenant or instance, browser/OS/device, network path, integrations involved, and whether other customers show the same symptom.
5. Build a timeline in UTC or a stated time zone: first occurrence, recent changes (releases, config, certificates, vendor changes), reports, actions taken.
6. List every troubleshooting step with its result, including negative results; mark steps that were reported but not verified.
7. Attach or reference evidence: log excerpts with timestamps, request/correlation IDs, reproduction steps and rate (for example, 3 of 5 attempts). Remove personal data from excerpts.
8. Write the exact ask for the receiving level: diagnose, fix, provide workaround, approve a data correction, or confirm a defect. Include the deadline and why.
9. Record customer communication status: what the customer was told, promised next update time, and sensitivities (executive attention, contract dispute).
10. Hand off: suggest `ticket-response` to update the customer, `bug-report` if the receiving team confirms a defect, or `problem-management` if the ticket matches a recurring pattern.

## Output format
```markdown
# Escalation: <ticket ID> – <one-line symptom>
| Field | Value |
|---|---|
| From / To | <L1 agent> → <L2 / L3 / team / vendor> |
| Priority / SLA | P<n> – <time remaining or [UNKNOWN]> |
| Customer / tier | <masked or account ID> |
| Business impact | <who, how many, what is blocked, workaround> |
| Ask | <diagnose / fix / workaround / confirm defect> by <time, reason> |

## Symptom
<exact error text, where, when, reproduction rate>
## Environment
- ...
## Timeline (<time zone>)
| Time | Event | Source |
|---|---|---|
## Already Tried
| Step | Result | Verified? |
|---|---|---|
## Evidence
- <log excerpt / correlation ID / screenshot reference>
## Hypotheses
- [ASSUMPTION] ... – supporting and contradicting evidence
## Missing Evidence
- ...
## Customer Communication
- Last told: ... Next update promised: ...
```

## Quality checklist
- [ ] The receiving team can start work without re-asking the customer for anything already provided.
- [ ] The symptom uses exact error text and observations, not the customer's paraphrase alone.
- [ ] Every tried step shows its result, and unverified steps are marked.
- [ ] Hypotheses are labeled `[ASSUMPTION]` and kept separate from facts.
- [ ] The ask and its deadline are explicit.
- [ ] Personal data is masked and no secrets appear in the summary.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Forwarding the raw thread with "please check". Summarize; the thread is an attachment, not the handover.
- Dropping negative results. "Cache clearing did not help" saves the next level an hour.
- Escalating without the environment and time of failure, which makes log correlation impossible.
- Promising the customer a fix time on behalf of the receiving team. Promise the next update time instead.

## Example
Input: 30-message thread; users get "session expired" every few minutes on the portal since Tuesday; caches cleared, passwords reset.

Weak: "Customer has login issues, tried everything, please urgent."

Strong excerpt:
- Symptom: "Your session has expired" after 2-5 min of activity, all browsers, about 60 users of tenant ACME-EU [ASSUMPTION: all users of that tenant].
- Timeline: first report Tuesday 09:10 CET; release 4.12 deployed Monday 22:00 CET (source: release calendar).
- Already tried: browser cache clear – no change (verified with 2 users); password reset – no change.
- Hypothesis [ASSUMPTION]: session token lifetime or load balancer stickiness changed in 4.12.
- Ask: L3 to check session configuration diff between 4.11 and 4.12 by 15:00 CET (SLA breach at 17:00).
