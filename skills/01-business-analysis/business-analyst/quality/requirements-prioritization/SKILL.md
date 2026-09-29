---
description: "Prioritizes a set of requirements using a fitting technique (MoSCoW, Kano, value/effort, weighted scoring or cost of delay), makes the criteria explicit, and justifies each ranking with evidence and stated assumptions. Use when scope must be cut to fit a date or budget, stakeholders disagree on what comes first, or a release or MVP scope needs a defensible order."
related: "backlog-prioritization, decision-matrix, mvp-scoping, stakeholder-map, requirements-sign-off"
prompt: "Prioritize these 25 requirements for the first release with MoSCoW; we have a fixed go-live date."
---

# Prioritize Requirements

## Purpose
Produce a transparent, defensible priority order for requirements so scope decisions are made on explicit criteria rather than on who shouts loudest. The output shows the method, criteria, ranking and the reasons behind each placement.

## When to use
- Scope exceeds capacity for a fixed date, budget or release.
- Stakeholders disagree on priority and need a shared basis.
- Defining the first release or MVP scope of a requirement set.

## When not to use
- Ordering an ongoing product backlog of work items. Use `backlog-prioritization`.
- Choosing between solution options rather than requirements. Use `decision-matrix`.
- Portfolio-level ordering of projects. Use `portfolio-prioritization`.

## Inputs
Required:
- The requirements list with IDs and short descriptions.
- The decision context: what the priority is for (release, MVP, budget cut) and the binding constraint.

Optional, improves quality:
- Business goals/OKRs, stakeholder input, effort estimates, dependencies, regulatory obligations.
- A preferred technique or organizational standard.

If the decision context is missing, ask for it; priority without a purpose is meaningless.

## Process
1. Choose the technique and state why:
   - MoSCoW for a fixed-scope release with a hard date; define "Must" as "release fails or is illegal/unsafe without it".
   - Kano when customer satisfaction drives the product (basic, performance, delighter).
   - Value/effort when estimates exist and quick wins matter.
   - Weighted scoring when several criteria and stakeholders must be balanced.
   - Cost of delay (and CD3) when time sensitivity differs strongly between items.
2. Define criteria and scales explicitly (e.g. business value 1-5, risk reduction 1-5, regulatory yes/no, effort S/M/L). Get or propose weights and mark proposed ones `[ASSUMPTION]`.
3. Pull out non-negotiables first: legal/regulatory, contractual, safety, security baseline. They are Must (or top) regardless of score.
4. Score each requirement with a one-line rationale citing a goal, stakeholder input or data. Where evidence is missing, mark `[ASSUMPTION]`.
5. Apply dependencies: a requirement cannot rank above something it depends on for delivery; raise enablers accordingly.
6. Check the balance: for MoSCoW, keep Must effort at or below roughly 60% of capacity if effort data exists, and flag if exceeded.
7. Produce the ranked list and a cut line against the constraint.
8. List contentious items with the stakeholders who disagree and the decision needed.
9. Recommend how to confirm: stakeholder review, sign-off owner, date to revisit.

## Output format
```markdown
# Requirements Prioritization: <scope / release>
Decision context: <purpose, constraint> · Technique: <name> – <why>

## Criteria
| Criterion | Scale | Weight | Source |
|---|---|---|---|

## Ranked Requirements
| Rank | Req ID | Title | Category/Score | Rationale | Dependencies | Effort |
|---|---|---|---|---|---|---|
--- cut line: <constraint> ---

## Non-negotiables
- <ID> – <regulation / contract reference>

## Contentious Items
| Req ID | Positions (who, what) | Decision needed | Decision owner |
|---|---|---|---|

## Assumptions and Next Steps
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] The technique choice is justified by the decision context.
- [ ] Every placement has a rationale; none is "stakeholder wants it" alone.
- [ ] Regulatory and contractual items are identified and placed first.
- [ ] Dependencies do not contradict the order.
- [ ] Must/top items fit the constraint, or the overflow is flagged explicitly.
- [ ] Assumed weights, values and efforts are marked `[ASSUMPTION]`.

## Common pitfalls
- Everything ends up "Must". Apply the "release fails without it" test and challenge each Must.
- Mixing techniques in one list (Kano categories next to value scores). Pick one primary method; others can inform rationale.
- Ranking by effort alone. Cheap items are not automatically valuable.

## Example
Input: 6 requirements for a mobile banking release, date fixed; R2 is a regulatory consent screen.

Excerpt of output:
| Rank | Req ID | Title | Category | Rationale |
|---|---|---|---|---|
| 1 | R2 | Consent screen | Must | Regulatory obligation `[confirm article reference]` |
| 2 | R1 | Login with biometrics | Must | Core flow; app store release depends on new auth |
| 5 | R5 | Dark mode | Could | Delighter per Kano view; no goal link |
