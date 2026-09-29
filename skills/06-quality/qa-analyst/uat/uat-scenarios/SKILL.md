---
name: uat-scenarios
description: "Writes end-to-end user acceptance scenarios in business language, built from real roles, business events and outcomes rather than screens and clicks, each with realistic data, business-verifiable checkpoints and pass criteria. Use when business users need scenarios to execute in UAT, when requirements or processes must be turned into acceptance walkthroughs, or when existing UAT scripts read like technical test cases."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 06-quality
  role: qa-analyst
  area: uat
  title: "Write UAT scenarios"
  related: "uat-plan, test-scenarios-from-requirements, to-be-process, acceptance-criteria, test-data-design"
  prompt: "Write UAT scenarios for the returns process: store staff, warehouse and finance will test the new returns flow end to end."
---

# Write UAT Scenarios

## Purpose
Give business users scenarios that mirror how they actually work, so acceptance tests prove the solution supports real business outcomes across roles and systems, and results can be judged without technical knowledge.

## When to use
- A UAT window is planned and business testers need something concrete to execute.
- Requirements, user stories or a to-be process exist and must become acceptance walkthroughs.
- Current UAT scripts are click-level test cases that business users find hard to follow or judge.

## When not to use
- You need to organize the UAT itself (people, schedule, sign-off). Use `uat-plan`.
- You need detailed, step-level system test cases for QA. Use `test-case-writing`.
- You need broad functional scenario coverage for system test. Use `test-scenarios-from-requirements`.

## Inputs
Required:
- The business process, requirements or stories in scope.
- The roles that take part.

Optional, improves quality:
- To-be process model, business rules, known exceptions, real-life volumes and calendar events (month end, campaigns).
- Available test data and accounts per role.

If the process or roles are missing, ask for them, one focused question at a time. Mark any business rule you infer as `[ASSUMPTION]` and confirm it with the process owner.

## Process
1. List the business events that start the process (customer returns an item, month-end close) and the business outcome each must produce.
2. For each event, write a main scenario as a story across roles and systems, from trigger to business outcome, in the users' own vocabulary.
3. Add business variants that matter in real operations: exceptions (damaged item, missing receipt), approvals and rejections, cancellations, corrections, period boundaries, high-volume days.
4. Add role and permission checks where acceptance depends on them (a store clerk cannot approve refunds above the limit).
5. Define realistic data per scenario (customer type, product, amount, dates) using masked or synthetic records; reference named datasets rather than real people.
6. Write checkpoints the business user can verify themselves: document produced, balance changed, status visible, notification received, report figure. Avoid checks that need database or log access.
7. State the pass criterion per scenario and what counts as a business-blocking failure versus a cosmetic issue.
8. Map each scenario to the requirements or process steps it covers and flag uncovered steps as gaps.
9. Order scenarios by business criticality and dependency (a return needs an existing sale) and group them per role and day for execution.
10. If the user continues, suggest `uat-plan` to schedule execution, `test-data-design` for the datasets, or `acceptance-criteria` when a gap reveals missing rules.

## Output format
```markdown
# UAT Scenarios: <process/release>
| ID | Scenario | Roles | Priority | Covers |
|---|---|---|---|---|

## UAT-<nn>: <business-language title>
- Business event: ...
- Roles: ...
- Preconditions and data: <dataset name, key values>
- Walkthrough:
  1. <role> <does business action> → checkpoint: <what they should see/receive>
  2. ...
- Expected business outcome: ...
- Pass criterion: ...
- Result: Pass / Fail / Blocked — notes: ...

## Coverage Gaps
- ...
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every scenario starts from a business event and ends in a verifiable business outcome.
- [ ] Wording is business language; no field IDs, endpoints or technical jargon.
- [ ] Checkpoints can be verified by the business user without technical access.
- [ ] Exceptions, approvals/rejections and period boundaries are covered, not only the happy path.
- [ ] Data is realistic and masked or synthetic; no real personal data.
- [ ] Every in-scope requirement or process step maps to a scenario, or is listed as a gap.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing screen-by-screen scripts. Business users then test the UI, not whether their work gets done; describe business actions and outcomes.
- Only happy paths. Real acceptance problems live in exceptions and corrections.
- Scenarios that stop at a single system. Follow the outcome to the downstream role (warehouse, finance, reporting).

## Example
Input: returns flow; roles: store staff, warehouse, finance.

Weak: "Open Returns screen, enter order no, click Save, verify success message."

Strong excerpt:
- UAT-03: Customer returns a damaged item bought with a gift card, without a receipt.
- Walkthrough: store staff finds the sale by card → checkpoint: sale and item listed; warehouse receives item as "damaged" → checkpoint: not added to sellable stock; finance → checkpoint: refund issued to a new gift card, amount matches the sale.
- Pass criterion: customer receives correct credit and stock stays accurate. `[ASSUMPTION]` no-receipt returns are allowed with card lookup — confirm with the process owner.
