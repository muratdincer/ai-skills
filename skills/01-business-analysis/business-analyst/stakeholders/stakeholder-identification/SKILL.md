---
description: "Identifies everyone who affects, is affected by, or decides on an initiative, including hidden and indirect stakeholders (compliance, operations, data owners, external parties), with their role, interest and what is needed from them. Use at the start of a request, project or analysis, or when asked 'who do we need to involve?'."
related: "stakeholder-map, raci-matrix, stakeholder-register, request-intake-document, communication-plan"
prompt: "Who are the stakeholders for replacing our paper-based expense approval with a digital workflow?"
---

# Identify Stakeholders

## Purpose
Produce a complete, categorized stakeholder list early, so no decision maker, affected group or veto holder surfaces late and forces rework.

## When to use
- A new request, project or analysis is starting.
- Requirements are being gathered and you need to know whom to interview.
- A change touches several departments, systems or external parties.

## When not to use
- Stakeholders are known and need prioritizing by power and interest. Use `stakeholder-map`.
- Responsibilities per activity must be assigned. Use `raci-matrix`.
- A project-management register with contact and engagement tracking is needed. Use `stakeholder-register`.

## Inputs
Required:
- A description of the initiative or request (goal and scope, even rough).

Optional, improves quality:
- Org chart or department list, affected systems, known external parties.
- Names already mentioned by the requester.

If the initiative description is missing, ask for it. Use roles, not invented names, when people are unknown.

## Process
1. Restate the initiative scope in one sentence to anchor the analysis.
2. Walk the value chain: who triggers the process, who performs each step, who consumes the output, who pays.
3. Apply the checklist of commonly missed groups: sponsor/budget owner, end users by segment, managers of end users, operations/support, IT owners of each affected system, data owners/stewards, security, legal/compliance/DPO, internal audit, finance, HR/works council (if roles or monitoring change), procurement, customers, suppliers/partners, regulators, trainers.
4. Follow the data and systems: every system and data set touched implies an owner.
5. Categorize each stakeholder: Decides, Influences, Affected, Informed; internal or external.
6. For each, write their interest (what they gain or fear) and what you need from them (approval, input, data, testing, sign-off).
7. Flag veto holders and stakeholders whose absence is a risk.
8. List gaps: roles whose person is unknown, marked `[UNKNOWN]`, with who can name them.

## Output format
```markdown
# Stakeholders: <initiative>
Scope anchor: <one sentence>

| # | Stakeholder (role / group) | Name | Internal/External | Category | Interest / concern | Needed from them | Veto? |
|---|---|---|---|---|---|---|---|
| 1 | Sponsor | [UNKNOWN] | Internal | Decides | ... | Budget, priority calls | Yes |

## Hidden or easily missed
- ...

## Unknowns to resolve
- <role> – who can name the person: ...
```

## Quality checklist
- [ ] Every affected system and data set has an owner listed.
- [ ] Compliance, security, operations and support were considered explicitly.
- [ ] External parties (customers, suppliers, regulators) were considered.
- [ ] No names were invented; unknown people are roles marked `[UNKNOWN]`.
- [ ] Each stakeholder has a concrete "needed from them".
- [ ] Veto holders are flagged.

## Common pitfalls
- Listing only the requester's department. Follow the process and data end to end.
- Treating "users" as one group. Segment them by role, channel or volume; their needs differ.
- Ignoring those who lose something (workload, control, headcount). They are often the strongest resistance.

## Example
Input: "Replace paper-based expense approval with a digital workflow."

Excerpt of output:
| # | Stakeholder | Category | Interest / concern | Needed from them | Veto? |
|---|---|---|---|---|---|
| 1 | CFO (sponsor) | Decides | Faster closing, control | Approval policy decisions | Yes |
| 2 | Employees submitting expenses | Affected | Speed of reimbursement, ease on mobile | Usability input, UAT | No |
| 3 | Internal audit | Influences | Evidence retention, segregation of duties | Control requirements | Yes |
| 4 | Payroll/ERP system owner | Influences | Integration load | Interface specification | No |
