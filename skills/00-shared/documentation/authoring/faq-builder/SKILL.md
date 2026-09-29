---
description: "Generates the questions a specific audience is likely to ask about a product, change, policy or project, and answers them strictly from provided source material, flagging gaps. Use when preparing an FAQ for a launch, migration, policy change, internal tool or customer help page, or when repeated questions keep arriving through support or chat channels."
related: "kb-article, announcement, org-change-communication, user-guide, ticket-response"
prompt: "Create an FAQ for employees about the move from our old VPN to the new zero-trust access client, based on this rollout plan."
---

# Build an FAQ

## Purpose
Anticipate and answer the questions an audience will actually have, grounded in source material, so that support load drops and people can self-serve, while unanswered questions are exposed to the owners before release.

## When to use
- A launch, migration, policy or organizational change will trigger predictable questions.
- Support, chat or email channels show recurring questions that deserve a canonical answer.
- A long document exists but readers need quick answers to specific concerns.

## When not to use
- One topic needs a full, step-by-step article. Use `kb-article` or `how-to-guide`.
- The need is to announce the change itself. Use `announcement` or `org-change-communication`.
- A single customer question must be answered. Use `ticket-response`.

## Inputs
Required:
- Source material: the plan, spec, policy, release notes or existing documentation.
- The audience (for example end users, employees, customers, partners, internal support).

Optional, improves quality:
- Real questions already received (tickets, chat logs, survey comments); mask personal data.
- Tone guidelines, publication channel and length limit.
- Contact or escalation channel for unanswered questions.

If source material or audience is missing, ask. Do not answer from general knowledge; missing answers become `[TBD]` for the owner.

## Process
1. Identify the audience's situation: what changes for them, what they must do, what they fear losing.
2. Harvest real questions first (tickets, logs, comments). Deduplicate and normalize wording to the user's language, not internal jargon.
3. Generate anticipated questions by lens: what/why, who is affected, when/deadlines, what must I do, what happens if I do nothing, cost/impact, data and privacy, exceptions, where to get help.
4. Prioritize by frequency and by consequence of misunderstanding; drop questions only the project team would ask.
5. Answer each question from the source only. Lead with the direct answer (yes/no/date/action) in the first sentence, then the necessary detail.
6. Where the source is silent or contradictory, write `[TBD — owner: <role>]` instead of an answer and add it to the gap list.
7. Group questions under 3-7 audience-oriented headings, ordered from most to least common.
8. Check consistency: dates, names and numbers must match across answers and the source.
9. Add links or references to the full documentation and a final "Still have questions?" entry with the support channel.

## Output format
```markdown
# FAQ: <topic>
Audience: <...> | Last updated: <date> | Source: <documents>

## <Group 1, e.g. What is changing>
**Q: <question in the user's words>**
A: <direct answer first>. <supporting detail>. See: <reference>.

## <Group 2 ...>
...

## Still have questions?
<channel, owner, hours>

---
## Gaps for Owners (not for publication)
| Question | Why unanswered | Owner | Needed by |
|---|---|---|---|
```

## Quality checklist
- [ ] Questions are phrased as the audience would ask them.
- [ ] Every answer starts with the direct answer.
- [ ] No answer contains information absent from the source; gaps are `[TBD]`.
- [ ] Dates, names and numbers are consistent across entries.
- [ ] The "do nothing" and "where to get help" questions are covered.
- [ ] The gap list is separated from publishable content.

## Common pitfalls
- Writing marketing questions nobody asks ("Why is the new tool so great?"). Use real and anticipated concerns.
- Burying the answer under context. First sentence answers; the rest supports.
- Letting the FAQ become the only documentation. Link to canonical docs and keep answers short.

## Example
Input: VPN to zero-trust access rollout plan; audience: all employees.

Excerpt of output:
- **Q: Do I have to do anything before the switch?** A: Yes. Install the new access client from the self-service portal before the cutover date `[TBD — owner: IT]`. The old VPN stops working after that date.
- **Q: Can I still reach internal systems from a personal laptop?** A: `[TBD — owner: Security]` The plan does not state the policy for unmanaged devices.
- Gap: unmanaged device policy — Security — needed before the announcement.
