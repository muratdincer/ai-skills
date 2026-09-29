---
name: decision-log
description: "Records decisions from meetings, threads or documents as numbered decision log entries with context, options considered, rationale, decider, date, consequences, reversibility and review trigger, and flags conflicts with earlier decisions. Use when a team needs a durable, searchable record of why something was decided, or when decisions keep being reopened."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: meetings
  area: after
  title: "Record decisions"
  related: "adr, meeting-minutes, meeting-notes, trade-off-analysis, raid-log"
  prompt: "Add the decisions from today's data platform meeting to our decision log; we chose Delta Lake over Iceberg and postponed the catalog choice."
---

# Record Decisions

## Purpose
Keep a durable record of what was decided, by whom, why and with which alternatives, so the team stops relitigating settled questions and newcomers can understand the reasoning.

## When to use
- Decisions were made in a meeting, chat or email and must not be lost.
- Decisions keep being reopened or people disagree about what was agreed.
- A project or product needs a running decision register for governance or audit.

## When not to use
- The decision is a significant architecture decision that needs its own record. Use `adr`.
- The decision has not been made yet and options must be compared. Use `trade-off-analysis` or `decision-matrix`.

## Inputs
Required:
- Source containing the decision(s): notes, transcript, thread or description.

Optional:
- Existing decision log (to number entries and check conflicts), decision rights/RACI, project name.

If it is unclear whether something was actually decided, record it as `Proposed` and list the confirmation needed.

## Process
1. Identify statements that close an option: approved, chose, agreed, rejected, will not, postponed until. Postponement with a trigger is also a decision.
2. For each decision write a one-line title in the form "<Choice> for <scope>" ("Use Delta Lake as table format for the lakehouse").
3. Capture context: the problem or trigger and constraints in 1-3 sentences.
4. List options considered, including "do nothing", with the main reason each was rejected. Only list options present in the source; mark missing ones `[UNKNOWN]`.
5. Write the rationale: the criteria that tipped the balance.
6. Record decider (person or body), date, participants consulted and dissent if any.
7. State consequences: what this enables, what it rules out, follow-up actions.
8. Classify reversibility: one-way door (costly to reverse) or two-way door; and set a review trigger (date, metric or event).
9. Set status: Proposed, Accepted, Superseded by <ID>, Rejected.
10. Compare with the existing log; if the new decision contradicts an earlier one, mark the earlier as Superseded and say so explicitly.
11. If the user's goal continues, suggest `adr` for architecturally significant decisions or `trade-off-analysis` when the alternatives were not compared rigorously.

## Output format
```markdown
## D-<nnn>: <Choice> for <scope>
| Field | Value |
|---|---|
| Status | Proposed / Accepted / Superseded by D-xxx / Rejected |
| Date | <date> |
| Decider | <name/body> |
| Consulted | <names/roles> |
| Reversibility | One-way / Two-way |
| Review trigger | <date, metric or event> |

Context: <...>
Options considered:
1. <option> – <why not chosen>
2. <chosen option> – chosen
Rationale: <criteria>
Consequences: <enables / rules out>
Follow-up actions: <action – owner – due>
Dissent: <none / summary>
Source: <meeting, date, link>
```

## Quality checklist
- [ ] Each entry records a real decision; unconfirmed ones are `Proposed`.
- [ ] Decider and date are present or marked `[UNKNOWN]`.
- [ ] At least one alternative and the rationale are recorded.
- [ ] Consequences and a review trigger are stated.
- [ ] Conflicts with earlier decisions are resolved via Superseded status.
- [ ] Anything not stated in the input is labeled `[ASSUMPTION]` or listed as an open question, never presented as fact.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Logging only the outcome. Without context and rejected options, the decision will be reopened.
- Recording the loudest opinion as a decision. Check who has the decision right.
- Silent contradiction of an earlier decision. Always link and supersede.

## Example
Input: "We go with Delta over Iceberg since our Spark stack supports it natively; catalog choice postponed until the security review in June."

Excerpt of output:
## D-014: Use Delta Lake as table format for the lakehouse
Status: Accepted | Decider: [UNKNOWN] | Reversibility: One-way
Options: Apache Iceberg – rejected, weaker native support in current Spark stack.
## D-015: Postpone data catalog selection until security review
Status: Accepted | Review trigger: security review in June `[confirm date]`
