---
description: "Generates the clarification questions to ask a requester about a new request, grouped by topic (business, users, data, integration, NFR, legal, operations, reporting, migration) and prioritized by how much each answer blocks analysis. Use when a request is vague, before a clarification meeting or email, or when someone asks 'what should I ask the business about this?'."
related: "request-intake-document, request-completeness-check, interview-question-set, open-questions-tracker"
prompt: "What should I ask the requester about this: 'We need customers to be able to update their address themselves in the mobile app.'"
---

# Generate Request Clarification Questions

## Purpose
Produce a short, prioritized set of questions that removes the ambiguity blocking analysis and estimation, so one clarification round is enough instead of five.

## When to use
- A new request is vague, solution-first or missing obvious facts.
- Before a clarification meeting, email or chat with the requester.
- An intake document has many `[UNKNOWN]` fields that need owners.

## When not to use
- You need a structured gap list with severity, not questions. Use `request-completeness-check`.
- You are preparing a full elicitation interview with a stakeholder group. Use `interview-question-set`.

## Inputs
Required:
- The request text or intake document.

Optional, improves quality:
- Who will receive the questions (requester, sponsor, IT, compliance) and the channel (meeting, email).
- Known context: affected systems, domain, regulatory environment, deadline.
- Answers already given in previous rounds.

If the request text is missing, ask for it. Never ask what the request already answers.

## Process
1. Read the request and list what is known (facts), what is implied (interpretation, labeled `[ASSUMPTION]`) and what is absent. Note the sender's role, decision power and stake; a sponsor's ask and an end user's ask need different questions.
2. Separate the literal ask from the underlying need (job to be done). If they may differ, the first question confirms the need. Check whether must-haves, success criteria and hard negatives (what they explicitly do not want) are known; each unknown one becomes a question.
3. Walk through every category in the question bank below. Keep only questions whose answer is not in the request and would change scope, design, estimate or risk.
4. Rewrite each kept question to be specific to this request (name the screen, entity, user group, date). Remove generic wording.
5. Prefer closed or option-based questions where possible ("A or B?", "Is it X, Y or something else?") to speed up answers.
6. Tag each question with priority: P1 blocks analysis/estimation, P2 affects design, P3 can wait until detailed analysis.
7. Add why it matters (one short clause) and the likely answer owner.
8. Limit the first round to about 10-15 questions; move the rest to a "later" list.
9. Order for the channel: meeting = conversational flow from goal to detail; email = numbered, P1 first, answerable in writing.
10. When the answers arrive, suggest `request-intake-document` to record them, `request-completeness-check` to confirm readiness, or `open-questions-tracker` for what stays open.

Question bank (adapt, never paste blindly):
- **Business and goal:** What problem happens today, to whom and how often? What is the underlying need behind the proposed solution? What triggers the date, and what happens if it slips? How will we know it worked (metric, baseline, target)? What happens if we do nothing? Who decides and who pays?
- **Scope and expectations:** What must the result contain on day one? What explicitly must not change or must not be built? Which related initiatives or earlier requests overlap? Is a partial or phased delivery acceptable?
- **Users and roles:** Which user groups, how many, internal or external? Who must not see or do this? Channels and devices? Accessibility needs? Which permissions or segregation-of-duties rules apply?
- **Process and rules:** Which process step changes? Business rules, approvals, exceptions? What happens on the unhappy path (rejection, timeout, invalid input, duplicate)? Which validations apply, and who fixes errors? What manual workaround exists today?
- **Data:** Which entities and fields? Source of truth? Volumes and growth? Quality issues? Personal or sensitive data? Retention?
- **Integration:** Which systems send or receive data? Real-time or batch? Who owns the interface? Error and retry expectations?
- **Non-functional:** Response time, peak load and when it occurs, availability window, recovery expectations, security level, audit trail (who, what, when), localization, browser/device support?
- **Legal and compliance:** KVKK/GDPR, sector regulation, contractual obligations, consent, audit requirements?
- **Operations and support:** Who supports it after go-live? Monitoring, alerts, manual fallback, training, runbooks?
- **Reporting:** Which KPIs or reports must reflect this change? Who consumes them, how often? Must history stay comparable before and after?
- **Migration and transition:** Existing data to migrate or clean? Cut-over constraints and freeze periods, parallel run, backward compatibility, rollback expectation, what gets decommissioned?

## Output format
```markdown
# Clarification Questions: <request title>
Audience: <requester / sponsor / ...> · Channel: <meeting / email>

## What we understood
- Literal ask: <in their words>
- Underlying need [ASSUMPTION]: <to confirm or correct>
- Known must-haves / success criteria / hard negatives: <or [UNKNOWN]>

## Priority 1 – blocks analysis
| # | Topic | Question | Why it matters | Owner |
|---|---|---|---|---|
| 1 | Business | ... | ... | ... |

## Priority 2 – affects design
| # | Topic | Question | Why it matters | Owner |

## Later (detailed analysis)
- ...

## Assumptions we will use if unanswered
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] No question is already answered by the request.
- [ ] Every question is specific to this request, not generic.
- [ ] Each question asks one thing only.
- [ ] Questions are neutral and do not push a solution.
- [ ] P1 questions are 10 or fewer and each has an owner.
- [ ] Data, legal and NFR topics were considered even if the request is "just UI".
- [ ] The literal ask and the underlying need are separated, and the questions cover must-haves, success criteria and hard negatives.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Dumping the whole bank on the requester. Filter hard; unanswered long lists damage trust.
- Asking "what are your requirements?" Ask about the problem, the situation and concrete examples instead.
- Forgetting non-requesters: compliance, operations and data owners often hold the blocking answers.

## Example
Input: "Customers should update their address themselves in the mobile app."

Excerpt of output:
| # | Topic | Question | Why it matters | Owner |
|---|---|---|---|---|
| 1 | Business | What problem does this solve today: call-center load, returned mail, or data quality? Is there a baseline number? | Defines success metric | Requester |
| 2 | Legal | Does an address change require identity re-verification or trigger any regulatory notification? | May add security steps | Compliance |
| 3 | Integration | Which systems hold the address (CRM, billing, shipping), and which is the master? | Drives integration scope | IT / data owner |
