---
description: "Selects which tests to automate by scoring candidates on execution frequency, business risk, stability of the feature, determinism, data and environment control, and build/maintenance cost, then placing each at the cheapest reliable test level and returning a ranked backlog with a rough payback estimate. Use when a team asks what to automate next, has a large manual regression suite, needs to justify automation investment, or wants to stop automating low-value UI tests."
related: automation-framework-design, test-automation-script, regression-selection, risk-based-testing, flaky-test-analysis
prompt: "We have 350 manual regression cases. Which ones should we automate first, and at which level?"
---

# Select Automation Candidates

## Purpose
Spend automation effort where it pays back: frequently run, high-risk, stable and deterministic checks, placed at the lowest test level that can prove them, so the suite stays fast and maintainable instead of growing into a brittle UI layer.

## When to use
- A manual regression suite is too slow for the release cadence and the team must choose where to start.
- Automation budget or capacity must be justified to management.
- An existing automated suite is expensive to maintain and needs pruning or re-leveling.

## When not to use
- You need to design the framework the tests will run in. Use `automation-framework-design`.
- You need to pick which tests to run for a specific change. Use `regression-selection`.
- You need to write the automated test itself. Use `test-automation-script`.

## Inputs
Required:
- The candidate list (test cases, scenarios or areas) with a short description of each.

Optional, improves quality:
- Execution frequency, manual execution time, defect history per area, risk ratings.
- Planned changes to features, test levels already automated, CI constraints, team skills.

If the candidate list is missing, ask for it. When frequency or effort figures are missing, use relative ratings (High/Medium/Low) and mark them `[ASSUMPTION]`; never invent hour or cost figures.

## Process
1. Group candidates by feature area and remove duplicates or obsolete cases before scoring.
2. Screen out non-candidates: one-off checks, usability and visual judgment, exploratory work, features about to be redesigned, and flows that cannot be made deterministic.
3. Score each remaining candidate 1-3 on: frequency of execution, business risk if it breaks, feature stability (low churn), determinism (clear oracle, controllable timing), data/environment controllability, and build plus maintenance effort (inverse).
4. Compute a value score (frequency × risk) and a feasibility score (stability, determinism, controllability, effort); place each candidate in a 2×2: automate now, automate after enabling work, keep manual, drop.
5. Choose the test level for each "automate" item: unit, component/contract, API/service, or UI end-to-end. Push checks down whenever the rule can be proven below the UI; keep UI tests to a few critical user journeys.
6. Identify enabling work that blocks high-value candidates (test IDs in the UI, API seeding, stubbing an external dependency, test data reset) and list it as backlog items.
7. Estimate relative payback: manual runs saved per period against build and maintenance effort. Use the user's numbers if given; otherwise express it as High/Medium/Low with the rationale.
8. Produce a ranked automation backlog in waves (first wave = highest value and feasibility, smallest enabling work), each item with a done criterion (runs in CI, deterministic over repeated runs, owner).
9. Record what stays manual and why, so the decision is visible and revisited when conditions change.
10. If the user continues, suggest `automation-framework-design` if no suitable framework exists, `test-automation-script` for first-wave items, or `flaky-test-analysis` when existing tests are unstable.

## Output format
```markdown
# Automation Candidate Selection: <product/suite>
## Scoring Scale
- 1 = low, 3 = high (effort: 3 = low effort). Assumed values marked [ASSUMPTION].

## Scored Candidates
| ID | Candidate | Freq | Risk | Stability | Determinism | Controllability | Effort | Value | Feasibility | Decision | Level |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Automation Backlog
| Wave | Item | Level | Enabling work | Payback (H/M/L) | Done criterion |
|---|---|---|---|---|---|

## Enabling Work
- ...
## Kept Manual (with reason)
- ...
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Non-candidates (visual, exploratory, volatile, non-deterministic) were screened out with a reason.
- [ ] Every "automate" decision names the lowest test level that can prove the behavior.
- [ ] UI end-to-end tests are limited to critical journeys.
- [ ] Payback figures come from user data or are relative ratings marked `[ASSUMPTION]`.
- [ ] Each backlog item has a done criterion including stable CI execution.
- [ ] Items kept manual are listed with the reason.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Automating the manual suite one-to-one through the UI. It produces slow, brittle tests; re-level rules to API or unit tests.
- Measuring success by number of automated cases. Count risk covered and manual time removed instead.
- Automating a feature that is about to change. Wait for stability or automate at a level insulated from the change.

## Example
Input: 350 manual regression cases; weekly release; checkout, pricing and profile areas.

Excerpt of output:
- PR-014 "Discount rules for 12 customer tiers": Freq 3, Risk 3, Stability 3, Determinism 3 → automate now at API level (table-driven), not UI.
- CO-002 "Card payment happy path": automate now as one of 5 UI journeys; enabling work: payment provider sandbox stub.
- PF-031 "Profile page layout on tablets": keep manual (visual judgment).
