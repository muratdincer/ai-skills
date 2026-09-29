---
name: effort-estimate-for-bid
description: "Builds an effort estimate for a bid or proposal by combining a bottom-up estimate from a work breakdown with a top-down or analogy check, making every assumption and exclusion explicit, adding risk-based contingency, and turning effort into a role-based staffing profile. Use when a presales team must price a fixed-price or time-and-materials bid, when an RFP asks for effort or team size, or when an existing bid estimate needs a sanity check."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 14-presales-consulting
  role: presales-consultant
  area: bid
  title: "Estimate effort for a bid"
  related: "rfp-analysis, proposal-writing, statement-of-work, estimation-three-point, wbs"
  prompt: "Estimate the effort for our bid to build a B2B customer portal with SSO, order tracking and ERP integration; they want a fixed price."
---

# Estimate Effort for a Bid

## Purpose
Produce a defensible, assumption-backed effort figure and staffing profile for a bid, so the commercial team can price it and the delivery team can later deliver within it.

## When to use
- An RFP, tender or client request needs an effort, team size or price basis.
- A fixed-price bid must be scoped and protected with assumptions and contingency.
- A sales-driven number needs an independent bottom-up check before submission.

## When not to use
- The project is won and needs a delivery estimate per work item. Use `estimation-three-point` or `technical-estimation`.
- You still need to decide whether to bid. Use `rfp-analysis`.
- You need to price cloud run costs, not effort. Use `cloud-cost-estimate`.

## Inputs
Required:
- Scope description: RFP, requirement list or the client's request.
- Commercial model: fixed price, time and materials, capped, or unknown.

Optional, improves quality:
- Historical actuals from similar projects; team productivity norms.
- Delivery model (onsite/offshore mix), roles and rate cards (rates stay with the commercial team unless given).
- Client constraints: deadline, mandated technologies, client-side responsibilities.

If scope is missing, ask for it. Never invent historical data, rates or client commitments; mark them `[UNKNOWN]`.

## Process
1. Extract scope items from the input into a bid-level WBS (phases, workstreams, features, integrations, data migration, non-functional work). Tag each with its source reference; items you added are `[ASSUMPTION]`.
2. Classify each item's certainty: known (clear spec), understood (typical, some unknowns), uncertain (vague, novel, dependent on client). Uncertain items get ranges and explicit assumptions, not single numbers.
3. Estimate bottom-up per item with three points (optimistic, most likely, pessimistic) in person-days; compute expected effort (O + 4M + P) / 6 and keep the spread visible.
4. Add the effort that bids typically forget: project management, architecture, environments and DevOps, testing and defect fixing, UAT support, data migration, documentation, training, hypercare, security and performance testing, governance meetings. State the percentage or basis used.
5. Cross-check top-down: compare total and phase distribution against an analogous project or a stated ratio (e.g. test share of build). If the gap exceeds about 20%, investigate and explain; do not average blindly.
6. Write the assumption register: each assumption that the number depends on, phrased so it can be copied into the SOW (client provides X by date Y; max N integrations; Z environments), plus explicit exclusions.
7. Build a risk list and derive contingency from it (per-risk exposure or the three-point spread), rather than a flat percentage. Distinguish contingency (known risks, inside the price) from management reserve (unknown unknowns, a commercial decision).
8. Convert effort into a staffing profile by role and phase, checking that the resulting duration fits the client's deadline; flag compression risks when it does not.
9. Present the estimate as a range with a recommended figure and its confidence, per commercial model: fixed price needs tighter assumptions and higher contingency; time and materials needs a clear rate basis and cap logic.
10. List open questions to the client that would narrow the range most, ordered by effort impact.
11. If the goal continues, suggest `proposal-writing` to present the approach, `statement-of-work` to lock assumptions into the contract, or `rfp-response` for per-requirement answers.

## Output format
```markdown
# Bid Effort Estimate: <client / opportunity>
| Field | Value |
|---|---|
| Commercial model | ... |
| Recommended effort | <person-days> (range <low>–<high>, confidence <H/M/L>) |
| Duration / team peak | ... |

## Estimate by Work Item
| ID | Item | Source | Certainty | O | M | P | Expected | Assumptions |

## Supporting Effort
| Area | Basis | Person-days |

## Top-down Cross-check
- Analogy / ratio: ...  - Gap and explanation: ...

## Contingency
| Risk | Probability | Impact (PD) | Exposure |
- Contingency: ...  - Management reserve (commercial decision): ...

## Staffing Profile
| Role | Phase 1 | Phase 2 | ... | Total PD |

## Assumptions and Exclusions (SOW-ready)
- A1: ...
- Excluded: ...

## Questions That Narrow the Range
1. <question> — <effort impact>
```

## Quality checklist
- [ ] Every scope item traces to the input or is labeled `[ASSUMPTION]`.
- [ ] Supporting effort (PM, testing, environments, migration, hypercare) is included with its basis.
- [ ] Bottom-up and top-down figures are reconciled, with gaps explained.
- [ ] Contingency is derived from named risks, and management reserve is separated.
- [ ] Assumptions are written so they can be copied into a SOW.
- [ ] No rates, historical figures or client commitments are invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Estimating only build effort. Non-development work often makes up a large share of the total; list it explicitly.
- Reverse-engineering the estimate to a target price. Keep the honest number and let the commercial team decide on discount or risk acceptance.
- Assumptions buried in the estimate spreadsheet. If they are not in the SOW, they do not protect the bid.

## Example
Input: "B2B portal: SSO, order tracking, ERP integration. Fixed price. No details on ERP."

Excerpt of output:
| ID | Item | Certainty | O | M | P | Expected | Assumptions |
|---|---|---|---|---|---|---|---|
| 3 | ERP order sync | uncertain | 25 | 45 | 90 | 49.2 | A4: ERP exposes documented APIs; max 3 entities; client provides test ERP by week 4 |

- Question that narrows the range: "Which ERP and version, and does it already expose order APIs?" — impact up to ±45 PD.
