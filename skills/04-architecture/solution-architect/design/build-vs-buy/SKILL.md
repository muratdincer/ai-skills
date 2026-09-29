---
description: Compares building, buying (COTS/SaaS), extending an existing platform or using open source for a capability, across strategic differentiation, functional fit, multi-year total cost of ownership, risk, time to value and exit cost, and produces a reasoned recommendation. Use when a team must decide whether to develop a capability in-house or acquire it, or when an existing custom system or product is up for replacement.
related: technology-selection, vendor-evaluation, cost-benefit-analysis, fit-gap-analysis, adr
prompt: Should we build our own customer notification service or buy a SaaS product? We send about 2 million emails and SMS a month and need templates in Turkish and English.
---

# Decide Build vs Buy

## Purpose
Reach a defensible sourcing decision for a capability by comparing options on strategic value, fit, total cost, risk and reversibility, instead of on licence price or developer enthusiasm.

## When to use
- A new capability is needed and both custom development and market products are plausible.
- A custom system is expensive to maintain and a product might replace it, or vice versa.
- Leadership asks for a sourcing recommendation with cost and risk.

## When not to use
- The decision is between comparable products or frameworks only. Use `technology-selection` or `vendor-evaluation`.
- Requirements are not yet known. Use `fit-gap-analysis` or `brd-writing` first.
- A pure financial appraisal of an approved investment is needed. Use `cost-benefit-analysis`.

## Inputs
Required:
- The capability and its key requirements, including must-haves.
- The options under consideration, or permission to propose them.

Optional:
- Volumes, users, growth; horizon for TCO (commonly 3-5 years).
- Team capacity and skills, internal rate/cost figures, vendor quotes.
- Constraints: data residency, KVKK/GDPR, security, integration landscape, procurement rules.

If the capability or must-haves are missing, ask. Never invent prices; use `[UNKNOWN]` or ranges supplied by the user.

## Process
1. Classify the capability as differentiating, necessary-but-common or commodity (e.g., via capability map or Wardley evolution). Default: build what differentiates, buy commodity.
2. Define options: build, buy SaaS, buy and self-host COTS, adopt open source, extend an existing platform, hybrid (buy core, build edges).
3. Define weighted criteria: strategic value, functional fit (must-haves are gates, not scores), non-functional fit, integration effort, time to value, TCO, vendor/ecosystem risk, lock-in and exit cost, team capability.
4. Assess fit per option: must-have gate pass/fail, then gaps and the customization needed to close them; label unverified vendor claims `[ASSUMPTION]`.
5. Build a TCO model over the horizon with categories: licence/subscription, implementation, integration, customization, infrastructure/run, support and operations staff, upgrades, training, exit/migration. Use supplied figures or placeholders only.
6. Assess risks: vendor viability, roadmap control, upgrade treadmill for customized products, security/compliance posture, key-person risk for build, delivery risk.
7. Evaluate reversibility: data export, standard interfaces, contract terms, cost to switch later.
8. Score and compare; run a sensitivity check on the two or three criteria with the highest weight or uncertainty.
9. Write the recommendation with conditions (e.g., "buy, provided data residency is contractually guaranteed") and the evidence still needed (PoC, reference calls, quotes).
10. If the goal continues, suggest `vendor-evaluation` for the product shortlist, `technology-selection` for the build stack or `adr` to record the decision.

## Output format
```markdown
# Build vs Buy: <capability>
## Capability Classification
<differentiating | common | commodity> – <reason>
## Options
## Must-Have Gates
| Must-have | Build | Buy A | OSS | Extend |
|---|---|---|---|---|
## Weighted Evaluation
| Criterion | Weight | Build | Buy A | OSS | Extend |
|---|---|---|---|---|---|
## TCO (<horizon>)
| Cost category | Build | Buy A | ... |
|---|---|---|---|
## Risks and Exit Considerations
## Sensitivity
## Recommendation and Conditions
## Evidence Still Needed / Open Questions
```

## Quality checklist
- [ ] Must-haves act as gates; an option failing one is not rescued by other scores.
- [ ] TCO covers the whole horizon and includes run, upgrade and exit costs, not only licence or build effort.
- [ ] No price or effort figure is invented; unknowns are marked.
- [ ] Customization of a bought product is costed, including upgrade impact.
- [ ] The recommendation states its conditions and the evidence still needed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Comparing year-one licence cost with build effort and ignoring the maintenance team a build requires for years.
- Buying and then customizing heavily, which creates a fork that cannot be upgraded. Prefer configuration or building at the edges.
- Building commodity capabilities because the team finds them interesting.

## Example
Input: "Build or buy a notification service; ~2M email/SMS per month, TR and EN templates."

Excerpt of output:
- Classification: commodity – notification delivery does not differentiate the business `[ASSUMPTION: confirm with product]`.
- Gate: SMS delivery through local operators in Turkey – Buy A `[UNKNOWN, ask vendor]`, Build pass (via existing SMS gateway).
- TCO note: Build includes an on-call rota and deliverability management; Buy A pricing per message `[UNKNOWN – request quote at 2M/month]`.
- Recommendation: Hybrid – buy email delivery, keep in-house template and preference service; conditional on data residency terms.
