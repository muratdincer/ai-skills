---
description: Writes a project scope statement that defines in-scope and out-of-scope work, deliverables with acceptance criteria, constraints, assumptions and exclusions, forming the baseline for change control. Use when a charter exists and scope must be made precise enough to plan, estimate and contract against, or when scope creep needs a clear reference.
related: project-charter, wbs, change-control, acceptance-certificate, statement-of-work
prompt: Write a scope statement for the customer self-service portal project based on this charter and the workshop notes.
---

# Write a Scope Statement

## Purpose
Create an unambiguous scope baseline so that planning, estimation, contracting and later change decisions all refer to the same definition of what will and will not be delivered.

## When to use
- After charter approval, before building the WBS and schedule.
- When stakeholders disagree about what is included.
- Before a vendor contract or internal commitment is signed.

## When not to use
- The project is not yet authorized. Use `project-charter` first.
- A contractual scope with commercial terms is needed. Use `statement-of-work`.
- Product-level scope for an iterative MVP. Use `mvp-scoping`.

## Inputs
Required:
- Charter, business case or a description of objectives and major deliverables.

Optional, improves quality:
- Requirements documents, workshop notes, existing contracts.
- Organizational constraints (standards, platforms, regulation).
- Known exclusions agreed with the sponsor.

If no objective or deliverable description exists, ask for it.

## Process
1. Extract the project objectives and restate the product/service description in 3-5 sentences.
2. List deliverables as nouns (e.g. "Migrated customer database", not "migrate"). Include project-management deliverables (training, documentation, handover).
3. For each deliverable, write acceptance criteria that are verifiable and name the acceptor.
4. Write explicit exclusions. Probe typical grey zones: data migration, legacy decommissioning, training, hypercare, integrations, reporting, localization, non-production environments.
5. Record constraints (date, budget, technology, regulatory, resource) and their source.
6. Record assumptions with an owner who can confirm them and the impact if false.
7. Define scope boundaries with interfaces: which systems, organizations and geographies are touched.
8. State how scope changes are handled and reference the change control route.
9. Mark every unsupported element `[UNKNOWN]` or `[ASSUMPTION]` and list open questions.
10. Label every inferred element `[ASSUMPTION]` and move it to assumptions or open questions. If the user's goal continues, suggest the next skill: `wbs` to decompose the deliverables, and `change-control` once the baseline is approved.

## Output format
```markdown
# Scope Statement: <project>
Version <x> | Date <date> | Baseline reference <charter id>

## Product / Service Description
## Deliverables and Acceptance Criteria
| ID | Deliverable | Acceptance criteria | Acceptor |
## In Scope
## Out of Scope (Exclusions)
## Boundaries and Interfaces
## Constraints
| Constraint | Source |
## Assumptions
| Assumption | Owner to confirm | Impact if false |
## Scope Change Handling
## Open Questions
## Approval
```

## Quality checklist
- [ ] Every deliverable is a noun and has verifiable acceptance criteria.
- [ ] Out-of-scope list covers the typical grey zones.
- [ ] Each assumption has an owner and impact.
- [ ] No vague terms ("etc.", "as needed", "user-friendly") without definition.
- [ ] Nothing invented; gaps are marked.
- [ ] Change handling references a concrete route.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Listing activities instead of deliverables, which makes WBS and acceptance impossible to trace.
- Silent exclusions. If it is not written as out of scope, stakeholders will assume it is in.
- Acceptance criteria like "works correctly". Tie them to test results, metrics or documents.

## Example
Input: "Self-service portal: customers see invoices and update contact data. Charter says go-live in 6 months."

Excerpt of output:
| D-03 | Invoice history page (last 24 months) | Displays invoices matching billing system for 50 sampled accounts | Finance lead |
- Out of scope: Online payment, invoice disputes, mobile native apps, migration of invoices older than 24 months `[confirm]`.
- Assumption: Billing system exposes an invoice API — Owner: Billing IT — Impact if false: +integration work, date at risk.
