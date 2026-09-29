---
description: Defines a small set of enterprise or domain architecture principles, each with a statement, rationale and implications in the TOGAF style, plus how compliance is checked and how exceptions are handled. Use when an organization needs guiding rules for architecture decisions, when principles are vague slogans, or when design reviews keep re-arguing the same trade-offs.
related: architecture-review, adr, target-state-architecture, technology-strategy, governance-framework
prompt: Define 8-10 architecture principles for our move to cloud-native, event-driven systems; our drivers are faster delivery, lower run cost and KVKK compliance.
---

# Define Architecture Principles

## Purpose
Produce a short, enforceable set of architecture principles that turn business drivers into decision rules. Good principles settle recurring trade-offs once, so reviews and ADRs can cite them instead of re-debating.

## When to use
- A new architecture practice, platform or transformation program needs guiding rules.
- Existing principles are slogans ("use best practices") with no rationale or implications.
- Design reviews repeatedly argue the same trade-off (reuse vs speed, buy vs build, central vs federated data).
- A merger or reorganization requires harmonizing two sets of principles.

## When not to use
- A single decision needs to be made and recorded. Use `adr`.
- The need is a concrete technology choice. Use `technology-selection` or `tech-radar`.
- Coding-level conventions are required. Use `coding-standards`.

## Inputs
Required:
- Business drivers and strategy (goals, constraints, regulatory context).
- Scope of the principles: enterprise-wide, a domain (data, integration, security) or a program.

Optional:
- Existing principles, standards and policies.
- Recent ADRs or review findings showing recurring conflicts.
- Organizational context: team autonomy model, sourcing strategy, risk appetite.

If drivers or scope are missing, ask. Everything else becomes an open question.

## Process
1. Restate each business driver as a measurable concern (e.g., "lead time for change", "run cost per transaction", "regulatory exposure").
2. Harvest candidate principles from drivers, existing policies and recurring review conflicts. Aim for 8-12 in total; more is not enforceable.
3. For each candidate, apply the TOGAF quality tests: understandable, robust (usable in hard cases), complete, consistent with the others, stable over years.
4. Reject non-principles: platitudes nobody would oppose ("systems must be secure"), technology picks ("use Kafka") and one-off decisions. A good principle has a credible opposite a reasonable organization could choose.
5. Write each principle: short imperative name, one-sentence statement, rationale tied to a driver, implications (what changes for teams, cost, skills, processes).
6. Map principles to drivers in a matrix; every principle traces to at least one driver and every driver is covered.
7. Identify tensions between principles (e.g., "reuse before buy" vs "team autonomy") and state the precedence rule or the decision forum.
8. Define compliance: how a reviewer checks the principle (review question, fitness function, metric) and who owns it.
9. Define the exception process: who approves, what is recorded (ADR), expiry or review date.
10. Mark every assumption about strategy or organization as `[ASSUMPTION]` and list open questions for the architecture board.
11. If the goal continues, suggest `architecture-review` to apply the principles to a design or `adr` to record principle exceptions.

## Output format
```markdown
# Architecture Principles – <scope>
Version: <x.y> · Owner: <role or [UNKNOWN]> · Review cycle: <e.g., yearly>

## Drivers
| ID | Driver | Measure |
|---|---|---|

## Principles
### P<n>. <Imperative name>
- Statement: <one sentence>
- Rationale: <why; driver IDs>
- Implications: <for teams, cost, skills, process>
- Compliance check: <review question / fitness function / metric>
- Precedence / tensions: <P-x wins when ...>

## Driver–Principle Matrix
| Principle | D1 | D2 | ... |

## Exception Process
<approver, record (ADR), expiry>

## Assumptions and Open Questions
```

## Quality checklist
- [ ] 8-12 principles; each has statement, rationale, implications and compliance check.
- [ ] Each principle has a credible opposite (not a platitude) and names no product.
- [ ] Every principle traces to a driver; every driver is covered.
- [ ] Known tensions have an explicit precedence rule or forum.
- [ ] Exception handling is defined and time-boxed.
- [ ] Nothing about the organization is invented; gaps are marked.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing 30 principles. Nobody applies them; merge or demote to standards.
- Omitting implications. Without cost and behavior consequences, principles get agreed and ignored.
- Treating principles as permanent. Tie them to drivers so they are revisited when strategy changes.

## Example
Input: "Drivers: faster delivery, lower run cost, KVKK compliance. Scope: enterprise."

Excerpt of output:
- P3. Data Is Owned by the Domain That Creates It
  - Statement: Each business data set has one owning domain that publishes it through a contract; others do not write to it.
  - Rationale: Reduces coupling that slows delivery (D1); clarifies KVKK accountability (D3).
  - Implications: Shared databases are phased out; domains must fund data contracts and publishing.
  - Compliance check: "Does any service write to a store owned by another domain?" in every design review.
