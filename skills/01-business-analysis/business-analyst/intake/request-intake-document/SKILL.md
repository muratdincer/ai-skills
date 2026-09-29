---
name: request-intake-document
description: "Turns a raw business request (email, chat message, meeting note, ticket) into a structured request intake document with goal, scope, value, stakeholders, constraints and open questions. Use when someone brings a new demand, idea or change request and it must be captured before analysis, estimation or prioritization."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: intake
  title: "Create a request intake document"
  related: "request-clarification-questions, request-completeness-check, request-triage, stakeholder-identification"
  prompt: "Create an intake document for this request: Sales wants an Excel export on the customer list screen by month end for the audit."
---

# Create a Request Intake Document

## Purpose
Capture a new request in a consistent, decision-ready form so it can be triaged, estimated and prioritized without going back to the requester for basics.

## When to use
- A new feature, change, report or integration request arrives in free text.
- A request is about to enter the backlog or a demand/portfolio board.

## When not to use
- The request is already analyzed into detailed requirements. Use `brd-writing` or `frd-writing`.
- It is an incident or defect. Use `bug-report` or `ticket-triage`.

## Inputs
Required:
- The raw request text (any format).

Optional, improves quality:
- Requester name, role and department.
- Related systems, documents, previous requests.
- Organization-specific intake template or mandatory fields.

If the raw request is missing, ask for it. Do not ask for optional inputs up front; list them as open questions instead.

## Process
1. Read the raw request and separate facts stated by the requester from your own interpretation.
2. Rewrite the need as a one-sentence problem or opportunity statement: who, what problem, what impact.
3. Identify the desired outcome and how success would be measured. If absent, propose a measurable candidate and mark it `[ASSUMPTION]`.
4. Classify the request type: new feature, change to existing, report/data, integration, regulatory/compliance, technical/infrastructure, other.
5. Draft scope: in scope, out of scope, and explicitly unknown.
6. List stakeholders: requester, sponsor/decision maker, affected users, affected teams/systems.
7. Capture constraints: deadline and its reason, budget, regulation, technology, dependencies.
8. Estimate business value and urgency qualitatively (High/Medium/Low) with a one-line justification each. Never invent monetary figures.
9. List risks and assumptions.
10. Write open questions, grouped by topic and ordered by how much they block analysis.
11. Fill the output template. Mark every field not supported by the input as `[UNKNOWN]` or `[ASSUMPTION]`.

## Output format
```markdown
# Request Intake: <short title>
| Field | Value |
|---|---|
| Request ID | <if given, else TBD> |
| Date received | <date> |
| Requester | <name, role, department> |
| Sponsor / decision maker | <name or [UNKNOWN]> |
| Request type | <type> |
| Business value | <H/M/L> – <justification> |
| Urgency | <H/M/L> – <justification> |
| Target date | <date and reason, or [UNKNOWN]> |

## Problem / Opportunity
<one-sentence statement + short context>

## Desired Outcome and Success Criteria
- <measurable outcome>

## Scope
- In scope: ...
- Out of scope: ...
- Unknown: ...

## Stakeholders and Affected Parties
- ...

## Constraints and Dependencies
- ...

## Assumptions and Risks
- [ASSUMPTION] ...
- [RISK] ...

## Open Questions
1. <question> — <why it matters> — <who can answer>

## Recommended Next Step
<clarification meeting / triage / feasibility / reject with reason>
```

## Quality checklist
- [ ] The problem statement does not describe a solution.
- [ ] Every success criterion is measurable.
- [ ] Nothing is invented: unsupported fields are marked `[UNKNOWN]` or `[ASSUMPTION]`.
- [ ] Out-of-scope items are listed explicitly.
- [ ] Open questions are specific and each has a likely owner.
- [ ] The document fits on about one page.

## Common pitfalls
- Copying the requester's proposed solution as the requirement. Capture it as "suggested solution" inside context, and keep the problem separate.
- Treating "ASAP" as a deadline. Ask for the actual event or reason behind the date.
- Assigning High value to everything. Justify each rating.

## Example
Input: "Sales wants an Excel export on the customer list screen, they need it by month end for the audit."

Excerpt of output:
- Problem: Sales cannot provide customer list data to auditors in a usable format, which risks audit findings.
- Request type: Change to existing (report/data).
- Target date: End of month – external audit `[confirm exact date]`.
- Open question: Which fields and filters do the auditors require? Does the export contain personal data that needs masking?
