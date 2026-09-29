---
description: Plans the end-of-life of a product, plan or feature with explicit sunset decision criteria, affected-customer segmentation, migration paths, a staged communication sequence, timeline gates and data retention/deletion handling. Use when a product or feature is being retired, replaced or consolidated, or when someone asks "how do we shut this down without losing customers or trust".
related: communication-plan, migration-strategy, api-deprecation-plan, impact-analysis, kpi-definition
prompt: We want to retire our legacy reporting module next year and move everyone to the new analytics dashboard. Draft the sunset plan.
---

# Plan a Product or Feature End-of-Life

## Purpose
Retire a product or feature deliberately: a defensible decision, a migration path for every affected segment, a communication sequence customers can act on, and gates that stop the shutdown if the damage would exceed the saving.

## When to use
- A product, plan tier or feature has low usage, high maintenance cost or is replaced by a newer offering.
- Two overlapping products are being consolidated after a merger or re-platforming.
- Leadership has decided to exit a market segment and needs an executable plan.

## When not to use
- The retired element is a public or partner API contract. Use `api-deprecation-plan` (combine both when a product sunset includes an API).
- The work is a technical platform migration with no customer-facing change. Use `migration-strategy`.
- Only the announcement text is needed for an already approved plan. Use `communication-plan` or `release-announcement`.

## Inputs
Required:
- What is being retired (product, feature, plan) and the reason or trigger.

Optional, improves quality:
- Usage data by segment, revenue attached, contractual commitments (SLA, notice periods, term end dates).
- The replacement or alternative, if any, and its feature gaps.
- Internal cost of keeping it (support, infrastructure, security patching).
- Regulatory constraints on data retention and export (KVKK/GDPR, sector rules).

If the retired element or the reason is missing, ask for it. Everything else becomes `[UNKNOWN]` or an open question.

## Process
1. State the sunset scope precisely (what stops: sales, new sign-ups, feature, support, data access) and the stated reason; label any reason you infer `[ASSUMPTION]`.
2. Test the decision against explicit criteria: usage trend, revenue and contractual exposure, cost to keep, strategic fit, security/compliance risk, and availability of a replacement. Record which criteria are evidenced and which are `[UNKNOWN]`; if the case is weak, say so rather than planning anyway.
3. Segment affected customers (e.g. heavy users, light users, strategic/contracted accounts, integrators, internal teams) and estimate each segment's impact qualitatively. Never invent counts or revenue.
4. Define the migration path per segment: replacement product, feature-gap workarounds, data export/import, assisted migration, commercial incentive, or graceful exit. Flag segments with no viable path as a risk.
5. Check obligations: contractual notice periods, committed SLAs, renewals already signed, refunds, and data retention/deletion duties. Personal data must be exported to the customer or deleted per KVKK/GDPR; mask personal data in any examples.
6. Build the timeline as phases with gates: announce, stop new sales, feature freeze, migration window, read-only, shutdown, data deletion. Each gate has an entry condition (e.g. migrated share of active accounts, no open P1 tickets from strategic accounts) and an owner.
7. Draft the communication sequence per audience: internal first (sales, support, success, partners), then customers by segment, with channel, timing relative to shutdown (T-minus) and the call to action. Reminders escalate as the date approaches.
8. Prepare internal readiness: support FAQ and macros, sales guidance (what not to sell), billing changes, documentation banners, in-product notices, and monitoring of residual usage.
9. Define success and stop metrics: migration rate, churn attributable to the sunset, support ticket volume, residual usage at shutdown. Add a rollback or delay trigger if churn exceeds an agreed threshold `[TBD]`.
10. List risks, assumptions and open questions, then fill the template.
11. Suggest next skills: `communication-plan` for detailed messaging, `migration-strategy` for the technical move, `api-deprecation-plan` if an API is part of the scope, or `impact-analysis` for downstream systems.

## Output format
```markdown
# Sunset Plan: <product / feature>
| Field | Value |
|---|---|
| Scope | <what stops> |
| Reason | <reason> |
| Replacement | <product or none> |
| Decision owner | <name or [UNKNOWN]> |
| Target shutdown | <date or [TBD]> |

## Decision Criteria
| Criterion | Evidence | Assessment |
|---|---|---|

## Affected Segments and Migration Paths
| Segment | Impact (H/M/L) | Migration path | Gaps / incentive | Owner |
|---|---|---|---|---|

## Obligations (contract, SLA, data)
- ...

## Timeline and Gates
| Phase | Target date | Entry gate | Owner |
|---|---|---|---|

## Communication Sequence
| T-minus | Audience | Channel | Message / call to action |
|---|---|---|---|

## Internal Readiness
- Support / Sales / Billing / Docs / In-product: ...

## Metrics and Stop Triggers
- ...

## Risks, Assumptions, Open Questions
- [RISK] ... / [ASSUMPTION] ... / 1. <question> — <owner>
```

## Quality checklist
- [ ] The decision is tested against criteria with evidence, and weak evidence is stated, not hidden.
- [ ] Every affected segment has a migration path or is explicitly flagged as having none.
- [ ] Contractual notice, SLA and data retention/deletion obligations are addressed.
- [ ] Each phase has an entry gate with a measurable condition and an owner.
- [ ] Internal teams are informed before customers.
- [ ] No counts, revenue or dates are invented; unknowns are marked.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Announcing a date before checking contract terms. Inventory notice periods and renewals first; the latest obligation sets the earliest shutdown.
- One message for all customers. Strategic and integrating accounts need direct, earlier contact and assisted migration.
- Treating shutdown as the end. Data deletion, billing cleanup and removal of dead code and docs are part of the plan.
- No stop condition. Define in advance what churn or escalation level delays the shutdown.

## Example
Input: "Retire the legacy reporting module next year; everyone moves to the new analytics dashboard."

Excerpt of output:
- Decision criteria: usage trend `[UNKNOWN – request monthly active accounts for 12 months]`; replacement exists but lacks scheduled e-mail exports `[ASSUMPTION – confirm gap list]`.
- Segment "customers with scheduled exports": Impact H; path: build scheduled export in new dashboard before the freeze gate, else offer CSV API.
- Gate "read-only": at least `[TBD]`% of active accounts have created a dashboard, and no open escalations from contracted accounts.
- Communication: T-180 days internal briefing; T-150 e-mail + in-product banner to all users; T-60 direct outreach to strategic accounts; T-14 final reminder.
