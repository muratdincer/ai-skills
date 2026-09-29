---
name: test-strategy
description: "Writes a test strategy that defines test levels, test types, environments, tooling categories, data approach and a risk-based focus for a product, program or organization. Use when a new product or major initiative starts, when testing approach is inconsistent across teams, or when someone asks how a system should be tested overall."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 06-quality
  role: qa-analyst
  area: strategy
  title: "Write a test strategy"
  related: "test-plan, risk-based-testing, environment-strategy, automation-framework-design, nfr-specification"
  prompt: "Write a test strategy for our new customer onboarding platform: web + mobile front ends, 12 microservices, integrations with a core banking system and a KYC provider."
---

# Write a Test Strategy

## Purpose
Define the long-lived testing approach for a product or program so that every team tests at the right level, against the right risks, with shared environments, data and quality criteria. A strategy is the "how we test here"; individual test plans inherit from it.

## When to use
- A new product, platform or large program is starting and no common testing approach exists.
- Teams test inconsistently (duplicated end-to-end suites, no contract tests, manual regression bottlenecks).
- Architecture changes significantly (monolith to services, new cloud platform, new integration landscape).
- An audit or customer requires a documented test approach.

## When not to use
- You need the scope, schedule and entry/exit criteria for one release or project. Use `test-plan`.
- You only need to rank features or modules by risk. Use `risk-based-testing`.
- You are designing the automation code architecture. Use `automation-framework-design`.

## Inputs
Required:
- Description of the system: main components, users, integrations, deployment model.
- Business context: what failure would cost (money, regulation, reputation, safety).

Optional, improves quality:
- Architecture diagrams, NFRs, regulatory obligations, existing defect history.
- Team setup, release cadence, current tooling and environment landscape.
- Organizational quality policy or mandatory standards.

If the system description or business context is missing, ask for it. Everything else becomes an open question.

## Process
1. Summarize the system under test and its quality drivers (e.g. correctness of money movement, availability, data privacy, usability).
2. Identify product risk areas at a coarse level (per component, integration and quality characteristic, ISO/IEC 25010 as a checklist) and rate them H/M/L.
3. Define test levels (unit, component, contract, integration, system, end-to-end, acceptance) with owner, goal and what is explicitly not tested at each level. Aim for a test portfolio shaped by risk, not a fixed pyramid.
4. Define test types per risk: functional, regression, API/contract, performance, security, accessibility (WCAG 2.2), usability, compatibility, resilience, data migration.
5. Specify environments: purpose, data, integrations (real, stubbed, virtualized) and who controls deployments to each.
6. Define the test data approach: synthetic vs masked production, refresh, privacy constraints (KVKK/GDPR), ownership.
7. Define automation approach by level: what must be automated, where it runs in the pipeline, target feedback time. Name tool categories, not products, unless the user specified them.
8. Define defect management: severity scale, triage cadence, required fields, SLAs for fixes by severity.
9. Define quality gates and metrics: entry/exit criteria per level, coverage expectations, escaped defects, flaky rate.
10. List roles and responsibilities (developers, QA, product, ops) and how testing fits into the delivery cadence, whatever the methodology.
11. Record assumptions, constraints and open questions. Mark unsupported content `[ASSUMPTION]` or `[UNKNOWN]`.
12. If the user continues, suggest `test-plan` for a specific release or `automation-framework-design` for the automation layer.

## Output format
```markdown
# Test Strategy: <product / program>
Version: <x.y> | Owner: <name or [UNKNOWN]> | Status: Draft

## 1. Context and Quality Drivers
## 2. Risk Overview
| Area | Risk | Likelihood | Impact | Test emphasis |
## 3. Test Levels
| Level | Goal | Owner | In scope | Not in scope | Automated? |
## 4. Test Types
| Type | Applies to | Approach | Trigger (every commit / nightly / pre-release) |
## 5. Environments
| Env | Purpose | Data | Integrations | Deploy control |
## 6. Test Data
## 7. Automation and Pipeline Integration
## 8. Defect Management
## 9. Quality Gates and Metrics
## 10. Roles and Responsibilities
## 11. Assumptions, Constraints, Open Questions
```

## Quality checklist
- [ ] Every high risk area maps to at least one test level and test type.
- [ ] Each level states what it does not cover, to avoid duplication.
- [ ] Non-functional testing (performance, security, accessibility) is addressed or explicitly excluded with reason.
- [ ] Test data approach respects privacy law; production data is never used unmasked.
- [ ] No tool, number or owner is invented; gaps are marked.
- [ ] The strategy is methodology-neutral and usable by several teams.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing a test plan with dates and names. Keep the strategy stable; put schedules in `test-plan`.
- Copying a generic test pyramid. Derive the portfolio from the architecture and risks (e.g. contract tests for many service integrations).
- Ignoring third-party integrations. Define stubbing/virtualization and who tests the real connection.

## Example
Input: "Onboarding platform: web + mobile, 12 microservices, core banking and KYC provider integrations."

Excerpt of output:
- Risk: KYC provider response variants (H likelihood, H impact) → consumer-driven contract tests per service + a small set of end-to-end tests against the provider sandbox.
- Level "End-to-end": 10-15 critical journeys only; business rule combinations are tested at component level.
- Environment "SIT": KYC provider virtualized `[ASSUMPTION: sandbox has rate limits]`.
