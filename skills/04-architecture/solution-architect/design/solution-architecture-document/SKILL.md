---
name: solution-architecture-document
description: "Writes a solution architecture document structured on arc42 - goals and quality requirements, constraints, context and scope, solution strategy, building blocks, runtime scenarios, deployment, crosscutting concepts, decisions, risks and glossary - from requirements and design notes. Use when a solution must be documented for review, handover, approval or audit, or when an existing design lives only in slides and heads."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 04-architecture
  role: solution-architect
  area: design
  title: "Write a solution architecture document"
  related: "c4-model, adr, nfr-to-architecture, architecture-review, technical-design-doc"
  prompt: "Write a solution architecture document for our new loan origination platform; here are the requirements, the integration list and our whiteboard notes."
---

# Write a Solution Architecture Document

## Purpose
Produce a single, reviewable description of a solution that explains what is built, why it is shaped this way and how it runs, at the level needed for architecture boards, delivery teams and operations.

## When to use
- A new solution or major change needs approval from an architecture board.
- A design exists only in slides, whiteboards or people's heads and must be handed over.
- Auditors, security or operations need a reference description.
- A vendor-delivered solution must be documented for the client.

## When not to use
- A single feature or component design for developers. Use `technical-design-doc`.
- Only one decision needs recording. Use `adr`.
- Only diagrams are needed. Use `c4-model`.

## Inputs
Required:
- Business goal and scope of the solution.
- Functional requirements or main use cases, and known quality requirements (NFRs).

Optional:
- Existing systems and integrations, constraints (standards, platforms, regulation, budget).
- Design notes, diagrams, decisions already taken.
- Organizational context: teams, operating model, hosting.

If goal or requirements are missing, ask. Sections without input stay in the document with `[TBD]` and an open question.

## Process
1. Section 1 Introduction and goals: top 3-5 requirements, top 3 quality goals with measurable targets, stakeholders and their expectations.
2. Section 2 Constraints: technical, organizational, regulatory (e.g., KVKK/GDPR, sector regulation), conventions.
3. Section 3 Context and scope: business context (actors, external systems, data exchanged) and technical context (channels, protocols). Include a C4 system context diagram as code.
4. Section 4 Solution strategy: the few fundamental decisions (architecture style, key technologies, decomposition approach, how top quality goals are achieved) with links to ADRs.
5. Section 5 Building block view: level 1 containers with responsibilities and interfaces; level 2 only for complex parts.
6. Section 6 Runtime view: 2-4 architecturally significant scenarios (critical path, failure path, batch) as sequence descriptions.
7. Section 7 Deployment view: environments, nodes, network zones, scaling units, mapping of containers to infrastructure.
8. Section 8 Crosscutting concepts: security (authN/Z, secrets, data protection), observability, error handling, persistence, integration, configuration.
9. Sections 9-11: decisions index, quality scenarios (stimulus/response/measure), risks and technical debt with mitigations.
10. Section 12 Glossary. Run a consistency pass: every container in section 5 appears in 7; every quality goal in 1 is addressed in 4, 8 or 10.
11. If the goal continues, suggest `architecture-review` before sign-off, `nfr-to-architecture` for weak quality sections or `technical-design-doc` for component-level design.

## Output format
```markdown
# Solution Architecture – <solution name>
Version · Status · Authors · Reviewers

1. Introduction and Goals (requirements overview, quality goals table, stakeholders)
2. Constraints
3. Context and Scope (business context table, technical context, context diagram)
4. Solution Strategy
5. Building Block View (container table: name, responsibility, tech, interfaces, owner)
6. Runtime View (scenarios)
7. Deployment View
8. Crosscutting Concepts
9. Architecture Decisions (ADR index)
10. Quality Requirements (quality tree, scenarios)
11. Risks and Technical Debt (risk, impact, mitigation, owner)
12. Glossary
Open Questions
```

## Quality checklist
- [ ] Quality goals are measurable and traced to strategy, concepts or scenarios.
- [ ] Every external system in the context has an interface with protocol and data.
- [ ] Every container has one clear responsibility and an owner.
- [ ] Runtime view includes at least one failure scenario.
- [ ] Personal data flows and their protection are explicit.
- [ ] Unknowns are `[TBD]` with an open question, not invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Documenting technology lists instead of reasons. Section 4 must say why.
- Only the happy path. Reviewers need failure, retry and recovery behavior.
- Diagrams without legends or inconsistent names across views.

## Example
Input: "Loan origination: web and branch channels, credit bureau integration, core banking for disbursement, target 99.9% availability."

Excerpt of output:
| Quality goal | Scenario | Target |
|---|---|---|
| Availability | Credit bureau times out during application | Application saved, user informed, retried asynchronously; 99.9% monthly for submission `[confirm SLO]` |
| Security | Branch user accesses another branch's application | Denied and audited; data scoped by branch claim |
