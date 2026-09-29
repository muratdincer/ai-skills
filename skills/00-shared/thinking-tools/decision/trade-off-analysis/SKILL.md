---
description: Makes explicit what each option gains and gives up across competing qualities (for example speed vs. safety, cost vs. resilience, flexibility vs. simplicity, scope vs. time), identifies the decisive tension, the reversibility of each choice and the conditions under which the preferred option stops being right. Use for architecture, product, scope or process decisions where no option wins on everything, when stakeholders talk past each other, or before recording a decision.
related: decision-matrix, adr, architecture-review, pros-cons, technology-selection
prompt: Analyze the trade-offs between a modular monolith and microservices for our new claims system.
---

# Analyze Trade-offs

## Purpose
Replace "which option is best" with "what are we willing to give up, and why", so the decision reflects the organization's priorities explicitly and can be revisited when those priorities or conditions change.

## When to use
- Options are each strong on different qualities and no option dominates.
- A decision must balance competing quality attributes (performance, availability, security, cost, time to market, maintainability).
- Stakeholders argue past each other because they optimize different goals.

## When not to use
- Many options must be scored and ranked. Use `decision-matrix`.
- A quick advantage/disadvantage list for one proposal is enough. Use `pros-cons`.
- A full architecture evaluation against requirements is needed. Use `architecture-review`.

## Inputs
Required:
- The decision and at least two options.
- The goal or drivers of the decision.

Optional, improves quality:
- Quality attribute priorities, constraints (budget, deadline, skills, regulation).
- Context: current system, team size, expected load and growth.

If the drivers are missing, ask which two or three outcomes matter most; trade-offs cannot be judged without them.

## Process
1. State the decision, its drivers in priority order and the fixed constraints.
2. List the qualities that matter for this decision (5-8), phrased so both directions are visible ("time to first release", "independent scaling").
3. For each option, describe concretely what it gains and what it gives up per quality, relative to the other options.
4. Find the decisive tensions: the one or two qualities where options differ most and the drivers disagree.
5. Make costs visible that are easy to miss: operational load, cognitive load, skills, migration effort, lock-in and cost of delay.
6. Assess reversibility: how expensive is it to change course later (one-way vs. two-way door)? Irreversible choices need more evidence.
7. Identify the conditions under which each option becomes the right one (scale, team size, change frequency, regulatory change).
8. Check for hybrid or staged options that buy time for the irreversible part (for example start modular, extract later).
9. Recommend an option, stating explicitly what is accepted as the cost, and define signals that would trigger revisiting the decision.
10. Label inferences and missing facts as `[ASSUMPTION]` or `[UNKNOWN]`, and list open questions.
11. If the user's goal continues, suggest `adr` to record the decision and its accepted trade-offs, or `decision-matrix` when more options appear.

## Output format
```markdown
# Trade-off Analysis: <decision>
**Drivers (priority order):** 1. ... 2. ... **Constraints:** ...

| Quality | Option A gains / gives up | Option B gains / gives up |
|---|---|---|
| <quality> | + ... / - ... | + ... / - ... |

## Decisive Tensions
- <quality X vs. quality Y>: ...

## Hidden Costs and Reversibility
| Option | Hidden costs | Reversibility (one-way / two-way) | Cost to change later |
|---|---|---|---|

## When Each Option Is Right
- Option A if ...; Option B if ...

## Recommendation
<option>. We accept <cost> in exchange for <gain>. Revisit when <signal>.

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every option shows both gains and costs; no option is presented as free.
- [ ] Decisive tensions are linked to the stated drivers.
- [ ] Reversibility and hidden costs (operations, skills, lock-in) are covered.
- [ ] The recommendation names the accepted cost and the revisit signals.
- [ ] Inferences and missing facts are labeled; no numbers are invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Judging options against an ideal instead of each other. Every gain is relative to a real alternative.
- Hiding the cost of the preferred option. State it plainly; that is what makes the decision trustworthy.
- Treating reversible decisions with the same ceremony as irreversible ones. Decide two-way doors fast.
- Choosing for a future scale that the drivers do not justify.

## Example
Input: "Modular monolith vs. microservices for our new claims system; team of 8, launch in 9 months."

Excerpt of output:
| Quality | Modular monolith | Microservices |
|---|---|---|
| Time to first release | + one deployable, one pipeline / - | - platform work before features / + |
| Independent scaling | - scales as one unit / | + per-service scaling / - more infrastructure |
| Operational load | + low / | - distributed tracing, many pipelines with 8 people `[ASSUMPTION: no platform team]` |

Recommendation: modular monolith with enforced module boundaries. We accept coarse-grained scaling in exchange for launch speed. Revisit when a module needs a separate release cadence or scaling profile.
