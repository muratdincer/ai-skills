---
description: Writes a go-to-market plan for a product or major feature covering launch tier, target segment and buyer, positioning and messages, channels, pricing and packaging hooks, timeline with readiness gates, sales/support enablement and launch success metrics. Use when a product, feature or market entry is heading to launch, when someone asks for a GTM or launch plan, or when marketing, sales and support need one aligned plan.
related: positioning-statement, release-announcement, pricing-analysis, competitive-battle-card, communication-plan
prompt: Write a go-to-market plan for launching our AI-assisted invoice matching module to existing mid-market ERP customers.
---

# Write a Go-to-Market Plan

## Purpose
Align product, marketing, sales, support and operations on who the launch targets, what it says, how it reaches them, when each team must be ready and how success is judged, so launch is a coordinated event rather than a release date.

## When to use
- A new product, major feature, new segment or new market is approaching launch.
- Several teams (marketing, sales, customer success, support, legal) must prepare in parallel.
- Leadership asks how a launch will generate adoption or revenue.

## When not to use
- Only the core positioning is undecided. Use `positioning-statement` first.
- Only the customer-facing announcement text is needed. Use `release-announcement`.
- The release is an internal or minor change needing only release notes. Use `release-notes`.

## Inputs
Required:
- What is launching (capability and main benefit), target customers, and the intended launch window.

Optional, improves quality:
- Positioning, competitor context, pricing/packaging decisions, business goal.
- Available channels and budget, sales motion (self-serve, sales-led, partner), regulatory constraints.

If the target customer or the launch scope is missing, ask. Do not invent budgets, dates or targets; mark them `[TBD]`.

## Process
1. Set the launch tier (e.g. Tier 1 market-moving, Tier 2 notable, Tier 3 quiet) from customer impact, revenue potential and competitive significance; the tier scales the effort of every later step.
2. Define the target: segment, ideal customer profile, buyer vs user vs influencer roles, and existing vs new customers. Name the segment explicitly excluded for now.
3. State the positioning in one line and derive a message house: core message, 3 supporting pillars each with proof points. Mark unproven claims `[ASSUMPTION]` or remove them.
4. Decide pricing and packaging touchpoints: included, add-on, new tier, trial/pilot terms; flag any decision still open with its owner.
5. Choose channels per audience and funnel stage (awareness, consideration, conversion, expansion): e.g. in-app, email to existing base, webinars, partners, sales outreach, PR. Justify each by audience fit.
6. Plan enablement: sales pitch and demo, objection handling, battle card, support FAQ and troubleshooting, documentation, pricing/quoting setup, partner briefings.
7. Build the timeline backward from launch day with readiness gates (e.g. T-6 weeks messaging locked, T-2 weeks enablement done, T-1 week go/no-go) and owners; include beta or early-access phase if relevant.
8. Define launch success metrics across horizons: leading (reach, trials, demo requests), adoption (activation among target accounts), business (pipeline, expansion revenue, churn impact). Baselines and targets given or `[TBD]`.
9. List risks and mitigations (readiness slip, capacity, compliance review, competitor response) and the go/no-go criteria.
10. Mark inferences `[ASSUMPTION]`. If the user's goal continues, suggest the next skill: `positioning-statement` if positioning is weak, `release-announcement` for the customer message, `competitive-battle-card` for sales, or `communication-plan` for detailed sequencing.

## Output format
```markdown
# Go-to-Market Plan: <product/feature> · launch window <...> · Tier <1/2/3>

## Target
- Segment / ICP: ... · Buyer / user / influencer: ... · Not targeting now: ...

## Positioning and Message House
- One-liner: ...
- Pillars: 1. <message> – proof: <...> 2. ... 3. ...

## Pricing and Packaging
- ...

## Channels
| Audience | Stage | Channel | Why | Owner |
|---|---|---|---|---|

## Enablement
| Team | Asset / training | Owner | Due |
|---|---|---|---|

## Timeline and Readiness Gates
| When | Milestone / gate | Owner | Exit criteria |
|---|---|---|---|

## Success Metrics
| Horizon | Metric | Baseline | Target |
|---|---|---|---|

## Risks and Go/No-Go Criteria
- ...
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] The launch tier is stated and effort matches it.
- [ ] Target segment and buyer/user roles are specific; an excluded segment is named.
- [ ] Every message pillar has a proof point or is marked `[ASSUMPTION]`.
- [ ] Each team has enablement items with owners and dates (or `[TBD]`).
- [ ] Success metrics cover leading, adoption and business horizons; no invented targets.
- [ ] Go/no-go criteria and readiness gates are explicit.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Treating GTM as a marketing checklist. Without sales and support readiness, demand turns into lost deals and tickets.
- Launching to "everyone". A named ICP and an explicit non-target focus scarce channels.
- Measuring only launch-day reach. Plan adoption and business metrics for weeks after launch.

## Example
Input: "AI-assisted invoice matching module for existing mid-market ERP customers."

Excerpt of output:
- Tier 2: notable add-on for existing base; no new-market entry.
- Target: finance operations leads at existing customers processing high invoice volume `[ASSUMPTION: threshold TBD]`; buyer: CFO; not targeting now: new-logo prospects.
- Pillar: "Close the month faster" – proof: pilot results `[TBD, from beta customers]`.
- Gate T-2 weeks: support team trained on explaining low-confidence matches; FAQ covers data processing location (KVKK/GDPR question).
- Business metric: add-on attach rate among target accounts, baseline 0, target `[TBD]`.
