---
description: Writes compliant, benefit-led answers to RFP/RFI/tender requirements, one per requirement, stating the compliance level first, then how the solution meets it, the evidence and the client benefit, in the client's format and within limits. Use when drafting or improving answers to an RFP questionnaire or compliance table, when answers are too generic or feature-led, or when partial compliance must be stated honestly.
related: rfp-analysis, proposal-writing, effort-estimate-for-bid, statement-of-work, traceability-matrix
prompt: Write our answers for requirements R-10 to R-25 in this RFP; our product covers most of them, two need customization.
---

# Write an RFP Response

## Purpose
Give evaluators answers they can score quickly and trust: each requirement answered directly and in the requested format, with an honest compliance level, concrete evidence and the benefit to this client.

## When to use
- Answering an RFP/RFI questionnaire, compliance table or technical response section.
- Existing draft answers are generic, copy-pasted or read like product brochures.
- Some requirements are only partly met and the deviation must be stated without losing the evaluation.

## When not to use
- Deciding whether to bid or understanding the RFP. Use `rfp-analysis`.
- A free-form proposal narrative (understanding, approach, team). Use `proposal-writing`.
- Contractual scope and acceptance terms after award. Use `statement-of-work`.

## Inputs
Required:
- The requirements to answer (text and reference numbers) and facts about the offered solution or service.

Optional, improves quality:
- The RFP analysis: evaluation criteria, weights, client pain points, format and length limits.
- Reusable content (previous answers, product documentation, certifications, case studies).
- Win themes agreed for this bid and competitor weaknesses to contrast implicitly.

If the solution facts for a requirement are missing, do not guess; write the answer skeleton with `[TBD – confirm with <role>]`. Never claim certifications, references, features or figures the user did not confirm.

## Process
1. Build the answer list from the requirements, keeping the client's numbering, order and required format (yes/no fields, character limits, templates).
2. For each requirement, decide the compliance level: Fully compliant (standard), Compliant with configuration, Compliant with customization/development, Partially compliant, Roadmap (with date only if confirmed), Not compliant; never upgrade a level to look better.
3. Open every answer with the compliance statement and a one-sentence direct answer; evaluators often read only the first line.
4. Explain how it is met: the specific mechanism, configuration or process, not general product claims; mirror the client's terminology.
5. Add evidence: reference project, certification, screenshot or document reference, measured result; mark missing evidence `[TBD]`.
6. State the client benefit tied to their stated pain point or goal (from the RFP background); label inferred pain points `[ASSUMPTION]`.
7. For partial or non-compliance, state the gap, the alternative or workaround, its effort and impact, and whether it affects price or timeline.
8. Weave in the 2-3 win themes where relevant, without repeating them in every answer.
9. Check consistency across answers and with the price and plan (e.g. a customization stated here must appear in the estimate); list any inconsistency.
10. Edit for scoring: short paragraphs, active voice, no marketing superlatives, within length limits.
11. Produce the list of items needing confirmation from product, delivery, legal or partners.
12. If the user's goal continues, suggest `effort-estimate-for-bid` to align effort with stated customizations, `proposal-writing` for the narrative part, or `traceability-matrix` to cross-check coverage.

## Output format
```markdown
# RFP Response: <client> – <RFP ref>

## R-<n>: <requirement short title>
**Compliance:** <level>
**Answer:** <one-sentence direct answer>
**How we meet it:** ...
**Evidence:** <reference / certification / document ref or [TBD]>
**Benefit to <client>:** ...
**Deviation (if any):** <gap – alternative – effort/impact>

## Items to Confirm
| Req | What to confirm | Owner (role) |
|---|---|---|

## Consistency Notes
- ...
```

## Quality checklist
- [ ] Every requirement is answered in the client's numbering and format, within limits.
- [ ] Each answer starts with an honest compliance level and a direct answer.
- [ ] Claims are backed by evidence or marked `[TBD]`; no invented references, certifications or figures.
- [ ] Partial and non-compliance state the gap, alternative and impact.
- [ ] Customizations and deviations are consistent with the estimate and plan.
- [ ] Benefits are specific to this client; inferred pain points are labeled.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Answering the question you wish had been asked. Evaluators score against the requirement text; answer it literally first.
- Claiming full compliance for custom work. It surfaces in demos or delivery and damages trust and margin.
- Brochure language ("best-in-class, seamless"). Replace with mechanism and evidence.

## Example
Input: R-17 "The solution must support single sign-on with the bank's identity provider."

Excerpt of output:
- Weak (avoid): "Our platform offers world-class, seamless security and integrates with all identity providers."
- Strong: "**Compliance:** Compliant with configuration. **Answer:** Yes, via SAML 2.0 and OpenID Connect. **How:** The bank's identity provider is configured as the trusted issuer; roles map from group claims. **Evidence:** `[TBD – reference project with same IdP]`. **Benefit:** Staff use existing credentials and access is revoked centrally when employees leave."
