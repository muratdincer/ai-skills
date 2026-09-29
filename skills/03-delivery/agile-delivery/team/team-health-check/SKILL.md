---
name: team-health-check
description: "Designs and analyzes a team health check: selects 8-12 dimensions (e.g. delivering value, speed, codebase health, learning, mission clarity, fun, support, psychological safety), writes traffic-light or 1-5 rating statements, runs it anonymously, reads results and trends per dimension, and turns the lowest or declining areas into a few owned follow-up actions. Use when a team or manager wants to take the team's pulse, compare with a previous round, or prepare a health check session."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: agile-delivery
  area: team
  title: "Run a team health check"
  related: "retrospective-facilitation, working-agreement, agile-maturity-assessment, questionnaire-design, engineering-metrics-review"
  prompt: "Here are our health check results from last quarter and this quarter across 10 dimensions (green/yellow/red per person). What stands out and what should we do?"
---

# Run a Team Health Check

## Purpose
Give the team a safe, repeatable way to see how it is doing across the dimensions that matter to it, spot trends early and pick a small number of improvements the team itself owns, without turning the results into a performance score.

## When to use
- A team wants a periodic pulse (e.g. quarterly) of its health.
- Results from a previous round exist and someone wants trends and actions.
- A new team lead or coach wants a structured baseline conversation.

## When not to use
- Scoring agile practices against a maturity model. Use `agile-maturity-assessment`.
- Designing a large organization-wide survey with sampling. Use `questionnaire-design`.
- Improving one iteration's way of working. Use `retrospective-facilitation`.

## Inputs
Required:
- Either the purpose and team context (to design a new health check) or the results per dimension (to analyze an existing one).

Optional, improves quality:
- Previous rounds' results for trends.
- Dimensions the team or organization already uses.
- Team events in the period (reorganization, incidents, new members).

If results are given as individual names with scores, remove the names and work on aggregates only; remind the user that identifiable answers undermine honesty.

## Process
1. Clarify the purpose: team self-reflection (default) versus input for management. If management will see results, recommend sharing only aggregates and themes agreed by the team.
2. Choose 8-12 dimensions and for each write a positive and a negative anchor statement (e.g. Codebase health – "Our code is easy to change safely" / "Every change feels risky"). Reuse existing dimensions to keep trends comparable.
3. Choose the scale: traffic light (green/yellow/red) plus trend arrow (improving/stable/declining), or 1-5. Keep the same scale across rounds.
4. Plan the run: anonymous individual voting first, then reveal the aggregate, then discussion. Timebox about 60-90 minutes; for remote teams use anonymous voting and a shared board.
5. Aggregate results per dimension: distribution (counts per color or mean and spread for 1-5) and trend vs previous round. High spread is a finding in itself; it means experiences differ.
6. Identify signals: dimensions that are red/low, declining for 2+ rounds, or strongly split. Rank them by team-perceived importance, not only by score.
7. For the top 1-3 signals, frame discussion questions ("What would green look like?", "What changed since last time?") and capture the team's explanations; label your own hypotheses `[INFERENCE]`.
8. Turn them into at most 3 actions, each with an owner in the team, a first step and a check date. Escalate only what the team cannot change and name it as a request to management.
9. Record the baseline and the next round's date; suggest `retrospective-facilitation` to work an action in depth or `working-agreement` if the findings are about norms.

## Output format
```markdown
# Team Health Check – <team>, <round/date>
Participants: <n of m> · Scale: <traffic light + trend / 1-5> · Previous round: <date or none>

| Dimension | Green | Yellow | Red | Trend vs last | Spread | Signal |
|---|---|---|---|---|---|---|

## Key Signals
1. <dimension> – <evidence> – team's explanation / [INFERENCE]

## Actions (max 3)
| Action | Owner | First step | Check on |
|---|---|---|---|

## Requests Outside Team Control
- ...

## Next Round
<date> · same dimensions and scale
```

## Quality checklist
- [ ] Individual answers are anonymous and no person is identifiable in the output.
- [ ] Dimensions and scale match earlier rounds, or the break in comparability is stated.
- [ ] Spread is reported, not only averages.
- [ ] Explanations come from the team; own hypotheses are labeled `[INFERENCE]`.
- [ ] No more than 3 actions, each with an owner, first step and check date.
- [ ] Results are not framed as a performance rating or compared across teams.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Using health check results to rank teams. Scores become political and honesty disappears.
- Changing dimensions every round. Trends, the main value, are lost.
- Collecting many actions and completing none. Pick few and check them next round.

## Example
Input: 10 dimensions, 7 participants, two rounds; "Codebase health" went from 4 green/3 yellow to 1 green/3 yellow/3 red.

Excerpt of output:
| Dimension | Green | Yellow | Red | Trend | Signal |
|---|---|---|---|---|---|
| Codebase health | 1 | 3 | 3 | Declining | Top signal |
| Fun | 5 | 2 | 0 | Stable | – |
- Hypothesis `[INFERENCE]`: the new payment module release pressure; confirm in discussion.
- Action: reserve capacity for the two riskiest modules' test coverage – owner: tech lead – check next round.
