---
description: "Prepares a requirements sign-off package: the baseline being approved (documents, versions, requirement IDs), what changed since the last review, open issues and accepted risks, conditions, the approvers needed and how later changes will be controlled. Use when requirements are reviewed and ready to be baselined, when a sponsor asks 'what exactly am I signing?', or before design, build or a contract milestone starts."
related: "requirements-review-checklist, traceability-matrix, change-control, change-request-analysis, decision-log"
prompt: "Prepare the sign-off package for the claims portal FRD v1.3 so the business owner and IT lead can approve it this week."
---

# Prepare Requirements Sign-Off

## Purpose
Give approvers a short, unambiguous package that states exactly what is being baselined, what is still open and under which conditions approval is given. A good package makes the signature meaningful and gives change control a fixed reference point.

## When to use
- Requirements have passed review and design, build or procurement is about to start.
- A contract milestone, funding gate or vendor handover needs formally approved scope.
- A re-baseline is needed after approved change requests.

## When not to use
- The requirements have not been reviewed yet. Use `requirements-review-checklist` first.
- A single change to an approved baseline needs a decision. Use `change-request-analysis`.
- You need to define the change process itself. Use `change-control`.

## Inputs
Required:
- The documents or requirement set to be baselined, with versions or dates.
- Who must approve (names or roles).

Optional, improves quality:
- Review findings and their status, traceability matrix, previous baseline.
- Organization's approval policy (who signs what, delegation, electronic approval rules).
- Contract or governance clauses tied to the sign-off.

If the document set or the approvers are missing, ask for them. Do not ask for anything else up front; record gaps as open issues.

## Process
1. Define the baseline precisely: document titles, versions, dates and the requirement ID range. A baseline without versions is not signable; mark missing versions `[TBD]`.
2. If a previous baseline exists, summarize the delta: added, changed and removed requirements by ID, and which change requests caused them.
3. List open issues from reviews and elsewhere. Classify each: Blocking (sign-off must wait), Conditional (sign with a dated condition) or Deferred (explicitly moved to a later release, with owner).
4. Record accepted risks and assumptions the approvers are agreeing to live with; keep inferred items labeled `[ASSUMPTION]` so approvers see what the baseline rests on.
5. Check readiness evidence: review completed, traceability to goals exists, NFRs and acceptance criteria present, out-of-scope stated. Report each as Yes / Partial / No with a pointer; never tick what you cannot see.
6. Build the approver list: role, name, what they approve (business content, technical feasibility, compliance, budget), and whether their approval is mandatory or advisory. Flag missing roles such as data protection, security or operations when personal data or production changes are in scope.
7. State the change-control rule after sign-off: how changes are requested, who decides, and what triggers a re-baseline.
8. Give a recommendation: Ready to sign / Sign with conditions / Not ready, with the reason in one line.
9. Draft a short approval request message the requester can send, stating the deadline and what silence means (silence is never approval unless the governance says so).
10. If the user wants to continue, suggest `traceability-matrix` to anchor the baseline, `change-control` for the post-sign-off process or `decision-log` to record the approval.

## Output format
```markdown
# Requirements Sign-Off: <project / scope>
Baseline ID: <e.g. BL-2 or TBD> · Prepared: <date> · Recommendation: <Ready / With conditions / Not ready>

## Baseline Content
| Document | Version | Date | Requirement IDs |
|---|---|---|---|

## Changes Since Previous Baseline
| Req ID | Added / Changed / Removed | Source (CR, review) |
|---|---|---|

## Readiness Evidence
| Check | Status | Evidence |
|---|---|---|

## Open Issues
| # | Issue | Class (Blocking / Conditional / Deferred) | Owner | Due |
|---|---|---|---|---|

## Accepted Risks and Assumptions
- [ASSUMPTION] ...

## Approvals
| Role | Name | Approves | Mandatory | Decision | Date |
|---|---|---|---|---|---|

## Change Control After Sign-Off
<how, who, re-baseline trigger>

## Approval Request Message
<short message text>
```

## Quality checklist
- [ ] Every baselined document has a version or date, or is marked `[TBD]` and the recommendation reflects it.
- [ ] Blocking issues are consistent with the recommendation (no "Ready" with blocking items).
- [ ] Each conditional approval has an owner and a due date.
- [ ] Approver roles cover business, technical and, where relevant, compliance and data protection.
- [ ] No approval, name or date is invented; decisions stay blank until given.
- [ ] Inferred risks and assumptions are labeled so approvers know what they accept.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Asking approvers to sign "the requirements" without versions. Later disputes cannot be resolved without a fixed reference.
- Hiding open issues to get a signature faster. They return as change requests with worse timing; show them classified instead.
- Treating a reply like "looks fine" as sign-off. Record the explicit decision, the version it refers to and the date.

## Example
Input: "FRD v1.3 and NFR list v1.1 for the claims portal are reviewed. Two review findings are open: document upload size limit and SMS notification wording. Business owner Ayşe K. and IT lead need to sign."

Excerpt of output:
- Baseline: FRD v1.3 (FR-001–FR-086), NFR v1.1 (NFR-01–NFR-22).
- Open issues: upload size limit, Conditional, owner IT lead, due `[TBD]`; SMS wording, Deferred to content review, owner Business.
- Missing approver `[ASSUMPTION]`: the portal processes health data, so a data protection approver is likely required.
- Recommendation: Sign with conditions.
