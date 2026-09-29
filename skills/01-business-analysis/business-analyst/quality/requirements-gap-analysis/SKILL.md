---
description: "Reviews a set of requirements (BRD, FRD, user stories, use cases) and detects what is missing: flows, actors and roles, edge cases, error handling, data rules, non-functional requirements and transition needs. Use when requirements look complete but have not been stress-tested, before estimation or sign-off, or when asked 'what are we missing?'."
related: "ambiguity-detection, requirements-consistency-check, requirements-review-checklist, nfr-specification, error-scenario-catalog"
prompt: "Here is our FRD for the loan application module. Find the gaps before we send it for estimation."
---

# Find Gaps in Requirements

## Purpose
Expose missing requirements before they surface as change requests, defects or rework. The output is a prioritized gap list with a concrete question or proposed requirement for each gap.

## When to use
- A requirements document or story set is about to be estimated, signed off or handed to design.
- Stakeholders say "it's all there" but only the happy path has been described.
- A new channel, role or region is being added to an existing feature.

## When not to use
- The problem is unclear wording rather than missing content. Use `ambiguity-detection`.
- Requirements contradict each other. Use `requirements-consistency-check`.
- Comparing current and target processes. Use `process-gap-analysis`.

## Inputs
Required:
- The requirements text (document, story list, use cases).

Optional, improves quality:
- Business goals or the intake document, to check coverage against objectives.
- Process model, data model, screen list or integration list.
- Applicable regulations (e.g. KVKK/GDPR, sector rules).

If the requirements text is missing, ask for it. Treat everything else as context you may lack and say so in the output.

## Process
1. Build an inventory: list actors, business objects, use cases/stories, screens, reports, integrations and stated NFRs found in the text.
2. Check goal coverage: every business goal must be served by at least one requirement; every requirement should trace to a goal.
3. Walk each flow with the CRUD+lifecycle lens: create, read, update, delete/archive, approve/reject, cancel, reopen, expire. Note missing lifecycle actions per business object.
4. Walk each flow with the exception lens: invalid input, timeouts, partial failure, duplicate submission, concurrent edit, external system down, no permission.
5. Check actors, roles and permissions: who can do what, delegation, substitution, admin/back-office, auditors, batch/system actors; also triggers, pre/postconditions, support/operations (monitoring, runbook needs) and reporting/audit trail.
6. Check data: mandatory fields, validation rules, defaults, calculations, rounding, reference data owners, retention, masking of personal data.
7. Check boundaries: volumes, limits, time zones, currencies, languages, date cut-offs, month/year end.
8. Check NFR categories: performance, availability, security, privacy, auditability, accessibility (WCAG 2.2), usability, operability, scalability.
9. Check transition needs: data migration, parallel run, training, communication, rollback, legacy decommissioning.
10. Classify each finding as ABSENT (not mentioned), WEAK (mentioned but not decidable or testable) or DEFERRED (explicitly postponed), quote the evidence, and do not polish over ambiguity. Rate impact (High/Medium/Low) by cost if found late and write a question or a candidate requirement marked `[ASSUMPTION]`.
11. If the user wants to continue, suggest `ambiguity-detection` for WEAK items, `nfr-specification` for missing quality attributes or `error-scenario-catalog` for missing exception behavior.

## Output format
```markdown
# Requirements Gap Analysis: <document / scope>
Reviewed: <document name, version> · Coverage basis: <goals / process / data model / none>

## Summary
<3-5 lines: overall completeness, top 3 risks>

## Gap List
| # | Category | Location (section/story) | Gap | Class (ABSENT/WEAK/DEFERRED) | Impact | Question or proposed requirement | Owner |
|---|---|---|---|---|---|---|---|
| G1 | Exception flow | UC-03 | No behavior when credit bureau is unreachable | ABSENT | High | What should the applicant see and can the application be saved? | Product owner |

## Coverage Check
| Goal / Area | Covered by | Status (Covered / Partial / Missing) |
|---|---|---|

## Out of Review Scope
- <what was not checked and why>
```

## Quality checklist
- [ ] Every gap points to a location or states "not present anywhere".
- [ ] Each gap has a specific question or candidate requirement, not "clarify this".
- [ ] Proposed requirements are marked `[ASSUMPTION]` until confirmed.
- [ ] NFR and transition categories were checked, not only functional flows.
- [ ] Impact ratings are justified by consequence, not by gut feel.
- [ ] Personal-data handling gaps are flagged where personal data appears.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Listing generic gaps ("security not defined") without saying what decision is missing. Name the exact decision, e.g. session timeout, role for approval.
- Inventing business rules to fill gaps. Propose them as candidates and route them to an owner.
- Stopping at the happy path of the main actor; back-office, batch and auditor roles are the usual blind spots.

## Example
Input: "Customer submits loan application online; system checks credit score; officer approves; customer is notified."

Excerpt of output:
| # | Category | Location | Gap | Class (ABSENT/WEAK/DEFERRED) | Impact | Question or proposed requirement | Owner |
|---|---|---|---|---|---|---|---|
| G1 | Exception flow | Credit check | No behavior if scoring service fails | ABSENT | High | Queue and retry, or allow manual scoring? | Credit risk |
| G2 | Lifecycle | Application | Customer cannot withdraw an application | ABSENT | Medium | [ASSUMPTION] Customer can withdraw until officer decision | Product owner |
| G3 | Role | Approval | No limit-based approval or substitute officer | WEAK | High | Which amounts need a second approver? | Operations |
