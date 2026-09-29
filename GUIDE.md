# Skill Usage Guide

Every skill with when to use it and a ready-to-use example request. Type the example (or your own version) in any AI tool where the skill is installed, or paste the skill file first and then the request. See [USAGE.md](USAGE.md) for tool setup and [METHODOLOGIES.md](METHODOLOGIES.md) for which skills fit which phase.

## Contents

- [Shared (Cross-Role)](#shared-cross-role)
  - [Meetings](#meetings)
  - [Communication](#communication)
  - [Documentation](#documentation)
  - [Problem Solving & Decision Tools](#problem-solving--decision-tools)
  - [Knowledge Management](#knowledge-management)
- [Business Analysis](#business-analysis)
  - [Business Analyst](#business-analyst)
  - [System Analyst](#system-analyst)
- [Product Management](#product-management)
  - [Product Manager](#product-manager)
  - [Product Owner](#product-owner)
- [Project & Delivery Management](#project--delivery-management)
  - [Project Manager](#project-manager)
  - [Scrum Master / Agile Coach](#scrum-master--agile-coach)
  - [Program Manager / PMO](#program-manager--pmo)
- [Architecture](#architecture)
  - [Enterprise Architect](#enterprise-architect)
  - [Solution Architect](#solution-architect)
  - [Software Architect](#software-architect)
- [Software Engineering](#software-engineering)
  - [Developer (Backend/Frontend/Mobile)](#developer-backendfrontendmobile)
  - [Tech Lead](#tech-lead)
- [Quality Assurance & Testing](#quality-assurance--testing)
  - [QA Analyst / Test Engineer](#qa-analyst--test-engineer)
  - [Test Automation Engineer](#test-automation-engineer)
  - [Performance Test Engineer](#performance-test-engineer)
- [DevOps, SRE & Platform](#devops-sre--platform)
  - [DevOps / Platform Engineer](#devops--platform-engineer)
  - [Release Manager](#release-manager)
  - [Site Reliability Engineer](#site-reliability-engineer)
- [Data & AI](#data--ai)
  - [Data Architect](#data-architect)
  - [Data Engineer](#data-engineer)
  - [Database Administrator](#database-administrator)
  - [Data / BI Analyst](#data--bi-analyst)
  - [Data Scientist / ML & AI Engineer](#data-scientist--ml--ai-engineer)
- [Security & Compliance](#security--compliance)
  - [Security Architect / AppSec Engineer](#security-architect--appsec-engineer)
  - [GRC / Compliance](#grc--compliance)
- [UX / UI Design](#ux--ui-design)
  - [UX Researcher](#ux-researcher)
  - [UX / UI Designer](#ux--ui-designer)
  - [UX Writer / Content Designer](#ux-writer--content-designer)
- [Support & IT Operations](#support--it-operations)
  - [Support Engineer (L1-L3)](#support-engineer-l1-l3)
  - [IT Service Management](#it-service-management)
- [Technical Writing](#technical-writing)
  - [Technical Writer](#technical-writer)
- [Engineering Management & Leadership](#engineering-management--leadership)
  - [Engineering Manager](#engineering-manager)
  - [CTO / VP / Director](#cto--vp--director)
- [Presales & Consulting](#presales--consulting)
  - [Presales / Solution Consultant](#presales--solution-consultant)

## Shared (Cross-Role)

### Meetings

#### Before the Meeting

**Prepare a meeting agenda** · `meeting-agenda`

- When: Builds a timeboxed meeting agenda with a clear objective, expected outcomes, agenda items with owners and durations, and required pre-reads. Use when planning any meeting, workshop or recurring session and you need a structured agenda that drives decisions instead of discussion.
- Try: _"Prepare a 60-minute agenda for a meeting to decide the Q3 release scope with product, engineering and QA leads."_
- Related: `meeting-invite`, `meeting-necessity-check`, `facilitation-guide`
- File: [skills/00-shared/meetings/before/meeting-agenda/SKILL.md](skills/00-shared/meetings/before/meeting-agenda/SKILL.md)

**Write a meeting invitation** · `meeting-invite`

- When: Drafts a clear meeting invitation stating purpose, expected outcome, agenda summary, attendees with the reason each is invited, and required preparation. Use when sending a calendar invite or meeting request email so recipients can decide to attend and come prepared.
- Try: _"Write a meeting invite for a 45-minute architecture review of the payment service redesign next Tuesday."_
- Related: `meeting-agenda`, `meeting-necessity-check`
- File: [skills/00-shared/meetings/before/meeting-invite/SKILL.md](skills/00-shared/meetings/before/meeting-invite/SKILL.md)

**Decide if a meeting is needed** · `meeting-necessity-check`

- When: Assesses whether a planned meeting is actually needed by testing its goal against async alternatives, and recommends meet, shorten, go async or cancel with a ready-to-use alternative. Use when someone plans a new or recurring meeting, asks "do we need a meeting for this?", or wants to cut meeting load.
- Try: _"I want to set up a weekly 1-hour sync with 9 people to share progress on the data migration. Do we really need it?"_
- Related: `meeting-agenda`, `meeting-invite`, `stakeholder-email`, `status-update`, `working-agreement`
- File: [skills/00-shared/meetings/before/meeting-necessity-check/SKILL.md](skills/00-shared/meetings/before/meeting-necessity-check/SKILL.md)

#### During the Meeting

**Take structured meeting notes** · `meeting-notes`

- When: Turn raw notes or transcript into topic-based structured notes
- File: [skills/00-shared/meetings/during/meeting-notes/SKILL.md](skills/00-shared/meetings/during/meeting-notes/SKILL.md)

**Clean up a meeting transcript** · `transcript-cleanup`

- When: Remove filler, fix speakers, keep meaning intact
- File: [skills/00-shared/meetings/during/transcript-cleanup/SKILL.md](skills/00-shared/meetings/during/transcript-cleanup/SKILL.md)

**Facilitate a meeting** · `facilitation-guide`

- When: Give a facilitator script with timeboxes, prompts and conflict handling
- File: [skills/00-shared/meetings/during/facilitation-guide/SKILL.md](skills/00-shared/meetings/during/facilitation-guide/SKILL.md)

#### After the Meeting

**Summarize a meeting** · `meeting-summary`

- When: Produce a short executive summary of outcomes, decisions and open points
- File: [skills/00-shared/meetings/after/meeting-summary/SKILL.md](skills/00-shared/meetings/after/meeting-summary/SKILL.md)

**Write formal meeting minutes** · `meeting-minutes`

- When: Produce formal minutes with attendance, agenda items and resolutions
- File: [skills/00-shared/meetings/after/meeting-minutes/SKILL.md](skills/00-shared/meetings/after/meeting-minutes/SKILL.md)

**Extract action items** · `action-item-extraction`

- When: Find every commitment and assign owner, due date and status
- File: [skills/00-shared/meetings/after/action-item-extraction/SKILL.md](skills/00-shared/meetings/after/action-item-extraction/SKILL.md)

**Record decisions** · `decision-log`

- When: Capture decisions with context, alternatives and rationale
- File: [skills/00-shared/meetings/after/decision-log/SKILL.md](skills/00-shared/meetings/after/decision-log/SKILL.md)

**Write a meeting follow-up message** · `meeting-follow-up`

- When: Send a recap with decisions, actions and next meeting
- File: [skills/00-shared/meetings/after/meeting-follow-up/SKILL.md](skills/00-shared/meetings/after/meeting-follow-up/SKILL.md)

**Track open questions** · `open-questions-tracker`

- When: List unresolved questions with owner and needed-by date
- File: [skills/00-shared/meetings/after/open-questions-tracker/SKILL.md](skills/00-shared/meetings/after/open-questions-tracker/SKILL.md)

### Communication

#### Written Communication

**Write a status update** · `status-update`

- When: Summarize progress, risks and next steps using RAG status
- File: [skills/00-shared/communication/written/status-update/SKILL.md](skills/00-shared/communication/written/status-update/SKILL.md)

**Write an executive summary** · `executive-summary`

- When: Condense any content to a one-page decision-oriented summary
- File: [skills/00-shared/communication/written/executive-summary/SKILL.md](skills/00-shared/communication/written/executive-summary/SKILL.md)

**Write a stakeholder email** · `stakeholder-email`

- When: Write a purpose-first email adapted to audience and tone
- File: [skills/00-shared/communication/written/stakeholder-email/SKILL.md](skills/00-shared/communication/written/stakeholder-email/SKILL.md)

**Write an escalation** · `escalation-message`

- When: Escalate with facts, impact, options and a clear ask
- File: [skills/00-shared/communication/written/escalation-message/SKILL.md](skills/00-shared/communication/written/escalation-message/SKILL.md)

**Write an announcement** · `announcement`

- When: Announce a change, release or decision with what/why/impact/when
- File: [skills/00-shared/communication/written/announcement/SKILL.md](skills/00-shared/communication/written/announcement/SKILL.md)

**Rewrite for tone** · `tone-rewrite`

- When: Rewrite a message to be clearer, softer, firmer or more formal
- File: [skills/00-shared/communication/written/tone-rewrite/SKILL.md](skills/00-shared/communication/written/tone-rewrite/SKILL.md)

**Deliver bad news** · `bad-news-delivery`

- When: Communicate delays, cancellations or failures transparently
- File: [skills/00-shared/communication/written/bad-news-delivery/SKILL.md](skills/00-shared/communication/written/bad-news-delivery/SKILL.md)

#### Presentation & Verbal

**Outline a presentation** · `presentation-outline`

- When: Build a storyline and slide-by-slide outline for an audience
- File: [skills/00-shared/communication/verbal/presentation-outline/SKILL.md](skills/00-shared/communication/verbal/presentation-outline/SKILL.md)

**Write a demo script** · `demo-script`

- When: Script a product or feature demo with flow, talking points and fallbacks
- File: [skills/00-shared/communication/verbal/demo-script/SKILL.md](skills/00-shared/communication/verbal/demo-script/SKILL.md)

**Write an elevator pitch** · `elevator-pitch`

- When: Explain an idea in 30-60 seconds for a given audience
- File: [skills/00-shared/communication/verbal/elevator-pitch/SKILL.md](skills/00-shared/communication/verbal/elevator-pitch/SKILL.md)

#### Interpersonal

**Give feedback (SBI)** · `feedback-sbi`

- When: Frame feedback as Situation-Behavior-Impact, constructive and specific
- File: [skills/00-shared/communication/interpersonal/feedback-sbi/SKILL.md](skills/00-shared/communication/interpersonal/feedback-sbi/SKILL.md)

**Resolve a conflict** · `conflict-resolution`

- When: Map positions and interests and propose a mediated resolution
- File: [skills/00-shared/communication/interpersonal/conflict-resolution/SKILL.md](skills/00-shared/communication/interpersonal/conflict-resolution/SKILL.md)

**Prepare for a negotiation** · `negotiation-prep`

- When: Define BATNA, interests, concessions and opening position
- File: [skills/00-shared/communication/interpersonal/negotiation-prep/SKILL.md](skills/00-shared/communication/interpersonal/negotiation-prep/SKILL.md)

### Documentation

#### Authoring

**Outline a document** · `document-outline`

- When: Propose a structure for any document type from its purpose
- File: [skills/00-shared/documentation/authoring/document-outline/SKILL.md](skills/00-shared/documentation/authoring/document-outline/SKILL.md)

**Build a glossary** · `glossary-builder`

- When: Extract domain terms and write unambiguous definitions
- File: [skills/00-shared/documentation/authoring/glossary-builder/SKILL.md](skills/00-shared/documentation/authoring/glossary-builder/SKILL.md)

**Build an FAQ** · `faq-builder`

- When: Generate likely questions and answers from source material
- File: [skills/00-shared/documentation/authoring/faq-builder/SKILL.md](skills/00-shared/documentation/authoring/faq-builder/SKILL.md)

**Produce a diagram as code** · `diagram-as-code`

- When: Turn a description into Mermaid/PlantUML diagrams
- File: [skills/00-shared/documentation/authoring/diagram-as-code/SKILL.md](skills/00-shared/documentation/authoring/diagram-as-code/SKILL.md)

**Translate technical content** · `technical-translation`

- When: Translate technical text EN<->TR preserving terminology
- File: [skills/00-shared/documentation/authoring/technical-translation/SKILL.md](skills/00-shared/documentation/authoring/technical-translation/SKILL.md)

#### Review

**Review a document** · `document-review`

- When: Review for clarity, completeness, consistency and audience fit
- File: [skills/00-shared/documentation/review/document-review/SKILL.md](skills/00-shared/documentation/review/document-review/SKILL.md)

**Simplify a document** · `document-simplify`

- When: Cut length and jargon without losing meaning
- File: [skills/00-shared/documentation/review/document-simplify/SKILL.md](skills/00-shared/documentation/review/document-simplify/SKILL.md)

**Summarize document changes** · `doc-diff-summary`

- When: Compare two versions and explain what changed and why it matters
- File: [skills/00-shared/documentation/review/doc-diff-summary/SKILL.md](skills/00-shared/documentation/review/doc-diff-summary/SKILL.md)

### Problem Solving & Decision Tools

#### Problem Framing

**Write a problem statement** · `problem-statement`

- When: Frame who has what problem, when, with what impact
- File: [skills/00-shared/thinking-tools/problem/problem-statement/SKILL.md](skills/00-shared/thinking-tools/problem/problem-statement/SKILL.md)

**Run a 5 Whys analysis** · `five-whys`

- When: Drill down from a symptom to a root cause
- File: [skills/00-shared/thinking-tools/problem/five-whys/SKILL.md](skills/00-shared/thinking-tools/problem/five-whys/SKILL.md)

**Run a fishbone analysis** · `fishbone-analysis`

- When: Categorize possible causes (Ishikawa)
- File: [skills/00-shared/thinking-tools/problem/fishbone-analysis/SKILL.md](skills/00-shared/thinking-tools/problem/fishbone-analysis/SKILL.md)

**Map assumptions** · `assumption-mapping`

- When: List assumptions and rank them by risk and evidence
- File: [skills/00-shared/thinking-tools/problem/assumption-mapping/SKILL.md](skills/00-shared/thinking-tools/problem/assumption-mapping/SKILL.md)

#### Decision Making

**Build a weighted decision matrix** · `decision-matrix`

- When: Score options against weighted criteria
- File: [skills/00-shared/thinking-tools/decision/decision-matrix/SKILL.md](skills/00-shared/thinking-tools/decision/decision-matrix/SKILL.md)

**List pros and cons** · `pros-cons`

- When: Balanced pros/cons with a recommendation
- File: [skills/00-shared/thinking-tools/decision/pros-cons/SKILL.md](skills/00-shared/thinking-tools/decision/pros-cons/SKILL.md)

**Run a SWOT analysis** · `swot-analysis`

- When: Strengths, weaknesses, opportunities, threats with actions
- File: [skills/00-shared/thinking-tools/decision/swot-analysis/SKILL.md](skills/00-shared/thinking-tools/decision/swot-analysis/SKILL.md)

**Analyze trade-offs** · `trade-off-analysis`

- When: Make explicit what is gained and lost per option
- File: [skills/00-shared/thinking-tools/decision/trade-off-analysis/SKILL.md](skills/00-shared/thinking-tools/decision/trade-off-analysis/SKILL.md)

**Run a pre-mortem** · `pre-mortem`

- When: Imagine failure and list how it happened to find risks early
- File: [skills/00-shared/thinking-tools/decision/pre-mortem/SKILL.md](skills/00-shared/thinking-tools/decision/pre-mortem/SKILL.md)

### Knowledge Management

#### Capture & Transfer

**Capture lessons learned** · `lessons-learned`

- When: Record what worked, what didn't and actions to keep/change
- File: [skills/00-shared/knowledge/capture/lessons-learned/SKILL.md](skills/00-shared/knowledge/capture/lessons-learned/SKILL.md)

**Write a handover document** · `handover-document`

- When: Transfer ownership: context, state, contacts, risks, open items
- File: [skills/00-shared/knowledge/capture/handover-document/SKILL.md](skills/00-shared/knowledge/capture/handover-document/SKILL.md)

**Write a knowledge base article** · `kb-article`

- When: Write a searchable how-to or explanation article
- File: [skills/00-shared/knowledge/capture/kb-article/SKILL.md](skills/00-shared/knowledge/capture/kb-article/SKILL.md)

**Write an onboarding guide** · `onboarding-guide`

- When: Guide a newcomer through context, tools, people and first tasks
- File: [skills/00-shared/knowledge/capture/onboarding-guide/SKILL.md](skills/00-shared/knowledge/capture/onboarding-guide/SKILL.md)

## Business Analysis

### Business Analyst

#### Request Intake

**Create a request intake document** · `request-intake-document`

- When: Turns a raw business request (email, chat message, meeting note, ticket) into a structured request intake document with goal, scope, value, stakeholders, constraints and open questions. Use when someone brings a new demand, idea or change request and it must be captured before analysis, estimation or prioritization.
- Try: _"Create an intake document for this request: Sales wants an Excel export on the customer list screen by month end for the audit."_
- Related: `request-clarification-questions`, `request-completeness-check`, `request-triage`, `stakeholder-identification`
- File: [skills/01-business-analysis/business-analyst/intake/request-intake-document/SKILL.md](skills/01-business-analysis/business-analyst/intake/request-intake-document/SKILL.md)

**Generate request clarification questions** · `request-clarification-questions`

- When: Generates the clarification questions to ask a requester about a new request, grouped by topic (business, users, data, integration, NFR, legal, operations, reporting, migration) and prioritized by how much each answer blocks analysis. Use when a request is vague, before a clarification meeting or email, or when someone asks 'what should I ask the business about this?'.
- Try: _"What should I ask the requester about this: 'We need customers to be able to update their address themselves in the mobile app.'"_
- Related: `request-intake-document`, `request-completeness-check`, `interview-question-set`, `open-questions-tracker`
- File: [skills/01-business-analysis/business-analyst/intake/request-clarification-questions/SKILL.md](skills/01-business-analysis/business-analyst/intake/request-clarification-questions/SKILL.md)

**Triage incoming requests** · `request-triage`

- When: Classify requests by type, urgency, value and route them
- File: [skills/01-business-analysis/business-analyst/intake/request-triage/SKILL.md](skills/01-business-analysis/business-analyst/intake/request-triage/SKILL.md)

**Check request completeness** · `request-completeness-check`

- When: Find what is missing or vague in a request before work starts
- File: [skills/01-business-analysis/business-analyst/intake/request-completeness-check/SKILL.md](skills/01-business-analysis/business-analyst/intake/request-completeness-check/SKILL.md)

#### Stakeholder Analysis

**Identify stakeholders** · `stakeholder-identification`

- When: List everyone affected, influencing or deciding
- File: [skills/01-business-analysis/business-analyst/stakeholders/stakeholder-identification/SKILL.md](skills/01-business-analysis/business-analyst/stakeholders/stakeholder-identification/SKILL.md)

**Map stakeholders by power/interest** · `stakeholder-map`

- When: Place stakeholders on a power/interest grid with engagement strategy
- File: [skills/01-business-analysis/business-analyst/stakeholders/stakeholder-map/SKILL.md](skills/01-business-analysis/business-analyst/stakeholders/stakeholder-map/SKILL.md)

**Build a RACI matrix** · `raci-matrix`

- When: Assign Responsible/Accountable/Consulted/Informed per activity
- File: [skills/01-business-analysis/business-analyst/stakeholders/raci-matrix/SKILL.md](skills/01-business-analysis/business-analyst/stakeholders/raci-matrix/SKILL.md)

#### Elicitation

**Prepare interview questions** · `interview-question-set`

- When: Build open, probing and validation questions per stakeholder type
- File: [skills/01-business-analysis/business-analyst/elicitation/interview-question-set/SKILL.md](skills/01-business-analysis/business-analyst/elicitation/interview-question-set/SKILL.md)

**Analyze interview notes** · `interview-notes-analysis`

- When: Extract needs, pains, rules and conflicts from interview notes
- File: [skills/01-business-analysis/business-analyst/elicitation/interview-notes-analysis/SKILL.md](skills/01-business-analysis/business-analyst/elicitation/interview-notes-analysis/SKILL.md)

**Plan a requirements workshop** · `workshop-plan`

- When: Design workshop goals, activities, timing and outputs
- File: [skills/01-business-analysis/business-analyst/elicitation/workshop-plan/SKILL.md](skills/01-business-analysis/business-analyst/elicitation/workshop-plan/SKILL.md)

**Design a questionnaire** · `questionnaire-design`

- When: Create an unbiased survey to gather requirements at scale
- File: [skills/01-business-analysis/business-analyst/elicitation/questionnaire-design/SKILL.md](skills/01-business-analysis/business-analyst/elicitation/questionnaire-design/SKILL.md)

**Elicit from existing documents** · `document-analysis`

- When: Mine specs, manuals, regulations for requirements
- File: [skills/01-business-analysis/business-analyst/elicitation/document-analysis/SKILL.md](skills/01-business-analysis/business-analyst/elicitation/document-analysis/SKILL.md)

**Structure job-shadowing observations** · `observation-notes`

- When: Turn shadowing notes into tasks, pains and workarounds
- File: [skills/01-business-analysis/business-analyst/elicitation/observation-notes/SKILL.md](skills/01-business-analysis/business-analyst/elicitation/observation-notes/SKILL.md)

#### Requirements Documentation

**Write a Business Requirements Document** · `brd-writing`

- When: Document business goals, scope, stakeholders and high-level requirements
- File: [skills/01-business-analysis/business-analyst/documentation/brd-writing/SKILL.md](skills/01-business-analysis/business-analyst/documentation/brd-writing/SKILL.md)

**Write a Functional Requirements Document** · `frd-writing`

- When: Specify system behavior, inputs, outputs and rules
- File: [skills/01-business-analysis/business-analyst/documentation/frd-writing/SKILL.md](skills/01-business-analysis/business-analyst/documentation/frd-writing/SKILL.md)

**Write user stories** · `user-story`

- When: Write As a/I want/So that stories with context
- File: [skills/01-business-analysis/business-analyst/documentation/user-story/SKILL.md](skills/01-business-analysis/business-analyst/documentation/user-story/SKILL.md)

**Write acceptance criteria** · `acceptance-criteria`

- When: Write testable criteria in Given/When/Then or rule form
- File: [skills/01-business-analysis/business-analyst/documentation/acceptance-criteria/SKILL.md](skills/01-business-analysis/business-analyst/documentation/acceptance-criteria/SKILL.md)

**Write a use case specification** · `use-case-spec`

- When: Actors, preconditions, main/alternate/exception flows
- File: [skills/01-business-analysis/business-analyst/documentation/use-case-spec/SKILL.md](skills/01-business-analysis/business-analyst/documentation/use-case-spec/SKILL.md)

**Specify non-functional requirements** · `nfr-specification`

- When: Make performance, security, availability etc. measurable
- File: [skills/01-business-analysis/business-analyst/documentation/nfr-specification/SKILL.md](skills/01-business-analysis/business-analyst/documentation/nfr-specification/SKILL.md)

**Build a business rules catalog** · `business-rules-catalog`

- When: Extract and normalize business rules with IDs and sources
- File: [skills/01-business-analysis/business-analyst/documentation/business-rules-catalog/SKILL.md](skills/01-business-analysis/business-analyst/documentation/business-rules-catalog/SKILL.md)

**Define data requirements** · `data-requirements`

- When: Entities, attributes, validations, ownership and retention
- File: [skills/01-business-analysis/business-analyst/documentation/data-requirements/SKILL.md](skills/01-business-analysis/business-analyst/documentation/data-requirements/SKILL.md)

**Specify report requirements** · `report-requirements`

- When: Define report purpose, fields, filters, calculations and audience
- File: [skills/01-business-analysis/business-analyst/documentation/report-requirements/SKILL.md](skills/01-business-analysis/business-analyst/documentation/report-requirements/SKILL.md)

**Specify screen/UI requirements** · `screen-requirements`

- When: Describe fields, validations, states and behaviors per screen
- File: [skills/01-business-analysis/business-analyst/documentation/screen-requirements/SKILL.md](skills/01-business-analysis/business-analyst/documentation/screen-requirements/SKILL.md)

**Specify integration requirements** · `integration-requirements`

- When: Define systems, data exchanged, frequency, errors and SLAs
- File: [skills/01-business-analysis/business-analyst/documentation/integration-requirements/SKILL.md](skills/01-business-analysis/business-analyst/documentation/integration-requirements/SKILL.md)

#### Requirements Quality

**Find gaps in requirements** · `requirements-gap-analysis`

- When: Reviews a set of requirements (BRD, FRD, user stories, use cases) and detects what is missing: flows, actors and roles, edge cases, error handling, data rules, non-functional requirements and transition needs. Use when requirements look complete but have not been stress-tested, before estimation or sign-off, or when asked 'what are we missing?'.
- Try: _"Here is our FRD for the loan application module. Find the gaps before we send it for estimation."_
- Related: `ambiguity-detection`, `requirements-consistency-check`, `requirements-review-checklist`, `nfr-specification`, `error-scenario-catalog`
- File: [skills/01-business-analysis/business-analyst/quality/requirements-gap-analysis/SKILL.md](skills/01-business-analysis/business-analyst/quality/requirements-gap-analysis/SKILL.md)

**Detect ambiguous requirements** · `ambiguity-detection`

- When: Flag vague words, undefined terms and untestable statements
- File: [skills/01-business-analysis/business-analyst/quality/ambiguity-detection/SKILL.md](skills/01-business-analysis/business-analyst/quality/ambiguity-detection/SKILL.md)

**Check requirements consistency** · `requirements-consistency-check`

- When: Find contradictions and duplicates across requirements
- File: [skills/01-business-analysis/business-analyst/quality/requirements-consistency-check/SKILL.md](skills/01-business-analysis/business-analyst/quality/requirements-consistency-check/SKILL.md)

**Check stories against INVEST** · `invest-check`

- When: Evaluate stories for Independent, Negotiable, Valuable, Estimable, Small, Testable
- File: [skills/01-business-analysis/business-analyst/quality/invest-check/SKILL.md](skills/01-business-analysis/business-analyst/quality/invest-check/SKILL.md)

**Build a traceability matrix** · `traceability-matrix`

- When: Link requirements to goals, designs, tests and releases
- File: [skills/01-business-analysis/business-analyst/quality/traceability-matrix/SKILL.md](skills/01-business-analysis/business-analyst/quality/traceability-matrix/SKILL.md)

**Prioritize requirements** · `requirements-prioritization`

- When: Apply MoSCoW, Kano or value/effort and justify ranking
- File: [skills/01-business-analysis/business-analyst/quality/requirements-prioritization/SKILL.md](skills/01-business-analysis/business-analyst/quality/requirements-prioritization/SKILL.md)

**Run a requirements review** · `requirements-review-checklist`

- When: Checklist-driven review before sign-off
- File: [skills/01-business-analysis/business-analyst/quality/requirements-review-checklist/SKILL.md](skills/01-business-analysis/business-analyst/quality/requirements-review-checklist/SKILL.md)

#### Process Analysis

**Document the as-is process** · `as-is-process`

- When: Capture current steps, actors, systems, pains and timings
- File: [skills/01-business-analysis/business-analyst/process/as-is-process/SKILL.md](skills/01-business-analysis/business-analyst/process/as-is-process/SKILL.md)

**Design the to-be process** · `to-be-process`

- When: Propose an improved process and highlight changes
- File: [skills/01-business-analysis/business-analyst/process/to-be-process/SKILL.md](skills/01-business-analysis/business-analyst/process/to-be-process/SKILL.md)

**Describe a process in BPMN** · `bpmn-model`

- When: Produce BPMN elements (events, gateways, lanes) as text/diagram code
- File: [skills/01-business-analysis/business-analyst/process/bpmn-model/SKILL.md](skills/01-business-analysis/business-analyst/process/bpmn-model/SKILL.md)

**Analyze as-is vs to-be gaps** · `process-gap-analysis`

- When: List gaps and required changes in people, process, tech
- File: [skills/01-business-analysis/business-analyst/process/process-gap-analysis/SKILL.md](skills/01-business-analysis/business-analyst/process/process-gap-analysis/SKILL.md)

**Map a value stream** · `value-stream-map`

- When: Identify value-add vs waste and lead/process times
- File: [skills/01-business-analysis/business-analyst/process/value-stream-map/SKILL.md](skills/01-business-analysis/business-analyst/process/value-stream-map/SKILL.md)

#### Solution Assessment

**Assess feasibility** · `feasibility-study`

- When: Evaluate technical, operational, economic and schedule feasibility
- File: [skills/01-business-analysis/business-analyst/solution/feasibility-study/SKILL.md](skills/01-business-analysis/business-analyst/solution/feasibility-study/SKILL.md)

**Run a cost-benefit analysis** · `cost-benefit-analysis`

- When: Quantify costs, benefits, ROI and payback
- File: [skills/01-business-analysis/business-analyst/solution/cost-benefit-analysis/SKILL.md](skills/01-business-analysis/business-analyst/solution/cost-benefit-analysis/SKILL.md)

**Analyze change impact** · `impact-analysis`

- When: Find affected processes, systems, data, users and reports
- File: [skills/01-business-analysis/business-analyst/solution/impact-analysis/SKILL.md](skills/01-business-analysis/business-analyst/solution/impact-analysis/SKILL.md)

**Analyze a change request** · `change-request-analysis`

- When: Assess scope, effort, risk and recommend accept/defer/reject
- File: [skills/01-business-analysis/business-analyst/solution/change-request-analysis/SKILL.md](skills/01-business-analysis/business-analyst/solution/change-request-analysis/SKILL.md)

**Prepare requirements sign-off** · `requirements-sign-off`

- When: Summarize baseline, open issues and approvals needed
- File: [skills/01-business-analysis/business-analyst/solution/requirements-sign-off/SKILL.md](skills/01-business-analysis/business-analyst/solution/requirements-sign-off/SKILL.md)

### System Analyst

#### System Specification

**Write a Software Requirements Specification** · `srs-writing`

- When: ISO/IEC/IEEE 29148 aligned SRS
- File: [skills/01-business-analysis/system-analyst/specification/srs-writing/SKILL.md](skills/01-business-analysis/system-analyst/specification/srs-writing/SKILL.md)

**Model entity states** · `state-model`

- When: Define states, transitions, triggers and guards for an entity
- File: [skills/01-business-analysis/system-analyst/specification/state-model/SKILL.md](skills/01-business-analysis/system-analyst/specification/state-model/SKILL.md)

**Describe a system interaction sequence** · `sequence-flow`

- When: Produce sequence diagrams for a scenario across systems
- File: [skills/01-business-analysis/system-analyst/specification/sequence-flow/SKILL.md](skills/01-business-analysis/system-analyst/specification/sequence-flow/SKILL.md)

**Map fields between systems** · `field-mapping`

- When: Source-to-target mapping with transformations and rules
- File: [skills/01-business-analysis/system-analyst/specification/field-mapping/SKILL.md](skills/01-business-analysis/system-analyst/specification/field-mapping/SKILL.md)

**Catalog error scenarios** · `error-scenario-catalog`

- When: List failure cases, messages and expected system behavior
- File: [skills/01-business-analysis/system-analyst/specification/error-scenario-catalog/SKILL.md](skills/01-business-analysis/system-analyst/specification/error-scenario-catalog/SKILL.md)

## Product Management

### Product Manager

#### Product Strategy

**Write a product vision** · `product-vision`

- When: Vision statement and vision board (target group, needs, product, goals)
- File: [skills/02-product/product-manager/strategy/product-vision/SKILL.md](skills/02-product/product-manager/strategy/product-vision/SKILL.md)

**Write a product strategy one-pager** · `product-strategy-one-pager`

- When: Where to play, how to win, bets and non-goals
- File: [skills/02-product/product-manager/strategy/product-strategy-one-pager/SKILL.md](skills/02-product/product-manager/strategy/product-strategy-one-pager/SKILL.md)

**Define OKRs** · `okr-definition`

- When: Write outcome-based objectives and measurable key results
- File: [skills/02-product/product-manager/strategy/okr-definition/SKILL.md](skills/02-product/product-manager/strategy/okr-definition/SKILL.md)

**Analyze a market** · `market-analysis`

- When: TAM/SAM/SOM, segments, trends and drivers
- File: [skills/02-product/product-manager/strategy/market-analysis/SKILL.md](skills/02-product/product-manager/strategy/market-analysis/SKILL.md)

**Analyze competitors** · `competitor-analysis`

- When: Feature, pricing, positioning comparison and gaps
- File: [skills/02-product/product-manager/strategy/competitor-analysis/SKILL.md](skills/02-product/product-manager/strategy/competitor-analysis/SKILL.md)

**Fill a business/lean canvas** · `business-model-canvas`

- When: Complete Business Model or Lean Canvas for an idea
- File: [skills/02-product/product-manager/strategy/business-model-canvas/SKILL.md](skills/02-product/product-manager/strategy/business-model-canvas/SKILL.md)

**Analyze pricing options** · `pricing-analysis`

- When: Compare pricing models and willingness-to-pay signals
- File: [skills/02-product/product-manager/strategy/pricing-analysis/SKILL.md](skills/02-product/product-manager/strategy/pricing-analysis/SKILL.md)

#### Discovery

**Build a persona** · `persona`

- When: Evidence-based persona with goals, pains, behaviors
- File: [skills/02-product/product-manager/discovery/persona/SKILL.md](skills/02-product/product-manager/discovery/persona/SKILL.md)

**Frame Jobs-to-be-Done** · `jobs-to-be-done`

- When: Write job statements and desired outcomes
- File: [skills/02-product/product-manager/discovery/jobs-to-be-done/SKILL.md](skills/02-product/product-manager/discovery/jobs-to-be-done/SKILL.md)

**Map the customer journey** · `customer-journey-map`

- When: Stages, actions, thoughts, emotions, touchpoints, pains
- File: [skills/02-product/product-manager/discovery/customer-journey-map/SKILL.md](skills/02-product/product-manager/discovery/customer-journey-map/SKILL.md)

**Build an opportunity solution tree** · `opportunity-solution-tree`

- When: Link outcome to opportunities, solutions and experiments
- File: [skills/02-product/product-manager/discovery/opportunity-solution-tree/SKILL.md](skills/02-product/product-manager/discovery/opportunity-solution-tree/SKILL.md)

**Write a product hypothesis** · `hypothesis-statement`

- When: We believe/will result in/we'll know when format
- File: [skills/02-product/product-manager/discovery/hypothesis-statement/SKILL.md](skills/02-product/product-manager/discovery/hypothesis-statement/SKILL.md)

**Design a product experiment** · `experiment-design`

- When: A/B or fake-door test with metric, sample and stop rules
- File: [skills/02-product/product-manager/discovery/experiment-design/SKILL.md](skills/02-product/product-manager/discovery/experiment-design/SKILL.md)

**Synthesize customer feedback** · `feedback-synthesis`

- When: Cluster feedback into themes with frequency and severity
- File: [skills/02-product/product-manager/discovery/feedback-synthesis/SKILL.md](skills/02-product/product-manager/discovery/feedback-synthesis/SKILL.md)

**Write a problem interview script** · `problem-interview-script`

- When: Non-leading customer interview (Mom Test style)
- File: [skills/02-product/product-manager/discovery/problem-interview-script/SKILL.md](skills/02-product/product-manager/discovery/problem-interview-script/SKILL.md)

#### Product Definition

**Write a Product Requirements Document** · `prd-writing`

- When: Problem, goals, users, scope, requirements, metrics, risks
- File: [skills/02-product/product-manager/definition/prd-writing/SKILL.md](skills/02-product/product-manager/definition/prd-writing/SKILL.md)

**Write a feature brief** · `feature-brief`

- When: One-page brief of a feature for alignment
- File: [skills/02-product/product-manager/definition/feature-brief/SKILL.md](skills/02-product/product-manager/definition/feature-brief/SKILL.md)

**Scope an MVP** · `mvp-scoping`

- When: Cut scope to the smallest testable value
- File: [skills/02-product/product-manager/definition/mvp-scoping/SKILL.md](skills/02-product/product-manager/definition/mvp-scoping/SKILL.md)

**Break an epic into stories** · `epic-breakdown`

- When: Decompose epics into thin vertical slices
- File: [skills/02-product/product-manager/definition/epic-breakdown/SKILL.md](skills/02-product/product-manager/definition/epic-breakdown/SKILL.md)

**Build a user story map** · `story-mapping`

- When: Backbone activities, steps, stories and release slices
- File: [skills/02-product/product-manager/definition/story-mapping/SKILL.md](skills/02-product/product-manager/definition/story-mapping/SKILL.md)

#### Metrics

**Define a North Star metric** · `north-star-metric`

- When: Pick a value metric and its input metrics tree
- File: [skills/02-product/product-manager/metrics/north-star-metric/SKILL.md](skills/02-product/product-manager/metrics/north-star-metric/SKILL.md)

**Define KPIs** · `kpi-definition`

- When: Name, formula, source, target, owner, cadence
- File: [skills/02-product/product-manager/metrics/kpi-definition/SKILL.md](skills/02-product/product-manager/metrics/kpi-definition/SKILL.md)

**Analyze a funnel** · `funnel-analysis`

- When: Find drop-off points and hypotheses to improve
- File: [skills/02-product/product-manager/metrics/funnel-analysis/SKILL.md](skills/02-product/product-manager/metrics/funnel-analysis/SKILL.md)

**Review feature adoption** · `feature-adoption-review`

- When: Assess usage, retention and outcome of a shipped feature
- File: [skills/02-product/product-manager/metrics/feature-adoption-review/SKILL.md](skills/02-product/product-manager/metrics/feature-adoption-review/SKILL.md)

#### Launch

**Write a go-to-market plan** · `go-to-market-plan`

- When: Audience, messaging, channels, timing, enablement
- File: [skills/02-product/product-manager/launch/go-to-market-plan/SKILL.md](skills/02-product/product-manager/launch/go-to-market-plan/SKILL.md)

**Write a release announcement** · `release-announcement`

- When: Customer-facing announcement focused on benefits
- File: [skills/02-product/product-manager/launch/release-announcement/SKILL.md](skills/02-product/product-manager/launch/release-announcement/SKILL.md)

**Write a positioning statement** · `positioning-statement`

- When: For/who/is a/that/unlike format
- File: [skills/02-product/product-manager/launch/positioning-statement/SKILL.md](skills/02-product/product-manager/launch/positioning-statement/SKILL.md)

### Product Owner

#### Backlog Management

**Refine the backlog** · `backlog-refinement`

- When: Clarify, split, estimate-ready and order items
- File: [skills/02-product/product-owner/backlog/backlog-refinement/SKILL.md](skills/02-product/product-owner/backlog/backlog-refinement/SKILL.md)

**Prioritize the backlog** · `backlog-prioritization`

- When: Apply WSJF, RICE, value/effort with rationale
- File: [skills/02-product/product-owner/backlog/backlog-prioritization/SKILL.md](skills/02-product/product-owner/backlog/backlog-prioritization/SKILL.md)

**Split large stories** · `story-splitting`

- When: Split by workflow, rule, data, interface or spike
- File: [skills/02-product/product-owner/backlog/story-splitting/SKILL.md](skills/02-product/product-owner/backlog/story-splitting/SKILL.md)

**Define Definition of Ready** · `definition-of-ready`

- When: Entry criteria for work to start
- File: [skills/02-product/product-owner/backlog/definition-of-ready/SKILL.md](skills/02-product/product-owner/backlog/definition-of-ready/SKILL.md)

**Define Definition of Done** · `definition-of-done`

- When: Quality checklist for work to be complete
- File: [skills/02-product/product-owner/backlog/definition-of-done/SKILL.md](skills/02-product/product-owner/backlog/definition-of-done/SKILL.md)

**Check backlog health** · `backlog-health-check`

- When: Detect stale, duplicate, oversized or orphan items
- File: [skills/02-product/product-owner/backlog/backlog-health-check/SKILL.md](skills/02-product/product-owner/backlog/backlog-health-check/SKILL.md)

#### Planning

**Build a product roadmap** · `roadmap`

- When: Now/Next/Later or timeline roadmap tied to outcomes
- File: [skills/02-product/product-owner/planning/roadmap/SKILL.md](skills/02-product/product-owner/planning/roadmap/SKILL.md)

**Plan a release** · `release-planning`

- When: Scope, dates, dependencies and confidence for a release
- File: [skills/02-product/product-owner/planning/release-planning/SKILL.md](skills/02-product/product-owner/planning/release-planning/SKILL.md)

**Write an iteration goal** · `iteration-goal`

- When: Single coherent goal for a sprint/iteration
- File: [skills/02-product/product-owner/planning/iteration-goal/SKILL.md](skills/02-product/product-owner/planning/iteration-goal/SKILL.md)

**Prepare a product review** · `stakeholder-review-prep`

- When: What was built, feedback asked, decisions needed
- File: [skills/02-product/product-owner/planning/stakeholder-review-prep/SKILL.md](skills/02-product/product-owner/planning/stakeholder-review-prep/SKILL.md)

## Project & Delivery Management

### Project Manager

#### Initiation

**Write a project charter** · `project-charter`

- When: Drafts a project charter that formally authorizes a project, stating purpose, measurable objectives, high-level scope, key stakeholders, budget envelope, milestones, risks and the project manager's authority. Use when a project has been approved or is seeking approval and needs a one-document mandate signed by a sponsor.
- Try: _"Write a project charter for migrating our on-prem CRM to a SaaS platform; sponsor is the Sales VP, target go-live is Q2."_
- Related: `scope-statement`, `stakeholder-register`, `kickoff-deck`, `business-model-canvas`, `governance-framework`
- File: [skills/03-delivery/project-manager/initiation/project-charter/SKILL.md](skills/03-delivery/project-manager/initiation/project-charter/SKILL.md)

**Write a scope statement** · `scope-statement`

- When: In-scope, out-of-scope, deliverables, constraints, assumptions
- File: [skills/03-delivery/project-manager/initiation/scope-statement/SKILL.md](skills/03-delivery/project-manager/initiation/scope-statement/SKILL.md)

**Prepare a kickoff** · `kickoff-deck`

- When: Kickoff agenda and content for team and sponsors
- File: [skills/03-delivery/project-manager/initiation/kickoff-deck/SKILL.md](skills/03-delivery/project-manager/initiation/kickoff-deck/SKILL.md)

**Build a stakeholder register** · `stakeholder-register`

- When: Roles, interests, influence, communication needs
- File: [skills/03-delivery/project-manager/initiation/stakeholder-register/SKILL.md](skills/03-delivery/project-manager/initiation/stakeholder-register/SKILL.md)

#### Planning

**Build a work breakdown structure** · `wbs`

- When: Decompose deliverables into work packages
- File: [skills/03-delivery/project-manager/planning/wbs/SKILL.md](skills/03-delivery/project-manager/planning/wbs/SKILL.md)

**Estimate with three-point/PERT** · `estimation-three-point`

- When: Optimistic/likely/pessimistic with expected value and range
- File: [skills/03-delivery/project-manager/planning/estimation-three-point/SKILL.md](skills/03-delivery/project-manager/planning/estimation-three-point/SKILL.md)

**Build a project schedule** · `schedule-plan`

- When: Sequence tasks, dependencies, milestones, critical path
- File: [skills/03-delivery/project-manager/planning/schedule-plan/SKILL.md](skills/03-delivery/project-manager/planning/schedule-plan/SKILL.md)

**Build a resource plan** · `resource-plan`

- When: Skills, allocation and gaps over time
- File: [skills/03-delivery/project-manager/planning/resource-plan/SKILL.md](skills/03-delivery/project-manager/planning/resource-plan/SKILL.md)

**Build a project budget** · `budget-plan`

- When: Cost breakdown, contingency and cash flow
- File: [skills/03-delivery/project-manager/planning/budget-plan/SKILL.md](skills/03-delivery/project-manager/planning/budget-plan/SKILL.md)

**Build a communication plan** · `communication-plan`

- When: Who gets what, when, how, from whom
- File: [skills/03-delivery/project-manager/planning/communication-plan/SKILL.md](skills/03-delivery/project-manager/planning/communication-plan/SKILL.md)

**Build a risk register** · `risk-register`

- When: Risks with probability, impact, owner, response
- File: [skills/03-delivery/project-manager/planning/risk-register/SKILL.md](skills/03-delivery/project-manager/planning/risk-register/SKILL.md)

**Map dependencies** · `dependency-map`

- When: Internal/external dependencies with owners and dates
- File: [skills/03-delivery/project-manager/planning/dependency-map/SKILL.md](skills/03-delivery/project-manager/planning/dependency-map/SKILL.md)

#### Monitoring & Control

**Write a project status report** · `project-status-report`

- When: Schedule, cost, scope, risks, decisions needed
- File: [skills/03-delivery/project-manager/monitoring/project-status-report/SKILL.md](skills/03-delivery/project-manager/monitoring/project-status-report/SKILL.md)

**Maintain a RAID log** · `raid-log`

- When: Risks, Assumptions, Issues, Dependencies
- File: [skills/03-delivery/project-manager/monitoring/raid-log/SKILL.md](skills/03-delivery/project-manager/monitoring/raid-log/SKILL.md)

**Run earned value analysis** · `earned-value-analysis`

- When: PV, EV, AC, SPI, CPI and forecast
- File: [skills/03-delivery/project-manager/monitoring/earned-value-analysis/SKILL.md](skills/03-delivery/project-manager/monitoring/earned-value-analysis/SKILL.md)

**Run change control** · `change-control`

- When: Evaluate and log scope/time/cost changes
- File: [skills/03-delivery/project-manager/monitoring/change-control/SKILL.md](skills/03-delivery/project-manager/monitoring/change-control/SKILL.md)

**Manage an issue** · `issue-management`

- When: Log, assess, assign and track an issue to closure
- File: [skills/03-delivery/project-manager/monitoring/issue-management/SKILL.md](skills/03-delivery/project-manager/monitoring/issue-management/SKILL.md)

**Review vendor performance** · `vendor-status-review`

- When: Check deliverables, SLAs and contract obligations
- File: [skills/03-delivery/project-manager/monitoring/vendor-status-review/SKILL.md](skills/03-delivery/project-manager/monitoring/vendor-status-review/SKILL.md)

#### Closure

**Write a project closure report** · `project-closure-report`

- When: Outcomes vs objectives, variances, handover, lessons
- File: [skills/03-delivery/project-manager/closure/project-closure-report/SKILL.md](skills/03-delivery/project-manager/closure/project-closure-report/SKILL.md)

**Prepare deliverable acceptance** · `acceptance-certificate`

- When: Acceptance record with criteria and sign-offs
- File: [skills/03-delivery/project-manager/closure/acceptance-certificate/SKILL.md](skills/03-delivery/project-manager/closure/acceptance-certificate/SKILL.md)

### Scrum Master / Agile Coach

#### Team Events

**Facilitate iteration planning** · `iteration-planning`

- When: Capacity, goal, selection and task breakdown
- File: [skills/03-delivery/agile-delivery/ceremonies/iteration-planning/SKILL.md](skills/03-delivery/agile-delivery/ceremonies/iteration-planning/SKILL.md)

**Summarize a daily sync** · `daily-sync-summary`

- When: Progress, plan, blockers per person and team
- File: [skills/03-delivery/agile-delivery/ceremonies/daily-sync-summary/SKILL.md](skills/03-delivery/agile-delivery/ceremonies/daily-sync-summary/SKILL.md)

**Prepare an iteration review** · `iteration-review-prep`

- When: Demo order, increment summary, feedback questions
- File: [skills/03-delivery/agile-delivery/ceremonies/iteration-review-prep/SKILL.md](skills/03-delivery/agile-delivery/ceremonies/iteration-review-prep/SKILL.md)

**Facilitate a retrospective** · `retrospective-facilitation`

- When: Pick a format, run it and produce actions
- File: [skills/03-delivery/agile-delivery/ceremonies/retrospective-facilitation/SKILL.md](skills/03-delivery/agile-delivery/ceremonies/retrospective-facilitation/SKILL.md)

**Design a retrospective format** · `retrospective-format`

- When: Tailor a retro format to team mood and topic
- File: [skills/03-delivery/agile-delivery/ceremonies/retrospective-format/SKILL.md](skills/03-delivery/agile-delivery/ceremonies/retrospective-format/SKILL.md)

**Facilitate relative estimation** · `estimation-session`

- When: Planning poker / t-shirt sizing guidance and reference stories
- File: [skills/03-delivery/agile-delivery/ceremonies/estimation-session/SKILL.md](skills/03-delivery/agile-delivery/ceremonies/estimation-session/SKILL.md)

#### Flow & Metrics

**Analyze velocity/throughput** · `velocity-analysis`

- When: Trends, variability and forecast
- File: [skills/03-delivery/agile-delivery/flow/velocity-analysis/SKILL.md](skills/03-delivery/agile-delivery/flow/velocity-analysis/SKILL.md)

**Read burndown/burnup charts** · `burndown-analysis`

- When: Interpret charts and flag risks
- File: [skills/03-delivery/agile-delivery/flow/burndown-analysis/SKILL.md](skills/03-delivery/agile-delivery/flow/burndown-analysis/SKILL.md)

**Analyze cycle/lead time** · `cycle-time-analysis`

- When: Percentiles, bottlenecks, aging work
- File: [skills/03-delivery/agile-delivery/flow/cycle-time-analysis/SKILL.md](skills/03-delivery/agile-delivery/flow/cycle-time-analysis/SKILL.md)

**Define WIP limits and flow policies** · `wip-policy`

- When: Board columns, WIP limits, entry/exit policies
- File: [skills/03-delivery/agile-delivery/flow/wip-policy/SKILL.md](skills/03-delivery/agile-delivery/flow/wip-policy/SKILL.md)

**Forecast delivery with Monte Carlo** · `monte-carlo-forecast`

- When: Probabilistic "when/how many" forecast from throughput
- File: [skills/03-delivery/agile-delivery/flow/monte-carlo-forecast/SKILL.md](skills/03-delivery/agile-delivery/flow/monte-carlo-forecast/SKILL.md)

**Track impediments** · `impediment-tracking`

- When: Log, escalate and resolve blockers
- File: [skills/03-delivery/agile-delivery/flow/impediment-tracking/SKILL.md](skills/03-delivery/agile-delivery/flow/impediment-tracking/SKILL.md)

#### Team Development

**Create a team working agreement** · `working-agreement`

- When: Norms for communication, availability, reviews, meetings
- File: [skills/03-delivery/agile-delivery/team/working-agreement/SKILL.md](skills/03-delivery/agile-delivery/team/working-agreement/SKILL.md)

**Run a team health check** · `team-health-check`

- When: Survey dimensions, trends and follow-ups
- File: [skills/03-delivery/agile-delivery/team/team-health-check/SKILL.md](skills/03-delivery/agile-delivery/team/team-health-check/SKILL.md)

**Assess agile maturity** · `agile-maturity-assessment`

- When: Score practices and suggest next improvements
- File: [skills/03-delivery/agile-delivery/team/agile-maturity-assessment/SKILL.md](skills/03-delivery/agile-delivery/team/agile-maturity-assessment/SKILL.md)

### Program Manager / PMO

#### Portfolio & Program

**Prioritize a project portfolio** · `portfolio-prioritization`

- When: Score initiatives on value, risk, strategic fit, capacity
- File: [skills/03-delivery/program-pmo/portfolio/portfolio-prioritization/SKILL.md](skills/03-delivery/program-pmo/portfolio/portfolio-prioritization/SKILL.md)

**Build a program roadmap** · `program-roadmap`

- When: Cross-team milestones and integration points
- File: [skills/03-delivery/program-pmo/portfolio/program-roadmap/SKILL.md](skills/03-delivery/program-pmo/portfolio/program-roadmap/SKILL.md)

**Run cross-team dependency planning** · `cross-team-dependency-board`

- When: Identify, negotiate and track inter-team dependencies
- File: [skills/03-delivery/program-pmo/portfolio/cross-team-dependency-board/SKILL.md](skills/03-delivery/program-pmo/portfolio/cross-team-dependency-board/SKILL.md)

**Prepare a steering committee pack** · `steering-committee-pack`

- When: Status, decisions needed, risks, financials
- File: [skills/03-delivery/program-pmo/portfolio/steering-committee-pack/SKILL.md](skills/03-delivery/program-pmo/portfolio/steering-committee-pack/SKILL.md)

**Define project governance** · `governance-framework`

- When: Decision rights, forums, gates, reporting cadence
- File: [skills/03-delivery/program-pmo/portfolio/governance-framework/SKILL.md](skills/03-delivery/program-pmo/portfolio/governance-framework/SKILL.md)

**Track benefits realization** · `benefits-realization`

- When: Planned vs actual benefits after delivery
- File: [skills/03-delivery/program-pmo/portfolio/benefits-realization/SKILL.md](skills/03-delivery/program-pmo/portfolio/benefits-realization/SKILL.md)

## Architecture

### Enterprise Architect

#### Architecture Strategy

**Define architecture principles** · `architecture-principles`

- When: Principle, rationale and implications (TOGAF style)
- File: [skills/04-architecture/enterprise-architect/strategy/architecture-principles/SKILL.md](skills/04-architecture/enterprise-architect/strategy/architecture-principles/SKILL.md)

**Build a business capability map** · `capability-map`

- When: Hierarchical capabilities with maturity and heatmap
- File: [skills/04-architecture/enterprise-architect/strategy/capability-map/SKILL.md](skills/04-architecture/enterprise-architect/strategy/capability-map/SKILL.md)

**Assess the application portfolio** · `application-portfolio-assessment`

- When: TIME model: tolerate, invest, migrate, eliminate
- File: [skills/04-architecture/enterprise-architect/strategy/application-portfolio-assessment/SKILL.md](skills/04-architecture/enterprise-architect/strategy/application-portfolio-assessment/SKILL.md)

**Define target-state architecture** · `target-state-architecture`

- When: Baseline, target, gap and transition roadmap
- File: [skills/04-architecture/enterprise-architect/strategy/target-state-architecture/SKILL.md](skills/04-architecture/enterprise-architect/strategy/target-state-architecture/SKILL.md)

**Maintain a technology radar** · `tech-radar`

- When: Classify technologies into adopt/trial/assess/hold
- File: [skills/04-architecture/enterprise-architect/strategy/tech-radar/SKILL.md](skills/04-architecture/enterprise-architect/strategy/tech-radar/SKILL.md)

### Solution Architect

#### Solution Design

**Write a solution architecture document** · `solution-architecture-document`

- When: arc42-style document: context, constraints, building blocks, runtime, deployment
- File: [skills/04-architecture/solution-architect/design/solution-architecture-document/SKILL.md](skills/04-architecture/solution-architect/design/solution-architecture-document/SKILL.md)

**Describe architecture with C4** · `c4-model`

- When: Context, container, component diagrams as code
- File: [skills/04-architecture/solution-architect/design/c4-model/SKILL.md](skills/04-architecture/solution-architect/design/c4-model/SKILL.md)

**Write an Architecture Decision Record** · `adr`

- When: Context, options, decision, consequences
- File: [skills/04-architecture/solution-architect/design/adr/SKILL.md](skills/04-architecture/solution-architect/design/adr/SKILL.md)

**Select a technology** · `technology-selection`

- When: Criteria, shortlist, PoC plan and recommendation
- File: [skills/04-architecture/solution-architect/design/technology-selection/SKILL.md](skills/04-architecture/solution-architect/design/technology-selection/SKILL.md)

**Choose integration patterns** · `integration-pattern-selection`

- When: Sync/async, API, messaging, file, CDC with trade-offs
- File: [skills/04-architecture/solution-architect/design/integration-pattern-selection/SKILL.md](skills/04-architecture/solution-architect/design/integration-pattern-selection/SKILL.md)

**Map NFRs to architecture tactics** · `nfr-to-architecture`

- When: Quality attribute scenarios and tactics
- File: [skills/04-architecture/solution-architect/design/nfr-to-architecture/SKILL.md](skills/04-architecture/solution-architect/design/nfr-to-architecture/SKILL.md)

**Decide build vs buy** · `build-vs-buy`

- When: TCO, fit, risk, strategic value comparison
- File: [skills/04-architecture/solution-architect/design/build-vs-buy/SKILL.md](skills/04-architecture/solution-architect/design/build-vs-buy/SKILL.md)

**Estimate cloud cost of a design** · `cloud-cost-estimate`

- When: Size components and estimate monthly run cost
- File: [skills/04-architecture/solution-architect/design/cloud-cost-estimate/SKILL.md](skills/04-architecture/solution-architect/design/cloud-cost-estimate/SKILL.md)

#### Architecture Review

**Review an architecture** · `architecture-review`

- When: Check against principles, NFRs, risks, anti-patterns
- File: [skills/04-architecture/solution-architect/review/architecture-review/SKILL.md](skills/04-architecture/solution-architect/review/architecture-review/SKILL.md)

**Run an ATAM-style evaluation** · `atam-evaluation`

- When: Utility tree, sensitivity points, trade-offs, risks
- File: [skills/04-architecture/solution-architect/review/atam-evaluation/SKILL.md](skills/04-architecture/solution-architect/review/atam-evaluation/SKILL.md)

**Review resilience** · `resilience-review`

- When: Failure modes, timeouts, retries, circuit breakers, DR
- File: [skills/04-architecture/solution-architect/review/resilience-review/SKILL.md](skills/04-architecture/solution-architect/review/resilience-review/SKILL.md)

**Review scalability** · `scalability-review`

- When: Bottlenecks, state, partitioning, caching
- File: [skills/04-architecture/solution-architect/review/scalability-review/SKILL.md](skills/04-architecture/solution-architect/review/scalability-review/SKILL.md)

### Software Architect

#### Domain Design

**Run event storming** · `event-storming`

- When: Domain events, commands, aggregates, policies, hot spots
- File: [skills/04-architecture/software-architect/domain/event-storming/SKILL.md](skills/04-architecture/software-architect/domain/event-storming/SKILL.md)

**Map bounded contexts** · `bounded-context-map`

- When: Contexts and relationships (ACL, OHS, shared kernel)
- File: [skills/04-architecture/software-architect/domain/bounded-context-map/SKILL.md](skills/04-architecture/software-architect/domain/bounded-context-map/SKILL.md)

**Design aggregates** · `aggregate-design`

- When: Invariants, boundaries, consistency rules
- File: [skills/04-architecture/software-architect/domain/aggregate-design/SKILL.md](skills/04-architecture/software-architect/domain/aggregate-design/SKILL.md)

**Design an event-driven flow** · `event-driven-design`

- When: Events, schemas, topics, ordering, idempotency, sagas
- File: [skills/04-architecture/software-architect/domain/event-driven-design/SKILL.md](skills/04-architecture/software-architect/domain/event-driven-design/SKILL.md)

**Decompose into services** · `service-decomposition`

- When: Identify service boundaries and data ownership
- File: [skills/04-architecture/software-architect/domain/service-decomposition/SKILL.md](skills/04-architecture/software-architect/domain/service-decomposition/SKILL.md)

#### Architecture Evolution

**Assess technical debt** · `tech-debt-assessment`

- When: Inventory, classify, estimate interest and prioritize
- File: [skills/04-architecture/software-architect/evolution/tech-debt-assessment/SKILL.md](skills/04-architecture/software-architect/evolution/tech-debt-assessment/SKILL.md)

**Plan a migration** · `migration-strategy`

- When: Strangler fig, parallel run, big bang with risks
- File: [skills/04-architecture/software-architect/evolution/migration-strategy/SKILL.md](skills/04-architecture/software-architect/evolution/migration-strategy/SKILL.md)

**Assess a legacy system** · `modernization-assessment`

- When: 7R options with effort and value
- File: [skills/04-architecture/software-architect/evolution/modernization-assessment/SKILL.md](skills/04-architecture/software-architect/evolution/modernization-assessment/SKILL.md)

**Review an API design** · `api-design-review`

- When: Naming, versioning, errors, pagination, idempotency, security
- File: [skills/04-architecture/software-architect/evolution/api-design-review/SKILL.md](skills/04-architecture/software-architect/evolution/api-design-review/SKILL.md)

## Software Engineering

### Developer (Backend/Frontend/Mobile)

#### Technical Design

**Write a technical design doc (RFC)** · `technical-design-doc`

- When: Problem, approach, alternatives, rollout, risks
- File: [skills/05-engineering/developer/design/technical-design-doc/SKILL.md](skills/05-engineering/developer/design/technical-design-doc/SKILL.md)

**Break a story into tasks** · `task-breakdown`

- When: Technical tasks with order and estimates
- File: [skills/05-engineering/developer/design/task-breakdown/SKILL.md](skills/05-engineering/developer/design/task-breakdown/SKILL.md)

**Write an API contract** · `api-contract`

- When: OpenAPI/AsyncAPI spec from requirements
- File: [skills/05-engineering/developer/design/api-contract/SKILL.md](skills/05-engineering/developer/design/api-contract/SKILL.md)

**Design a database schema** · `database-schema-design`

- When: Tables, keys, constraints, indexes from a domain
- File: [skills/05-engineering/developer/design/database-schema-design/SKILL.md](skills/05-engineering/developer/design/database-schema-design/SKILL.md)

**Write a spike report** · `spike-report`

- When: Question, findings, options, recommendation
- File: [skills/05-engineering/developer/design/spike-report/SKILL.md](skills/05-engineering/developer/design/spike-report/SKILL.md)

#### Implementation

**Implement a feature from a story** · `implement-from-story`

- When: Plan and implement against acceptance criteria
- File: [skills/05-engineering/developer/coding/implement-from-story/SKILL.md](skills/05-engineering/developer/coding/implement-from-story/SKILL.md)

**Refactor code** · `refactoring`

- When: Apply named refactorings safely with tests
- File: [skills/05-engineering/developer/coding/refactoring/SKILL.md](skills/05-engineering/developer/coding/refactoring/SKILL.md)

**Review for clean code** · `clean-code-review`

- When: Naming, functions, SOLID, duplication, smells
- File: [skills/05-engineering/developer/coding/clean-code-review/SKILL.md](skills/05-engineering/developer/coding/clean-code-review/SKILL.md)

**Review error handling** · `error-handling-review`

- When: Exceptions, retries, fallbacks, user-facing errors
- File: [skills/05-engineering/developer/coding/error-handling-review/SKILL.md](skills/05-engineering/developer/coding/error-handling-review/SKILL.md)

**Add logging and instrumentation** · `logging-instrumentation`

- When: Structured logs, metrics and traces at the right points
- File: [skills/05-engineering/developer/coding/logging-instrumentation/SKILL.md](skills/05-engineering/developer/coding/logging-instrumentation/SKILL.md)

**Optimize performance** · `performance-optimization`

- When: Profile-driven hotspots and fixes
- File: [skills/05-engineering/developer/coding/performance-optimization/SKILL.md](skills/05-engineering/developer/coding/performance-optimization/SKILL.md)

**Review concurrency** · `concurrency-review`

- When: Races, deadlocks, thread safety, async pitfalls
- File: [skills/05-engineering/developer/coding/concurrency-review/SKILL.md](skills/05-engineering/developer/coding/concurrency-review/SKILL.md)

**Upgrade a dependency** · `dependency-upgrade`

- When: Breaking changes, migration steps, verification
- File: [skills/05-engineering/developer/coding/dependency-upgrade/SKILL.md](skills/05-engineering/developer/coding/dependency-upgrade/SKILL.md)

**Explain code** · `code-explanation`

- When: Explain what code does, why, and its risks
- File: [skills/05-engineering/developer/coding/code-explanation/SKILL.md](skills/05-engineering/developer/coding/code-explanation/SKILL.md)

**Understand legacy code** · `legacy-code-comprehension`

- When: Map modules, flows and hidden rules in unfamiliar code
- File: [skills/05-engineering/developer/coding/legacy-code-comprehension/SKILL.md](skills/05-engineering/developer/coding/legacy-code-comprehension/SKILL.md)

**Build and explain a regex** · `regex-builder`

- When: Write, test cases and explain a regular expression
- File: [skills/05-engineering/developer/coding/regex-builder/SKILL.md](skills/05-engineering/developer/coding/regex-builder/SKILL.md)

**Write a SQL query** · `sql-query-writing`

- When: Correct, readable, index-friendly queries
- File: [skills/05-engineering/developer/coding/sql-query-writing/SKILL.md](skills/05-engineering/developer/coding/sql-query-writing/SKILL.md)

#### Developer Testing

**Write unit tests** · `unit-test-writing`

- When: Arrange-Act-Assert tests covering behavior and edges
- File: [skills/05-engineering/developer/testing/unit-test-writing/SKILL.md](skills/05-engineering/developer/testing/unit-test-writing/SKILL.md)

**Write integration tests** · `integration-test-writing`

- When: Tests across real boundaries with test doubles where needed
- File: [skills/05-engineering/developer/testing/integration-test-writing/SKILL.md](skills/05-engineering/developer/testing/integration-test-writing/SKILL.md)

**Drive code with TDD** · `tdd-cycle`

- When: Red-green-refactor steps for a behavior
- File: [skills/05-engineering/developer/testing/tdd-cycle/SKILL.md](skills/05-engineering/developer/testing/tdd-cycle/SKILL.md)

**Find untested code paths** · `test-gap-finder`

- When: Spot missing tests for branches and edge cases
- File: [skills/05-engineering/developer/testing/test-gap-finder/SKILL.md](skills/05-engineering/developer/testing/test-gap-finder/SKILL.md)

#### Code Collaboration

**Write a commit message** · `commit-message`

- When: Conventional Commits with why
- File: [skills/05-engineering/developer/collaboration/commit-message/SKILL.md](skills/05-engineering/developer/collaboration/commit-message/SKILL.md)

**Write a pull request description** · `pull-request-description`

- When: What, why, how tested, risks, screenshots
- File: [skills/05-engineering/developer/collaboration/pull-request-description/SKILL.md](skills/05-engineering/developer/collaboration/pull-request-description/SKILL.md)

**Review a pull request** · `code-review`

- When: Correctness, design, tests, security, readability
- File: [skills/05-engineering/developer/collaboration/code-review/SKILL.md](skills/05-engineering/developer/collaboration/code-review/SKILL.md)

**Write review comments** · `review-comment-writing`

- When: Specific, kind, actionable, labeled (nit/blocker)
- File: [skills/05-engineering/developer/collaboration/review-comment-writing/SKILL.md](skills/05-engineering/developer/collaboration/review-comment-writing/SKILL.md)

**Choose a branching strategy** · `branching-strategy`

- When: Trunk-based vs GitFlow vs GitHub Flow for context
- File: [skills/05-engineering/developer/collaboration/branching-strategy/SKILL.md](skills/05-engineering/developer/collaboration/branching-strategy/SKILL.md)

#### Debugging

**Reproduce a bug** · `bug-reproduction`

- When: Minimal reproduction steps and environment
- File: [skills/05-engineering/developer/debugging/bug-reproduction/SKILL.md](skills/05-engineering/developer/debugging/bug-reproduction/SKILL.md)

**Analyze a stack trace** · `stack-trace-analysis`

- When: Locate failing frame, cause and fix candidates
- File: [skills/05-engineering/developer/debugging/stack-trace-analysis/SKILL.md](skills/05-engineering/developer/debugging/stack-trace-analysis/SKILL.md)

**Analyze logs** · `log-analysis`

- When: Correlate events, find anomalies and timeline
- File: [skills/05-engineering/developer/debugging/log-analysis/SKILL.md](skills/05-engineering/developer/debugging/log-analysis/SKILL.md)

**Generate debugging hypotheses** · `debugging-hypotheses`

- When: Ranked hypotheses and cheapest test for each
- File: [skills/05-engineering/developer/debugging/debugging-hypotheses/SKILL.md](skills/05-engineering/developer/debugging/debugging-hypotheses/SKILL.md)

#### Developer Documentation

**Write a README** · `readme-writing`

- When: Purpose, setup, usage, config, contributing
- File: [skills/05-engineering/developer/docs/readme-writing/SKILL.md](skills/05-engineering/developer/docs/readme-writing/SKILL.md)

**Write code documentation** · `code-documentation`

- When: Docstrings/comments that explain why, not what
- File: [skills/05-engineering/developer/docs/code-documentation/SKILL.md](skills/05-engineering/developer/docs/code-documentation/SKILL.md)

**Write API reference docs** · `api-reference-docs`

- When: Endpoints, params, examples, errors
- File: [skills/05-engineering/developer/docs/api-reference-docs/SKILL.md](skills/05-engineering/developer/docs/api-reference-docs/SKILL.md)

**Write a changelog entry** · `changelog-entry`

- When: Keep a Changelog formatted entries
- File: [skills/05-engineering/developer/docs/changelog-entry/SKILL.md](skills/05-engineering/developer/docs/changelog-entry/SKILL.md)

#### Frontend Specific

**Design a UI component** · `component-design`

- When: Props, state, events, variants, accessibility
- File: [skills/05-engineering/developer/frontend/component-design/SKILL.md](skills/05-engineering/developer/frontend/component-design/SKILL.md)

**Audit accessibility (WCAG)** · `accessibility-audit`

- When: Check WCAG 2.2 criteria and propose fixes
- File: [skills/05-engineering/developer/frontend/accessibility-audit/SKILL.md](skills/05-engineering/developer/frontend/accessibility-audit/SKILL.md)

**Audit web performance** · `web-performance-audit`

- When: Core Web Vitals issues and fixes
- File: [skills/05-engineering/developer/frontend/web-performance-audit/SKILL.md](skills/05-engineering/developer/frontend/web-performance-audit/SKILL.md)

**Design state management** · `state-management-design`

- When: Local vs global vs server state decisions
- File: [skills/05-engineering/developer/frontend/state-management-design/SKILL.md](skills/05-engineering/developer/frontend/state-management-design/SKILL.md)

#### Mobile Specific

**Write app store release notes** · `app-store-release-notes`

- When: Short user-facing notes per store limits
- File: [skills/05-engineering/developer/mobile/app-store-release-notes/SKILL.md](skills/05-engineering/developer/mobile/app-store-release-notes/SKILL.md)

**Run a mobile release checklist** · `mobile-release-checklist`

- When: Versioning, signing, permissions, store assets, rollout
- File: [skills/05-engineering/developer/mobile/mobile-release-checklist/SKILL.md](skills/05-engineering/developer/mobile/mobile-release-checklist/SKILL.md)

### Tech Lead

#### Technical Leadership

**Write coding standards** · `coding-standards`

- When: Team conventions with examples and rationale
- File: [skills/05-engineering/tech-lead/leadership/coding-standards/SKILL.md](skills/05-engineering/tech-lead/leadership/coding-standards/SKILL.md)

**Estimate technical work** · `technical-estimation`

- When: Decompose, estimate with ranges and assumptions
- File: [skills/05-engineering/tech-lead/leadership/technical-estimation/SKILL.md](skills/05-engineering/tech-lead/leadership/technical-estimation/SKILL.md)

**Onboard a developer** · `technical-onboarding`

- When: Codebase tour, setup, first issues, contacts
- File: [skills/05-engineering/tech-lead/leadership/technical-onboarding/SKILL.md](skills/05-engineering/tech-lead/leadership/technical-onboarding/SKILL.md)

**Review technical risks** · `technical-risk-review`

- When: Identify delivery and quality risks early
- File: [skills/05-engineering/tech-lead/leadership/technical-risk-review/SKILL.md](skills/05-engineering/tech-lead/leadership/technical-risk-review/SKILL.md)

**Report on code quality** · `code-quality-report`

- When: Interpret static analysis metrics and trends
- File: [skills/05-engineering/tech-lead/leadership/code-quality-report/SKILL.md](skills/05-engineering/tech-lead/leadership/code-quality-report/SKILL.md)

## Quality Assurance & Testing

### QA Analyst / Test Engineer

#### Test Strategy & Planning

**Write a test strategy** · `test-strategy`

- When: Levels, types, environments, tools, risk-based focus
- File: [skills/06-quality/qa-analyst/strategy/test-strategy/SKILL.md](skills/06-quality/qa-analyst/strategy/test-strategy/SKILL.md)

**Write a test plan** · `test-plan`

- When: Scope, approach, schedule, entry/exit criteria (ISO 29119)
- File: [skills/06-quality/qa-analyst/strategy/test-plan/SKILL.md](skills/06-quality/qa-analyst/strategy/test-plan/SKILL.md)

**Prioritize tests by risk** · `risk-based-testing`

- When: Likelihood x impact to focus test effort
- File: [skills/06-quality/qa-analyst/strategy/risk-based-testing/SKILL.md](skills/06-quality/qa-analyst/strategy/risk-based-testing/SKILL.md)

**Review requirements for testability** · `testability-review`

- When: Flag untestable or unclear requirements
- File: [skills/06-quality/qa-analyst/strategy/testability-review/SKILL.md](skills/06-quality/qa-analyst/strategy/testability-review/SKILL.md)

#### Test Design

**Derive test scenarios** · `test-scenarios-from-requirements`

- When: High-level positive, negative and edge scenarios
- File: [skills/06-quality/qa-analyst/design/test-scenarios-from-requirements/SKILL.md](skills/06-quality/qa-analyst/design/test-scenarios-from-requirements/SKILL.md)

**Write test cases** · `test-case-writing`

- When: Steps, data, expected results, preconditions
- File: [skills/06-quality/qa-analyst/design/test-case-writing/SKILL.md](skills/06-quality/qa-analyst/design/test-case-writing/SKILL.md)

**Apply equivalence and boundary analysis** · `equivalence-boundary-analysis`

- When: Partition inputs and pick boundary values
- File: [skills/06-quality/qa-analyst/design/equivalence-boundary-analysis/SKILL.md](skills/06-quality/qa-analyst/design/equivalence-boundary-analysis/SKILL.md)

**Build decision table tests** · `decision-table-testing`

- When: Combine conditions and actions for rules
- File: [skills/06-quality/qa-analyst/design/decision-table-testing/SKILL.md](skills/06-quality/qa-analyst/design/decision-table-testing/SKILL.md)

**Build state transition tests** · `state-transition-testing`

- When: Cover valid/invalid transitions
- File: [skills/06-quality/qa-analyst/design/state-transition-testing/SKILL.md](skills/06-quality/qa-analyst/design/state-transition-testing/SKILL.md)

**Generate pairwise combinations** · `pairwise-testing`

- When: Reduce combinations while covering pairs
- File: [skills/06-quality/qa-analyst/design/pairwise-testing/SKILL.md](skills/06-quality/qa-analyst/design/pairwise-testing/SKILL.md)

**Write exploratory test charters** · `exploratory-test-charter`

- When: Mission, areas, heuristics, timebox
- File: [skills/06-quality/qa-analyst/design/exploratory-test-charter/SKILL.md](skills/06-quality/qa-analyst/design/exploratory-test-charter/SKILL.md)

**Design test data** · `test-data-design`

- When: Realistic, anonymized, edge-covering datasets
- File: [skills/06-quality/qa-analyst/design/test-data-design/SKILL.md](skills/06-quality/qa-analyst/design/test-data-design/SKILL.md)

**Write BDD feature files** · `bdd-feature-file`

- When: Gherkin scenarios and scenario outlines
- File: [skills/06-quality/qa-analyst/design/bdd-feature-file/SKILL.md](skills/06-quality/qa-analyst/design/bdd-feature-file/SKILL.md)

**Design API tests** · `api-test-design`

- When: Contract, status codes, auth, validation, negative cases
- File: [skills/06-quality/qa-analyst/design/api-test-design/SKILL.md](skills/06-quality/qa-analyst/design/api-test-design/SKILL.md)

#### Execution & Defects

**Write a bug report** · `bug-report`

- When: Title, steps, expected/actual, environment, evidence, severity
- File: [skills/06-quality/qa-analyst/execution/bug-report/SKILL.md](skills/06-quality/qa-analyst/execution/bug-report/SKILL.md)

**Triage bugs** · `bug-triage`

- When: Severity vs priority, duplicates, assignment
- File: [skills/06-quality/qa-analyst/execution/bug-triage/SKILL.md](skills/06-quality/qa-analyst/execution/bug-triage/SKILL.md)

**Select regression tests** · `regression-selection`

- When: Pick tests based on change impact
- File: [skills/06-quality/qa-analyst/execution/regression-selection/SKILL.md](skills/06-quality/qa-analyst/execution/regression-selection/SKILL.md)

**Write a test summary report** · `test-summary-report`

- When: Coverage, results, defects, residual risk, recommendation
- File: [skills/06-quality/qa-analyst/execution/test-summary-report/SKILL.md](skills/06-quality/qa-analyst/execution/test-summary-report/SKILL.md)

**Evaluate release readiness** · `release-quality-gate`

- When: Go/no-go assessment against exit criteria
- File: [skills/06-quality/qa-analyst/execution/release-quality-gate/SKILL.md](skills/06-quality/qa-analyst/execution/release-quality-gate/SKILL.md)

**Analyze defect trends** · `defect-trend-analysis`

- When: Density, leakage, root cause categories
- File: [skills/06-quality/qa-analyst/execution/defect-trend-analysis/SKILL.md](skills/06-quality/qa-analyst/execution/defect-trend-analysis/SKILL.md)

#### User Acceptance

**Plan UAT** · `uat-plan`

- When: Participants, scenarios, schedule, sign-off
- File: [skills/06-quality/qa-analyst/uat/uat-plan/SKILL.md](skills/06-quality/qa-analyst/uat/uat-plan/SKILL.md)

**Write UAT scenarios** · `uat-scenarios`

- When: Business-language end-to-end scenarios
- File: [skills/06-quality/qa-analyst/uat/uat-scenarios/SKILL.md](skills/06-quality/qa-analyst/uat/uat-scenarios/SKILL.md)

### Test Automation Engineer

#### Automation

**Select automation candidates** · `automation-candidate-selection`

- When: ROI-based selection of what to automate
- File: [skills/06-quality/automation-engineer/automation/automation-candidate-selection/SKILL.md](skills/06-quality/automation-engineer/automation/automation-candidate-selection/SKILL.md)

**Write an automated test** · `test-automation-script`

- When: Framework-agnostic page/API object test code
- File: [skills/06-quality/automation-engineer/automation/test-automation-script/SKILL.md](skills/06-quality/automation-engineer/automation/test-automation-script/SKILL.md)

**Analyze flaky tests** · `flaky-test-analysis`

- When: Classify causes and propose stabilizations
- File: [skills/06-quality/automation-engineer/automation/flaky-test-analysis/SKILL.md](skills/06-quality/automation-engineer/automation/flaky-test-analysis/SKILL.md)

**Design a test automation framework** · `automation-framework-design`

- When: Layers, patterns, reporting, CI integration
- File: [skills/06-quality/automation-engineer/automation/automation-framework-design/SKILL.md](skills/06-quality/automation-engineer/automation/automation-framework-design/SKILL.md)

### Performance Test Engineer

#### Performance Testing

**Write a performance test plan** · `performance-test-plan`

- When: Workload model, scenarios, SLAs, environment
- File: [skills/06-quality/performance-engineer/performance/performance-test-plan/SKILL.md](skills/06-quality/performance-engineer/performance/performance-test-plan/SKILL.md)

**Analyze load test results** · `load-test-analysis`

- When: Throughput, latency percentiles, errors, bottlenecks
- File: [skills/06-quality/performance-engineer/performance/load-test-analysis/SKILL.md](skills/06-quality/performance-engineer/performance/load-test-analysis/SKILL.md)

**Write a capacity report** · `capacity-test-report`

- When: Max sustainable load and headroom
- File: [skills/06-quality/performance-engineer/performance/capacity-test-report/SKILL.md](skills/06-quality/performance-engineer/performance/capacity-test-report/SKILL.md)

## DevOps, SRE & Platform

### DevOps / Platform Engineer

#### CI/CD

**Design a CI/CD pipeline** · `pipeline-design`

- When: Stages, gates, artifacts, environments, promotion
- File: [skills/07-devops-sre/devops-engineer/cicd/pipeline-design/SKILL.md](skills/07-devops-sre/devops-engineer/cicd/pipeline-design/SKILL.md)

**Triage a pipeline failure** · `pipeline-failure-triage`

- When: Read logs, find cause, propose fix
- File: [skills/07-devops-sre/devops-engineer/cicd/pipeline-failure-triage/SKILL.md](skills/07-devops-sre/devops-engineer/cicd/pipeline-failure-triage/SKILL.md)

**Choose a deployment strategy** · `deployment-strategy`

- When: Blue-green, canary, rolling, feature flags
- File: [skills/07-devops-sre/devops-engineer/cicd/deployment-strategy/SKILL.md](skills/07-devops-sre/devops-engineer/cicd/deployment-strategy/SKILL.md)

**Define environment strategy** · `environment-strategy`

- When: Env purposes, parity, data, access
- File: [skills/07-devops-sre/devops-engineer/cicd/environment-strategy/SKILL.md](skills/07-devops-sre/devops-engineer/cicd/environment-strategy/SKILL.md)

#### Infrastructure & Containers

**Review a Dockerfile** · `dockerfile-review`

- When: Size, layers, security, reproducibility
- File: [skills/07-devops-sre/devops-engineer/infrastructure/dockerfile-review/SKILL.md](skills/07-devops-sre/devops-engineer/infrastructure/dockerfile-review/SKILL.md)

**Review Kubernetes manifests** · `kubernetes-manifest-review`

- When: Resources, probes, security context, HA
- File: [skills/07-devops-sre/devops-engineer/infrastructure/kubernetes-manifest-review/SKILL.md](skills/07-devops-sre/devops-engineer/infrastructure/kubernetes-manifest-review/SKILL.md)

**Review infrastructure as code** · `iac-review`

- When: Terraform/Bicep/etc. for security, drift, modularity
- File: [skills/07-devops-sre/devops-engineer/infrastructure/iac-review/SKILL.md](skills/07-devops-sre/devops-engineer/infrastructure/iac-review/SKILL.md)

**Plan secrets management** · `secrets-management-plan`

- When: Vaults, rotation, injection, least privilege
- File: [skills/07-devops-sre/devops-engineer/infrastructure/secrets-management-plan/SKILL.md](skills/07-devops-sre/devops-engineer/infrastructure/secrets-management-plan/SKILL.md)

**Review cloud cost** · `finops-review`

- When: Waste, rightsizing, commitments, tagging
- File: [skills/07-devops-sre/devops-engineer/infrastructure/finops-review/SKILL.md](skills/07-devops-sre/devops-engineer/infrastructure/finops-review/SKILL.md)

### Release Manager

#### Release Management

**Write a release plan** · `release-plan`

- When: Contents, schedule, owners, comms, rollback
- File: [skills/07-devops-sre/release-manager/release/release-plan/SKILL.md](skills/07-devops-sre/release-manager/release/release-plan/SKILL.md)

**Write release notes** · `release-notes`

- When: Features, fixes, breaking changes, known issues
- File: [skills/07-devops-sre/release-manager/release/release-notes/SKILL.md](skills/07-devops-sre/release-manager/release/release-notes/SKILL.md)

**Build a deployment checklist** · `deployment-checklist`

- When: Pre, during, post deployment checks
- File: [skills/07-devops-sre/release-manager/release/deployment-checklist/SKILL.md](skills/07-devops-sre/release-manager/release/deployment-checklist/SKILL.md)

**Write a rollback plan** · `rollback-plan`

- When: Triggers, steps, data considerations, verification
- File: [skills/07-devops-sre/release-manager/release/rollback-plan/SKILL.md](skills/07-devops-sre/release-manager/release/rollback-plan/SKILL.md)

**Run a go/no-go decision** · `go-no-go`

- When: Criteria, evidence, decision record
- File: [skills/07-devops-sre/release-manager/release/go-no-go/SKILL.md](skills/07-devops-sre/release-manager/release/go-no-go/SKILL.md)

**Decide a version number** · `semantic-versioning`

- When: Apply SemVer from change list
- File: [skills/07-devops-sre/release-manager/release/semantic-versioning/SKILL.md](skills/07-devops-sre/release-manager/release/semantic-versioning/SKILL.md)

### Site Reliability Engineer

#### Reliability

**Define SLIs and SLOs** · `slo-definition`

- When: User-centric indicators, targets, windows
- File: [skills/07-devops-sre/sre/reliability/slo-definition/SKILL.md](skills/07-devops-sre/sre/reliability/slo-definition/SKILL.md)

**Write an error budget policy** · `error-budget-policy`

- When: Actions when budget burns
- File: [skills/07-devops-sre/sre/reliability/error-budget-policy/SKILL.md](skills/07-devops-sre/sre/reliability/error-budget-policy/SKILL.md)

**Design alerts** · `alert-design`

- When: Symptom-based, actionable, burn-rate alerts
- File: [skills/07-devops-sre/sre/reliability/alert-design/SKILL.md](skills/07-devops-sre/sre/reliability/alert-design/SKILL.md)

**Plan observability** · `observability-plan`

- When: Logs, metrics, traces, dashboards per service
- File: [skills/07-devops-sre/sre/reliability/observability-plan/SKILL.md](skills/07-devops-sre/sre/reliability/observability-plan/SKILL.md)

**Plan capacity** · `capacity-planning`

- When: Forecast demand and resources with headroom
- File: [skills/07-devops-sre/sre/reliability/capacity-planning/SKILL.md](skills/07-devops-sre/sre/reliability/capacity-planning/SKILL.md)

**Design a chaos experiment** · `chaos-experiment`

- When: Hypothesis, blast radius, abort conditions
- File: [skills/07-devops-sre/sre/reliability/chaos-experiment/SKILL.md](skills/07-devops-sre/sre/reliability/chaos-experiment/SKILL.md)

**Write a disaster recovery plan** · `dr-plan`

- When: RTO/RPO, scenarios, procedures, tests
- File: [skills/07-devops-sre/sre/reliability/dr-plan/SKILL.md](skills/07-devops-sre/sre/reliability/dr-plan/SKILL.md)

#### Incident Management

**Write a runbook** · `runbook`

- When: Symptom, diagnosis, remediation, escalation
- File: [skills/07-devops-sre/sre/incident/runbook/SKILL.md](skills/07-devops-sre/sre/incident/runbook/SKILL.md)

**Run incident response** · `incident-response`

- When: Roles, severity, timeline, mitigation steps
- File: [skills/07-devops-sre/sre/incident/incident-response/SKILL.md](skills/07-devops-sre/sre/incident/incident-response/SKILL.md)

**Write incident communications** · `incident-communication`

- When: Internal and status-page updates per phase
- File: [skills/07-devops-sre/sre/incident/incident-communication/SKILL.md](skills/07-devops-sre/sre/incident/incident-communication/SKILL.md)

**Write a blameless postmortem** · `postmortem`

- When: Timeline, impact, root causes, actions
- File: [skills/07-devops-sre/sre/incident/postmortem/SKILL.md](skills/07-devops-sre/sre/incident/postmortem/SKILL.md)

**Write an on-call handover** · `on-call-handover`

- When: Open incidents, risks, changes, watch items
- File: [skills/07-devops-sre/sre/incident/on-call-handover/SKILL.md](skills/07-devops-sre/sre/incident/on-call-handover/SKILL.md)

## Data & AI

### Data Architect

#### Data Modeling

**Build a conceptual data model** · `conceptual-data-model`

- When: Entities and relationships in business language
- File: [skills/08-data/data-architect/modeling/conceptual-data-model/SKILL.md](skills/08-data/data-architect/modeling/conceptual-data-model/SKILL.md)

**Build a logical data model** · `logical-data-model`

- When: Normalized entities, attributes, keys
- File: [skills/08-data/data-architect/modeling/logical-data-model/SKILL.md](skills/08-data/data-architect/modeling/logical-data-model/SKILL.md)

**Design a dimensional model** · `dimensional-model`

- When: Facts, dimensions, grain, SCD types
- File: [skills/08-data/data-architect/modeling/dimensional-model/SKILL.md](skills/08-data/data-architect/modeling/dimensional-model/SKILL.md)

**Design a Data Vault model** · `data-vault-model`

- When: Hubs, links, satellites
- File: [skills/08-data/data-architect/modeling/data-vault-model/SKILL.md](skills/08-data/data-architect/modeling/data-vault-model/SKILL.md)

**Design a data platform** · `data-platform-architecture`

- When: Lakehouse/warehouse/mesh layers and flows
- File: [skills/08-data/data-architect/modeling/data-platform-architecture/SKILL.md](skills/08-data/data-architect/modeling/data-platform-architecture/SKILL.md)

**Write a data contract** · `data-contract`

- When: Schema, semantics, SLAs, ownership, versioning
- File: [skills/08-data/data-architect/modeling/data-contract/SKILL.md](skills/08-data/data-architect/modeling/data-contract/SKILL.md)

#### Data Governance

**Write a data catalog entry** · `data-catalog-entry`

- When: Description, owner, lineage, quality, sensitivity
- File: [skills/08-data/data-architect/governance/data-catalog-entry/SKILL.md](skills/08-data/data-architect/governance/data-catalog-entry/SKILL.md)

**Classify data sensitivity** · `data-classification`

- When: PII/special category tagging (KVKK/GDPR)
- File: [skills/08-data/data-architect/governance/data-classification/SKILL.md](skills/08-data/data-architect/governance/data-classification/SKILL.md)

**Define data quality rules** · `data-quality-rules`

- When: Completeness, validity, uniqueness, timeliness checks
- File: [skills/08-data/data-architect/governance/data-quality-rules/SKILL.md](skills/08-data/data-architect/governance/data-quality-rules/SKILL.md)

**Document data lineage** · `data-lineage-doc`

- When: Source to consumption flow with transformations
- File: [skills/08-data/data-architect/governance/data-lineage-doc/SKILL.md](skills/08-data/data-architect/governance/data-lineage-doc/SKILL.md)

**Define master data management** · `master-data-strategy`

- When: Golden record, match/merge, stewardship
- File: [skills/08-data/data-architect/governance/master-data-strategy/SKILL.md](skills/08-data/data-architect/governance/master-data-strategy/SKILL.md)

**Define data retention** · `retention-policy`

- When: Retention periods, archival, deletion rules
- File: [skills/08-data/data-architect/governance/retention-policy/SKILL.md](skills/08-data/data-architect/governance/retention-policy/SKILL.md)

### Data Engineer

#### Data Pipelines

**Specify a data pipeline** · `pipeline-spec`

- When: Sources, schedule, transformations, targets, SLAs
- File: [skills/08-data/data-engineer/pipelines/pipeline-spec/SKILL.md](skills/08-data/data-engineer/pipelines/pipeline-spec/SKILL.md)

**Write a source-to-target mapping** · `source-to-target-mapping`

- When: Column-level mapping with transformation logic
- File: [skills/08-data/data-engineer/pipelines/source-to-target-mapping/SKILL.md](skills/08-data/data-engineer/pipelines/source-to-target-mapping/SKILL.md)

**Design incremental loads** · `incremental-load-design`

- When: CDC, watermarks, idempotency, late data
- File: [skills/08-data/data-engineer/pipelines/incremental-load-design/SKILL.md](skills/08-data/data-engineer/pipelines/incremental-load-design/SKILL.md)

**Analyze a data pipeline failure** · `pipeline-failure-analysis`

- When: Root cause, data impact, backfill plan
- File: [skills/08-data/data-engineer/pipelines/pipeline-failure-analysis/SKILL.md](skills/08-data/data-engineer/pipelines/pipeline-failure-analysis/SKILL.md)

**Plan schema evolution** · `schema-evolution-plan`

- When: Backward/forward compatible changes and migration
- File: [skills/08-data/data-engineer/pipelines/schema-evolution-plan/SKILL.md](skills/08-data/data-engineer/pipelines/schema-evolution-plan/SKILL.md)

### Database Administrator

#### Database Operations

**Optimize a slow query** · `query-optimization`

- When: Read execution plan and propose rewrites/indexes
- File: [skills/08-data/dba/database/query-optimization/SKILL.md](skills/08-data/dba/database/query-optimization/SKILL.md)

**Recommend indexes** · `index-recommendation`

- When: Workload-based indexes with write-cost trade-off
- File: [skills/08-data/dba/database/index-recommendation/SKILL.md](skills/08-data/dba/database/index-recommendation/SKILL.md)

**Plan a schema migration** · `schema-migration-plan`

- When: Zero-downtime steps, rollback, verification
- File: [skills/08-data/dba/database/schema-migration-plan/SKILL.md](skills/08-data/dba/database/schema-migration-plan/SKILL.md)

**Plan backup and restore** · `backup-restore-plan`

- When: Frequency, retention, restore tests, RPO/RTO
- File: [skills/08-data/dba/database/backup-restore-plan/SKILL.md](skills/08-data/dba/database/backup-restore-plan/SKILL.md)

**Run a database health check** · `database-health-check`

- When: Waits, locks, growth, fragmentation, config
- File: [skills/08-data/dba/database/database-health-check/SKILL.md](skills/08-data/dba/database/database-health-check/SKILL.md)

### Data / BI Analyst

#### Analytics & Reporting

**Write an analysis plan** · `analysis-plan`

- When: Question, hypotheses, data, method, output
- File: [skills/08-data/data-analyst/analytics/analysis-plan/SKILL.md](skills/08-data/data-analyst/analytics/analysis-plan/SKILL.md)

**Specify a dashboard** · `dashboard-spec`

- When: Audience, questions, KPIs, visuals, filters
- File: [skills/08-data/data-analyst/analytics/dashboard-spec/SKILL.md](skills/08-data/data-analyst/analytics/dashboard-spec/SKILL.md)

**Write an insight summary** · `insight-summary`

- When: So-what narrative from data results
- File: [skills/08-data/data-analyst/analytics/insight-summary/SKILL.md](skills/08-data/data-analyst/analytics/insight-summary/SKILL.md)

**Define a metric precisely** · `metric-definition`

- When: Formula, filters, grain, edge cases
- File: [skills/08-data/data-analyst/analytics/metric-definition/SKILL.md](skills/08-data/data-analyst/analytics/metric-definition/SKILL.md)

**Explore a dataset** · `data-exploration`

- When: Profile distributions, nulls, outliers, correlations
- File: [skills/08-data/data-analyst/analytics/data-exploration/SKILL.md](skills/08-data/data-analyst/analytics/data-exploration/SKILL.md)

**Analyze an A/B test** · `ab-test-analysis`

- When: Significance, effect size, guardrails, decision
- File: [skills/08-data/data-analyst/analytics/ab-test-analysis/SKILL.md](skills/08-data/data-analyst/analytics/ab-test-analysis/SKILL.md)

### Data Scientist / ML & AI Engineer

#### Machine Learning

**Frame an ML problem** · `ml-problem-framing`

- When: Target, features, success metric, baseline, feasibility
- File: [skills/08-data/ml-ai-engineer/ml/ml-problem-framing/SKILL.md](skills/08-data/ml-ai-engineer/ml/ml-problem-framing/SKILL.md)

**Plan feature engineering** · `feature-engineering-plan`

- When: Candidate features, leakage checks, transformations
- File: [skills/08-data/ml-ai-engineer/ml/feature-engineering-plan/SKILL.md](skills/08-data/ml-ai-engineer/ml/feature-engineering-plan/SKILL.md)

**Write a model evaluation report** · `model-evaluation-report`

- When: Metrics, slices, errors, fairness, comparison
- File: [skills/08-data/ml-ai-engineer/ml/model-evaluation-report/SKILL.md](skills/08-data/ml-ai-engineer/ml/model-evaluation-report/SKILL.md)

**Write a model card** · `model-card`

- When: Intended use, data, performance, limits, ethics
- File: [skills/08-data/ml-ai-engineer/ml/model-card/SKILL.md](skills/08-data/ml-ai-engineer/ml/model-card/SKILL.md)

**Plan model monitoring** · `ml-monitoring-plan`

- When: Drift, performance decay, retraining triggers
- File: [skills/08-data/ml-ai-engineer/ml/ml-monitoring-plan/SKILL.md](skills/08-data/ml-ai-engineer/ml/ml-monitoring-plan/SKILL.md)

#### Generative AI

**Design a prompt** · `prompt-design`

- When: Role, task, context, constraints, examples, output format
- File: [skills/08-data/ml-ai-engineer/genai/prompt-design/SKILL.md](skills/08-data/ml-ai-engineer/genai/prompt-design/SKILL.md)

**Build an LLM evaluation set** · `llm-eval-set`

- When: Test cases, rubrics and graders for an LLM feature
- File: [skills/08-data/ml-ai-engineer/genai/llm-eval-set/SKILL.md](skills/08-data/ml-ai-engineer/genai/llm-eval-set/SKILL.md)

**Design a RAG system** · `rag-design`

- When: Chunking, embedding, retrieval, reranking, grounding
- File: [skills/08-data/ml-ai-engineer/genai/rag-design/SKILL.md](skills/08-data/ml-ai-engineer/genai/rag-design/SKILL.md)

**Author a new AI skill** · `ai-skill-authoring`

- When: Write a portable SKILL.md following this library's conventions
- File: [skills/08-data/ml-ai-engineer/genai/ai-skill-authoring/SKILL.md](skills/08-data/ml-ai-engineer/genai/ai-skill-authoring/SKILL.md)

**Assess an AI use case** · `ai-use-case-assessment`

- When: Value, feasibility, risk, data readiness
- File: [skills/08-data/ml-ai-engineer/genai/ai-use-case-assessment/SKILL.md](skills/08-data/ml-ai-engineer/genai/ai-use-case-assessment/SKILL.md)

## Security & Compliance

### Security Architect / AppSec Engineer

#### Secure Design

**Build a threat model** · `threat-model`

- When: STRIDE per element with mitigations
- File: [skills/09-security/security-engineer/design/threat-model/SKILL.md](skills/09-security/security-engineer/design/threat-model/SKILL.md)

**Define security requirements** · `security-requirements`

- When: OWASP ASVS aligned requirements
- File: [skills/09-security/security-engineer/design/security-requirements/SKILL.md](skills/09-security/security-engineer/design/security-requirements/SKILL.md)

**Design authentication and authorization** · `authn-authz-design`

- When: Flows, tokens, roles/claims, least privilege
- File: [skills/09-security/security-engineer/design/authn-authz-design/SKILL.md](skills/09-security/security-engineer/design/authn-authz-design/SKILL.md)

#### Security Assessment

**Review code for security** · `secure-code-review`

- When: OWASP Top 10 and CWE focused review
- File: [skills/09-security/security-engineer/assessment/secure-code-review/SKILL.md](skills/09-security/security-engineer/assessment/secure-code-review/SKILL.md)

**Triage a vulnerability** · `vulnerability-triage`

- When: CVSS, exploitability, reachability, fix plan
- File: [skills/09-security/security-engineer/assessment/vulnerability-triage/SKILL.md](skills/09-security/security-engineer/assessment/vulnerability-triage/SKILL.md)

**Review dependency vulnerabilities** · `dependency-vulnerability-review`

- When: SCA findings, upgrade paths, risk acceptance
- File: [skills/09-security/security-engineer/assessment/dependency-vulnerability-review/SKILL.md](skills/09-security/security-engineer/assessment/dependency-vulnerability-review/SKILL.md)

**Define a penetration test scope** · `pentest-scope`

- When: Targets, rules of engagement, exclusions, reporting
- File: [skills/09-security/security-engineer/assessment/pentest-scope/SKILL.md](skills/09-security/security-engineer/assessment/pentest-scope/SKILL.md)

**Write a security finding** · `security-finding-report`

- When: Description, impact, reproduction, remediation
- File: [skills/09-security/security-engineer/assessment/security-finding-report/SKILL.md](skills/09-security/security-engineer/assessment/security-finding-report/SKILL.md)

#### Security Operations

**Respond to a security incident** · `security-incident-response`

- When: Contain, eradicate, recover, notify
- File: [skills/09-security/security-engineer/operations/security-incident-response/SKILL.md](skills/09-security/security-engineer/operations/security-incident-response/SKILL.md)

**Run an access review** · `access-review`

- When: Detect excessive, orphaned and toxic permissions
- File: [skills/09-security/security-engineer/operations/access-review/SKILL.md](skills/09-security/security-engineer/operations/access-review/SKILL.md)

### GRC / Compliance

#### Compliance

**Run a privacy impact assessment** · `privacy-impact-assessment`

- When: KVKK/GDPR DPIA for a feature or system
- File: [skills/09-security/compliance/compliance/privacy-impact-assessment/SKILL.md](skills/09-security/compliance/compliance/privacy-impact-assessment/SKILL.md)

**Map controls to a standard** · `control-mapping`

- When: ISO 27001 / SOC 2 control evidence mapping
- File: [skills/09-security/compliance/compliance/control-mapping/SKILL.md](skills/09-security/compliance/compliance/control-mapping/SKILL.md)

**Write a security/IT policy** · `policy-writing`

- When: Purpose, scope, rules, roles, exceptions
- File: [skills/09-security/compliance/compliance/policy-writing/SKILL.md](skills/09-security/compliance/compliance/policy-writing/SKILL.md)

**Prepare for an audit** · `audit-preparation`

- When: Evidence list, gaps, owners, timeline
- File: [skills/09-security/compliance/compliance/audit-preparation/SKILL.md](skills/09-security/compliance/compliance/audit-preparation/SKILL.md)

**Assess IT risk** · `it-risk-assessment`

- When: Asset, threat, vulnerability, likelihood, impact
- File: [skills/09-security/compliance/compliance/it-risk-assessment/SKILL.md](skills/09-security/compliance/compliance/it-risk-assessment/SKILL.md)

## UX / UI Design

### UX Researcher

#### User Research

**Write a research plan** · `research-plan`

- When: Objectives, questions, methods, participants, timeline
- File: [skills/10-design/ux-researcher/research/research-plan/SKILL.md](skills/10-design/ux-researcher/research/research-plan/SKILL.md)

**Write a usability test script** · `usability-test-script`

- When: Tasks, prompts, success criteria, debrief
- File: [skills/10-design/ux-researcher/research/usability-test-script/SKILL.md](skills/10-design/ux-researcher/research/usability-test-script/SKILL.md)

**Synthesize research findings** · `research-synthesis`

- When: Affinity clustering into insights and recommendations
- File: [skills/10-design/ux-researcher/research/research-synthesis/SKILL.md](skills/10-design/ux-researcher/research/research-synthesis/SKILL.md)

**Write a participant screener** · `screener-survey`

- When: Criteria and questions to recruit the right users
- File: [skills/10-design/ux-researcher/research/screener-survey/SKILL.md](skills/10-design/ux-researcher/research/screener-survey/SKILL.md)

### UX / UI Designer

#### Interaction & Visual Design

**Design a user flow** · `user-flow`

- When: Steps, decisions, entry/exit, error paths
- File: [skills/10-design/ux-ui-designer/design/user-flow/SKILL.md](skills/10-design/ux-ui-designer/design/user-flow/SKILL.md)

**Structure information architecture** · `information-architecture`

- When: Navigation, hierarchy, labeling, card sort plan
- File: [skills/10-design/ux-ui-designer/design/information-architecture/SKILL.md](skills/10-design/ux-ui-designer/design/information-architecture/SKILL.md)

**Describe a wireframe** · `wireframe-spec`

- When: Layout, components, content priority, states
- File: [skills/10-design/ux-ui-designer/design/wireframe-spec/SKILL.md](skills/10-design/ux-ui-designer/design/wireframe-spec/SKILL.md)

**Run a heuristic evaluation** · `heuristic-evaluation`

- When: Nielsen's 10 heuristics with severity
- File: [skills/10-design/ux-ui-designer/design/heuristic-evaluation/SKILL.md](skills/10-design/ux-ui-designer/design/heuristic-evaluation/SKILL.md)

**Give design critique** · `design-critique`

- When: Goal-based, specific, prioritized feedback
- File: [skills/10-design/ux-ui-designer/design/design-critique/SKILL.md](skills/10-design/ux-ui-designer/design/design-critique/SKILL.md)

**Specify a design system component** · `design-system-component-spec`

- When: Anatomy, variants, states, tokens, usage rules
- File: [skills/10-design/ux-ui-designer/design/design-system-component-spec/SKILL.md](skills/10-design/ux-ui-designer/design/design-system-component-spec/SKILL.md)

**Prepare a design handoff** · `design-handoff`

- When: Specs, interactions, edge states, assets for developers
- File: [skills/10-design/ux-ui-designer/design/design-handoff/SKILL.md](skills/10-design/ux-ui-designer/design/design-handoff/SKILL.md)

### UX Writer / Content Designer

#### Content

**Write microcopy** · `microcopy`

- When: Buttons, labels, hints, empty states
- File: [skills/10-design/ux-writer/content/microcopy/SKILL.md](skills/10-design/ux-writer/content/microcopy/SKILL.md)

**Write error messages** · `error-message-writing`

- When: What happened, why, what to do next
- File: [skills/10-design/ux-writer/content/error-message-writing/SKILL.md](skills/10-design/ux-writer/content/error-message-writing/SKILL.md)

**Write a voice and tone guide** · `voice-and-tone-guide`

- When: Brand voice principles with do/don't examples
- File: [skills/10-design/ux-writer/content/voice-and-tone-guide/SKILL.md](skills/10-design/ux-writer/content/voice-and-tone-guide/SKILL.md)

## Support & IT Operations

### Support Engineer (L1-L3)

#### Ticket Handling

**Triage a support ticket** · `ticket-triage`

- When: Category, priority, impact, routing
- File: [skills/11-support-ops/support-engineer/tickets/ticket-triage/SKILL.md](skills/11-support-ops/support-engineer/tickets/ticket-triage/SKILL.md)

**Write a ticket response** · `ticket-response`

- When: Empathetic, clear, next-step focused reply
- File: [skills/11-support-ops/support-engineer/tickets/ticket-response/SKILL.md](skills/11-support-ops/support-engineer/tickets/ticket-response/SKILL.md)

**Summarize a ticket for escalation** · `ticket-escalation-summary`

- When: Context, attempts, evidence for next level
- File: [skills/11-support-ops/support-engineer/tickets/ticket-escalation-summary/SKILL.md](skills/11-support-ops/support-engineer/tickets/ticket-escalation-summary/SKILL.md)

**Write a known error article** · `known-error-article`

- When: Symptom, cause, workaround, fix status
- File: [skills/11-support-ops/support-engineer/tickets/known-error-article/SKILL.md](skills/11-support-ops/support-engineer/tickets/known-error-article/SKILL.md)

**Write a customer outage notice** · `customer-outage-notice`

- When: Impact, status, ETA, workaround
- File: [skills/11-support-ops/support-engineer/tickets/customer-outage-notice/SKILL.md](skills/11-support-ops/support-engineer/tickets/customer-outage-notice/SKILL.md)

### IT Service Management

#### ITSM Processes

**Run problem management** · `problem-management`

- When: Link incidents, find root cause, known error
- File: [skills/11-support-ops/it-service-management/itsm/problem-management/SKILL.md](skills/11-support-ops/it-service-management/itsm/problem-management/SKILL.md)

**Write a change request (RFC)** · `change-request-rfc`

- When: Description, risk, backout, schedule for CAB
- File: [skills/11-support-ops/it-service-management/itsm/change-request-rfc/SKILL.md](skills/11-support-ops/it-service-management/itsm/change-request-rfc/SKILL.md)

**Analyze SLA breaches** · `sla-breach-analysis`

- When: Patterns, causes, improvement actions
- File: [skills/11-support-ops/it-service-management/itsm/sla-breach-analysis/SKILL.md](skills/11-support-ops/it-service-management/itsm/sla-breach-analysis/SKILL.md)

**Write a service catalog entry** · `service-catalog-entry`

- When: Service description, SLAs, request process
- File: [skills/11-support-ops/it-service-management/itsm/service-catalog-entry/SKILL.md](skills/11-support-ops/it-service-management/itsm/service-catalog-entry/SKILL.md)

## Technical Writing

### Technical Writer

#### Product Documentation

**Write a user guide** · `user-guide`

- When: Task-based guide with steps and screenshots placeholders
- File: [skills/12-technical-writing/technical-writer/docs/user-guide/SKILL.md](skills/12-technical-writing/technical-writer/docs/user-guide/SKILL.md)

**Write a tutorial** · `tutorial`

- When: Learning-oriented step-by-step walkthrough (Diátaxis)
- File: [skills/12-technical-writing/technical-writer/docs/tutorial/SKILL.md](skills/12-technical-writing/technical-writer/docs/tutorial/SKILL.md)

**Write a how-to guide** · `how-to-guide`

- When: Goal-oriented recipe (Diátaxis)
- File: [skills/12-technical-writing/technical-writer/docs/how-to-guide/SKILL.md](skills/12-technical-writing/technical-writer/docs/how-to-guide/SKILL.md)

**Structure documentation** · `docs-information-architecture`

- When: Organize docs into tutorials, how-tos, reference, explanation
- File: [skills/12-technical-writing/technical-writer/docs/docs-information-architecture/SKILL.md](skills/12-technical-writing/technical-writer/docs/docs-information-architecture/SKILL.md)

**Check against a style guide** · `style-guide-check`

- When: Consistency with terminology and writing rules
- File: [skills/12-technical-writing/technical-writer/docs/style-guide-check/SKILL.md](skills/12-technical-writing/technical-writer/docs/style-guide-check/SKILL.md)

## Engineering Management & Leadership

### Engineering Manager

#### People Management

**Prepare a 1:1** · `one-on-one-prep`

- When: Prepares a focused 1:1 meeting plan with a direct report, including follow-ups from the previous session, report-owned topics, open coaching questions and signals to watch. Use when a manager has an upcoming 1:1, wants to structure a recurring 1:1, or needs to prepare for a harder conversation (feedback, workload, career, morale).
- Try: _"Prepare my 1:1 with Ayşe tomorrow. Last time she said she felt stuck on the billing migration and wanted more design ownership."_
- Related: `one-on-one-notes`, `feedback-sbi`, `career-development-plan`, `goal-setting`, `conflict-resolution`
- File: [skills/13-leadership/engineering-manager/people/one-on-one-prep/SKILL.md](skills/13-leadership/engineering-manager/people/one-on-one-prep/SKILL.md)

**Capture 1:1 notes** · `one-on-one-notes`

- When: Topics, commitments, career signals
- File: [skills/13-leadership/engineering-manager/people/one-on-one-notes/SKILL.md](skills/13-leadership/engineering-manager/people/one-on-one-notes/SKILL.md)

**Write a performance review** · `performance-review`

- When: Evidence-based, competency-aligned, balanced
- File: [skills/13-leadership/engineering-manager/people/performance-review/SKILL.md](skills/13-leadership/engineering-manager/people/performance-review/SKILL.md)

**Set individual goals** · `goal-setting`

- When: SMART goals tied to team outcomes and growth
- File: [skills/13-leadership/engineering-manager/people/goal-setting/SKILL.md](skills/13-leadership/engineering-manager/people/goal-setting/SKILL.md)

**Write a career development plan** · `career-development-plan`

- When: Current vs target level, gaps, actions
- File: [skills/13-leadership/engineering-manager/people/career-development-plan/SKILL.md](skills/13-leadership/engineering-manager/people/career-development-plan/SKILL.md)

**Write a performance improvement plan** · `underperformance-plan`

- When: Expectations, support, milestones, consequences
- File: [skills/13-leadership/engineering-manager/people/underperformance-plan/SKILL.md](skills/13-leadership/engineering-manager/people/underperformance-plan/SKILL.md)

**Write a recognition message** · `recognition-message`

- When: Specific, impact-focused appreciation
- File: [skills/13-leadership/engineering-manager/people/recognition-message/SKILL.md](skills/13-leadership/engineering-manager/people/recognition-message/SKILL.md)

#### Hiring

**Write a job description** · `job-description`

- When: Role mission, responsibilities, requirements, inclusive language
- File: [skills/13-leadership/engineering-manager/hiring/job-description/SKILL.md](skills/13-leadership/engineering-manager/hiring/job-description/SKILL.md)

**Design an interview loop** · `interview-plan`

- When: Stages, competencies per stage, interviewers
- File: [skills/13-leadership/engineering-manager/hiring/interview-plan/SKILL.md](skills/13-leadership/engineering-manager/hiring/interview-plan/SKILL.md)

**Prepare technical interview questions** · `technical-interview-questions`

- When: Level-calibrated questions with rubric
- File: [skills/13-leadership/engineering-manager/hiring/technical-interview-questions/SKILL.md](skills/13-leadership/engineering-manager/hiring/technical-interview-questions/SKILL.md)

**Write an interview scorecard** · `interview-scorecard`

- When: Evidence per competency and hire recommendation
- File: [skills/13-leadership/engineering-manager/hiring/interview-scorecard/SKILL.md](skills/13-leadership/engineering-manager/hiring/interview-scorecard/SKILL.md)

**Summarize a candidate debrief** · `candidate-debrief`

- When: Consolidate signals into a decision
- File: [skills/13-leadership/engineering-manager/hiring/candidate-debrief/SKILL.md](skills/13-leadership/engineering-manager/hiring/candidate-debrief/SKILL.md)

**Write a 30-60-90 day onboarding plan** · `onboarding-plan-30-60-90`

- When: Goals and milestones for a new hire
- File: [skills/13-leadership/engineering-manager/hiring/onboarding-plan-30-60-90/SKILL.md](skills/13-leadership/engineering-manager/hiring/onboarding-plan-30-60-90/SKILL.md)

#### Team & Org Design

**Design team topology** · `team-topology`

- When: Stream-aligned, platform, enabling, subsystem teams
- File: [skills/13-leadership/engineering-manager/team/team-topology/SKILL.md](skills/13-leadership/engineering-manager/team/team-topology/SKILL.md)

**Define a role** · `role-definition`

- When: Responsibilities, decision rights, interfaces
- File: [skills/13-leadership/engineering-manager/team/role-definition/SKILL.md](skills/13-leadership/engineering-manager/team/role-definition/SKILL.md)

**Build a career ladder** · `career-ladder`

- When: Levels with expectations per competency
- File: [skills/13-leadership/engineering-manager/team/career-ladder/SKILL.md](skills/13-leadership/engineering-manager/team/career-ladder/SKILL.md)

**Review engineering metrics (DORA/SPACE)** · `engineering-metrics-review`

- When: Interpret delivery metrics without gaming
- File: [skills/13-leadership/engineering-manager/team/engineering-metrics-review/SKILL.md](skills/13-leadership/engineering-manager/team/engineering-metrics-review/SKILL.md)

### CTO / VP / Director

#### Technology Strategy

**Write a technology strategy** · `technology-strategy`

- When: Diagnosis, guiding policy, coherent actions
- File: [skills/13-leadership/executive/strategy/technology-strategy/SKILL.md](skills/13-leadership/executive/strategy/technology-strategy/SKILL.md)

**Run quarterly planning** · `quarterly-planning`

- When: Capacity, priorities, commitments, trade-offs
- File: [skills/13-leadership/executive/strategy/quarterly-planning/SKILL.md](skills/13-leadership/executive/strategy/quarterly-planning/SKILL.md)

**Write a budget proposal** · `budget-proposal`

- When: Investments, run costs, justification, scenarios
- File: [skills/13-leadership/executive/strategy/budget-proposal/SKILL.md](skills/13-leadership/executive/strategy/budget-proposal/SKILL.md)

**Evaluate vendors (RFP)** · `vendor-evaluation`

- When: Requirements, scoring model, comparison, recommendation
- File: [skills/13-leadership/executive/strategy/vendor-evaluation/SKILL.md](skills/13-leadership/executive/strategy/vendor-evaluation/SKILL.md)

**Write an executive/board update** · `board-update`

- When: Highlights, metrics, risks, asks
- File: [skills/13-leadership/executive/strategy/board-update/SKILL.md](skills/13-leadership/executive/strategy/board-update/SKILL.md)

**Communicate an org change** · `org-change-communication`

- When: Why, what changes, what doesn't, support
- File: [skills/13-leadership/executive/strategy/org-change-communication/SKILL.md](skills/13-leadership/executive/strategy/org-change-communication/SKILL.md)

## Presales & Consulting

### Presales / Solution Consultant

#### Bids & Proposals

**Analyze an RFP** · `rfp-analysis`

- When: Requirements, evaluation criteria, risks, bid/no-bid
- File: [skills/14-presales-consulting/presales-consultant/bid/rfp-analysis/SKILL.md](skills/14-presales-consulting/presales-consultant/bid/rfp-analysis/SKILL.md)

**Write an RFP response** · `rfp-response`

- When: Compliant, benefit-led answers per requirement
- File: [skills/14-presales-consulting/presales-consultant/bid/rfp-response/SKILL.md](skills/14-presales-consulting/presales-consultant/bid/rfp-response/SKILL.md)

**Write a proposal** · `proposal-writing`

- When: Understanding, solution, approach, plan, team, commercials
- File: [skills/14-presales-consulting/presales-consultant/bid/proposal-writing/SKILL.md](skills/14-presales-consulting/presales-consultant/bid/proposal-writing/SKILL.md)

**Estimate effort for a bid** · `effort-estimate-for-bid`

- When: Top-down/bottom-up estimate with assumptions and contingency
- File: [skills/14-presales-consulting/presales-consultant/bid/effort-estimate-for-bid/SKILL.md](skills/14-presales-consulting/presales-consultant/bid/effort-estimate-for-bid/SKILL.md)

**Write a statement of work** · `statement-of-work`

- When: Scope, deliverables, acceptance, responsibilities, assumptions
- File: [skills/14-presales-consulting/presales-consultant/bid/statement-of-work/SKILL.md](skills/14-presales-consulting/presales-consultant/bid/statement-of-work/SKILL.md)

#### Consulting

**Run a client discovery workshop** · `discovery-workshop`

- When: Agenda, questions and output for early engagement
- File: [skills/14-presales-consulting/presales-consultant/consulting/discovery-workshop/SKILL.md](skills/14-presales-consulting/presales-consultant/consulting/discovery-workshop/SKILL.md)

**Assess a client's current state** · `current-state-assessment`

- When: Findings, maturity, pain points, recommendations
- File: [skills/14-presales-consulting/presales-consultant/consulting/current-state-assessment/SKILL.md](skills/14-presales-consulting/presales-consultant/consulting/current-state-assessment/SKILL.md)

**Run a fit-gap analysis** · `fit-gap-analysis`

- When: Compare package/standard capabilities to requirements
- File: [skills/14-presales-consulting/presales-consultant/consulting/fit-gap-analysis/SKILL.md](skills/14-presales-consulting/presales-consultant/consulting/fit-gap-analysis/SKILL.md)

**Write a client steering report** · `client-steering-report`

- When: Progress, value delivered, risks, decisions
- File: [skills/14-presales-consulting/presales-consultant/consulting/client-steering-report/SKILL.md](skills/14-presales-consulting/presales-consultant/consulting/client-steering-report/SKILL.md)
