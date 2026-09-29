---
description: "Designs an improved (to-be) business process from an as-is description, pain points and goals: applies redesign levers (eliminate, simplify, automate, parallelize, move decisions, add controls), shows each change against the as-is, and states expected effects, assumptions and required enablers. Use when a process must be improved, digitized or re-engineered and the target way of working must be agreed before requirements or system design."
related: "as-is-process, process-gap-analysis, bpmn-model, value-stream-map, business-rules-catalog"
prompt: "Using this as-is invoice approval process and its pain points, design a to-be process that cuts approval time in half."
---

# Design the To-Be Process

## Purpose
Define how the process should work in the future, with every change against today made explicit and justified, so stakeholders can agree on it and analysts can derive requirements and transition work from it.

## When to use
- After an as-is analysis has exposed pain points or when new goals (cost, speed, compliance, customer experience) require change.
- Before writing requirements for a new or changed system that supports the process.
- When merging or standardizing processes across units, regions or companies.

## When not to use
- The current process is not yet understood. Use `as-is-process` first.
- You need only the list of gaps and change actions. Use `process-gap-analysis`.
- You need notation-level modeling. Use `bpmn-model`.

## Inputs
Required:
- The as-is process (or a clear description of current steps).
- The improvement goals or problems to solve. If none are given, derive candidate goals from pain points and ask for confirmation.

Optional, improves quality:
- Constraints: regulation, controls, systems that cannot change, budget, organizational limits.
- Target metrics, benchmark or reference process.

## Process
1. Restate goals as measurable targets (e.g. lead time, error rate, touch count); unknown targets become `[TBD]`.
2. Tag each as-is pain point with a root cause (waiting, handoff, rework, manual data entry, unclear rule, missing information, approval layering).
3. Apply redesign levers step by step: eliminate non-value steps, combine steps done by the same role, move decisions to where information exists, parallelize independent work, automate rule-based steps, capture data once at source, add straight-through processing with exception handling, standardize variants.
4. Keep or strengthen required controls (segregation of duties, approval limits, audit trail); never remove a control without naming who accepts the risk.
5. Write the to-be steps with actor, system, input, output, rule and target time; mark each as New / Changed / Unchanged / Removed relative to as-is.
6. Define exception and escalation paths, including what happens when automation fails.
7. List enablers: system capabilities, data, roles and skills, policy changes.
8. Estimate effects per goal qualitatively or with stated calculation from given data; mark assumptions.
9. Note risks and change impact on people (roles removed or changed, training).
10. Recommend validation: walkthrough with process owner, simulation or pilot.
11. If the user wants to continue, suggest `process-gap-analysis` to turn the changes into a work list, `bpmn-model` for the diagram or `business-rules-catalog` for the new rules.

## Output format
```markdown
# To-Be Process: <name>
Owner: <role> · Goals: <targets> · Based on as-is: <version/date>

## Design Principles Applied
- <e.g. capture data once, decide at source, approve by exception>

## To-Be Steps
| # | Step | Actor | System | Rule/Decision | Target time | Change vs as-is (New/Changed/Unchanged) | Addresses pain point |
|---|---|---|---|---|---|---|---|

## Removed Steps
| As-is step | Reason for removal | Risk accepted by |
|---|---|---|

## Exceptions and Escalation
- ...

## Controls
| Control | Where | Type (preventive/detective) |
|---|---|---|

## Enablers and Dependencies
- ...

## Expected Effects
| Goal | As-is | To-be (expected) | Basis |
|---|---|---|---|

## Risks, People Impact and Open Questions
- ...
```

## Quality checklist
- [ ] Each change links to a goal or pain point.
- [ ] Removed steps and controls have an explicit risk owner.
- [ ] Exception paths exist for every automated or straight-through step.
- [ ] Expected effects show their basis; no invented savings figures.
- [ ] The design is technology-neutral unless a system is a given constraint.
- [ ] People impact (roles, training) is stated.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Automating the as-is ("paving the cow path"). Question each step before automating it.
- Designing only the happy path; exceptions usually drive most of the effort.
- Promising time savings without data. Show the calculation or mark it `[ASSUMPTION]`.

## Example
Input: As-is invoice approval with manual keying and email approvals; goal: halve lead time.

Excerpt of output:
| # | Step | Actor | System | Rule/Decision | Change vs as-is | Addresses pain point |
|---|---|---|---|---|---|---|
| 1 | Capture invoice data | System | Invoice capture/OCR `[ASSUMPTION]` | Validate supplier and PO | Changed (was manual) | Manual keying |
| 2 | Auto-approve matched invoice | System | ERP | 3-way match within tolerance `[TBD]` | New | Approval waiting |
| 3 | Approve exceptions | Budget owner | Workflow inbox | Reminder after `[TBD]` days, escalate to deputy | Changed | Phone chasing |
