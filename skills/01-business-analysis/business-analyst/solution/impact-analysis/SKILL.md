---
description: "Analyzes the impact of a proposed change on processes, systems, interfaces, data, reports, users, documents, controls and tests, following direct and indirect dependencies, and rates each impact with evidence and confidence. Use when a new requirement, change request, rule change or system modification is proposed and the team must know what else it touches before estimating, approving or releasing it."
related: "change-request-analysis, traceability-matrix, process-gap-analysis, regression-selection, dependency-map"
prompt: "What is the impact of changing the customer ID from numeric to alphanumeric in our core banking system?"
---

# Analyze Change Impact

## Purpose
Make the ripple effect of a change visible before it is estimated or approved, so nothing downstream breaks silently and the effort, test scope and communication are based on the full picture.

## When to use
- A change request, new rule or regulatory change affects an existing system or process.
- A field, code list, calculation or interface is being modified.
- The test team needs to know what to regression-test.

## When not to use
- You need a recommendation to accept, defer or reject the change. Use `change-request-analysis` (it uses this analysis as input).
- You are planning the whole as-is to to-be transition. Use `process-gap-analysis`.
- You only need test selection from a known impact list. Use `regression-selection`.

## Inputs
Required:
- A precise description of the change (what changes, from what to what).

Optional, improves quality:
- Traceability matrix, system landscape or interface list, data dictionary.
- Process models, report inventory, list of downstream consumers.
- Access to people who know each system (to confirm impacts).

If the change description is vague ("improve the customer screen"), ask for the concrete change first. Missing landscape information becomes "to be confirmed" items, not guesses.

## Process
1. Restate the change as a precise delta: object, attribute or rule, old behavior, new behavior, effective date.
2. Identify the change origin point (the system, table, rule or process step where it happens).
3. Trace first-order impacts across layers: business processes and steps; user roles and screens; business rules and calculations; data (tables, fields, formats, reference data, historical data); interfaces and APIs (producers and consumers); reports, dashboards and extracts; batch jobs.
4. Trace second-order impacts: consumers of the impacted interfaces and reports, archived data, data warehouse and analytics, partner systems, documents and training material, controls and audit trails.
5. Check cross-cutting concerns: security and permissions, personal data (KVKK/GDPR), performance and volume, migration of existing records, backward compatibility and versioning.
6. For each impact record: area, item, nature of change (none / configuration / code / data / document / process), rating (High/Medium/Low), evidence, confidence (Confirmed / Likely / To be confirmed) and who can confirm.
7. Identify what is explicitly not impacted and why, to bound the scope.
8. Derive consequences: estimated effort drivers (not numbers unless given), test scope, migration needs, communication and training, release sequencing.
9. List risks and open questions, ordered by how much they could change the estimate.
10. If the user wants to continue, suggest `change-request-analysis` for the decision, `regression-selection` for the test scope or `traceability-matrix` to keep links current.

## Output format
```markdown
# Impact Analysis: <change>
Change: <old → new> · Origin: <system/process> · Effective: <date or [UNKNOWN]>

## Summary
<3-5 lines: breadth of impact, top risks, confidence level>

## Impact Register
| # | Area | Item | Nature of change | Rating | Evidence | Confidence | Confirm with |
|---|---|---|---|---|---|---|---|

## Not Impacted (and why)
- ...

## Consequences
- Effort drivers: ...
- Test scope: ...
- Data migration: ...
- Communication / training: ...

## Risks and Open Questions
1. ...
```

## Quality checklist
- [ ] The change is stated as a precise old → new delta.
- [ ] All layers were checked: process, users, rules, data, interfaces, reports, batch, documents, controls.
- [ ] Downstream consumers (second-order impacts) are listed, not just the origin system.
- [ ] Each impact has evidence and a confidence level; unconfirmed items say who can confirm.
- [ ] Personal data, security and existing-data migration were explicitly assessed.
- [ ] Inferred impacts are labeled Likely or To be confirmed, never Confirmed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Stopping at the system being changed. Most incidents come from unknown consumers: extracts, reports, partner files.
- Forgetting historical data. A new format or rule must say what happens to existing records.
- Treating "no code change" as "no impact". Configuration, documents, training and tests still change.

## Example
Input: "Customer ID changes from 10-digit numeric to 12-character alphanumeric."

Excerpt of output:
| # | Area | Item | Nature | Rating | Confidence | Confirm with |
|---|---|---|---|---|---|---|
| 1 | Data | CUSTOMER.ID column type and all foreign keys | Code + data | High | Confirmed | DBA |
| 2 | Interface | Card system daily file (fixed-width, 10 chars) | Code | High | Likely | Card system owner |
| 3 | Report | Regulatory report sorts by numeric ID | Code | Medium | To be confirmed | Regulatory reporting |
| 4 | Users | Call-center search accepts digits only | Configuration | Medium | Likely | Channel team |
