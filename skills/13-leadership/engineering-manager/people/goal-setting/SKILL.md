---
name: goal-setting
description: "Drafts 3-5 SMART individual goals for an engineer or team member that connect team outcomes with the person's growth, each with measures, milestones and the support needed. Use at the start of a review period, after a promotion or role change, or when goals are vague, activity-based or disconnected from team priorities."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 13-leadership
  role: engineering-manager
  area: people
  title: "Set individual goals"
  related: "okr-definition, performance-review, career-development-plan, career-ladder, one-on-one-prep"
  prompt: "Help me set H2 goals for Deniz, a mid-level backend engineer. Team OKR is cutting checkout latency and she wants to grow toward senior."
---

# Set Individual Goals

## Purpose
Give a person a small set of goals they helped shape, that are measurable, within their influence, and clearly linked to team outcomes and their own development.

## When to use
- A new review period or iteration of goal setting starts.
- Someone changes role, level or team.
- Existing goals are task lists ("finish ticket X") or cannot be assessed at period end.

## When not to use
- Team- or company-level objectives. Use `okr-definition`.
- A long-term development roadmap across levels. Use `career-development-plan`.
- Goals within a formal improvement process. Use `underperformance-plan`.

## Inputs
Required:
- The person's role and level, the goal period, and the team's priorities or objectives for that period.

Optional, improves quality:
- The person's own aspirations and self-identified growth areas.
- Career ladder expectations for current and next level.
- Last review's focus areas; known capacity limits (on-call, leave, part-time).

If team priorities are missing, ask; goals without them drift into activity lists.

## Process
1. List team outcomes for the period and identify which ones this person can materially influence.
2. Draft 2-3 impact goals tied to those outcomes. State the outcome, not the task.
3. Draft 1-2 growth goals from the person's aspirations and the gap to the next level expectations.
4. Make each goal SMART: specific, measurable (metric or observable evidence), achievable given capacity, relevant, time-bound with a date.
5. For goals that cannot be measured by a number, define observable evidence (e.g. "led two design reviews that were accepted").
6. Check influence: remove or reword goals whose success depends mostly on other teams or luck.
7. Add milestones (e.g. mid-period checkpoint) and the support the manager commits to (access, time, mentoring, budget).
8. Balance the set: no more than five goals, at most one stretch goal clearly labeled as such.
9. Check fairness: comparable scope and difficulty to peers at the same level; capacity adjusted for part-time or planned leave without lowering the bar for the level.
10. Mark proposed values the person has not confirmed as `[ASSUMPTION]` and plan to finalize them together.
11. If the user's goal continues, suggest `career-development-plan` for growth goals, or `performance-review` at period end to assess them.

## Output format
```markdown
# Goals: <name> – <period>
Role / level: <role, level> · Linked team objectives: <list>

| # | Goal (outcome) | Type | Measure / evidence | Target & date | Milestone | Support from manager |
|---|---|---|---|---|---|---|
| 1 | ... | Impact / Growth / Stretch | ... | ... | ... | ... |

## Link to Team Outcomes
- Goal 1 → <team objective>

## Link to Growth
- Goal <n> → <ladder expectation or aspiration>

## Assumptions and Open Points
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] 3-5 goals, each stated as an outcome, not a task.
- [ ] Each goal has a measure or observable evidence and a date.
- [ ] Success is mainly within the person's influence.
- [ ] At least one goal supports growth toward their stated aspiration.
- [ ] Manager commitments are listed.
- [ ] Goals are comparable in scope to peers at the same level.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Output metrics that are easy to game (number of PRs, story points). Prefer outcomes or quality of evidence.
- Setting goals for the person instead of with them. Present drafts as proposals to discuss.
- Static goals in a changing context. Plan a mid-period review and record changes.

## Example
Input: "Deniz, mid-level backend. Team OKR: checkout p95 below 300 ms. She wants to grow toward senior."

Excerpt of output:
| 1 | Reduce payment-service contribution to checkout p95 | Impact | p95 of payment call on dashboard | ≤ 120 ms by 30 Nov `[ASSUMPTION: baseline unknown]` | Profiling report by 15 Sep | Dedicated performance test environment |
| 2 | Lead the design of the retry/idempotency change | Growth | Design doc accepted in architecture review | By 31 Oct | Draft reviewed with tech lead | Pairing with staff engineer |
