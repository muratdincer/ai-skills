---
name: alert-design
description: "Designs a paging and ticketing alert set for a service: symptom-based alerts tied to SLOs, multi-window multi-burn-rate conditions, severity and routing, runbook links and an audit of existing noisy alerts. Use when alerts are missing, noisy, cause-based (CPU, disk) instead of user-impacting, when on-call is burning out, or when new SLOs need alerting."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: sre
  area: reliability
  title: "Design alerts"
  related: "slo-definition, error-budget-policy, observability-plan, runbook, incident-response"
  prompt: "Design alerts for our payments API. SLO is 99.9% availability over 28 days; today we page on CPU > 80% and get 40 pages a week."
---

# Design Alerts

## Purpose
Produce a small set of alerts where every page means real or imminent user impact that a human must act on now, and everything else becomes a ticket or a dashboard, so on-call load stays sustainable and incidents are caught early.

## When to use
- A service has SLOs but no alerting on them, or alerts only on resource metrics.
- On-call reports alert fatigue: frequent pages, flapping, pages with no action.
- A new service is going live and needs a paging policy.

## When not to use
- No SLIs or SLOs exist yet. Use `slo-definition` first; burn-rate alerts need them.
- The telemetry itself is missing (no metrics, logs, traces). Use `observability-plan`.
- The question is how to respond once paged. Use `runbook` or `incident-response`.

## Inputs
Required:
- The service and its SLOs (or at least the user-facing symptoms that matter).
- The current alert list, or a statement that there is none.

Optional, improves quality:
- Alert history: counts per alert, actioned vs. ignored, time to acknowledge.
- On-call structure: rotations, hours, escalation paths, paging channels.
- Available signals and the alerting engine's capabilities (windows, recording rules).

If SLOs and symptoms are both unknown, ask for them first. Do not guess thresholds; mark proposed values `[PROPOSED]`.

## Process
1. Inventory existing alerts with volume and outcome; classify each as symptom (user impact) or cause (resource, component state). Mark the history as `[UNKNOWN]` if not provided.
2. For each SLO, define burn-rate alerts: a fast-burn page (e.g. 2% of the budget in 1 hour, 14.4x) and a slow-burn page or ticket (e.g. 5% in 6 hours, 6x; 10% in 3 days, 1x), each with a short confirmation window to reset quickly.
3. Add symptom alerts that the SLO does not cover: total traffic drop to zero, stuck queues or data freshness for pipelines, certificate expiry, synthetic probe failures on low-traffic paths.
4. Demote cause-based alerts (CPU, memory, disk, pod restarts) to tickets or dashboards unless they predict imminent user impact with a clear lead time (e.g. disk full in under 4 hours by linear projection).
5. Assign severity and routing: page (act now, 24/7), ticket (act within business hours), log-only. Every page must name an owning rotation and escalation path.
6. For each alert write the payload: summary with the user impact, current value vs. threshold, dashboard link, runbook link, and the first diagnostic step.
7. Remove noise mechanisms: minimum duration or confirmation windows, grouping and deduplication by service, inhibition of downstream alerts when an upstream dependency alert fires, maintenance silences with expiry.
8. Estimate expected page volume; if it exceeds a sustainable level (a common heuristic is at most two incidents per 12-hour shift), raise thresholds or move alerts to tickets and note the trade-off.
9. Define the review loop: every page is tagged actionable or not, and alerts with a low action rate are tuned or deleted at a regular review.
10. Label every inference `[ASSUMPTION]` and list open questions. If the goal continues, suggest `runbook` for each paging alert, `observability-plan` for missing signals, or `error-budget-policy` for what happens when budget burns.

## Output format
```markdown
# Alert Design: <service>
SLOs covered: <list> · On-call rotation: <name or [UNKNOWN]>

## Current Alert Audit
| Alert | Type (symptom/cause) | Volume/week | Actioned % | Decision (keep/tune/ticket/delete) |

## Alert Catalog
| Name | Condition (window, threshold) | Severity | Route | Runbook | Rationale |

## Notification Payload Template
## Noise Controls (grouping, inhibition, silences)
## Expected Load and Review Cadence
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every paging alert reflects user impact or imminent user impact with stated lead time.
- [ ] SLO alerts use burn rates over at least two windows, not a raw error-rate threshold.
- [ ] Every page has an owner, a runbook link and a first diagnostic step.
- [ ] Cause-based alerts are demoted or justified individually.
- [ ] Thresholds without data are marked `[PROPOSED]`.
- [ ] Expected page volume is estimated and a review loop is defined.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Paging on a single short window error rate: it flaps on low traffic and misses slow burns. Use multi-window burn rates and a minimum request count.
- Keeping an alert "just in case". An alert nobody acts on trains on-call to ignore pages; delete or demote it.
- Alerting on every dependency separately. Inhibit downstream noise and page on the user symptom once.

## Example
Input: "Payments API, 99.9% over 28 days, pages on CPU > 80%, ~40 pages/week, most auto-resolve."

Excerpt of output:
| Name | Condition | Severity | Route |
|---|---|---|---|
| PaymentsFastBurn | burn rate > 14.4 over 1h AND > 14.4 over 5m | Page | payments-oncall |
| PaymentsSlowBurn | burn rate > 6 over 6h AND > 6 over 30m | Page | payments-oncall |
| PaymentsBudgetDrift | burn rate > 1 over 3d AND > 1 over 6h | Ticket | payments-team |
| HighCPU | CPU > 80% for 10m | Delete (auto-resolves, no user impact recorded) `[ASSUMPTION: confirm with history]` | - |
