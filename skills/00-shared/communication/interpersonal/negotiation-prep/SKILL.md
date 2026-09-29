---
name: negotiation-prep
description: "Prepares a negotiation by defining your goal, interests, BATNA, walk-away point, the counterpart's likely interests and BATNA, the zone of possible agreement, tradeable concessions and an opening position with its justification. Use when someone must negotiate scope, deadline, budget, resources, a vendor contract, rates or terms with a customer, vendor, sponsor or another team."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: communication
  area: interpersonal
  title: "Prepare for a negotiation"
  related: "conflict-resolution, stakeholder-map, trade-off-analysis, vendor-evaluation, pricing-analysis"
  prompt: "Help me prepare to negotiate with the business sponsor who wants the full scope by March while we can only deliver about 60% with the current team."
---

# Prepare for a Negotiation

## Purpose
Enter a negotiation knowing what you need, what you can give, where you walk away and what the other side probably needs, so the outcome is decided by preparation and objective criteria rather than pressure in the room.

## When to use
- Negotiating scope, deadline, budget or headcount with a sponsor or customer.
- Negotiating a vendor contract, rates, SLA or payment terms.
- Agreeing resources or priorities with another team that competes for the same capacity.

## When not to use
- You are a neutral party helping others resolve a dispute. Use `conflict-resolution`.
- The question is which technical or delivery option is best, not terms between parties. Use `trade-off-analysis`.
- Comparing vendors before choosing one. Use `vendor-evaluation`.

## Inputs
Required:
- What is being negotiated, with whom, and the user's goal.

Optional:
- Current offer or demand, constraints (budget ceiling, legal, contract), relationship history, deadline, market or internal benchmarks, authority limits of each side.

If the goal or the counterpart is unknown, ask first. Never invent prices, rates, dates or the counterpart's limits; mark estimates `[ASSUMPTION]` and unknowns `[UNKNOWN]`. Contract and commercial data may be confidential; keep it to what is needed.

## Process
1. Define the issues on the table (scope, date, price, quality, risk sharing, payment, support) and your goal for each; rank them by importance to you.
2. Write your interests behind each goal (why it matters), separate from your positions.
3. Define your BATNA: what you will actually do if there is no agreement, and how good it is. Strengthen it before the meeting if possible.
4. Set your walk-away point (reservation value) per key issue, derived from the BATNA, and your target (ambitious but justifiable).
5. Model the counterpart: interests, constraints, decision authority, likely BATNA and pressure (deadlines, internal politics). Label all of it `[ASSUMPTION]` and list questions to test it.
6. Estimate the zone of possible agreement; if none appears, plan to improve your BATNA, add issues, or not negotiate.
7. Build a concession plan: tradeables that are cheap for you and valuable to them, and what you ask in return for each (never concede without getting something).
8. Prepare objective criteria and evidence to justify positions (velocity data, market rates, effort estimates, precedent).
9. Draft the opening: position, justification, and whether to anchor first (anchor first when you have good information; otherwise let them open and probe).
10. Prepare questions to uncover interests, answers to expected pressure tactics (deadline pressure, "final offer", nibbling), and who has final sign-off on both sides.
11. Plan the close: how agreements will be summarized in writing, open items, and next steps.
12. If the user's goal continues, suggest `stakeholder-map` to analyze influencers behind the counterpart, `trade-off-analysis` to evaluate package options, or `conflict-resolution` if the relationship has already broken down.

## Output format
```markdown
# Negotiation Prep: <topic> with <counterpart>
Goal: ... | Date: ... | Authority: ours <...> / theirs <...>

| Issue | Priority | Our target | Our walk-away | Their likely position [ASSUMPTION] |
|---|---|---|---|---|

Our interests: ...
Our BATNA: ... (strength: strong/medium/weak) | How to improve it: ...
Their interests and BATNA [ASSUMPTION]: ...
Zone of possible agreement: ...

## Concession plan
| We can give | Cost to us | Value to them | We ask in return |

## Opening position and justification
...
## Questions to ask
1. ...
## Pressure tactics and responses
- "<tactic>" -> <response>
## Close
Written summary owner: ... | Open items: ... | Next step: ...
```

## Quality checklist
- [ ] Every key issue has a target and a walk-away point derived from a stated BATNA.
- [ ] Interests are separated from positions for both sides; counterpart analysis is labeled `[ASSUMPTION]`.
- [ ] Every concession has something asked in return.
- [ ] Positions are backed by objective criteria or evidence; no invented numbers.
- [ ] Decision authority on both sides is known or listed as an open question.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Negotiating a single issue (price or date only). Add issues so trades become possible.
- No real BATNA, so any deal looks acceptable. Work out the no-deal alternative first.
- Agreeing verbally and moving on. Summarize the agreement in writing the same day.

## Example
Input: sponsor wants full scope by March; team can deliver about 60%.

Weak: "Tell the sponsor it is impossible and ask for more time."

Strong (excerpt):
- Issues: scope, date, team size, quality bar.
- Our BATNA: deliver the 60% core by March and escalate remaining scope to the steering committee `[ASSUMPTION: escalation is available]`.
- Their interest `[ASSUMPTION]`: the March regulatory reporting feature, not every item in scope.
- Concession: we commit to the regulatory feature by March if they move `[TBD]` low-value items to Q2 and approve one extra developer.
- Evidence: last four iterations' throughput `[TBD: numbers]` projected to March.
