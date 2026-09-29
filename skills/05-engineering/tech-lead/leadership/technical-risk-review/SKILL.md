---
description: Runs a structured technical risk review of a feature, project or release plan: identifies delivery and quality risks across architecture, dependencies, technology novelty, data, integration, performance, security, operability, skills and schedule, rates probability and impact, names early warning signals, and proposes mitigations with owners and the cheapest risk-reducing experiments. Use at kickoff or before committing to a plan, before a major release, when a project shows warning signs, or when stakeholders ask what could go wrong technically.
related: risk-register, technical-estimation, spike-report, threat-model, architecture-review
prompt: We start a 3-month project to move invoice generation to an event-driven service. Review the technical risks before we commit to the plan.
---

# Review Technical Risks

## Purpose
Surface the technical risks that could derail delivery or quality while there is still time to act, and turn each into a concrete mitigation, an early warning signal and an owner. The review is about decisions to make now, not a list to file away.

## When to use
- At project or feature kickoff, before scope and dates are committed.
- Before a major release, migration or architecture change.
- When a running project shows symptoms: slipping estimates, repeated incidents, unclear integration status.

## When not to use
- The goal is to maintain the project's overall risk log across all categories. Use `risk-register`.
- Security threats of a design must be modeled in depth. Use `threat-model`.
- The architecture itself needs a quality-attribute evaluation. Use `architecture-review`.

## Inputs
Required:
- Description of the work: goal, scope, main components and technologies, timeline or milestone.

Optional, improves quality:
- Architecture sketch, dependency list, team composition and experience, estimate and its assumptions.
- Known issues, incident history, constraints (compliance, freeze windows, vendor contracts).

If the scope or the main components are unknown, ask. Ask at most five questions; everything else becomes an assumption or open question.

## Process
1. Restate the objective and what failure would look like (late, over budget, poor quality, incident in production); this anchors impact ratings.
2. Walk systematically through risk sources: architecture and design, technology novelty, external and team dependencies, data (migration, quality, volume), integration and contracts, performance and scalability, security and privacy, operability (monitoring, rollback), testing and environments, people and skills (key-person, availability), schedule and scope.
3. Write each risk as cause → event → consequence ("because the partner API has no sandbox, integration defects may be found late, delaying release"). Separate risks from issues that are already happening.
4. Rate probability and impact (Low/Medium/High) with a one-line rationale; mark ratings not supported by the input `[ASSUMPTION]`.
5. For each Medium/High risk define an early warning signal (a measurable trigger) and a response: avoid, reduce, transfer or accept.
6. Prefer the cheapest risk-reducing actions first: time-boxed spikes, walking skeleton end to end, contract tests, load test of the critical path, early production-like environment, feature flags and rollback rehearsal.
7. Order the plan so that the riskiest assumptions are validated earliest; state the effect on the estimate if a risk materializes.
8. Assign an owner role and a review date to each mitigation; never invent names.
9. Summarize the top three risks and the decision needed now (e.g., start with a spike, change scope, add a dependency milestone).
10. If the goal continues, suggest `risk-register` to track the risks over time, `spike-report` for the top unknown, or `technical-estimation` to re-baseline the plan.

## Output format
```markdown
# Technical Risk Review: <project/feature>
Objective: ... · Horizon: <milestone/date> · Reviewed with: <roles>

## Top Risks and Decision Needed
1. ...
Decision needed now: ...

## Risk Table
| # | Risk (cause → event → consequence) | Source | P | I | Early warning signal | Response | Mitigation action | Owner role | Review date |
|---|---|---|---|---|---|---|---|---|---|

## Current Issues (already happening)
- ...

## Risk-Reducing Experiments
| Experiment | Risk addressed | Time box | Success criterion |
|---|---|---|---|

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] All risk sources in step 2 were considered; empty ones are stated as "no significant risk identified".
- [ ] Each risk is written as cause → event → consequence, and issues are separated from risks.
- [ ] Every Medium/High risk has an early warning signal, a mitigation and an owner role.
- [ ] Ratings not supported by the input are labeled `[ASSUMPTION]`; no names or dates are invented.
- [ ] The top risks lead to a concrete decision or experiment now.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Vague risks such as "complexity" or "tight timeline". Name the cause and the consequence so a mitigation becomes obvious.
- Mitigations that are only "monitor closely". Define the signal and the action taken when it fires.
- Rating everything High. Force a ranking so the team knows where to spend the first weeks.

## Example
Input: "Move invoice generation from nightly batch to event-driven service in 3 months; team new to the message broker."

Weak: "Risk: new technology. Mitigation: be careful."

Strong excerpt:
| # | Risk | Source | P | I | Early warning signal | Response | Mitigation action | Owner role |
|---|---|---|---|---|---|---|---|---|
| 1 | Because the team is new to the broker, message ordering and duplicate handling may be designed wrongly, causing double invoices | Technology novelty | M | H | Duplicate events in integration tests | Reduce | 1-week spike: idempotent consumer + ordering test | Tech lead |
| 2 | Because finance reports read the batch tables, switching off the batch may break month-end reports | Data/dependency | M `[ASSUMPTION]` | H | Unknown consumers found in DB audit | Avoid | Inventory table consumers before design freeze | Architect |
