---
description: Writes a specific, impact-focused recognition message for an individual or team, naming the concrete behavior, the result it produced and why it matters, adapted to channel (private, team, company-wide). Use when a manager or peer wants to thank someone for work, highlight invisible contributions, or celebrate a launch, incident response or mentoring effort.
related: feedback-sbi, announcement, tone-rewrite, performance-review
prompt: Write a team-channel thank-you for Selin, who spent the weekend untangling the data migration rollback and wrote a clean postmortem.
---

# Write a Recognition Message

## Purpose
Recognize contributions in a way that feels genuine to the recipient and teaches the wider team which behaviors matter, by being specific about what was done and its impact.

## When to use
- Someone did work worth acknowledging: delivery, incident handling, mentoring, quality or glue work.
- A launch or milestone should credit everyone who contributed, including less visible roles.
- A manager wants to reinforce a behavior that aligns with team values.

## When not to use
- Developmental or corrective feedback. Use `feedback-sbi`.
- Formal review write-ups. Use `performance-review`.
- A general release or org announcement. Use `announcement`.

## Inputs
Required:
- Who is recognized and what they did (at least one concrete example).

Optional, improves quality:
- The measurable or observable impact (users, time saved, incident duration, risk avoided).
- The channel and audience: private message, team channel, all-hands, written note to their manager.
- The recipient's preference for public or private recognition, if known.
- Team values or principles to link to.

If there is no concrete example, ask for one; generic praise has little value.

## Process
1. Identify the specific behavior (what they did) and separate it from the outcome (what changed because of it).
2. Quantify impact only with numbers the user provided; otherwise describe it qualitatively. Do not invent figures.
3. Explain why it mattered: user, customer, team or business consequence, or a value it demonstrates.
4. Credit everyone who materially contributed; check for overlooked contributors (reviewers, testers, on-call, support, documentation).
5. Match the channel: private notes can be personal; public messages stay professional and avoid private details.
6. Respect preferences: if the person is known to prefer private recognition, recommend a private message and optionally a note to their manager.
7. Keep it short: 3-6 sentences, no superlatives stacked on each other, no comparison with other people.
8. Avoid tying recognition to overwork as the ideal (e.g. praising weekend hours) without also addressing sustainability.
9. Offer one alternate version (shorter or for another channel) if useful.

## Output format
```markdown
**Channel:** <private / team / company / note to manager>

<Opening: who and what, in one sentence>
<Specific behavior with a concrete detail>
<Impact and why it matters>
<Credit to others involved, if any>
<Closing thanks>

---
Alternate (<channel>): <short version>
```

## Quality checklist
- [ ] Names at least one concrete behavior, not only a trait ("great job").
- [ ] Impact is real: numbers only if provided, otherwise qualitative.
- [ ] All material contributors are credited.
- [ ] Tone fits the channel; no private details in public messages.
- [ ] Does not glorify unsustainable effort.
- [ ] 3-6 sentences.

## Common pitfalls
- Generic praise ("rockstar", "amazing work") that could be sent to anyone. Name the action.
- Recognizing only the visible hero of an incident or launch. Ask who else helped.
- Recognizing some people consistently in public and others never. Keep recognition fair across the team over time.

## Example
Input: "Selin spent the weekend untangling the data migration rollback and wrote a clean postmortem."

Output excerpt (team channel):
"Thank you, Selin, for leading the data migration rollback on Saturday. You worked through the rollback until the data was consistent again, and then wrote a postmortem clear enough for the whole team to learn from. That combination of calm incident handling and honest follow-up is exactly how we want to learn from failures. `[Add others who helped, if any – not stated in input]` Selin, please take the time back this week."
