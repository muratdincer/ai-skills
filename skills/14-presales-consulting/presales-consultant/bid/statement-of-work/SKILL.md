---
description: Writes a statement of work (SOW) that defines objectives, in-scope and out-of-scope work, deliverables with acceptance criteria and procedure, milestones, roles and responsibilities of both parties, assumptions, dependencies, change control, and commercial references, in testable, unambiguous language. Use when a proposal is accepted and scope must be contractually fixed, when a project or phase needs a SOW under a master agreement, or when an existing SOW must be reviewed for ambiguity and scope-creep risk.
related: proposal-writing, effort-estimate-for-bid, scope-statement, acceptance-certificate, change-control
prompt: Draft a SOW for phase 1 of the customer portal project: SSO, order tracking and ERP order sync, fixed price, 4 months.
---

# Write a Statement of Work

## Purpose
Fix what will be delivered, how it will be accepted and who is responsible for what, so both parties share one enforceable understanding of scope and disputes are resolved by the document, not by memory.

## When to use
- A proposal is accepted and scope, deliverables and acceptance must be contractually agreed.
- A new project, phase or work package is ordered under an existing master agreement.
- An existing SOW must be reviewed for vague language, missing acceptance or hidden obligations.

## When not to use
- You are still persuading the client. Use `proposal-writing`.
- Internal project scope for your own team is needed without a contractual party. Use `scope-statement`.
- Formal acceptance of delivered work is being recorded. Use `acceptance-certificate`.

## Inputs
Required:
- The agreed scope basis: proposal, estimate, requirement list or discovery output.
- Commercial model (fixed price, time and materials, capped) and parties.

Optional, improves quality:
- Master agreement terms the SOW must reference (legal terms stay there).
- Estimate assumptions and exclusions; plan and milestones.
- Client's mandatory SOW template, acceptance policy, warranty expectations.

If the scope basis or commercial model is missing, ask. Do not draft legal clauses (liability, IP, termination); reference the master agreement and flag `[LEGAL REVIEW]`.

## Process
1. State background and objectives in two to four sentences, traceable to the proposal. Objectives explain intent; they are not deliverables and must not create extra obligations.
2. Define in-scope work by workstream with measurable boundaries (number of integrations, environments, user roles, languages, data volume, sites). Replace every "including but not limited to", "etc." and "as required" with a closed list.
3. Write explicit out-of-scope items, especially the ones the client might reasonably assume are included (data cleansing, third-party licences, hardware, production support after hypercare, content migration).
4. List deliverables with ID, description, format and acceptance criteria that an independent reviewer could verify. Every deliverable maps to a scope item.
5. Define the acceptance procedure: who reviews, review period, how defects are classified, what blocks acceptance, re-submission, and deemed acceptance if the client does not respond.
6. Set milestones and, if fixed price, link payment milestones to accepted deliverables. Dates are relative (e.g. "kickoff + 6 weeks") unless dates are given.
7. Write responsibilities for both parties in a RACI-style table; client responsibilities include access, environments, SMEs, decisions and turnaround times. Tie each to the consequence of delay.
8. Carry over assumptions and dependencies from the estimate verbatim; each assumption states what happens if it proves false (change request).
9. Define change control: how changes are requested, impact-assessed, approved and priced, and who can approve.
10. Add governance and reporting (meeting cadence, status reports, escalation path), key personnel if any, and references to warranty, confidentiality and data protection terms (KVKK/GDPR data processing where personal data is involved).
11. Run an ambiguity pass: flag weak words ("support", "assist", "best effort", "user-friendly", "optimize"), undefined terms and obligations without owner or measure; add a glossary for key terms. Label inferred content `[ASSUMPTION]`.
12. If the goal continues, suggest `change-control` for the change process, `acceptance-certificate` for sign-off, or `project-charter` to start delivery.

## Output format
```markdown
# Statement of Work: <project / phase>
| Field | Value |
|---|---|
| Parties | ... |
| Master agreement ref | <ref or [UNKNOWN]> |
| Commercial model | ... |
| Term | <start / end or relative> |

## 1. Background and Objectives
## 2. Scope
### 2.1 In scope (with limits)
### 2.2 Out of scope
## 3. Deliverables
| ID | Deliverable | Format | Acceptance criteria | Scope ref |
## 4. Acceptance Procedure
## 5. Milestones and Payment
| Milestone | Deliverables | Target | Payment trigger |
## 6. Responsibilities
| Activity | Supplier | Client | Consequence of delay |
## 7. Assumptions and Dependencies
| ID | Assumption | If false |
## 8. Change Control
## 9. Governance and Reporting
## 10. Other Terms (references to master agreement) [LEGAL REVIEW]
## 11. Glossary
## Open Points
```

## Quality checklist
- [ ] Every deliverable has verifiable acceptance criteria and maps to a scope item.
- [ ] Scope has measurable limits; no "etc.", "including but not limited to" or "as required".
- [ ] Out-of-scope lists the items the client is most likely to assume are included.
- [ ] Client responsibilities have turnaround times and delay consequences.
- [ ] Assumptions match the estimate and state what happens if false.
- [ ] No legal clauses drafted; they reference the master agreement and are flagged for review.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Deliverables described as activities ("support UAT"). Define an output and how it is accepted, or cap the effort.
- No deemed-acceptance clause. Without it, milestones and payments can stall indefinitely.
- Assumptions left in the proposal only. They protect nobody unless written into the SOW.

## Example
Input: "Phase 1: SSO, order tracking, ERP order sync. Fixed price, 4 months."

Weak: "Supplier will integrate the portal with the ERP and support testing as required."

Strong:
| ID | Deliverable | Acceptance criteria |
|---|---|---|
| D3 | ERP order sync (orders, order lines, shipment status) | All test cases in the agreed UAT set pass in the client test environment; no open Severity 1-2 defects |
- Assumption A4: Client provides a test ERP environment with documented APIs by kickoff + 4 weeks. If false: change request for schedule and effort.
