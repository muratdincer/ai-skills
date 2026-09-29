---
description: "Builds a product roadmap tied to outcomes, either as Now/Next/Later or as a timeline with confidence levels, showing themes, target outcomes, key initiatives, dependencies, what is explicitly not planned and how the roadmap will be updated. Use when a product owner or manager needs to communicate direction to stakeholders, align teams for the coming quarters, or turn a feature list into an outcome-based plan."
related: "product-vision, okr-definition, release-planning, backlog-prioritization, program-roadmap"
prompt: "Turn this list of 25 feature requests into a Now/Next/Later roadmap for our HR self-service app; our goals this year are fewer HR tickets and better mobile adoption."
---

# Build a Product Roadmap

## Purpose
Communicate where the product is heading and why, in a form that aligns stakeholders on outcomes and sequence while remaining honest about uncertainty. A good roadmap is a statement of intent and priorities, not a delivery contract.

## When to use
- Planning the next quarters or a planning increment and communicating it to leadership, sales or other teams.
- A feature list or backlog needs to be translated into strategic themes.
- Stakeholders keep asking "when will X come?" and the answer must be consistent.
- After a strategy change, to show what moves and what is dropped.

## When not to use
- Committing scope and dates for one specific release. Use `release-planning`.
- Coordinating milestones of many teams in a program. Use `program-roadmap`.
- Setting the long-term aspiration itself. Use `product-vision`.

## Inputs
Required:
- Product goals or outcomes for the horizon (OKRs, strategy, vision). If absent, ask; a roadmap without goals is a feature list.
- Candidate initiatives or features.

Optional, improves quality:
- Audience (executives, customers, internal teams) and horizon (e.g. 12 months).
- Capacity signals, known commitments, regulatory dates, dependencies.
- Preferred format: Now/Next/Later or timeline.

## Process
1. Clarify the audience and horizon; this decides granularity and whether dates appear. External audiences get less date precision.
2. Choose the format: Now/Next/Later when uncertainty is high or the team works in continuous flow; timeline with quarters when external dates, contracts or regulation drive the plan.
3. Group candidate items into 3-6 themes, each linked to a goal and a measurable outcome.
4. Place themes/initiatives into horizons based on priority, dependencies and capacity. Now = committed and in progress; Next = planned, being refined; Later = direction, open to change.
5. Assign a confidence level to each placement (High/Medium/Low) and state the main assumption behind it.
6. Mark fixed-date items separately with the source of the date (regulation, contract, event).
7. Record key dependencies and risks that could move items between horizons.
8. List what is explicitly not on the roadmap and why; this prevents silent expectations.
9. Define the update cadence and change rule (e.g. reviewed monthly; changes to Now are communicated to stakeholders).
10. Draft a short narrative (3-5 sentences) the owner can use when presenting.

## Output format
```markdown
# Product Roadmap: <product> – <horizon>
Audience: <audience> · Last updated: <date> · Next review: <date or [TBD]>

## Goals
- G1: <goal> – outcome metric: <metric>

## Roadmap
| Theme (goal) | Now | Next | Later |
|---|---|---|---|
| <theme> (G1) | <initiative> [H] | <initiative> [M] | <initiative> [L] |

## Fixed-Date Commitments
- <item> – <date> – <source>

## Key Assumptions, Dependencies and Risks
- <item>

## Not on the Roadmap
- <item> – <reason>

## How This Roadmap Changes
<cadence, change rule, communication>

## Narrative
<3-5 sentences>
```

## Quality checklist
- [ ] Every item links to a goal and an outcome metric.
- [ ] Confidence is shown per item, lowest for Later.
- [ ] Dates appear only where justified by a real source; otherwise horizons are used.
- [ ] A "Not on the roadmap" section exists.
- [ ] Detail matches the audience (no ticket-level items for executives).
- [ ] No capacity, revenue or date figures are invented.

## Common pitfalls
- Presenting a Later item with a date. Stakeholders treat it as a promise; keep dates for committed work.
- Listing features instead of problems/outcomes. Frame items as "Reduce payroll questions via self-service payslip" rather than "Payslip screen".
- Overloading Now. If Now exceeds real capacity, nothing moves; keep it to what is actually in progress.

## Example
Input: "HR self-service app. Goals: fewer HR tickets, better mobile adoption. 25 requests."

Excerpt of output:
| Self-service answers (G1: HR tickets -20%) | Payslip and leave balance self-service [H] | Policy search with top 20 questions [M] | Chat-based HR assistant [L] |
| Mobile first (G2: mobile MAU share) | Mobile leave request [H] | Push notifications for approvals [M] | Offline mode [L] |
- Not on the roadmap: Custom report builder – serves few users, no link to either goal.
