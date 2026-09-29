---
description: "Writes a reproducible, triage-ready bug report with a precise title, environment and build, preconditions, minimal numbered steps, expected versus actual result, reproduction rate, evidence, impact and a proposed severity. Use when a tester, developer or user has found a defect and it must be logged, when an existing report is vague or cannot be reproduced, or when someone pastes observations and asks to turn them into a bug ticket."
related: bug-triage, bug-reproduction, log-analysis, test-case-writing, ticket-triage
prompt: "Write a bug report: on the iOS app, after changing the delivery address at checkout, the shipping fee still uses the old city. Happens most of the time, build 4.12.0 on staging."
---

# Write a Bug Report

## Purpose
Give developers and triagers everything needed to reproduce, understand and prioritize a defect in one read, without a round-trip to the reporter.

## When to use
- A defect was observed during testing, UAT or production use and must be logged.
- An existing ticket says "doesn't work" or was closed as "cannot reproduce".
- Raw notes, screenshots or chat messages need to become a structured ticket.

## When not to use
- You are still investigating the cause in code. Use `bug-reproduction` or `debugging-hypotheses`.
- You need to rank or assign many existing bugs. Use `bug-triage`.
- It is a user support request without confirmed defect. Use `ticket-triage`.

## Inputs
Required:
- What was done and what happened (observation), in any form.

Optional, improves quality:
- Environment, build/version, device/browser, account or role used, time of occurrence.
- Screenshots, recordings, logs, request IDs, correlation IDs.
- Requirement or acceptance criterion that defines the expected behavior.

If the observation is missing, ask for it. Ask at most three focused questions for blocking gaps (environment, exact steps, expected behavior); everything else becomes `[UNKNOWN]`.

## Process
1. Separate what the reporter observed from what they interpret or guess about the cause; keep guesses out of steps and put them under "Notes".
2. Write the title as "<component>: <what goes wrong> when <condition>". It must be specific enough to spot duplicates.
3. Record the environment: environment name, build/version, platform, device/browser, locale, feature flags, user role. Never include passwords or tokens.
4. State preconditions and data (masked): account state, basket content, configuration.
5. Reduce steps to the minimal numbered sequence that reproduces the problem; one action per step.
6. Write the expected result with its source (requirement, criterion, previous behavior, or `[ASSUMPTION]` if only common sense).
7. Write the actual result factually: exact message, wrong value, HTTP status, time. Include the reproduction rate (e.g. 4/5 attempts).
8. Attach or reference evidence: screenshots with the defect area highlighted, log excerpt with timestamps, request/correlation IDs. Mask personal data.
9. Describe impact: who is affected, how often, workaround availability, data or money risk.
10. Propose severity (technical impact) and leave priority for triage unless the team process says otherwise; justify in one line.
11. Check for likely duplicates or related tickets if the user can supply them; if the user continues, suggest `bug-triage` for prioritization or `bug-reproduction` when the rate is low.

## Output format
```markdown
**Title:** <component>: <symptom> when <condition>

| Field | Value |
|---|---|
| Environment / build | <env, version> |
| Platform | <OS, device, browser, locale> |
| Role / account | <role, masked account> |
| Reproduction rate | <n/m> |
| Severity (proposed) | <Critical/Major/Minor/Trivial> – <reason> |
| Related requirement | <ID or [UNKNOWN]> |

**Preconditions:** ...
**Steps to reproduce:**
1. ...
**Expected result:** ... (source: ...)
**Actual result:** ...
**Evidence:** <screenshot / log / request ID>
**Impact and workaround:** ...
**Notes (reporter's hypotheses, not verified):** ...
```

## Quality checklist
- [ ] The title alone tells what is wrong and under which condition.
- [ ] Steps are minimal, numbered, and start from a stated precondition.
- [ ] Expected and actual results are specific and the expected result cites its source.
- [ ] Environment, build and reproduction rate are present or marked `[UNKNOWN]`.
- [ ] Evidence contains no unmasked personal data, passwords or tokens.
- [ ] Guesses about cause are separated from observed facts.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- One ticket for several problems. Split them; each defect gets its own lifecycle.
- Severity inflated to get attention. Tie it to impact, and let triage set priority.
- Steps that start from "log in and go to the page" but omit the data state that actually triggers the bug.

## Example
Input: "iOS app: after changing delivery address at checkout, shipping fee still uses old city. Mostly happens, 4.12.0, staging."

Weak: "Shipping fee wrong on iOS. Please fix ASAP."

Strong (excerpt):
- Title: Checkout (iOS): shipping fee not recalculated when delivery address is changed to another city
- Reproduction rate: `[UNKNOWN: n/m]`, reporter says "most of the time"
- Steps: 1. Add one item to basket with address in Ankara. 2. Open checkout; note fee. 3. Change delivery address to an İzmir address. 4. Return to order summary.
- Expected: Fee recalculated for İzmir (source: `[UNKNOWN: pricing rule ID]`). Actual: Fee still shows Ankara amount; order can be placed with it.
- Impact: Possible revenue loss or overcharge on every cross-city address change; workaround: remove and re-add item.
