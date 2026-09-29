---
name: discovery-workshop
description: "Designs and documents a client discovery workshop for an early engagement, with objectives, participant mix, pre-work, a timeboxed agenda, question bank by topic, breakout and note-and-vote convergence mechanics, and a structured output (goals, pain points, current landscape, requirements themes, constraints, risks, next steps). Use when starting a new client engagement or presales pursuit, when a vague client need must be shaped into scope, or when workshop notes must be turned into a discovery summary."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 14-presales-consulting
  role: presales-consultant
  area: consulting
  title: "Run a client discovery workshop"
  related: "workshop-plan, facilitation-guide, current-state-assessment, stakeholder-map, interview-question-set"
  prompt: "Plan a one-day discovery workshop with a retail client who wants to \"modernize their e-commerce platform\" and has not shared details."
---

# Run a Client Discovery Workshop

## Purpose
Turn an early, loosely defined client need into a shared understanding of goals, pain points, landscape and constraints, so the next step (assessment, proposal or estimate) rests on evidence gathered with the client, not on assumptions.

## When to use
- A new engagement or pursuit starts and the client's need is still broad.
- Several client stakeholders hold different views that must be surfaced and aligned.
- Raw workshop notes must be synthesized into a discovery summary for the client.

## When not to use
- A generic internal workshop is being planned. Use `workshop-plan`.
- The client wants a formal evaluation of its current systems and maturity. Use `current-state-assessment`.
- The need is already clear and a package must be compared to requirements. Use `fit-gap-analysis`.

## Inputs
Required:
- The client's stated need or trigger for the engagement, and the workshop format (duration, onsite/remote).

Optional, improves quality:
- Client industry, size, known systems, prior documents.
- Expected attendees and their roles.
- What the engagement should lead to (proposal, roadmap, assessment).
- Raw notes or transcript if the workshop already took place.

If the need or format is missing, ask. If running synthesis only, ask for the notes. Other gaps become pre-work questions.

## Process
1. Set 2-4 workshop objectives stated as outputs (e.g. "agreed top 5 business goals with measures"), and state what the workshop will not decide.
2. Define the participant mix: executive sponsor (opening and closing), business process owners, IT/architecture, operations, and end-user representatives. Keep active participants around 6-12; flag missing roles as a risk.
3. Design pre-work: a short questionnaire and a document request (org chart, system landscape, KPIs, prior initiatives) so workshop time goes to discussion, not data collection.
4. Build a timeboxed agenda: opening with sponsor's why-now; goals and success measures; current process and pain points; system and data landscape; constraints (budget, regulation, timeline, skills); risks and ideas; prioritization; wrap-up with next steps. Add breaks roughly every 90 minutes.
5. Prepare a question bank per agenda block, ordered from broad to specific (funnel), with probes such as "what happens today when…", "how often…", "what does it cost you when…". Avoid leading or solution-first questions.
6. Plan convergence mechanics: silent individual note writing, clustering by theme, dot voting or impact/effort placement, and breakouts by domain when the group exceeds about 8 active people, each reporting back with a fixed template.
7. Assign roles: facilitator, scribe, domain expert, timekeeper; agree how notes are captured and how personal data in examples is minimized.
8. After the workshop, synthesize: separate what participants said (with attribution by role) from your interpretation (`[ASSUMPTION]`); cluster pain points and goals; note conflicts between stakeholders explicitly rather than averaging them.
9. Produce the discovery summary: goals with measures, prioritized pain points, current landscape sketch, requirement themes, constraints, risks, hypotheses to validate, and open questions with owners.
10. Propose next steps with owners and dates only if agreed; otherwise `[TBD]`.
11. If the goal continues, suggest `current-state-assessment` for a deeper diagnosis, `fit-gap-analysis` if a package is in play, or `proposal-writing` to shape the offer.

## Output format
```markdown
# Discovery Workshop: <client> — <topic>
## Plan
- Objectives (outputs): ...  - Out of scope: ...
- Participants: | Role | Name / TBD | Why needed |
- Pre-work: questionnaire items, documents requested

## Agenda
| Time | Block | Goal | Method | Lead |

## Question Bank
### <Block>
1. <broad question> → probes: ...

## Discovery Summary (after workshop)
### Goals and Success Measures
| Goal | Measure | Raised by (role) | Priority (votes) |
### Pain Points
| Pain point | Impact | Frequency | Raised by | Evidence / [ASSUMPTION] |
### Current Landscape
### Requirement Themes
### Constraints and Risks
### Stakeholder Divergences
### Hypotheses to Validate
### Open Questions — owner — needed by
### Next Steps
```

## Quality checklist
- [ ] Objectives are phrased as tangible workshop outputs.
- [ ] The agenda is timeboxed with breaks and a clear convergence step.
- [ ] Questions are open, funnel-ordered and not solution-leading.
- [ ] Said versus inferred is separated; inferences are labeled `[ASSUMPTION]`.
- [ ] Stakeholder conflicts are recorded, not averaged away.
- [ ] Every open question and next step has an owner or is marked `[TBD]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Pitching the solution during discovery. It anchors the client and hides real needs; hold solution talk for the wrap-up.
- Only senior people in the room. They describe the process as designed, not as lived; include operational users.
- Summaries that list everything said. Prioritize with the client's votes and tie pain points to impact.

## Example
Input: "Retail client, 'modernize e-commerce', one day onsite, attendees unknown."

Excerpt of output:
| Time | Block | Goal | Method |
|---|---|---|---|
| 09:00 | Why now (sponsor) | Shared reason and success picture | Sponsor talk + Q&A |
| 10:45 | Pain points | Top pain points with impact | Silent notes → cluster → dot vote |

- Question: "Walk us through what happens today from a customer placing an order to it leaving the warehouse." Probe: "Where do people re-enter or check data by hand?"
- Risk: No operations or warehouse attendee confirmed `[TBD]`.
