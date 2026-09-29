---
name: tech-debt-assessment
description: "Builds a technical debt register by inventorying debt items across code, architecture, tests, infrastructure, dependencies and documentation, classifying them (deliberate/inadvertent, prudent/reckless), estimating principal (cost to fix) and interest (ongoing cost and risk), and prioritizing them into a paydown plan tied to business impact. Use when a team feels slowed down by the codebase, when leadership asks how much debt exists and what to fix first, or when debt must be justified in planning."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 04-architecture
  role: software-architect
  area: evolution
  title: "Assess technical debt"
  related: "code-quality-report, refactoring, modernization-assessment, dependency-upgrade, technical-risk-review"
  prompt: "Assess the technical debt in our billing platform; releases take two weeks, test coverage is 30% and we still run an unsupported framework version."
---

# Assess Technical Debt

## Purpose
Turn vague complaints about "legacy" and "debt" into a prioritized, evidence-based register that shows what each item costs today, what it costs to fix and in which order to pay it down.

## When to use
- Delivery is slowing, incident or defect rates rise, and the team suspects the codebase or platform.
- Leadership or product asks for a debt overview to decide investment.
- Planning needs a justified share of capacity for debt paydown.

## When not to use
- A metrics snapshot of one codebase is enough (complexity, coverage, duplication). Use `code-quality-report`.
- The whole system's future (retain, replatform, replace) is the question. Use `modernization-assessment`.
- A single known item needs a concrete fix. Use `refactoring` or `dependency-upgrade`.

## Inputs
Required:
- The system or area in scope and the symptoms observed (slow changes, incidents, onboarding pain, audit findings).

Optional:
- Static analysis results, coverage, dependency and end-of-life lists, incident and defect history, lead time and change failure rate.
- Team interviews or survey results, architecture documents, upcoming roadmap items.

If no symptoms or evidence are given, ask for the two or three pains that triggered the request. Do not invent metrics; mark gaps `[UNKNOWN]`.

## Process
1. Anchor on outcomes: link symptoms to delivery and operational measures (lead time, change failure rate, recovery time, onboarding time, defect escape) where available.
2. Inventory debt items by category: code, architecture/design, tests, build and pipeline, infrastructure, dependencies and end-of-life components, data, documentation and knowledge (single points of expertise).
3. For each item, record evidence (metric, incident, file hotspot, interview quote) and label items based only on opinion as `[ASSUMPTION]`.
4. Classify cause with the technical debt quadrant (deliberate/inadvertent × prudent/reckless) to separate conscious trade-offs from process problems that will keep creating new debt.
5. Estimate principal as a range in effort (e.g., person-days) and interest as recurring cost: extra effort per change, incident hours, risk exposure (security, compliance, end-of-life). Use ranges and state the basis.
6. Weight interest by hotspot: debt in code that changes often or sits on critical paths costs more than debt in stable, rarely touched areas.
7. Score each item on interest, risk, and fit with upcoming roadmap work; prioritize high interest and risk with low principal first, and items on the roadmap's path.
8. Choose a treatment per item: fix now, fix alongside related feature work, schedule as a dedicated item, contain (isolate behind an interface) or accept and document.
9. Identify root-cause process fixes (missing definition of done items, no review, no dependency update routine) so debt does not grow back.
10. Build the paydown plan: capacity share or dedicated items per iteration or quarter, owners and measures that will show improvement.
11. If the goal continues, suggest `refactoring` or `dependency-upgrade` for top items, `modernization-assessment` if debt is systemic, or `technical-risk-review` for risk items.

## Output format
```markdown
# Technical Debt Assessment: <system>
Scope: ... · Evidence sources: ... · Baseline measures: <lead time, CFR, ... or [UNKNOWN]>

## Debt Register
| ID | Item | Category | Quadrant | Evidence | Principal (range) | Interest (per month/change) | Risk | Hotspot | Priority | Treatment |
|---|---|---|---|---|---|---|---|---|---|---|

## Top Priorities
1. <item> — why now — expected effect

## Root Causes and Process Fixes
- ...

## Paydown Plan
| Period | Items | Capacity | Owner | Success measure |
|---|---|---|---|---|

## Accepted Debt
- <item> — reason — review date

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every item has evidence or is labeled `[ASSUMPTION]`.
- [ ] Principal and interest are ranges with a stated basis; no invented precision or money figures.
- [ ] Prioritization uses interest and hotspots, not only size or severity.
- [ ] Each item has a treatment, including explicit acceptance where appropriate.
- [ ] Process causes are addressed so debt does not regrow.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Listing every code smell a scanner finds. Keep items that measurably slow delivery or create risk; aggregate the rest.
- Asking for a "debt sprint" with no business link. Tie each item to lead time, incidents or roadmap work.
- Treating end-of-life dependencies as normal debt. They carry security and support risk with a date; prioritize them by that date.

## Example
Input: "Billing platform: releases take two weeks, 30% coverage, unsupported framework version."

Excerpt of output:
- TD-01 Unsupported framework (dependencies, deliberate/prudent): no security patches; principal 20–40 person-days `[ASSUMPTION: based on similar upgrades]`; interest: open security exposure; priority 1, treatment: schedule this quarter.
- TD-02 Missing tests around invoice calculation (tests, inadvertent/reckless): hotspot changed in 70% of releases `[confirm with history]`; interest: manual regression adds ~3 days per release; treatment: add characterization tests alongside next pricing change.
- Process fix: add "tests for changed logic" to the definition of done.
