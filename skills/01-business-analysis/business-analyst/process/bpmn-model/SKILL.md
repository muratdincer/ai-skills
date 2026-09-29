---
name: bpmn-model
description: "Turns a process description into a BPMN 2.0 model: pools and lanes, events, tasks, gateways, message flows and data objects, delivered as a structured element list plus diagram code that renders or imports. Use when a process must be drawn formally, when a textual as-is or to-be process needs a diagram, or when someone asks for BPMN, a swimlane diagram or process diagram code."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: process
  title: "Describe a process in BPMN"
  related: "as-is-process, to-be-process, diagram-as-code, business-rules-catalog, use-case-spec"
  prompt: "Model this purchase approval process in BPMN: employee submits request, manager approves up to 10k, above that finance also approves, then procurement orders."
---

# Describe a Process in BPMN

## Purpose
Produce a BPMN 2.0 model that is semantically correct (right event, task and gateway types) and readable by business and IT alike, so the process can be validated, automated or used as a basis for requirements.

## When to use
- A textual as-is or to-be process needs a formal diagram.
- A workflow engine or process-automation initiative needs a clean starting model.
- Handoffs between departments or systems must be made visible (pools, lanes, message flows).

## When not to use
- The process itself has not been captured yet. Use `as-is-process` or `to-be-process` first.
- You need a system-to-system call sequence rather than a business process. Use `sequence-flow`.
- You need the lifecycle of a single object (order states). Use `state-model`.

## Inputs
Required:
- A process description: steps, actors, decisions (text, notes or an existing as-is/to-be document).

Optional, improves quality:
- Target level: descriptive (high-level), analytical (with exceptions) or executable.
- Preferred output notation: BPMN XML, Mermaid flowchart, PlantUML or a tool-neutral element list.
- Business rules behind decisions, SLAs and timers.

If the description is missing, ask for it. If the level is not given, default to analytical and state it.

## Process
1. Set scope: process name, trigger (start event), end states (one end event per distinct business outcome), level of detail.
2. Identify participants: a pool per organization or external party, a lane per role or internal system inside your organization. External parties stay black-box pools unless their steps matter.
3. List activities in verb-object form ("Approve request"). Type each: user, service, manual, send, receive, business rule or script task; use a call activity for reusable subprocesses.
4. Model decisions with the right gateway: exclusive (XOR) for one path, parallel (AND) for concurrent paths, inclusive (OR) for one-or-more, event-based for "whichever happens first". Label outgoing flows with conditions; add a default flow.
5. Close every split with a matching join of the same type, except XOR paths ending in separate end events.
6. Add events: timers (deadlines, reminders), messages between pools, errors and escalations as boundary events on the activity that can fail, compensation where a completed step must be undone.
7. Use sequence flow only inside a pool and message flow only between pools. Add data objects or data stores where a document or system record drives the flow.
8. Validate: no dead ends, no activity without incoming/outgoing flow, no implicit merges, every loop has an exit condition, every lane has work.
9. Produce the diagram code in the requested notation and an element table so the model can be reviewed without rendering.
10. List assumptions (gateway conditions, timers, roles you inferred) and open questions for the process owner.
11. If the user wants to continue, suggest `business-rules-catalog` for the gateway rules, `use-case-spec` for system-supported tasks or `to-be-process` if the model exposes improvement needs.

## Output format
```markdown
# BPMN Model: <process name>
Level: <descriptive / analytical / executable> · Trigger: <start event> · Outcomes: <end events>

## Participants
| Pool | Lanes | Notes |
|---|---|---|

## Elements
| ID | Type | Name | Lane | Incoming | Outgoing / condition |
|---|---|---|---|---|---|
| SE1 | Start event (message) | Request received | Employee | – | T1 |
| G1 | Exclusive gateway | Amount > limit? | Manager | T2 | yes: T3 / default: T4 |

## Diagram Code
<BPMN XML / Mermaid / PlantUML>

## Assumptions and Open Questions
- [ASSUMPTION] ...
- Q: ... — owner: ...
```

## Quality checklist
- [ ] Every gateway has labeled conditions and a default flow where applicable; splits and joins match.
- [ ] Message flows cross pools only; sequence flows never cross pool boundaries.
- [ ] Each end event represents a distinct, named business outcome.
- [ ] Exceptions and timers from the input are modeled as boundary or intermediate events, not hidden in task names.
- [ ] Inferred conditions, roles and timers are marked `[ASSUMPTION]`.
- [ ] The diagram code matches the element table one to one.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Using a gateway to make a decision. Gateways route; the decision is a task (often a business rule task) before the gateway.
- Modeling each internal department as a separate pool with message flows. Internal roles are lanes in one pool.
- Putting "if approved" into a task name instead of a gateway, which hides the branching from reviewers.
- Drawing systems and people in the same lane without distinction, which makes automation scope unclear.

## Example
Input: "Employee submits purchase request; manager approves up to 10k; above 10k finance also approves; procurement orders; rejection notifies employee."

Excerpt of output:
| ID | Type | Name | Lane | Outgoing / condition |
|---|---|---|---|---|
| T2 | User task | Approve request | Manager | G1 |
| G1 | Exclusive gateway | Decision? | Manager | rejected: T5 / approved: G2 |
| G2 | Exclusive gateway | Amount > 10k? | Manager | yes: T3 / default: T4 |
| T3 | User task | Approve as finance | Finance | G3 (rejected: T5 / default: T4) |
| B1 | Timer boundary on T2 | 3 working days `[ASSUMPTION]` | Manager | Escalate to deputy |
