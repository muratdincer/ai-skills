---
description: Runs a quarterly planning cycle for a technology organization, turning strategy and demand into a capacity-backed set of commitments, stretch items and explicit trade-offs, with dependencies and risks visible. Use when a CTO, VP or director has to decide what the teams commit to next quarter, when demand exceeds capacity, or when previous quarters overcommitted and underdelivered.
related: technology-strategy, capacity-planning, okr-definition, portfolio-prioritization, cross-team-dependency-board
prompt: Help me plan Q3 for our 6 engineering teams; we have 40 requests from the business, a platform migration and 20% of capacity already lost to support.
---

# Run Quarterly Planning

## Purpose
Produce a quarterly plan leadership can stand behind: commitments sized to real capacity, a short stretch list, and a visible record of what was traded away and why, so that the business knows what to expect and teams are not overloaded.

## When to use
- Preparing the next quarter's plan across several teams or a department.
- Business demand clearly exceeds engineering capacity and choices must be made openly.
- Past quarters show a pattern of overcommitment, carry-over or constant re-planning.

## When not to use
- Multi-year direction and choices. Use `technology-strategy`.
- Ranking a portfolio of projects without capacity mapping. Use `portfolio-prioritization`.
- Planning one team's next iteration. Use `iteration-planning`.

## Inputs
Required:
- The candidate work (initiatives, requests, obligations) and the teams involved with their approximate size.

Optional, improves quality:
- Strategy, OKRs or business goals for the period; last quarter's plan versus actual delivery.
- Headcount, planned leave, hiring and attrition; share of capacity lost to support, incidents and maintenance.
- Known deadlines (regulatory, contractual, events) and cross-team dependencies.

If candidate work or team structure is missing, ask for it. Do not invent capacity numbers; mark them `[UNKNOWN]` and plan in relative terms until the user confirms.

## Process
1. Review last quarter: planned versus delivered, carry-over, and the main causes of slippage; derive a realistic delivery ratio rather than assuming 100%.
2. Compute available capacity per team: people × working days, minus leave, onboarding, on-call, support and a keep-the-lights-on share. Label every estimate you make `[ASSUMPTION]`.
3. Classify demand: mandatory (regulatory, contractual, security, end-of-life), strategic (linked to a stated goal), improvement (debt, reliability, developer experience), and requests without a stated goal.
4. Reserve capacity for mandatory work first, then an explicit health budget (debt, reliability) as a percentage; state that percentage and who agreed to it.
5. Rank the remaining strategic and improvement items by value, urgency, risk reduction and effort, using one visible method; do not rank by who asked loudest.
6. Fill capacity to roughly 70-80% of the realistic figure with commitments; list the next items as stretch, clearly marked as not promised.
7. Map dependencies between teams and on external parties; move any commitment that depends on an unconfirmed dependency to stretch or add a dated decision point.
8. Write the trade-off list: what is deferred or declined, the reason, and the requester informed; this is the most important output for stakeholders.
9. Define 3-5 quarter outcomes (not task lists) and how progress will be seen mid-quarter.
10. Record risks, assumptions and the re-planning rule (what event triggers a change and who decides).
11. Summarize for leadership on one page; keep team-level detail in an appendix.
12. If the user's goal continues, suggest `okr-definition` to phrase outcomes, `cross-team-dependency-board` for dependency tracking, or `budget-proposal` if capacity must grow.

## Output format
```markdown
# Quarterly Plan <quarter>: <organization>

## Summary
- Outcomes this quarter: ...
- Capacity used for commitments: <x% of realistic capacity>
- Key trade-offs: ...

## Last Quarter Review
| Planned | Delivered | Carry-over | Main causes |
|---|---|---|---|

## Capacity
| Team | Gross | Leave/on-call/support | Health budget | Available | Basis |
|---|---|---|---|---|---|

## Commitments
| # | Item | Class | Outcome/goal | Team(s) | Size | Dependencies |
|---|---|---|---|---|---|---|

## Stretch (not promised)
- ...

## Deferred or Declined
| Item | Requester | Reason | Revisit |
|---|---|---|---|

## Risks, Assumptions, Re-planning Rule
- [ASSUMPTION] ...
- [RISK] ...
- Re-plan when: <trigger> – decided by: <role>
```

## Quality checklist
- [ ] Capacity is net of leave, support and health budget, and the basis is shown.
- [ ] Commitments fill no more than about 80% of realistic capacity.
- [ ] Every commitment links to a goal or a mandatory obligation.
- [ ] Deferred and declined items are listed with reasons and requesters.
- [ ] Dependencies on unconfirmed parties are not hidden inside commitments.
- [ ] No invented headcount, sizes or dates; estimates are labeled `[ASSUMPTION]` or `[UNKNOWN]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Planning at 100% capacity. Unplanned work always arrives; use last quarter's actual ratio.
- A plan with no "no". If nothing is deferred, the prioritization did not happen.
- Output lists instead of outcomes. Leadership needs to know what changes for the business, not which tickets close.

## Example
Input: 6 teams, 40 business requests, a platform migration, 20% of capacity already on support.

Excerpt of output:
- Capacity: 6 teams × ~`[ASSUMPTION: 6 engineers]` × 60 days, minus 20% support and 15% health budget, delivery ratio 0.8 from last quarter `[confirm]`.
- Weak outcome (avoid): "Deliver 25 tickets." Strong outcome: "Checkout service runs on the new platform in production for all traffic."
- Declined: 14 requests without a stated goal – returned to requesters with the question "which goal does this move?"
