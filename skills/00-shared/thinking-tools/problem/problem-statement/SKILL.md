---
description: "Frames a problem as a precise, solution-free statement of who is affected, what happens, when and where, with quantified impact and evidence, plus boundaries and success signals. Use at the start of any initiative, investigation, improvement or design effort, when a team jumps to solutions, when stakeholders describe the same issue differently, or when someone asks to define or reframe a problem."
related: "five-whys, fishbone-analysis, assumption-mapping, hypothesis-statement, request-intake-document"
prompt: "Write a problem statement: customers keep complaining that the monthly invoice is wrong and support is overloaded at the start of each month."
---

# Write a Problem Statement

## Purpose
Create a shared, evidence-based definition of the problem that keeps solution options open and lets the team measure whether any later change actually solved it.

## When to use
- An initiative, project, experiment or root cause analysis is starting.
- Stakeholders propose solutions before agreeing on the problem.
- A complaint, metric drop or incident pattern must be turned into a workable problem.
- A problem has been worked on for a while without progress and needs reframing.

## When not to use
- The cause of a known problem is sought. Use `five-whys` or `fishbone-analysis` after this skill.
- A formal business request needs capturing for triage. Use `request-intake-document`.
- A product hypothesis to test is needed. Use `hypothesis-statement`.

## Inputs
Required:
- A description of the situation, complaint or symptom.

Optional, improves quality:
- Data: metrics, ticket counts, incident records, user feedback (anonymized).
- Affected users, processes, systems.
- Prior attempts to solve it and why they failed.

If the situation description is missing, ask for it. Missing data becomes `[UNKNOWN]` with the evidence needed to fill it.

## Process
1. Collect the raw statements and separate observations (what was seen, measured) from interpretations, causes and proposed solutions; park the latter.
2. Identify who experiences the problem (user segment, role, team), not who reports it.
3. Describe what happens using observable behavior or outcomes, avoiding "lack of X" phrasing that hides a solution.
4. Bound it with 5W2H and Is/Is-Not: where and when it occurs and where and when it does not; this boundary often points to causes later.
5. Quantify the impact: frequency, volume, cost, time, risk, customer or employee effect. Use given data only; otherwise mark `[UNKNOWN]` and name the measure needed.
6. Name the gap: current state versus expected state or standard.
7. Write the statement in one or two sentences: "<Who> experiences <what> when <context>, resulting in <impact>, whereas <expected>." Add a "How might we <reach the expected state> for <who>?" reframe that opens the solution space without naming a solution.
8. Test it: does it contain a solution? Could two readers picture different problems? Is it too broad to act on or so narrow it presupposes the cause? Revise.
9. Define success signals: the observable metric change that would show the problem is solved.
10. List assumptions and evidence gaps to validate.
11. If the user's goal continues, suggest `five-whys` or `fishbone-analysis` to find causes, or `assumption-mapping` to prioritize what to validate first.

## Output format
```markdown
# Problem Statement: <short title>

**Statement:** <Who> experiences <what> when <context>, resulting in <impact>, whereas <expected state>.

**How might we:** <reach the expected state> for <who>?

| Dimension | Is | Is not |
|---|---|---|
| Who | ... | ... |
| What | ... | ... |
| Where | ... | ... |
| When | ... | ... |
| Extent | ... | ... |

## Evidence and Impact
- <data point + source> / [UNKNOWN] – needed: <measure>

## Out of Scope / Parked Solutions
- <ideas raised, kept for later>

## Success Signals
- <metric moves from X to Y> (baseline [UNKNOWN] if not available)

## Assumptions to Validate
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] The statement contains no solution or technology choice.
- [ ] The affected party is specific.
- [ ] Impact is quantified or explicitly marked `[UNKNOWN]` with the needed measure.
- [ ] Is/Is-Not boundaries are filled where information exists.
- [ ] Success signals are observable and linked to the impact.
- [ ] Proposed solutions are parked, not discarded.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- "We don't have a dashboard" is a missing solution, not a problem. Ask what people cannot do or decide today.
- Framing too broadly ("customer experience is poor"). Narrow until the team can name a first measurement.
- Embedding a cause ("because the batch job is slow") in the statement before it is verified.

## Example
Input: "Customers complain the monthly invoice is wrong; support is overloaded at the start of each month."

Excerpt of output:
- Statement: Business customers with mid-cycle plan changes receive invoices whose amounts differ from their expectation in the first week of each month, generating a spike in billing tickets, whereas invoices should be self-explanatory and correct.
- Is not: customers without plan changes `[ASSUMPTION — verify with ticket sample]`.
- Evidence: billing tickets per month-start week `[UNKNOWN]` – needed: ticket count by category for the last 3 months.
