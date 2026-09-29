---
name: raci-matrix
description: "Builds a RACI matrix that assigns Responsible, Accountable, Consulted and Informed roles per activity or deliverable, then validates it (exactly one A, at least one R, no overloaded roles, no empty rows). Use when responsibilities are unclear, work falls between teams, or someone asks 'who owns what?' for a project, process or analysis activity."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: stakeholders
  title: "Build a RACI matrix"
  related: "stakeholder-identification, stakeholder-map, communication-plan, project-charter, role-definition"
  prompt: "Create a RACI for the requirements phase of our payment gateway integration: BA, PO, architect, dev lead, QA, security, vendor."
---

# Build a RACI Matrix

## Purpose
Remove ownership ambiguity by making it explicit who does, who owns, who is asked and who is told for each activity, so decisions and hand-offs do not stall.

## When to use
- A project, phase or process involves several roles and hand-offs are unclear.
- Work repeatedly falls between teams or two people think they own the same decision.
- Setting up governance for analysis, sign-off or release activities.

## When not to use
- You still need to find out who the stakeholders are. Use `stakeholder-identification`.
- You need an engagement plan by influence. Use `stakeholder-map`.
- You need job-level responsibilities rather than activity-level ones. Use `role-definition`.

## Inputs
Required:
- Activities, deliverables or decisions to cover (or the scope so they can be derived).
- Roles or teams involved.

Optional, improves quality:
- Existing governance rules, approval policies, organizational constraints.
- Known pain points ("nobody approves test data", "architecture decisions are late").

If activities are missing, derive a draft list from the scope and mark it `[ASSUMPTION]` for confirmation. If roles are missing, ask.

## Process
1. List activities at a consistent granularity: verb + object ("Approve BRD", "Define API contract"), 8-25 rows. Split activities that have different owners.
2. List roles as columns (roles, not individuals; names can be added in a legend).
3. Assign exactly one A per row: the person who answers for the outcome and can say yes/no.
4. Assign at least one R: who does the work. A and R may be the same role for small tasks.
5. Add C only where input is needed before completion (two-way); add I where notification after completion is enough (one-way).
6. Validate: rows without A or R; rows with multiple A; columns with many A (bottleneck); columns with no R or A (why is the role here?); rows with excessive C (slow decisions).
7. Highlight decisions that need escalation paths and state the escalation role.
8. List open points where ownership is disputed or unknown; do not resolve them by guessing. Any assignment inferred rather than stated by the user is marked `[ASSUMPTION]`.
9. If the goal continues, suggest `communication-plan` to turn C and I into a communication rhythm, or `stakeholder-map` if engagement strategy is still missing.

## Output format
```markdown
# RACI: <scope>
Legend: R = Responsible, A = Accountable, C = Consulted, I = Informed

| Activity / deliverable | <Role 1> | <Role 2> | <Role 3> | ... |
|---|---|---|---|---|
| ... | A/R | C | I | |

## Validation findings
- ...

## Escalation
- <decision type> → <role>

## Open ownership questions
- ...
```

## Quality checklist
- [ ] Every row has exactly one A and at least one R.
- [ ] Activities are verb + object and at a consistent level.
- [ ] No role is Accountable for so many rows that it becomes a bottleneck, or this is flagged.
- [ ] C is used sparingly and only where input is really required.
- [ ] Disputed ownership is listed as an open question, not silently assigned.
- [ ] Roles, not invented names, are used.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Making a committee Accountable. Name a single role; the committee can be Consulted.
- Marking everyone as Consulted to be polite. Each C adds a wait state.
- Building the RACI alone. Review it with the roles listed, otherwise it documents assumptions, not agreements.

## Example
Input: "Requirements phase for payment gateway integration; roles: BA, PO, architect, dev lead, QA, security, vendor."

Excerpt of output:
| Activity | BA | PO | Architect | Dev lead | QA | Security | Vendor |
|---|---|---|---|---|---|---|---|
| Elicit business requirements | R | A | C | I | I | | |
| Define API contract | C | I | A | R | C | C | C |
| Approve security requirements | C | I | C | | | A/R | I |

Validation: Architect is A for 4 of 10 rows – confirm capacity or delegate.
