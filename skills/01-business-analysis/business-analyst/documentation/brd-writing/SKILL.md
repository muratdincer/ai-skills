---
description: "Writes a Business Requirements Document that states the business problem, objectives with measurable success criteria, scope, stakeholders, high-level business requirements, business rules, constraints, assumptions and risks, independent of any solution design. Use when an initiative needs an agreed business baseline before solution or functional design, or when asked to 'write the BRD' for a project or change."
related: "request-intake-document, frd-writing, stakeholder-identification, requirements-review-checklist, requirements-sign-off"
prompt: "Write a BRD for replacing our manual supplier onboarding (email and Excel) with a self-service process; here are the workshop notes."
---

# Write a Business Requirements Document

## Purpose
Establish one agreed statement of why the initiative exists, what the business needs and how success will be judged, so solution design, estimation and sign-off rest on a shared baseline rather than on individual expectations.

## When to use
- An initiative or larger change has passed intake and needs a business baseline before design.
- Several departments have different expectations that must be reconciled in one document.
- A sponsor, portfolio board or vendor needs a solution-neutral statement of need.

## When not to use
- System behavior, screens and interfaces must be specified. Use `frd-writing` or `srs-writing`.
- The request is still raw and unqualified. Use `request-intake-document`.
- The team works from a product-level document for a feature. Use `prd-writing`.

## Inputs
Required:
- The source material: intake document, notes, workshop or interview outputs, or a description of the initiative.
- The sponsor or decision maker (role at least).

Optional, improves quality:
- Strategic goals or OKRs it supports; as-is process description; known constraints (budget band, dates, regulation).
- The organization's BRD template or mandatory sections.

If source material is missing, ask for it. If the sponsor is unknown, continue with `[UNKNOWN]` and make it the first open question. Ask at most 5 blocking questions at a time.

## Process
1. Extract from the sources: problem, drivers, goals, stakeholders, needs, rules, constraints. Label anything inferred `[ASSUMPTION]`.
2. Write the business problem or opportunity and its evidence (volumes, cost, incidents) only as given; mark missing evidence `[TBD]`.
3. Define 2-5 business objectives, each with a measurable success criterion: metric, baseline, target, date. Never invent baselines.
4. Set scope: in scope, out of scope, and future considerations. Name organizational units, processes, products and channels.
5. List stakeholders with role, interest and what is needed from them (approval, input, acceptance).
6. Describe the as-is situation briefly and the to-be business capability, without prescribing screens or technology.
7. Write high-level business requirements as "The business needs to be able to ..." statements, each with an ID, source, priority and link to an objective. Keep them solution-neutral.
8. Capture business rules, regulatory obligations (e.g., KVKK/GDPR, sector rules), data and reporting needs and quality expectations at business level.
9. Record constraints, dependencies, assumptions and risks, each with an owner where known.
10. State the transition needs: organizational change, training, data migration, parallel run.
11. Add open questions and the approval block (role, decision, date left blank).
12. If the goal continues, suggest `frd-writing` for system behavior, `requirements-review-checklist` before sign-off, or `requirements-sign-off` to obtain approvals.

## Output format
```markdown
# Business Requirements Document: <initiative>
Version: <x.y> · Status: Draft · Sponsor: <role/name or [UNKNOWN]> · Author: <role>

## 1. Executive Summary
## 2. Business Problem / Opportunity and Evidence
## 3. Objectives and Success Criteria
| ID | Objective | Metric | Baseline | Target | By |
## 4. Scope (In / Out / Future)
## 5. Stakeholders
| Stakeholder | Role | Interest | Needed from them |
## 6. As-Is Summary and To-Be Business Capability
## 7. Business Requirements
| ID | Requirement ("The business needs to be able to…") | Objective | Priority | Source |
## 8. Business Rules and Regulatory Obligations
## 9. Data, Reporting and Quality Expectations
## 10. Constraints, Dependencies, Assumptions, Risks
## 11. Transition Needs
## 12. Open Questions
## 13. Approval
| Role | Name | Decision | Date |
```

## Quality checklist
- [ ] Every business requirement traces to at least one objective, and every objective has a measurable criterion.
- [ ] No requirement prescribes a screen, technology or vendor.
- [ ] Out-of-scope items are explicit.
- [ ] Baselines, figures and dates come from the sources or are marked `[TBD]` / `[ASSUMPTION]`.
- [ ] Regulatory and data protection obligations were considered and stated or ruled out with a reason.
- [ ] Each risk and open question has an owner or is marked `[UNKNOWN]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing an FRD in disguise. If it names fields, buttons or APIs, it belongs in the functional specification.
- Objectives without a baseline. "Reduce onboarding time" is untestable; record the baseline as `[TBD]` and name who will measure it.
- Missing the "do nothing" option. State the consequence of not acting; it anchors priority.

## Example
Input: "Supplier onboarding takes weeks via email and Excel; procurement wants self-service; audit found missing tax certificates."

Excerpt of output:
| ID | Objective | Metric | Baseline | Target | By |
|---|---|---|---|---|---|
| OBJ-1 | Shorten supplier onboarding | Median days from request to active supplier | [TBD – procurement to measure] | [TBD] | [TBD] |
| OBJ-2 | Close audit finding on supplier documents | Active suppliers without valid tax certificate | Audit finding (count [TBD]) | 0 | Next audit |

BR-04: The business needs to be able to prevent a supplier from being activated until mandatory documents are verified. (OBJ-2, Must, audit report)
