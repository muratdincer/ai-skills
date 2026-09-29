---
name: interview-notes-analysis
description: "Analyzes raw interview notes or transcripts and extracts needs, pain points, business rules, exceptions, data and system mentions, conflicts and open questions, each traced to its source. Use after one or more elicitation interviews, when notes are messy, or when asked 'what did we learn from these interviews?'."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: elicitation
  title: "Analyze interview notes"
  related: "interview-question-set, business-rules-catalog, requirements-consistency-check, feedback-synthesis, open-questions-tracker"
  prompt: "Here are my notes from interviews with three accounts payable clerks. Extract the needs, pains, rules and any contradictions."
---

# Analyze Interview Notes

## Purpose
Convert interview notes into structured, traceable findings that can feed requirements, while keeping facts, opinions and interpretations separate.

## When to use
- After elicitation interviews, before writing requirements.
- Notes from several interviewees must be compared.
- A transcript is long and the analyst needs the substance quickly.

## When not to use
- The notes are from a meeting where decisions and actions matter most. Use `meeting-notes` or `action-item-extraction`.
- Large volumes of customer feedback must be themed by frequency. Use `feedback-synthesis`.

## Inputs
Required:
- Interview notes or transcript(s), with interviewee role for each.

Optional, improves quality:
- Interview objectives, initiative scope, previous findings, glossary.

If notes are missing, ask for them. If roles are missing, label sources as Interviewee A, B, C and continue.

## Process
1. Mask personal data that is not needed (names of third parties, customer details); refer to interviewees by role or code.
2. Split notes into statements; tag each as Fact (observed/stated practice), Opinion, Need, Pain, Rule, Exception, Workaround, Data/System mention, Metric, or Idea/solution suggestion.
3. Rewrite needs as problem-oriented statements ("need to know X before Y"), keeping solution ideas separate. Needs you infer from pains rather than heard stated are labeled `[ASSUMPTION]`.
4. Extract business rules in a normalized form (condition → action) with the stated source; mark rules heard from only one person as `[TO CONFIRM]`.
5. Quantify where the notes allow (frequency, volume, time); never invent numbers.
6. Compare interviewees: find agreements, contradictions and different practices for the same step.
7. Prioritize findings by frequency across interviewees and stated impact.
8. List open questions and follow-ups, each with who can answer.
9. If the goal continues, suggest `business-rules-catalog` for the extracted rules, `requirements-consistency-check` for the contradictions, or `open-questions-tracker` for the follow-ups.

## Output format
```markdown
# Interview Analysis: <initiative>
Sources: <codes and roles> · Date(s): <...>

## Key findings (top 5)
1. ... (sources: A, C)

## Needs
| ID | Need | Sources | Evidence (short quote) |
|---|---|---|---|

## Pains and workarounds
| ID | Pain | Workaround | Frequency / impact | Sources |

## Business rules and exceptions
| ID | Rule (condition → action) | Exception | Source | Status |

## Data and systems mentioned
- ...

## Conflicts
- A says ..., B says ... → question to resolve

## Solution ideas raised (not requirements)
- ...

## Open questions
- ...
```

## Quality checklist
- [ ] Every finding is traceable to at least one source.
- [ ] Facts, opinions and solution ideas are kept separate.
- [ ] Rules from a single source are marked `[TO CONFIRM]`.
- [ ] Contradictions are shown, not averaged away.
- [ ] Unneeded personal data is masked.
- [ ] No number appears that is not in the notes.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Promoting a strong opinion to a requirement. Count sources and look for evidence.
- Losing exceptions. The "except when..." sentences often drive most of the design effort.
- Summarizing each interview separately without cross-comparison. The value is in the differences.

## Example
Input: "A: 'I check each invoice against the PO manually, takes ages, except for utilities which we just pay.' B: 'We never pay without a PO match.'"

Excerpt of output:
| ID | Rule (condition → action) | Exception | Source | Status |
|---|---|---|---|---|
| BR-1 | Invoice received → match to PO before payment | Utility invoices paid without PO (A) | A, B | Conflict |

Conflicts: A describes a utility exception; B states no exceptions → confirm policy with AP manager.
