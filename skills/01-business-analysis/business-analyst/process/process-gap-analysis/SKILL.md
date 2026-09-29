---
description: "Compares an as-is process with a to-be process step by step and lists every gap as a required change in people, process, technology, data or policy, with impact, dependencies and an owner. Use when a target process has been designed and the organization needs the change list, work packages or transition plan to get there, or when asked 'what has to change to go from as-is to to-be?'."
related: "as-is-process, to-be-process, impact-analysis, fit-gap-analysis, raci-matrix"
prompt: "Here are the as-is and to-be versions of our invoice approval process. Give me the gap analysis and what has to change."
---

# Analyze As-Is vs To-Be Gaps

## Purpose
Turn the difference between the current and target process into a concrete, owned change list so the transition can be planned, estimated and tracked. Without it, a to-be model stays a drawing.

## When to use
- An as-is and a to-be process both exist and the transition must be planned.
- A process redesign must be broken into work packages across IT, operations, HR and compliance.
- Stakeholders need to see what changes for their role before sign-off.

## When not to use
- Checking whether a packaged product covers requirements. Use `fit-gap-analysis`.
- Finding missing content in a requirements document. Use `requirements-gap-analysis`.
- Assessing the ripple effect of one change on existing systems. Use `impact-analysis`.

## Inputs
Required:
- The as-is process (steps, actors, systems).
- The to-be process (steps, actors, systems).

Optional, improves quality:
- Pain points and KPIs of the as-is; target KPIs of the to-be.
- Organization chart, system landscape, applicable policies and regulations.
- Constraints: budget envelope, deadline, freeze periods.

If one of the two processes is missing, ask for it or offer `as-is-process` / `to-be-process` first. Do not invent the missing side.

## Process
1. Align both processes to a common step list: map each as-is step to its to-be counterpart and mark it Unchanged, Changed, Removed, New or Merged.
2. For every non-Unchanged step, describe the gap as "from X to Y" in one line; avoid solution design beyond what the to-be states.
3. Classify each gap by dimension: People (roles, skills, headcount), Process (steps, rules, controls, SLAs), Technology (systems, integrations, automation), Data (new fields, quality, migration), Policy/Compliance (approvals, segregation of duties, KVKK/GDPR).
4. Derive the required change for each gap: what must be built, bought, trained, rewritten or retired.
5. Check control impact: removed approvals, changed segregation of duties or audit trails need explicit compliance review.
6. Rate each change by impact (High/Medium/Low) and complexity (High/Medium/Low) with a one-line justification. No monetary figures unless given.
7. Identify dependencies between changes (e.g. training depends on the system change, data migration before go-live).
8. Group changes into work packages and propose a sequence (quick wins, prerequisites, big-bang vs phased).
9. Assign an owner role per work package and list open questions and assumptions; label every inferred gap `[ASSUMPTION]`.
10. If the user wants to continue, suggest `impact-analysis` for affected systems and reports, `raci-matrix` for ownership of the transition or `cost-benefit-analysis` for the business case.

## Output format
```markdown
# Process Gap Analysis: <process>
As-is source: <doc/version> · To-be source: <doc/version>

## Step Alignment
| As-is step | To-be step | Status (Unchanged/Changed/Removed/New/Merged) |
|---|---|---|

## Gap and Change List
| # | Gap (from → to) | Dimension | Required change | Impact | Complexity | Depends on | Owner role |
|---|---|---|---|---|---|---|---|

## Control and Compliance Impact
- ...

## Work Packages and Sequence
1. <package> – <changes> – <why this order>

## Assumptions and Open Questions
- [ASSUMPTION] ...
- Q: ... — owner: ...
```

## Quality checklist
- [ ] Every as-is and to-be step appears in the alignment table; nothing is silently dropped.
- [ ] Each gap names a dimension and a concrete required change, not "improve X".
- [ ] Removed or changed controls are called out for compliance review.
- [ ] Dependencies are reflected in the proposed sequence.
- [ ] People-side changes (roles, training, communication) are present, not only IT work.
- [ ] Inferred gaps and ratings are labeled `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Listing only system changes. Most process redesigns fail on roles, training and incentives; cover the People dimension.
- Treating removed steps as free. Removing a manual check may remove a control; confirm with audit or compliance.
- Mixing gap analysis with a new to-be design. If you disagree with the to-be, raise it as an open question.

## Example
Input: As-is: invoices arrive by email, AP clerk keys them in, manager approves by email. To-be: invoices via e-invoice integration, automatic 3-way match, exceptions to manager in the ERP.

Excerpt of output:
| # | Gap (from → to) | Dimension | Required change | Impact | Complexity | Owner role |
|---|---|---|---|---|---|---|
| 1 | Manual keying → e-invoice intake | Technology | Build e-invoice integration and mapping | High | High | IT integration |
| 2 | Clerk keys data → clerk handles match exceptions | People | Redefine AP clerk role, train on exception queue | High | Medium | AP manager |
| 3 | Email approval → ERP workflow | Policy | Confirm ERP approval trail satisfies audit `[ASSUMPTION]` | Medium | Low | Internal audit |
