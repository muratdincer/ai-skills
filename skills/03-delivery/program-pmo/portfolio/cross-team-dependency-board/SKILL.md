---
description: Runs cross-team dependency planning by surfacing every dependency between teams, making each one explicit (provider, consumer, what, needed-by date), negotiating a commitment or alternative, and tracking status with escalation rules on a shared board. Use when several teams plan the same period together, when a program keeps slipping because of waiting between teams, or when someone asks to map, negotiate or track inter-team dependencies.
related: dependency-map, program-roadmap, raid-log, escalation-message, negotiation-prep
prompt: Set up a dependency board for next quarter's planning; 4 teams, and the checkout team depends on payments and identity for almost everything.
---

# Run Cross-Team Dependency Planning

## Purpose
Make every inter-team dependency explicit, agreed and visible, so that teams plan against real commitments rather than hopes, and dependencies at risk are escalated early enough to change the plan.

## When to use
- Several teams plan the same period and their work intersects.
- A program repeatedly slips because work waits on another team.
- A joint planning event needs a board and a negotiation routine for dependencies.

## When not to use
- Dependencies are within a single project schedule. Use `dependency-map`.
- The need is the program's overall timeline and milestones. Use `program-roadmap`.
- Only an escalation message for one blocked item is needed. Use `escalation-message`.

## Inputs
Required:
- The teams involved and the planning horizon.
- Each team's planned work or objectives for that horizon (a list is enough).

Optional, improves quality:
- Known dependencies, shared platforms or specialists, vendor inputs.
- Team capacity and iteration calendar.
- Existing escalation paths and decision owners.

If teams or planned work are missing, ask. Unknown dates or commitments stay `[TBD]` and are shown as unconfirmed.

## Process
1. Scan each team's planned work for dependencies with these prompts: needs an API, data, environment, decision, approval, specialist skill, shared component or vendor delivery from someone else. Also ask the reverse: who needs something from this team? Mark inferred dependencies `[ASSUMPTION]`.
2. Write each dependency as a card: ID, consumer team, provider team, what exactly is needed (verifiable deliverable), needed-by date or iteration, consumer work blocked by it.
3. Classify type (build, decision, environment, knowledge, external) and criticality: does it sit on a program milestone or critical path?
4. Negotiate each card in a provider-consumer pairing: provider confirms capacity and a committed date, or proposes an alternative (reduced scope, interim stub or contract, reordering, consumer self-service). Record the outcome as Committed, Committed with conditions, Not committed, or Removed by redesign.
5. For not-committed or late-committed cards, find the least costly fix: resequence consumer work, decouple via a contract or mock, move capacity, or escalate to the decision owner.
6. Lay the cards on the board: teams as rows, iterations or weeks as columns, a line from provider delivery to consumer need. Flag red where delivery is after need or where one team holds too many incoming dependencies.
7. Identify concentration risk: provider teams with the most inbound dependencies and single points of failure (one specialist, one environment). Propose mitigations.
8. Define the tracking routine: status values (Not started, On track, At risk, Late, Done), update cadence, who updates, and escalation rules (e.g. At risk for more than one cycle or needed-by within two weeks goes to the program lead).
9. Record open dependencies with no provider owner and decisions needed, each with who should decide and by when.
10. If the goal continues, suggest `program-roadmap` to reflect committed dates, `raid-log` to track the risky ones, or `escalation-message` for items that must be escalated.

## Output format
```markdown
# Dependency Board: <program / planning period>
Teams: <list> · Horizon: <iterations / dates> · Updated: <date>

## Dependency Register
| ID | Consumer | Provider | What is needed (verifiable) | Needed by | Committed date | Type | Critical path | Status | Notes / alternative |
|---|---|---|---|---|---|---|---|---|---|

## Board View
| Team | <iter 1> | <iter 2> | <iter 3> | <iter 4> |
|---|---|---|---|---|
| <provider team> | D-01 ▶ | | | |
| <consumer team> | | ▶ D-01 needed | | |
Red flags: <cards where delivery > need>

## Concentration and Single Points of Failure
## Tracking and Escalation Rules
## Unresolved Items and Decisions Needed
1. <item> — <decision owner> — <by when>
## Assumptions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every dependency names consumer, provider, a verifiable deliverable and a needed-by date or `[TBD]`.
- [ ] Each card has a negotiated status; unconfirmed commitments are not shown as committed.
- [ ] Cards where delivery is later than need are flagged with a proposed resolution.
- [ ] Concentration risk and single points of failure are identified.
- [ ] Escalation rules state trigger, route and timing.
- [ ] Inferred dependencies are labeled and listed for confirmation.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Vague cards such as "needs payments team support". Define a deliverable both sides can verify as done.
- Recording a dependency as committed because the provider did not object. Only an explicit provider confirmation counts.
- Accepting dependencies as fixed. Often the cheapest fix is redesign (stub, contract-first, consumer self-service), not more coordination.

## Example
Input: "4 teams; checkout depends on payments and identity for almost everything."

Excerpt of output:
| ID | Consumer | Provider | What is needed | Needed by | Committed | Status |
|---|---|---|---|---|---|---|
| D-01 | Checkout | Payments | Refund API on staging with agreed contract v1 | Iter 2 | Iter 3 | At risk |
| D-02 | Checkout | Identity | Decision: guest checkout allowed? | Iter 1 | `[TBD]` | Not committed |

- D-01 alternative: checkout builds against a contract stub in iter 2; payments delivers real API in iter 3; integration test moved to iter 3.
- Concentration: payments holds 7 of 11 inbound dependencies; propose a shared API-contract review at the start of each iteration.
