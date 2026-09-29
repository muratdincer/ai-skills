---
name: technology-strategy
description: "Writes a technology strategy structured as diagnosis, guiding policy and coherent actions, linked to business goals, with explicit trade-offs, what will not be done, and measures of progress. Use when a CTO or technology leader needs a multi-year direction, when existing plans are wish lists without choices, or when aligning architecture, platform, talent and investment decisions with business strategy."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 13-leadership
  role: executive
  area: strategy
  title: "Write a technology strategy"
  related: "target-state-architecture, architecture-principles, product-strategy-one-pager, tech-radar, budget-proposal"
  prompt: "Write a 3-year technology strategy for our insurance company; we have a legacy core, slow releases and a new digital sales goal."
---

# Write a Technology Strategy

## Purpose
Give the organization a small set of clear technology choices that address its most important challenge, so that teams can make consistent decisions and leadership can fund and track them.

## When to use
- A new technology leader or a new business strategy requires a technology direction.
- Current plans list many initiatives but no diagnosis or priorities.
- Architecture, platform, sourcing and talent decisions conflict and need a shared frame.

## When not to use
- Detailed target architecture and transition states. Use `target-state-architecture`.
- Next quarter's commitments and capacity. Use `quarterly-planning`.
- Funding request for already chosen initiatives. Use `budget-proposal`.

## Inputs
Required:
- Business strategy or goals the technology must support, and the current main technology challenges.

Optional, improves quality:
- Current architecture, application portfolio, delivery metrics, cost base, incident history.
- Organization and talent situation, regulatory constraints, market and competitor moves.
- Time horizon and planning cadence.

If business goals are missing, ask for them; a strategy without them becomes a technology wish list.

## Process
1. Gather facts per area (business goals, architecture, delivery, reliability, security, data, cost, people) and separate evidence from opinion.
2. Write the diagnosis: the 1-3 critical challenges that most block the business goals, with evidence, in plain language.
3. Define the guiding policy: 3-5 principles or choices that address the diagnosis, each stating what it favors and what it gives up.
4. State explicitly what will not be done or will be stopped, to free capacity.
5. Derive coherent actions: 5-8 initiatives that reinforce each other, sequenced by dependency and risk, with the first 6-12 months more detailed than later years.
6. Link each action to a business goal and to the diagnosis; drop actions that link to neither.
7. Define measures: outcome indicators (e.g. lead time, availability, cost per transaction, time to onboard a partner) with baselines marked `[UNKNOWN]` if not provided.
8. Identify major risks, assumptions and decision points where the strategy should be revisited.
9. Describe the implications for organization, skills and sourcing (build, buy, partner) at a level that does not name individuals.
10. Summarize on one page for executives; keep details in appendices.
11. If the user's goal continues, suggest `target-state-architecture` for the architecture detail, `budget-proposal` for funding or `quarterly-planning` for the first commitments.

## Output format
```markdown
# Technology Strategy <horizon>: <organization>

## Executive Summary (one page)

## Business Context and Goals
- ...

## Diagnosis
1. <challenge> – evidence – impact on business goals

## Guiding Policy
| Choice | We favor | We give up |
|---|---|---|

## What We Will Stop or Not Do
- ...

## Coherent Actions
| # | Action | Addresses | Business goal | Horizon | Depends on |
|---|---|---|---|---|---|

## Measures
| Indicator | Baseline | Target direction | Review cadence |
|---|---|---|---|

## Organization and Sourcing Implications
- ...

## Risks, Assumptions, Revisit Triggers
- ...
```

## Quality checklist
- [ ] The diagnosis names the critical challenge with evidence, not a list of everything.
- [ ] Every guiding choice states what is given up.
- [ ] Every action traces to the diagnosis and a business goal.
- [ ] "Stop / not do" items exist and are concrete.
- [ ] No invented baselines, costs or dates; unknowns are marked.
- [ ] Revisit triggers and review cadence are defined.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Goals disguised as strategy ("be cloud-native, AI-first, world-class"). Force a diagnosis and choices.
- Too many initiatives with equal priority. Limit and sequence; show what gets less funding.
- Ignoring the people side. Capability and sourcing gaps often decide whether actions happen.

## Example
Input: Insurance company, legacy core, quarterly releases, goal: sell via partners digitally.

Excerpt of output:
- Diagnosis: Partner onboarding takes months because pricing and policy logic live only in the legacy core with batch interfaces `[confirm current onboarding time]`.
- Guiding choice: Expose product and pricing via stable APIs in front of the core (favor) instead of a full core replacement now (give up: faster decommissioning).
- Weak action (avoid): "Modernize IT." Strong action: "Build pricing API layer for top 2 products, first partner live within 12 months."
