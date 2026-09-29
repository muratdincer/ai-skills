---
description: "Writes a technical design document (RFC) covering problem, goals and non-goals, proposed design, alternatives, rollout, risks and open questions, sized to the change. Use when a feature or change is large, risky or cross-team enough to need review before coding, or when someone asks for an RFC, design doc or technical proposal."
related: "adr, solution-architecture-document, task-breakdown, api-contract, trade-off-analysis"
prompt: "Write a design doc for moving our order confirmation emails from synchronous sending in the checkout request to an outbox plus background worker."
---

# Write a Technical Design Doc (RFC)

## Purpose
Produce a reviewable design document that lets peers challenge the approach before code is written, so that expensive mistakes (wrong data model, unsafe rollout, missed dependency) are caught on paper instead of in production.

## When to use
- The change touches several components, teams, data stores or public contracts.
- The change is hard to reverse: schema change, data migration, new external dependency, protocol change.
- Reviewers or leads ask "is there a design for this?" or an RFC process exists.
- Two or more viable approaches exist and the choice needs a written rationale.

## When not to use
- A single architectural decision needs to be recorded. Use `adr`.
- System-level architecture for a whole solution or program. Use `solution-architecture-document`.
- A time-boxed investigation of an unknown. Use `spike-report` first, then this skill.

## Inputs
Required:
- The problem or requirement (story, ticket, incident, request) and the part of the system it affects.

Optional, improves quality:
- Current architecture notes, relevant code or schemas, traffic and data volumes.
- Constraints: deadline, team size, platform standards, compliance rules.
- Known alternatives or a preferred approach.

If the problem statement is missing, ask for it. Everything else becomes `[UNKNOWN]` or an open question.

## Process
1. Restate the problem in 2-4 sentences, including why now and the cost of doing nothing.
2. Write goals and explicit non-goals. Non-goals prevent scope creep in review.
3. Describe the current state briefly: components, data flow, pain points. Mark gaps `[UNKNOWN]`.
4. Describe the proposed design: components and responsibilities, data model changes, interfaces/contracts, sequence of the main flow and the main failure flow.
5. Cover cross-cutting concerns that apply: consistency and idempotency, concurrency, security and authorization, privacy (mask/minimize personal data), observability, performance and capacity, cost.
6. List at least two alternatives, including "do nothing" or "minimal change", with the reason each was rejected.
7. Plan the rollout: feature flags, migration order (expand-migrate-contract for schemas), backward compatibility, rollback path and data repair if rollback is partial.
8. Define how success is verified: tests, metrics, SLO impact, acceptance signals after release.
9. List risks with likelihood/impact and mitigation, then open questions with an owner.
10. Scale the document to the change: one to two pages for a medium change; skip sections that truly do not apply and say so in one line.
11. If the goal continues, suggest `adr` for each significant decision, `api-contract` for new interfaces and `task-breakdown` to plan implementation.

## Output format
```markdown
# RFC: <title>
Status: Draft | In review | Accepted | Rejected · Author: <name> · Reviewers: <names or [TBD]> · Date: <date>

## 1. Problem and Context
## 2. Goals / Non-goals
## 3. Current State
## 4. Proposed Design
### 4.1 Components and Responsibilities
### 4.2 Data Model Changes
### 4.3 Interfaces and Contracts
### 4.4 Main Flow and Failure Flow (sequence)
## 5. Cross-cutting Concerns (security, privacy, consistency, observability, performance, cost)
## 6. Alternatives Considered
| Option | Pros | Cons | Why not chosen |
## 7. Rollout, Migration and Rollback
## 8. Verification and Success Metrics
## 9. Risks
| Risk | Likelihood | Impact | Mitigation |
## 10. Open Questions
1. <question> — <owner> — <needed by>
```

## Quality checklist
- [ ] Problem and goals are stated without referring to the chosen solution.
- [ ] At least two real alternatives are compared with a rejection reason.
- [ ] The failure path is designed, not only the happy path (timeouts, retries, duplicates, partial failure).
- [ ] Rollout is reversible or the irreversible step is explicitly called out.
- [ ] No volumes, SLAs or dates are invented; unknowns are marked.
- [ ] A reviewer can find the decision they are asked to approve within one minute.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing a code walkthrough instead of a design. Stay at the level of responsibilities, contracts and data; leave code to the pull request.
- Straw-man alternatives. Each alternative must be something a competent engineer might choose.
- Ignoring migration of existing data and in-flight requests. Always describe the transition period.
- Leaving the document unowned after review. Record the final status and link the resulting ADRs.

## Example
Input: "Checkout sends the confirmation email inline; SMTP timeouts fail the order request."

Excerpt of output:
- Goal: Order placement success must not depend on email provider availability. Non-goal: changing email templates.
- Proposed design: write an `outbox` row in the same transaction as the order; a worker publishes and sends with idempotency key `order_id + template`.
- Alternative rejected: fire-and-forget async call after commit, because messages are lost if the process crashes between commit and send.
- Rollout: flag `email.outbox` per tenant; rollback = flag off, worker drains remaining rows.
- Open question: Required delivery delay tolerance? `[UNKNOWN]` — product owner.
