---
description: "Assesses whether a proposed initiative or solution option is feasible across technical, operational, economic, schedule, legal/compliance and organizational dimensions, rates each with evidence, names the conditions and showstoppers, and recommends go, go with conditions or no-go. Use when an idea or request must be vetted before investment, when comparing solution options at a high level, or when asked 'can we actually do this?'."
related: "cost-benefit-analysis, build-vs-buy, pre-mortem, risk-register, technology-selection"
prompt: "Assess the feasibility of replacing our on-prem CRM with a SaaS CRM within 6 months; we have 2 developers and strict KVKK requirements."
---

# Assess Feasibility

## Purpose
Give decision makers an evidence-based view of whether an initiative can succeed under real constraints, with the conditions that must hold and the showstoppers that would kill it, before money and people are committed.

## When to use
- A request or idea passed triage and needs a go/no-go before detailed analysis or funding.
- Two or three solution options must be screened before a full comparison.
- A deadline, budget or team size looks tight and someone must say whether it is realistic.

## When not to use
- You need the financial case with ROI and payback. Use `cost-benefit-analysis`.
- The question is build, buy or reuse for a specific component. Use `build-vs-buy`.
- The option is chosen and you need to identify delivery risks. Use `risk-register` or `pre-mortem`.

## Inputs
Required:
- A description of the initiative or the options to assess.
- The key constraints known so far (deadline, budget envelope, team, regulation), or a statement that they are unknown.

Optional, improves quality:
- Current system landscape, integration points, data volumes.
- Available skills and capacity, vendor information, organizational change history.
- Mandatory policies (security, data residency, procurement).

If the initiative description is missing, ask for it. For unknown constraints, proceed and list them as open questions; do not fill them in.

## Process
1. Restate the initiative and its success criteria in two or three lines; if several options exist, name them O1, O2...
2. Technical: fit with current architecture, integration complexity, data migration, maturity of required technology, NFRs (performance, security, availability), in-house skills.
3. Operational: will users and operations be able to run it? Process changes, support model, training load, peak periods.
4. Economic: order-of-magnitude cost and benefit drivers only; reference given figures, otherwise describe drivers and mark estimates `[ASSUMPTION]`.
5. Schedule: critical path items (procurement, security approval, migration, freeze periods) against the target date; give a realistic range, not a single date.
6. Legal/compliance: KVKK/GDPR (data location, transfer abroad, processor agreements), sector regulation, contracts and licensing.
7. Organizational: sponsorship, stakeholder readiness, competing initiatives, change fatigue.
8. Rate each dimension Feasible / Feasible with conditions / Not feasible / Unknown, with evidence and the condition that would change the rating.
9. List showstoppers (any single one means no-go) and key assumptions to validate first, cheapest check first (spike, vendor demo, legal opinion).
10. Recommend: Go, Go with conditions, No-go or Need more information, and state what would change the recommendation.
11. If the user wants to continue, suggest `cost-benefit-analysis` for the financial case, `build-vs-buy` or `technology-selection` for option choice, or `risk-register` for delivery risks.

## Output format
```markdown
# Feasibility Assessment: <initiative>
Options: <O1, O2 ... or single> · Target: <date / budget / constraints as given>

## Summary and Recommendation
<Go / Go with conditions / No-go / Need more information> – <2-3 lines why>

## Dimension Ratings
| Dimension | Rating | Evidence | Condition / what would change it |
|---|---|---|---|
| Technical | | | |
| Operational | | | |
| Economic | | | |
| Schedule | | | |
| Legal / compliance | | | |
| Organizational | | | |

## Showstoppers
- ...

## Assumptions to Validate First
| Assumption | Validation method | Owner | Needed by |
|---|---|---|---|

## Open Questions
1. ...
```

## Quality checklist
- [ ] Every dimension has a rating and evidence; missing evidence yields Unknown, not a guess.
- [ ] No cost, benefit or date is invented; estimates are ranges marked `[ASSUMPTION]`.
- [ ] Showstoppers are separated from ordinary risks.
- [ ] The recommendation follows from the ratings and names what would change it.
- [ ] Legal and data-protection aspects are assessed where personal data is involved.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Declaring "technically feasible" and stopping. Most initiatives fail on schedule, operations or organization, not technology.
- Giving a single-point date. Present a range with the critical-path drivers.
- Letting the sponsor's enthusiasm fill in unknowns. Unknown stays Unknown until validated.

## Example
Input: "Replace on-prem CRM with a SaaS CRM in 6 months; 2 developers; strict KVKK requirements."

Excerpt of output:
| Dimension | Rating | Evidence | Condition |
|---|---|---|---|
| Legal / compliance | Unknown | Data location of SaaS vendor not given | Feasible if data is hosted in an approved location or a valid transfer mechanism exists |
| Schedule | Feasible with conditions | 2 developers vs. migration + 5 integrations `[ASSUMPTION]` | Holds only if the vendor or a partner takes integrations |

Recommendation: Need more information – confirm data residency and integration count before committing.
