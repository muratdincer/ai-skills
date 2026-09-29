---
description: "Designs a test automation framework: test levels and their share, layered architecture (tests, business actions, page objects/API clients, drivers), test data and environment management, configuration and secrets, reporting and traceability, CI integration with parallelism and quality gates, and conventions for maintainability. Use when a team starts automation, when an existing suite is slow, brittle or unowned and needs a redesign, or when choosing a structure for UI, API and contract tests."
related: test-strategy, automation-candidate-selection, test-automation-script, pipeline-design, flaky-test-analysis
prompt: "Design a test automation framework for our web app and its REST APIs; the suite must run on every pull request in under 15 minutes."
---

# Design a Test Automation Framework

## Purpose
Define a structure in which automated tests are fast to write, cheap to maintain and trustworthy in CI, so automation scales with the product instead of collapsing under brittle UI scripts and shared data.

## When to use
- A team is starting automation or consolidating several ad-hoc suites.
- The current suite is slow, flaky or so coupled to the UI that small changes break many tests.
- A new product, platform (mobile, API-only, event-driven) or CI setup requires a fresh structure.

## When not to use
- You need the overall test approach (levels, types, environments) across the product. Use `test-strategy`.
- You need to decide which tests to automate. Use `automation-candidate-selection`.
- You need one automated test written in an existing framework. Use `test-automation-script`.

## Inputs
Required:
- System under test: type (web, mobile, API, event-driven, batch), main interfaces and tech stack.
- Team context: who writes tests (developers, automation engineers, both) and their languages.

Optional, improves quality:
- Existing suites and their pain points, CI platform constraints, feedback time targets, environments available.
- Test data sources, authentication mechanisms, external dependencies, compliance needs for reporting.

If the system or team context is missing, ask for them (one short numbered batch). Tool choices must follow the team's stack; where you propose a specific tool, give the selection criteria so the team can substitute an equivalent.

## Process
1. Set goals and constraints: feedback time per pipeline stage (for example pull request vs nightly), target flake rate, who authors tests, supported browsers/devices, and what must be reported to whom.
2. Define the test level mix: unit and component tests owned by developers, contract tests at service boundaries, API/service tests for business rules, and a thin layer of UI end-to-end journeys. State the intended proportion and which level owns which kind of risk.
3. Design the layers: test specs (intent only) → business actions/flows → page objects, screen objects or API clients → drivers and adapters. Tests never touch locators, HTTP details or waits directly.
4. Define test data management: data created per test through APIs, builders or factories with unique identifiers; seeded reference data versioned with the code; no dependency on production copies; masking for any real personal data; cleanup or disposable environments.
5. Handle dependencies and environments: which external systems are stubbed, virtualized or covered by contract tests; environment configuration by variables; secrets injected from the pipeline's secret store, never committed.
6. Specify reliability rules: condition-based waits only, test isolation and parallel safety, deterministic clock and locale, retries allowed only for evidence collection with flake tracking.
7. Define reporting and traceability: results per level with failure artifacts (screenshots, request/response, logs), tags for feature/risk/requirement IDs, trend data for duration and flake rate.
8. Integrate with CI: which subsets run on pull request, merge, nightly and pre-release; sharding and parallelism; quality gates (what blocks a merge); quarantine mechanism with owner and expiry.
9. Set conventions: folder and naming structure, test naming (behavior + expected outcome), code review rules for tests, ownership per area, definition of done for a new test.
10. Plan the rollout: a thin vertical slice (one UI journey, one API test, one contract test through the full pipeline) first, then migration of existing tests by value; list risks and decision points.
11. If the user continues, suggest `automation-candidate-selection` to fill the backlog, `test-automation-script` for the first slice, or `pipeline-design` for pipeline changes.

## Output format
```markdown
# Test Automation Framework Design: <product>
## Goals and Constraints
- Feedback time targets / flake target / authors / platforms

## Test Level Mix
| Level | Owns which risks | Owner | Runs in stage | Share |
|---|---|---|---|---|

## Architecture
<layer diagram or list: specs → actions → page objects / API clients → drivers>

## Test Data and Environments
- ...
## Dependencies (stub / virtualize / contract)
| Dependency | Approach | Reason |
|---|---|---|
## Reliability Rules
- ...
## Reporting and Traceability
- ...
## CI Integration
| Stage | Subset | Parallelism | Gate |
|---|---|---|---|
## Conventions
- ...
## Rollout Plan and Risks
- ...
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Each test level has a clear risk ownership, and UI end-to-end tests are a thin layer.
- [ ] Tests are separated from locators, protocol details and waits through the layers.
- [ ] Test data is created per test and is safe for parallel runs; personal data is masked or synthetic.
- [ ] Secrets come from the pipeline's secret store and never from the repository.
- [ ] CI stages have explicit feedback time targets and merge gates, including a time-boxed quarantine.
- [ ] Proposed tools come with selection criteria so equivalents can be substituted.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Building an "ice cream cone" suite: most checks in UI end-to-end tests. Push business rules down to API and component levels.
- Designing a framework nobody but its author understands. Keep layers thin and conventions written down; review test code like production code.
- Starting with a big-bang migration. Prove the design on one vertical slice before moving hundreds of tests.

## Example
Input: web app plus REST APIs; developers and two automation engineers; pull request pipeline must finish in 15 minutes.

Excerpt of output:
- Level mix: unit/component (developers) on every commit; contract tests for 4 service boundaries; ~150 API tests for pricing and order rules; 8 UI journeys (login, search, checkout, returns...) in parallel shards.
- CI: pull request runs unit, contract, API smoke (target under 12 minutes); merge runs full API; nightly runs UI journeys on 2 browsers. `[ASSUMPTION]` the CI platform supports 4 parallel shards.
- Data: builders create customers and products per test via internal APIs; no shared accounts.
