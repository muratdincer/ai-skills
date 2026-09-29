---
description: Evaluates vendors or products for a technology purchase, from requirements and knock-out criteria through a weighted scoring model fixed before responses are read, evidence-based scoring, total cost of ownership and risk, to a documented recommendation. Use when selecting a software product, platform, cloud or service provider, preparing or scoring an RFP, or when a vendor choice must be defensible to procurement, audit or leadership.
related: decision-matrix, build-vs-buy, fit-gap-analysis, vendor-status-review, it-risk-assessment
prompt: We have 3 responses to our RFP for an API management platform; build the evaluation model and recommend a vendor.
---

# Evaluate Vendors (RFP)

## Purpose
Reach a vendor decision that is traceable and fair: the criteria and weights are agreed before anyone scores, every score rests on evidence, and total cost and risk are compared alongside functionality.

## When to use
- Selecting a product, platform, managed service or implementation partner.
- Designing the evaluation part of an RFP or scoring received responses.
- A preferred vendor must be justified to procurement, audit, security or the board.

## When not to use
- Deciding whether to buy at all versus build. Use `build-vs-buy` first.
- Checking one package's fit against detailed requirements. Use `fit-gap-analysis`.
- Reviewing an existing vendor's delivery performance. Use `vendor-status-review`.

## Inputs
Required:
- The need or requirements, and the candidate vendors or their responses (if scoring has started).

Optional, improves quality:
- Budget range, contract term, procurement rules and mandatory clauses.
- Architecture, security, data residency and compliance constraints (KVKK/GDPR, sector rules).
- Demo, proof-of-concept or reference-call notes.

If requirements are missing, ask for them; without them any scoring is opinion. Do not invent vendor capabilities, prices or references; use only what the responses or the user provide.

## Process
1. Define the decision: what is being bought, horizon, decision owner and who scores; declare conflicts of interest among evaluators.
2. Set knock-out criteria (mandatory, pass/fail): e.g. data residency, security certification, integration with a named system, support hours; a vendor failing any is excluded with the reason recorded.
3. Build weighted criteria in groups: functional fit, non-functional (performance, availability, security), integration and architecture fit, vendor viability and support, delivery approach, commercial/TCO; agree weights before reading responses.
4. Define a scoring scale with anchors (e.g. 0 = not met, 3 = met with workaround, 5 = met natively with evidence) so evaluators score the same way.
5. Score each vendor per criterion with a one-line evidence reference (response section, demo observation, PoC result); mark claims without evidence as unverified and score them lower or verify.
6. Have evaluators score independently first, then reconcile large differences through evidence, not seniority.
7. Compute total cost of ownership over the contract horizon: licenses/subscription, implementation, integration, infrastructure, internal staff, training, exit/migration cost; mark estimates `[ASSUMPTION]`.
8. Assess risks: lock-in and exit options, vendor financial and roadmap risk, security and privacy, key-person dependency, contractual gaps.
9. Run a sensitivity check: would the ranking change with reasonable weight shifts? State how robust the winner is.
10. Write the recommendation with conditions (contract clauses, PoC gates, negotiation points) and the runner-up as fallback.
11. If the user's goal continues, suggest `decision-log` to record the decision, `it-risk-assessment` for a deeper risk review, or `vendor-status-review` once the vendor is onboarded.

## Output format
```markdown
# Vendor Evaluation: <purchase>
Decision owner: <role> · Evaluators: <roles> · Conflicts declared: <none/...>

## Knock-out Criteria
| Criterion | Vendor A | Vendor B | Vendor C |
|---|---|---|---|

## Weighted Scoring (scale 0-5, anchors in appendix)
| Group / criterion | Weight | A | B | C | Evidence refs |
|---|---|---|---|---|---|
| Weighted total | 100% | | | | |

## Total Cost of Ownership (<n> years)
| Cost element | A | B | C | Basis |
|---|---|---|---|---|

## Risks
| Risk | Vendor | Likelihood | Impact | Mitigation |
|---|---|---|---|---|

## Sensitivity
- ...

## Recommendation
- Preferred: <vendor> – why – conditions
- Fallback: <vendor>
- Open questions: ...
```

## Quality checklist
- [ ] Knock-out criteria, weights and scale anchors were fixed before responses were scored.
- [ ] Every score cites evidence; unverified vendor claims are marked.
- [ ] TCO covers the whole horizon, including internal effort and exit cost.
- [ ] Lock-in, security and vendor viability risks are assessed.
- [ ] No invented capabilities, prices or references; assumptions are labeled.
- [ ] The recommendation states conditions and a fallback.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Setting weights after seeing responses. This bends the model toward a favorite; freeze weights first.
- Comparing license price only. Implementation, integration and internal staff often dominate TCO.
- Scoring the best demo. A polished demo is not evidence of fit on your data and integrations; use a PoC for critical criteria.

## Example
Input: Three RFP responses for an API management platform.

Excerpt of output:
- Knock-out: on-premises or in-country data plane required `[confirm]`; Vendor C offers only a foreign-region SaaS – excluded.
- Weak evidence (avoid): "Vendor A has good security." Strong: "Vendor A: mTLS and OAuth 2.0 policies shown in demo; independent security certification copy not provided – unverified, score 3 until received."
- TCO: Vendor B license is lower but requires 2 FTE `[ASSUMPTION]` for self-hosting; 3-year TCO ranks it second.
