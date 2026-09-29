---
description: "Audits a backlog export or list for health problems (stale, duplicate, oversized, orphan, unowned, unprioritized or goal-less items, too much ready work or too little) and produces findings with metrics, a cleanup proposal and hygiene rules. Use when the backlog has grown unmanageable, nobody trusts it, before a planning cycle, or someone asks to clean up, audit or assess the backlog."
related: "backlog-refinement, backlog-prioritization, definition-of-ready, roadmap, cycle-time-analysis"
prompt: "Here is our backlog export with 340 items (title, type, created date, last updated, epic, status). Check its health and tell me what to delete."
---

# Check Backlog Health

## Purpose
Give the product owner an evidence-based picture of backlog hygiene and a concrete cleanup plan, so the backlog becomes a trusted, manageable tool that reflects current strategy instead of a wish archive.

## When to use
- The backlog contains hundreds of items and nobody can say what matters.
- Before quarterly or release planning, or after a strategy change.
- A new product owner takes over a product.
- The team complains about unclear or outdated items.

## When not to use
- Refining a handful of upcoming items. Use `backlog-refinement`.
- Ranking items. Use `backlog-prioritization`.
- Analyzing flow delays of in-progress work. Use `cycle-time-analysis`.

## Inputs
Required:
- The backlog list or export. Useful fields: ID, title, type, status, created date, last updated date, parent epic/goal, estimate, owner/requester. If no data is given, ask; work with whatever fields exist and note the missing ones.

Optional, improves quality:
- Current goals, roadmap themes or OKRs.
- Team throughput (items completed per iteration/sprint or per week).
- Organization rules (e.g. items older than N months are archived).

## Process
1. Profile the data: item count by type and status, age distribution (median, 85th percentile), share without parent/goal, without estimate or description.
2. Estimate backlog depth: items in ready or near-ready state divided by throughput gives weeks or iterations of ready work. Healthy ranges are roughly 1-3 iterations of ready work; flag too little (planning starvation) or far too much (waste).
3. Detect stale items: not updated beyond a threshold (default 6 months `[ASSUMPTION]`, or the organization's rule).
4. Detect likely duplicates by similar titles or same intent; list pairs with a confidence note.
5. Detect oversized items: estimates far above team norm, or vague titles covering multiple capabilities.
6. Detect orphan items: no link to an epic, goal or roadmap theme; and items whose parent goal was dropped.
7. Check order quality: top items align with current goals; bugs and technical debt are visible, not buried.
8. Classify every finding as delete/archive, merge, split, re-parent, refine or keep, with a reason.
9. Propose hygiene rules to prevent recurrence (intake filter, max age, max backlog size, review cadence) and a first cleanup session plan.
10. If the user's goal continues, suggest `backlog-refinement` for items flagged as unclear or oversized and `backlog-prioritization` to re-order what remains.

## Output format
```markdown
# Backlog Health Check: <product> – <date>
Data: <n items, fields available, fields missing>

## Health Summary
| Metric | Value | Signal |
|---|---|---|
| Total items | <n> | |
| Median age / 85th pct | <days> | |
| Stale (> <threshold>) | <n, %> | Red/Amber/Green |
| No parent goal | <n, %> | |
| Ready work depth | <iterations/weeks or [UNKNOWN]> | |
| Likely duplicates | <pairs> | |

## Findings and Proposed Action
| Item(s) | Issue | Action | Reason |
|---|---|---|---|

## Hygiene Rules Proposed
- <rule>

## First Cleanup Session
- Scope, participants, timebox, decisions needed
```

## Quality checklist
- [ ] Metrics are calculated only from supplied data; missing fields are stated.
- [ ] Thresholds used (staleness, size) are explicit and marked if assumed.
- [ ] Duplicates are presented as candidates with a confidence note, not auto-deleted.
- [ ] Every proposed deletion has a reason and can be reviewed by the product owner.
- [ ] Recommendations tie back to current goals when those are provided.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Keeping everything "just in case". Deleted items with real value come back; archive with a note instead of hoarding.
- Measuring only size. A small backlog of unrelated items is still unhealthy; check goal alignment.
- Cleaning once without rules. Without an intake filter and review cadence the backlog regrows within months.

## Example
Input: "340 items; fields: title, type, created, updated, epic."

Excerpt of output:
| Stale (> 180 days) | 142 (42%) | Red |
| No parent epic | 97 (29%) | Amber |
- "Export to Excel" (#88) and "Download list as XLSX" (#231) – likely duplicate, high confidence – merge into #231.
- Hygiene rule: items not updated for 180 days are archived at the monthly review unless the product owner re-confirms them.
