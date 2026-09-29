---
description: Writes a working-backwards press release dated at a future launch, plus a customer FAQ and an internal FAQ, to test whether a product idea is compelling, clear and feasible before anything is built; ends with the open questions and risks the document exposed. Use when a new product or major feature is proposed, when a team needs to align on the customer outcome before design, or when someone asks for a "PR/FAQ", "working backwards" document or "future press release".
related: product-vision, prd-writing, value-proposition-canvas, positioning-statement, pre-mortem
prompt: Write a working-backwards PR/FAQ for a feature that lets our B2B customers get a delivery ETA on WhatsApp without logging into the portal.
---

# Write a Working-Backwards Press Release and FAQ

## Purpose
Start from the customer and the launch day, and work backwards: if the press release is not compelling and the FAQ cannot answer the hard questions, the idea is not ready to build. The document is a thinking and decision tool, not marketing copy.

## When to use
- A new product, service or major feature is being proposed for investment.
- Stakeholders disagree on what the product is for, or who it is for.
- Before a PRD or design work, to agree on the customer outcome and the boundaries.

## When not to use
- The product already exists and a real launch announcement is needed. Use `release-announcement`.
- Detailed requirements are needed for the build. Use `prd-writing` after the PR/FAQ is accepted.
- Only the long-term direction is needed. Use `product-vision`.

## Inputs
Required:
- The idea: target customer, the problem, and the proposed solution in a few sentences.

Optional, improves quality:
- Customer evidence, competing alternatives, constraints, business goals, launch horizon, pricing idea.

If the target customer or problem is missing, ask for it one question at a time. Do not invent customer quotes as real: write them as illustrative and label them `[ILLUSTRATIVE]`. Never invent market figures.

## Process
1. Write the headline and subheadline in customer language: who gets what benefit. No internal jargon, no technology names unless the customer cares.
2. Write the dateline with a future launch date given by the user or `[TBD]`, and a first paragraph summarizing the product and the benefit.
3. Problem paragraph: the customer's current pain in concrete terms, as the customer would describe it.
4. Solution paragraph: how the product solves it, focusing on the experience, not the architecture.
5. Add an illustrative leader quote (why we built it) and an illustrative customer quote (the outcome they got), both labeled `[ILLUSTRATIVE]`.
6. Add "how to get started" and availability in one or two sentences; keep the release around one page.
7. Customer FAQ: 6-10 questions a real customer would ask (price, availability, setup, data, limitations, what happens to the old way).
8. Internal FAQ: 6-12 hard questions for decision makers: target segment size and evidence, why now, success metrics, business model, cost and team, dependencies, legal/privacy, top risks and how we would know we are wrong, what we will not do. Answer with evidence or mark `[UNKNOWN]`.
9. Run a self-critique: Is the benefit clear in the headline? Would the target customer care? Which FAQ answers are weak or `[UNKNOWN]`? List these as open questions and risks with owners.
10. Recommend a decision (proceed / refine / stop) with reasons, and suggest the next skill: `prd-writing` to specify, `pre-mortem` to stress-test risks, or `value-proposition-canvas` if the customer value is unclear.

## Output format
```markdown
# <Headline: customer benefit>
## <Subheadline: who, what, why it matters>
**<City>, <future launch date or TBD>** – <summary paragraph>

<Problem paragraph>
<Solution paragraph>
"<Leader quote>" – <role> [ILLUSTRATIVE]
<How it works / experience>
"<Customer quote>" – <customer type> [ILLUSTRATIVE]
<How to get started, availability>

---
## Customer FAQ
**Q:** ... **A:** ...

## Internal FAQ
**Q:** Who exactly is the customer and how many are there? **A:** ... [EVIDENCE / UNKNOWN]
**Q:** How will we measure success? **A:** ...
**Q:** What are we explicitly not doing? **A:** ...

## Open Questions and Risks
| # | Question / risk | Why it matters | Owner |
|---|---|---|---|

## Recommendation
<Proceed / Refine / Stop> – <reasons>
```

## Quality checklist
- [ ] The headline states a customer benefit that a non-expert understands.
- [ ] The press release fits on about one page and contains no internal jargon or architecture.
- [ ] Quotes and dates are labeled illustrative or TBD; no figures are invented.
- [ ] The internal FAQ answers the hard questions honestly, with gaps marked `[UNKNOWN]`.
- [ ] Out-of-scope items and success metrics are explicit.
- [ ] Open questions and risks have owners, and a recommendation is given.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing a feature list as a press release. Lead with the customer outcome; features come later if at all.
- Softball internal FAQ. The value is in the uncomfortable questions; if every answer is positive, the FAQ is not doing its job.
- Treating the draft as a commitment. Iterate the PR/FAQ until the idea is clear or stop the idea.

## Example
Input: "B2B customers get a delivery ETA on WhatsApp without logging into the portal."

Weak headline: "Company launches WhatsApp integration with real-time ETA engine."
Strong headline: "Know when your delivery arrives without logging in: ETAs now come to the chat you already use."
Internal FAQ excerpt:
**Q:** How will we know this worked? **A:** Fewer "where is my delivery" calls to the service desk `[baseline UNKNOWN – owner: service desk lead]`.
**Q:** What are we not doing? **A:** No two-way ordering via chat in the first release.
