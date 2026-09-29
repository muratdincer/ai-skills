---
description: Produces a defensible estimate for technical work by decomposing it into small verifiable tasks ordered by dependency and risk, estimating each as a range, making assumptions and unknowns explicit, adding integration, testing and release effort, and stating confidence and what would change the number. Use when a tech lead is asked "how long will this take?", when a feature, migration or technical initiative needs sizing for planning or commitment, or when an existing estimate must be challenged or re-baselined.
related: task-breakdown, estimation-three-point, spike-report, technical-risk-review, monte-carlo-forecast
prompt: Product wants to know how long it will take to add SSO with our corporate identity provider to our web app. Give me an estimate with ranges and assumptions.
---

# Estimate Technical Work

## Purpose
Give decision makers an estimate they can plan with: a range with a stated confidence, the assumptions it rests on, and the unknowns that could move it. A good estimate is a communication tool about risk, not a promise of a date.

## When to use
- Someone asks how long a feature, migration, integration or refactoring will take.
- Work must be sized for roadmap, iteration or budget planning.
- A previous estimate looks wrong and needs to be re-baselined with new information.

## When not to use
- Breaking a single story into implementation tasks without sizing the whole. Use `task-breakdown`.
- Formal project schedules with three-point math across many work packages. Use `estimation-three-point`.
- Forecasting completion from a team's historical throughput. Use `monte-carlo-forecast`.

## Inputs
Required:
- A description of the work (feature, epic, technical initiative) and what "done" means.

Optional, improves quality:
- Relevant code, architecture and constraints; team size, experience and availability.
- Historical data for similar work (actual durations, throughput).
- Deadlines, fixed-scope or fixed-date constraints, dependencies on other teams.

If "done" is unclear (e.g., does it include migration, documentation, production rollout), ask. Ask at most five questions; everything else becomes an explicit assumption.

## Process
1. Restate the scope and the definition of done, including non-coding work: tests, security review, documentation, deployment, data migration, monitoring, stabilization.
2. Decompose into small verifiable tasks (target: each fits within a couple of days of effort), each with a done criterion and how it will be verified. Stop decomposing where uncertainty, not size, dominates.
3. Order tasks by dependency and risk: riskiest or most uncertain items first; mark tasks that depend on other teams or external parties.
4. Classify uncertainty per task: known (done before), known-unknown (needs investigation), unknown (new technology or unclear requirement). Propose a time-boxed spike for items too uncertain to estimate.
5. Estimate each task as a range (optimistic / likely / pessimistic or low / high) in effort; never a single number. Use reference tasks or history where available and say so.
6. Add the often-forgotten work explicitly: integration and end-to-end testing, code review cycles, environment setup, release and rollout, bug fixing after first usage.
7. Convert effort to calendar time using stated availability (focus factor, parallel work, on-call, holidays) as an `[ASSUMPTION]` if not given; show where parallelization is and is not possible.
8. Aggregate: sum ranges sensibly (do not add all pessimistic values as the "likely" total), and state a confidence level for the overall range.
9. List assumptions, dependencies and the top risks with their effect on the estimate ("if the identity provider requires a custom claim mapping, add 3-5 days").
10. State what would narrow the range (spike, prototype, answer from another team) and when the estimate should be revisited.
11. If the user continues, suggest `task-breakdown` for detailed stories, `spike-report` to resolve the largest unknown, or `technical-risk-review` for risks that threaten the plan.

## Output format
```markdown
# Estimate: <work item>
Definition of done: ...
Overall: <low>–<high> <unit> effort · <low>–<high> calendar weeks · Confidence: <low/medium/high>

## Task Breakdown
| # | Task | Done when / verified by | Depends on | Uncertainty | Estimate (low–likely–high) |
|---|---|---|---|---|---|

## Calendar Assumptions
- Team: ... · Availability: ... [ASSUMPTION] · Parallelism: ...

## Assumptions
- [ASSUMPTION] ...

## Risks and Their Effect
| Risk | Effect on estimate | Mitigation |
|---|---|---|

## How to Narrow the Range
- ...
```

## Quality checklist
- [ ] Every estimate is a range, and the overall range has a stated confidence.
- [ ] Tasks are small, each with a done criterion and a verification step, ordered by dependency and risk.
- [ ] Non-coding work (testing, review, release, migration, stabilization) is included.
- [ ] Every assumption is labeled and none of the numbers is invented without a stated basis.
- [ ] Risks are quantified as their effect on the estimate, not only listed.
- [ ] Effort and calendar time are shown separately.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Giving a single number under pressure; it becomes a commitment. Give a range and the assumptions that bound it.
- Estimating only the coding. Integration, review, release and stabilization often take as long as writing the code.
- Converting effort to dates at 100% availability, ignoring meetings, support duty and other projects.

## Example
Input: "Add SSO with corporate identity provider to our web app."

Weak: "About two weeks."

Strong excerpt:
| # | Task | Done when / verified by | Depends on | Uncertainty | Estimate (days) |
|---|---|---|---|---|---|
| 1 | Spike: confirm protocol, claims and test tenant access | Login succeeds against test tenant | IdP admin team | Unknown | 1–2–3 (time-boxed) |
| 2 | Implement login/logout flow with the standard protocol library | Integration test passes | 1 | Known-unknown | 2–3–5 |
| 3 | Map IdP claims to app roles; migrate existing accounts | Existing users log in with same permissions in staging | 1 | Known-unknown | 2–4–7 |

Overall: 10–18 days effort, 3–5 calendar weeks at 60% availability `[ASSUMPTION]`, confidence medium. Biggest driver: account linking for existing users.
