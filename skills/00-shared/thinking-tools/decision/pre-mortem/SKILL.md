---
description: Runs a pre-mortem on a plan, project, launch or decision by assuming it has already failed and working backwards to the most plausible causes, early warning signals and mitigations. Use before committing to a plan, launch, migration or major decision, when a team seems overconfident, or when someone asks "what could go wrong?" or "run a pre-mortem".
related: risk-register, assumption-mapping, bias-check, raid-log, technical-risk-review
prompt: Run a pre-mortem on our plan to migrate the billing database to a new cloud region over one weekend in March.
---

# Run a Pre-Mortem

## Purpose
Surface the risks a team knows about but does not say, by making failure the premise instead of a possibility. The result is a ranked list of failure stories with owners, tripwires and mitigations, produced while the plan can still change cheaply.

## When to use
- A plan, launch, migration, contract or hiring decision is about to be committed.
- The team shows optimism or consensus that has not been challenged.
- A risk register exists but feels generic ("scope creep", "resource shortage").

## When not to use
- Something has already failed and you need causes. Use `postmortem` or `five-whys`.
- You need a maintained, ongoing risk log rather than a one-off exercise. Use `risk-register` or `raid-log`.
- You want to test the reasoning of a single analysis for bias. Use `bias-check`.

## Inputs
Required:
- The plan or decision: goal, scope, timeline and key steps (a short description is enough).

Optional, improves quality:
- Success criteria and the date by which success will be judged.
- Team, dependencies, constraints, previous similar efforts and what happened.
- Existing risk list, so the pre-mortem adds rather than repeats.

If the plan description is missing, ask for it. If success criteria are missing, propose one and mark it `[ASSUMPTION]`.

## Process
1. Restate the plan in two lines and fix the "failure date": a concrete point after which the outcome is judged (for example "8 weeks after go-live"). Define what failure means there in observable terms.
2. Write the premise: "It is <failure date>. The plan failed badly." Treat failure as certain; do not debate whether it could fail.
3. Generate failure stories across lenses so the list is not one-sided: people and skills, dependencies and suppliers, technology and data, process and decisions, customers and market, regulation and security, timing and sequencing. Aim for 10-20 stories, each one sentence with a cause and a consequence.
4. If working with a group, ask each person to write their stories silently before sharing, then collect them round-robin one at a time; this prevents the most senior voice from anchoring the list.
5. Separate facts from inference: mark each story as grounded in something the user stated or observed, or as `[ASSUMPTION]`. Do not invent incidents, names or numbers.
6. Merge duplicates and rank stories by likelihood and impact (High/Medium/Low each), with a one-line justification. Flag "silent killers": high-impact items nobody currently owns.
7. For the top 5-7 stories, write: an early warning signal (a tripwire that would show it is starting), a preventive action, a contingency if it happens anyway, and an owner (or `[TBD]`).
8. Identify the plan changes the ranking implies: scope cuts, extra checkpoints, reordering, a go/no-go gate, or a decision to stop. State explicitly if no change is needed and why.
9. List open questions and the assumptions the plan rests on that nobody has verified.
10. Fill the output template and keep it to about one page.
11. If the goal continues, suggest the next skill: `risk-register` or `raid-log` to track the risks, `assumption-mapping` to test the riskiest assumptions, or `bias-check` if the decision itself looks overconfident.

## Output format
```markdown
# Pre-Mortem: <plan name>
Failure date: <date/point> · Failure means: <observable definition>

## Failure Stories (ranked)
| # | Story (cause → consequence) | Lens | Likelihood | Impact | Basis |
|---|---|---|---|---|---|
| 1 | ... | Dependencies | H | H | Stated / [ASSUMPTION] |

## Top Risks: Signals and Responses
| # | Early warning signal | Preventive action | Contingency | Owner |
|---|---|---|---|---|

## Recommended Plan Changes
- ...

## Unverified Assumptions and Open Questions
1. <question> — <why it matters> — <who can answer>
```

## Quality checklist
- [ ] Failure is defined in observable terms at a concrete point in time.
- [ ] Stories cover at least four different lenses, not only technology.
- [ ] Each top risk has a measurable early warning signal, not just "monitor closely".
- [ ] Facts and inferences are separated; nothing is invented.
- [ ] At least one concrete plan change is proposed, or its absence is justified.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Asking "what might go wrong?" instead of "it failed, why?". The hypothetical framing invites defensive, generic answers; keep the failure premise.
- Ending with a list and no plan change. A pre-mortem that changes nothing was only a ritual.
- Vague risks ("communication issues"). Rewrite each as a specific cause with a consequence.

## Example
Input: "Migrate the billing database to a new region over one weekend in March."

Weak story: "Migration might have technical problems."
Strong story: "Replication lag was not measured under month-end load, so cutover took 30 hours and invoices went out late." Basis: `[ASSUMPTION]` (load test not mentioned).
- Early warning signal: replication lag above the agreed threshold in the rehearsal run.
- Preventive action: full rehearsal with production-sized data two weeks before; go/no-go gate on Friday noon.
- Contingency: documented rollback to the old region within 2 hours `[TBD: confirm with DBA]`.
