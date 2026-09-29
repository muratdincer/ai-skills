---
name: regression-selection
description: "Selects a regression test set for a specific change by analyzing what changed, its direct and indirect impact (shared code, data, integrations, configuration), risk and recent defect history, then tiers tests into must-run, should-run and optional with explicit residual risk. Use when a release, hotfix or merge needs regression testing but the full suite is too slow or expensive, or when someone asks what must be retested after a change."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 06-quality
  role: qa-analyst
  area: execution
  title: "Select regression tests"
  related: "impact-analysis, risk-based-testing, test-summary-report, automation-candidate-selection, test-gap-finder"
  prompt: "We changed the discount calculation service and upgraded the PDF library. Which regression tests must we run before tomorrow's hotfix?"
---

# Select Regression Tests

## Purpose
Choose the smallest regression set that gives justified confidence for a given change, and make the risk of what is not run visible to the people deciding to ship.

## When to use
- A hotfix, patch or feature release must be retested in limited time.
- The full regression suite takes longer than the release window allows.
- A shared component, library or configuration changed and its reach is unclear.

## When not to use
- You need to decide what is worth automating long term. Use `automation-candidate-selection`.
- You need test prioritization for a whole product, not a specific change. Use `risk-based-testing`.
- You need to find missing tests in code. Use `test-gap-finder`.

## Inputs
Required:
- A description of the change (stories, commits, pull requests, configuration or dependency changes).

Optional, improves quality:
- Existing test inventory with areas/tags, automation status and duration.
- Architecture or dependency map, recent defect and incident history, usage analytics.
- Time and environment budget for testing.

If the change description is missing, ask for it. If no test inventory exists, output test areas and scenario names to cover instead of test IDs.

## Process
1. List each change item and classify it: code logic, shared library/dependency, data/schema, configuration/feature flag, infrastructure, UI only.
2. Map direct impact: features, APIs, screens and batch jobs that call the changed code.
3. Map indirect impact: consumers of shared components, data read or written by the change, integrations and downstream reports, security and permission paths. Mark inferred links `[ASSUMPTION]`.
4. Add risk modifiers: business criticality, recent defects or incidents in the area, change complexity, first release of a dependency upgrade, low existing coverage.
5. Select tests in tiers: Tier 1 must-run (verify the change itself plus high-risk direct impact), Tier 2 should-run (indirect impact, high-traffic journeys), Tier 3 optional (remaining related areas).
6. Always include a smoke set of critical business journeys regardless of the change.
7. Prefer automated tests where they exist; list manual tests only where automation does not cover the risk.
8. Estimate effort per tier from given durations, or mark `[UNKNOWN]`; fit the plan to the time budget and state what is cut.
9. Write the residual risk: areas intentionally not retested and why the risk is acceptable or needs sign-off.
10. Define the trigger to expand scope (e.g. any Tier 1 failure, defects found in indirect areas).
11. If the user continues, suggest `test-summary-report` to report results or `automation-candidate-selection` when manual Tier 1 tests recur.

## Output format
```markdown
# Regression Selection: <release / change>
## Change Items
| Change | Type | Direct impact | Indirect impact | Risk modifiers |
|---|---|---|---|---|

## Selected Tests
| Tier | Test / area | Reason (change link) | Auto/Manual | Est. effort |
|---|---|---|---|---|

## Always-run Smoke Set
- ...

## Not Selected and Residual Risk
- <area>: <why not> – <risk level, sign-off needed?>

## Expansion Triggers
- ...
```

## Quality checklist
- [ ] Every change item leads to at least one selected test or an explicit "no impact" justification.
- [ ] Indirect impacts through shared code, data and integrations are considered.
- [ ] Tiers fit the stated time budget, or the gap is stated.
- [ ] Residual risk names concrete areas, not "everything else".
- [ ] Inferred dependencies are marked `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Testing only the changed feature. Regressions usually appear in consumers of shared code and data.
- Treating dependency upgrades as low risk. Library upgrades change behavior in serialization, dates, PDF rendering and security defaults.
- Silently skipping tests to meet the deadline. Record the cut and make the decision owner visible.

## Example
Input: "Discount calculation service changed; PDF library upgraded; hotfix tomorrow."

Excerpt of output:
| Tier | Test / area | Reason | Auto/Manual |
|---|---|---|---|
| 1 | Discount rules suite (percentage, fixed, stacked, caps) | Direct change | Auto |
| 1 | Invoice and credit note PDF rendering, Turkish characters, multi-page | Library upgrade | Manual |
| 2 | Order refund amount after discounted purchase | Consumes discount result | Auto |
| 2 | Monthly sales report totals | Reads discounted amounts `[ASSUMPTION]` | Manual |

Residual risk: Loyalty points accrual not retested; it reads net amounts `[UNKNOWN]`; needs product owner sign-off.
