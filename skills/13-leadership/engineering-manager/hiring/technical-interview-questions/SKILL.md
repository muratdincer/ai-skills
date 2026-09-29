---
name: technical-interview-questions
description: "Prepares level-calibrated technical interview questions with follow-up probes and a behaviorally anchored scoring rubric for one interview stage. Use when an interviewer needs a question set for coding, system design, debugging or domain stages, when calibrating questions to a level, or when replacing trivia and puzzle questions with job-relevant ones."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 13-leadership
  role: engineering-manager
  area: hiring
  title: "Prepare technical interview questions"
  related: "interview-plan, interview-scorecard, career-ladder, job-description, candidate-debrief"
  prompt: "Prepare a 60-minute system design question set for a senior backend engineer, with rubric. We work on event-driven order processing."
---

# Prepare Technical Interview Questions

## Purpose
Give interviewers a small set of job-relevant questions with probes and a rubric, so every candidate at the same level is asked comparable questions and scored against the same observable anchors rather than gut feeling.

## When to use
- An interview stage has competencies assigned but no questions yet.
- Existing questions are trivia, puzzles or tied to one interviewer's favorite topic.
- Interviewers disagree on scores and need shared anchors for a level.

## When not to use
- The whole loop (stages, owners, competencies per stage) is not designed. Use `interview-plan`.
- Recording what a specific candidate said and scoring it. Use `interview-scorecard`.
- Defining what each level means. Use `career-ladder`.

## Inputs
Required:
- Role, target level, stage type (coding, system design, debugging, architecture, domain) and duration.
- Competencies this stage must assess.

Optional, improves quality:
- Team's real problem domain and tech stack, career ladder wording for the level.
- Existing question bank, known leaks, accessibility or language needs of candidates.

If the stage's competencies are missing, ask for them first; do not derive them from the question you would like to ask.

## Process
1. Restate the competencies and the level bar in observable terms (what a meets-bar answer at this level shows).
2. Choose 1-2 core problems for the stage length; a 60-minute stage rarely supports more than one deep problem plus one short one.
3. Base problems on realistic work from the team's domain, stripped of proprietary detail; avoid trivia, brain teasers and questions that reward memorized API details.
4. For each problem write the prompt exactly as it will be read, the intentionally left-open constraints, and what the candidate should ask to clarify.
5. Add progressive probes (base, extension, level-up) so the same problem can distinguish mid, senior and staff signals.
6. Write a rubric per competency with 4 anchors (strong no, no, yes, strong yes) described as observable behaviors, not adjectives.
7. List red flags and green flags that are job-relevant; exclude signals about accent, pedigree, confidence style or speed of speech.
8. Add a time plan (intro, problem, probes, candidate questions) and interviewer notes on hints and how hints affect scoring.
9. Check fairness: the question does not depend on knowledge unrelated to the role, allows reasonable accommodation, and is answerable in the candidate's chosen language/tooling where possible.
10. Mark domain facts or level expectations you inferred as `[ASSUMPTION]` and list open points for the hiring manager.
11. If the user's goal continues, suggest `interview-scorecard` to capture evidence against this rubric, or `interview-plan` to fit the stage into the loop.

## Output format
```markdown
# Question Set: <role> – <level> – <stage> (<duration>)
Competencies assessed: <list>

## Time Plan
| Minute | Segment |
|---|---|

## Problem 1: <title>
Prompt (read aloud): ...
Open constraints: ...
Expected clarifying questions: ...
Probes: base → extension → level-up
Hint policy: <hint> – <effect on score>

## Rubric
| Competency | Strong no | No | Yes | Strong yes |
|---|---|---|---|---|

## Green / Red Flags (job-relevant only)
- ...

## Assumptions and Open Points
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every question maps to at least one assigned competency.
- [ ] Rubric anchors describe observable behaviors for the target level.
- [ ] No trivia, puzzles, pedigree signals or culture-fit proxies.
- [ ] Problem fits the time with room for candidate questions.
- [ ] Hint policy and its effect on scoring are explicit.
- [ ] Inferred domain facts and level expectations are marked `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Scoring "got the answer" instead of reasoning, trade-offs and communication. Anchor the rubric on how the candidate works, not only the end state.
- Using one question for every level. Use probes to raise the bar instead of different, incomparable questions.
- Letting interviewers improvise follow-ups that change difficulty. Script the probes.

## Example
Input: Senior backend, system design, 60 min, competencies: distributed design, trade-offs, operability.

Excerpt of output:
- Problem: "Design order status updates for a marketplace where payment, stock and shipping services publish events."
- Level-up probe: "An event arrives twice and out of order during a broker failover. What does the customer see and how do you prevent it?"
- Rubric, trade-offs, Yes: names at least two options (outbox vs. dual write), states the failure each prevents and picks one with a reason.
- Weak anchor (avoid): "Good understanding of Kafka." Strong anchor: "Explains idempotency key choice and its storage cost."
