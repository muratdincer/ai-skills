---
description: Surfaces the assumptions behind a plan, product idea, estimate or decision, classifies them (desirability, viability, feasibility, usability, ethical/regulatory, delivery), plots them by importance and evidence, and turns the riskiest into testable statements with the cheapest test. Use before committing budget or scope, when a plan feels optimistic, or when someone asks what must be true for this to work.
related: hypothesis-statement, experiment-design, pre-mortem, risk-register, problem-statement
prompt: Map the assumptions behind our plan to launch self-service onboarding for SME customers next quarter.
---

# Map Assumptions

## Purpose
Make visible what must be true for a plan to succeed, and focus validation effort on the few assumptions that are both critical and weakly evidenced, before they turn into expensive surprises.

## When to use
- A new product, feature, initiative or business case is about to be approved or funded.
- A plan, roadmap or estimate rests on beliefs nobody has checked.
- A team disagrees and the disagreement is really about unstated beliefs.

## When not to use
- The goal is to list things that could go wrong in delivery. Use `pre-mortem` or `risk-register`.
- A single assumption is already chosen and needs a formal test. Use `hypothesis-statement` and `experiment-design`.
- The problem itself is not yet defined. Use `problem-statement`.

## Inputs
Required:
- The plan, idea or decision, with its intended outcome.

Optional, improves quality:
- Target users or customers, business model, timeline, dependencies.
- Evidence already available (research, data, pilots, benchmarks).
- Known constraints (budget, regulation, technology).

If the plan or its intended outcome is missing, ask for it. Ask at most five focused questions at once; everything else becomes an open question.

## Process
1. Restate the plan and its intended outcome in one sentence each.
2. Extract assumptions with "For this to work, it must be true that...". Include the stated ones and the implicit ones you infer, labeling inferred ones `[INFERRED]`.
3. Write each as a single, falsifiable belief ("SME admins will complete setup without a call"), not a topic ("onboarding").
4. Classify each: desirability (they want it), usability (they can use it), feasibility (we can build/operate it), viability (it pays off), ethical/regulatory (we are allowed to), delivery (we can do it on time with these people).
5. Rate importance: if false, does the plan fail (High), weaken (Medium) or barely change (Low)?
6. Rate evidence: Strong (observed behavior, data), Some (stated intent, analogies, expert opinion), None (belief).
7. Place them in the 2x2: high importance / weak evidence = test first; high importance / strong evidence = monitor; low importance = park.
8. For each "test first" item, write a testable statement with a pass threshold and the cheapest credible test (data lookup, interviews, prototype, smoke test, spike, legal review), plus owner role and time box.
9. Note dependencies: which assumptions, if false, invalidate others.
10. Summarize what would change the go/no-go decision and which assumptions remain untested.
11. If the user's goal continues, suggest `hypothesis-statement` and `experiment-design` for the top items, or `risk-register` to track the delivery-related ones.

## Output format
```markdown
# Assumption Map: <plan>

**Plan:** <one sentence> **Intended outcome:** <one sentence>

| # | Assumption (falsifiable) | Type | Importance | Evidence | Quadrant | Source |
|---|---|---|---|---|---|---|
| A1 | ... | Desirability | H | None | Test first | Stated / [INFERRED] |

## Test First
| # | Testable statement | Pass threshold | Cheapest test | Owner (role) | Time box |
|---|---|---|---|---|---|
| A1 | We believe ... | <threshold or [TBD]> | ... | ... | ... |

## Monitor
- ...

## Parked
- ...

## Dependencies and Decision Impact
- If A1 is false, then ...

## Open Questions
- ...
```

## Quality checklist
- [ ] Every assumption is a single falsifiable sentence, not a topic.
- [ ] All six types were considered; empty types are a conscious outcome.
- [ ] Inferred assumptions are labeled `[INFERRED]`; nothing is presented as evidence without a source.
- [ ] Each "test first" item has a threshold, a test and an owner role.
- [ ] Thresholds and numbers not given by the user are marked `[TBD]`, not invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Listing only feasibility assumptions because they are comfortable for technical teams. Desirability and viability usually kill more plans.
- Treating stakeholder conviction as evidence. Opinion is "Some" at best.
- Designing expensive tests first. Start with the cheapest test that could prove the assumption false.

## Example
Input: "We plan to launch self-service onboarding for SME customers next quarter."

Excerpt of output:
| # | Assumption | Type | Importance | Evidence | Quadrant |
|---|---|---|---|---|---|
| A1 | SME admins can finish setup without calling support. | Usability | H | None | Test first |
| A2 | Self-service reduces onboarding cost enough to cover the build. | Viability | H | Some – cost per onboarding known, effort [TBD] | Test first |
| A3 | Identity verification can be done online under current regulation. | Regulatory | H | None `[INFERRED]` | Test first |

Test for A1: unmoderated prototype test with 5-8 SME admins; pass if [TBD — agree threshold] complete setup unaided.
