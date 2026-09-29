---
name: nfr-to-architecture
description: "Turns non-functional requirements into measurable quality attribute scenarios (source, stimulus, environment, artifact, response, response measure) and maps each to architectural tactics, with the trade-offs and verification method. Use when NFRs are vague (\"fast\", \"secure\", \"highly available\"), when a design must show how it meets quality goals, or before an architecture review or ATAM."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 04-architecture
  role: solution-architect
  area: design
  title: "Map NFRs to architecture tactics"
  related: "nfr-specification, solution-architecture-document, atam-evaluation, trade-off-analysis, slo-definition"
  prompt: "Map these NFRs to architecture tactics: checkout must be fast, available 24/7, handle Black Friday peaks and comply with PCI DSS."
---

# Map NFRs to Architecture Tactics

## Purpose
Make quality requirements testable and traceable to concrete design decisions, so the architecture visibly answers each quality goal and its costs are understood.

## When to use
- NFRs exist but are adjectives without measures.
- A solution design must justify how it achieves availability, performance, security, modifiability or other qualities.
- Preparing input for `architecture-review` or `atam-evaluation`.

## When not to use
- NFRs have not been elicited at all. Use `nfr-specification` first.
- The goal is to define service-level objectives for an existing service. Use `slo-definition`.
- A full trade-off evaluation with stakeholders is needed. Use `atam-evaluation`.

## Inputs
Required:
- The NFRs or quality goals, in any form.
- A short description of the system or its main containers.

Optional:
- Business context (peak events, regulation, user base), current measurements, constraints (budget, platform, team).
- Existing architecture documents or ADRs.

If the system description is missing, ask for it. Missing measures become `[TBD]` with a proposed candidate marked `[ASSUMPTION]`.

## Process
1. Group the NFRs by quality attribute using ISO/IEC 25010 characteristics (performance efficiency, reliability, security, maintainability, compatibility, usability, portability) plus operability and cost.
2. Rewrite each as a quality attribute scenario: source, stimulus, environment, artifact, response, response measure. Separate what the user stated from proposed measures.
3. Flag conflicts and ambiguity (e.g., "real-time" with "cheapest option", strong consistency with multi-region writes).
4. Prioritize scenarios by business importance and technical difficulty (H/M/L each); focus on H/H and H/M.
5. For each priority scenario, select tactics from the attribute's tactic families (e.g., availability: detect, recover, prevent faults; performance: control demand, manage resources; security: resist, detect, react, recover; modifiability: reduce coupling, increase cohesion, defer binding).
6. Map tactics to concrete architectural elements: which container, component, platform service or pattern implements them.
7. State the trade-offs of each tactic on other attributes and cost (e.g., caching improves latency but adds staleness and invalidation complexity).
8. Define verification per scenario: load test, chaos experiment, security test, architecture fitness function, monitoring SLI.
9. Mark residual risks where no tactic fully meets the measure, and sensitivity points where one parameter drives several qualities.
10. Produce the traceability table and a list of ADR candidates.
11. If the goal continues, suggest `solution-architecture-document` to embed the result, `atam-evaluation` to validate with stakeholders or `slo-definition` for run-time targets.

## Output format
```markdown
# NFR to Architecture Mapping: <system>
## Quality Attribute Scenarios
| ID | Attribute | Source | Stimulus | Environment | Artifact | Response | Measure | Priority (Biz/Tech) |
|---|---|---|---|---|---|---|---|---|
## Tactics and Architectural Elements
| Scenario | Tactics | Implemented by | Trade-offs | Verification |
|---|---|---|---|---|
## Conflicts and Sensitivity Points
## Residual Risks
## ADR Candidates
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every scenario has a numeric or otherwise testable response measure, or is marked `[TBD]`.
- [ ] Stated measures and proposed measures are distinguishable.
- [ ] Each tactic maps to a named architectural element, not only to a pattern name.
- [ ] Trade-offs on other qualities and cost are stated for each tactic.
- [ ] Each priority scenario has a verification method.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Scenarios without environment: "p95 < 300 ms" means nothing without load level and mode (normal, peak, degraded).
- Listing tactics as a checklist of buzzwords. Each must connect to a scenario and a component.
- Treating security as one scenario. Split by threat and asset; link to `threat-model` where needed.

## Example
Input: "Checkout must be fast, 24/7, survive Black Friday, PCI DSS."

Excerpt of output:
| ID | Attribute | Stimulus | Environment | Measure |
|---|---|---|---|---|
| P1 | Performance | Customer submits payment | Peak load `[TBD: x × normal, from last year's data]` | p95 checkout API < `[TBD]` ms `[ASSUMPTION: 500 ms]` |
| A1 | Availability | Payment provider times out | Normal operation | Order accepted and payment retried; no customer-visible error for 99.9% of attempts |

Tactics for A1: timeout + circuit breaker on the payment adapter, outbox for pending payments. Trade-off: order status becomes "pending" and needs customer messaging.
