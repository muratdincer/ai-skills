# Methodologies Guide

The skills are methodology-independent: a user story, a risk register or a retrospective is the same piece of work whether the team runs Scrum, Kanban or a phased plan. This guide maps each common way of working to the skills you use at each step.

## 1. Lifecycle view (works for every methodology)

| Lifecycle stage | Key questions | Skills |
|---|---|---|
| Initiation | Why, for whom, is it worth it? | `request-intake-document`, `request-triage`, `problem-statement`, `feasibility-study`, `cost-benefit-analysis`, `project-charter`, `stakeholder-identification`, `stakeholder-map` |
| Discovery | What problem exactly, which users? | `persona`, `jobs-to-be-done`, `problem-interview-script`, `customer-journey-map`, `opportunity-solution-tree`, `assumption-mapping`, `experiment-design` |
| Requirements | What must the solution do? | `interview-question-set`, `workshop-plan`, `brd-writing`, `frd-writing`, `srs-writing`, `user-story`, `acceptance-criteria`, `nfr-specification`, `requirements-gap-analysis`, `ambiguity-detection`, `traceability-matrix` |
| Planning | How much, when, who? | `wbs`, `estimation-three-point`, `schedule-plan`, `resource-plan`, `risk-register`, `roadmap`, `release-planning`, `dependency-map` |
| Design | How will it work? | `solution-architecture-document`, `c4-model`, `adr`, `event-storming`, `api-contract`, `database-schema-design`, `threat-model`, `user-flow`, `wireframe-spec` |
| Build | Make it | `task-breakdown`, `implement-from-story`, `unit-test-writing`, `code-review`, `pull-request-description`, `commit-message`, `pipeline-design` |
| Verify | Does it work, is it good enough? | `test-strategy`, `test-plan`, `test-case-writing`, `bug-report`, `uat-plan`, `secure-code-review`, `performance-test-plan`, `release-quality-gate` |
| Release | Ship it safely | `release-plan`, `deployment-checklist`, `rollback-plan`, `go-no-go`, `release-notes`, `go-to-market-plan` |
| Operate | Keep it healthy | `slo-definition`, `alert-design`, `runbook`, `incident-response`, `ticket-triage`, `problem-management` |
| Improve | Learn and adapt | `postmortem`, `lessons-learned`, `feature-adoption-review`, `tech-debt-assessment`, `retrospective-facilitation` |

## 2. Plan-driven (Waterfall, V-Model)

Work flows through sequential phases with formal documents and sign-offs (gates) between them.

| Phase / gate | Skills |
|---|---|
| Project start, charter approval | `project-charter`, `scope-statement`, `raci-matrix`, `communication-plan`, `kickoff-deck` |
| Requirements baseline | `brd-writing`, `frd-writing`, `srs-writing`, `use-case-spec`, `requirements-review-checklist`, `requirements-sign-off` |
| Design baseline | `solution-architecture-document`, `technical-design-doc`, `architecture-review` |
| Planning and control | `wbs`, `schedule-plan`, `budget-plan`, `earned-value-analysis`, `change-control`, `raid-log`, `project-status-report` |
| Test levels (V-Model: each spec pairs with a test level) | requirements ↔ `uat-plan`, design ↔ `integration-test-writing`, detailed design ↔ `unit-test-writing`; plus `test-plan`, `traceability-matrix`, `test-summary-report` |
| Acceptance and closure | `acceptance-certificate`, `project-closure-report`, `lessons-learned` |

Tip: in plan-driven work, change is expensive, so run `requirements-gap-analysis`, `ambiguity-detection` and `requirements-consistency-check` before the requirements sign-off.

## 3. Iterative frameworks (Scrum and similar)

Work is delivered in fixed-length iterations (sprints) with a small set of events.

| Event / artifact | Skills |
|---|---|
| Product goal, product backlog | `product-vision`, `roadmap`, `backlog-refinement`, `backlog-prioritization`, `story-splitting`, `definition-of-ready` |
| Iteration planning | `iteration-goal`, `iteration-planning`, `task-breakdown`, `estimation-session` |
| Daily sync | `daily-sync-summary`, `impediment-tracking` |
| Increment and Definition of Done | `definition-of-done`, `code-review`, `release-quality-gate` |
| Iteration review | `iteration-review-prep`, `stakeholder-review-prep`, `demo-script` |
| Retrospective | `retrospective-format`, `retrospective-facilitation`, `action-item-extraction` |
| Forecasting | `velocity-analysis`, `burndown-analysis`, `monte-carlo-forecast` |

## 4. Flow-based (Kanban)

Work flows continuously; the focus is on limiting work in progress and improving flow.

| Practice | Skills |
|---|---|
| Visualize and define the workflow | `wip-policy`, `value-stream-map`, `definition-of-done` |
| Limit WIP, manage flow | `wip-policy`, `cycle-time-analysis`, `impediment-tracking` |
| Replenishment | `request-triage`, `backlog-prioritization` |
| Delivery planning | `monte-carlo-forecast`, `release-planning` |
| Service delivery / operations review | `cycle-time-analysis`, `sla-breach-analysis`, `status-update` |
| Improve collaboratively | `retrospective-facilitation`, `five-whys` |

## 5. Engineering practices (XP)

| Practice | Skills |
|---|---|
| Test-driven development | `tdd-cycle`, `unit-test-writing` |
| Refactoring, simple design | `refactoring`, `clean-code-review` |
| Pair / mob programming, collective ownership | `code-review`, `review-comment-writing`, `coding-standards` |
| Continuous integration, small releases | `pipeline-design`, `branching-strategy`, `commit-message` |
| Customer tests | `bdd-feature-file`, `acceptance-criteria` |

## 6. Lean and Lean Startup

| Idea | Skills |
|---|---|
| Identify value, remove waste | `value-stream-map`, `process-gap-analysis` |
| Build-measure-learn | `hypothesis-statement`, `experiment-design`, `mvp-scoping`, `ab-test-analysis` |
| Validated learning | `feedback-synthesis`, `feature-adoption-review`, `assumption-mapping` |

## 7. Scaled agile (SAFe, LeSS, Nexus and similar)

| Need | Skills |
|---|---|
| Portfolio decisions | `portfolio-prioritization`, `backlog-prioritization` (WSJF), `benefits-realization` |
| Multi-team planning event | `program-roadmap`, `cross-team-dependency-board`, `dependency-map`, `iteration-planning` |
| Governance | `governance-framework`, `steering-committee-pack` |
| Architecture runway | `target-state-architecture`, `architecture-principles`, `tech-radar` |
| Team topologies | `team-topology`, `role-definition` |

## 8. DevOps and continuous delivery

| Practice | Skills |
|---|---|
| Pipelines and deployment | `pipeline-design`, `deployment-strategy`, `environment-strategy`, `iac-review` |
| Release safety | `rollback-plan`, `deployment-checklist`, `semantic-versioning` |
| Reliability (SRE) | `slo-definition`, `error-budget-policy`, `alert-design`, `observability-plan` |
| Incident learning | `incident-response`, `postmortem`, `runbook` |
| Measuring delivery | `engineering-metrics-review` (DORA) |

## 9. Design thinking and UX

| Stage | Skills |
|---|---|
| Empathize | `research-plan`, `problem-interview-script`, `observation-notes`, `persona` |
| Define | `research-synthesis`, `problem-statement`, `jobs-to-be-done` |
| Ideate | `opportunity-solution-tree`, `user-flow` |
| Prototype | `wireframe-spec`, `information-architecture` |
| Test | `usability-test-script`, `heuristic-evaluation` |

## 10. Hybrid setups

Most organizations mix: phased funding and contracts with iterative delivery inside, or Scrum teams feeding a plan-driven release process. Pick the skills per activity, not per methodology:

- Contract and funding level: `statement-of-work`, `project-charter`, `budget-plan`, `steering-committee-pack`.
- Team level: iterative or flow skills from sections 3 and 4.
- Release level: `release-plan`, `go-no-go`, `change-request-rfc`.

When a skill step says "if the team works in fixed iterations…", apply it only if that is your case; otherwise skip it.
