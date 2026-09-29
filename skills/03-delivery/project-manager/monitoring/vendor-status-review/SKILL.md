---
name: vendor-status-review
description: "Reviews a vendor's delivery performance against the contract or statement of work: deliverables and milestones, SLA and KPI results, quality, staffing, invoices and open obligations on both sides, and produces a scored assessment with evidence, issues and agreed actions. Use before a periodic vendor governance meeting, when a supplier is slipping, before approving an invoice or milestone payment, or when deciding whether to escalate or invoke contract remedies."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: project-manager
  area: monitoring
  title: "Review vendor performance"
  related: "statement-of-work, sla-breach-analysis, issue-management, acceptance-certificate, vendor-evaluation"
  prompt: "Prepare the monthly performance review for our implementation partner using the SOW milestones, their status report and our SLA report."
---

# Review Vendor Performance

## Purpose
Give an evidence-based view of whether a vendor is meeting its contractual commitments, what is at risk and what both parties must do next, so that payments, escalations and relationship decisions rest on facts.

## When to use
- Periodic (e.g. monthly or quarterly) vendor governance or service review.
- A supplier misses milestones, SLA targets or quality expectations.
- Before approving a milestone payment or invoice.
- Before renewal, extension or exit discussions.

## When not to use
- Selecting a new vendor. Use `vendor-evaluation`.
- Detailed analysis of one SLA breach. Use `sla-breach-analysis`.
- Formal acceptance of a specific deliverable. Use `acceptance-certificate`.

## Inputs
Required:
- The contractual baseline: SOW, contract obligations, milestones, SLA/KPI definitions (or relevant excerpts).
- Performance evidence for the period: vendor status report, SLA/KPI measurements, delivery records.

Optional, improves quality:
- Invoices and payment schedule, change orders, previous review actions.
- Internal team feedback, defect data, staffing plan vs actual.

If the contractual baseline or the period's evidence is missing, ask for it. Do not score what cannot be evidenced.

## Process
1. Set the review period and list the obligations due in it: deliverables, milestones, SLA/KPI targets, staffing commitments, reporting duties.
2. Also list the client's own obligations (access, decisions, environments, reviews) and whether they were met; vendor delays caused by client dependencies must be separated.
3. Compare each obligation to evidence: met, partially met, not met, not measurable. Cite the source for each; where evidence is missing write `[UNKNOWN]`, and label every inference `[ASSUMPTION]` and move it to open questions.
4. Evaluate SLA/KPI results against the contract formula (measurement window, exclusions, service credits); do not re-define targets.
5. Assess quality signals: defect rates, rework, acceptance rejections, documentation completeness.
6. Check commercial position: invoiced vs accepted deliverables, pending change orders, credits due; flag invoices for unaccepted work.
7. Score each area on a stated scale (e.g. 1-5) with a one-line justification; keep internal team opinions labeled as perceptions, not evidence.
8. Identify issues and risks, and decide which need contractual escalation versus relationship-level resolution.
9. Draft agreed actions for both sides with owners and dates, and carry over open actions from the last review.
10. If the user's goal continues, suggest `sla-breach-analysis` for a specific breach, `issue-management` for a vendor issue or `acceptance-certificate` to accept delivered items.

## Output format
```markdown
# Vendor Performance Review: <vendor> – <period>
Contract / SOW ref: <...> | Reviewers: <...>

## Summary
<overall rating, top 3 points, decisions needed>

## Obligations vs Evidence
| Obligation | Due | Result (Met/Partial/Not met/Not measurable) | Evidence |

## SLA / KPI Results
| Metric | Target | Actual | Status | Credit / remedy |

## Client-Side Obligations
| Obligation | Met? | Effect on vendor |

## Scorecard
| Area | Score (1-5) | Justification |
| Delivery / Quality / SLA / Staffing / Communication / Commercial |

## Commercial Position
## Issues, Risks and Escalations
## Assumptions and Open Questions
## Actions
| # | Action | Party | Owner | Due | Status |
```

## Quality checklist
- [ ] Every rating cites contract terms and evidence, not impressions.
- [ ] Client-side dependencies are assessed separately.
- [ ] SLA results use the contract's formula and exclusions.
- [ ] Invoices are reconciled against accepted deliverables.
- [ ] Actions have owners on both sides and dates.
- [ ] Personal data about vendor staff is limited to roles needed for the review.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Relying on the vendor's own green status report. Verify with independent evidence.
- Ignoring client-caused delays; this weakens any later claim or remedy.
- Escalating everything contractually; reserve formal remedies for material or repeated breaches.

## Example
Input: "SOW milestone M3 (data migration) due 15th, vendor reports 90% done; SLA P1 response 30 min, 2 of 5 missed."

Excerpt of output:
- M3 Data migration – Due 15th – Not met – vendor report says 90%; no accepted migration run yet.
- P1 response: 3/5 within 30 min (60%) vs target `[contract %]` – Not met – credit per clause `[ref]` to verify.
- Client side: production data extract delivered late `[confirm date]` – may explain part of M3 delay.
