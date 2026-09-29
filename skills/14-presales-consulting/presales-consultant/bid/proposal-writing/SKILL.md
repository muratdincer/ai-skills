---
description: Writes a client-centric proposal covering executive summary, understanding of the client's situation and goals, proposed solution, delivery approach, plan and milestones, team, assumptions, and commercial summary, with win themes and proof points traced to the client's own priorities. Use when responding to a client request or RFP with a narrative proposal, when a solution must be presented for a buying decision, or when a draft proposal reads as a generic capabilities brochure.
related: rfp-analysis, rfp-response, effort-estimate-for-bid, statement-of-work, executive-summary
prompt: Write a proposal for modernizing a logistics company's legacy dispatch system; here are the discovery notes and our estimate.
---

# Write a Proposal

## Purpose
Persuade a client's decision makers that you understand their problem, have a credible solution and plan, and are the lowest-risk partner, in a document that is easy to evaluate and consistent with the estimate and SOW.

## When to use
- A client requests a proposal after discovery, or an RFP asks for a narrative response.
- An internal solution and estimate exist and must be packaged for a buying decision.
- A draft proposal is feature-led or generic and needs to be made client-specific.

## When not to use
- The RFP needs per-requirement compliance answers. Use `rfp-response`.
- You need the contractual scope and acceptance terms. Use `statement-of-work`.
- You are still deciding whether to bid. Use `rfp-analysis`.

## Inputs
Required:
- The client's request, RFP or discovery notes (their situation, goals, constraints).
- The proposed solution outline, or permission to draft one as `[ASSUMPTION]`.

Optional, improves quality:
- Effort estimate, plan and commercial model; pricing (from the commercial team only).
- Evaluation criteria and decision makers; competitors in the deal.
- Reference projects, case studies, certifications, team CVs.
- Mandated structure, page limits and submission format.

If the client context is missing, ask for it. Never invent references, client names, metrics, prices or certifications; use `[TBD: reference]` placeholders.

## Process
1. Extract the client's goals, pain points, success measures, constraints and evaluation criteria in their own words. Note each decision maker's main concern (business, technical, financial, risk).
2. Define 2-4 win themes: each links a client priority to your differentiator and a proof point. A theme without proof is marked `[NEEDS PROOF]`.
3. Write the understanding section first, in the client's terms: current situation, why change now, desired outcome. It should read as if the client wrote it; no mention of your company yet.
4. Describe the solution by outcome: how it achieves each client goal, key components, what changes for users, and the options considered with the reason for the choice. Map features to benefits, not the reverse.
5. Describe the delivery approach: phases, how the client is involved, governance, quality and risk management, change and knowledge transfer. Stay methodology-neutral unless the client mandates one.
6. Present the plan: milestones with deliverables and decision points, critical dependencies on the client, and duration consistent with the effort estimate.
7. Present the team: roles, responsibilities, and relevant experience; use named people only if provided.
8. State assumptions, client responsibilities and exclusions, consistent with the estimate and ready to carry into the SOW.
9. Summarize commercials only as given (model, price, payment milestones, validity); leave figures `[TBD: commercial]` if not provided.
10. Write the executive summary last: one page, client goal, proposed outcome, why you, investment and next step. It must stand alone for a reader who reads nothing else.
11. Check compliance with mandated structure and limits, consistency of numbers across sections, and that each evaluation criterion is visibly answered. Label unsupported claims `[ASSUMPTION]`.
12. If the goal continues, suggest `statement-of-work` to formalize scope, `rfp-response` for compliance matrices, or `presentation-outline` for the orals.

## Output format
```markdown
# Proposal: <client> — <initiative>
## 1. Executive Summary
## 2. Our Understanding
- Situation / Why now / Desired outcomes / Success measures
## 3. Proposed Solution
- Outcome-to-solution mapping | Options considered
## 4. Delivery Approach
## 5. Plan and Milestones
| Milestone | Deliverables | Client dependency | Target |
## 6. Team
| Role | Responsibility | Relevant experience |
## 7. Why Us
| Win theme | Client priority | Proof point |
## 8. Assumptions, Client Responsibilities, Exclusions
## 9. Commercial Summary
## 10. Next Steps
Appendix: evaluation criteria → section map
```

## Quality checklist
- [ ] The understanding section uses the client's goals and words and does not talk about us.
- [ ] Every win theme has a proof point or is marked `[NEEDS PROOF]`.
- [ ] Each evaluation criterion maps to a section.
- [ ] Plan, team, assumptions and figures are consistent with the estimate.
- [ ] No references, metrics, prices or names are invented.
- [ ] The executive summary stands alone on one page.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Opening with company history. Evaluators look for their problem first; lead with understanding and outcome.
- Features without benefits. Tie each capability to a client goal or it reads as a brochure.
- Proposal promises that the SOW and estimate do not cover. Keep one assumption list across all three.

## Example
Input: "Logistics firm, dispatch system is 15 years old, dispatchers re-key orders, they want real-time tracking; our estimate: 3 phases."

Weak opening: "Founded in 2005, we are a leading provider of digital transformation services..."

Strong opening: "Your dispatchers re-enter every order into a system that cannot show where trucks are. The goal is a single real-time view from order to delivery, delivered in three phases so the first depot benefits early `[ASSUMPTION: phasing by depot]`."
