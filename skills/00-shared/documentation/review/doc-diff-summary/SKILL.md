---
description: "Compares two versions of a document (contract, specification, policy, runbook, requirements) and produces a categorized summary of substantive changes, their impact on each stakeholder and the questions they raise, separating meaning changes from editorial ones. Use when a new version of a document arrives, before re-approval or sign-off, when a vendor or client sends a revised draft, or when someone asks what changed between two versions."
related: "change-request-analysis, impact-analysis, document-review, changelog-entry, requirements-sign-off"
prompt: "Here are v1.3 and v1.4 of the integration specification from the vendor. What changed and what does it mean for us?"
---

# Summarize Document Changes

## Purpose
Let reviewers understand what really changed between two versions and why it matters, without re-reading the whole document, and make sure no silent change in obligations, scope, numbers or dates slips through approval.

## When to use
- A revised specification, contract, policy or plan must be re-approved.
- A vendor, client or other team sends a new version and claims only minor edits.
- A change log or version history entry must be written for a document.

## When not to use
- The change is a proposed modification to agreed requirements that needs a decision. Use `change-request-analysis`.
- The need is to assess the wider effect of a change on systems and processes. Use `impact-analysis`.
- Only one version exists and needs quality feedback. Use `document-review`.

## Inputs
Required:
- Both versions (full text or clearly marked excerpts), labeled old and new.

Optional, improves quality:
- The reader's role and interests (for example our team as the integrating party).
- Author's change notes or cover letter to verify against the actual diff.
- Areas of special concern (price, SLA, data fields, deadlines).

If either version is missing, ask. If only a list of claimed changes is available, say that the analysis relies on the claim and cannot detect undeclared changes.

## Process
1. Align the versions by section; note sections added, removed, moved or renumbered.
2. Detect changes at clause level, not only paragraph level: numbers, dates, units, modal verbs (shall to should), conditions, exceptions, parties, definitions and references.
3. Classify each change: Substantive (changes meaning, obligation, scope, value, behavior), Clarification (same meaning, clearer), Editorial (formatting, typos, renumbering).
4. Pay special attention to definition changes and renumbered references; a changed definition silently changes every clause that uses it.
5. For each substantive change, state the old and new wording briefly, what it means in practice, and who is affected.
6. Rate impact per change (High/Medium/Low) with a one-line reason, from the reader's perspective.
7. Compare with the author's stated change notes; list undeclared substantive changes separately.
8. Formulate questions or negotiation points for changes that are unclear, unfavorable or unexplained.
9. Summarize in 3-5 bullets for decision makers at the top.

## Output format
```markdown
# Changes: <document> <old version> → <new version>
Reader perspective: <...> | Compared: <full text / excerpts>

## Summary
- <n> substantive, <n> clarifications, <n> editorial changes
- Most important: <...>
- Undeclared substantive changes: <count or none>

## Substantive Changes
| # | Location (new) | Old | New | Practical meaning | Affected | Impact |
|---|---|---|---|---|---|---|

## Clarifications
- <location>: <short description>

## Editorial
- <grouped description>

## Structural Changes
- Added / removed / moved sections: <...>

## Questions and Points to Raise
1. <question> — <change #> — <to whom>
```

## Quality checklist
- [ ] Every number, date, modal verb and condition change is captured.
- [ ] Definition changes are traced to the clauses they affect.
- [ ] Substantive and editorial changes are clearly separated.
- [ ] Undeclared substantive changes are highlighted.
- [ ] Impact is stated from the reader's perspective with a reason.
- [ ] Nothing is reported as changed without citing both wordings.

## Common pitfalls
- Trusting the author's cover note. Always compare the texts themselves.
- Missing "shall" becoming "should" or "within 5 business days" becoming "within 5 days". Small words, large impact.
- Reporting renumbering as dozens of changes. Collapse it into one structural note and map old to new numbers.

## Example
Input: Integration spec v1.3 and v1.4 from a vendor; reader: our integration team.

Excerpt of output:
- Summary: 4 substantive, 6 clarifications, editorial renumbering of §5-§7. Undeclared: 1.
- | 1 | §3.2 | Retries: "vendor shall retry 3 times" | "client should retry" | Retry responsibility moves to us | Integration team | High |
- | 2 | §6.1 (was §5.1) | Rate limit 100 req/s | 50 req/s | Batch sync may exceed limit at peak `[verify our peak rate]` | Ops | High |
- Question: Why was retry responsibility moved, and is it reflected in the SLA? — change 1 — vendor account manager.
