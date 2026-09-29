---
name: acceptance-certificate
description: "Prepares a deliverable acceptance certificate that records what was delivered, the agreed acceptance criteria and the evidence for each, open defects and accepted deviations, conditions for conditional acceptance, and sign-offs from authorized parties. Use when a deliverable, milestone or phase must be formally accepted by a client, sponsor or business owner, before a milestone payment, or when a vendor delivery must be accepted or rejected on record."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: project-manager
  area: closure
  title: "Prepare deliverable acceptance"
  related: "acceptance-criteria, uat-plan, statement-of-work, project-closure-report, change-control"
  prompt: "Prepare the acceptance certificate for milestone 2 (reporting module). UAT is done with 3 minor defects open; the client wants to sign conditionally."
---

# Prepare Deliverable Acceptance

## Purpose
Create an unambiguous, signed record that a specific deliverable meets its agreed acceptance criteria, or under which conditions it is accepted, so that payment, warranty and handover rest on a clear, auditable decision.

## When to use
- A deliverable, milestone or phase is complete and needs formal acceptance.
- A contract ties payment or warranty start to acceptance.
- A client wants to accept with conditions, or reject, and this must be recorded.

## When not to use
- Defining the acceptance criteria themselves. Use `acceptance-criteria` or the SOW via `statement-of-work`.
- Planning or running user acceptance testing. Use `uat-plan`.
- Closing the whole project. Use `project-closure-report`.

## Inputs
Required:
- The deliverable (name, version, scope) and the agreed acceptance criteria or their source (SOW, contract, requirements).
- Evidence of fulfilment (test results, UAT sign-off, review records, demos).

Optional, improves quality:
- Open defect list, deviations or waivers, contract clauses on acceptance periods and deemed acceptance.
- Names and roles of authorized signatories.

If the acceptance criteria or evidence are missing, ask for them. Never mark a criterion met without evidence.

## Process
1. Identify the deliverable precisely: name, version or build, delivery date, scope reference, and what is explicitly excluded.
2. List every agreed acceptance criterion from the source, without rewording its meaning.
3. Map evidence to each criterion and record the result: met, met with deviation, not met, not tested. Cite the evidence reference.
4. List open defects with severity and agreed fix dates; check them against the contract's acceptance thresholds (e.g. no open critical or high defects).
5. Record deviations and waivers that the accepting party knowingly accepts, each with justification and who approved.
6. Determine the recommended decision: accepted, conditionally accepted (with conditions, owners and deadlines), or rejected (with reasons tied to criteria).
7. Check contractual mechanics: acceptance period, deemed-acceptance clauses, effect on payment and warranty start; mark unknowns `[TBD – check contract]`.
8. Verify signatories have the authority to accept; if unknown, mark `[ASSUMPTION]` and list it as an open question.
9. Produce the certificate with sign-off lines for both parties and distribution.
10. If the user's goal continues, suggest `change-control` if conditions change scope, or `project-closure-report` once all deliverables are accepted.

## Output format
```markdown
# Acceptance Certificate: <deliverable> – <version>
| Field | Value |
|---|---|
| Project / contract ref | <...> |
| Deliverable and scope ref | <...> |
| Delivered on | <date> |
| Excluded from this acceptance | <...> |
| Decision | Accepted / Conditionally accepted / Rejected |

## Acceptance Criteria and Evidence
| # | Criterion (source ref) | Result | Evidence |
## Open Defects
| ID | Severity | Description | Fix by | Blocks acceptance? |
## Accepted Deviations / Waivers
| Deviation | Justification | Approved by |
## Conditions (if conditional)
| Condition | Owner | Deadline | Consequence if not met |
## Contractual Effects
- Payment milestone: ... | Warranty start: ... | Acceptance period: ...
## Sign-off
| Party | Name | Role | Signature | Date |
```

## Quality checklist
- [ ] Every agreed criterion appears with a result and an evidence reference.
- [ ] The deliverable version and exclusions are unambiguous.
- [ ] Conditions have owners, deadlines and consequences.
- [ ] Open defects are checked against contractual thresholds.
- [ ] Signatories' authority is confirmed or flagged.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Signing "accepted" with vague open points; they become disputes. Use conditional acceptance with explicit conditions.
- Adding new criteria at acceptance time. New expectations go through `change-control`.
- Missing deemed-acceptance deadlines in the contract, which accept the deliverable by default.

## Example
Input: "Milestone 2 reporting module v1.4, UAT passed except 3 minor defects; client wants conditional sign-off."

Excerpt of output:
- Decision: Conditionally accepted.
- Criterion 4 "Monthly sales report matches ledger totals" – Met – UAT case R-12 evidence `[ref]`.
- Condition: fix defects D-31, D-33, D-34 by `[date]` – Owner vendor lead – if not met, milestone payment 2b withheld `[confirm with contract]`.
