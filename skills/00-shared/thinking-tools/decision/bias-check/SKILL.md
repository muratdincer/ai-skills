---
name: bias-check
description: "Reviews an analysis, recommendation or decision for cognitive biases such as confirmation, anchoring, survivorship, sunk cost, availability, overconfidence and groupthink, cites the evidence for each suspected bias and proposes a concrete debiasing action. Use when a decision is about to be made or an analysis is about to be shared, when someone asks \"am I missing something?\", \"is this biased?\", \"challenge my reasoning\" or wants a red-team view of a conclusion."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: thinking-tools
  area: decision
  title: "Check for cognitive bias"
  related: "pre-mortem, assumption-mapping, decision-matrix, trade-off-analysis, decision-log"
  prompt: "Check this recommendation for bias before I send it to the steering committee: we should keep investing in the in-house scheduler because we already spent 18 months on it and the two pilot teams love it."
---

# Check for Cognitive Bias

## Purpose
Find the places where an analysis or decision rests on distorted reasoning rather than evidence, and turn each finding into a specific corrective action. The goal is a better decision, not a verdict on the author.

## When to use
- A recommendation, business case, estimate or architecture choice is about to be approved or shared.
- A conclusion feels unanimous, fast or emotionally loaded, and nobody has argued the other side.
- A post-hoc review needs to separate bad luck from bad reasoning.
- The user explicitly asks to challenge or red-team their thinking.

## When not to use
- The goal is to imagine how a plan fails in the future. Use `pre-mortem`.
- The goal is to list and test the assumptions behind a plan. Use `assumption-mapping`.
- Options still need to be scored against criteria. Use `decision-matrix`.

## Inputs
Required:
- The analysis, recommendation or decision text, including the reasoning and evidence used.

Optional, improves quality:
- Options that were considered and rejected, and why.
- Who made the decision, their stake, and how the group reached it.
- Data sources, sample sizes, time frame, prior commitments or spend.

If the reasoning text is missing, ask for it. Do not ask for optional inputs up front; list their absence as open questions.

## Process
1. Restate the conclusion in one sentence and list the claims it depends on, each tagged as stated evidence, stated opinion or your inference.
2. Map where the evidence came from: who collected it, sample size, selection method, time window, and what evidence would have been needed but is absent.
3. Screen against the bias set: confirmation, anchoring, availability, survivorship, sunk cost, overconfidence/planning fallacy, framing, authority/HiPPO, groupthink/bandwagon, status quo, base-rate neglect, recency, optimism, IKEA/not-invented-here, outcome bias.
4. For each suspected bias, quote or cite the exact sentence or data point that triggers it. No quote, no finding.
5. Rate each finding: Impact on the decision (High/Medium/Low) and Confidence that the bias is present (High/Medium/Low). Keep "possible" biases separate from "evident" ones.
6. Write the strongest opposing case (steelman) in 3-5 sentences, using only facts in the input or clearly marked assumptions.
7. For each High-impact finding, propose a concrete debiasing action: a disconfirming test, a base-rate or reference-class check, an independent estimate, a zero-based ("if we started today") question, a blind review, or a named devil's advocate.
8. Identify what evidence would change the conclusion (kill criteria) and whether it can be obtained before the decision date.
9. State an overall judgment: reasoning is sound / sound with caveats / needs rework before deciding, with a one-line justification.
10. Fill the template. If the user wants to go further, suggest `pre-mortem` for failure modes, `assumption-mapping` to test the riskiest assumptions, or `decision-log` to record the final decision with its caveats.

## Output format
```markdown
# Bias Check: <decision or analysis title>
**Conclusion under review:** <one sentence>
**Overall judgment:** <Sound / Sound with caveats / Needs rework> – <why>

## Claims and Evidence
| # | Claim | Type (evidence / opinion / inference) | Source | Gap |
|---|---|---|---|---|

## Findings
| # | Bias | Trigger (quote or data point) | Impact | Confidence | Debiasing action |
|---|---|---|---|---|---|

## Steelman of the Opposing View
<3-5 sentences>

## What Would Change the Conclusion
- <evidence> – <obtainable before decision? yes/no>

## Assumptions and Open Questions
- [ASSUMPTION] ...
- <question> – <who can answer>
```

## Quality checklist
- [ ] Every finding cites a specific sentence, number or process fact from the input.
- [ ] Evident biases are separated from merely possible ones, with confidence stated.
- [ ] Each High-impact finding has an actionable debiasing step, not just a label.
- [ ] The steelman argues the other side fairly and invents no facts.
- [ ] The tone critiques reasoning, not people; no motive is attributed without evidence.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Bias bingo: listing ten bias names without evidence. Keep only findings you can anchor to the text.
- Treating a bad outcome as proof of bad reasoning (outcome bias in the reviewer). Judge the reasoning with the information available at the time.
- Dismissing a correct conclusion because a bias is present. A biased path can still reach the right answer; say whether the conclusion survives after correction.

## Example
Input: "Keep investing in the in-house scheduler: we spent 18 months on it and the two pilot teams love it."

Excerpt of output:
| # | Bias | Trigger | Impact | Confidence | Debiasing action |
|---|---|---|---|---|---|
| 1 | Sunk cost | "we already spent 18 months" | High | High | Ask: if we started today, would we build it or buy it? Compare remaining cost only. |
| 2 | Survivorship / small sample | "two pilot teams love it" | High | Medium | Ask teams that declined or dropped the pilot; define adoption and satisfaction metrics. |
| 3 | IKEA effect | Built and evaluated by the same team | Medium | Medium `[inference]` | Independent review by a team that did not build it. |

Weak finding: "There may be confirmation bias." Strong finding: "Only positive pilot feedback is cited; no data from the 6 teams that did not join `[ASSUMPTION: count to confirm]`."
