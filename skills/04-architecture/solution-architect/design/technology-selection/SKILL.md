---
description: Runs a structured technology selection - problem framing, weighted criteria including quality attributes, cost, risk and ecosystem health, a long-to-short list, a proof-of-concept plan with pass/fail criteria and a recommendation recorded as an ADR. Use when choosing a database, message broker, framework, platform, SaaS product or library for a significant need, or when a team's preferred tool must be justified objectively.
related: adr, build-vs-buy, tech-radar, vendor-evaluation, spike-report
prompt: Help us select a message broker for order and inventory events; we need ordering per order, replay for 7 days and we run on Kubernetes.
---

# Select a Technology

## Purpose
Reach a defensible technology choice through explicit criteria, evidence and a focused proof of concept, so the decision survives scrutiny and its risks are known before commitment.

## When to use
- A significant component (database, broker, API gateway, identity provider, framework, SaaS) must be chosen.
- Several teams advocate different tools and need an objective comparison.
- A radar Trial or Assess item is proposed for a real project.
- Procurement requires documented evaluation.

## When not to use
- The core question is whether to build or buy at all. Use `build-vs-buy`.
- Commercial vendor comparison with contracts and pricing. Use `vendor-evaluation`.
- A time-boxed technical investigation of one unknown. Use `spike-report`.

## Inputs
Required:
- The problem or capability needed and its key requirements (functional and quality).
- Hard constraints (hosting, licensing, regulation, existing stack, budget envelope).

Optional:
- Candidates already on the table, tech radar and standards.
- Team skills, operating model (who runs it), timeline.
- Volume and growth figures.

If requirements or constraints are missing, ask. Do not invent benchmark numbers, prices or version features; mark them `[VERIFY]`.

## Process
1. Frame the need as capabilities and quality scenarios, not as a product ("durable per-key ordered event log with 7-day replay"), so candidates are compared on the need.
2. Separate must-have constraints (knock-out) from weighted criteria. Typical criteria: functional fit, quality attributes (performance, availability, scalability, security), operability, cost (licence, infra, people), ecosystem and vendor health, skills, lock-in/exit cost, license compatibility.
3. Agree weights with stakeholders before scoring; weights must sum to 100.
4. Build the long list (5-8) from radar, market and team input; apply knock-outs to reach a short list of 2-3 with reasons for each exclusion.
5. Score the short list 1-5 per criterion with evidence and confidence; note where scores depend on unverified claims.
6. Identify the riskiest assumptions per candidate and design a proof of concept that tests them: scenarios, data volume, failure injection, success thresholds, time box, people.
7. Run a sensitivity check: does the winner change if the top two weights shift by ±10 points? If yes, state it.
8. Recommend with conditions: the choice, why, key risks with mitigations, exit strategy, and what the PoC must confirm.
9. Draft the ADR summary and the radar impact (e.g., new Trial item).
10. If the goal continues, suggest `adr` to record the decision, `spike-report` for PoC results or `build-vs-buy` when a product is compared with custom build.

## Output format
```markdown
# Technology Selection – <need>
## Need and Quality Scenarios
## Constraints (knock-out)
## Criteria and Weights
| Criterion | Weight | How measured |
## Long List and Exclusions
| Candidate | Excluded? | Reason |
## Short List Scoring
| Criterion (weight) | Cand. A | Cand. B | Cand. C | Evidence / confidence |
## PoC Plan
| Hypothesis | Test | Pass threshold | Time box | Owner |
## Sensitivity
## Recommendation, Risks and Exit Strategy
## ADR Draft Summary · Open Questions
```

## Quality checklist
- [ ] Need is stated independently of any product.
- [ ] Weights were fixed before scoring and sum to 100.
- [ ] Every exclusion and score has a reason; unverified claims are marked.
- [ ] PoC tests the riskiest assumptions with measurable pass thresholds.
- [ ] Exit cost and lock-in are assessed.
- [ ] Recommendation states conditions and is ready to become an ADR.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Starting from the favorite tool and reverse-engineering criteria. Frame the need first.
- Ignoring operability and people cost. The cheapest licence can be the most expensive to run.
- PoCs that demo happy paths. Test failure, scale and the unknowns.

## Example
Input: "Order and inventory events, per-order ordering, 7-day replay, Kubernetes."

Excerpt of output:
| Criterion (weight) | Log-based broker | Queue-based broker | Managed cloud stream |
|---|---|---|---|
| Per-key ordering + replay (30) | 5 | 2 (no native replay) | 4 `[VERIFY retention limits]` |
| Operability on our Kubernetes (20) | 3 | 4 | 5 (managed) |
- PoC hypothesis: Consumer rebalancing does not break per-order ordering under pod restarts; pass = zero out-of-order events in 1M messages `[volume to confirm]`.
