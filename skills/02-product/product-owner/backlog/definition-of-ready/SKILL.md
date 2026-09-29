---
name: definition-of-ready
description: "Creates or revises a team's Definition of Ready: the entry criteria a work item must meet before the team commits to or starts it, tailored to item types, with how each criterion is checked and when exceptions are allowed. Use when a team keeps starting unclear work, planning stalls on missing information, or someone asks for a DoR, readiness criteria or an entry checklist."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-owner
  area: backlog
  title: "Define Definition of Ready"
  related: "definition-of-done, backlog-refinement, invest-check, acceptance-criteria, working-agreement"
  prompt: "Write a Definition of Ready for our team; we build a B2B web portal and keep getting blocked by missing API contracts and UX designs."
---

# Define Definition of Ready

## Purpose
Give the team a short, agreed set of entry criteria that prevents unclear or blocked work from being started, without turning readiness into a bureaucratic stage gate.

## When to use
- Work items are frequently blocked or reworked because information was missing at start.
- A new team is forming its working agreements.
- Refinement or planning sessions repeatedly stall on the same missing inputs.
- An existing DoR is ignored or has grown too long.

## When not to use
- Defining when work is complete. Use `definition-of-done`.
- Checking a single story's quality. Use `invest-check`.
- Agreeing broader team norms. Use `working-agreement`.

## Inputs
Required:
- Team context: what the team builds and the recurring causes of blocked or unclear work. If missing, ask for the top 2-3 problems; a DoR without a problem to solve becomes generic.

Optional, improves quality:
- Existing DoR, DoD, work item types (story, bug, spike, technical item).
- Dependencies on other teams (UX, API providers, data, security).
- Regulatory or compliance needs (e.g. KVKK/GDPR data classification).

## Process
1. List the observed failure modes (blocked by design, missing API contract, unclear acceptance, no test data) and map each to one candidate criterion.
2. Start from a minimal core that applies to all items: value stated, acceptance criteria testable, small enough for one iteration/sprint or a few days of flow, dependencies identified, no blocking open question.
3. Add type-specific criteria only where failures occurred (e.g. story: UX available if UI changes; integration: contract agreed; bug: reproducible steps and environment; spike: question and timebox).
4. Phrase each criterion as a yes/no check and state who verifies it and when (refinement, before planning, at pull).
5. Keep the core list to 5-8 criteria; move nice-to-haves to guidance.
6. Define the exception rule: when a not-ready item may still be pulled (e.g. urgent fix, explicit risk accepted by product owner) and how it is labeled.
7. Define how the DoR is reviewed (e.g. at retrospectives, every few iterations) and a signal that it is too strict (items waiting long only for readiness).
8. Write the DoR as a one-page artifact the team can paste into its board or wiki.
9. If the user's goal continues, suggest `definition-of-done` for the matching exit criteria or `invest-check` to test current items against the new DoR.

## Output format
```markdown
# Definition of Ready – <team>
Version: <n> · Agreed on: <date or [TBD]> · Review cadence: <cadence>

## Core Criteria (all items)
| # | Criterion (yes/no) | Checked by | When |
|---|---|---|---|
| 1 | Value and target user are stated | Product owner | Refinement |

## Type-Specific Criteria
- Story with UI change: <criterion>
- Integration/API: <criterion>
- Bug: <criterion>
- Spike: <criterion>

## Exceptions
<when a not-ready item may start, who accepts the risk, how it is labeled>

## Problems This DoR Addresses
- <failure mode> → criterion <#>

## Review
<when and how the DoR is revisited; signal that it is too strict>
```

## Quality checklist
- [ ] Every criterion is a verifiable yes/no statement.
- [ ] Each criterion traces to a real problem or a clearly justified baseline.
- [ ] The core list has at most 8 criteria.
- [ ] An exception rule exists so the DoR does not block urgent work.
- [ ] No criterion duplicates the Definition of Done.
- [ ] Dates and agreement status are marked `[TBD]` until the team confirms them.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Turning the DoR into a waterfall gate ("full specification signed off"). Readiness means enough to start safely, not everything known.
- Requiring an estimate as a criterion when the team does not estimate. Use "small enough" instead.
- Writing the DoR for the team instead of with it. Present it as a draft for the team to agree.

## Example
Input: "B2B portal team, blocked by missing API contracts and late UX designs."

Excerpt of output:
| 4 | For items consuming another team's API: contract (endpoints, payloads, error codes) is agreed and versioned | Developer + provider team | Before planning |
| 5 | For items changing UI: design is available and reviewed with a developer | Product owner + designer | Refinement |
- Exceptions: A not-ready item may start only if the product owner records the accepted risk on the item and labels it "started-not-ready".
