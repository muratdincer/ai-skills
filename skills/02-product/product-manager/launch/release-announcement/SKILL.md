---
name: release-announcement
description: "Writes a customer-facing release announcement that leads with the benefit to the reader, explains what changed and who it affects, states availability and any action required, and ends with a clear next step, adapted to the channel (email, blog, in-app, social). Use when a feature or product version ships to customers, when release notes must be turned into marketing-ready copy, or when someone asks to \"announce\" or \"tell customers about\" a release."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-manager
  area: launch
  title: "Write a release announcement"
  related: "positioning-statement, go-to-market-plan, release-notes, announcement, microcopy"
  prompt: "Write a customer announcement for our new bulk-invoice upload feature, going out by email and in-app next Tuesday."
---

# Write a Release Announcement

## Purpose
Turn a shipped change into a short, benefit-first message that customers read, understand and act on, without overpromising or burying required actions, so the release drives adoption rather than support tickets.

## When to use
- A new feature, product version or significant improvement becomes available to customers.
- Internal release notes or a PRD must be rewritten as customer-facing copy.
- The same release needs consistent versions for email, blog, in-app and social channels.

## When not to use
- The audience is technical and wants a complete change list. Use `release-notes` or `changelog-entry`.
- The message is internal to employees. Use `announcement`.
- Launch strategy, timing and channel mix are undecided. Use `go-to-market-plan`.

## Inputs
Required:
- What is being released (feature description, release notes or PRD excerpt).
- The target audience (all customers, a plan tier, a segment, a region).

Optional, improves quality:
- Positioning statement or message pillars.
- Availability: date, rollout stages, plans/regions, pricing impact.
- Required customer action, breaking changes, deprecations.
- Channels and length limits; brand voice guide; links to docs or demo.
- Customer quote or result (only if real and approved).

If the release content or audience is missing, ask. Mark everything else not provided `[TBD]`.

## Process
1. Identify the audience and what they care about; if segments differ materially (admins vs end users), plan separate versions.
2. Translate each feature into a customer benefit: what they can now do, how much faster or safer, or which pain disappears. Keep only the one to three benefits that matter most to this audience. Mark inferred benefits `[ASSUMPTION]`.
3. Write the headline as the benefit, not the feature name or internal code name.
4. Write a lead paragraph (2-3 sentences) answering: what is new, who it is for, why it matters.
5. Explain how it works in plain language with one concrete scenario; cut internal jargon and architecture details.
6. State availability precisely: date, plans, regions, rollout pace. Never imply general availability if it is staged.
7. Surface anything the reader must do (opt in, update, reconfigure) and any breaking change or deprecation, visibly and early, with a date.
8. Add one clear call to action and supporting links (docs, video, contact).
9. Adapt for each requested channel: email (subject + preview text), blog (full), in-app (one or two lines + link), social (short hook). Respect length limits.
10. Check claims: every number, quote and comparison must come from the inputs; otherwise remove or mark `[NEEDS PROOF]`. Check tone against the brand guide.
11. If the goal continues, suggest `go-to-market-plan` for wider launch activities, `release-notes` for the technical change list, or `microcopy` for in-product text.

## Output format
```markdown
# Release Announcement: <feature / version>
Audience: <segment> · Channels: <list> · Availability: <date / plans / regions>

## Headline
<benefit-led headline>

## Lead
<what is new, for whom, why it matters — 2-3 sentences>

## What You Can Do Now
- <benefit 1 with concrete scenario>
- <benefit 2>

## Availability
<date, plans, regions, rollout>

## Action Required (if any)
<what, by when, how>

## Call to Action
<one action + link>

## Channel Versions
- Email subject / preview: ...
- In-app: ...
- Social: ...

## Assumptions and Items to Confirm
- [ASSUMPTION] / [TBD] / [NEEDS PROOF] ...
```

## Quality checklist
- [ ] The headline and lead state a customer benefit, not a feature name.
- [ ] Availability (date, plans, regions, rollout) is precise and not overstated.
- [ ] Required actions and breaking changes are visible before the fold, with dates.
- [ ] There is exactly one primary call to action.
- [ ] No invented numbers, quotes or comparisons; unsupported claims are removed or marked.
- [ ] Internal jargon and code names are gone; inferences are labeled.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Listing everything shipped. Customers skim; choose the few benefits that matter to this audience and link to full notes.
- Hiding the required action or price change at the bottom. It damages trust and creates tickets; put it near the top.
- Announcing to all customers a feature that is staged by plan or region. Say who has it and when others will.

## Example
Input: "Bulk invoice upload: up to 500 PDFs at once, auto-extracts fields. All paid plans, rolling out from Tuesday."

Weak headline: "Introducing BulkUpload v2.3 with the new OCR pipeline"

Strong (excerpt):
- Headline: "Upload a month of invoices in one go"
- Lead: "You can now drop up to 500 invoice PDFs at once, and we fill in supplier, date and amount for you. Month-end entry that took hours becomes a review step `[ASSUMPTION: confirm time-saving claim]`."
- Availability: "Rolling out to all paid plans from Tuesday `[TBD: date]`; every account will have it within `[TBD]` days."
