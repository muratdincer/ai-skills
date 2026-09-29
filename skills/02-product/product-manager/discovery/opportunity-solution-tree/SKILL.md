---
name: opportunity-solution-tree
description: "Builds an opportunity solution tree that links one measurable outcome to customer opportunities (needs, pains, desires) from research, several candidate solutions per target opportunity, and assumption tests. Use when a team must choose what to work on to move an outcome, when discovery work lacks structure, or when someone asks to connect a goal to ideas and experiments."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-manager
  area: discovery
  title: "Build an opportunity solution tree"
  related: "okr-definition, jobs-to-be-done, hypothesis-statement, experiment-design, assumption-mapping"
  prompt: "Build an opportunity solution tree for increasing 30-day retention of new mobile banking users."
---

# Build an Opportunity Solution Tree

## Purpose
Make the path from a business outcome to what the team builds explicit and testable, so the team compares options instead of committing to the first idea, and learns quickly which assumptions hold.

## When to use
- A team has an outcome (OKR, North Star input) and must decide where to focus.
- Discovery findings pile up without a structure for decisions.
- Stakeholders push solutions and the team needs to show alternatives and rationale.

## When not to use
- There is no agreed outcome yet. Use `okr-definition` or `north-star-metric`.
- You only need to write one hypothesis. Use `hypothesis-statement`.
- You need the detailed design of one experiment. Use `experiment-design`.

## Inputs
Required:
- One measurable outcome the team can influence.

Optional, improves quality:
- Research: interviews, journey maps, feedback themes, analytics.
- Solution ideas already on the table, team constraints.

If the outcome is missing or is an output ("launch X"), ask for or propose an outcome. Opportunities without evidence are marked `[ASSUMPTION]`.

## Process
1. Put the outcome at the root, phrased as a metric the team can move (product outcome, not business lagging metric).
2. Derive opportunities from research: customer needs, pains or desires, phrased from the customer's perspective, never as solutions.
3. Structure opportunities hierarchically: broad parent opportunities, then specific child opportunities that are small enough to address.
4. Assess each child opportunity on size (how many, how often), importance to customers, alignment with strategy and evidence strength. Choose one target opportunity.
5. Generate at least three distinct solutions for the target opportunity, including a non-software option.
6. For each solution list key assumptions by type: desirability, viability, feasibility, usability, ethics.
7. Pick the riskiest assumptions and define small tests (prototype, fake door, one-question survey, data check), each with a success threshold.
8. Present the tree as a nested list or diagram, plus the decision log and next tests.
9. Mark every point you inferred rather than read in the input as `[ASSUMPTION]` and carry it into assumptions or open questions. If the user's goal continues, suggest the next skill: `hypothesis-statement` and `experiment-design` for the top solution, or `assumption-mapping` to rank its riskiest assumptions.

## Output format
```markdown
# Opportunity Solution Tree: <outcome>
- **Outcome:** <metric, baseline, target>
  - Opportunity A: "<customer need/pain>" (evidence)
    - A1: "..." ← target (size, importance, evidence)
      - Solution 1: ...
        - Assumption: ... → Test: ... → Threshold: ...
      - Solution 2: ...
      - Solution 3: ...
    - A2: "..."
  - Opportunity B: ...

## Why This Target Opportunity
...
## Next Tests
| Test | Assumption | Method | Threshold | Owner | Duration |
|---|---|---|---|---|---|
```

## Quality checklist
- [ ] The root is a single measurable product outcome.
- [ ] Opportunities are customer needs or pains, not disguised solutions.
- [ ] At least three solutions exist for the target opportunity.
- [ ] Each test has a success threshold defined before running it.
- [ ] Evidence strength is visible for opportunities.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing solutions as opportunities ("need a chatbot"). Rephrase from the customer's view.
- Working on many opportunities at once. Focus on one target, compare solutions within it.
- Testing whole ideas instead of assumptions. Test the riskiest assumption cheaply.

## Example
Input: "Increase 30-day retention of new mobile banking users."

Excerpt of output:
- Outcome: share of new users with 3+ sessions in first 30 days, baseline `[UNKNOWN]`.
- Opportunity: "I don't see why I would open the app if my salary goes to another bank" (interviews 7/12).
- Solutions: salary transfer incentive; bill-payment reminders; branch staff setup session.
- Test: fake-door "move your salary" banner, threshold ≥5% tap rate `[ASSUMPTION]`.
