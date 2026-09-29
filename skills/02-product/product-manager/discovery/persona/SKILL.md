---
name: persona
description: "Builds an evidence-based persona with context, goals, pains, behaviors, decision criteria and quotes, tracing every attribute to research and flagging proto-persona assumptions. Use when research data (interviews, surveys, analytics, support tickets) must be turned into a shared user model, or when someone asks for a persona or user profile for design and product decisions."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-manager
  area: discovery
  title: "Build a persona"
  related: "jobs-to-be-done, customer-journey-map, research-synthesis, feedback-synthesis, problem-interview-script"
  prompt: "Create a persona for warehouse shift supervisors from these 8 interview summaries."
---

# Build a Persona

## Purpose
Condense research about a user group into a persona that teams can use to make design and prioritization decisions, with each attribute traceable to evidence so the persona does not become fiction.

## When to use
- After interviews, surveys or field studies, to share who the users are.
- Teams argue from personal opinion about "the user" and need a common reference.
- An assumption-based proto-persona is needed to plan research (clearly labeled as such).

## When not to use
- You need the job and outcomes independent of user type. Use `jobs-to-be-done`.
- You need the step-by-step experience over time. Use `customer-journey-map`.
- You need to synthesize raw research into themes first. Use `research-synthesis`.

## Inputs
Required:
- Research material (notes, transcripts, survey results) or, for a proto-persona, explicit team assumptions.

Optional, improves quality:
- Analytics on behavior and segments, support data, sales notes.
- Product decisions the persona should inform.

If no material is given, ask whether to build a proto-persona; label it `[PROTO-PERSONA – ASSUMPTIONS]`. Mask or remove personal data from quotes.

## Process
1. Define the segment boundary: which behaviors or context set this group apart (not age or gender unless it changes behavior).
2. Extract attributes from each source: context/environment, goals, pains, current behaviors and workarounds, tools, decision criteria, constraints.
3. Cluster attributes; keep those seen in several participants. Note frequency (e.g. 6/8).
4. Check for multiple personas hiding in one: if goals or behaviors split into distinct patterns, create separate personas.
5. Write the persona: a descriptive name tied to role, short context, top 3 goals, top 3 pains, key behaviors, what triggers them to seek a solution, what makes them adopt or reject.
6. Add 2-3 real, anonymized quotes that capture the mindset.
7. State design implications: 3-5 "therefore we should / should not" statements.
8. Add an evidence table and a confidence level; list gaps for the next research round.
9. Mark every point you inferred rather than read in the input as `[ASSUMPTION]` and carry it into assumptions or open questions. If the user's goal continues, suggest the next skill: `jobs-to-be-done` or `customer-journey-map` to go deeper on the persona's goals, or `problem-interview-script` to close evidence gaps.

## Output format
```markdown
# Persona: <descriptive name> (<role/segment>)
Confidence: H/M/L · Based on: <sources, n>

## Context
...
## Goals
1. ...
## Pains
1. ...
## Behaviors and Workarounds
- ...
## Triggers and Decision Criteria
- ...
## Quotes (anonymized)
> "..."
## Design Implications
- Therefore we should ...
## Evidence
| Attribute | Evidence | Frequency |
|---|---|---|
## Gaps
- ...
```

## Quality checklist
- [ ] Every attribute traces to a source or is marked `[ASSUMPTION]`.
- [ ] Demographic details are included only if they change behavior.
- [ ] Quotes are real and anonymized; no personal data.
- [ ] Design implications are concrete and actionable.
- [ ] Confidence and sample size are stated.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Inventing a stock photo, hobbies and a backstory. Decorative fiction reduces trust; keep to behavior-relevant facts.
- Averaging distinct groups into one persona. Split when goals diverge.
- Treating the persona as permanent. Date it and revisit after major research.

## Example
Input: "8 interview summaries with warehouse shift supervisors."

Excerpt of output:
- Name: "Firefighting Shift Supervisor" — Confidence: Medium, n=8.
- Pain: Learns about late inbound trucks only when the dock is idle (6/8).
- Workaround: Personal WhatsApp group with drivers (5/8).
- Implication: Surface inbound delay alerts on mobile before the shift starts.
