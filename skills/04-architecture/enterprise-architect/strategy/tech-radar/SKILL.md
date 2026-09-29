---
description: Builds or updates a technology radar that classifies technologies into Adopt, Trial, Assess and Hold rings across quadrants (techniques, platforms, tools, languages and frameworks), with evidence-based rationale, movement since the last edition and guidance for teams. Use when standardizing a technology landscape, publishing a periodic radar, or deciding whether a team may use a new technology.
related: technology-selection, architecture-principles, technology-strategy, adr, dependency-upgrade
prompt: Update our tech radar with these proposals: move gRPC from Assess to Trial, put AngularJS on Hold, and add OpenTelemetry.
---

# Maintain a Technology Radar

## Purpose
Publish a concise, evidence-based view of which technologies the organization adopts, trials, assesses or avoids, so teams can choose within guardrails and the architecture function can steer the landscape without case-by-case approvals.

## When to use
- Preparing a periodic (e.g., semi-annual) radar edition.
- A team proposes a new language, framework, platform or technique.
- The landscape has sprawled and needs consolidation signals.
- End-of-life or security issues require moving items to Hold.

## When not to use
- A single, high-stakes technology decision for a project. Use `technology-selection`.
- Upgrading one dependency in a codebase. Use `dependency-upgrade`.
- Setting multi-year technology direction for leadership. Use `technology-strategy`.

## Inputs
Required:
- Proposed items or the current radar, with the quadrant and proposed ring for each.
- Evidence per item: who used it, where, outcome.

Optional:
- Architecture principles and standards.
- Usage inventory (repository scans, license data), incident or security history.
- Support and licensing status, skills availability.

If evidence is missing for an item, keep it in Assess or mark `[NEEDS EVIDENCE]`; do not promote on hype.

## Process
1. Fix the quadrants (Techniques; Platforms; Tools; Languages & Frameworks) and ring definitions: Adopt = default choice, proven in production here; Trial = use in a production project with a sponsor and exit plan; Assess = explore via spikes, not production; Hold = do not start new work, plan exit.
2. Collect proposals and existing items; deduplicate and normalize names and versions.
3. For each item, gather evidence: production usage count, outcomes, incidents, community/vendor health, license, security posture, skills in-house, fit with principles.
4. Apply ring entry criteria: Adopt requires at least two successful production uses here `[adjust to org policy]`; Trial requires a named team, success criteria and review date.
5. Record movement (new, in, out, unchanged) and a 2-4 sentence rationale per moved or new item.
6. Check overlaps: two Adopt items solving the same problem need a clear usage boundary or one moves to Hold.
7. For every Hold item, state the migration guidance and the owner of the exit.
8. Flag governance implications: what teams can do without approval (Adopt), what needs notification (Trial), what needs an ADR (Hold exceptions).
9. Produce the radar table and a short "what changed" summary for teams.

## Output format
```markdown
# Technology Radar – <edition/date>
Ring definitions: <Adopt / Trial / Assess / Hold as defined>

## What Changed
- <item>: <old ring> → <new ring> – <one-line reason>

## Radar
| Quadrant | Item | Ring | Movement | Rationale | Evidence | Owner | Review date |
|---|---|---|---|---|---|---|---|

## Hold Items – Exit Guidance
| Item | Replacement | Deadline or trigger | Owner |

## Overlaps Resolved
## Governance Notes and Open Questions
```

## Quality checklist
- [ ] Every ring placement cites local evidence, not industry popularity alone.
- [ ] Trial items have a team, success criteria and review date.
- [ ] Hold items have replacement guidance and an owner.
- [ ] No two Adopt items overlap without a stated boundary.
- [ ] Names, versions and license status are accurate or marked `[UNKNOWN]`.

## Common pitfalls
- Using the radar as a wish list. Items without local evidence stay in Assess.
- Never removing items. Stale entries erode trust; retire items that no longer need guidance.
- Hold without an exit path. Teams ignore Hold if there is no replacement or deadline.

## Example
Input: "Move gRPC to Trial (payments team used it internally), put AngularJS on Hold, add OpenTelemetry."

Excerpt of output:
| Quadrant | Item | Ring | Movement | Rationale |
|---|---|---|---|---|
| Languages & Frameworks | gRPC | Trial | In | One internal service-to-service use in payments; needs second team and schema governance before Adopt. |
| Languages & Frameworks | AngularJS | Hold | In | End of vendor support; migrate front ends on next major change `[owner TBD]`. |
| Techniques | OpenTelemetry instrumentation | Assess | New | No production use yet `[NEEDS EVIDENCE]`; run a spike with the platform team. |
