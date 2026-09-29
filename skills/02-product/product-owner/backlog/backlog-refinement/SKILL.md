---
description: "Prepares a set of backlog items for a refinement session and turns them into clear, right-sized, estimate-ready and ordered work items with acceptance criteria, open questions and a readiness verdict. Use when a backlog needs grooming, items are vague or too big before iteration/sprint planning, or someone asks to refine, clean up or get stories ready."
related: "story-splitting, definition-of-ready, acceptance-criteria, backlog-prioritization, estimation-session"
prompt: "Refine these 8 backlog items for next week's planning; tell me which are ready, which need splitting and what we still have to ask the business."
---

# Refine the Backlog

## Purpose
Move the top of the backlog from "ideas and fragments" to items the team can understand, size and pull without surprises. The result is a refined list with a readiness verdict per item and a short list of what still blocks each one.

## When to use
- Before iteration/sprint planning or before items are pulled into a flow board.
- Items have one-line titles, no acceptance criteria or unclear value.
- A new epic or feature has just been broken down and the pieces need tightening.
- The team regularly discovers missing information mid-work.

## When not to use
- The task is only to decide order across many items. Use `backlog-prioritization`.
- A single item is clearly too large and needs slicing. Use `story-splitting`.
- The whole backlog needs an audit for stale, duplicate or orphan items. Use `backlog-health-check`.

## Inputs
Required:
- The backlog items to refine (titles plus whatever description exists).

Optional, improves quality:
- Product/iteration goal, roadmap theme or target outcome.
- Team's Definition of Ready and Definition of Done.
- Estimation scale used (points, t-shirt, none) and recent throughput.
- Known dependencies, domain rules, UX or technical notes.

If no items are provided, ask for them. Treat missing optional inputs as open questions.

## Process
1. Restrict scope to the top of the backlog: roughly the next 1-2 iterations of work or the next few weeks of flow. Leave the rest untouched.
2. For each item, restate the value in one line: who benefits, what changes for them, why now. Flag items whose value cannot be stated.
3. Rewrite unclear titles into outcome language. Use the user story format only when it adds clarity; technical enablers may use "Enable X so that Y".
4. Draft 3-7 testable acceptance criteria per item (rule-based or Given/When/Then). Mark inferred ones `[ASSUMPTION]`.
5. Check size against the team's norm: if an item cannot plausibly be finished within one iteration or a few days of flow, recommend a split and name the split pattern (workflow step, business rule, data variation, interface, spike).
6. Identify dependencies (other teams, vendors, data, environments, decisions) and whether they are resolved.
7. List open questions per item with the person or role that can answer.
8. Evaluate each item against the Definition of Ready (or a default: value clear, AC testable, small enough, dependencies known, no blocking question).
9. Propose an order for the refined items with a one-line reason; defer detailed scoring to `backlog-prioritization`.
10. Produce the output and a short agenda for the refinement session covering only items that need team discussion.

## Output format
```markdown
# Backlog Refinement: <product/team> – <date>
Goal/theme: <goal or [UNKNOWN]>

| # | Item | Value (one line) | Size signal | Readiness | Blocking |
|---|---|---|---|---|---|
| 1 | <title> | <who/what/why> | OK / Split / Spike | Ready / Almost / Not ready | <question or dependency> |

## Item Details
### <#> <refined title>
- Description: <1-3 lines>
- Acceptance criteria:
  1. <criterion>
- Split proposal: <pattern and resulting items, or none>
- Dependencies: <item – owner – status>
- Open questions: <question – who answers>

## Proposed Order
1. <item> – <reason>

## Refinement Session Agenda
- <item>: <what the team must decide/estimate> (<minutes>)
```

## Quality checklist
- [ ] Every item has a one-line value statement or is flagged as lacking one.
- [ ] Acceptance criteria are testable and describe behavior, not implementation.
- [ ] Oversized items have a named split pattern, not just "split it".
- [ ] Readiness verdicts are consistent with the stated Definition of Ready.
- [ ] Nothing is invented: estimates, dates and owners come from input or are marked.
- [ ] The session agenda lists only items that need collective discussion.

## Common pitfalls
- Refining too far ahead. Detail decays; refine only what will be pulled soon.
- Producing estimates on behalf of the team. The skill prepares items; the team sizes them in `estimation-session`.
- Hiding unresolved dependencies behind "Ready". An external blocker makes the item Not ready.
- Writing tasks ("create table", "add endpoint") instead of user-visible or testable outcomes.

## Example
Input: "Items: 1) Export report, 2) Login with SSO, 3) Fix slow search."

Excerpt of output:
| 2 | Sign in with corporate SSO | Employees stop managing a separate password | Split | Not ready | Which identity provider and protocol? – IT security |
- Split proposal (interface): (a) SSO login for web, (b) SSO for mobile, (c) fallback login for external users.
- Item 3 open question: What is "slow" today and what response time is acceptable? `[UNKNOWN]`
