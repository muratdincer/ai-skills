---
description: Turns a product idea, feature request or assumption into a falsifiable hypothesis in the "We believe / will result in / We will know when" format, with the target segment, the riskiest assumption, a measurable signal, a threshold and a time box. Use when a team wants to test an idea before building it fully, when a backlog item lacks a clear expected outcome, or when someone asks to write, sharpen or review a product hypothesis.
related: experiment-design, assumption-mapping, opportunity-solution-tree, problem-statement, ab-test-analysis
prompt: Write a hypothesis for adding a "save cart for later" button; we think it will reduce checkout abandonment on mobile.
---

# Write a Product Hypothesis

## Purpose
Express an idea as a testable bet that states who changes behavior, how, and what evidence will confirm or refute it, so the team decides in advance what "worked" means instead of rationalizing results afterwards.

## When to use
- An idea or feature request arrives with an implied benefit but no measurable expected outcome.
- A solution in an opportunity solution tree needs to be tested before investment.
- A team is about to run an experiment and needs the bet written down first.
- A shipped feature is being reviewed and the original expectation was never stated.

## When not to use
- The problem itself is not yet understood. Use `problem-statement` or `problem-interview-script`.
- The hypothesis exists and the test mechanics (variants, sample, stop rules) are needed. Use `experiment-design`.
- Many assumptions must be ranked before choosing which to test. Use `assumption-mapping`.

## Inputs
Required:
- The idea, change or assumption to test, and the problem or opportunity it addresses.

Optional, improves quality:
- Target segment, current baseline for the relevant metric, available traffic or users.
- Evidence behind the idea (research, support data, analytics).
- The decision the result will inform and who makes it.

If the idea or its intended problem is missing, ask for it. Missing baselines become `[UNKNOWN]` with a measurement action; never invent them.

## Process
1. Restate the idea and separate the proposed change (what we will do) from the claimed benefit (what we expect to change). Mark any benefit the user only implied as `[ASSUMPTION]`.
2. Name the specific segment whose behavior should change (e.g. "first-time mobile buyers with 3+ items in cart"), not "users".
3. Identify the underlying assumptions (desirability, usability, feasibility, viability) and pick the riskiest one: the one that would kill the idea if wrong and has the least evidence.
4. Write the hypothesis: "We believe that <change> for <segment> will result in <behavior change>. We will know we are right when <metric> moves from <baseline> to <threshold> within <time box>."
5. Choose one primary metric that measures behavior (not opinion or output), plus 1-2 guardrail metrics that must not degrade.
6. Set the threshold as the smallest change that would justify the investment; if the user cannot give one, propose a candidate and mark it `[ASSUMPTION]`.
7. State the falsification rule and the decision it triggers: what result makes us stop, iterate or scale.
8. Suggest the cheapest credible test type (interview, prototype test, fake door, concierge, A/B) matched to the riskiest assumption.
9. List evidence so far and open questions (baseline source, traffic, owner).
10. If the user's goal continues, suggest the next skill: `experiment-design` to plan the test, or `assumption-mapping` if several assumptions compete for testing.

## Output format
```markdown
# Hypothesis: <short name>
**Riskiest assumption:** <type> – <statement>

> We believe that **<change>** for **<segment>**
> will result in **<observable behavior change>**.
> We will know we are right when **<primary metric>** moves from **<baseline | [UNKNOWN]>** to **<threshold>** within **<time box>**.

| Item | Value |
|---|---|
| Primary metric | <name, definition, source> |
| Guardrail metrics | <metric – must not drop below X> |
| Falsified if | <result> |
| Decision on success / failure | <scale / iterate / stop> |
| Suggested test | <type> – <why it fits this assumption> |
| Decision owner | <name or [UNKNOWN]> |

## Evidence So Far
- <source> – <what it suggests>

## Assumptions and Open Questions
- [ASSUMPTION] ...
- <question> – <who can answer>
```

## Quality checklist
- [ ] The segment is specific and the behavior change is observable.
- [ ] The metric measures behavior, not opinions, page views of the feature itself, or delivery.
- [ ] A threshold and a time box exist, and a result that would refute the hypothesis is stated.
- [ ] Baselines and thresholds are sourced or marked `[UNKNOWN]` / `[ASSUMPTION]`.
- [ ] The suggested test targets the riskiest assumption, not the easiest one.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing an unfalsifiable hypothesis ("will improve the experience"). Force a metric and threshold that could come out wrong.
- Measuring usage of the new feature as success. Clicks on the button prove curiosity, not the outcome; measure the downstream behavior.
- Bundling several changes into one hypothesis. Split them, or you cannot tell which one worked.

## Example
Input: "Add a 'save cart for later' button; we think it will reduce checkout abandonment on mobile."

Weak: "We believe a save-for-later button will improve conversion."

Strong (excerpt):
> We believe that a "save cart for later" option for mobile visitors with 3+ items in cart will result in more of them returning to complete the purchase. We will know we are right when 7-day cart recovery rate moves from [UNKNOWN – measure current] to +3 pp within 4 weeks.
- Riskiest assumption (desirability): mobile abandoners intend to buy later rather than abandoning on price `[ASSUMPTION]`.
- Guardrail: same-session conversion must not drop by more than 1 pp.
