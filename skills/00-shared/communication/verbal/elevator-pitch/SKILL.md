---
name: elevator-pitch
description: "Writes a 30-60 second spoken pitch for an idea, project, product or request, tailored to one listener, with a hook, the problem, the proposal, proof, and a single concrete ask. Use when someone has a short window (corridor, call opening, intro at a meeting, funding or sponsorship request) to get a busy person interested enough to take the next step."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: communication
  area: verbal
  title: "Write an elevator pitch"
  related: "presentation-outline, executive-summary, value-proposition-canvas, problem-statement, stakeholder-map"
  prompt: "Give me a 45-second pitch to convince our CTO to sponsor a pilot for automated contract testing between our microservices."
---

# Write an Elevator Pitch

## Purpose
Condense an idea into 80-150 spoken words that make one specific listener care, believe it is credible, and agree to one small next step, so a short opportunity turns into a meeting, a sponsor or a decision.

## When to use
- Asking a senior person for sponsorship, budget, time or a meeting.
- Introducing a project or product at the start of a meeting or event.
- Preparing to explain your team's work to someone outside it in under a minute.

## When not to use
- The listener needs a written, self-contained summary. Use `executive-summary`.
- There is a full presentation slot. Use `presentation-outline`.
- The problem itself is still unclear. Use `problem-statement` first.

## Inputs
Required:
- The idea or request, and who the listener is (role, what they care about).
- The ask: what you want them to do next.

Optional:
- Evidence (numbers, customer quotes, pilot results), constraints, the setting and time limit, listener's known objections.

If the listener or the ask is missing, ask for it; a pitch without a target listener is a slogan. Never invent metrics or results; use `[TBD: figure]` placeholders the user must fill.

## Process
1. Name the listener and their top concern (cost, risk, growth, customers, team velocity, compliance). Label it `[ASSUMPTION]` if inferred.
2. Define one ask that is small and easy to say yes to (a 30-minute meeting, a pilot, an intro), not the whole program.
3. Write the hook: one sentence that links to the listener's concern with a concrete fact, question or consequence. Avoid jargon and acronyms the listener does not use.
4. State the problem in their terms: who is affected, how much, how often. One sentence.
5. State the proposal in one sentence: what you will do, not how it works internally.
6. Add proof: one number, pilot result, customer signal or precedent. Mark unverified proof `[TBD]`.
7. Say why now and why you: timing trigger and your credibility, in one sentence each at most.
8. Close with the ask and the next step, phrased as a question that invites yes.
9. Trim to the time limit: about 130 words per minute of speech; remove adjectives and anything the listener would not repeat to someone else.
10. Prepare one-line answers to the two most likely objections and a shorter 15-second variant.
11. If the user's goal continues, suggest `presentation-outline` for the follow-up meeting or `executive-summary` for a leave-behind.

## Output format
```markdown
# Elevator Pitch: <topic>
Listener: <role> – top concern: <...> | Length: <seconds> (~<words> words)
Ask: <one small next step>

## Pitch (spoken)
<Hook.> <Problem in their terms.> <Proposal.> <Proof.> <Why now / why us.> <Ask as a question.>

## 15-second version
<...>

## Likely objections
- "<objection>" -> <one-line answer>

Placeholders to fill: [TBD] ... | Assumptions: [ASSUMPTION] ...
```

## Quality checklist
- [ ] Written for one named listener and their concern.
- [ ] Exactly one ask, small enough to accept on the spot.
- [ ] Fits the time limit when read aloud (about 130 words per minute).
- [ ] No jargon the listener would not use; no invented numbers.
- [ ] The listener could repeat the core message in one sentence.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Starting with the solution's technology. Start with the listener's problem.
- Asking for everything at once (budget, team, roadmap). Ask for the next step only.
- Memorized text delivered like a script. Keep it as bullet cues if it will be spoken.

## Example
Input: CTO, sponsor a pilot for automated contract testing between microservices, 45 seconds.

Weak: "We want to introduce consumer-driven contract testing with a broker and CI integration because it is best practice and improves quality."

Strong (excerpt): "Last quarter, `[TBD: n]` of our production incidents came from one service changing an API another one depended on. We catch those today only after release. I'd like to run a six-week pilot with the two teams behind the payment flow, where every API change is checked against its consumers before merge. If it cuts those incidents, we roll it out; if not, we stop. Could you sponsor it and give us 30 minutes next week to agree the success measure?"
