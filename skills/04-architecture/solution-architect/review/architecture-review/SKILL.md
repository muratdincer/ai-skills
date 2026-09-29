---
description: Reviews a solution or software architecture against its business drivers, quality attribute requirements, architecture principles, known risks and common anti-patterns, and produces severity-rated findings with concrete recommendations and a review verdict. Use when a design document, diagram set or ADRs are submitted for architecture board approval, before a major build or go-live, or when a system shows recurring structural problems.
related: architecture-principles, nfr-to-architecture, atam-evaluation, resilience-review, scalability-review
prompt: Review this solution architecture document for our new loan origination platform before the architecture board next week.
---

# Review an Architecture

## Purpose
Give an evidence-based assessment of whether an architecture is fit for its purpose and compliant with agreed principles, with findings the design team can act on and a clear verdict for the approving body.

## When to use
- A solution architecture document, C4 diagrams or ADR set is submitted for approval.
- A major build, procurement or go-live milestone needs an architecture gate.
- A running system shows repeated incidents, delivery slowness or cost overruns with a suspected structural cause.

## When not to use
- A structured stakeholder workshop on quality trade-offs is needed. Use `atam-evaluation`.
- Only one quality attribute is in question. Use `resilience-review`, `scalability-review` or `threat-model`.
- Code-level review of a change. Use `code-review`.

## Inputs
Required:
- The architecture description (document, diagrams, ADRs or a detailed verbal description).
- The business goal or driver of the solution.

Optional:
- NFRs/quality scenarios, architecture principles and standards, reference architectures.
- Constraints (budget, timeline, platforms), previous review findings, incident history.

If the description is too thin to review, ask for the specific missing views (context, containers, deployment, data flows) rather than guessing.

## Process
1. Restate the drivers: business goals, top quality attributes with measures, key constraints. Flag missing measures as a finding, not an assumption.
2. Check completeness of views: context, containers/building blocks, runtime scenarios for critical flows, deployment, data (ownership, flows, classification), cross-cutting concepts.
3. Assess fit to quality goals: for each top quality attribute, find the design decisions that address it; mark "not addressed" explicitly.
4. Check against principles and standards; each deviation is either justified by an ADR/waiver or becomes a finding.
5. Look for anti-patterns: distributed monolith, shared database across services, synchronous call chains on critical paths, chatty interfaces, god service, missing idempotency on retried operations, unclear data ownership, single points of failure, unmanaged vendor lock-in.
6. Check cross-cutting concerns: security (identity, secrets, data protection, KVKK/GDPR), observability, deployment and rollback, backup/DR, operability and support ownership.
7. Check feasibility: team skills, delivery plan, migration and transition states, cost against budget.
8. Rate each finding: Critical (blocks approval), Major (must be resolved before build/go-live), Minor (improve), Observation. Cite the evidence (section, diagram, ADR) for every finding and separate observed facts from inferences.
9. For each Critical and Major finding, propose a concrete remediation and an owner role.
10. Give the verdict: Approved, Approved with conditions (list them), or Not approved (list what must change), and list questions for the design team.
11. If the goal continues, suggest `atam-evaluation` for contested trade-offs, `resilience-review` or `scalability-review` for deep dives, or `adr` to record conditions.

## Output format
```markdown
# Architecture Review: <solution> – <date>
Verdict: <Approved | Approved with conditions | Not approved>
## Scope and Inputs Reviewed
## Drivers Understood
## Summary
<3-5 sentences: strengths, main risks>
## Findings
| ID | Severity | Area | Finding | Evidence | Recommendation | Owner |
|---|---|---|---|---|---|---|
## Quality Attribute Coverage
| Attribute | Target | Addressed by | Status (OK / Partial / Missing) |
|---|---|---|---|
## Principle Compliance and Waivers
## Conditions for Approval
## Questions for the Design Team
```

## Quality checklist
- [ ] Every finding cites evidence from the reviewed material or is labeled as an inference.
- [ ] Every Critical/Major finding has a concrete, actionable recommendation.
- [ ] Each top quality attribute has an explicit coverage status.
- [ ] Deviations from principles are either tied to a waiver/ADR or raised as findings.
- [ ] The verdict follows from the findings (no Critical open under "Approved").
- [ ] Strengths are acknowledged, not only problems.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reviewing personal preferences ("I would use Kafka") instead of fitness to drivers. Tie each finding to a driver, principle or risk.
- Vague findings ("scalability concerns"). State the mechanism, the trigger and the impact.
- Approving on diagrams alone. Ask for runtime and deployment views of critical flows.

## Example
Input: SAD for a loan origination platform; goal: decision in under 10 minutes; principles include "API first" and "no shared databases".

Excerpt of output:
| ID | Severity | Finding | Evidence | Recommendation |
|---|---|---|---|---|
| F1 | Critical | Scoring and document services write to the same schema, violating "no shared databases" | Deployment view, §7 | Give scoring its own store; publish `ApplicationScored` events; or record a waiver ADR with exit date |
| F2 | Major | 10-minute decision target has no runtime view; credit bureau call is synchronous with no timeout stated | §6 missing, §8 | Add runtime scenario, timeout + fallback to manual queue |
