---
description: "Writes a Functional Requirements Document that specifies system behavior per function: actors and permissions, triggers, inputs with validations, processing and business rules, outputs, states, error handling and interfaces, each requirement uniquely identified, testable and traced to a business need. Use when business requirements are agreed and development or a vendor needs an unambiguous behavioral specification, or when asked to 'write the FRD'."
related: "brd-writing, use-case-spec, business-rules-catalog, nfr-specification, traceability-matrix"
prompt: "Based on this BRD, write the FRD for the supplier self-registration and document verification functions."
---

# Write a Functional Requirements Document

## Purpose
Specify what the system must do, precisely enough that developers can build it and testers can verify it without guessing, while staying traceable to the business requirements it fulfills.

## When to use
- Business requirements are agreed and must be translated into system behavior.
- A vendor, outsourced team or package configuration needs a contractual functional baseline.
- Several teams implement parts of one capability and need one behavioral reference.

## When not to use
- The business need and objectives are not yet agreed. Use `brd-writing`.
- A full ISO/IEC/IEEE 29148 style system specification is required. Use `srs-writing`.
- The team works in small increments from backlog items. Use `user-story` with `acceptance-criteria`.

## Inputs
Required:
- The business requirements (BRD, feature brief or equivalent) and the functions in scope.

Optional, improves quality:
- Process models, business rules, data model, screen sketches, interface descriptions, existing system behavior.
- Numbering conventions and the organization's FRD template.

If business requirements are missing, ask for them or for a description of the functions; do not derive behavior from a solution idea alone. Ask at most 5 blocking questions at a time.

## Process
1. List the functions in scope as verb + object ("Register supplier", "Verify document") and map each to the business requirements it serves.
2. Define actors and roles, and a permission matrix: which role can view, create, change, approve, delete per function.
3. For each function specify: trigger, preconditions, main behavior, alternate behavior, postconditions (success and failure).
4. Specify inputs: fields, type, format, mandatory/optional, default, validation rule and the exact error behavior. Reference the data dictionary instead of redefining entities.
5. Specify processing: calculations, rule references (BR-IDs), state changes, idempotency, and what happens on duplicates or concurrent edits.
6. Specify outputs: screens or messages, documents, notifications (recipient, trigger, content), records written, audit entries.
7. Specify interfaces touched: system, direction, data, timing, and behavior when the other system is unavailable.
8. Write each requirement as "The system shall ..." with a unique ID, one behavior per statement, a priority and a source link. Avoid vague terms ("user-friendly", "fast", "etc.").
9. Add the relevant NFRs by reference (performance, security, accessibility) rather than mixing them into functional statements.
10. Mark every gap `[TBD]` and every interpretation `[ASSUMPTION]`; collect them in open questions with an owner.
11. Build the traceability table: business requirement → functional requirements → (later) test cases.
12. If the goal continues, suggest `use-case-spec` for complex flows, `nfr-specification` for quality attributes, or `traceability-matrix` to link tests.

## Output format
```markdown
# Functional Requirements Document: <system / release>
Version: <x.y> · Status: Draft · Based on: <BRD id/version>

## 1. Scope and Functions
| Function | Description | Business requirement(s) |
## 2. Actors and Permissions
| Function | Role A | Role B | ... |  (V/C/U/A/D)
## 3. Functional Requirements
### F-01 <function>
- Trigger / Preconditions / Postconditions
| ID | Requirement ("The system shall…") | Rule ref | Priority | Source |
- Inputs and validations: | Field | Type | Mandatory | Validation | Error behavior |
- Outputs and notifications
- Errors and exceptions
## 4. Interfaces
## 5. Referenced NFRs
## 6. Traceability (BR → FR)
## 7. Assumptions and Open Questions
```

## Quality checklist
- [ ] Every functional requirement has a unique ID, one behavior, and a source link.
- [ ] Every function has preconditions, postconditions and error behavior.
- [ ] Every input field has a validation rule and a defined error behavior.
- [ ] Permissions are defined per role and function.
- [ ] No vague terms remain; each statement is testable.
- [ ] Every business requirement in scope maps to at least one functional requirement.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Describing only the happy path. Most defects come from rejection, timeout, duplicate and partial-failure cases; specify them.
- Embedding UI design ("a blue button on the right"). Specify behavior and information; leave layout to screen requirements.
- Compound requirements ("shall validate and save and notify"). Split them so each can be tested and traced.

## Example
Input: BR-04 "Prevent supplier activation until mandatory documents are verified."

Excerpt of output:
| ID | Requirement | Rule ref | Priority | Source |
|---|---|---|---|---|
| FR-4.1 | The system shall keep a supplier in status "Pending verification" while any mandatory document is missing or unverified. | BR-17 | Must | BR-04 |
| FR-4.2 | The system shall reject an activation request for a supplier in "Pending verification" and show the list of unverified documents. | BR-17 | Must | BR-04 |
| FR-4.3 | The system shall record who verified each document and when. | – | Must | BR-04, audit |

Open question: Which documents are mandatory per supplier type? `[TBD]` – Procurement.
