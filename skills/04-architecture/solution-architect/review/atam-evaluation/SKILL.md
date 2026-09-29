---
name: atam-evaluation
description: "Plans and documents an evaluation modeled on the Architecture Tradeoff Analysis Method (ATAM), producing business drivers, a prioritized quality attribute utility tree, analysis of architectural approaches against high-priority scenarios, and the resulting sensitivity points, trade-off points, risks, non-risks and risk themes. Use when a significant architecture must be evaluated with stakeholders before commitment, when quality goals conflict, or when an independent structured evaluation is requested."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 04-architecture
  role: solution-architect
  area: review
  title: "Run an ATAM-style evaluation"
  related: "nfr-to-architecture, architecture-review, trade-off-analysis, workshop-plan, adr"
  prompt: "Prepare an ATAM-style evaluation for our event-driven payments platform; the key concerns are latency, availability across two data centers and auditability."
---

# Run an ATAM-Style Evaluation

## Purpose
Expose how architectural decisions affect competing quality goals, so stakeholders commit to an architecture knowing its sensitivity points, trade-offs and risks rather than discovering them in production.

## When to use
- A high-stakes architecture is about to be committed (funding, procurement, build start).
- Quality goals conflict (e.g., latency vs. auditability, availability vs. consistency) and stakeholders disagree.
- An independent, structured evaluation is requested by a board or client.

## When not to use
- A quick compliance and completeness check is enough. Use `architecture-review`.
- Quality scenarios are not yet defined and no stakeholders are available. Use `nfr-to-architecture` first.
- Only one decision between options is needed. Use `trade-off-analysis` or `adr`.

## Inputs
Required:
- The architecture description (views and key decisions) or access to the architect to present it.
- Business drivers or the people who can state them.

Optional:
- Existing quality scenarios/NFRs, stakeholder list, constraints, previous evaluation outputs.
- Session format constraints (days available, remote/in person).

If running live, ask one focused question at a time or a short batch of at most five. If inputs come as documents, extract drivers and approaches from them and label every extraction you infer.

## Process
1. Plan the evaluation: evaluation team roles (leader, scribe, questioner), stakeholder groups (architects, developers, operations, business, security), agenda and outputs; keep it methodology-neutral.
2. Capture business drivers: goals, constraints, key quality attributes, and what "success" means to the sponsor.
3. Capture the architecture: main views and the architectural approaches used (e.g., event sourcing, active-active, CQRS, circuit breakers).
4. Build the utility tree: Utility → quality attribute → refinement → concrete scenario, each rated (H/M/L importance, H/M/L difficulty).
5. Brainstorm additional stakeholder scenarios (use-case, growth, exploratory) and prioritize them by vote; merge with the utility tree.
6. Analyze each high-priority scenario: which approaches respond, how, with what evidence; ask probing questions per attribute (e.g., "what happens when the secondary site lags by N seconds?").
7. Record for each analysis: sensitivity points (parameters that strongly affect one attribute), trade-off points (affect several attributes in opposite directions), risks, and non-risks (sound decisions with their rationale).
8. Group risks into risk themes and link each theme to the business driver it threatens.
9. Summarize for the sponsor: top risk themes, recommended mitigations or further analysis, and decisions requiring ADRs.
10. If the goal continues, suggest `adr` for decisions taken, `architecture-review` for follow-up checks or `resilience-review` for availability-related risk themes.

## Output format
```markdown
# ATAM-Style Evaluation: <system> – <date>
## Business Drivers
## Architectural Approaches
## Utility Tree
| Quality attribute | Refinement | Scenario | Importance | Difficulty |
|---|---|---|---|---|
## Scenario Analyses
### <scenario ID>: <scenario>
- Approaches involved: ...
- Sensitivity points: ...
- Trade-off points: ...
- Risks: ...
- Non-risks: ...
## Risk Themes
| Theme | Risks | Business driver impacted | Suggested action |
|---|---|---|---|
## Open Questions and Follow-Ups
```

## Quality checklist
- [ ] Every scenario is concrete (stimulus, environment, measurable response), not a quality adjective.
- [ ] High-priority scenarios (H,H and H,M) were all analyzed or explicitly deferred.
- [ ] Sensitivity and trade-off points name the parameter and the attributes affected.
- [ ] Non-risks are recorded with rationale, not only risks.
- [ ] Risk themes link to business drivers.
- [ ] Stakeholder statements are distinguishable from evaluator inferences.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Turning the evaluation into a design session. Record issues and move on; redesign comes after.
- Letting only architects write scenarios. Operations and business scenarios expose different risks.
- Listing dozens of isolated risks. Group them into themes the sponsor can act on.

## Example
Input: "Event-driven payments platform; concerns: latency, two data centers, auditability."

Excerpt of output:
| Attribute | Refinement | Scenario | Imp. | Diff. |
|---|---|---|---|---|
| Availability | Site failure | Primary DC fails during peak; payments continue from secondary with no lost authorized payments; RPO `[TBD]` | H | H |
| Auditability | Traceability | Auditor requests full history of a payment; produced in < 1 hour from event store | H | M |

Trade-off point: asynchronous cross-DC replication lag – lowers write latency, raises risk of lost events on failover (availability vs. auditability).
