---
description: Writes an Architecture Decision Record (ADR) capturing context, decision drivers, considered options with pros and cons, the decision, and its consequences, in a Nygard or MADR style, including status and supersession links. Use when an architecturally significant decision has been made or must be made, when a past decision needs to be documented retroactively, or when a decision is being reversed.
related: decision-log, trade-off-analysis, technology-selection, solution-architecture-document, architecture-principles
prompt: Write an ADR for choosing PostgreSQL over MongoDB for the order service; drivers are transactional consistency, team skills and reporting needs.
---

# Write an Architecture Decision Record

## Purpose
Record one architecturally significant decision so future readers understand what was decided, why, what else was considered and what it costs, without reconstructing the discussion.

## When to use
- A decision affects structure, quality attributes, interfaces, dependencies or build/deploy approach and is hard to reverse.
- A decision was made in a meeting or chat and exists nowhere in writing.
- A previous ADR is being superseded or deprecated.
- A principle exception is granted.

## When not to use
- Everyday business or project decisions. Use `decision-log`.
- Options are still wide open and need structured comparison first. Use `trade-off-analysis` or `technology-selection`, then record the result here.
- The whole solution needs documenting. Use `solution-architecture-document`.

## Inputs
Required:
- The decision question (or the decision already taken) and its context.
- The options considered, or enough context to identify realistic ones.

Optional:
- Decision drivers: quality attributes, constraints, principles, costs, deadlines.
- Participants, date, related ADRs, evidence (spikes, benchmarks, PoCs).
- Preferred template (Nygard short form or MADR).

If the decision question is unclear, ask. If the decision is not yet made, write the ADR with status Proposed and a recommendation.

## Process
1. Check significance: if it is easy to reverse and local to one component, suggest a code comment or design note instead.
2. Write a title as a short noun phrase of the decision ("Use PostgreSQL for order persistence"), and a sequential number if the team uses one.
3. Describe context neutrally: forces, constraints, current state, what triggered the decision. No option advocacy here.
4. List decision drivers as named, ranked criteria (e.g., "transactional consistency across order lines", "team experience", "reporting queries").
5. List 2-4 realistic options including "do nothing / keep current" where relevant.
6. For each option, write pros and cons against the drivers; cite evidence or mark `[ASSUMPTION]`.
7. State the decision in one sentence using active voice ("We will ..."), and why it wins on the top drivers.
8. Write consequences: positive, negative (costs, risks, new debt) and follow-up actions with owners.
9. Set status (Proposed, Accepted, Deprecated, Superseded by ADR-n) and date; link related or superseded ADRs.
10. Add a review trigger: the condition under which this decision should be revisited.

## Output format
```markdown
# ADR-<n>: <decision title>
Status: <Proposed | Accepted | Deprecated | Superseded by ADR-x> · Date: <date> · Deciders: <roles or [UNKNOWN]>

## Context
## Decision Drivers
1. ...
## Considered Options
- Option A – <name>
- Option B – <name>
## Pros and Cons of the Options
### Option A
- Good, because ...
- Bad, because ...
## Decision
We will <decision>, because <top drivers>.
## Consequences
- Positive: ...
- Negative: ...
- Follow-up: <action – owner>
## Review Trigger
## Links
```

## Quality checklist
- [ ] One decision per ADR; the title states the decision, not the problem.
- [ ] Context is neutral and understandable to a newcomer in a year.
- [ ] At least two real options were considered, with pros and cons against named drivers.
- [ ] Negative consequences are listed honestly.
- [ ] Status, date and links are set; no deciders or dates invented.

## Common pitfalls
- Straw-man alternatives added only to justify the choice. Include options a competent team could have chosen.
- Editing accepted ADRs to change the decision. Write a new ADR and mark the old one superseded.
- Missing the "why now" in context, which makes the decision look arbitrary later.

## Example
Input: "We chose PostgreSQL over MongoDB for the order service; consistency, skills and reporting matter."

Excerpt of output:
- Title: ADR-012: Use PostgreSQL for Order Service Persistence
- Decision: We will store orders in PostgreSQL, because multi-row transactional consistency and SQL reporting rank highest and the team operates PostgreSQL today.
- Negative consequence: Schema changes need migration scripts in the pipeline; flexible attributes will use JSONB with validation.
- Review trigger: Order write volume exceeds what a single primary can sustain `[threshold TBD after load test]`.
