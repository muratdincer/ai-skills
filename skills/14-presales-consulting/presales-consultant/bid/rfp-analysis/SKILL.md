---
name: rfp-analysis
description: "Analyzes a client RFP/RFQ/tender document from the bidder's side, extracting mandatory and scored requirements, evaluation criteria, commercial and legal terms, deadlines, hidden expectations and risks, and produces a compliance matrix and a reasoned bid/no-bid recommendation. Use when a new RFP or tender arrives, before committing presales effort, or when the team must decide whether and how to bid."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 14-presales-consulting
  role: presales-consultant
  area: bid
  title: "Analyze an RFP"
  related: "rfp-response, effort-estimate-for-bid, proposal-writing, requirements-gap-analysis, risk-register"
  prompt: "Analyze this 80-page RFP for a core banking integration project and tell me whether we should bid."
---

# Analyze an RFP

## Purpose
Understand exactly what the client asks, how they will judge responses and what could hurt the bidder, so the team can make an informed bid/no-bid decision and plan a compliant, competitive response.

## When to use
- A new RFP, RFQ, RFI or tender document arrives.
- The team must decide whether to invest presales effort in a bid.
- Before writing the response, to build the compliance matrix and question list.

## When not to use
- Writing the actual answers. Use `rfp-response`.
- Evaluating vendor responses as the buyer. Use `vendor-evaluation`.
- Estimating the effort of the solution. Use `effort-estimate-for-bid`.

## Inputs
Required:
- The RFP document or its relevant sections (requirements, evaluation criteria, terms, timeline).

Optional, improves quality:
- Relationship history with the client, known competitors, incumbent vendor.
- Own capabilities, references, partner options and capacity for the delivery period.
- Company bid policy (minimum margin, risk appetite, excluded contract terms).

If the RFP text is missing, ask for it. Do not invent requirements, weights or dates that the document does not state; mark gaps `[UNKNOWN]` and turn them into clarification questions.

## Process
1. Extract the administrative frame: issuer, submission deadline and format, question deadline, validity period, mandatory forms, bonds or guarantees, language and page limits.
2. Extract every requirement with its reference number and classify it: mandatory (pass/fail), scored, informational; note format demands (e.g. "answer yes/no plus explanation").
3. Capture the evaluation model: criteria, weights, technical/commercial split, minimum technical threshold, price formula; if not disclosed, mark `[UNKNOWN]`.
4. Read between the lines: repeated themes, unusually specific requirements (may favor an incumbent), pain points in the background section; label these interpretations `[ASSUMPTION]`.
5. Review commercial and legal terms: payment milestones, penalties and liquidated damages, liability caps, IP ownership, acceptance, warranty, data protection (KVKK/GDPR), subcontracting limits; flag unacceptable or high-risk clauses.
6. Build the compliance matrix: requirement → comply / partial / not comply / needs clarification, with the planned evidence or approach.
7. List clarification questions for the client, ordered by impact on solution, price or eligibility, respecting the question deadline.
8. Assess win factors: fit to requirements, relationship and client knowledge, references, price competitiveness, incumbent advantage, team availability.
9. Assess risks: scope ambiguity, fixed price on unclear scope, aggressive timeline, penalties, dependency on client or third parties, capacity to deliver.
10. Recommend bid / no-bid / bid with conditions, scored transparently on win probability and risk-adjusted attractiveness, and name the decision owner.
11. If the user's goal continues, suggest `effort-estimate-for-bid` for sizing, `rfp-response` to write the answers, or `proposal-writing` if a free-form proposal is requested.

## Output format
```markdown
# RFP Analysis: <client> – <RFP title/ref>

## Key Facts
| Item | Value |
|---|---|
| Submission deadline / format | ... |
| Question deadline | ... |
| Evaluation model | <weights, threshold, price formula or [UNKNOWN]> |
| Contract type / term | ... |

## Requirements Summary
| Ref | Requirement (short) | Type | Compliance | Evidence / approach | Note |
|---|---|---|---|---|---|

## Commercial and Legal Flags
| Clause | Risk | Proposed position |
|---|---|---|

## Hidden Expectations (interpretation)
- [ASSUMPTION] ...

## Clarification Questions
1. <question> – RFP ref – why it matters

## Win Factors and Risks
| Factor | Assessment | Evidence |
|---|---|---|

## Recommendation
Bid / No-bid / Bid with conditions – reasons – conditions – decision owner
```

## Quality checklist
- [ ] Every mandatory requirement is listed with its reference and compliance status.
- [ ] The evaluation model and deadlines are taken from the document, or marked `[UNKNOWN]`.
- [ ] High-risk commercial and legal clauses are flagged with a proposed position.
- [ ] Interpretations of hidden expectations are labeled `[ASSUMPTION]`.
- [ ] Clarification questions reference RFP sections and are ordered by impact.
- [ ] The bid/no-bid recommendation states reasons, conditions and the decision owner.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Bidding on everything. A low-probability bid consumes the same presales effort as a winnable one; decide with evidence.
- Missing a single pass/fail requirement (a form, a certificate, a bond). It disqualifies the whole response regardless of quality.
- Accepting unlimited liability or penalties on unclear scope. Raise it as a clarification or a stated deviation.

## Example
Input: 80-page RFP, core banking integration, fixed price, 6-month timeline.

Excerpt of output:
- Mandatory: R-14 "Vendor must have delivered 2 integrations with <named core banking product> in the last 3 years" – our references: `[UNKNOWN – confirm]`; if none, this is a knock-out.
- Legal flag: penalty of 1% per day of delay without cap – propose a 10% cap and client-dependency exclusions.
- Recommendation: Bid with conditions – only if R-14 references are confirmed and the question on test environment availability is answered.
