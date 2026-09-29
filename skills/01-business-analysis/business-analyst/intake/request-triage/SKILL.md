---
description: "Classifies one or more incoming business requests by type, urgency, value, effort class and risk, detects duplicates, and routes each to the right path (fast track, analysis, feasibility, project, support, reject). Use when a queue of new requests must be sorted, at a demand review, or when asked 'where should these requests go and what comes first?'."
related: "request-intake-document, request-completeness-check, ticket-triage, backlog-prioritization, change-request-analysis"
prompt: "Triage these 8 requests from this week's inbox and tell me which go to analysis, which are support tickets and which we should reject."
---

# Triage Incoming Requests

## Purpose
Turn an unsorted inflow of requests into a routed, justified list, so capacity goes to the right work and requesters get a fast, explainable answer.

## When to use
- A batch of new requests accumulated in an inbox, form or demand board.
- Before a weekly demand or intake review meeting.
- Requests of very different sizes and types arrive through the same channel.

## When not to use
- A single request needs to be written up properly first. Use `request-intake-document`.
- Items are incidents or service desk tickets. Use `ticket-triage`.
- Refined backlog items need ranking. Use `backlog-prioritization`.

## Inputs
Required:
- The requests (text, list or intake documents).

Optional, improves quality:
- Routing options that exist in the organization (e.g., small change path, project gate, service desk).
- Current strategic goals or OKRs, capacity constraints, freeze periods.
- Triage criteria or scoring model already in use.

If no requests are given, ask for them. If routing options are unknown, use the default set below and say so.

## Process
1. Normalize each request into one line: requester, need, stated date. Assign a temporary ID if none exists.
2. Detect duplicates and overlaps; merge or link them and note the requesters involved.
3. Classify type: new feature, change to existing, report/data, integration, regulatory/compliance, technical/infrastructure, defect/incident (misrouted), question/access request (misrouted).
4. Rate urgency with a reason tied to an event: regulatory date, contractual date, revenue/cost impact per period, operational risk. "ASAP" alone is Low evidence.
5. Rate value (H/M/L) against stated goals; rate effort class as T-shirt size (XS-XL) only as a rough band, marked `[ASSUMPTION]`.
6. Flag risk markers: personal data, financial calculation, external parties, multiple systems, irreversible changes.
7. Check readiness: enough information to route? If not, route to "clarify" with the 2-3 blocking questions.
8. Route each request. Default paths: Fast track (XS/S, low risk, clear), Analysis, Feasibility/estimate, Project/portfolio gate, Service desk/support, Clarify, Reject/park (with a respectful reason).
9. Suggest an order for the routed items using urgency and value; show the reasoning, not a hidden score.
10. Draft the one-line response to each requester.

## Output format
```markdown
# Request Triage – <date / batch name>

| ID | Request (one line) | Type | Urgency | Value | Effort band | Risk flags | Route | Reason |
|---|---|---|---|---|---|---|---|---|
| R1 | ... | ... | H – regulatory date | M | S [ASSUMPTION] | Personal data | Analysis | ... |

## Duplicates / merged
- R3 + R6: ...

## Needs clarification
- R4: <blocking questions>

## Suggested order
1. R1 – ...

## Messages to requesters
- R5 (reject/park): ...
```

## Quality checklist
- [ ] Every request has exactly one route and a reason.
- [ ] Urgency ratings refer to a concrete event or impact, not the requester's tone.
- [ ] Effort bands are marked as assumptions; no hours or money invented.
- [ ] Misrouted incidents and access requests are sent to support, not analysis.
- [ ] Rejections or parked items have a respectful, specific reason.
- [ ] Duplicates are linked so no requester is forgotten.

## Common pitfalls
- Ranking by who shouts loudest or by seniority. Anchor on the stated goals and event dates.
- Sending everything to analysis. A fast-track path for small, clear, low-risk changes keeps analysts for real problems.
- Silently parking requests. Every requester should get an answer and a next step.

## Example
Input: "R1 Finance: VAT rate change must be reflected in invoices from 1 January. R2 Marketing: new dashboard 'would be nice'. R3 User can't log in to the portal."

Excerpt of output:
| ID | Type | Urgency | Value | Route | Reason |
|---|---|---|---|---|---|
| R1 | Regulatory | H – legal effective date | H | Analysis (priority) | Tax calculation, invoices, possibly reports affected |
| R2 | Report/data | L – no date | [UNKNOWN] | Clarify | Goal and decisions the dashboard supports are unstated |
| R3 | Incident (misrouted) | – | – | Service desk | Access problem, not a change request |
