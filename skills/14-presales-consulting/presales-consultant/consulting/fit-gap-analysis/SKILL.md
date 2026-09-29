---
name: fit-gap-analysis
description: "Runs a fit-gap analysis that compares requirements against the standard capabilities of a package, platform or reference process, classifies each as fit, fit with configuration, gap or not applicable, proposes a resolution per gap (process change, configuration, extension, integration, third-party, workaround, defer) with effort band and risk, and summarizes the fit ratio and decisions needed. Use when evaluating or implementing an ERP, CRM, SaaS or other packaged solution, when a client asks how much customization a package will need, or when requirements must be aligned to a standard process."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 14-presales-consulting
  role: presales-consultant
  area: consulting
  title: "Run a fit-gap analysis"
  related: "requirements-gap-analysis, build-vs-buy, vendor-evaluation, current-state-assessment, effort-estimate-for-bid"
  prompt: "Do a fit-gap of these 40 order-to-cash requirements against a standard cloud ERP sales module and tell us where customization is unavoidable."
---

# Run a Fit-Gap Analysis

## Purpose
Show, requirement by requirement, what a package does out of the box, what needs configuration and what does not fit, with a justified resolution for each gap, so the client can decide how much to adapt its process versus the product and what that costs in effort and risk.

## When to use
- A packaged solution (ERP, CRM, HCM, SaaS platform) is being selected, bid or implemented.
- A client asks how much customization, extension or integration a package will require.
- Requirements must be aligned to a standard or reference process before design.

## When not to use
- Checking a requirement set for its own missing content, not against a product. Use `requirements-gap-analysis`.
- Comparing several vendors with weighted scoring. Use `vendor-evaluation`.
- Deciding whether to build or buy at all. Use `build-vs-buy`.

## Inputs
Required:
- Requirements list (IDs, descriptions, priority if known) or business processes in scope.
- The package, platform or reference process to compare against, and its edition/scope if relevant.

Optional, improves quality:
- Product documentation, demo notes or vendor answers as capability evidence.
- Client priority (must/should/could) and regulatory or localization needs.
- Customization policy (e.g. "clean core", no code changes to standard objects).

If requirements or the target package are missing, ask. Never assert a product capability without evidence; mark it `[VERIFY WITH VENDOR]`.

## Process
1. Normalize requirements: one capability per line, stable IDs, priority, and process area. Split compound requirements; flag vague ones `[AMBIGUOUS]` instead of rating them.
2. Separate the literal requirement from the underlying business need; many apparent gaps disappear when the need, not the legacy way of working, is compared.
3. For each requirement, determine coverage with evidence source: Fit (standard), Fit with configuration (settings, workflows, fields without code), Gap, or Not applicable. Record evidence type (documentation, demo, vendor statement, assumption).
4. For each gap, identify the resolution options in order of preference: adopt standard process (process change), configuration, extension using supported mechanisms, integration with another system, third-party add-on, manual workaround, or defer. Prefer options that keep upgrades safe.
5. Rate each gap's effort band (S/M/L), upgrade and support risk, and business criticality; combine into a recommended resolution with rationale.
6. Mark decisions that belong to the client: process change acceptance, deviation from customization policy, deferral of must-have items. Name the decision owner type.
7. Check non-functional and cross-cutting areas often skipped: roles and authorizations, reporting, localization and legal requirements (e.g. e-invoicing, tax), data migration, integrations, audit trail, performance, KVKK/GDPR.
8. Summarize: counts and percentages by category overall and by process area, must-have gaps, total effort band of gaps, and top risks.
9. List open items needing vendor confirmation or client clarification, with owner.
10. Label every inference and every capability claim not backed by evidence.
11. If the goal continues, suggest `effort-estimate-for-bid` to cost gap resolutions, `vendor-evaluation` if several packages are compared, or `statement-of-work` to fix the agreed scope.

## Output format
```markdown
# Fit-Gap Analysis: <package / scope>
## Summary
| Process area | Fit | Fit w/ config | Gap | N/A | Must-have gaps |
- Overall fit ratio: ...  - Gap effort band: ...  - Top risks: ...

## Detailed Assessment
| Req ID | Requirement (need) | Priority | Classification | Evidence | Resolution | Effort | Upgrade risk | Decision owner |

## Gaps Requiring Client Decision
| Req ID | Options | Recommendation | Trade-off |

## Cross-cutting Checks
- Authorizations / reporting / localization / migration / integrations / audit / privacy

## Open Items
| Item | Needed from (vendor / client) | Owner |

## Assumptions
- ...
```

## Quality checklist
- [ ] Every requirement has one classification and an evidence type; vague ones are `[AMBIGUOUS]`, not rated.
- [ ] No capability claim lacks evidence; unverified ones are `[VERIFY WITH VENDOR]`.
- [ ] Each gap has resolution options, a recommendation, effort band and upgrade risk.
- [ ] Process-change options were considered before extensions.
- [ ] Client decisions are listed separately with an owner type.
- [ ] Cross-cutting areas (authorizations, localization, migration, reporting) are covered.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Comparing against the legacy system's behavior instead of the business need. It inflates gaps and customization.
- Trusting the sales demo as evidence. Record the evidence type and verify critical fits in documentation or a proof of concept.
- Reporting only the fit percentage. A high ratio can hide a few must-have gaps that dominate cost and risk.

## Example
Input: "Req OTC-17: Credit limit check must block orders over limit and notify the regional finance manager by SMS."

Excerpt of output:
| Req ID | Requirement (need) | Classification | Evidence | Resolution | Effort | Upgrade risk |
|---|---|---|---|---|---|---|
| OTC-17a | Block orders over credit limit | Fit w/ config | Product docs `[VERIFY WITH VENDOR: edition]` | Configure credit management | S | Low |
| OTC-17b | Notify finance manager by SMS | Gap | No native SMS `[ASSUMPTION]` | Use standard email/workflow notification (process change) or integrate SMS gateway | S / M | Low / Medium |

- Client decision: accept email notification instead of SMS? Owner: finance process owner.
