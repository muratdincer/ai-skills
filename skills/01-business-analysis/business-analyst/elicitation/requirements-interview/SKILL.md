---
description: Interviews the user one question at a time, adapting each question to the previous answer (diagnose, narrow, confirm), keeps a running specification visible, stops when a readiness checklist passes and ends with a structured requirements summary. Use when a need is vague ("we need a dashboard", "automate approvals"), when the user says "ask me questions", "help me specify this" or "interview me", or before writing stories or a PRD from thin input.
related: request-clarification-questions, requirements-gap-analysis, user-story, acceptance-criteria, edge-case-elicitation
prompt: Interview me until this is clear enough to build: we want suppliers to upload their invoices themselves instead of emailing them.
---

# Run an Interactive Requirements Interview

## Purpose
Turn a vague need into a specification a team can build and test, by asking the fewest, best-targeted questions one at a time instead of handing the user a long questionnaire.

## When to use
- The user has an idea or problem but not a specification, and is available to answer now.
- A request is too thin to write stories, acceptance criteria or a PRD.
- The user explicitly asks to be interviewed or questioned.

## When not to use
- The requester is not available and questions must be sent in one batch. Use `request-clarification-questions`.
- A written specification exists and needs to be checked for holes. Use `requirements-gap-analysis`.
- A stakeholder interview with third parties must be planned. Use `interview-question-set`.

## Inputs
Required:
- An initial statement of the need, even one sentence.

Optional, improves quality:
- Existing documents, screenshots, current process, constraints, deadline.
- Who the users are and who decides.

If the initial statement is missing, ask "What do you want to achieve, and for whom?" as the first question. Never ask for something the user already said.

## Process
1. Open with a one-line restatement of the need and a draft running spec (sections below, mostly `[UNKNOWN]`). Tell the user they can answer "skip" or "don't know" at any time.
2. Diagnose: ask about the underlying outcome and the trigger first (why now, what happens today, what goes wrong). Separate the literal ask from the underlying need.
3. Pick the next question by one rule: the unknown that blocks the most other decisions. Ask exactly ONE question per turn, offer 2-4 likely options when useful, and say briefly why you ask.
4. Narrow: after each answer, update the running spec, mark new facts as `[confirmed]` and your inferences as `[inferred]`, then drill into actors, main flow, data, rules, permissions, exceptions and non-functional needs in that priority.
5. Detect contradictions or vague words ("fast", "all", "usually") in answers and ask one follow-up to make them measurable before moving on.
6. Every 4-5 questions, show the compact running spec so the user can correct it.
7. Confirm: when the readiness checklist looks satisfied, play back the key decisions in 3-6 bullets and ask the user to confirm or correct. Treat "skip"/"don't know" answers as open questions with an owner, not as blockers, unless they block the readiness checklist.
8. Stop when the readiness checklist passes or the user asks to stop; do not ask about nice-to-have details.
9. Produce the final structured summary with must-haves, success criteria, hard negatives (what they explicitly do not want), open questions and assumptions.
10. Suggest the next skill: `user-story` or `acceptance-criteria` to turn the summary into backlog items, `edge-case-elicitation` to stress the flow, or `requirements-gap-analysis` for a formal completeness check.

Readiness checklist: goal and success measure; primary users/actors; trigger and main flow; key data in/out; business rules and permissions; main exceptions; NFRs that matter (volume, security, availability); scope out; decision owner.

## Output format
```markdown
<!-- During the interview, each turn: -->
**Q<n> (<topic>):** <one question> — *why:* <one line>
Options: a) ... b) ... c) other

<!-- Final summary -->
# Requirements Summary: <title>
**Need (literal ask):** ... **Underlying goal:** ...
**Success criteria:** <measurable>
## Actors and Permissions
## Main Flow
1. ...
## Data (in / out / retained)
## Business Rules
## Exceptions and Edge Cases
## Non-functional Requirements
## Out of Scope / Hard Negatives
## Assumptions ([inferred])
## Open Questions – <owner>
## Readiness: <passed items> / 9 – <what is still missing>
```

## Quality checklist
- [ ] Each turn asked exactly one question (or at most a batch of 5 on explicit request) and none repeated known information.
- [ ] Every item in the summary is traceable to an answer or labeled `[inferred]`/`[ASSUMPTION]`.
- [ ] Vague terms were converted into measurable statements or listed as open questions.
- [ ] The readiness checklist was evaluated explicitly and gaps are named.
- [ ] Hard negatives and out-of-scope items are captured, not only features.
- [ ] Personal data mentioned in answers is minimized or masked in the summary.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Dumping 20 questions at once. The user answers the easy ones and the critical ones stay open.
- Asking about UI details before the goal and flow are settled. Follow the priority order.
- Never stopping. Stop at readiness; the remaining details become open questions.
- Silently filling gaps with your own design. Propose options and let the user choose.

## Example
Input: "Suppliers should upload invoices themselves instead of emailing them."

Weak first turn: "Please answer: 1) users? 2) formats? 3) volume? 4) ERP? 5) approval? ... 15) SLA?"
Strong first turn:
**Q1 (goal):** What is the main problem with email today: manual data entry effort, lost invoices, late payments, or something else? — *why:* it decides what "done" means.
Options: a) entry effort b) lost/duplicate invoices c) payment delays d) other

Summary excerpt: Success criteria: manual keying reduced for uploaded invoices `[target TBD with AP lead]`. Hard negative: "suppliers must not see other suppliers' documents" `[confirmed]`.
