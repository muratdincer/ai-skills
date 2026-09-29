---
description: Defines a target-state architecture by describing the baseline, the target across business, data, application and technology views, the gaps between them and a transition roadmap of plateaus with dependencies and decision points. Use when a transformation, platform consolidation or multi-year program needs a shared picture of where the architecture should be and how to get there.
related: capability-map, architecture-principles, migration-strategy, application-portfolio-assessment, roadmap
prompt: Define the target-state architecture for moving our monolithic order management and nightly batch integrations to domain services with event streaming over three years.
---

# Define Target-State Architecture

## Purpose
Give sponsors and delivery teams one agreed description of the baseline, the target and the ordered transitions between them, so investments and projects move the estate in one direction.

## When to use
- A multi-year transformation or program needs direction before projects start.
- Several initiatives change the same landscape and must converge.
- A strategy (cloud, data, API-first) must be translated into architecture.
- A funding decision needs a gap analysis and phased roadmap.

## When not to use
- Only one system is being designed. Use `solution-architecture-document`.
- The question is how to cut over a specific system. Use `migration-strategy`.
- Guiding rules are missing entirely. Start with `architecture-principles`.

## Inputs
Required:
- Scope and business drivers (what must change and why).
- A baseline description: main applications, integrations, data stores, platforms (a list is enough).

Optional:
- Capability map, application portfolio assessment, principles, standards.
- Constraints: budget envelope, regulatory dates, contracts, skills.
- Program timeline or funding cycles.

If drivers or baseline are missing, ask. Do not invent dates or budgets.

## Process
1. State drivers as target outcomes with measures (e.g., "release lead time per domain", "real-time order status", "exit data center by contract end").
2. Describe the baseline in four views (business, data, application, technology) at the same abstraction level; note known pain points per view.
3. Describe the target in the same four views, derived from principles and drivers. Keep it technology-neutral where the decision is not yet made; mark those as `[DECISION PENDING]`.
4. Run a gap analysis: for each element, baseline → target with action (retain, change, new, retire).
5. Group gaps into work packages; identify dependencies (platform before domain, data before reports).
6. Define 2-4 transition architectures (plateaus); each must be a coherent, operable state that delivers value on its own.
7. For each plateau, list entry criteria, what is live, what is retired, interim integrations, and risks.
8. Identify architecture decisions and their latest responsible date; link to ADRs.
9. Define measures to verify the target is being reached (fitness functions, KPIs per driver).
10. Record assumptions, constraints and open questions for the steering body.
11. If the goal continues, suggest `migration-strategy` for each transition, `roadmap` for scheduling or `adr` for the key target decisions.

## Output format
```markdown
# Target-State Architecture – <scope>
Horizon: <e.g., 3 years> · Status: Draft

## Drivers and Target Outcomes
| Driver | Target outcome | Measure |

## Baseline (Business / Data / Application / Technology)
## Target (Business / Data / Application / Technology)
## Gap Analysis
| View | Element | Baseline | Target | Action | Work package |

## Transition Architectures
### Plateau 1 – <name>
- Live: ... · Retired: ... · Interim integrations: ... · Entry criteria: ... · Risks: ...

## Decisions Pending
| Decision | Options | Latest responsible date | Owner |

## Measures, Assumptions and Open Questions
```

## Quality checklist
- [ ] Baseline and target use the same views and abstraction level.
- [ ] Every gap has an action and belongs to a work package.
- [ ] Each plateau is operable and delivers value alone; interim integrations are explicit.
- [ ] Undecided technology choices are marked, not assumed.
- [ ] Each driver has a measure to track progress.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Drawing only the target. Without baseline and plateaus there is no plan, only a picture.
- Ignoring interim states. Temporary integrations and dual-running cost are often the largest risk.
- Target frozen at tool level. Specify capabilities and patterns; choose products through decisions.

## Example
Input: "Monolithic order management, nightly batch to ERP and warehouse; goal: real-time order status."

Excerpt of output:
| View | Element | Baseline | Target | Action |
|---|---|---|---|---|
| Application | Order management | Monolith | Order, Fulfilment, Billing domain services | Change |
| Data | Order status to warehouse | Nightly file | Order events on a streaming platform `[DECISION PENDING: platform]` | New |
- Plateau 1: Order events published from the monolith via CDC; warehouse consumes events; nightly file retired for warehouse only.
