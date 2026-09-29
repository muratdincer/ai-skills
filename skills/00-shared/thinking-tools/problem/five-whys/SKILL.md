---
name: five-whys
description: "Runs a disciplined 5 Whys analysis from a clearly stated symptom down to one or more verifiable root causes, with evidence for each link, a branch per contributing cause and countermeasures that address the cause, not the symptom. Use when an incident, defect, missed target or recurring problem needs a root cause, when someone asks 'why does this keep happening', or when a postmortem or lessons-learned needs causal depth."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: thinking-tools
  area: problem
  title: "Run a 5 Whys analysis"
  related: "problem-statement, fishbone-analysis, postmortem, debugging-hypotheses, lessons-learned"
  prompt: "Run a 5 Whys on this: the nightly customer export failed three times this month and finance got the report late each time."
---

# Run a 5 Whys Analysis

## Purpose
Trace a concrete symptom through a chain of evidenced cause-effect links to a root cause the organization can act on, so the countermeasure prevents recurrence instead of patching the latest occurrence.

## When to use
- An incident, defect or process failure has been contained and now needs a root cause.
- The same problem recurs and previous fixes did not hold.
- A postmortem, lessons-learned or corrective action report needs causal reasoning.

## When not to use
- The problem itself is vague or disputed. Use `problem-statement` first.
- Many interacting causes are suspected across people, process, tools and environment. Use `fishbone-analysis`, then run 5 Whys on the strongest branches.
- A live technical failure is being debugged. Use `debugging-hypotheses`.

## Inputs
Required:
- The symptom: what happened, where, when, and its impact.

Optional, improves quality:
- Timeline, logs, metrics, tickets, change history (personal data masked).
- Who was involved in detection and response (roles, not blame).
- Previous fixes and why they did not hold.

If the symptom is missing or only described as a solution ("we need monitoring"), ask what actually happened. Ask one question at a time about any link you cannot support.

## Process
1. Write the symptom as a factual, bounded statement: what, where, when, how often, impact. No causes in it.
2. Ask "Why did this happen?" and write the direct cause as a verifiable fact about a system or process, not a person ("the retry limit was 0", not "Ali forgot").
3. For each answer, record the evidence (log line, metric, config, document, interview) or mark it `[ASSUMPTION — verify by <check>]`.
4. Run the "therefore" test backwards: read the chain from bottom to top with "therefore"; every step must follow logically.
5. When an answer has several contributing causes, branch; analyze each branch separately instead of forcing one line.
6. Continue until you reach a cause that is within the organization's control and whose removal would prevent recurrence. Five is a heuristic: stop earlier or go further as the evidence allows.
7. Stop a branch at "human error", "lack of time" or "budget" only after asking why the system allowed that error or constraint; these are rarely root causes.
8. Distinguish the root cause from contributing factors and from why the problem was not detected earlier (detection gap).
9. Define countermeasures per root cause: immediate containment, permanent corrective action, and a detection improvement; each with an owner role and a verification method.
10. List the assumptions and evidence gaps that would change the conclusion.
11. If the user's goal continues, suggest `postmortem` to document the incident, `fishbone-analysis` if the causes remain broad, or `lessons-learned` to share the learning.

## Output format
```markdown
# 5 Whys: <symptom short title>

**Symptom:** <what, where, when, how often, impact>

| # | Why? | Answer (cause) | Evidence |
|---|---|---|---|
| 1 | Why did <symptom>? | ... | <source> / [ASSUMPTION] |
| 2 | Why did <answer 1>? | ... | ... |
| ... | | | |

**Branch B (if any):** <same table>

## Root Cause(s)
- <root cause> – within our control: yes/no

## Contributing Factors and Detection Gap
- ...

## Countermeasures
| Type | Action | Owner (role) | Verification |
|---|---|---|---|
| Containment | ... | ... | ... |
| Corrective | ... | ... | ... |
| Detection | ... | ... | ... |

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] The symptom statement contains no cause or solution.
- [ ] Every link has evidence or is marked `[ASSUMPTION]` with a verification step.
- [ ] The chain reads logically bottom-up with "therefore".
- [ ] No root cause is a person's name or "human error" without the system reason behind it.
- [ ] Each root cause has a corrective action and a way to verify it worked.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Following the first plausible answer. Check each link against evidence; an unverified chain produces confident but wrong fixes.
- Stopping at the symptom's owner ("the ops team missed the alert"). Ask why the alert was missable.
- Jumping outside your control ("the vendor is unreliable"). Go one step back to what your process assumed about the vendor.
- Countermeasures that only add a manual check. Prefer changes that remove the failure mode.

## Example
Input: "The nightly customer export failed three times this month; finance got the report late each time."

Excerpt of output:
| # | Why? | Answer | Evidence |
|---|---|---|---|
| 1 | Why was the report late? | The export job failed and nobody re-ran it before 08:00. | Scheduler history |
| 2 | Why did the job fail? | The source database was in its maintenance window when the job started. | DB maintenance calendar |
| 3 | Why did they overlap? | The maintenance window moved last month; the job schedule was not updated. | Change record `[ASSUMPTION — confirm change ID]` |
| 4 | Why was the job not updated? | Job dependencies on maintenance windows are not recorded anywhere. | [ASSUMPTION] |

Root cause: schedule dependencies are undocumented, so changes to one side do not trigger a review of the other. Detection gap: job failure alerts go to a shared mailbox nobody watches at night.
