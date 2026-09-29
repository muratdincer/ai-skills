---
name: retrospective-format
description: "Designs a retrospective format tailored to the team's current mood, topic, size and setting: picks or adapts activities for each retro phase, writes the prompts, timings and materials, and explains why the format fits. Use when retros feel stale, when a specific theme (incident, conflict, milestone, new team) needs a dedicated retro, or when someone asks for a new retro idea or template."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: agile-delivery
  area: ceremonies
  title: "Design a retrospective format"
  related: "retrospective-facilitation, team-health-check, workshop-plan, facilitation-guide, conflict-resolution"
  prompt: "Our retros have become boring and the same three people talk. Design a 45-minute remote retro format for a tired team of 9 after a hard release."
---

# Design a Retrospective Format

## Purpose
Give the facilitator a ready-to-run retrospective design whose activities match the team's energy and the topic at hand, so the session surfaces real issues and converges on actions instead of repeating a worn-out routine.

## When to use
- The usual format produces the same topics or low participation.
- A themed retro is needed: after an incident or difficult release, at a milestone, for a newly formed team, around a conflict, or at year end.
- The setting changes (remote, hybrid, large group, very short time box).

## When not to use
- Running the session and producing actions from notes. Use `retrospective-facilitation`.
- A general workshop not about reflecting on past work. Use `workshop-plan`.
- An interpersonal conflict that needs mediation rather than a group session. Use `conflict-resolution`.

## Inputs
Required:
- Team size, setting (remote/on-site/hybrid) and time available.
- The reason for a new format or the theme to address.

Optional, improves quality:
- Team mood or health signals, recent events.
- Formats already used recently (to avoid repeats).
- Participation issues (dominant voices, silence, new members).

If the reason or setting is missing, ask for it (at most 3 questions).

## Process
1. Diagnose the need: energy level (low/normal/high), safety level (low if blame, silence or recent conflict), and topic breadth (open reflection vs. a focused theme). State the diagnosis and mark inferred parts `[INFERRED]`.
2. Choose one activity per phase (set the stage, gather data, generate insights, decide actions, close) from well-known patterns, e.g. check-in scales, timeline, mad/sad/glad, 4Ls, sailboat, start/stop/continue, 5 whys, circle of influence, dot-voting, ROTI. Explain the fit of each choice in one line.
3. Adapt for safety: when safety is low, use anonymous input, pairs before plenary, and focus on the system ("what made this hard") rather than people. Consider a safety check vote at the start.
4. Adapt for participation: silent writing before talking, round-robin read-outs, time caps per speaker, breakouts of 3-4 for groups larger than about 8.
5. Adapt for setting: for remote, specify board layout, anonymous mode and camera-optional parts; for hybrid, make everyone use the same digital board.
6. Write the exact prompts the facilitator will say or put on the board for each activity.
7. Allocate minutes per activity so the phases sum to the time box, reserving at least a quarter for insights and actions.
8. List materials and preparation (board template, timeline data, previous actions).
9. Add a fallback: what to cut if time runs short, and what to do if energy is very low.
10. If the user's goal continues, suggest `retrospective-facilitation` to run the session and turn results into actions.

## Output format
```markdown
# Retro Format: <name> – <theme>
For: <team size, setting> · Time: <min>
Diagnosis: energy <L/N/H>, safety <L/N/H>, focus <open/theme> – <why>

| Phase | Activity | Minutes | Prompt (verbatim) | Why it fits |
|---|---|---|---|---|
| Set the stage | | | | |
| Gather data | | | | |
| Generate insights | | | | |
| Decide actions | | | | |
| Close | | | | |

## Participation and Safety Rules
- ...

## Preparation and Materials
- ...

## If Time Runs Short / Energy Is Low
- ...
```

## Quality checklist
- [ ] All five phases are covered and minutes sum to the time box.
- [ ] Each activity has a verbatim prompt and a one-line rationale tied to the diagnosis.
- [ ] Safety and participation adaptations match the stated problem.
- [ ] At least a quarter of the time is left for insights and actions.
- [ ] The format differs from formats the team used recently, if those were given.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Choosing a fun activity that does not serve the goal. Novelty is a means; convergence on actions is the outcome.
- Using a "what went wrong" frame after a painful event with low safety. Start with facts (timeline) and the system, not the people.
- Packing too many activities. One activity per phase is enough for 45-60 minutes.

## Example
Input: "Tired team of 9, remote, 45 minutes, after a hard release; same three people talk."

Excerpt of output:
- Diagnosis: energy low, safety normal `[INFERRED]`, focus theme "the release".
- Gather data: Release timeline (10 min) – "Add one moment where you felt the release was at risk, anonymously."
- Insights: Circle of influence in 3 breakouts of 3 (12 min) – moves discussion from venting to what the team controls.
- Close: ROTI 1-5 (3 min).
