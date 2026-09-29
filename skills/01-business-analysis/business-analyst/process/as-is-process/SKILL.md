---
description: "Documents the current (as-is) business process from interviews, observation notes, procedures or system logs: trigger, steps, actors, systems, inputs/outputs, decision points, timings, volumes, pain points and workarounds. Use when a process is to be improved, automated or replaced and the team first needs a shared, evidence-based picture of how work is actually done today."
related: "to-be-process, bpmn-model, value-stream-map, observation-notes, interview-notes-analysis"
prompt: "Document the as-is process for supplier invoice approval from these interview notes with AP and two department managers."
---

# Document the As-Is Process

## Purpose
Create a factual, shared description of how the process really runs today, including the informal parts, so improvement and automation decisions rest on evidence rather than on the official procedure.

## When to use
- Before designing a to-be process, automation or system replacement.
- When stakeholders describe the same process differently.
- When a process has known complaints (delays, errors, rework) but no clear picture of causes.

## When not to use
- The goal is to design the future process. Use `to-be-process`.
- You need formal BPMN notation. Use `bpmn-model` (after this skill, or together).
- You need to quantify waste and flow times end to end. Use `value-stream-map`.

## Inputs
Required:
- At least one source describing the current process: interview or workshop notes, observation notes, procedure documents, or system/ticket data.
- The process boundary: which trigger starts it and which outcome ends it. If missing, propose one and mark it `[ASSUMPTION]`.

Optional, improves quality:
- Volumes, cycle times, error or rework rates.
- Organization chart, system list, forms and templates in use.

## Process
1. Fix the boundary: name, trigger, end state(s), in/out of scope variants, process owner.
2. Separate sources: note which statements come from procedures (as-designed) and which from practitioners or data (as-performed). Where they differ, the as-performed version wins in the model, with the difference noted.
3. List actors (roles, not names) and systems, including spreadsheets, email and paper.
4. Sequence the steps as verb + object ("Check PO match"), each with actor, system, input, output and business rule applied.
5. Mark decision points with their conditions and each outgoing path; include rework loops and exceptions, not only the main path.
6. Capture handoffs between actors or systems; each handoff is a candidate for delay and error.
7. Record timings and volumes where known: processing time, waiting time, frequency, peak periods. Unknown values are `[UNKNOWN]`, never estimated as facts.
8. Log pain points and workarounds per step with evidence (who said it, data point), and controls (approvals, reconciliations, audit points).
9. Note personal or sensitive data handled in each step; mask real names or customer data from the source notes.
10. List discrepancies between sources and questions for validation; recommend a walkthrough with practitioners.
11. If the user wants to continue, suggest `to-be-process` to design the improvement, `bpmn-model` for a formal diagram or `value-stream-map` to quantify waste.

## Output format
```markdown
# As-Is Process: <name>
Owner: <role> · Trigger: <event> · End state(s): <outcomes> · Sources: <list> · Version/date

## Scope
In: ... · Out: ... · Variants: ...

## Actors and Systems
| Actor (role) | Responsibility | Systems/tools used |
|---|---|---|

## Process Steps
| # | Step (verb + object) | Actor | System | Input | Output | Rule/Decision | Time (proc/wait) | Pain point / workaround |
|---|---|---|---|---|---|---|---|---|

## Decision Points and Exceptions
- D1 <condition> → yes: step x, no: step y

## Metrics (known)
Volume: ... · Lead time: ... · Rework rate: ...

## Pain Points Summary
| # | Pain point | Steps | Evidence | Impact |
|---|---|---|---|---|

## Discrepancies and Open Questions
- ...
```

## Quality checklist
- [ ] The boundary (trigger and end state) is explicit.
- [ ] Every step has an actor and output; handoffs are visible.
- [ ] Exceptions and rework loops are documented, not just the happy path.
- [ ] Pain points cite evidence; no numbers are invented.
- [ ] Differences between procedure and practice are recorded.
- [ ] No improvement ideas are mixed into the as-is description (park them separately).
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Documenting the procedure manual instead of reality. Validate with people who do the work.
- Designing the solution while mapping. Keep an "improvement ideas" parking list outside the model.
- Using person names as actors. Use roles; names change and may be personal data.

## Example
Input: "AP clerk receives invoice by email, types it into ERP, emails the department manager for approval, chases by phone if no reply after a week."

Excerpt of output:
| # | Step | Actor | System | Output | Time (proc/wait) | Pain point / workaround |
|---|---|---|---|---|---|---|
| 1 | Receive invoice | AP clerk | Shared mailbox | Invoice PDF | [UNKNOWN] | Duplicates arrive via several addresses |
| 2 | Key invoice data | AP clerk | ERP | Draft invoice | [UNKNOWN] | Manual keying |
| 3 | Request approval | AP clerk | Email | Approval email | wait up to 1 week | Phone chasing (workaround) |
