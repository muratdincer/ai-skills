---
name: observation-notes
description: "Structures raw job-shadowing or contextual observation notes into a task sequence with timings, tools used, pains, workarounds, interruptions and the gap between the documented and the actual process. Use after observing users at work, when field notes are messy, or when asked 'what did we learn from watching the team do this?'."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: elicitation
  title: "Structure job-shadowing observations"
  related: "as-is-process, interview-notes-analysis, value-stream-map, customer-journey-map, research-synthesis"
  prompt: "Here are my notes from shadowing two call-center agents for three hours. Structure them into tasks, pains and workarounds."
---

# Structure Job-Shadowing Observations

## Purpose
Turn raw observation notes into evidence about how work is really done, so requirements address actual tasks, workarounds and friction instead of the process as described in documents or interviews.

## When to use
- After job shadowing, contextual inquiry or a "follow me around" session.
- When interviews and procedures disagree and you observed the real work.
- Before as-is process modeling, to ground it in what people actually do.

## When not to use
- The notes are from a question-and-answer interview. Use `interview-notes-analysis`.
- You need a formal as-is process model with lanes and timings. Use `as-is-process` (it can take this output as input).
- The observations are from usability testing of a prototype. Use `research-synthesis`.

## Inputs
Required:
- The observation notes (raw text, time-stamped if possible).

Optional, improves quality:
- Who was observed (role, experience level, site), date, duration, and what triggered the work.
- The documented procedure for comparison.
- Photos or descriptions of screens, forms, sticky notes and spreadsheets used.

If no notes are given, ask for them. If role and context are missing, continue and list them as open questions.

## Process
1. Anonymize: refer to observed people by role and code (Agent A), and mask any customer or colleague data in the notes.
2. Separate observation from interpretation: what was seen or heard ("switched to Excel, copied the policy number") versus what you think it means. Label every interpretation `[ASSUMPTION]`.
3. Reconstruct the task sequence per session: trigger, steps, systems/tools, hand-offs, end state. Keep timestamps or durations where noted; never estimate missing ones.
4. Tag each event: Task step, Tool/system switch, Wait, Interruption, Error/rework, Workaround, Informal rule ("we always call first if..."), Artifact (shadow spreadsheet, paper list, note), Quote.
5. Extract workarounds and shadow artifacts explicitly; each one signals an unmet need. State the need it covers.
6. Identify pains with evidence: frequency seen in the session, time lost if measured, consequence (error, delay, customer impact).
7. Compare to the documented procedure, if given: steps skipped, added, reordered, done in another tool.
8. Compare across observed people or sites: shared patterns versus individual habits. A pattern needs at least two observations; single observations are marked `[SINGLE OBSERVATION]`.
9. Derive candidate needs and requirement hypotheses in problem form, each linked to the observation IDs that support it.
10. List open questions to verify with the observed people or their managers (why they do it, how often it happens outside the session).
11. If the goal continues, suggest `as-is-process` to model the flow, `value-stream-map` for waiting and rework, or `interview-notes-analysis` if follow-up interviews are held.

## Output format
```markdown
# Observation Summary: <process / team>
Sessions: <role codes, site, date, duration> · Observer: <role>

## Task Sequence (session <code>)
| # | Time | Step | Tool / system | Tag | Note |
|---|---|---|---|---|---|

## Workarounds and Shadow Artifacts
| # | Workaround | Need it covers | Seen in | Risk |

## Pains
| # | Pain | Evidence (obs. IDs, frequency, time) | Consequence |

## Documented vs Actual
- ...

## Candidate Needs
- N1: <problem-form need> (obs. 3, 7, 12)

## Interpretations [ASSUMPTION] and Open Questions
- ...
```

## Quality checklist
- [ ] Observations and interpretations are separated; every interpretation is labeled.
- [ ] No timings or frequencies were invented.
- [ ] Every workaround has the underlying need stated.
- [ ] Patterns rest on at least two observations or are marked `[SINGLE OBSERVATION]`.
- [ ] People and customer data are anonymized.
- [ ] Candidate needs are problem statements, not features, and cite observations.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Judging the workaround as bad practice. It usually exists because the system fails a real need; capture the need first.
- Generalizing from one expert user. Experts skip steps novices need; note experience level.
- Recording only the main flow. Interruptions, waits and rework are the most valuable findings.

## Example
Input: "10:02 A opens CRM, searches customer. 10:04 switches to own Excel, copies policy no. 'CRM search is too slow for old policies.' 10:09 phone rings, puts caller on hold."

Excerpt of output:
| # | Time | Step | Tool | Tag | Note |
|---|---|---|---|---|---|
| 1 | 10:02 | Search customer | CRM | Task step | |
| 2 | 10:04 | Look up policy no. in personal list | Excel | Workaround | Quote: "too slow for old policies" |

Candidate need N1: Agents need to find legacy policies within a call without a personal lookup list (obs. 2). Cause `[ASSUMPTION]`: CRM search performance on legacy data.
