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

- When: Assesses whether a planned meeting is actually needed by testing its goal against async alternatives, and recommends meet, shorten, go async or cancel with a ready-to-use alternative. Use when someone plans a new or recurring meeting, asks \"do we need a meeting for this?\", or wants to cut meeting load.
- Try: _"I want to set up a weekly 1-hour sync with 9 people to share progress on the data migration. Do we really need it?"_
- Related: `meeting-agenda`, `meeting-invite`, `stakeholder-email`, `status-update`, `working-agreement`
- File: [skills/00-shared/meetings/before/meeting-necessity-check/SKILL.md](skills/00-shared/meetings/before/meeting-necessity-check/SKILL.md)

#### During the Meeting

**Take structured meeting notes** · `meeting-notes`

- When: Turns raw meeting notes, chat logs or a transcript into topic-based structured notes that separate discussion points, decisions, action items and open questions, with speakers attributed where it matters. Use when someone shares messy notes or a transcript and asks to \"clean up\", \"structure\" or \"write up\" what was discussed.
- Try: _"Here are my raw notes from today's sprint planning with the platform team. Turn them into structured meeting notes."_
- Related: `transcript-cleanup`, `meeting-summary`, `action-item-extraction`, `decision-log`, `open-questions-tracker`
- File: [skills/00-shared/meetings/during/meeting-notes/SKILL.md](skills/00-shared/meetings/during/meeting-notes/SKILL.md)

**Clean up a meeting transcript** · `transcript-cleanup`

- When: Cleans up a raw or auto-generated meeting transcript by removing filler, false starts and crosstalk, fixing speaker labels and obvious recognition errors, and keeping the meaning and wording intact. Use when a transcript must be made readable, quotable or archivable without turning it into a summary.
- Try: _"Clean up this auto-generated transcript of our vendor call. Speaker 1 is me (Selin), Speaker 2 is the vendor PM."_
- Related: `meeting-notes`, `meeting-minutes`, `meeting-summary`, `glossary-builder`
- File: [skills/00-shared/meetings/during/transcript-cleanup/SKILL.md](skills/00-shared/meetings/during/transcript-cleanup/SKILL.md)

**Facilitate a meeting** · `facilitation-guide`

- When: Produces a facilitator script for a meeting or workshop with a minute-by-minute run sheet, opening and closing words, prompts per agenda item, decision rules, and tactics for dominance, silence, derailment and conflict. Use when someone will run a meeting and wants to lead it confidently, especially decision, alignment or cross-team sessions.
- Try: _"I am facilitating a 90-minute session with product, sales and engineering to agree on Q3 priorities. Give me a facilitation guide."_
- Related: `meeting-agenda`, `conflict-resolution`, `retrospective-facilitation`, `workshop-plan`, `decision-matrix`
- File: [skills/00-shared/meetings/during/facilitation-guide/SKILL.md](skills/00-shared/meetings/during/facilitation-guide/SKILL.md)

#### After the Meeting

**Summarize a meeting** · `meeting-summary`

- When: Produces a short executive summary of a meeting that leads with outcomes, lists decisions, key actions and open points, and flags what needs the reader's attention, readable in under a minute. Use when a manager, sponsor or absent stakeholder needs to know what came out of a meeting without reading full notes or a transcript.
- Try: _"Summarize this 1-hour architecture review transcript for our CTO in a few lines."_
- Related: `meeting-notes`, `meeting-minutes`, `meeting-follow-up`, `executive-summary`, `action-item-extraction`
- File: [skills/00-shared/meetings/after/meeting-summary/SKILL.md](skills/00-shared/meetings/after/meeting-summary/SKILL.md)

**Write formal meeting minutes** · `meeting-minutes`

- When: Produces formal meeting minutes with meeting metadata, attendance and quorum, agenda items in order, concise discussion records, numbered resolutions with voting or approval outcome, actions and approval signatures. Use for steering committees, boards, change advisory boards, audits, contractual or vendor meetings, or whenever the record may be relied on as evidence.
- Try: _"Write formal minutes for yesterday's project steering committee from these notes; two change requests were approved and one deferred."_
- Related: `meeting-notes`, `meeting-summary`, `decision-log`, `steering-committee-pack`, `audit-preparation`
- File: [skills/00-shared/meetings/after/meeting-minutes/SKILL.md](skills/00-shared/meetings/after/meeting-minutes/SKILL.md)

**Extract action items** · `action-item-extraction`

- When: Finds every explicit and implicit commitment in meeting notes, transcripts, emails or chat threads and turns each into a verifiable action item with a single owner, due date, status and source reference, flagging missing owners or dates. Use when someone asks \"what are the action items?\", \"who does what?\", or needs tasks ready for a tracker after a meeting or discussion.
- Try: _"Extract all action items from this transcript of our release readiness call and put them in a table."_
- Related: `meeting-notes`, `meeting-follow-up`, `open-questions-tracker`, `decision-log`, `task-breakdown`
- File: [skills/00-shared/meetings/after/action-item-extraction/SKILL.md](skills/00-shared/meetings/after/action-item-extraction/SKILL.md)

**Record decisions** · `decision-log`

- When: Records decisions from meetings, threads or documents as numbered decision log entries with context, options considered, rationale, decider, date, consequences, reversibility and review trigger, and flags conflicts with earlier decisions. Use when a team needs a durable, searchable record of why something was decided, or when decisions keep being reopened.
- Try: _"Add the decisions from today's data platform meeting to our decision log; we chose Delta Lake over Iceberg and postponed the catalog choice."_
- Related: `adr`, `meeting-minutes`, `meeting-notes`, `trade-off-analysis`, `raid-log`
- File: [skills/00-shared/meetings/after/decision-log/SKILL.md](skills/00-shared/meetings/after/decision-log/SKILL.md)

**Write a meeting follow-up message** · `meeting-follow-up`

- When: Writes the post-meeting follow-up message to attendees and stakeholders with a thank-you line, outcome, decisions, action items with owners and dates, open questions, next meeting and a correction deadline. Use right after a meeting when a recap email or chat message must be sent so everyone leaves with the same understanding and commitments.
- Try: _"Write a follow-up email to the attendees of today's kickoff with the vendor based on these notes."_
- Related: `meeting-summary`, `action-item-extraction`, `meeting-notes`, `stakeholder-email`, `open-questions-tracker`
- File: [skills/00-shared/meetings/after/meeting-follow-up/SKILL.md](skills/00-shared/meetings/after/meeting-follow-up/SKILL.md)

**Track open questions** · `open-questions-tracker`

- When: Collects unresolved questions from meetings, documents and threads into a tracker with a precise question, why it matters, what it blocks, owner, needed-by date, status and answer, and prioritizes by what each blocks. Use when a project has many loose questions, when analysis or design is waiting on answers, or when someone asks \"what are we still waiting on?\".
- Try: _"Go through these three meeting notes and the requirements doc and build an open questions list with owners and due dates."_
- Related: `action-item-extraction`, `meeting-notes`, `raid-log`, `request-clarification-questions`, `decision-log`
- File: [skills/00-shared/meetings/after/open-questions-tracker/SKILL.md](skills/00-shared/meetings/after/open-questions-tracker/SKILL.md)

### Communication

#### Written Communication

**Write a status update** · `status-update`

- When: Writes a concise status update with an overall RAG rating, progress against plan, risks and issues, decisions or help needed, and next steps. Use when someone must report progress on a project, workstream, initiative or incident to a manager, sponsor, steering group or team channel, or asks for a \"weekly update\", \"status report\" or \"where are we\".
- Try: _"Write this week's status update for the data platform migration: 3 of 5 domains moved, the finance domain is blocked on a firewall change, go-live still planned for the 30th."_
- Related: `project-status-report`, `executive-summary`, `escalation-message`, `raid-log`, `steering-committee-pack`
- File: [skills/00-shared/communication/written/status-update/SKILL.md](skills/00-shared/communication/written/status-update/SKILL.md)

**Write an executive summary** · `executive-summary`

- When: Condenses a document, analysis, proposal or discussion into a one-page, decision-oriented executive summary that leads with the conclusion and the ask, followed by the supporting points, options, risks and next steps. Use when a senior reader must understand and act on long or technical content quickly, or someone asks for a \"TL;DR\", \"exec summary\" or \"one-pager for leadership\".
- Try: _"Turn this 20-page vendor evaluation into an executive summary for the CIO, who has to choose between the two shortlisted vendors next week."_
- Related: `status-update`, `steering-committee-pack`, `document-simplify`, `decision-matrix`, `presentation-outline`
- File: [skills/00-shared/communication/written/executive-summary/SKILL.md](skills/00-shared/communication/written/executive-summary/SKILL.md)

**Write a stakeholder email** · `stakeholder-email`

- When: Writes a purpose-first email to a stakeholder with a subject line that states the action, the ask or key message in the first two lines, only the context needed, and a tone matched to the reader's role and relationship. Use when someone needs to request something, inform, align or follow up with a manager, sponsor, customer, vendor or another team by email or long chat message.
- Try: _"Write an email to the head of finance asking her team to validate the new cost allocation rules by Friday so we can start UAT next week."_
- Related: `tone-rewrite`, `escalation-message`, `bad-news-delivery`, `stakeholder-map`, `meeting-follow-up`
- File: [skills/00-shared/communication/written/stakeholder-email/SKILL.md](skills/00-shared/communication/written/stakeholder-email/SKILL.md)

**Write an escalation** · `escalation-message`

- When: Writes an escalation that states the issue, verified facts, business impact and deadline, what has already been tried, the options with trade-offs, a recommendation and one clear ask of the escalation owner. Use when a blocker, dependency, conflict or risk cannot be resolved at the current level and needs a decision, resources or intervention from a manager, sponsor, vendor account lead or another team's leadership.
- Try: _"Escalate to my director that the identity team has not delivered the SSO integration for three weeks and our pilot on the 15th will slip if it does not land by the 8th."_
- Related: `stakeholder-email`, `status-update`, `raid-log`, `trade-off-analysis`, `conflict-resolution`
- File: [skills/00-shared/communication/written/escalation-message/SKILL.md](skills/00-shared/communication/written/escalation-message/SKILL.md)

**Write an announcement** · `announcement`

- When: Writes an announcement of a change, release, policy, process or decision structured as what is changing, why, who is affected and how, when it takes effect, what readers must do, and where to get help. Use when a team, department or user base must be informed of something new or different through email, chat channel, intranet post or newsletter.
- Try: _"Announce to all engineering teams that from 1 March every production deployment must pass the new security scan gate, and what they need to do before then."_
- Related: `release-announcement`, `org-change-communication`, `communication-plan`, `faq-builder`, `stakeholder-email`
- File: [skills/00-shared/communication/written/announcement/SKILL.md](skills/00-shared/communication/written/announcement/SKILL.md)

**Rewrite for tone** · `tone-rewrite`

- When: Rewrites an existing message to a target tone (clearer, softer, firmer, more formal, more concise, more neutral) while preserving its facts, commitments and asks, and explains the key changes. Use when someone has a draft email, chat message, review comment or reply that sounds too harsh, too vague, too long, too informal or too passive, or asks to \"make this sound better\", \"soften\", \"be more assertive\" or \"make it professional\".
- Try: _"Make this reply to a customer firmer but still polite: \"Sorry, we might not be able to do the custom report this month, maybe next month if possible?"_
- Related: `stakeholder-email`, `feedback-sbi`, `bad-news-delivery`, `document-simplify`, `technical-translation`
- File: [skills/00-shared/communication/written/tone-rewrite/SKILL.md](skills/00-shared/communication/written/tone-rewrite/SKILL.md)

**Deliver bad news** · `bad-news-delivery`

- When: Communicates a delay, cancellation, scope cut, failed delivery, rejected request or missed commitment transparently, stating the news early, the cause without blame, the impact on the reader, what is being done, options and the next update. Use when someone must tell a customer, sponsor, manager or team that something will not happen as promised or expected, in writing or as talking points for a conversation.
- Try: _"Help me tell the sponsor that the reporting release planned for the 20th will slip by three weeks because the data vendor's API changed, and what we propose instead."_
- Related: `tone-rewrite`, `escalation-message`, `stakeholder-email`, `status-update`, `customer-outage-notice`
- File: [skills/00-shared/communication/written/bad-news-delivery/SKILL.md](skills/00-shared/communication/written/bad-news-delivery/SKILL.md)

#### Presentation & Verbal

**Outline a presentation** · `presentation-outline`

- When: Builds an audience-specific storyline and a slide-by-slide outline with one message per slide, supporting evidence, a clear ask and timing. Use when someone must present a proposal, status, design, result or decision to managers, customers, a committee or a team and needs the structure before designing slides.
- Try: _"Outline a 20-minute presentation to the leadership team proposing we move our reporting workloads to a new data platform next year."_
- Related: `executive-summary`, `steering-committee-pack`, `demo-script`, `elevator-pitch`, `stakeholder-map`
- File: [skills/00-shared/communication/verbal/presentation-outline/SKILL.md](skills/00-shared/communication/verbal/presentation-outline/SKILL.md)

**Write a demo script** · `demo-script`

- When: Writes a product or feature demo script with a user-story flow, click-by-click steps, talking points tied to audience value, prepared data, timing and a fallback for every risky step. Use when a team must demo software to stakeholders, customers, a review session or a sales prospect and wants a rehearsable run sheet instead of improvising.
- Try: _"Write a 10-minute demo script for showing the new invoice approval workflow to the finance managers at the iteration review."_
- Related: `presentation-outline`, `iteration-review-prep`, `stakeholder-review-prep`, `uat-scenarios`, `elevator-pitch`
- File: [skills/00-shared/communication/verbal/demo-script/SKILL.md](skills/00-shared/communication/verbal/demo-script/SKILL.md)

**Write an elevator pitch** · `elevator-pitch`

- When: Writes a 30-60 second spoken pitch for an idea, project, product or request, tailored to one listener, with a hook, the problem, the proposal, proof, and a single concrete ask. Use when someone has a short window (corridor, call opening, intro at a meeting, funding or sponsorship request) to get a busy person interested enough to take the next step.
- Try: _"Give me a 45-second pitch to convince our CTO to sponsor a pilot for automated contract testing between our microservices."_
- Related: `presentation-outline`, `executive-summary`, `value-proposition-canvas`, `problem-statement`, `stakeholder-map`
- File: [skills/00-shared/communication/verbal/elevator-pitch/SKILL.md](skills/00-shared/communication/verbal/elevator-pitch/SKILL.md)

#### Interpersonal

**Give feedback (SBI)** · `feedback-sbi`

- When: Frames positive or corrective feedback with the Situation-Behavior-Impact model, separating observed behavior from interpretation, stating the concrete impact, and ending with a request and an open question. Use when someone must give feedback to a colleague, report, peer or manager, prepare a difficult conversation, or rewrite feedback that sounds like a judgment of the person.
- Try: _"Help me give feedback to a senior developer who keeps merging pull requests without waiting for review, in a way that doesn't make him defensive."_
- Related: `one-on-one-prep`, `performance-review`, `conflict-resolution`, `tone-rewrite`, `underperformance-plan`
- File: [skills/00-shared/communication/interpersonal/feedback-sbi/SKILL.md](skills/00-shared/communication/interpersonal/feedback-sbi/SKILL.md)

**Resolve a conflict** · `conflict-resolution`

- When: Maps a workplace conflict into parties, stated positions, underlying interests, facts versus perceptions and conflict type, then proposes a mediated resolution path with options that serve shared interests and agreed next steps. Use when two people, teams or functions disagree on priorities, ownership, approach or behavior and the disagreement is blocking work or damaging the relationship.
- Try: _"Our backend and mobile teams keep arguing about who owns API versioning and releases are slipping. Help me mediate."_
- Related: `feedback-sbi`, `negotiation-prep`, `facilitation-guide`, `trade-off-analysis`, `decision-log`
- File: [skills/00-shared/communication/interpersonal/conflict-resolution/SKILL.md](skills/00-shared/communication/interpersonal/conflict-resolution/SKILL.md)

**Prepare for a negotiation** · `negotiation-prep`

- When: Prepares a negotiation by defining your goal, interests, BATNA, walk-away point, the counterpart's likely interests and BATNA, the zone of possible agreement, tradeable concessions and an opening position with its justification. Use when someone must negotiate scope, deadline, budget, resources, a vendor contract, rates or terms with a customer, vendor, sponsor or another team.
- Try: _"Help me prepare to negotiate with the business sponsor who wants the full scope by March while we can only deliver about 60% with the current team."_
- Related: `conflict-resolution`, `stakeholder-map`, `trade-off-analysis`, `vendor-evaluation`, `pricing-analysis`
- File: [skills/00-shared/communication/interpersonal/negotiation-prep/SKILL.md](skills/00-shared/communication/interpersonal/negotiation-prep/SKILL.md)

### Documentation

#### Authoring

**Outline a document** · `document-outline`

- When: Proposes a fit-for-purpose structure for any document (design doc, policy, guide, report, proposal, specification) from its purpose, audience and decisions it must support, with section goals and content notes. Use when someone must start a new document, faces a blank page, inherited a messy document to restructure, or asks what sections a document should have.
- Try: _"Outline a document proposing that we move our batch reporting jobs to an event-driven pipeline; readers are the architecture board."_
- Related: `docs-information-architecture`, `document-review`, `executive-summary`, `technical-design-doc`, `brd-writing`
- File: [skills/00-shared/documentation/authoring/document-outline/SKILL.md](skills/00-shared/documentation/authoring/document-outline/SKILL.md)

**Build a glossary** · `glossary-builder`

- When: Extracts domain terms, acronyms and overloaded words from source material and writes unambiguous, testable definitions with synonyms, forbidden usages and owners. Use when a project, document or team has inconsistent terminology, when onboarding people to a domain, when writing requirements or data models, or when someone asks for a glossary or ubiquitous language.
- Try: _"Build a glossary from these requirement notes; people use customer, client, account and subscriber interchangeably."_
- Related: `business-rules-catalog`, `bounded-context-map`, `technical-translation`, `data-catalog-entry`, `ambiguity-detection`
- File: [skills/00-shared/documentation/authoring/glossary-builder/SKILL.md](skills/00-shared/documentation/authoring/glossary-builder/SKILL.md)

**Build an FAQ** · `faq-builder`

- When: Generates the questions a specific audience is likely to ask about a product, change, policy or project, and answers them strictly from provided source material, flagging gaps. Use when preparing an FAQ for a launch, migration, policy change, internal tool or customer help page, or when repeated questions keep arriving through support or chat channels.
- Try: _"Create an FAQ for employees about the move from our old VPN to the new zero-trust access client, based on this rollout plan."_
- Related: `kb-article`, `announcement`, `org-change-communication`, `user-guide`, `ticket-response`
- File: [skills/00-shared/documentation/authoring/faq-builder/SKILL.md](skills/00-shared/documentation/authoring/faq-builder/SKILL.md)

**Produce a diagram as code** · `diagram-as-code`

- When: Turns a textual description of a system, process, sequence, data model or state machine into a correct, readable diagram in Mermaid or PlantUML, choosing the right diagram type and listing assumptions. Use when someone asks to draw, visualize or diagram something, needs a version-controllable diagram for docs or a pull request, or wants to convert a whiteboard photo description or legacy diagram into code.
- Try: _"Draw a Mermaid sequence diagram: the mobile app calls the API gateway, which validates the token with the identity provider and then calls the order service, which publishes an OrderCreated event."_
- Related: `c4-model`, `bpmn-model`, `sequence-flow`, `state-model`, `document-outline`
- File: [skills/00-shared/documentation/authoring/diagram-as-code/SKILL.md](skills/00-shared/documentation/authoring/diagram-as-code/SKILL.md)

**Translate technical content** · `technical-translation`

- When: Translates technical content (specifications, documentation, UI text, error messages, release notes, runbooks) between English and Turkish while preserving terminology, code, identifiers, formatting and meaning, and flags ambiguous source text. Use when a technical document, message or interface must be delivered in the other language, or when an existing translation needs terminology alignment.
- Try: _"Translate this API error-handling section of our developer guide from English to Turkish; keep code and HTTP terms as they are."_
- Related: `glossary-builder`, `microcopy`, `error-message-writing`, `document-review`, `style-guide-check`
- File: [skills/00-shared/documentation/authoring/technical-translation/SKILL.md](skills/00-shared/documentation/authoring/technical-translation/SKILL.md)

#### Review

**Review a document** · `document-review`

- When: Reviews any document for clarity, completeness, internal consistency, correctness of claims and fit to its audience and purpose, returning prioritized, located findings with suggested fixes and a verdict. Use when someone asks for feedback on a draft, needs a document checked before approval or publication, or wants a second opinion on a specification, proposal, policy, guide or report.
- Try: _"Review this incident process document before we send it to the operations directors for approval."_
- Related: `requirements-review-checklist`, `architecture-review`, `document-simplify`, `style-guide-check`, `doc-diff-summary`
- File: [skills/00-shared/documentation/review/document-review/SKILL.md](skills/00-shared/documentation/review/document-review/SKILL.md)

**Simplify a document** · `document-simplify`

- When: Rewrites a document or passage to be shorter and easier to read for its audience by removing redundancy, jargon, hedging and nominalizations while preserving every obligation, number, condition and decision. Use when a text is too long, dense or technical for its readers, when someone asks to shorten, simplify or make something plain-language, or when a document must fit a length limit.
- Try: _"Simplify this three-page data retention policy so that team leads can understand what they must do; keep all obligations."_
- Related: `document-review`, `executive-summary`, `tone-rewrite`, `microcopy`, `technical-translation`
- File: [skills/00-shared/documentation/review/document-simplify/SKILL.md](skills/00-shared/documentation/review/document-simplify/SKILL.md)

**Summarize document changes** · `doc-diff-summary`

- When: Compares two versions of a document (contract, specification, policy, runbook, requirements) and produces a categorized summary of substantive changes, their impact on each stakeholder and the questions they raise, separating meaning changes from editorial ones. Use when a new version of a document arrives, before re-approval or sign-off, when a vendor or client sends a revised draft, or when someone asks what changed between two versions.
- Try: _"Here are v1.3 and v1.4 of the integration specification from the vendor. What changed and what does it mean for us?"_
- Related: `change-request-analysis`, `impact-analysis`, `document-review`, `changelog-entry`, `requirements-sign-off`
- File: [skills/00-shared/documentation/review/doc-diff-summary/SKILL.md](skills/00-shared/documentation/review/doc-diff-summary/SKILL.md)

### Problem Solving & Decision Tools

#### Problem Framing

**Write a problem statement** · `problem-statement`

- When: Frames a problem as a precise, solution-free statement of who is affected, what happens, when and where, with quantified impact and evidence, plus boundaries and success signals. Use at the start of any initiative, investigation, improvement or design effort, when a team jumps to solutions, when stakeholders describe the same issue differently, or when someone asks to define or reframe a problem.
- Try: _"Write a problem statement: customers keep complaining that the monthly invoice is wrong and support is overloaded at the start of each month."_
- Related: `five-whys`, `fishbone-analysis`, `assumption-mapping`, `hypothesis-statement`, `request-intake-document`
- File: [skills/00-shared/thinking-tools/problem/problem-statement/SKILL.md](skills/00-shared/thinking-tools/problem/problem-statement/SKILL.md)

**Run a 5 Whys analysis** · `five-whys`

- When: Runs a disciplined 5 Whys analysis from a clearly stated symptom down to one or more verifiable root causes, with evidence for each link, a branch per contributing cause and countermeasures that address the cause, not the symptom. Use when an incident, defect, missed target or recurring problem needs a root cause, when someone asks 'why does this keep happening', or when a postmortem or lessons-learned needs causal depth.
- Try: _"Run a 5 Whys on this: the nightly customer export failed three times this month and finance got the report late each time."_
- Related: `problem-statement`, `fishbone-analysis`, `postmortem`, `debugging-hypotheses`, `lessons-learned`
- File: [skills/00-shared/thinking-tools/problem/five-whys/SKILL.md](skills/00-shared/thinking-tools/problem/five-whys/SKILL.md)

**Run a fishbone analysis** · `fishbone-analysis`

- When: Builds an Ishikawa (fishbone) diagram that organizes all plausible causes of a clearly stated effect into categories suited to the domain, separates evidenced causes from hypotheses, and selects the few causes worth verifying first. Use when a problem likely has several interacting causes, when a team brainstorms causes and needs structure, or before running 5 Whys on the most promising branches.
- Try: _"Do a fishbone analysis: our release lead time went from 3 days to 2 weeks over the last two quarters."_
- Related: `problem-statement`, `five-whys`, `postmortem`, `diagram-as-code`, `assumption-mapping`
- File: [skills/00-shared/thinking-tools/problem/fishbone-analysis/SKILL.md](skills/00-shared/thinking-tools/problem/fishbone-analysis/SKILL.md)

**Map assumptions** · `assumption-mapping`

- When: Surfaces the assumptions behind a plan, product idea, estimate or decision, classifies them (desirability, viability, feasibility, usability, ethical/regulatory, delivery), plots them by importance and evidence, and turns the riskiest into testable statements with the cheapest test. Use before committing budget or scope, when a plan feels optimistic, or when someone asks what must be true for this to work.
- Try: _"Map the assumptions behind our plan to launch self-service onboarding for SME customers next quarter."_
- Related: `hypothesis-statement`, `experiment-design`, `pre-mortem`, `risk-register`, `problem-statement`
- File: [skills/00-shared/thinking-tools/problem/assumption-mapping/SKILL.md](skills/00-shared/thinking-tools/problem/assumption-mapping/SKILL.md)

#### Decision Making

**Build a weighted decision matrix** · `decision-matrix`

- When: Builds a weighted decision matrix that compares options against agreed, independent criteria with explicit weights, scoring scales and must-have knock-out rules, then tests how sensitive the result is to weights and uncertain scores. Use when choosing between three or more options (vendors, technologies, designs, candidates for investment), when a decision must be defensible to others, or when a group needs to converge.
- Try: _"Build a weighted decision matrix to choose between three message brokers for our order platform."_
- Related: `trade-off-analysis`, `pros-cons`, `vendor-evaluation`, `technology-selection`, `decision-log`
- File: [skills/00-shared/thinking-tools/decision/decision-matrix/SKILL.md](skills/00-shared/thinking-tools/decision/decision-matrix/SKILL.md)

**List pros and cons** · `pros-cons`

- When: Produces a balanced pros and cons analysis for one proposal or a small set of options, weighing each point by impact and likelihood, separating facts from opinions, including the do-nothing baseline and ending with a clear, conditional recommendation. Use for quick decisions, yes/no proposals, or when someone asks for the advantages and disadvantages of an approach before committing.
- Try: _"Give me the pros and cons of moving our weekly release to on-demand releases, and a recommendation."_
- Related: `decision-matrix`, `trade-off-analysis`, `bias-check`, `pre-mortem`, `decision-log`
- File: [skills/00-shared/thinking-tools/decision/pros-cons/SKILL.md](skills/00-shared/thinking-tools/decision/pros-cons/SKILL.md)

**Run a SWOT analysis** · `swot-analysis`

- When: Runs a SWOT analysis for a clearly scoped subject (product, team, platform, initiative, business unit) against a stated objective, keeping internal strengths and weaknesses separate from external opportunities and threats, backing each item with evidence and converting the result into TOWS strategies and prioritized actions. Use for strategy or planning sessions, before a major investment, when entering a market, or when someone asks for a SWOT.
- Try: _"Do a SWOT analysis for our internal data platform team ahead of next year's planning."_
- Related: `competitor-analysis`, `product-strategy-one-pager`, `technology-strategy`, `assumption-mapping`, `risk-register`
- File: [skills/00-shared/thinking-tools/decision/swot-analysis/SKILL.md](skills/00-shared/thinking-tools/decision/swot-analysis/SKILL.md)

**Analyze trade-offs** · `trade-off-analysis`

- When: Makes explicit what each option gains and gives up across competing qualities (for example speed vs. safety, cost vs. resilience, flexibility vs. simplicity, scope vs. time), identifies the decisive tension, the reversibility of each choice and the conditions under which the preferred option stops being right. Use for architecture, product, scope or process decisions where no option wins on everything, when stakeholders talk past each other, or before recording a decision.
- Try: _"Analyze the trade-offs between a modular monolith and microservices for our new claims system."_
- Related: `decision-matrix`, `adr`, `architecture-review`, `pros-cons`, `technology-selection`
- File: [skills/00-shared/thinking-tools/decision/trade-off-analysis/SKILL.md](skills/00-shared/thinking-tools/decision/trade-off-analysis/SKILL.md)

**Run a pre-mortem** · `pre-mortem`

- When: Runs a pre-mortem on a plan, project, launch or decision by assuming it has already failed and working backwards to the most plausible causes, early warning signals and mitigations. Use before committing to a plan, launch, migration or major decision, when a team seems overconfident, or when someone asks \"what could go wrong?\" or \"run a pre-mortem\".
- Try: _"Run a pre-mortem on our plan to migrate the billing database to a new cloud region over one weekend in March."_
- Related: `risk-register`, `assumption-mapping`, `bias-check`, `raid-log`, `technical-risk-review`
- File: [skills/00-shared/thinking-tools/decision/pre-mortem/SKILL.md](skills/00-shared/thinking-tools/decision/pre-mortem/SKILL.md)

**Check for cognitive bias** · `bias-check`

- When: Reviews an analysis, recommendation or decision for cognitive biases such as confirmation, anchoring, survivorship, sunk cost, availability, overconfidence and groupthink, cites the evidence for each suspected bias and proposes a concrete debiasing action. Use when a decision is about to be made or an analysis is about to be shared, when someone asks \"am I missing something?\", \"is this biased?\", \"challenge my reasoning\" or wants a red-team view of a conclusion.
- Try: _"Check this recommendation for bias before I send it to the steering committee: we should keep investing in the in-house scheduler because we already spent 18 months on it and the two pilot teams love it."_
- Related: `pre-mortem`, `assumption-mapping`, `decision-matrix`, `trade-off-analysis`, `decision-log`
- File: [skills/00-shared/thinking-tools/decision/bias-check/SKILL.md](skills/00-shared/thinking-tools/decision/bias-check/SKILL.md)

### Knowledge Management

#### Capture & Transfer

**Capture lessons learned** · `lessons-learned`

- When: Captures lessons learned from a project, release, phase, incident or initiative as evidence-backed observations of what worked and what did not, their causes, and specific actions to keep or change, each with an owner and a place where it will be applied. Use at the end of a project or phase, after a release or major event, when preparing a closure report, or when someone asks to \"write up lessons learned\" from notes, retrospectives or timelines.
- Try: _"Write up lessons learned from our CRM migration project using these retro notes and the timeline."_
- Related: `retrospective-facilitation`, `postmortem`, `project-closure-report`, `kb-article`, `action-item-extraction`
- File: [skills/00-shared/knowledge/capture/lessons-learned/SKILL.md](skills/00-shared/knowledge/capture/lessons-learned/SKILL.md)

**Write a handover document** · `handover-document`

- When: Writes a handover document that transfers ownership of a system, project, service, workstream or role to a new owner, covering context, current state, responsibilities, contacts, access, recurring duties, risks, open items and a transition plan with an acceptance point. Use when someone leaves, changes role, goes on long leave, when a project moves from delivery to operations, when a vendor or team changes, or when asked to \"prepare a handover\".
- Try: _"I'm moving to another team in two weeks. Help me write a handover for the payment reconciliation service I own."_
- Related: `on-call-handover`, `runbook`, `onboarding-guide`, `raid-log`, `kb-article`
- File: [skills/00-shared/knowledge/capture/handover-document/SKILL.md](skills/00-shared/knowledge/capture/handover-document/SKILL.md)

**Write a knowledge base article** · `kb-article`

- When: Writes a searchable knowledge base article (how-to, troubleshooting, or explanation) from notes, tickets, chat threads or expert input, with a findable title, the symptoms and search terms readers actually use, applicability, verified steps, expected results and ownership. Use when a question keeps being asked, a support ticket or incident produced a reusable fix, tribal knowledge must be written down, or someone asks to \"write a KB article\" or \"document this for the wiki\".
- Try: _"Turn this support thread about VPN certificate errors on new laptops into a KB article."_
- Related: `how-to-guide`, `faq-builder`, `runbook`, `document-review`, `glossary-builder`
- File: [skills/00-shared/knowledge/capture/kb-article/SKILL.md](skills/00-shared/knowledge/capture/kb-article/SKILL.md)

**Write an onboarding guide** · `onboarding-guide`

- When: Writes an onboarding guide that takes a newcomer to a team, department or project through context, ways of working, tools and access, key people, vocabulary and a sequenced set of first tasks with clear \"you are ready when\" milestones. Use when a team expects new members, contractors or transfers, when existing onboarding is scattered across wikis and chats, or when someone asks to \"write an onboarding guide\" for a role or team.
- Try: _"Write an onboarding guide for new business analysts joining our payments team."_
- Related: `onboarding-plan-30-60-90`, `technical-onboarding`, `handover-document`, `glossary-builder`, `kb-article`
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

- When: Classifies one or more incoming business requests by type, urgency, value, effort class and risk, detects duplicates, and routes each to the right path (fast track, analysis, feasibility, project, support, reject). Use when a queue of new requests must be sorted, at a demand review, or when asked 'where should these requests go and what comes first?'.
- Try: _"Triage these 8 requests from this week's inbox and tell me which go to analysis, which are support tickets and which we should reject."_
- Related: `request-intake-document`, `request-completeness-check`, `ticket-triage`, `backlog-prioritization`, `change-request-analysis`
- File: [skills/01-business-analysis/business-analyst/intake/request-triage/SKILL.md](skills/01-business-analysis/business-analyst/intake/request-triage/SKILL.md)

**Check request completeness** · `request-completeness-check`

- When: Checks a request or intake document against a gap checklist (business, users, data, integration, NFR, legal, operations, reporting, migration) and reports what is missing, vague or contradictory with severity and a ready/not-ready verdict. Use before a request enters analysis, estimation or a sprint/backlog, or when asked 'is this request complete enough to start?'.
- Try: _"Check whether this request is complete enough to start analysis: 'Add a discount approval step for orders above a limit, managers approve by email.'"_
- Related: `request-intake-document`, `request-clarification-questions`, `ambiguity-detection`, `requirements-gap-analysis`, `definition-of-ready`
- File: [skills/01-business-analysis/business-analyst/intake/request-completeness-check/SKILL.md](skills/01-business-analysis/business-analyst/intake/request-completeness-check/SKILL.md)

#### Stakeholder Analysis

**Identify stakeholders** · `stakeholder-identification`

- When: Identifies everyone who affects, is affected by, or decides on an initiative, including hidden and indirect stakeholders (compliance, operations, data owners, external parties), with their role, interest and what is needed from them. Use at the start of a request, project or analysis, or when asked 'who do we need to involve?'.
- Try: _"Who are the stakeholders for replacing our paper-based expense approval with a digital workflow?"_
- Related: `stakeholder-map`, `raci-matrix`, `stakeholder-register`, `request-intake-document`, `communication-plan`
- File: [skills/01-business-analysis/business-analyst/stakeholders/stakeholder-identification/SKILL.md](skills/01-business-analysis/business-analyst/stakeholders/stakeholder-identification/SKILL.md)

**Map stakeholders by power/interest** · `stakeholder-map`

- When: Places stakeholders on a power/interest grid with evidence for each rating, adds current vs desired attitude, and defines an engagement strategy, channel and frequency per quadrant and per key person. Use after stakeholders are identified, before planning communication or when support for an initiative is uncertain; triggers include 'power interest grid', 'who do we manage closely?'.
- Try: _"Map these 9 stakeholders on a power/interest grid and tell me how to engage each for the CRM migration."_
- Related: `stakeholder-identification`, `raci-matrix`, `communication-plan`, `stakeholder-register`, `conflict-resolution`
- File: [skills/01-business-analysis/business-analyst/stakeholders/stakeholder-map/SKILL.md](skills/01-business-analysis/business-analyst/stakeholders/stakeholder-map/SKILL.md)

**Build a RACI matrix** · `raci-matrix`

- When: Builds a RACI matrix that assigns Responsible, Accountable, Consulted and Informed roles per activity or deliverable, then validates it (exactly one A, at least one R, no overloaded roles, no empty rows). Use when responsibilities are unclear, work falls between teams, or someone asks 'who owns what?' for a project, process or analysis activity.
- Try: _"Create a RACI for the requirements phase of our payment gateway integration: BA, PO, architect, dev lead, QA, security, vendor."_
- Related: `stakeholder-identification`, `stakeholder-map`, `communication-plan`, `project-charter`, `role-definition`
- File: [skills/01-business-analysis/business-analyst/stakeholders/raci-matrix/SKILL.md](skills/01-business-analysis/business-analyst/stakeholders/raci-matrix/SKILL.md)

#### Elicitation

**Prepare interview questions** · `interview-question-set`

- When: Prepares a requirements interview guide tailored to a stakeholder type (executive, process owner, end user, IT/system owner, compliance), with opening, context, open, probing and validation questions, timing and follow-up prompts. Use before an elicitation interview or when asked 'what should I ask the users/managers in the interview?'.
- Try: _"Prepare a 45-minute interview for warehouse shift supervisors about how they handle stock discrepancies today."_
- Related: `interview-notes-analysis`, `request-clarification-questions`, `workshop-plan`, `stakeholder-identification`, `problem-interview-script`
- File: [skills/01-business-analysis/business-analyst/elicitation/interview-question-set/SKILL.md](skills/01-business-analysis/business-analyst/elicitation/interview-question-set/SKILL.md)

**Analyze interview notes** · `interview-notes-analysis`

- When: Analyzes raw interview notes or transcripts and extracts needs, pain points, business rules, exceptions, data and system mentions, conflicts and open questions, each traced to its source. Use after one or more elicitation interviews, when notes are messy, or when asked 'what did we learn from these interviews?'.
- Try: _"Here are my notes from interviews with three accounts payable clerks. Extract the needs, pains, rules and any contradictions."_
- Related: `interview-question-set`, `business-rules-catalog`, `requirements-consistency-check`, `feedback-synthesis`, `open-questions-tracker`
- File: [skills/01-business-analysis/business-analyst/elicitation/interview-notes-analysis/SKILL.md](skills/01-business-analysis/business-analyst/elicitation/interview-notes-analysis/SKILL.md)

**Plan a requirements workshop** · `workshop-plan`

- When: Designs a requirements workshop: objectives, participants and roles, pre-work, a timed agenda of elicitation activities (e.g., process walk-through, story mapping, rules/exceptions round, prioritization), materials, decision rules and expected outputs, for on-site or remote formats. Use when several stakeholders must align or co-create requirements, or when asked 'plan a workshop for...'.
- Try: _"Plan a half-day remote workshop with finance, sales ops and IT to define the requirements for automated credit limit checks."_
- Related: `facilitation-guide`, `meeting-agenda`, `interview-question-set`, `story-mapping`, `discovery-workshop`
- File: [skills/01-business-analysis/business-analyst/elicitation/workshop-plan/SKILL.md](skills/01-business-analysis/business-analyst/elicitation/workshop-plan/SKILL.md)

**Design a questionnaire** · `questionnaire-design`

- When: Designs an unbiased requirements questionnaire for a large or distributed audience: objectives, target population, question types and wording free of leading or double-barreled items, logic/branching, pilot plan, privacy notice and analysis plan. Use when many users or sites must be asked the same things, or when asked to 'create a survey to gather requirements'.
- Try: _"Design a survey for 400 branch employees to find out which tasks in the current loan application screen take the most time."_
- Related: `interview-question-set`, `screener-survey`, `feedback-synthesis`, `research-plan`, `data-classification`
- File: [skills/01-business-analysis/business-analyst/elicitation/questionnaire-design/SKILL.md](skills/01-business-analysis/business-analyst/elicitation/questionnaire-design/SKILL.md)

**Elicit from existing documents** · `document-analysis`

- When: Elicits requirements from existing documents such as specifications, user manuals, procedures, contracts, regulations, forms and reports, producing a source-traced list of candidate requirements, business rules, data items and conflicts. Use when legacy documentation, a regulation or a contract must be mined before interviews, or when asked 'what requirements can we get out of these documents?'.
- Try: _"Extract the requirements from this 20-page operations manual of our current claims system and the new regulation text, and show where they conflict."_
- Related: `business-rules-catalog`, `interview-question-set`, `requirements-consistency-check`, `traceability-matrix`, `glossary-builder`
- File: [skills/01-business-analysis/business-analyst/elicitation/document-analysis/SKILL.md](skills/01-business-analysis/business-analyst/elicitation/document-analysis/SKILL.md)

**Structure job-shadowing observations** · `observation-notes`

- When: Structures raw job-shadowing or contextual observation notes into a task sequence with timings, tools used, pains, workarounds, interruptions and the gap between the documented and the actual process. Use after observing users at work, when field notes are messy, or when asked 'what did we learn from watching the team do this?'.
- Try: _"Here are my notes from shadowing two call-center agents for three hours. Structure them into tasks, pains and workarounds."_
- Related: `as-is-process`, `interview-notes-analysis`, `value-stream-map`, `customer-journey-map`, `research-synthesis`
- File: [skills/01-business-analysis/business-analyst/elicitation/observation-notes/SKILL.md](skills/01-business-analysis/business-analyst/elicitation/observation-notes/SKILL.md)

**Run an interactive requirements interview** · `requirements-interview`

- When: Interviews the user one question at a time, adapting each question to the previous answer (diagnose, narrow, confirm), keeps a running specification visible, stops when a readiness checklist passes and ends with a structured requirements summary. Use when a need is vague (\"we need a dashboard\", \"automate approvals\"), when the user says \"ask me questions\", \"help me specify this\" or \"interview me\", or before writing stories or a PRD from thin input.
- Try: _"Interview me until this is clear enough to build: we want suppliers to upload their invoices themselves instead of emailing them."_
- Related: `request-clarification-questions`, `requirements-gap-analysis`, `user-story`, `acceptance-criteria`, `edge-case-elicitation`
- File: [skills/01-business-analysis/business-analyst/elicitation/requirements-interview/SKILL.md](skills/01-business-analysis/business-analyst/elicitation/requirements-interview/SKILL.md)

#### Requirements Documentation

**Write a Business Requirements Document** · `brd-writing`

- When: Writes a Business Requirements Document that states the business problem, objectives with measurable success criteria, scope, stakeholders, high-level business requirements, business rules, constraints, assumptions and risks, independent of any solution design. Use when an initiative needs an agreed business baseline before solution or functional design, or when asked to 'write the BRD' for a project or change.
- Try: _"Write a BRD for replacing our manual supplier onboarding (email and Excel) with a self-service process; here are the workshop notes."_
- Related: `request-intake-document`, `frd-writing`, `stakeholder-identification`, `requirements-review-checklist`, `requirements-sign-off`
- File: [skills/01-business-analysis/business-analyst/documentation/brd-writing/SKILL.md](skills/01-business-analysis/business-analyst/documentation/brd-writing/SKILL.md)

**Write a Functional Requirements Document** · `frd-writing`

- When: Writes a Functional Requirements Document that specifies system behavior per function: actors and permissions, triggers, inputs with validations, processing and business rules, outputs, states, error handling and interfaces, each requirement uniquely identified, testable and traced to a business need. Use when business requirements are agreed and development or a vendor needs an unambiguous behavioral specification, or when asked to 'write the FRD'.
- Try: _"Based on this BRD, write the FRD for the supplier self-registration and document verification functions."_
- Related: `brd-writing`, `use-case-spec`, `business-rules-catalog`, `nfr-specification`, `traceability-matrix`
- File: [skills/01-business-analysis/business-analyst/documentation/frd-writing/SKILL.md](skills/01-business-analysis/business-analyst/documentation/frd-writing/SKILL.md)

**Write user stories** · `user-story`

- When: Writes user stories in the As a / I want / So that form with a specific persona, a real outcome, context, business rules, dependencies and acceptance criteria hooks, and flags items that are really technical tasks or need splitting. Use when a need, requirement or feature must become backlog items, or when asked to 'write stories', 'turn this into user stories' or rewrite weak ones.
- Try: _"Write user stories for letting store managers approve staff shift swaps from their phone."_
- Related: `acceptance-criteria`, `invest-check`, `story-splitting`, `persona`, `epic-breakdown`
- File: [skills/01-business-analysis/business-analyst/documentation/user-story/SKILL.md](skills/01-business-analysis/business-analyst/documentation/user-story/SKILL.md)

**Write acceptance criteria** · `acceptance-criteria`

- When: Writes testable acceptance criteria for a user story or requirement, in Given/When/Then scenarios or rule form, covering the happy path, business rule variations, validation, permissions and failure cases, with one trigger and one outcome per scenario. Use when a story needs its conditions of done, when criteria are vague or untestable, or when asked for 'AC', 'Gherkin' or 'Given/When/Then'.
- Try: _"Write acceptance criteria for: As a store manager, I want to approve or reject a pending shift swap from my phone."_
- Related: `user-story`, `invest-check`, `edge-case-elicitation`, `bdd-feature-file`, `test-scenarios-from-requirements`
- File: [skills/01-business-analysis/business-analyst/documentation/acceptance-criteria/SKILL.md](skills/01-business-analysis/business-analyst/documentation/acceptance-criteria/SKILL.md)

**Write a use case specification** · `use-case-spec`

- When: Writes a use case specification with goal, primary and supporting actors, stakeholders' interests, trigger, preconditions, minimal and success guarantees, a numbered main success scenario, and alternate and exception flows keyed to the steps they branch from. Use when an interaction has many branches, several actors or system-to-system steps, or when asked for a 'use case', 'UC spec' or 'fully dressed use case'.
- Try: _"Write the use case for 'Return a purchased item in store' with card refunds and missing receipts."_
- Related: `frd-writing`, `user-story`, `business-rules-catalog`, `error-scenario-catalog`, `sequence-flow`
- File: [skills/01-business-analysis/business-analyst/documentation/use-case-spec/SKILL.md](skills/01-business-analysis/business-analyst/documentation/use-case-spec/SKILL.md)

**Specify non-functional requirements** · `nfr-specification`

- When: Specifies non-functional requirements as measurable statements across quality characteristics (performance, availability, reliability, security, privacy, usability, accessibility, maintainability, compatibility, portability, operability, compliance), each with metric, target, measurement condition, verification method and source. Use when quality expectations are vague ('fast', 'secure', '24/7'), when NFRs are missing from a BRD or FRD, or when asked to 'define NFRs'.
- Try: _"Define the NFRs for our new customer self-service portal; the business only said it must be fast, secure and always available."_
- Related: `frd-writing`, `nfr-to-architecture`, `slo-definition`, `security-requirements`, `performance-test-plan`
- File: [skills/01-business-analysis/business-analyst/documentation/nfr-specification/SKILL.md](skills/01-business-analysis/business-analyst/documentation/nfr-specification/SKILL.md)

**Build a business rules catalog** · `business-rules-catalog`

- When: Extracts business rules from documents, notes, requirements or code descriptions and normalizes them into a catalog with IDs, rule type (constraint, computation, inference, action enabler, fact), atomic declarative statement, source, owner, effective dates, exceptions and the requirements that use them. Use when rules are scattered or buried in processes and screens, conflict between sources, or when asked to 'list the business rules' or build a rulebook.
- Try: _"Extract and normalize the business rules from these credit application procedure notes into a catalog."_
- Related: `document-analysis`, `decision-table-testing`, `requirements-consistency-check`, `frd-writing`, `glossary-builder`
- File: [skills/01-business-analysis/business-analyst/documentation/business-rules-catalog/SKILL.md](skills/01-business-analysis/business-analyst/documentation/business-rules-catalog/SKILL.md)

**Define data requirements** · `data-requirements`

- When: Defines data requirements from a business perspective: entities and relationships, attributes with meaning, type, format, mandatory rules, validations and allowed values, identifiers, data ownership, sources and consumers, sensitivity classification, quality expectations, retention and deletion. Use when a feature or system introduces or changes data, when a data dictionary is needed for development or migration, or when asked to 'define the data' or 'what fields do we need'.
- Try: _"Define the data requirements for the supplier onboarding feature: supplier, contacts, bank details and documents."_
- Related: `conceptual-data-model`, `data-classification`, `data-quality-rules`, `retention-policy`, `frd-writing`
- File: [skills/01-business-analysis/business-analyst/documentation/data-requirements/SKILL.md](skills/01-business-analysis/business-analyst/documentation/data-requirements/SKILL.md)

**Specify report requirements** · `report-requirements`

- When: Specifies report requirements starting from the decision the report supports: audience, questions answered, fields and measures with exact calculation and grain, dimensions, filters and parameters, sorting and grouping, data sources and freshness, access and masking, delivery and format, and acceptance checks against a reconciled figure. Use when someone asks for a new report, export or list, when an existing report is disputed, or when asked to 'spec a report'.
- Try: _"Specify the monthly overdue receivables report Finance asked for, by customer segment and aging bucket."_
- Related: `dashboard-spec`, `metric-definition`, `data-requirements`, `kpi-definition`, `request-intake-document`
- File: [skills/01-business-analysis/business-analyst/documentation/report-requirements/SKILL.md](skills/01-business-analysis/business-analyst/documentation/report-requirements/SKILL.md)

**Specify screen/UI requirements** · `screen-requirements`

- When: Specifies screen or UI requirements per screen: purpose and entry points, roles and permissions, fields with source, format, mandatory rules, defaults and validations with message behavior, actions and their outcomes, screen states (empty, loading, error, read-only, no permission), navigation, accessibility and responsive needs, without prescribing visual design. Use when a screen, form or page must be specified for design and development, or when asked 'what should this screen do'.
- Try: _"Specify the screen requirements for the 'Edit customer address' form in the call-center application."_
- Related: `wireframe-spec`, `error-message-writing`, `frd-writing`, `data-requirements`, `accessibility-audit`
- File: [skills/01-business-analysis/business-analyst/documentation/screen-requirements/SKILL.md](skills/01-business-analysis/business-analyst/documentation/screen-requirements/SKILL.md)

**Specify integration requirements** · `integration-requirements`

- When: Specifies integration requirements between systems, covering participating systems, direction, data exchanged, trigger and frequency, volumes, error handling, security and SLAs, in a form both sides can build and test against. Use when a feature needs data to flow to or from another system, a new interface or API is requested, or a third-party/vendor integration must be agreed before design.
- Try: _"Specify the integration requirements for sending approved orders from our e-commerce platform to the ERP and getting stock levels back."_
- Related: `field-mapping`, `error-scenario-catalog`, `api-contract`, `integration-pattern-selection`, `data-requirements`
- File: [skills/01-business-analysis/business-analyst/documentation/integration-requirements/SKILL.md](skills/01-business-analysis/business-analyst/documentation/integration-requirements/SKILL.md)

#### Requirements Quality

**Find gaps in requirements** · `requirements-gap-analysis`

- When: Reviews a set of requirements (BRD, FRD, user stories, use cases) and detects what is missing: flows, actors and roles, edge cases, error handling, data rules, non-functional requirements and transition needs. Use when requirements look complete but have not been stress-tested, before estimation or sign-off, or when asked 'what are we missing?'.
- Try: _"Here is our FRD for the loan application module. Find the gaps before we send it for estimation."_
- Related: `ambiguity-detection`, `requirements-consistency-check`, `requirements-review-checklist`, `nfr-specification`, `error-scenario-catalog`
- File: [skills/01-business-analysis/business-analyst/quality/requirements-gap-analysis/SKILL.md](skills/01-business-analysis/business-analyst/quality/requirements-gap-analysis/SKILL.md)

**Detect ambiguous requirements** · `ambiguity-detection`

- When: Scans requirements text for vague words, undefined terms, weak or subjective phrases, unbounded lists, passive voice without an actor and untestable statements, and proposes precise rewrites. Use when reviewing requirements, user stories or acceptance criteria for clarity, or when testers or developers say a requirement can be read more than one way.
- Try: _"Check these 20 requirements for ambiguous wording and suggest testable rewrites."_
- Related: `requirements-gap-analysis`, `requirements-consistency-check`, `glossary-builder`, `acceptance-criteria`, `testability-review`
- File: [skills/01-business-analysis/business-analyst/quality/ambiguity-detection/SKILL.md](skills/01-business-analysis/business-analyst/quality/ambiguity-detection/SKILL.md)

**Elicit edge cases** · `edge-case-elicitation`

- When: Systematically surfaces edge cases for a feature, flow, API or requirement across boundaries, empty/null, duplicates, concurrency, time zones and dates, permissions, partial failure, retries and idempotency, volume and abuse, and turns each into an expected behavior or an open question. Use when a story, spec or design looks \"happy-path only\", before acceptance criteria or test design, or when someone asks \"what could go wrong?\" or \"what cases are we missing?\".
- Try: _"Find the edge cases for this story: as a warehouse clerk I want to reserve stock for a customer order so that the items are not sold twice."_
- Related: `acceptance-criteria`, `error-scenario-catalog`, `equivalence-boundary-analysis`, `requirements-gap-analysis`, `test-scenarios-from-requirements`
- File: [skills/01-business-analysis/business-analyst/quality/edge-case-elicitation/SKILL.md](skills/01-business-analysis/business-analyst/quality/edge-case-elicitation/SKILL.md)

**Check requirements consistency** · `requirements-consistency-check`

- When: Compares requirements against each other and against business rules, glossary, data and NFRs to find contradictions, duplicates, overlaps, inconsistent terminology and conflicting values, and proposes a resolution path for each. Use when several documents, authors or versions describe the same scope, after merging stories from multiple teams, or before baselining requirements.
- Try: _"We have a BRD, an FRD and 45 user stories for the same billing scope. Find contradictions and duplicates."_
- Related: `ambiguity-detection`, `requirements-gap-analysis`, `business-rules-catalog`, `glossary-builder`, `traceability-matrix`
- File: [skills/01-business-analysis/business-analyst/quality/requirements-consistency-check/SKILL.md](skills/01-business-analysis/business-analyst/quality/requirements-consistency-check/SKILL.md)

**Check stories against INVEST** · `invest-check`

- When: Evaluates user stories against the INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable), scores each criterion with evidence and gives concrete fixes such as splits, rewrites or missing acceptance criteria. Use when refining a backlog, before stories enter an iteration or commitment, or when a story keeps getting re-estimated or carried over.
- Try: _"Run an INVEST check on these 8 stories for the checkout epic and tell me which ones are not ready."_
- Related: `user-story`, `acceptance-criteria`, `story-splitting`, `definition-of-ready`, `backlog-refinement`
- File: [skills/01-business-analysis/business-analyst/quality/invest-check/SKILL.md](skills/01-business-analysis/business-analyst/quality/invest-check/SKILL.md)

**Build a traceability matrix** · `traceability-matrix`

- When: Builds a requirements traceability matrix linking business goals and sources to requirements, design elements, test cases and releases in both directions, and reports orphans, uncovered requirements and coverage percentages. Use when an audit, regulator or customer needs proof of coverage, before a release or UAT, or when assessing which items a change affects.
- Try: _"Build a traceability matrix from these 30 requirements and 55 test cases and show me what is not covered."_
- Related: `requirements-gap-analysis`, `impact-analysis`, `test-scenarios-from-requirements`, `requirements-sign-off`, `release-quality-gate`
- File: [skills/01-business-analysis/business-analyst/quality/traceability-matrix/SKILL.md](skills/01-business-analysis/business-analyst/quality/traceability-matrix/SKILL.md)

**Prioritize requirements** · `requirements-prioritization`

- When: Prioritizes a set of requirements using a fitting technique (MoSCoW, Kano, value/effort, weighted scoring or cost of delay), makes the criteria explicit, and justifies each ranking with evidence and stated assumptions. Use when scope must be cut to fit a date or budget, stakeholders disagree on what comes first, or a release or MVP scope needs a defensible order.
- Try: _"Prioritize these 25 requirements for the first release with MoSCoW; we have a fixed go-live date."_
- Related: `backlog-prioritization`, `decision-matrix`, `mvp-scoping`, `stakeholder-map`, `requirements-sign-off`
- File: [skills/01-business-analysis/business-analyst/quality/requirements-prioritization/SKILL.md](skills/01-business-analysis/business-analyst/quality/requirements-prioritization/SKILL.md)

**Run a requirements review** · `requirements-review-checklist`

- When: Runs a structured, checklist-driven review of a requirements document or story set before sign-off, covering structure, individual requirement quality (ISO/IEC/IEEE 29148 characteristics), set-level completeness and consistency, NFRs, traceability and approval readiness, and returns findings with a go/no-go recommendation. Use when a BRD, FRD, SRS or backlog slice is about to be baselined, handed to a vendor or approved.
- Try: _"Review this FRD before we send it to the business for sign-off. Use a proper checklist and tell me if it is ready."_
- Related: `ambiguity-detection`, `requirements-gap-analysis`, `requirements-consistency-check`, `requirements-sign-off`, `document-review`
- File: [skills/01-business-analysis/business-analyst/quality/requirements-review-checklist/SKILL.md](skills/01-business-analysis/business-analyst/quality/requirements-review-checklist/SKILL.md)

#### Process Analysis

**Document the as-is process** · `as-is-process`

- When: Documents the current (as-is) business process from interviews, observation notes, procedures or system logs: trigger, steps, actors, systems, inputs/outputs, decision points, timings, volumes, pain points and workarounds. Use when a process is to be improved, automated or replaced and the team first needs a shared, evidence-based picture of how work is actually done today.
- Try: _"Document the as-is process for supplier invoice approval from these interview notes with AP and two department managers."_
- Related: `to-be-process`, `bpmn-model`, `value-stream-map`, `observation-notes`, `interview-notes-analysis`
- File: [skills/01-business-analysis/business-analyst/process/as-is-process/SKILL.md](skills/01-business-analysis/business-analyst/process/as-is-process/SKILL.md)

**Design the to-be process** · `to-be-process`

- When: Designs an improved (to-be) business process from an as-is description, pain points and goals: applies redesign levers (eliminate, simplify, automate, parallelize, move decisions, add controls), shows each change against the as-is, and states expected effects, assumptions and required enablers. Use when a process must be improved, digitized or re-engineered and the target way of working must be agreed before requirements or system design.
- Try: _"Using this as-is invoice approval process and its pain points, design a to-be process that cuts approval time in half."_
- Related: `as-is-process`, `process-gap-analysis`, `bpmn-model`, `value-stream-map`, `business-rules-catalog`
- File: [skills/01-business-analysis/business-analyst/process/to-be-process/SKILL.md](skills/01-business-analysis/business-analyst/process/to-be-process/SKILL.md)

**Describe a process in BPMN** · `bpmn-model`

- When: Turns a process description into a BPMN 2.0 model: pools and lanes, events, tasks, gateways, message flows and data objects, delivered as a structured element list plus diagram code that renders or imports. Use when a process must be drawn formally, when a textual as-is or to-be process needs a diagram, or when someone asks for BPMN, a swimlane diagram or process diagram code.
- Try: _"Model this purchase approval process in BPMN: employee submits request, manager approves up to 10k, above that finance also approves, then procurement orders."_
- Related: `as-is-process`, `to-be-process`, `diagram-as-code`, `business-rules-catalog`, `use-case-spec`
- File: [skills/01-business-analysis/business-analyst/process/bpmn-model/SKILL.md](skills/01-business-analysis/business-analyst/process/bpmn-model/SKILL.md)

**Analyze as-is vs to-be gaps** · `process-gap-analysis`

- When: Compares an as-is process with a to-be process step by step and lists every gap as a required change in people, process, technology, data or policy, with impact, dependencies and an owner. Use when a target process has been designed and the organization needs the change list, work packages or transition plan to get there, or when asked 'what has to change to go from as-is to to-be?'.
- Try: _"Here are the as-is and to-be versions of our invoice approval process. Give me the gap analysis and what has to change."_
- Related: `as-is-process`, `to-be-process`, `impact-analysis`, `fit-gap-analysis`, `raci-matrix`
- File: [skills/01-business-analysis/business-analyst/process/process-gap-analysis/SKILL.md](skills/01-business-analysis/business-analyst/process/process-gap-analysis/SKILL.md)

**Map a value stream** · `value-stream-map`

- When: Maps a value stream from customer request to delivered value, separating process time from wait time for every step, classifying steps as value-adding, necessary non-value-adding or waste, and computing lead time, process time, flow efficiency and rework rates. Use when a process or delivery flow feels slow, when lead time must be reduced, or when someone asks where the waste, waiting or bottleneck is.
- Try: _"Map the value stream for our customer onboarding: from application to active account it takes about 12 days and we want to know where the time goes."_
- Related: `as-is-process`, `to-be-process`, `cycle-time-analysis`, `five-whys`, `process-gap-analysis`
- File: [skills/01-business-analysis/business-analyst/process/value-stream-map/SKILL.md](skills/01-business-analysis/business-analyst/process/value-stream-map/SKILL.md)

#### Solution Assessment

**Assess feasibility** · `feasibility-study`

- When: Assesses whether a proposed initiative or solution option is feasible across technical, operational, economic, schedule, legal/compliance and organizational dimensions, rates each with evidence, names the conditions and showstoppers, and recommends go, go with conditions or no-go. Use when an idea or request must be vetted before investment, when comparing solution options at a high level, or when asked 'can we actually do this?'.
- Try: _"Assess the feasibility of replacing our on-prem CRM with a SaaS CRM within 6 months; we have 2 developers and strict KVKK requirements."_
- Related: `cost-benefit-analysis`, `build-vs-buy`, `pre-mortem`, `risk-register`, `technology-selection`
- File: [skills/01-business-analysis/business-analyst/solution/feasibility-study/SKILL.md](skills/01-business-analysis/business-analyst/solution/feasibility-study/SKILL.md)

**Run a cost-benefit analysis** · `cost-benefit-analysis`

- When: Quantifies the costs and benefits of an initiative or of competing options over a defined horizon, separating one-off and recurring items, tangible and intangible benefits, and computes net benefit, ROI, payback period and optionally NPV with sensitivity on the key assumptions. Use when a business case, investment decision or option comparison needs numbers, or when asked 'is it worth it?' or 'what is the ROI?'.
- Try: _"Run a cost-benefit analysis for automating invoice matching: licence 40k/year, implementation 120k, it should save 3 FTE of manual work."_
- Related: `feasibility-study`, `budget-proposal`, `cloud-cost-estimate`, `benefits-realization`, `decision-matrix`
- File: [skills/01-business-analysis/business-analyst/solution/cost-benefit-analysis/SKILL.md](skills/01-business-analysis/business-analyst/solution/cost-benefit-analysis/SKILL.md)

**Analyze change impact** · `impact-analysis`

- When: Analyzes the impact of a proposed change on processes, systems, interfaces, data, reports, users, documents, controls and tests, following direct and indirect dependencies, and rates each impact with evidence and confidence. Use when a new requirement, change request, rule change or system modification is proposed and the team must know what else it touches before estimating, approving or releasing it.
- Try: _"What is the impact of changing the customer ID from numeric to alphanumeric in our core banking system?"_
- Related: `change-request-analysis`, `traceability-matrix`, `process-gap-analysis`, `regression-selection`, `dependency-map`
- File: [skills/01-business-analysis/business-analyst/solution/impact-analysis/SKILL.md](skills/01-business-analysis/business-analyst/solution/impact-analysis/SKILL.md)

**Analyze a change request** · `change-request-analysis`

- When: Analyzes a change request against the agreed baseline: classifies it (new scope, modification, clarification, defect in disguise), assesses value, scope, effort drivers, schedule, cost and risk impact, lists options and recommends accept, accept with trade-off, defer or reject with rationale for the change authority. Use when a stakeholder asks to add or change something after requirements were baselined or during delivery, or when a change control board needs a decision paper.
- Try: _"Marketing wants to add SMS notifications to the loyalty release two weeks before go-live. Analyze the change request and give a recommendation."_
- Related: `impact-analysis`, `change-control`, `change-request-rfc`, `requirements-sign-off`, `trade-off-analysis`
- File: [skills/01-business-analysis/business-analyst/solution/change-request-analysis/SKILL.md](skills/01-business-analysis/business-analyst/solution/change-request-analysis/SKILL.md)

**Prepare requirements sign-off** · `requirements-sign-off`

- When: Prepares a requirements sign-off package: the baseline being approved (documents, versions, requirement IDs), what changed since the last review, open issues and accepted risks, conditions, the approvers needed and how later changes will be controlled. Use when requirements are reviewed and ready to be baselined, when a sponsor asks 'what exactly am I signing?', or before design, build or a contract milestone starts.
- Try: _"Prepare the sign-off package for the claims portal FRD v1.3 so the business owner and IT lead can approve it this week."_
- Related: `requirements-review-checklist`, `traceability-matrix`, `change-control`, `change-request-analysis`, `decision-log`
- File: [skills/01-business-analysis/business-analyst/solution/requirements-sign-off/SKILL.md](skills/01-business-analysis/business-analyst/solution/requirements-sign-off/SKILL.md)

### System Analyst

#### System Specification

**Write a Software Requirements Specification** · `srs-writing`

- When: Writes a Software Requirements Specification aligned with ISO/IEC/IEEE 29148: purpose and scope, system context and interfaces, functional requirements, quality attributes, data, constraints and verification method per requirement, each uniquely identified and traceable. Use when a system or subsystem must be specified for design, build, a vendor or an audit, or when business requirements must be turned into a verifiable system-level specification.
- Try: _"Write an SRS for the payment reconciliation service based on this FRD and the interface list."_
- Related: `frd-writing`, `nfr-specification`, `use-case-spec`, `integration-requirements`, `traceability-matrix`
- File: [skills/01-business-analysis/system-analyst/specification/srs-writing/SKILL.md](skills/01-business-analysis/system-analyst/specification/srs-writing/SKILL.md)

**Model entity states** · `state-model`

- When: Models the lifecycle of a business entity (order, application, claim, contract, ticket): states, transitions, triggering events, guard conditions, actions, who may trigger each transition, and invalid transitions, delivered as a transition table plus diagram code. Use when an entity has statuses that drive behaviour, when status rules are scattered or disputed, or before designing workflows, APIs or state transition tests.
- Try: _"Model the states of an insurance claim from submission to payment or rejection, including reopen and cancel."_
- Related: `business-rules-catalog`, `state-transition-testing`, `sequence-flow`, `error-scenario-catalog`, `diagram-as-code`
- File: [skills/01-business-analysis/system-analyst/specification/state-model/SKILL.md](skills/01-business-analysis/system-analyst/specification/state-model/SKILL.md)

**Describe a system interaction sequence** · `sequence-flow`

- When: Describes how systems, services and actors interact in one end-to-end scenario: participants, ordered messages, sync or async style, payload essentials, responses, timeouts, retries and alternative or failure paths, delivered as a step table plus sequence diagram code. Use when a scenario crosses several systems, when integration behaviour must be agreed between teams, or when someone asks 'what calls what, in which order, and what happens if it fails?'.
- Try: _"Describe the sequence for an online order: web shop, order service, payment gateway, stock service and notification, including payment timeout."_
- Related: `integration-requirements`, `api-contract`, `error-scenario-catalog`, `state-model`, `diagram-as-code`
- File: [skills/01-business-analysis/system-analyst/specification/sequence-flow/SKILL.md](skills/01-business-analysis/system-analyst/specification/sequence-flow/SKILL.md)

**Map fields between systems** · `field-mapping`

- When: Produces a source-to-target field mapping between two systems or messages: each target field with its source, transformation, default, validation, code-value translation, null and error handling, plus unmapped fields on both sides and open decisions. Use when building an integration, API adapter, data exchange file or system replacement, when two systems must exchange records, or when someone asks 'which field goes where and how is it converted?'.
- Try: _"Map the customer fields from our CRM export to the new billing system's customer API, including code conversions."_
- Related: `integration-requirements`, `api-contract`, `source-to-target-mapping`, `data-quality-rules`, `error-scenario-catalog`
- File: [skills/01-business-analysis/system-analyst/specification/field-mapping/SKILL.md](skills/01-business-analysis/system-analyst/specification/field-mapping/SKILL.md)

**Catalog error scenarios** · `error-scenario-catalog`

- When: Builds a catalog of error scenarios for a feature, flow or interface: each failure case with trigger, detection point, expected system behaviour, data state afterwards, user or caller message, error code, logging and alerting, and recovery path. Use when requirements describe only the happy path, before design or test of an integration or transaction flow, or when support and developers disagree on what the system should do when something fails.
- Try: _"Create an error scenario catalog for our money transfer flow: validation, limits, core banking timeout and duplicate submissions."_
- Related: `error-message-writing`, `edge-case-elicitation`, `sequence-flow`, `resilience-review`, `test-case-writing`
- File: [skills/01-business-analysis/system-analyst/specification/error-scenario-catalog/SKILL.md](skills/01-business-analysis/system-analyst/specification/error-scenario-catalog/SKILL.md)

## Product Management

### Product Manager

#### Product Strategy

**Write a product vision** · `product-vision`

- When: Writes an inspiring, testable product vision statement and a vision board covering target group, needs, product, and business goals. Use when a new product or major pivot needs a shared north, when teams disagree on what the product is for, or when someone asks for a vision statement, vision board or \"why does this product exist\".
- Try: _"Write a product vision and vision board for our self-service invoice portal for small business customers."_
- Related: `product-strategy-one-pager`, `positioning-statement`, `north-star-metric`, `persona`, `okr-definition`
- File: [skills/02-product/product-manager/strategy/product-vision/SKILL.md](skills/02-product/product-manager/strategy/product-vision/SKILL.md)

**Write a product strategy one-pager** · `product-strategy-one-pager`

- When: Writes a one-page product strategy that states the diagnosis, where to play, how to win, the few strategic bets and explicit non-goals, linked to vision and outcome metrics. Use when a product needs a strategy for the next 12-24 months, when a roadmap lacks a rationale, or when leadership asks \"what is our product strategy\".
- Try: _"Draft a product strategy one-pager for our B2B field service app for the next 18 months."_
- Related: `product-vision`, `market-analysis`, `competitor-analysis`, `okr-definition`, `roadmap`
- File: [skills/02-product/product-manager/strategy/product-strategy-one-pager/SKILL.md](skills/02-product/product-manager/strategy/product-strategy-one-pager/SKILL.md)

**Define OKRs** · `okr-definition`

- When: Writes outcome-based objectives with 2-5 measurable key results each, including baselines, targets, measurement source and owner, and flags output-style or unmeasurable KRs. Use when a team plans a quarter or half-year, when strategy must be turned into measurable goals, or when someone asks to write or review OKRs.
- Try: _"Write Q3 OKRs for our onboarding team based on the goal of getting new customers to value faster."_
- Related: `product-strategy-one-pager`, `north-star-metric`, `kpi-definition`, `goal-setting`, `quarterly-planning`
- File: [skills/02-product/product-manager/strategy/okr-definition/SKILL.md](skills/02-product/product-manager/strategy/okr-definition/SKILL.md)

**Analyze a market** · `market-analysis`

- When: Structures a market analysis with TAM/SAM/SOM sizing (top-down and bottom-up, with every figure sourced or marked as assumption), segments, trends, drivers and barriers. Use when evaluating a new market, product idea or expansion, when a business case needs market size, or when someone asks how big a market is or which segment to target.
- Try: _"Do a market analysis for a scheduling SaaS for independent physiotherapy clinics in Turkey."_
- Related: `competitor-analysis`, `business-model-canvas`, `product-strategy-one-pager`, `persona`, `pricing-analysis`
- File: [skills/02-product/product-manager/strategy/market-analysis/SKILL.md](skills/02-product/product-manager/strategy/market-analysis/SKILL.md)

**Analyze competitors** · `competitor-analysis`

- When: Compares direct, indirect and substitute competitors on target segment, jobs served, features, pricing and positioning, then identifies gaps, threats and differentiation opportunities with dated sources. Use when entering a market, planning strategy or positioning, preparing for sales losses, or when someone asks how a product stacks up against rivals.
- Try: _"Compare our expense management app with the main competitors used by Turkish SMEs and show where we can differentiate."_
- Related: `market-analysis`, `positioning-statement`, `pricing-analysis`, `product-strategy-one-pager`, `swot-analysis`
- File: [skills/02-product/product-manager/strategy/competitor-analysis/SKILL.md](skills/02-product/product-manager/strategy/competitor-analysis/SKILL.md)

**Run a PESTLE analysis** · `pestle-analysis`

- When: Runs a PESTLE analysis (political, economic, social, technological, legal, environmental) for a product, market entry or strategic decision, rating each factor by impact, likelihood and time horizon and translating the top factors into concrete product and business implications. Use when entering a new market or country, reviewing a strategy or roadmap, assessing regulatory or macro risk, or when someone asks for a PESTEL/PEST or \"external environment\" scan.
- Try: _"Do a PESTLE analysis for launching our SME payroll SaaS in Germany next year."_
- Related: `market-analysis`, `swot-analysis`, `porters-five-forces`, `product-strategy-one-pager`, `assumption-mapping`
- File: [skills/02-product/product-manager/strategy/pestle-analysis/SKILL.md](skills/02-product/product-manager/strategy/pestle-analysis/SKILL.md)

**Analyze Porter's five forces** · `porters-five-forces`

- When: Analyzes an industry or market segment with Porter's five forces (rivalry, threat of new entrants, threat of substitutes, buyer power, supplier power), rates each force with its drivers and evidence, and derives what the structure means for profitability, positioning and product strategy. Use when assessing the attractiveness of a market or segment, preparing a strategy or entry decision, explaining margin pressure, or when someone asks for a five forces or industry structure analysis.
- Try: _"Run a five forces analysis for the mid-market field service management software segment in Turkey; we are deciding whether to enter it."_
- Related: `pestle-analysis`, `competitor-analysis`, `market-analysis`, `swot-analysis`, `pricing-analysis`
- File: [skills/02-product/product-manager/strategy/porters-five-forces/SKILL.md](skills/02-product/product-manager/strategy/porters-five-forces/SKILL.md)

**Build a competitive battle card** · `competitive-battle-card`

- When: Builds a one-page competitive battle card for sales and presales against a named competitor, covering when we win and lose, strengths and weaknesses on both sides, discovery and landmine questions, objection handling with proof points and quick-dismiss answers. Use when sales meets a competitor in deals, before a competitive pitch or RFP, when win/loss notes need to become field guidance, or when someone asks for a \"battle card\", \"kill sheet\" or \"how do we beat X\".
- Try: _"Build a battle card for our sales team against VendorX; we keep losing mid-size deals to them on price but win when integrations matter."_
- Related: `competitor-analysis`, `positioning-statement`, `pricing-analysis`, `rfp-response`, `elevator-pitch`
- File: [skills/02-product/product-manager/strategy/competitive-battle-card/SKILL.md](skills/02-product/product-manager/strategy/competitive-battle-card/SKILL.md)

**Fill a business/lean canvas** · `business-model-canvas`

- When: Completes a Business Model Canvas or Lean Canvas for a product idea, separating evidence from assumptions and ranking the riskiest assumptions to test first. Use when a new idea, venture or product line needs its business logic laid out, when comparing business model options, or when someone asks for a business model or lean canvas.
- Try: _"Fill a lean canvas for a marketplace that connects freelance accountants with small e-commerce sellers."_
- Related: `market-analysis`, `pricing-analysis`, `assumption-mapping`, `hypothesis-statement`, `product-vision`
- File: [skills/02-product/product-manager/strategy/business-model-canvas/SKILL.md](skills/02-product/product-manager/strategy/business-model-canvas/SKILL.md)

**Analyze pricing options** · `pricing-analysis`

- When: Compares pricing models (flat, tiered, per-seat, usage-based, freemium, hybrid) against value metric, cost-to-serve, competitor anchors and willingness-to-pay signals, and recommends a model with price-test options. Use when launching a product, adding a paid tier, revisiting prices, or when someone asks how to price or package a product.
- Try: _"Analyze pricing options for our API monitoring tool; today it is a flat 49 USD per month."_
- Related: `market-analysis`, `competitor-analysis`, `business-model-canvas`, `experiment-design`, `persona`
- File: [skills/02-product/product-manager/strategy/pricing-analysis/SKILL.md](skills/02-product/product-manager/strategy/pricing-analysis/SKILL.md)

#### Discovery

**Build a persona** · `persona`

- When: Builds an evidence-based persona with context, goals, pains, behaviors, decision criteria and quotes, tracing every attribute to research and flagging proto-persona assumptions. Use when research data (interviews, surveys, analytics, support tickets) must be turned into a shared user model, or when someone asks for a persona or user profile for design and product decisions.
- Try: _"Create a persona for warehouse shift supervisors from these 8 interview summaries."_
- Related: `jobs-to-be-done`, `customer-journey-map`, `research-synthesis`, `feedback-synthesis`, `problem-interview-script`
- File: [skills/02-product/product-manager/discovery/persona/SKILL.md](skills/02-product/product-manager/discovery/persona/SKILL.md)

**Frame Jobs-to-be-Done** · `jobs-to-be-done`

- When: Frames Jobs-to-be-Done by writing a solution-free core job statement, related and emotional/social jobs, job steps, and measurable desired outcome statements that can be prioritized by importance and satisfaction. Use when defining what customers are trying to get done, when innovation or roadmap work needs a solution-agnostic frame, or when someone asks for JTBD, job stories or desired outcomes.
- Try: _"Frame the jobs-to-be-done for restaurant owners who manage supplier orders."_
- Related: `persona`, `opportunity-solution-tree`, `customer-journey-map`, `problem-interview-script`, `feedback-synthesis`
- File: [skills/02-product/product-manager/discovery/jobs-to-be-done/SKILL.md](skills/02-product/product-manager/discovery/jobs-to-be-done/SKILL.md)

**Fill a value proposition canvas** · `value-proposition-canvas`

- When: Fills a value proposition canvas for one customer segment, mapping customer jobs, pains and gains to products and services, pain relievers and gain creators, ranks them by importance, checks problem-solution fit and lists the assumptions to test. Use when defining or sharpening a value proposition, checking whether a product idea addresses real pains, preparing positioning or discovery work, or when someone asks for a \"value proposition canvas\" or \"fit\" analysis.
- Try: _"Fill a value proposition canvas for our expense app for field sales reps at mid-size distributors."_
- Related: `jobs-to-be-done`, `persona`, `positioning-statement`, `business-model-canvas`, `hypothesis-statement`
- File: [skills/02-product/product-manager/discovery/value-proposition-canvas/SKILL.md](skills/02-product/product-manager/discovery/value-proposition-canvas/SKILL.md)

**Map the customer journey** · `customer-journey-map`

- When: Maps a customer journey for one persona and scenario across stages, with actions, thoughts, emotions, touchpoints, channels, pains, moments of truth and backstage owners, and ranks improvement opportunities. Use when you need to understand an end-to-end experience, find where customers struggle or drop out, align teams across channels, or when someone asks for a journey map.
- Try: _"Map the customer journey for a first-time buyer of home insurance through our website and call center."_
- Related: `persona`, `jobs-to-be-done`, `funnel-analysis`, `user-flow`, `as-is-process`
- File: [skills/02-product/product-manager/discovery/customer-journey-map/SKILL.md](skills/02-product/product-manager/discovery/customer-journey-map/SKILL.md)

**Build an opportunity solution tree** · `opportunity-solution-tree`

- When: Builds an opportunity solution tree that links one measurable outcome to customer opportunities (needs, pains, desires) from research, several candidate solutions per target opportunity, and assumption tests. Use when a team must choose what to work on to move an outcome, when discovery work lacks structure, or when someone asks to connect a goal to ideas and experiments.
- Try: _"Build an opportunity solution tree for increasing 30-day retention of new mobile banking users."_
- Related: `okr-definition`, `jobs-to-be-done`, `hypothesis-statement`, `experiment-design`, `assumption-mapping`
- File: [skills/02-product/product-manager/discovery/opportunity-solution-tree/SKILL.md](skills/02-product/product-manager/discovery/opportunity-solution-tree/SKILL.md)

**Write a product hypothesis** · `hypothesis-statement`

- When: Turns a product idea, feature request or assumption into a falsifiable hypothesis in the \"We believe / will result in / We will know when\" format, with the target segment, the riskiest assumption, a measurable signal, a threshold and a time box. Use when a team wants to test an idea before building it fully, when a backlog item lacks a clear expected outcome, or when someone asks to write, sharpen or review a product hypothesis.
- Try: _"Write a hypothesis for adding a \"save cart for later\" button; we think it will reduce checkout abandonment on mobile."_
- Related: `experiment-design`, `assumption-mapping`, `opportunity-solution-tree`, `problem-statement`, `ab-test-analysis`
- File: [skills/02-product/product-manager/discovery/hypothesis-statement/SKILL.md](skills/02-product/product-manager/discovery/hypothesis-statement/SKILL.md)

**Design a product experiment** · `experiment-design`

- When: Designs a product experiment (A/B test, fake-door, painted-door, concierge or prototype test) from a hypothesis, with variants, randomization unit, primary and guardrail metrics, minimum detectable effect, sample size and duration, stop rules and a pre-committed decision rule. Use when a team wants to validate a hypothesis with real users, asks how to set up an A/B or fake-door test, or needs to check an experiment plan before launch.
- Try: _"Design an A/B test for our new pricing page layout; we get about 40,000 visitors a week and trial sign-up is 3.2%."_
- Related: `hypothesis-statement`, `ab-test-analysis`, `assumption-mapping`, `metric-definition`, `funnel-analysis`
- File: [skills/02-product/product-manager/discovery/experiment-design/SKILL.md](skills/02-product/product-manager/discovery/experiment-design/SKILL.md)

**Synthesize customer feedback** · `feedback-synthesis`

- When: Clusters raw customer feedback (support tickets, NPS/CSAT verbatims, app reviews, sales notes, community posts) into themes with frequency, severity, affected segments, representative anonymized quotes and the underlying need behind each request. Use when a pile of feedback must be turned into prioritizable insights, when someone asks \"what are customers telling us\", or before roadmap and backlog discussions.
- Try: _"Here are 120 NPS comments from last quarter; group them into themes and tell me what matters most."_
- Related: `research-synthesis`, `jobs-to-be-done`, `opportunity-solution-tree`, `persona`, `backlog-prioritization`
- File: [skills/02-product/product-manager/discovery/feedback-synthesis/SKILL.md](skills/02-product/product-manager/discovery/feedback-synthesis/SKILL.md)

**Write a problem interview script** · `problem-interview-script`

- When: Writes a non-leading customer problem interview script in the spirit of The Mom Test, asking about past behavior, real spending and current workarounds instead of opinions or pitches, with a funnel-ordered guide, follow-up probes, commitment signals and a note-taking sheet. Use when a team wants to validate that a problem exists before building, prepares discovery interviews, or asks to review questions that may be leading or hypothetical.
- Try: _"Write a problem interview script to check whether small clinic owners actually struggle with appointment no-shows."_
- Related: `interview-question-set`, `research-plan`, `screener-survey`, `jobs-to-be-done`, `research-synthesis`
- File: [skills/02-product/product-manager/discovery/problem-interview-script/SKILL.md](skills/02-product/product-manager/discovery/problem-interview-script/SKILL.md)

#### Product Definition

**Write a Product Requirements Document** · `prd-writing`

- When: Writes a Product Requirements Document covering problem and evidence, goals and success metrics, target users, scope and non-goals, prioritized requirements with acceptance criteria, user experience, non-functional needs, dependencies, risks, release plan and open questions. Use when a product initiative must be aligned across engineering, design and stakeholders before build, when someone asks for a PRD or product spec, or when an existing PRD needs a review for gaps.
- Try: _"Write a PRD for letting B2B customers set approval workflows on purchase orders above a threshold."_
- Related: `feature-brief`, `mvp-scoping`, `epic-breakdown`, `nfr-specification`, `acceptance-criteria`
- File: [skills/02-product/product-manager/definition/prd-writing/SKILL.md](skills/02-product/product-manager/definition/prd-writing/SKILL.md)

**Write a feature brief** · `feature-brief`

- When: Writes a one-page feature brief that aligns a team on a single feature: the problem and who has it, the expected outcome and success signal, the proposed approach, scope boundaries, key risks and the decisions still needed. Use when a feature is small enough not to need a full PRD, when a stakeholder asks for \"a quick write-up\" before a kickoff or refinement, or when a request must be framed for a go/no-go conversation.
- Try: _"Write a feature brief for adding bulk CSV import of contacts to our CRM."_
- Related: `prd-writing`, `hypothesis-statement`, `mvp-scoping`, `epic-breakdown`, `problem-statement`
- File: [skills/02-product/product-manager/definition/feature-brief/SKILL.md](skills/02-product/product-manager/definition/feature-brief/SKILL.md)

**Scope an MVP** · `mvp-scoping`

- When: Cuts a product or feature scope down to the smallest release that tests the riskiest value assumption with real users, using an assumption-led cut, a must/later/never scope table, explicit quality floor, learning goals and exit criteria. Use when a scope is too big for the available time, when someone asks \"what is our MVP\", or when a team must decide what to leave out of a first release.
- Try: _"We have 8 weeks and a 40-item feature list for a field-service scheduling app; help me scope the MVP."_
- Related: `hypothesis-statement`, `story-mapping`, `prd-writing`, `assumption-mapping`, `release-planning`
- File: [skills/02-product/product-manager/definition/mvp-scoping/SKILL.md](skills/02-product/product-manager/definition/mvp-scoping/SKILL.md)

**Break an epic into stories** · `epic-breakdown`

- When: Decomposes an epic into thin, vertical, independently valuable stories with a specific persona, a real outcome and a walking-skeleton first slice, ordered by value, risk and dependency. Use when an epic, initiative or large feature must become backlog items, when stories keep coming out as layers (UI/API/DB) or technical tasks, or when a team asks \"how do we split this epic\".
- Try: _"Break this epic into stories: \"Self-service contract renewal for SME customers in the customer portal\"."_
- Related: `story-splitting`, `user-story`, `acceptance-criteria`, `story-mapping`, `invest-check`
- File: [skills/02-product/product-manager/definition/epic-breakdown/SKILL.md](skills/02-product/product-manager/definition/epic-breakdown/SKILL.md)

**Build a user story map** · `story-mapping`

- When: Builds a user story map with a left-to-right backbone of user activities and steps, stories stacked by priority beneath each step, and horizontal release slices that each deliver a usable end-to-end outcome. Use when planning a product or large feature across the whole user journey, when the flat backlog has lost the big picture, or when a team must agree on what goes into the first and following releases.
- Try: _"Build a story map for our B2B expense management app, from employee submitting a receipt to finance reimbursing it."_
- Related: `epic-breakdown`, `mvp-scoping`, `release-planning`, `customer-journey-map`, `roadmap`
- File: [skills/02-product/product-manager/definition/story-mapping/SKILL.md](skills/02-product/product-manager/definition/story-mapping/SKILL.md)

#### Metrics

**Define a North Star metric** · `north-star-metric`

- When: Selects a North Star metric that captures the value customers get from the product and links it to revenue, then decomposes it into a tree of 3-5 controllable input metrics with owners and counter-metrics. Use when a product team lacks a shared value metric, when teams optimize conflicting numbers, or when someone asks \"what should our North Star be\" or wants a metric tree for a product.
- Try: _"Define a North Star metric and input metric tree for our B2B invoicing SaaS for small businesses."_
- Related: `kpi-definition`, `okr-definition`, `metric-definition`, `product-strategy-one-pager`, `funnel-analysis`
- File: [skills/02-product/product-manager/metrics/north-star-metric/SKILL.md](skills/02-product/product-manager/metrics/north-star-metric/SKILL.md)

**Define KPIs** · `kpi-definition`

- When: Defines product KPIs as an unambiguous KPI sheet with name, purpose, formula, inclusion rules, data source, baseline, target, thresholds, owner, cadence and the decision each KPI informs. Use when a product, feature or team needs a KPI set, when existing KPIs are vague or disputed, or when someone asks \"which KPIs should we track and how exactly are they calculated\".
- Try: _"Define the KPIs for our new mobile self check-in feature at hotels."_
- Related: `north-star-metric`, `metric-definition`, `okr-definition`, `dashboard-spec`, `feature-adoption-review`
- File: [skills/02-product/product-manager/metrics/kpi-definition/SKILL.md](skills/02-product/product-manager/metrics/kpi-definition/SKILL.md)

**Analyze a funnel** · `funnel-analysis`

- When: Analyzes a conversion funnel step by step, computing step and cumulative conversion, locating the biggest absolute drop-offs, segmenting them, separating data artefacts from real behaviour and turning findings into ranked, testable improvement hypotheses. Use when given funnel numbers or event data for sign-up, onboarding, checkout or activation, or when someone asks \"where are we losing users and why\".
- Try: _"Here are our sign-up funnel numbers for last month by step and device; find where we lose users and what to try."_
- Related: `experiment-design`, `hypothesis-statement`, `customer-journey-map`, `north-star-metric`, `data-exploration`
- File: [skills/02-product/product-manager/metrics/funnel-analysis/SKILL.md](skills/02-product/product-manager/metrics/funnel-analysis/SKILL.md)

**Review feature adoption** · `feature-adoption-review`

- When: Reviews a shipped feature's adoption, retention and outcome against the goals set before launch, using a reach-activation-retention-outcome breakdown, segment cuts and qualitative signals, and ends with a keep, iterate, promote or retire recommendation. Use some weeks after a release, in a post-launch review, or when someone asks \"is anyone using this feature and did it work\".
- Try: _"Review adoption of the bulk-edit feature we shipped 8 weeks ago; here are usage numbers and support tickets."_
- Related: `kpi-definition`, `funnel-analysis`, `feedback-synthesis`, `benefits-realization`, `product-sunset-plan`
- File: [skills/02-product/product-manager/metrics/feature-adoption-review/SKILL.md](skills/02-product/product-manager/metrics/feature-adoption-review/SKILL.md)

#### Launch

**Write a go-to-market plan** · `go-to-market-plan`

- When: Writes a go-to-market plan for a product or major feature covering launch tier, target segment and buyer, positioning and messages, channels, pricing and packaging hooks, timeline with readiness gates, sales/support enablement and launch success metrics. Use when a product, feature or market entry is heading to launch, when someone asks for a GTM or launch plan, or when marketing, sales and support need one aligned plan.
- Try: _"Write a go-to-market plan for launching our AI-assisted invoice matching module to existing mid-market ERP customers."_
- Related: `positioning-statement`, `release-announcement`, `pricing-analysis`, `competitive-battle-card`, `communication-plan`
- File: [skills/02-product/product-manager/launch/go-to-market-plan/SKILL.md](skills/02-product/product-manager/launch/go-to-market-plan/SKILL.md)

**Write a release announcement** · `release-announcement`

- When: Writes a customer-facing release announcement that leads with the benefit to the reader, explains what changed and who it affects, states availability and any action required, and ends with a clear next step, adapted to the channel (email, blog, in-app, social). Use when a feature or product version ships to customers, when release notes must be turned into marketing-ready copy, or when someone asks to \"announce\" or \"tell customers about\" a release.
- Try: _"Write a customer announcement for our new bulk-invoice upload feature, going out by email and in-app next Tuesday."_
- Related: `positioning-statement`, `go-to-market-plan`, `release-notes`, `announcement`, `microcopy`
- File: [skills/02-product/product-manager/launch/release-announcement/SKILL.md](skills/02-product/product-manager/launch/release-announcement/SKILL.md)

**Write a positioning statement** · `positioning-statement`

- When: Writes a product or feature positioning statement in the For/Who/Is a/That/Unlike/Our product format, grounded in a specific target segment, a real alternative and a provable differentiator, plus the proof points and messaging guardrails that follow from it. Use when launching a product or major feature, when sales and marketing describe the product inconsistently, or when someone asks \"how do we position this\" or \"what makes us different\".
- Try: _"Write a positioning statement for our new invoice-matching module aimed at mid-size manufacturers' finance teams."_
- Related: `value-proposition-canvas`, `competitor-analysis`, `persona`, `go-to-market-plan`, `elevator-pitch`
- File: [skills/02-product/product-manager/launch/positioning-statement/SKILL.md](skills/02-product/product-manager/launch/positioning-statement/SKILL.md)

**Write a working-backwards press release and FAQ** · `press-release-faq`

- When: Writes a working-backwards press release dated at a future launch, plus a customer FAQ and an internal FAQ, to test whether a product idea is compelling, clear and feasible before anything is built; ends with the open questions and risks the document exposed. Use when a new product or major feature is proposed, when a team needs to align on the customer outcome before design, or when someone asks for a \"PR/FAQ\", \"working backwards\" document or \"future press release\".
- Try: _"Write a working-backwards PR/FAQ for a feature that lets our B2B customers get a delivery ETA on WhatsApp without logging into the portal."_
- Related: `product-vision`, `prd-writing`, `value-proposition-canvas`, `positioning-statement`, `pre-mortem`
- File: [skills/02-product/product-manager/launch/press-release-faq/SKILL.md](skills/02-product/product-manager/launch/press-release-faq/SKILL.md)

#### Product Lifecycle

**Plan a product or feature end-of-life** · `product-sunset-plan`

- When: Plans the end-of-life of a product, plan or feature with explicit sunset decision criteria, affected-customer segmentation, migration paths, a staged communication sequence, timeline gates and data retention/deletion handling. Use when a product or feature is being retired, replaced or consolidated, or when someone asks \"how do we shut this down without losing customers or trust\".
- Try: _"We want to retire our legacy reporting module next year and move everyone to the new analytics dashboard. Draft the sunset plan."_
- Related: `communication-plan`, `migration-strategy`, `api-deprecation-plan`, `impact-analysis`, `kpi-definition`
- File: [skills/02-product/product-manager/lifecycle/product-sunset-plan/SKILL.md](skills/02-product/product-manager/lifecycle/product-sunset-plan/SKILL.md)

### Product Owner

#### Backlog Management

**Refine the backlog** · `backlog-refinement`

- When: Prepares a set of backlog items for a refinement session and turns them into clear, right-sized, estimate-ready and ordered work items with acceptance criteria, open questions and a readiness verdict. Use when a backlog needs grooming, items are vague or too big before iteration/sprint planning, or someone asks to refine, clean up or get stories ready.
- Try: _"Refine these 8 backlog items for next week's planning; tell me which are ready, which need splitting and what we still have to ask the business."_
- Related: `story-splitting`, `definition-of-ready`, `acceptance-criteria`, `backlog-prioritization`, `estimation-session`
- File: [skills/02-product/product-owner/backlog/backlog-refinement/SKILL.md](skills/02-product/product-owner/backlog/backlog-refinement/SKILL.md)

**Prioritize the backlog** · `backlog-prioritization`

- When: Orders backlog items with an explicit, defensible method (WSJF, RICE, value/effort, MoSCoW or cost of delay) and produces a ranked list with scores, rationale, sensitivity notes and items to drop or defer. Use when a product owner must decide what comes next, stakeholders dispute priorities, or someone asks to rank, score or justify backlog order.
- Try: _"Prioritize these 12 backlog items with WSJF; effort estimates are in the table, value comes from sales and support feedback."_
- Related: `backlog-refinement`, `requirements-prioritization`, `portfolio-prioritization`, `roadmap`, `decision-matrix`
- File: [skills/02-product/product-owner/backlog/backlog-prioritization/SKILL.md](skills/02-product/product-owner/backlog/backlog-prioritization/SKILL.md)

**Split large stories** · `story-splitting`

- When: Splits a large user story or work item into thin, independently valuable vertical slices using named patterns (workflow step, business rule, data variation, interface, operation, happy/unhappy path, spike) and shows acceptance criteria and a suggested order for each slice. Use when a story is too big for one iteration/sprint, estimates are wide, or someone asks to break down, slice or split a story.
- Try: _"This story is 21 points and nobody trusts the estimate: 'As a customer I want to pay my invoice online.' Split it."_
- Related: `epic-breakdown`, `invest-check`, `backlog-refinement`, `acceptance-criteria`, `user-story`
- File: [skills/02-product/product-owner/backlog/story-splitting/SKILL.md](skills/02-product/product-owner/backlog/story-splitting/SKILL.md)

**Define Definition of Ready** · `definition-of-ready`

- When: Creates or revises a team's Definition of Ready: the entry criteria a work item must meet before the team commits to or starts it, tailored to item types, with how each criterion is checked and when exceptions are allowed. Use when a team keeps starting unclear work, planning stalls on missing information, or someone asks for a DoR, readiness criteria or an entry checklist.
- Try: _"Write a Definition of Ready for our team; we build a B2B web portal and keep getting blocked by missing API contracts and UX designs."_
- Related: `definition-of-done`, `backlog-refinement`, `invest-check`, `acceptance-criteria`, `working-agreement`
- File: [skills/02-product/product-owner/backlog/definition-of-ready/SKILL.md](skills/02-product/product-owner/backlog/definition-of-ready/SKILL.md)

**Define Definition of Done** · `definition-of-done`

- When: Creates or revises a Definition of Done: the shared quality checklist every increment or work item must pass to count as complete, layered by item, release and organization level, with verification method per criterion and a plan to close gaps. Use when 'done' means different things to different people, quality escapes to production, or someone asks for a DoD or completion criteria.
- Try: _"Draft a Definition of Done for our mobile banking team; we have code review and unit tests but releases still break accessibility and security checks."_
- Related: `definition-of-ready`, `release-quality-gate`, `acceptance-criteria`, `coding-standards`, `working-agreement`
- File: [skills/02-product/product-owner/backlog/definition-of-done/SKILL.md](skills/02-product/product-owner/backlog/definition-of-done/SKILL.md)

**Check backlog health** · `backlog-health-check`

- When: Audits a backlog export or list for health problems (stale, duplicate, oversized, orphan, unowned, unprioritized or goal-less items, too much ready work or too little) and produces findings with metrics, a cleanup proposal and hygiene rules. Use when the backlog has grown unmanageable, nobody trusts it, before a planning cycle, or someone asks to clean up, audit or assess the backlog.
- Try: _"Here is our backlog export with 340 items (title, type, created date, last updated, epic, status). Check its health and tell me what to delete."_
- Related: `backlog-refinement`, `backlog-prioritization`, `definition-of-ready`, `roadmap`, `cycle-time-analysis`
- File: [skills/02-product/product-owner/backlog/backlog-health-check/SKILL.md](skills/02-product/product-owner/backlog/backlog-health-check/SKILL.md)

#### Planning

**Build a product roadmap** · `roadmap`

- When: Builds a product roadmap tied to outcomes, either as Now/Next/Later or as a timeline with confidence levels, showing themes, target outcomes, key initiatives, dependencies, what is explicitly not planned and how the roadmap will be updated. Use when a product owner or manager needs to communicate direction to stakeholders, align teams for the coming quarters, or turn a feature list into an outcome-based plan.
- Try: _"Turn this list of 25 feature requests into a Now/Next/Later roadmap for our HR self-service app; our goals this year are fewer HR tickets and better mobile adoption."_
- Related: `product-vision`, `okr-definition`, `release-planning`, `backlog-prioritization`, `program-roadmap`
- File: [skills/02-product/product-owner/planning/roadmap/SKILL.md](skills/02-product/product-owner/planning/roadmap/SKILL.md)

**Plan a release** · `release-planning`

- When: Plans a release: target outcome, candidate scope split into committed and stretch, forecast of when the scope can be done based on throughput or velocity ranges, dependencies, milestones, risks and a confidence level, plus the scope-versus-date trade-off options. Use when a product owner must answer what will be in a release and when, negotiate a fixed date, or prepare a release plan for stakeholders.
- Try: _"We want to release the new onboarding flow by 15 March. Here are the 18 remaining items and our last 8 iterations' throughput. Is it feasible and what scope should we commit?"_
- Related: `roadmap`, `monte-carlo-forecast`, `velocity-analysis`, `release-plan`, `dependency-map`
- File: [skills/02-product/product-owner/planning/release-planning/SKILL.md](skills/02-product/product-owner/planning/release-planning/SKILL.md)

**Write an iteration goal** · `iteration-goal`

- When: Writes a single, coherent iteration/sprint goal that states the outcome the team commits to, why it matters and how success will be observed, and checks which candidate items serve it and which do not. Use when preparing iteration/sprint planning, when a draft goal is just a list of tickets, or when someone asks for a sprint goal or iteration objective.
- Try: _"Our next sprint candidates are: SSO login, password reset email fix, audit log export and two tech-debt items. Write a sprint goal."_
- Related: `iteration-planning`, `backlog-prioritization`, `roadmap`, `okr-definition`, `iteration-review-prep`
- File: [skills/02-product/product-owner/planning/iteration-goal/SKILL.md](skills/02-product/product-owner/planning/iteration-goal/SKILL.md)

**Prepare a product review** · `stakeholder-review-prep`

- When: Prepares a product or stakeholder review: what was built and why, how it moves the product goal, what feedback is needed from whom, which decisions must be taken, and an agenda with demo flow and the updated outlook. Use before an iteration/sprint review, a monthly product review or a steering-style product checkpoint where stakeholders must inspect progress and give input.
- Try: _"Prepare our monthly product review with the sales and operations heads: we shipped bulk upload and the new invoice screen; I need decisions on the pricing page and feedback on the mobile beta."_
- Related: `iteration-review-prep`, `demo-script`, `roadmap`, `feature-adoption-review`, `meeting-agenda`
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

- When: Writes a project scope statement that defines in-scope and out-of-scope work, deliverables with acceptance criteria, constraints, assumptions and exclusions, forming the baseline for change control. Use when a charter exists and scope must be made precise enough to plan, estimate and contract against, or when scope creep needs a clear reference.
- Try: _"Write a scope statement for the customer self-service portal project based on this charter and the workshop notes."_
- Related: `project-charter`, `wbs`, `change-control`, `acceptance-certificate`, `statement-of-work`
- File: [skills/03-delivery/project-manager/initiation/scope-statement/SKILL.md](skills/03-delivery/project-manager/initiation/scope-statement/SKILL.md)

**Prepare a kickoff** · `kickoff-deck`

- When: Prepares a project kickoff session, producing a timeboxed agenda and slide-by-slide content covering objectives, scope, team and roles, plan and milestones, ways of working, risks and immediate next steps for the team and sponsors. Use when a project is about to start or a new phase or major team change needs a shared start.
- Try: _"Prepare the kickoff for our data warehouse modernization project: 20 people, sponsor attends the first 30 minutes."_
- Related: `project-charter`, `scope-statement`, `stakeholder-register`, `communication-plan`, `meeting-agenda`
- File: [skills/03-delivery/project-manager/initiation/kickoff-deck/SKILL.md](skills/03-delivery/project-manager/initiation/kickoff-deck/SKILL.md)

**Build a stakeholder register** · `stakeholder-register`

- When: Builds a project stakeholder register listing each stakeholder's role, interest, influence, current and desired engagement, key concerns and communication needs, with an engagement strategy per group. Use when a project starts, when new parties join, or when resistance or silence from a group signals that engagement must be planned deliberately.
- Try: _"Build a stakeholder register for our ERP rollout to three plants; here is the org chart and the charter."_
- Related: `stakeholder-identification`, `stakeholder-map`, `raci-matrix`, `communication-plan`, `project-charter`
- File: [skills/03-delivery/project-manager/initiation/stakeholder-register/SKILL.md](skills/03-delivery/project-manager/initiation/stakeholder-register/SKILL.md)

#### Planning

**Build a work breakdown structure** · `wbs`

- When: Builds a deliverable-oriented work breakdown structure that decomposes project scope into a numbered hierarchy of work packages, with a WBS dictionary covering description, owner, acceptance and dependencies. Use when scope is agreed and must be broken down for estimation, scheduling, resourcing and progress tracking.
- Try: _"Create a WBS for the mobile banking app redesign using this scope statement."_
- Related: `scope-statement`, `estimation-three-point`, `schedule-plan`, `resource-plan`, `task-breakdown`
- File: [skills/03-delivery/project-manager/planning/wbs/SKILL.md](skills/03-delivery/project-manager/planning/wbs/SKILL.md)

**Estimate with three-point/PERT** · `estimation-three-point`

- When: Produces three-point estimates (optimistic, most likely, pessimistic) per work item and aggregates them with PERT or triangular formulas into expected values, standard deviations and confidence ranges for the total. Use when effort or duration is uncertain and stakeholders need a range with a stated confidence instead of a single number.
- Try: _"Give me a three-point estimate for these 12 work packages and tell me the total at 85% confidence."_
- Related: `wbs`, `schedule-plan`, `budget-plan`, `technical-estimation`, `monte-carlo-forecast`
- File: [skills/03-delivery/project-manager/planning/estimation-three-point/SKILL.md](skills/03-delivery/project-manager/planning/estimation-three-point/SKILL.md)

**Build a project schedule** · `schedule-plan`

- When: Builds a project schedule by sequencing work packages with dependency types and lags, assigning durations, setting milestones, calculating the critical path and float, and adding schedule buffers. Use when a WBS and estimates exist and a baseline timeline, critical path or realistic end date must be produced or checked.
- Try: _"Build a schedule from these work packages and durations and show me the critical path to the June go-live."_
- Related: `wbs`, `estimation-three-point`, `dependency-map`, `resource-plan`, `release-planning`
- File: [skills/03-delivery/project-manager/planning/schedule-plan/SKILL.md](skills/03-delivery/project-manager/planning/schedule-plan/SKILL.md)

**Build a resource plan** · `resource-plan`

- When: Builds a project resource plan showing required roles and skills over time, allocation per person or role per period, over-allocations, capacity gaps and options to close them (hire, contract, reprioritize, reschedule). Use when a schedule exists and the team must be staffed, when people are shared across projects, or when a skill gap threatens the plan.
- Try: _"Build a resource plan for the next 6 months of our payment gateway project; here is the schedule and the team list with availability."_
- Related: `schedule-plan`, `wbs`, `budget-plan`, `raci-matrix`, `onboarding-plan-30-60-90`
- File: [skills/03-delivery/project-manager/planning/resource-plan/SKILL.md](skills/03-delivery/project-manager/planning/resource-plan/SKILL.md)

**Build a project budget** · `budget-plan`

- When: Builds a project budget with a cost breakdown by WBS and cost category, separation of capex and opex where relevant, contingency and management reserves, and a time-phased cash flow that becomes the cost baseline. Use when a project needs a budget for approval, a cost baseline for tracking, or a re-forecast after scope or schedule changes.
- Try: _"Build a project budget from this resource plan and vendor quotes, with contingency and monthly cash flow."_
- Related: `wbs`, `resource-plan`, `estimation-three-point`, `earned-value-analysis`, `cloud-cost-estimate`
- File: [skills/03-delivery/project-manager/planning/budget-plan/SKILL.md](skills/03-delivery/project-manager/planning/budget-plan/SKILL.md)

**Build a communication plan** · `communication-plan`

- When: Builds a project communication plan that specifies, for each audience, what information they receive, when and how often, through which channel, from whom, and how feedback and escalations flow back. Use at project start, when stakeholders complain about being uninformed or overloaded, or when governance and reporting cadences must be agreed.
- Try: _"Create a communication plan for our core banking upgrade covering executives, branch staff, IT operations and the vendor."_
- Related: `stakeholder-register`, `project-status-report`, `governance-framework`, `status-update`, `announcement`
- File: [skills/03-delivery/project-manager/planning/communication-plan/SKILL.md](skills/03-delivery/project-manager/planning/communication-plan/SKILL.md)

**Build a risk register** · `risk-register`

- When: Builds a project risk register with cause-event-effect risk statements, probability and impact scores, proximity, owners, response strategies (avoid, mitigate, transfer, accept, exploit) with actions and triggers, and residual risk. Use when planning a project, before a gate or steering meeting, or when new threats or opportunities emerge.
- Try: _"Build a risk register for our warehouse management system rollout; here are the plan and concerns raised in the kickoff."_
- Related: `raid-log`, `pre-mortem`, `technical-risk-review`, `it-risk-assessment`, `budget-plan`
- File: [skills/03-delivery/project-manager/planning/risk-register/SKILL.md](skills/03-delivery/project-manager/planning/risk-register/SKILL.md)

**Map dependencies** · `dependency-map`

- When: Maps a project's internal and external dependencies, stating what is needed, from whom, by when, the providing and receiving owners, commitment status, criticality and the fallback if the dependency slips. Use when a project relies on other teams, vendors, platforms or decisions, or when missed hand-offs are threatening milestones.
- Try: _"Map all dependencies for our loyalty program launch: marketing, the POS vendor, data team and the legal review."_
- Related: `schedule-plan`, `raid-log`, `cross-team-dependency-board`, `risk-register`, `integration-requirements`
- File: [skills/03-delivery/project-manager/planning/dependency-map/SKILL.md](skills/03-delivery/project-manager/planning/dependency-map/SKILL.md)

#### Monitoring & Control

**Write a project status report** · `project-status-report`

- When: Writes a periodic project status report covering overall and per-dimension RAG status (schedule, cost, scope, quality, resources), progress against milestones, variance explanations, top risks and issues, and decisions needed from sponsors. Use for weekly or monthly reporting to sponsors or steering bodies, or when project health must be summarized objectively from plan and actual data.
- Try: _"Write this month's status report for the HR system project from these milestone updates, budget actuals and the RAID log."_
- Related: `status-update`, `steering-committee-pack`, `earned-value-analysis`, `raid-log`, `executive-summary`
- File: [skills/03-delivery/project-manager/monitoring/project-status-report/SKILL.md](skills/03-delivery/project-manager/monitoring/project-status-report/SKILL.md)

**Maintain a RAID log** · `raid-log`

- When: Creates or updates a RAID log that tracks Risks, Assumptions, Issues and Dependencies in one place with consistent IDs, owners, dates, status and cross-links, and produces a short summary of what changed and what needs attention. Use for ongoing project control, when raw notes, meeting outputs or emails must be triaged into the right RAID category, or before status reporting.
- Try: _"Update our RAID log with the points from today's steering meeting notes and tell me what needs escalation."_
- Related: `risk-register`, `issue-management`, `dependency-map`, `decision-log`, `project-status-report`
- File: [skills/03-delivery/project-manager/monitoring/raid-log/SKILL.md](skills/03-delivery/project-manager/monitoring/raid-log/SKILL.md)

**Run earned value analysis** · `earned-value-analysis`

- When: Runs an earned value analysis from a cost-loaded baseline and progress data, computing PV, EV, AC, SV, CV, SPI, CPI, EAC, ETC, VAC and TCPI, interpreting the variances and forecasting completion cost and date with stated assumptions. Use when a project with a budget and schedule baseline needs an objective performance reading, a forecast at completion, or evidence for a status report or steering decision.
- Try: _"Here is our baseline per work package and this month's actuals and percent complete. Run earned value analysis and tell me whether we will finish within budget."_
- Related: `budget-plan`, `schedule-plan`, `project-status-report`, `change-control`, `monte-carlo-forecast`
- File: [skills/03-delivery/project-manager/monitoring/earned-value-analysis/SKILL.md](skills/03-delivery/project-manager/monitoring/earned-value-analysis/SKILL.md)

**Run change control** · `change-control`

- When: Runs a change request through change control: captures the request, assesses impact on scope, schedule, cost, quality, risk and contract, lays out options, routes it to the right decision authority and updates the change log and baselines. Use when someone asks to add, remove or alter approved scope, dates or budget, when a vendor submits a change order, or when scope creep must be made visible and decided.
- Try: _"The client now wants SSO with their Azure AD in addition to the agreed login. Prepare a change request with impact assessment for the change board."_
- Related: `scope-statement`, `impact-analysis`, `raid-log`, `decision-log`, `earned-value-analysis`
- File: [skills/03-delivery/project-manager/monitoring/change-control/SKILL.md](skills/03-delivery/project-manager/monitoring/change-control/SKILL.md)

**Manage an issue** · `issue-management`

- When: Manages a single project issue from logging to closure: states it precisely, assesses impact and urgency, finds the cause, sets a resolution plan with owner and dates, defines escalation triggers and closure criteria, and tracks it until verified resolved. Use when something is already going wrong and affecting scope, schedule, cost or quality, such as a blocked team, a failed dependency, a vendor slip or a realized risk.
- Try: _"Our test environment has been down for 4 days and the vendor keeps postponing. Help me log and manage this as an issue with an escalation path."_
- Related: `raid-log`, `escalation-message`, `five-whys`, `change-control`, `decision-log`
- File: [skills/03-delivery/project-manager/monitoring/issue-management/SKILL.md](skills/03-delivery/project-manager/monitoring/issue-management/SKILL.md)

**Review vendor performance** · `vendor-status-review`

- When: Reviews a vendor's delivery performance against the contract or statement of work: deliverables and milestones, SLA and KPI results, quality, staffing, invoices and open obligations on both sides, and produces a scored assessment with evidence, issues and agreed actions. Use before a periodic vendor governance meeting, when a supplier is slipping, before approving an invoice or milestone payment, or when deciding whether to escalate or invoke contract remedies.
- Try: _"Prepare the monthly performance review for our implementation partner using the SOW milestones, their status report and our SLA report."_
- Related: `statement-of-work`, `sla-breach-analysis`, `issue-management`, `acceptance-certificate`, `vendor-evaluation`
- File: [skills/03-delivery/project-manager/monitoring/vendor-status-review/SKILL.md](skills/03-delivery/project-manager/monitoring/vendor-status-review/SKILL.md)

#### Closure

**Write a project closure report** · `project-closure-report`

- When: Writes a project closure report that compares outcomes with the original objectives and baselines, explains scope, schedule, cost and quality variances, confirms acceptance and handover to operations, lists open items with owners, records lessons learned and sets up benefits tracking. Use when a project or phase is ending, when the sponsor needs a formal close-out decision, or when a project is cancelled and must be closed in an orderly way.
- Try: _"Our CRM migration went live last month. Write the closure report from the charter, final status report and budget actuals."_
- Related: `acceptance-certificate`, `handover-document`, `lessons-learned`, `benefits-realization`, `earned-value-analysis`
- File: [skills/03-delivery/project-manager/closure/project-closure-report/SKILL.md](skills/03-delivery/project-manager/closure/project-closure-report/SKILL.md)

**Prepare deliverable acceptance** · `acceptance-certificate`

- When: Prepares a deliverable acceptance certificate that records what was delivered, the agreed acceptance criteria and the evidence for each, open defects and accepted deviations, conditions for conditional acceptance, and sign-offs from authorized parties. Use when a deliverable, milestone or phase must be formally accepted by a client, sponsor or business owner, before a milestone payment, or when a vendor delivery must be accepted or rejected on record.
- Try: _"Prepare the acceptance certificate for milestone 2 (reporting module). UAT is done with 3 minor defects open; the client wants to sign conditionally."_
- Related: `acceptance-criteria`, `uat-plan`, `statement-of-work`, `project-closure-report`, `change-control`
- File: [skills/03-delivery/project-manager/closure/acceptance-certificate/SKILL.md](skills/03-delivery/project-manager/closure/acceptance-certificate/SKILL.md)

### Scrum Master / Agile Coach

#### Team Events

**Facilitate iteration planning** · `iteration-planning`

- When: Facilitates an iteration/sprint planning session end to end: calculates realistic capacity, confirms the iteration goal, selects work that fits and breaks it into tasks, and records risks and the resulting plan. Use when a team is about to start an iteration/sprint, when someone asks for a planning agenda or capacity calculation, or when past plans were routinely overcommitted.
- Try: _"Help me run sprint planning for 6 developers over a 2-week sprint; one is on leave 3 days and we have a release freeze on the last day. Here are the top 12 backlog items."_
- Related: `iteration-goal`, `estimation-session`, `velocity-analysis`, `task-breakdown`, `definition-of-ready`
- File: [skills/03-delivery/agile-delivery/ceremonies/iteration-planning/SKILL.md](skills/03-delivery/agile-delivery/ceremonies/iteration-planning/SKILL.md)

**Summarize a daily sync** · `daily-sync-summary`

- When: Turns notes or a transcript of a daily team sync (stand-up) into a short summary of progress toward the iteration goal, today's plan, blockers with owners and follow-up conversations, per person and for the team. Use when someone shares stand-up notes, a chat thread of async updates or a meeting transcript and asks for a summary, blocker list or update for absent members.
- Try: _"Summarize today's stand-up from these notes and list the blockers: Emre finished the payment API mock, stuck on test env certificate; Selin reviewing Emre's PR, then starts refund flow..."_
- Related: `impediment-tracking`, `meeting-summary`, `action-item-extraction`, `burndown-analysis`, `iteration-goal`
- File: [skills/03-delivery/agile-delivery/ceremonies/daily-sync-summary/SKILL.md](skills/03-delivery/agile-delivery/ceremonies/daily-sync-summary/SKILL.md)

**Prepare an iteration review** · `iteration-review-prep`

- When: Prepares an iteration/sprint review: summarizes the increment against the iteration goal, orders the demo around user scenarios, states what was not done and why, and drafts targeted feedback questions and backlog-impact prompts. Use when a team's iteration review, sprint review or end-of-iteration demo is coming up and someone asks for an agenda, demo order or increment summary.
- Try: _"Prepare our sprint review for Thursday. Goal was 'merchants can issue partial refunds'. Done: refund API, refund UI, email notice. Not done: refund report. 8 stakeholders from finance and support are coming."_
- Related: `stakeholder-review-prep`, `demo-script`, `iteration-goal`, `burndown-analysis`, `retrospective-facilitation`
- File: [skills/03-delivery/agile-delivery/ceremonies/iteration-review-prep/SKILL.md](skills/03-delivery/agile-delivery/ceremonies/iteration-review-prep/SKILL.md)

**Facilitate a retrospective** · `retrospective-facilitation`

- When: Plans and runs a team retrospective end to end: sets the stage, gathers data, generates insights, converges with note-and-vote and produces a small number of owned, verifiable improvement actions, and follows up on previous actions. Use when a retrospective is due, when someone shares retro board notes and wants actions, or when past retros produced actions that never happened.
- Try: _"Run our sprint retro: remote team of 7, 60 minutes. Last sprint had two production incidents and a lot of context switching. Last retro's actions: pair on reviews (not done), fix flaky tests (done)."_
- Related: `retrospective-format`, `team-health-check`, `working-agreement`, `five-whys`, `impediment-tracking`
- File: [skills/03-delivery/agile-delivery/ceremonies/retrospective-facilitation/SKILL.md](skills/03-delivery/agile-delivery/ceremonies/retrospective-facilitation/SKILL.md)

**Design a retrospective format** · `retrospective-format`

- When: Designs a retrospective format tailored to the team's current mood, topic, size and setting: picks or adapts activities for each retro phase, writes the prompts, timings and materials, and explains why the format fits. Use when retros feel stale, when a specific theme (incident, conflict, milestone, new team) needs a dedicated retro, or when someone asks for a new retro idea or template.
- Try: _"Our retros have become boring and the same three people talk. Design a 45-minute remote retro format for a tired team of 9 after a hard release."_
- Related: `retrospective-facilitation`, `team-health-check`, `workshop-plan`, `facilitation-guide`, `conflict-resolution`
- File: [skills/03-delivery/agile-delivery/ceremonies/retrospective-format/SKILL.md](skills/03-delivery/agile-delivery/ceremonies/retrospective-format/SKILL.md)

**Facilitate relative estimation** · `estimation-session`

- When: Prepares and guides a relative estimation session (planning poker, t-shirt sizing, affinity estimation): selects the scale, builds a reference-story ladder, runs estimation rounds that surface assumptions, and records sizes, spread and follow-ups. Use when a team needs to size backlog items, calibrate a new scale, speed up slow estimation meetings, or when someone asks how to run planning poker or t-shirt sizing.
- Try: _"We have 25 unsized stories for the new onboarding epic and a 1-hour session. The team is new and has no reference stories. How should we estimate?"_
- Related: `backlog-refinement`, `story-splitting`, `technical-estimation`, `velocity-analysis`, `iteration-planning`
- File: [skills/03-delivery/agile-delivery/ceremonies/estimation-session/SKILL.md](skills/03-delivery/agile-delivery/ceremonies/estimation-session/SKILL.md)

#### Flow & Metrics

**Analyze velocity/throughput** · `velocity-analysis`

- When: Analyzes a team's velocity (points per iteration) or throughput (items per week/iteration) history: trend, variability, outliers and their causes, and a range-based forecast for remaining work. Use when someone shares iteration or throughput numbers and asks whether the team is speeding up or slowing down, how predictable it is, or how many iterations a backlog will take.
- Try: _"Here are our last 10 sprint velocities: 21, 34, 29, 18, 31, 33, 12, 30, 28, 32. We have 180 points left in the release. What does this tell us and when can we finish?"_
- Related: `monte-carlo-forecast`, `burndown-analysis`, `cycle-time-analysis`, `release-planning`, `engineering-metrics-review`
- File: [skills/03-delivery/agile-delivery/flow/velocity-analysis/SKILL.md](skills/03-delivery/agile-delivery/flow/velocity-analysis/SKILL.md)

**Read burndown/burnup charts** · `burndown-analysis`

- When: Interprets burndown and burnup charts or their underlying daily data for an iteration or release: reads the shape, separates progress from scope change, detects patterns such as late drops, flat lines and scope creep, and flags risks with recommended actions. Use when someone shares a burndown/burnup chart, daily remaining-work numbers or asks whether an iteration or release is on track.
- Try: _"Day 7 of 10 in our sprint. Remaining points by day: 40, 40, 38, 38, 38, 35, 35. Two stories were added on day 4. Are we going to make it?"_
- Related: `velocity-analysis`, `monte-carlo-forecast`, `daily-sync-summary`, `iteration-planning`, `project-status-report`
- File: [skills/03-delivery/agile-delivery/flow/burndown-analysis/SKILL.md](skills/03-delivery/agile-delivery/flow/burndown-analysis/SKILL.md)

**Analyze cycle/lead time** · `cycle-time-analysis`

- When: Analyzes cycle time and lead time from work item start/finish dates: computes percentiles, reads the distribution, finds bottleneck states from time-in-state data, flags aging work in progress against the historical percentiles and proposes a service level expectation. Use when someone shares item start/end dates or board state history and asks how long work takes, where it waits or which items are at risk of getting stuck.
- Try: _"Here are 40 finished items with start and done dates and 9 items in progress with their start dates. How long does our work take and what is stuck?"_
- Related: `wip-policy`, `monte-carlo-forecast`, `velocity-analysis`, `value-stream-map`, `engineering-metrics-review`
- File: [skills/03-delivery/agile-delivery/flow/cycle-time-analysis/SKILL.md](skills/03-delivery/agile-delivery/flow/cycle-time-analysis/SKILL.md)

**Define WIP limits and flow policies** · `wip-policy`

- When: Designs a board and its flow policies: columns that mirror the real workflow including wait states, work-in-progress limits per column or person, explicit entry and exit criteria, classes of service, blocked-item and aging rules, and a review cadence for adjusting the limits. Use when a team sets up or redesigns its board, has too much work started and little finished, or asks what WIP limits and pull rules to use.
- Try: _"We are 6 developers and 1 tester, everything is 'in progress' and nothing finishes. Help us define board columns and WIP limits."_
- Related: `cycle-time-analysis`, `working-agreement`, `definition-of-ready`, `definition-of-done`, `impediment-tracking`
- File: [skills/03-delivery/agile-delivery/flow/wip-policy/SKILL.md](skills/03-delivery/agile-delivery/flow/wip-policy/SKILL.md)

**Forecast delivery with Monte Carlo** · `monte-carlo-forecast`

- When: Produces a probabilistic delivery forecast from historical throughput using Monte Carlo simulation: answers 'when will N items be done?' or 'how many items by date D?' with confidence levels (50/85/95%), accounts for backlog growth and splitting, and explains the method and caveats. Use when someone shares weekly or per-iteration throughput and asks for a release date, a scope forecast for a deadline, or the probability of hitting a commitment.
- Try: _"Our weekly throughput for the last 12 weeks: 3, 5, 4, 0, 6, 4, 5, 3, 7, 4, 2, 5. We have 38 items left. When can we be done with 85% confidence?"_
- Related: `velocity-analysis`, `cycle-time-analysis`, `release-planning`, `burndown-analysis`, `schedule-plan`
- File: [skills/03-delivery/agile-delivery/flow/monte-carlo-forecast/SKILL.md](skills/03-delivery/agile-delivery/flow/monte-carlo-forecast/SKILL.md)

**Track impediments** · `impediment-tracking`

- When: Builds and maintains an impediment log: captures each blocker with the blocked work, impact, owner and next action, classifies it by what is needed to remove it (team, other team, management, external), applies an escalation ladder with time thresholds, and surfaces recurring systemic causes. Use when a team reports blockers in a daily sync, work is stuck waiting on others, or someone asks to organize, escalate or report on open impediments.
- Try: _"Here are the blockers from this week's syncs: test environment down since Tuesday, waiting for the security team's approval on the firewall rule, and the product owner hasn't answered on the refund rules. Organize and tell me what to escalate."_
- Related: `daily-sync-summary`, `escalation-message`, `cross-team-dependency-board`, `raid-log`, `retrospective-facilitation`
- File: [skills/03-delivery/agile-delivery/flow/impediment-tracking/SKILL.md](skills/03-delivery/agile-delivery/flow/impediment-tracking/SKILL.md)

#### Team Development

**Create a team working agreement** · `working-agreement`

- When: Facilitates and writes a team working agreement: collects norms for communication channels and response times, availability and core hours, code review and pairing, meetings, decision making, on-call and conflict handling, turns them into specific observable commitments, and sets how the agreement is reviewed and enforced. Use when a team forms or changes, recurring friction appears (slow reviews, meeting overload, after-hours pings), or someone asks for a team charter or ground rules.
- Try: _"Our team is now split between Istanbul and Berlin, reviews wait for days and people get pinged at night. Help us draft a working agreement."_
- Related: `wip-policy`, `team-health-check`, `retrospective-facilitation`, `definition-of-done`, `conflict-resolution`
- File: [skills/03-delivery/agile-delivery/team/working-agreement/SKILL.md](skills/03-delivery/agile-delivery/team/working-agreement/SKILL.md)

**Run a team health check** · `team-health-check`

- When: Designs and analyzes a team health check: selects 8-12 dimensions (e.g. delivering value, speed, codebase health, learning, mission clarity, fun, support, psychological safety), writes traffic-light or 1-5 rating statements, runs it anonymously, reads results and trends per dimension, and turns the lowest or declining areas into a few owned follow-up actions. Use when a team or manager wants to take the team's pulse, compare with a previous round, or prepare a health check session.
- Try: _"Here are our health check results from last quarter and this quarter across 10 dimensions (green/yellow/red per person). What stands out and what should we do?"_
- Related: `retrospective-facilitation`, `working-agreement`, `agile-maturity-assessment`, `questionnaire-design`, `engineering-metrics-review`
- File: [skills/03-delivery/agile-delivery/team/team-health-check/SKILL.md](skills/03-delivery/agile-delivery/team/team-health-check/SKILL.md)

**Assess agile maturity** · `agile-maturity-assessment`

- When: Assesses a team's or unit's agile maturity in a methodology-neutral way: scores practice areas (customer value and product ownership, planning and forecasting, flow and delivery, technical practices, quality, continuous improvement, team autonomy, stakeholder collaboration) on a 1-5 evidence-based scale, identifies constraints rather than averaging, and proposes the next 2-3 improvements with observable outcomes. Use when a leader or coach asks how agile a team really is, needs a baseline before a transformation, or wants to decide what to improve next.
- Try: _"Assess our team's agile maturity. We do two-week iterations, releases are quarterly, the product owner is part-time, and there is no test automation."_
- Related: `team-health-check`, `retrospective-facilitation`, `wip-policy`, `engineering-metrics-review`, `current-state-assessment`
- File: [skills/03-delivery/agile-delivery/team/agile-maturity-assessment/SKILL.md](skills/03-delivery/agile-delivery/team/agile-maturity-assessment/SKILL.md)

### Program Manager / PMO

#### Portfolio & Program

**Prioritize a project portfolio** · `portfolio-prioritization`

- When: Prioritizes a portfolio of projects or initiatives by scoring them on value, strategic fit, risk and effort, checking the ranked list against real capacity and dependencies, and producing a funded / queued / stopped recommendation with rationale. Use when there are more initiatives than capacity, during annual or quarterly portfolio planning, when a new demand must be slotted in, or when leadership asks \"what should we fund or stop\".
- Try: _"Prioritize these 12 initiatives for next year; we have roughly 6 delivery teams and the strategy is to grow digital sales and cut operating cost."_
- Related: `decision-matrix`, `cost-benefit-analysis`, `okr-definition`, `program-roadmap`, `steering-committee-pack`
- File: [skills/03-delivery/program-pmo/portfolio/portfolio-prioritization/SKILL.md](skills/03-delivery/program-pmo/portfolio/portfolio-prioritization/SKILL.md)

**Build a program roadmap** · `program-roadmap`

- When: Builds a program roadmap that sequences the work of several teams or projects toward shared outcomes, showing cross-team milestones, integration points, decision gates and the critical path, with confidence levels instead of false precision. Use when a program spans multiple teams or vendors, when leadership needs one view of how parallel workstreams converge, or when someone asks for a program-level plan, timeline or integrated roadmap.
- Try: _"Build a program roadmap for our core banking migration: 5 teams, a vendor, and a regulatory go-live in Q4."_
- Related: `cross-team-dependency-board`, `portfolio-prioritization`, `roadmap`, `release-planning`, `schedule-plan`
- File: [skills/03-delivery/program-pmo/portfolio/program-roadmap/SKILL.md](skills/03-delivery/program-pmo/portfolio/program-roadmap/SKILL.md)

**Run cross-team dependency planning** · `cross-team-dependency-board`

- When: Runs cross-team dependency planning by surfacing every dependency between teams, making each one explicit (provider, consumer, what, needed-by date), negotiating a commitment or alternative, and tracking status with escalation rules on a shared board. Use when several teams plan the same period together, when a program keeps slipping because of waiting between teams, or when someone asks to map, negotiate or track inter-team dependencies.
- Try: _"Set up a dependency board for next quarter's planning; 4 teams, and the checkout team depends on payments and identity for almost everything."_
- Related: `dependency-map`, `program-roadmap`, `raid-log`, `escalation-message`, `negotiation-prep`
- File: [skills/03-delivery/program-pmo/portfolio/cross-team-dependency-board/SKILL.md](skills/03-delivery/program-pmo/portfolio/cross-team-dependency-board/SKILL.md)

**Prepare a steering committee pack** · `steering-committee-pack`

- When: Prepares a steering committee pack that leads with the decisions needed, then gives a concise status against baseline, key risks and issues, financials (budget, actuals, forecast) and benefits outlook, with options and a recommendation for each decision. Use before a steering committee, project board or sponsor review, when monthly program reporting must be turned into a decision-oriented pack, or when someone asks to prepare \"the steerco deck\" or \"board update\" for a project or program.
- Try: _"Prepare the steering committee pack for next Thursday: we are 3 weeks late on integration testing, 8% over budget, and need a decision on descoping the reporting module."_
- Related: `project-status-report`, `executive-summary`, `raid-log`, `decision-log`, `presentation-outline`
- File: [skills/03-delivery/program-pmo/portfolio/steering-committee-pack/SKILL.md](skills/03-delivery/program-pmo/portfolio/steering-committee-pack/SKILL.md)

**Define project governance** · `governance-framework`

- When: Defines project or program governance sized to its risk: decision rights by decision type, governance forums with membership and mandate, stage or decision gates with entry criteria, tolerances and escalation paths, and the reporting cadence that feeds each forum. Use when a new project or program is being set up, when decisions stall or are taken in the wrong place, when an audit or sponsor asks \"who decides what\", or when existing governance is too heavy or too light.
- Try: _"Define governance for a 14-month ERP replacement program with an external integrator, three business units and an IT steering committee that already exists."_
- Related: `raci-matrix`, `steering-committee-pack`, `project-charter`, `change-control`, `communication-plan`
- File: [skills/03-delivery/program-pmo/portfolio/governance-framework/SKILL.md](skills/03-delivery/program-pmo/portfolio/governance-framework/SKILL.md)

**Track benefits realization** · `benefits-realization`

- When: Tracks benefits realization after delivery by turning planned benefits into measurable indicators with baselines, targets, owners and measurement dates, comparing planned versus actual values, attributing the change, and recommending corrective actions or re-forecasts. Use after a project or program goes live, at a post-implementation or benefits review, when a business case needs to be checked against results, or when someone asks \"did we get the value we promised\".
- Try: _"Check benefits realization for our self-service portal six months after go-live; the business case promised 30% fewer call-center contacts and faster onboarding."_
- Related: `kpi-definition`, `cost-benefit-analysis`, `feature-adoption-review`, `project-closure-report`, `portfolio-prioritization`
- File: [skills/03-delivery/program-pmo/portfolio/benefits-realization/SKILL.md](skills/03-delivery/program-pmo/portfolio/benefits-realization/SKILL.md)

## Architecture

### Enterprise Architect

#### Architecture Strategy

**Define architecture principles** · `architecture-principles`

- When: Defines a small set of enterprise or domain architecture principles, each with a statement, rationale and implications in the TOGAF style, plus how compliance is checked and how exceptions are handled. Use when an organization needs guiding rules for architecture decisions, when principles are vague slogans, or when design reviews keep re-arguing the same trade-offs.
- Try: _"Define 8-10 architecture principles for our move to cloud-native, event-driven systems; our drivers are faster delivery, lower run cost and KVKK compliance."_
- Related: `architecture-review`, `adr`, `target-state-architecture`, `technology-strategy`, `governance-framework`
- File: [skills/04-architecture/enterprise-architect/strategy/architecture-principles/SKILL.md](skills/04-architecture/enterprise-architect/strategy/architecture-principles/SKILL.md)

**Build a business capability map** · `capability-map`

- When: Builds a hierarchical business capability map (levels 1-3) with maturity, strategic importance and a heatmap, and maps applications and owners to capabilities. Use when planning investments, rationalizing applications, scoping a transformation or aligning IT with business strategy, or when someone asks what the business does independent of org chart and systems.
- Try: _"Build a level-2 capability map for our retail bank with maturity and strategic importance, and highlight where to invest next year."_
- Related: `application-portfolio-assessment`, `target-state-architecture`, `value-stream-map`, `bounded-context-map`, `portfolio-prioritization`
- File: [skills/04-architecture/enterprise-architect/strategy/capability-map/SKILL.md](skills/04-architecture/enterprise-architect/strategy/capability-map/SKILL.md)

**Assess the application portfolio** · `application-portfolio-assessment`

- When: Assesses an application portfolio on business fit and technical fit and assigns each application a TIME disposition (Tolerate, Invest, Migrate, Eliminate) with rationale, cost and risk signals and a sequenced rationalization plan. Use when rationalizing applications, preparing a budget cycle, planning cloud or ERP programs, or after a merger leaves overlapping systems.
- Try: _"Here is our list of 40 applications with owners, costs and user counts; classify them with TIME and propose what to retire first."_
- Related: `capability-map`, `modernization-assessment`, `tech-debt-assessment`, `build-vs-buy`, `target-state-architecture`
- File: [skills/04-architecture/enterprise-architect/strategy/application-portfolio-assessment/SKILL.md](skills/04-architecture/enterprise-architect/strategy/application-portfolio-assessment/SKILL.md)

**Define target-state architecture** · `target-state-architecture`

- When: Defines a target-state architecture by describing the baseline, the target across business, data, application and technology views, the gaps between them and a transition roadmap of plateaus with dependencies and decision points. Use when a transformation, platform consolidation or multi-year program needs a shared picture of where the architecture should be and how to get there.
- Try: _"Define the target-state architecture for moving our monolithic order management and nightly batch integrations to domain services with event streaming over three years."_
- Related: `capability-map`, `architecture-principles`, `migration-strategy`, `application-portfolio-assessment`, `roadmap`
- File: [skills/04-architecture/enterprise-architect/strategy/target-state-architecture/SKILL.md](skills/04-architecture/enterprise-architect/strategy/target-state-architecture/SKILL.md)

**Maintain a technology radar** · `tech-radar`

- When: Builds or updates a technology radar that classifies technologies into Adopt, Trial, Assess and Hold rings across quadrants (techniques, platforms, tools, languages and frameworks), with evidence-based rationale, movement since the last edition and guidance for teams. Use when standardizing a technology landscape, publishing a periodic radar, or deciding whether a team may use a new technology.
- Try: _"Update our tech radar with these proposals: move gRPC from Assess to Trial, put AngularJS on Hold, and add OpenTelemetry."_
- Related: `technology-selection`, `architecture-principles`, `technology-strategy`, `adr`, `dependency-upgrade`
- File: [skills/04-architecture/enterprise-architect/strategy/tech-radar/SKILL.md](skills/04-architecture/enterprise-architect/strategy/tech-radar/SKILL.md)

### Solution Architect

#### Solution Design

**Write a solution architecture document** · `solution-architecture-document`

- When: Writes a solution architecture document structured on arc42 - goals and quality requirements, constraints, context and scope, solution strategy, building blocks, runtime scenarios, deployment, crosscutting concepts, decisions, risks and glossary - from requirements and design notes. Use when a solution must be documented for review, handover, approval or audit, or when an existing design lives only in slides and heads.
- Try: _"Write a solution architecture document for our new loan origination platform; here are the requirements, the integration list and our whiteboard notes."_
- Related: `c4-model`, `adr`, `nfr-to-architecture`, `architecture-review`, `technical-design-doc`
- File: [skills/04-architecture/solution-architect/design/solution-architecture-document/SKILL.md](skills/04-architecture/solution-architect/design/solution-architecture-document/SKILL.md)

**Describe architecture with C4** · `c4-model`

- When: Describes a software system with the C4 model - system context, container and, where useful, component diagrams - as diagrams-as-code (Structurizr DSL, PlantUML C4 or Mermaid) with consistent element names, responsibilities, technologies and labeled relationships. Use when someone needs architecture diagrams for a design, review, onboarding or documentation, or wants to turn a textual description or existing sketch into C4 views.
- Try: _"Create C4 context and container diagrams in Structurizr DSL for our e-commerce checkout: web shop, mobile app, checkout API, payment provider, order DB and message broker."_
- Related: `solution-architecture-document`, `diagram-as-code`, `bounded-context-map`, `adr`, `architecture-review`
- File: [skills/04-architecture/solution-architect/design/c4-model/SKILL.md](skills/04-architecture/solution-architect/design/c4-model/SKILL.md)

**Write an Architecture Decision Record** · `adr`

- When: Writes an Architecture Decision Record (ADR) capturing context, decision drivers, considered options with pros and cons, the decision, and its consequences, in a Nygard or MADR style, including status and supersession links. Use when an architecturally significant decision has been made or must be made, when a past decision needs to be documented retroactively, or when a decision is being reversed.
- Try: _"Write an ADR for choosing PostgreSQL over MongoDB for the order service; drivers are transactional consistency, team skills and reporting needs."_
- Related: `decision-log`, `trade-off-analysis`, `technology-selection`, `solution-architecture-document`, `architecture-principles`
- File: [skills/04-architecture/solution-architect/design/adr/SKILL.md](skills/04-architecture/solution-architect/design/adr/SKILL.md)

**Select a technology** · `technology-selection`

- When: Runs a structured technology selection - problem framing, weighted criteria including quality attributes, cost, risk and ecosystem health, a long-to-short list, a proof-of-concept plan with pass/fail criteria and a recommendation recorded as an ADR. Use when choosing a database, message broker, framework, platform, SaaS product or library for a significant need, or when a team's preferred tool must be justified objectively.
- Try: _"Help us select a message broker for order and inventory events; we need ordering per order, replay for 7 days and we run on Kubernetes."_
- Related: `adr`, `build-vs-buy`, `tech-radar`, `vendor-evaluation`, `spike-report`
- File: [skills/04-architecture/solution-architect/design/technology-selection/SKILL.md](skills/04-architecture/solution-architect/design/technology-selection/SKILL.md)

**Choose integration patterns** · `integration-pattern-selection`

- When: Selects integration patterns for each interaction between systems (synchronous API, asynchronous messaging, event streaming, file/batch transfer, CDC, shared database) by analyzing coupling, latency, consistency, volume, ordering and failure behavior, and records the trade-offs. Use when designing how two or more systems exchange data or commands, replacing point-to-point or file interfaces, or when an integration keeps failing under load or change.
- Try: _"Choose integration patterns between our order system, the ERP and the warehouse system; ERP only supports SOAP and nightly files, the warehouse needs stock updates within a minute."_
- Related: `integration-requirements`, `event-driven-design`, `api-contract`, `adr`, `resilience-review`
- File: [skills/04-architecture/solution-architect/design/integration-pattern-selection/SKILL.md](skills/04-architecture/solution-architect/design/integration-pattern-selection/SKILL.md)

**Map NFRs to architecture tactics** · `nfr-to-architecture`

- When: Turns non-functional requirements into measurable quality attribute scenarios (source, stimulus, environment, artifact, response, response measure) and maps each to architectural tactics, with the trade-offs and verification method. Use when NFRs are vague (\"fast\", \"secure\", \"highly available\"), when a design must show how it meets quality goals, or before an architecture review or ATAM.
- Try: _"Map these NFRs to architecture tactics: checkout must be fast, available 24/7, handle Black Friday peaks and comply with PCI DSS."_
- Related: `nfr-specification`, `solution-architecture-document`, `atam-evaluation`, `trade-off-analysis`, `slo-definition`
- File: [skills/04-architecture/solution-architect/design/nfr-to-architecture/SKILL.md](skills/04-architecture/solution-architect/design/nfr-to-architecture/SKILL.md)

**Decide build vs buy** · `build-vs-buy`

- When: Compares building, buying (COTS/SaaS), extending an existing platform or using open source for a capability, across strategic differentiation, functional fit, multi-year total cost of ownership, risk, time to value and exit cost, and produces a reasoned recommendation. Use when a team must decide whether to develop a capability in-house or acquire it, or when an existing custom system or product is up for replacement.
- Try: _"Should we build our own customer notification service or buy a SaaS product? We send about 2 million emails and SMS a month and need templates in Turkish and English."_
- Related: `technology-selection`, `vendor-evaluation`, `cost-benefit-analysis`, `fit-gap-analysis`, `adr`
- File: [skills/04-architecture/solution-architect/design/build-vs-buy/SKILL.md](skills/04-architecture/solution-architect/design/build-vs-buy/SKILL.md)

**Estimate cloud cost of a design** · `cloud-cost-estimate`

- When: Sizes each component of a solution design (compute, storage, database, network egress, managed services, observability, licences) from workload drivers and produces a transparent monthly run-cost estimate with ranges, assumptions and cost-reduction levers. Use when a design needs a cost figure for approval, when comparing architecture options on cost, or when a cloud budget must be set before build.
- Try: _"Estimate the monthly cloud cost of this design: 6 containerized services, a managed PostgreSQL, Redis, object storage for 5 TB of documents and about 20 million API calls a month."_
- Related: `finops-review`, `capacity-planning`, `build-vs-buy`, `solution-architecture-document`, `budget-proposal`
- File: [skills/04-architecture/solution-architect/design/cloud-cost-estimate/SKILL.md](skills/04-architecture/solution-architect/design/cloud-cost-estimate/SKILL.md)

#### Architecture Review

**Review an architecture** · `architecture-review`

- When: Reviews a solution or software architecture against its business drivers, quality attribute requirements, architecture principles, known risks and common anti-patterns, and produces severity-rated findings with concrete recommendations and a review verdict. Use when a design document, diagram set or ADRs are submitted for architecture board approval, before a major build or go-live, or when a system shows recurring structural problems.
- Try: _"Review this solution architecture document for our new loan origination platform before the architecture board next week."_
- Related: `architecture-principles`, `nfr-to-architecture`, `atam-evaluation`, `resilience-review`, `scalability-review`
- File: [skills/04-architecture/solution-architect/review/architecture-review/SKILL.md](skills/04-architecture/solution-architect/review/architecture-review/SKILL.md)

**Run an ATAM-style evaluation** · `atam-evaluation`

- When: Plans and documents an evaluation modeled on the Architecture Tradeoff Analysis Method (ATAM), producing business drivers, a prioritized quality attribute utility tree, analysis of architectural approaches against high-priority scenarios, and the resulting sensitivity points, trade-off points, risks, non-risks and risk themes. Use when a significant architecture must be evaluated with stakeholders before commitment, when quality goals conflict, or when an independent structured evaluation is requested.
- Try: _"Prepare an ATAM-style evaluation for our event-driven payments platform; the key concerns are latency, availability across two data centers and auditability."_
- Related: `nfr-to-architecture`, `architecture-review`, `trade-off-analysis`, `workshop-plan`, `adr`
- File: [skills/04-architecture/solution-architect/review/atam-evaluation/SKILL.md](skills/04-architecture/solution-architect/review/atam-evaluation/SKILL.md)

**Review resilience** · `resilience-review`

- When: Reviews the resilience of a system by walking every critical flow and dependency through its failure modes, and checking timeouts, retries, circuit breakers, bulkheads, idempotency, graceful degradation, data durability and disaster recovery against availability targets (SLO, RTO, RPO). Use before go-live of a critical service, after incidents caused by dependency failures, when adding a new external dependency, or when DR readiness must be demonstrated.
- Try: _"Review the resilience of our checkout flow: it calls pricing, inventory, a payment provider and a fraud service synchronously, and we had two outages last month when the fraud service slowed down."_
- Related: `chaos-experiment`, `dr-plan`, `slo-definition`, `integration-pattern-selection`, `architecture-review`
- File: [skills/04-architecture/solution-architect/review/resilience-review/SKILL.md](skills/04-architecture/solution-architect/review/resilience-review/SKILL.md)

**Review scalability** · `scalability-review`

- When: Reviews how a system scales by modeling load growth against each component, locating bottlenecks (CPU, I/O, locks, connections, hot partitions, shared state), and assessing statelessness, partitioning, caching, asynchronous processing and data-tier limits, with prioritized recommendations and the scaling limit of the current design. Use before an expected growth step or peak event, when latency degrades with load, or when choosing between scale-up and scale-out.
- Try: _"Review the scalability of our reporting API; traffic will grow 5x after we onboard a large customer and p95 latency already rises sharply at month end."_
- Related: `capacity-planning`, `performance-test-plan`, `load-test-analysis`, `resilience-review`, `query-optimization`
- File: [skills/04-architecture/solution-architect/review/scalability-review/SKILL.md](skills/04-architecture/solution-architect/review/scalability-review/SKILL.md)

### Software Architect

#### Domain Design

**Run event storming** · `event-storming`

- When: Plans and runs a big-picture or design-level event storming session and turns the result into a structured model of domain events, commands, actors, policies, read models, external systems, aggregates and hot spots. Use when a team needs a shared understanding of a business flow, wants to discover bounded contexts or aggregates, or has a messy wall of stickies to consolidate.
- Try: _"Help me run a design-level event storming for our order-to-delivery flow and structure the stickies from yesterday's session."_
- Related: `bounded-context-map`, `aggregate-design`, `event-driven-design`, `workshop-plan`, `glossary-builder`
- File: [skills/04-architecture/software-architect/domain/event-storming/SKILL.md](skills/04-architecture/software-architect/domain/event-storming/SKILL.md)

**Map bounded contexts** · `bounded-context-map`

- When: Produces a context map that names each bounded context, its ubiquitous language and ownership, and classifies the relationships between contexts (partnership, shared kernel, customer-supplier, conformist, anticorruption layer, open host service, published language, separate ways) with upstream/downstream direction and integration style. Use when defining module or service boundaries, onboarding a team to a landscape, or diagnosing coupling and translation problems between teams.
- Try: _"Draw a context map for our retail platform: catalog, pricing, ordering, payment (external PSP), warehouse and CRM, owned by four teams."_
- Related: `event-storming`, `service-decomposition`, `aggregate-design`, `integration-pattern-selection`, `team-topology`
- File: [skills/04-architecture/software-architect/domain/bounded-context-map/SKILL.md](skills/04-architecture/software-architect/domain/bounded-context-map/SKILL.md)

**Design aggregates** · `aggregate-design`

- When: Designs DDD aggregates by deriving the aggregate root, boundaries and members from the invariants that must hold in one transaction, then defines commands, emitted events, identity, cross-aggregate references and eventual-consistency rules, and checks size and contention. Use when a domain model must be turned into consistency boundaries, when aggregates are too large or cause lock contention, or when deciding what must be strongly versus eventually consistent.
- Try: _"Design the aggregates for our ordering context; rules are credit limit per customer, max 50 lines per order, and no changes after dispatch."_
- Related: `event-storming`, `bounded-context-map`, `event-driven-design`, `database-schema-design`, `business-rules-catalog`
- File: [skills/04-architecture/software-architect/domain/aggregate-design/SKILL.md](skills/04-architecture/software-architect/domain/aggregate-design/SKILL.md)

**Design an event-driven flow** · `event-driven-design`

- When: Designs an event-driven flow end to end, covering event types and naming, schemas and versioning, topics and partition keys, ordering, delivery semantics, idempotent consumers, outbox publishing, error handling with retries and dead-letter queues, and saga orchestration or choreography with compensations. Use when services must integrate asynchronously through events, when a business process spans several services, or when an existing event flow suffers duplicates, lost messages or ordering bugs.
- Try: _"Design the event flow for order placement across ordering, payment, inventory and shipping, with compensation when payment fails."_
- Related: `event-storming`, `aggregate-design`, `integration-pattern-selection`, `data-contract`, `schema-evolution-plan`
- File: [skills/04-architecture/software-architect/domain/event-driven-design/SKILL.md](skills/04-architecture/software-architect/domain/event-driven-design/SKILL.md)

**Decompose into services** · `service-decomposition`

- When: Decomposes a system or monolith into service or module boundaries by combining business capabilities, bounded contexts, data ownership, change and scaling drivers and team structure, then evaluates each candidate for coupling, chattiness and distributed-transaction risk and recommends a granularity, including a modular monolith when services are not justified. Use when splitting a monolith, designing a new service landscape, or reviewing whether existing services are too fine or too coarse.
- Try: _"We want to split our 400k-line insurance monolith into services; help us find the boundaries and data ownership for policy, claims, billing and customer."_
- Related: `bounded-context-map`, `event-storming`, `migration-strategy`, `team-topology`, `database-schema-design`
- File: [skills/04-architecture/software-architect/domain/service-decomposition/SKILL.md](skills/04-architecture/software-architect/domain/service-decomposition/SKILL.md)

#### Architecture Evolution

**Assess technical debt** · `tech-debt-assessment`

- When: Builds a technical debt register by inventorying debt items across code, architecture, tests, infrastructure, dependencies and documentation, classifying them (deliberate/inadvertent, prudent/reckless), estimating principal (cost to fix) and interest (ongoing cost and risk), and prioritizing them into a paydown plan tied to business impact. Use when a team feels slowed down by the codebase, when leadership asks how much debt exists and what to fix first, or when debt must be justified in planning.
- Try: _"Assess the technical debt in our billing platform; releases take two weeks, test coverage is 30% and we still run an unsupported framework version."_
- Related: `code-quality-report`, `refactoring`, `modernization-assessment`, `dependency-upgrade`, `technical-risk-review`
- File: [skills/04-architecture/software-architect/evolution/tech-debt-assessment/SKILL.md](skills/04-architecture/software-architect/evolution/tech-debt-assessment/SKILL.md)

**Plan a migration** · `migration-strategy`

- When: Plans how to move from a current system or platform to a target one by comparing strangler fig, parallel run, phased and big-bang approaches, defining slices and their order, data migration and synchronization, coexistence and routing, verification and rollback per step, and cutover criteria. Use when replacing or re-platforming a system, extracting services from a monolith, moving to a new database or cloud, or when a migration plan needs a risk review.
- Try: _"Plan the migration of our on-premise order management monolith to the new cloud-based order services without downtime during the sales season."_
- Related: `target-state-architecture`, `service-decomposition`, `modernization-assessment`, `rollback-plan`, `schema-migration-plan`
- File: [skills/04-architecture/software-architect/evolution/migration-strategy/SKILL.md](skills/04-architecture/software-architect/evolution/migration-strategy/SKILL.md)

**Assess a legacy system** · `modernization-assessment`

- When: Assesses a legacy system across business fit, technical health, operational risk and change drivers, then evaluates the 7R options (retire, retain, rehost, relocate, replatform, repurchase, refactor/re-architect) with relative effort, value and risk, and recommends a path with decision criteria and first steps. Use when a legacy application is under pressure (end of support, cost, skills, scalability, compliance), when leadership asks \"what should we do with system X?\", or before committing budget to a migration or rewrite.
- Try: _"Assess our 15-year-old .NET Framework order management monolith on-premises. Support for its OS ends next year and only two people know it. What are our options?"_
- Related: `legacy-code-comprehension`, `tech-debt-assessment`, `migration-strategy`, `build-vs-buy`, `application-portfolio-assessment`
- File: [skills/04-architecture/software-architect/evolution/modernization-assessment/SKILL.md](skills/04-architecture/software-architect/evolution/modernization-assessment/SKILL.md)

**Plan an API deprecation** · `api-deprecation-plan`

- When: Plans the deprecation and removal of an API, version, endpoint, field or event with a consumer inventory, versioning strategy, machine-readable Deprecation/Sunset signalling, a migration guide, brownouts and measurable removal gates. Use when a breaking change, a new API version or a retired endpoint must reach internal, partner or public consumers without surprise outages.
- Try: _"We are replacing /v1/orders with /v2/orders (new pagination and money format). Plan the deprecation of v1 for our partners and internal apps."_
- Related: `api-design-review`, `api-contract`, `migration-strategy`, `api-reference-docs`, `product-sunset-plan`
- File: [skills/04-architecture/software-architect/evolution/api-deprecation-plan/SKILL.md](skills/04-architecture/software-architect/evolution/api-deprecation-plan/SKILL.md)

**Review an API design** · `api-design-review`

- When: Reviews an API design (OpenAPI/AsyncAPI spec, gRPC/protobuf definition, GraphQL schema or a written proposal) for resource modeling, naming consistency, versioning and compatibility, error model, pagination and filtering, idempotency and concurrency, security and operability, and returns rated findings with concrete fixes. Use when an API is proposed or changed before implementation or publication, when a public or partner API is about to be released, or when an existing API needs a consistency audit.
- Try: _"Review this OpenAPI spec for our new orders API before we publish it to partners. Focus on versioning, errors and pagination."_
- Related: `api-contract`, `api-deprecation-plan`, `api-test-design`, `threat-model`, `api-reference-docs`
- File: [skills/04-architecture/software-architect/evolution/api-design-review/SKILL.md](skills/04-architecture/software-architect/evolution/api-design-review/SKILL.md)

## Software Engineering

### Developer (Backend/Frontend/Mobile)

#### Technical Design

**Write a technical design doc (RFC)** · `technical-design-doc`

- When: Writes a technical design document (RFC) covering problem, goals and non-goals, proposed design, alternatives, rollout, risks and open questions, sized to the change. Use when a feature or change is large, risky or cross-team enough to need review before coding, or when someone asks for an RFC, design doc or technical proposal.
- Try: _"Write a design doc for moving our order confirmation emails from synchronous sending in the checkout request to an outbox plus background worker."_
- Related: `adr`, `solution-architecture-document`, `task-breakdown`, `api-contract`, `trade-off-analysis`
- File: [skills/05-engineering/developer/design/technical-design-doc/SKILL.md](skills/05-engineering/developer/design/technical-design-doc/SKILL.md)

**Break a story into tasks** · `task-breakdown`

- When: Breaks a user story or work item into ordered, independently verifiable technical tasks with dependencies, relative estimates and a definition of done per task. Use when a developer or team picks up a story and needs an implementation plan, wants to parallelize work, or asks how to split a story into tasks or subtasks.
- Try: _"Break this story into technical tasks: As a customer I want to download my invoices as PDF from the order history page."_
- Related: `user-story`, `story-splitting`, `technical-estimation`, `implement-from-story`, `technical-design-doc`
- File: [skills/05-engineering/developer/design/task-breakdown/SKILL.md](skills/05-engineering/developer/design/task-breakdown/SKILL.md)

**Write an API contract** · `api-contract`

- When: Writes an API contract as an OpenAPI (HTTP) or AsyncAPI (events/messages) specification from requirements, including resources, operations, schemas, error model, security, versioning and examples. Use when a new endpoint, service or event must be agreed between producer and consumers before implementation, or when someone asks for an OpenAPI/Swagger or AsyncAPI spec.
- Try: _"Write an OpenAPI contract for a service that lets partners create shipments, get shipment status and cancel a shipment before pickup."_
- Related: `api-design-review`, `api-reference-docs`, `integration-requirements`, `technical-design-doc`, `api-test-design`
- File: [skills/05-engineering/developer/design/api-contract/SKILL.md](skills/05-engineering/developer/design/api-contract/SKILL.md)

**Design a database schema** · `database-schema-design`

- When: Designs a relational database schema from a domain description: tables, columns and types, primary and foreign keys, constraints, indexes driven by access patterns, and a migration script outline. Use when a new feature needs persistent storage, an existing schema must be extended, or someone asks for tables, an ER model, DDL or indexes for a domain.
- Try: _"Design the database schema for a meeting room booking feature: rooms, bookings with start/end time, attendees, and no overlapping bookings per room."_
- Related: `logical-data-model`, `data-requirements`, `schema-migration-plan`, `index-recommendation`, `aggregate-design`
- File: [skills/05-engineering/developer/design/database-schema-design/SKILL.md](skills/05-engineering/developer/design/database-schema-design/SKILL.md)

**Write a spike report** · `spike-report`

- When: Writes a spike report that records the question a time-boxed investigation had to answer, what was tried, evidence found, options with trade-offs and a clear recommendation with follow-up work. Use when a spike, proof of concept or technical investigation has finished (or is being planned) and its result must be shared so the team can decide and estimate.
- Try: _"Write a spike report: we spent two days checking whether our current search can handle typo-tolerant product search or whether we need a dedicated search engine."_
- Related: `technical-design-doc`, `adr`, `technology-selection`, `trade-off-analysis`, `task-breakdown`
- File: [skills/05-engineering/developer/design/spike-report/SKILL.md](skills/05-engineering/developer/design/spike-report/SKILL.md)

#### Implementation

**Implement a feature from a story** · `implement-from-story`

- When: Plans and implements a feature from a user story by mapping acceptance criteria to behaviors, reading the existing code conventions, writing code and tests in small verifiable steps, and reporting what was built, how it was verified and what remains open. Use when a developer asks to implement, build or code a story, ticket or feature against given acceptance criteria.
- Try: _"Implement this story in our service: a customer can set a default shipping address; only one address can be default; the default is preselected at checkout."_
- Related: `task-breakdown`, `acceptance-criteria`, `tdd-cycle`, `unit-test-writing`, `pull-request-description`
- File: [skills/05-engineering/developer/coding/implement-from-story/SKILL.md](skills/05-engineering/developer/coding/implement-from-story/SKILL.md)

**Refactor code** · `refactoring`

- When: Refactors code safely by identifying the smells that matter for the next change, securing behavior with characterization tests, and applying named refactorings (Extract Function, Replace Conditional with Polymorphism, Introduce Parameter Object, etc.) in small behavior-preserving steps. Use when code is hard to change, before adding a feature to messy code, or when someone asks to clean up, restructure or refactor code without changing behavior.
- Try: _"Refactor this 200-line calculatePrice method; I need to add a new discount type next sprint and every change here breaks something."_
- Related: `clean-code-review`, `legacy-code-comprehension`, `unit-test-writing`, `tech-debt-assessment`, `code-review`
- File: [skills/05-engineering/developer/coding/refactoring/SKILL.md](skills/05-engineering/developer/coding/refactoring/SKILL.md)

**Review for clean code** · `clean-code-review`

- When: Reviews code for maintainability: naming, function size and responsibility, SOLID and coupling, duplication, comments, and recognizable code smells, producing prioritized findings with location, impact and a concrete fix. Use when someone asks whether code is clean, readable or well designed, wants a maintainability review of a file, class or module, or prepares code for handover.
- Try: _"Do a clean code review of this OrderService class; it has grown over two years and new people struggle to change it."_
- Related: `refactoring`, `code-review`, `coding-standards`, `review-comment-writing`, `code-quality-report`
- File: [skills/05-engineering/developer/coding/clean-code-review/SKILL.md](skills/05-engineering/developer/coding/clean-code-review/SKILL.md)

**Review error handling** · `error-handling-review`

- When: Reviews how code detects, propagates, retries, falls back from and reports errors: exception design, swallowed or over-broad catches, retry and timeout policy, idempotency, resource cleanup, transactional consistency and user-facing error messages. Use when failures are silent or confusing, before hardening a service or integration, or when someone asks to review error handling, exceptions or resilience of code.
- Try: _"Review the error handling in this payment client: it calls the provider over HTTP, retries on failure and updates the order status."_
- Related: `resilience-review`, `logging-instrumentation`, `error-message-writing`, `code-review`, `error-scenario-catalog`
- File: [skills/05-engineering/developer/coding/error-handling-review/SKILL.md](skills/05-engineering/developer/coding/error-handling-review/SKILL.md)

**Add logging and instrumentation** · `logging-instrumentation`

- When: Adds structured logs, metrics and distributed traces to code at the points that answer real operational questions, with consistent field names, correct levels, low-cardinality metric labels, trace context propagation and no secrets or personal data. Use when a feature is going to production, an incident showed missing visibility, or someone asks to add logging, metrics, tracing or telemetry (e.g. OpenTelemetry) to code.
- Try: _"Add logging, metrics and tracing to this order import job that reads a file, validates rows and calls the inventory API."_
- Related: `observability-plan`, `alert-design`, `slo-definition`, `error-handling-review`, `log-analysis`
- File: [skills/05-engineering/developer/coding/logging-instrumentation/SKILL.md](skills/05-engineering/developer/coding/logging-instrumentation/SKILL.md)

**Optimize performance** · `performance-optimization`

- When: Finds and fixes performance hotspots in code from measurements rather than guesses: defines the target metric, reads profiles, traces or query plans, ranks bottlenecks by share of cost, proposes fixes with expected gain and trade-offs, and specifies how to verify the improvement. Use when code, an endpoint or a job is too slow or too resource-hungry, or someone asks to optimize, speed up or reduce CPU, memory or latency.
- Try: _"Our order search endpoint has a p95 of 2.4 s under normal load. Here is the handler code and a CPU profile, help me make it faster."_
- Related: `sql-query-writing`, `query-optimization`, `load-test-analysis`, `web-performance-audit`, `logging-instrumentation`
- File: [skills/05-engineering/developer/coding/performance-optimization/SKILL.md](skills/05-engineering/developer/coding/performance-optimization/SKILL.md)

**Review concurrency** · `concurrency-review`

- When: Reviews code for concurrency defects: data races, check-then-act and lost updates, deadlocks and lock ordering, unsafe publication, async/await misuse, thread-pool starvation, and duplicate or out-of-order processing in distributed consumers, with a concrete interleaving and fix per finding. Use when code uses threads, async, locks, shared state, background workers, message consumers or concurrent database updates, or when someone reports intermittent failures that look timing-related.
- Try: _"Review this wallet top-up service for concurrency problems; it reads the balance, adds the amount and saves, and is called from both the API and a message consumer."_
- Related: `code-review`, `error-handling-review`, `debugging-hypotheses`, `resilience-review`, `integration-test-writing`
- File: [skills/05-engineering/developer/coding/concurrency-review/SKILL.md](skills/05-engineering/developer/coding/concurrency-review/SKILL.md)

**Upgrade a dependency** · `dependency-upgrade`

- When: Plans and executes a library, framework or runtime upgrade: reads release notes and migration guides between the current and target versions, lists breaking changes that actually affect the codebase, orders migration steps, handles transitive conflicts and defines verification and rollback. Use when a dependency must be upgraded for security, end of support or a needed feature, when an automated update pull request fails, or when someone asks how to move from version X to Y.
- Try: _"Plan the upgrade of our web framework from major version 6 to 8; here is the dependency manifest and the list of features we use."_
- Related: `dependency-vulnerability-review`, `semantic-versioning`, `refactoring`, `changelog-entry`, `pull-request-description`
- File: [skills/05-engineering/developer/coding/dependency-upgrade/SKILL.md](skills/05-engineering/developer/coding/dependency-upgrade/SKILL.md)

**Explain code** · `code-explanation`

- When: Explains what a piece of code does, why it is likely written that way and what risks it carries, at the depth the reader needs: a one-paragraph summary, a step-by-step walkthrough of control and data flow, side effects, assumptions, edge cases and suspicious spots. Use when someone pastes code and asks what it does, how it works, why it behaves a certain way, or needs to understand code before changing or reviewing it.
- Try: _"Explain what this function does and whether anything in it looks risky."_
- Related: `legacy-code-comprehension`, `code-documentation`, `clean-code-review`, `regex-builder`, `technical-onboarding`
- File: [skills/05-engineering/developer/coding/code-explanation/SKILL.md](skills/05-engineering/developer/coding/code-explanation/SKILL.md)

**Understand legacy code** · `legacy-code-comprehension`

- When: Builds a working map of unfamiliar or legacy code: entry points, modules and their responsibilities, main runtime flows, data stores, external integrations, hidden business rules, dead or risky areas and safe places to change, with every conclusion tied to evidence in the code. Use when a developer inherits a system, must change code nobody fully understands, plans a modernization, or asks how an old codebase works.
- Try: _"I inherited this billing module with no documentation. Here is the folder structure and the main classes; help me understand how an invoice gets created."_
- Related: `code-explanation`, `refactoring`, `tech-debt-assessment`, `modernization-assessment`, `business-rules-catalog`
- File: [skills/05-engineering/developer/coding/legacy-code-comprehension/SKILL.md](skills/05-engineering/developer/coding/legacy-code-comprehension/SKILL.md)

**Build and explain a regex** · `regex-builder`

- When: Writes a regular expression for a stated matching need in the target engine's dialect, with a plain-language breakdown, a table of should-match and should-not-match test cases, anchoring and escaping decisions, and a check for catastrophic backtracking. Also explains or fixes an existing regex. Use when someone needs a pattern to validate, extract, search or replace text, pastes a regex and asks what it does, or reports a regex that matches too much, too little or runs slowly.
- Try: _"Write a regex that extracts invoice numbers like INV-2024-000123 from email subjects; we use it in JavaScript."_
- Related: `code-explanation`, `unit-test-writing`, `data-quality-rules`, `secure-code-review`, `business-rules-catalog`
- File: [skills/05-engineering/developer/coding/regex-builder/SKILL.md](skills/05-engineering/developer/coding/regex-builder/SKILL.md)

**Write a SQL query** · `sql-query-writing`

- When: Writes a correct, readable and index-friendly SQL query for a stated question in the target database dialect: clarifies grain and join cardinality, handles NULLs, duplicates and time zones, uses sargable predicates and parameters, and states the indexes it relies on and how to verify results. Use when someone needs a query for a report, feature, data fix or investigation, asks to translate a question into SQL, or wants an existing query rewritten for correctness or readability.
- Try: _"Write a PostgreSQL query that returns, per customer, the number of orders and total revenue in the last 90 days, including customers with no orders."_
- Related: `query-optimization`, `index-recommendation`, `database-schema-design`, `metric-definition`, `performance-optimization`
- File: [skills/05-engineering/developer/coding/sql-query-writing/SKILL.md](skills/05-engineering/developer/coding/sql-query-writing/SKILL.md)

#### Developer Testing

**Write unit tests** · `unit-test-writing`

- When: Writes unit tests in Arrange-Act-Assert form that pin down observable behavior of a function, class or module, covering the happy path, equivalence classes, boundaries, error paths and state transitions, with test doubles only at true boundaries and names that read as specifications. Use when someone asks to write, add or improve unit tests, increase coverage of specific code, or secure code before a change.
- Try: _"Write unit tests for this ShippingCostCalculator class; it has rules for weight tiers, free shipping over a threshold and express surcharge."_
- Related: `tdd-cycle`, `test-gap-finder`, `integration-test-writing`, `equivalence-boundary-analysis`, `refactoring`
- File: [skills/05-engineering/developer/testing/unit-test-writing/SKILL.md](skills/05-engineering/developer/testing/unit-test-writing/SKILL.md)

**Write integration tests** · `integration-test-writing`

- When: Writes integration tests that exercise code across real boundaries (database, message broker, HTTP APIs, file storage, cache) with disposable real dependencies where feasible and test doubles only for systems the team does not own, covering mapping, transactions, serialization, error and timeout behavior, with isolated data and deterministic setup. Use when someone asks for integration tests, wants to verify a repository, API endpoint, consumer or external client against real infrastructure, or when unit tests with mocks cannot prove the behavior.
- Try: _"Write integration tests for our OrderRepository and the OrderPlaced consumer; we use a relational database and a message broker."_
- Related: `unit-test-writing`, `api-test-design`, `test-data-design`, `flaky-test-analysis`, `test-gap-finder`
- File: [skills/05-engineering/developer/testing/integration-test-writing/SKILL.md](skills/05-engineering/developer/testing/integration-test-writing/SKILL.md)

**Drive code with TDD** · `tdd-cycle`

- When: Drives a behavior into code with strict red-green-refactor cycles: a test list ordered from simplest to hardest, one failing test at a time that is seen failing for the right reason, the minimal code to pass, and refactoring only on green, with no production code written without a failing test. Use when someone wants to build a feature, function or bug fix test-first, asks for TDD steps, or wants to practice or demonstrate TDD on a concrete behavior.
- Try: _"Let's build a password strength validator with TDD: min 12 chars, at least one digit and one symbol, and it must reject the user's email."_
- Related: `unit-test-writing`, `implement-from-story`, `refactoring`, `acceptance-criteria`, `test-gap-finder`
- File: [skills/05-engineering/developer/testing/tdd-cycle/SKILL.md](skills/05-engineering/developer/testing/tdd-cycle/SKILL.md)

**Find untested code paths** · `test-gap-finder`

- When: Finds untested code paths by comparing code with its existing tests: enumerates branches, boundaries, error handlers, state transitions and requirement rules, maps each to covering tests, flags gaps and weak tests (no assertion, over-mocked, happy-path only), and ranks them by risk with a concrete test to add. Use when someone asks what is missing from the tests, wants to raise coverage meaningfully, reviews a pull request's tests, or has a coverage report and needs to know which gaps matter.
- Try: _"Here is our InvoiceService and its test class. Which paths are not tested and which gaps matter most?"_
- Related: `unit-test-writing`, `integration-test-writing`, `code-review`, `regression-selection`, `risk-based-testing`
- File: [skills/05-engineering/developer/testing/test-gap-finder/SKILL.md](skills/05-engineering/developer/testing/test-gap-finder/SKILL.md)

#### Code Collaboration

**Write a commit message** · `commit-message`

- When: Writes a commit message in Conventional Commits format with a precise subject, a body that explains why the change was made, and footers for breaking changes and work item references. Use when a developer has a diff, a list of changes or a short description and needs a commit message, or wants to split a mixed change into well-scoped commits.
- Try: _"Write a commit message for this diff. It adds retry with backoff to the payment client and fixes the timeout config key name."_
- Related: `pull-request-description`, `changelog-entry`, `semantic-versioning`, `branching-strategy`
- File: [skills/05-engineering/developer/collaboration/commit-message/SKILL.md](skills/05-engineering/developer/collaboration/commit-message/SKILL.md)

**Write a pull request description** · `pull-request-description`

- When: Writes a pull request description that states what changed, why, how it was tested, the risks and rollout notes, and where reviewers should focus. Use when a developer opens or updates a pull/merge request and has a diff, commit list, work item or rough notes to summarize for reviewers.
- Try: _"Write a PR description for these commits. The change moves invoice PDF generation to a background job."_
- Related: `commit-message`, `code-review`, `implement-from-story`, `release-notes`, `rollback-plan`
- File: [skills/05-engineering/developer/collaboration/pull-request-description/SKILL.md](skills/05-engineering/developer/collaboration/pull-request-description/SKILL.md)

**Review a pull request** · `code-review`

- When: Reviews a pull request or diff for correctness, design, tests, security, performance and readability, and returns prioritized, actionable findings with a clear verdict. Use when someone asks to review a PR, a diff, a patch or a code snippet before merge, or wants a second opinion on a change.
- Try: _"Review this pull request diff. It adds a discount calculation endpoint to the order service."_
- Related: `review-comment-writing`, `clean-code-review`, `secure-code-review`, `error-handling-review`, `pull-request-description`
- File: [skills/05-engineering/developer/collaboration/code-review/SKILL.md](skills/05-engineering/developer/collaboration/code-review/SKILL.md)

**Write review comments** · `review-comment-writing`

- When: Writes or rewrites code review comments so they are specific, kind and actionable, labeled by severity and intent (Critical, Required, Nit, Optional, FYI, plus question and praise) and backed by a reason and a proposed change. Use when a reviewer has raw observations or blunt draft comments on a pull request and wants them phrased clearly, or when review threads are turning tense.
- Try: _"Rewrite my review comments so they are clear but not harsh. First one is 'this is wrong, why would you query in a loop?'"_
- Related: `code-review`, `feedback-sbi`, `tone-rewrite`, `coding-standards`, `conflict-resolution`
- File: [skills/05-engineering/developer/collaboration/review-comment-writing/SKILL.md](skills/05-engineering/developer/collaboration/review-comment-writing/SKILL.md)

**Choose a branching strategy** · `branching-strategy`

- When: Recommends a branching strategy (trunk-based development, GitHub Flow, GitFlow or a documented variant) based on release cadence, number of supported versions, team size, CI maturity and compliance needs, and defines the resulting branch, merge and release rules. Use when a team sets up a repository, struggles with merge conflicts or long-lived branches, changes its release model, or must support multiple production versions.
- Try: _"We are 12 developers on one service, we deploy weekly but want daily, and hotfixes take too long because of our develop branch. Which branching strategy should we use?"_
- Related: `pipeline-design`, `release-plan`, `semantic-versioning`, `deployment-strategy`, `working-agreement`
- File: [skills/05-engineering/developer/collaboration/branching-strategy/SKILL.md](skills/05-engineering/developer/collaboration/branching-strategy/SKILL.md)

#### Debugging

**Reproduce a bug** · `bug-reproduction`

- When: Turns a vague bug report into a minimal, deterministic reproduction with exact steps, environment, data preconditions, expected versus actual result and a reproduction rate, ideally ending in a failing automated test. Use when a defect is reported as hard to reproduce, intermittent, environment-specific, or only described in user terms, and before starting a fix.
- Try: _"Users say the export sometimes produces an empty file. Help me build a reliable reproduction."_
- Related: `bug-report`, `debugging-hypotheses`, `log-analysis`, `unit-test-writing`, `flaky-test-analysis`
- File: [skills/05-engineering/developer/debugging/bug-reproduction/SKILL.md](skills/05-engineering/developer/debugging/bug-reproduction/SKILL.md)

**Analyze a stack trace** · `stack-trace-analysis`

- When: Analyzes a stack trace or crash report to identify the failing frame, the exception chain and root cause candidates, and proposes fixes and the next diagnostic step. Use when a developer pastes an exception, stack trace, crash log, panic or unhandled error from any language or runtime and asks what went wrong or where to look.
- Try: _"What is causing this stack trace? NullPointerException in OrderMapper.toDto called from OrderController.getOrder."_
- Related: `debugging-hypotheses`, `log-analysis`, `bug-reproduction`, `error-handling-review`, `code-explanation`
- File: [skills/05-engineering/developer/debugging/stack-trace-analysis/SKILL.md](skills/05-engineering/developer/debugging/stack-trace-analysis/SKILL.md)

**Analyze logs** · `log-analysis`

- When: Analyzes application, infrastructure or access logs to build a timeline, correlate events across services by request or trace ID, detect anomalies and error clusters, and state what the evidence supports and what it does not. Use when a developer shares log excerpts or exports around an incident, failure, slowdown or odd behavior and asks what happened, when it started or which component is at fault.
- Try: _"Here are logs from the API gateway and the order service between 14:00 and 14:20. What happened when checkout started failing?"_
- Related: `stack-trace-analysis`, `debugging-hypotheses`, `incident-response`, `postmortem`, `logging-instrumentation`
- File: [skills/05-engineering/developer/debugging/log-analysis/SKILL.md](skills/05-engineering/developer/debugging/log-analysis/SKILL.md)

**Generate debugging hypotheses** · `debugging-hypotheses`

- When: Generates a ranked list of debugging hypotheses from symptoms and evidence, and pairs each with the cheapest discriminating test, so the investigation converges instead of wandering. Use when a bug's cause is unknown, several explanations seem plausible, a debugging session is going in circles, or a team needs to split investigation work.
- Try: _"After the last deploy, about 2% of API requests take over 5 seconds, only on some pods. Give me ranked hypotheses and how to test each."_
- Related: `bug-reproduction`, `stack-trace-analysis`, `log-analysis`, `five-whys`, `fishbone-analysis`
- File: [skills/05-engineering/developer/debugging/debugging-hypotheses/SKILL.md](skills/05-engineering/developer/debugging/debugging-hypotheses/SKILL.md)

#### Developer Documentation

**Write a README** · `readme-writing`

- When: Writes or restructures a repository README that states what the project is, who it is for, how to get it running, how to use and configure it, and how to contribute, with commands that can be copied and verified. Use when a repository has no README, an outdated or sprawling one, new joiners struggle to run the project, or a library or service is about to be shared with other teams.
- Try: _"Write a README for our internal invoice-service repo. It is a REST API with a PostgreSQL database and a background worker; here is the folder structure and the Makefile."_
- Related: `code-documentation`, `api-reference-docs`, `technical-onboarding`, `how-to-guide`, `changelog-entry`
- File: [skills/05-engineering/developer/docs/readme-writing/SKILL.md](skills/05-engineering/developer/docs/readme-writing/SKILL.md)

**Write code documentation** · `code-documentation`

- When: Writes or improves docstrings, API comments and inline comments so they state contracts, intent, constraints and non-obvious reasons (the why), not a restatement of the code (the what), and flags comments that are wrong, stale or should become code. Use when a developer asks to document a function, class, module or public API, to review existing comments, or to prepare code for handover.
- Try: _"Add proper documentation to this pricing module. Keep it useful; I do not want comments that just repeat the code."_
- Related: `readme-writing`, `api-reference-docs`, `clean-code-review`, `code-explanation`, `legacy-code-comprehension`
- File: [skills/05-engineering/developer/docs/code-documentation/SKILL.md](skills/05-engineering/developer/docs/code-documentation/SKILL.md)

**Write API reference docs** · `api-reference-docs`

- When: Writes API reference documentation for HTTP, RPC or message-based APIs, covering authentication, each endpoint or operation with parameters, request and response examples, error codes, pagination, rate limits and versioning, derived from a contract, code or notes. Use when an API needs consumer-facing reference docs, existing docs drift from the implementation, or a spec exists but lacks descriptions and examples.
- Try: _"Write API reference docs for our orders API from this OpenAPI file. Consumers keep asking what the error codes mean and how paging works."_
- Related: `api-contract`, `api-design-review`, `readme-writing`, `error-message-writing`, `changelog-entry`
- File: [skills/05-engineering/developer/docs/api-reference-docs/SKILL.md](skills/05-engineering/developer/docs/api-reference-docs/SKILL.md)

**Write a changelog entry** · `changelog-entry`

- When: Writes changelog entries in the Keep a Changelog format (Added, Changed, Deprecated, Removed, Fixed, Security) from commits, merged pull requests or a change list, written for the people who consume the software, with breaking changes and migration steps called out. Use when preparing a release section, updating the Unreleased section after a merge, or turning noisy commit history into a readable change history.
- Try: _"Turn these merged PR titles into a changelog entry for version 2.4.0 of our client library."_
- Related: `commit-message`, `release-notes`, `semantic-versioning`, `pull-request-description`, `app-store-release-notes`
- File: [skills/05-engineering/developer/docs/changelog-entry/SKILL.md](skills/05-engineering/developer/docs/changelog-entry/SKILL.md)

#### Frontend Specific

**Design a UI component** · `component-design`

- When: Designs the technical API of a UI component before implementation: responsibility, props or inputs, internal and controlled state, events, slots or composition points, variants, visual and interaction states, accessibility semantics and keyboard behavior, and test cases, in a framework-neutral form. Use when a developer is about to build or refactor a reusable component, a design handoff must be turned into a component contract, or a component has grown too many props.
- Try: _"Design the component API for a searchable select (combobox) we will reuse across our admin screens. It needs async options and multi-select."_
- Related: `design-system-component-spec`, `accessibility-audit`, `state-management-design`, `unit-test-writing`, `design-handoff`
- File: [skills/05-engineering/developer/frontend/component-design/SKILL.md](skills/05-engineering/developer/frontend/component-design/SKILL.md)

**Audit accessibility (WCAG)** · `accessibility-audit`

- When: Audits a web or mobile UI (page, flow, component, or its markup) against WCAG 2.2 Level A and AA success criteria, records each finding with the criterion, affected users, evidence and severity, and proposes concrete code or design fixes. Use when a screen or component needs an accessibility check before release, after a complaint or legal request, or when someone asks \"is this accessible?\" or \"check this for WCAG\".
- Try: _"Audit this checkout form markup against WCAG 2.2 AA and tell me what to fix first."_
- Related: `component-design`, `heuristic-evaluation`, `design-handoff`, `microcopy`, `test-case-writing`
- File: [skills/05-engineering/developer/frontend/accessibility-audit/SKILL.md](skills/05-engineering/developer/frontend/accessibility-audit/SKILL.md)

**Audit web performance** · `web-performance-audit`

- When: Audits a web page or front-end application for loading and runtime performance using Core Web Vitals (LCP, INP, CLS) and supporting metrics, traces each problem to its cause in the critical rendering path, JavaScript, images, fonts or third parties, and returns prioritized fixes with expected effect and a way to verify them. Use when a page feels slow, Core Web Vitals fail in field data, a performance budget is exceeded, or a lab report or trace needs interpreting.
- Try: _"Our product listing page has LCP around 4.8 s and INP 350 ms on mobile. Here is the lab report and the page's head section. What should we fix first?"_
- Related: `performance-optimization`, `performance-test-plan`, `observability-plan`, `slo-definition`, `component-design`
- File: [skills/05-engineering/developer/frontend/web-performance-audit/SKILL.md](skills/05-engineering/developer/frontend/web-performance-audit/SKILL.md)

**Design state management** · `state-management-design`

- When: Designs where each piece of front-end state lives (local component, URL, form, shared client, server cache, persisted) and how it flows, is synchronized, invalidated and tested, in a framework-neutral way, and justifies any global store. Use when starting a front-end feature or app, when state is duplicated or out of sync between screens, when a team debates adopting or removing a global store, or when server data caching and optimistic updates must be decided.
- Try: _"Our order management screens keep showing stale data after edits and we have everything in one global store. Help us redesign the state management."_
- Related: `component-design`, `technical-design-doc`, `api-contract`, `adr`, `web-performance-audit`
- File: [skills/05-engineering/developer/frontend/state-management-design/SKILL.md](skills/05-engineering/developer/frontend/state-management-design/SKILL.md)

#### Mobile Specific

**Write app store release notes** · `app-store-release-notes`

- When: Writes short, user-facing \"What's new\" release notes for mobile app stores from a changelog, ticket list or pull request titles, filters out internal changes, fits each store's character limit and prepares localized variants. Use when a mobile version is about to be submitted to an app store, when a raw changelog must be turned into store copy, or when notes must be localized or shortened for a store.
- Try: _"Turn this sprint's merged PR titles into App Store and Google Play release notes for version 5.3, in English and Turkish."_
- Related: `release-notes`, `changelog-entry`, `mobile-release-checklist`, `microcopy`, `voice-and-tone-guide`
- File: [skills/05-engineering/developer/mobile/app-store-release-notes/SKILL.md](skills/05-engineering/developer/mobile/app-store-release-notes/SKILL.md)

**Run a mobile release checklist** · `mobile-release-checklist`

- When: Builds and runs a go/no-go checklist for a mobile app release covering versioning, build and signing, permissions and privacy declarations, store listing and assets, quality gates, backend and forced-update compatibility, staged rollout, monitoring and rollback, and reports each item as done, open or blocked with evidence. Use when an iOS or Android build is being prepared for store submission or phased rollout, or when a team wants a repeatable mobile release checklist.
- Try: _"We're submitting version 4.2.0 of our Android and iOS apps next Tuesday. It adds location-based offers. Run the mobile release checklist with me."_
- Related: `app-store-release-notes`, `release-quality-gate`, `deployment-checklist`, `rollback-plan`, `go-no-go`
- File: [skills/05-engineering/developer/mobile/mobile-release-checklist/SKILL.md](skills/05-engineering/developer/mobile/mobile-release-checklist/SKILL.md)

### Tech Lead

#### Technical Leadership

**Write coding standards** · `coding-standards`

- When: Writes or revises a team's coding standards as a short set of numbered rules, each with rationale, a good and a bad example, a severity (must or should) and how it is enforced (formatter, linter, review, test), focusing on decisions that tools cannot settle. Use when a team is forming or merging, reviews keep arguing about the same style or design questions, a new language or framework is adopted, or existing standards are too long, outdated or ignored.
- Try: _"Write coding standards for our backend team. We keep arguing in reviews about exception handling, naming and how big a pull request should be."_
- Related: `clean-code-review`, `code-review`, `review-comment-writing`, `working-agreement`, `adr`
- File: [skills/05-engineering/tech-lead/leadership/coding-standards/SKILL.md](skills/05-engineering/tech-lead/leadership/coding-standards/SKILL.md)

**Estimate technical work** · `technical-estimation`

- When: Produces a defensible estimate for technical work by decomposing it into small verifiable tasks ordered by dependency and risk, estimating each as a range, making assumptions and unknowns explicit, adding integration, testing and release effort, and stating confidence and what would change the number. Use when a tech lead is asked \"how long will this take?\", when a feature, migration or technical initiative needs sizing for planning or commitment, or when an existing estimate must be challenged or re-baselined.
- Try: _"Product wants to know how long it will take to add SSO with our corporate identity provider to our web app. Give me an estimate with ranges and assumptions."_
- Related: `task-breakdown`, `estimation-three-point`, `spike-report`, `technical-risk-review`, `monte-carlo-forecast`
- File: [skills/05-engineering/tech-lead/leadership/technical-estimation/SKILL.md](skills/05-engineering/tech-lead/leadership/technical-estimation/SKILL.md)

**Onboard a developer** · `technical-onboarding`

- When: Builds a technical onboarding plan for a developer joining a team: environment setup with verification, a guided codebase and architecture tour, ways of working, a sequence of progressively harder first work items, key contacts and checkpoints, adapted to the person's experience and role. Use when a new or transferring developer starts, when a tech lead must prepare the first weeks for a newcomer, or when an existing onboarding path is too slow and needs restructuring.
- Try: _"A mid-level backend developer joins our payments team on Monday. Prepare a technical onboarding plan for the first two weeks, including setup and first tickets."_
- Related: `onboarding-plan-30-60-90`, `readme-writing`, `legacy-code-comprehension`, `coding-standards`, `onboarding-guide`
- File: [skills/05-engineering/tech-lead/leadership/technical-onboarding/SKILL.md](skills/05-engineering/tech-lead/leadership/technical-onboarding/SKILL.md)

**Review technical risks** · `technical-risk-review`

- When: Runs a structured technical risk review of a feature, project or release plan: identifies delivery and quality risks across architecture, dependencies, technology novelty, data, integration, performance, security, operability, skills and schedule, rates probability and impact, names early warning signals, and proposes mitigations with owners and the cheapest risk-reducing experiments. Use at kickoff or before committing to a plan, before a major release, when a project shows warning signs, or when stakeholders ask what could go wrong technically.
- Try: _"We start a 3-month project to move invoice generation to an event-driven service. Review the technical risks before we commit to the plan."_
- Related: `risk-register`, `technical-estimation`, `spike-report`, `threat-model`, `architecture-review`
- File: [skills/05-engineering/tech-lead/leadership/technical-risk-review/SKILL.md](skills/05-engineering/tech-lead/leadership/technical-risk-review/SKILL.md)

**Report on code quality** · `code-quality-report`

- When: Interprets static analysis and code metrics (coverage, complexity, duplication, code smells, vulnerabilities, dependency age) and their trends into a code quality report that separates signal from noise, links hotspots to change frequency and defects, and recommends a small set of prioritized actions. Use when a tech lead must report code health to the team or management, when quality gate results or a metrics dashboard need interpretation, or when deciding where to invest refactoring effort.
- Try: _"Here is our static analysis export for the last three releases. Write a code quality report for the engineering manager and tell us where to focus next quarter."_
- Related: `tech-debt-assessment`, `coding-standards`, `test-gap-finder`, `refactoring`, `defect-trend-analysis`
- File: [skills/05-engineering/tech-lead/leadership/code-quality-report/SKILL.md](skills/05-engineering/tech-lead/leadership/code-quality-report/SKILL.md)

## Quality Assurance & Testing

### QA Analyst / Test Engineer

#### Test Strategy & Planning

**Write a test strategy** · `test-strategy`

- When: Writes a test strategy that defines test levels, test types, environments, tooling categories, data approach and a risk-based focus for a product, program or organization. Use when a new product or major initiative starts, when testing approach is inconsistent across teams, or when someone asks how a system should be tested overall.
- Try: _"Write a test strategy for our new customer onboarding platform: web + mobile front ends, 12 microservices, integrations with a core banking system and a KYC provider."_
- Related: `test-plan`, `risk-based-testing`, `environment-strategy`, `automation-framework-design`, `nfr-specification`
- File: [skills/06-quality/qa-analyst/strategy/test-strategy/SKILL.md](skills/06-quality/qa-analyst/strategy/test-strategy/SKILL.md)

**Write a test plan** · `test-plan`

- When: Writes a test plan for a release, project or feature set, covering test items, scope, approach, environments, schedule, roles, entry/exit and suspension criteria, deliverables and risks, aligned with ISO/IEC/IEEE 29119-3. Use when a release or project needs an agreed testing scope and schedule, or when someone asks for a test plan document.
- Try: _"Prepare a test plan for release 4.2 of the claims portal: new document upload, revised approval workflow, and two bug fixes. Code freeze is in three weeks."_
- Related: `test-strategy`, `risk-based-testing`, `release-quality-gate`, `test-summary-report`, `uat-plan`
- File: [skills/06-quality/qa-analyst/strategy/test-plan/SKILL.md](skills/06-quality/qa-analyst/strategy/test-plan/SKILL.md)

**Prioritize tests by risk** · `risk-based-testing`

- When: Prioritizes test effort by assessing product risk items for likelihood and impact, producing a risk matrix, a test depth per item and an execution order. Use when time or people are limited, when deciding what to test first or how deeply, or when stakeholders need to see which risks are covered and which remain.
- Try: _"We have 5 test days for this release. Here are the 14 changes. Tell me what to test first and how deep."_
- Related: `test-strategy`, `test-plan`, `regression-selection`, `risk-register`, `impact-analysis`
- File: [skills/06-quality/qa-analyst/strategy/risk-based-testing/SKILL.md](skills/06-quality/qa-analyst/strategy/risk-based-testing/SKILL.md)

**Review requirements for testability** · `testability-review`

- When: Reviews requirements, user stories or acceptance criteria for testability and flags items that are ambiguous, unmeasurable, incomplete, untestable or missing error behavior, with a concrete rewrite suggestion for each. Use before test design or estimation, in refinement sessions, or when someone asks whether requirements are clear enough to test.
- Try: _"Check these 8 user stories for testability before we start writing test cases."_
- Related: `ambiguity-detection`, `acceptance-criteria`, `requirements-review-checklist`, `test-scenarios-from-requirements`, `nfr-specification`
- File: [skills/06-quality/qa-analyst/strategy/testability-review/SKILL.md](skills/06-quality/qa-analyst/strategy/testability-review/SKILL.md)

#### Test Design

**Derive test scenarios** · `test-scenarios-from-requirements`

- When: Derives high-level test scenarios (positive, negative, edge, permission, integration and non-functional) from requirements, user stories, use cases or acceptance criteria, with traceability to the source and a priority for each. Use when test design starts for a feature, when checking coverage of a story, or when someone asks what should be tested for a requirement.
- Try: _"Derive test scenarios for this story: a customer can cancel an order until it is shipped and gets a refund to the original payment method."_
- Related: `test-case-writing`, `testability-review`, `equivalence-boundary-analysis`, `traceability-matrix`, `bdd-feature-file`
- File: [skills/06-quality/qa-analyst/design/test-scenarios-from-requirements/SKILL.md](skills/06-quality/qa-analyst/design/test-scenarios-from-requirements/SKILL.md)

**Write test cases** · `test-case-writing`

- When: Writes detailed, executable test cases with ID, title, preconditions, test data, numbered steps, expected results per step, priority and traceability to requirements. Use when scenarios need to become repeatable manual cases, when preparing cases for execution or automation, or when someone asks to write test cases for a feature or story.
- Try: _"Write test cases for the password reset flow: email link valid for 30 minutes, new password must meet the policy, old sessions are logged out."_
- Related: `test-scenarios-from-requirements`, `equivalence-boundary-analysis`, `test-data-design`, `test-automation-script`, `traceability-matrix`
- File: [skills/06-quality/qa-analyst/design/test-case-writing/SKILL.md](skills/06-quality/qa-analyst/design/test-case-writing/SKILL.md)

**Apply equivalence and boundary analysis** · `equivalence-boundary-analysis`

- When: Applies equivalence partitioning and boundary value analysis to input fields, parameters and business rules, producing valid and invalid partitions, boundary values (two- or three-value) and a minimal set of test values with expected outcomes. Use when an input has ranges, lengths, formats, dates or enumerations, or when someone asks which values to test for a field or rule.
- Try: _"Apply boundary value analysis to the loan application: amount 1,000-50,000, term 6-60 months, applicant age 18-70 at loan end."_
- Related: `test-case-writing`, `decision-table-testing`, `pairwise-testing`, `test-data-design`, `test-scenarios-from-requirements`
- File: [skills/06-quality/qa-analyst/design/equivalence-boundary-analysis/SKILL.md](skills/06-quality/qa-analyst/design/equivalence-boundary-analysis/SKILL.md)

**Build decision table tests** · `decision-table-testing`

- When: Builds decision tables from business rules by listing conditions and actions, enumerating combinations, collapsing irrelevant ones and deriving one test per rule column, while exposing missing and contradictory rules. Use when behavior depends on combinations of conditions (eligibility, pricing, approvals, discounts, routing), or when someone asks to test a set of if-then rules.
- Try: _"Build a decision table for shipping fees: free for members over 200 TL, 29 TL standard, express +40 TL, islands add 50 TL, members get express at half price."_
- Related: `equivalence-boundary-analysis`, `business-rules-catalog`, `test-case-writing`, `pairwise-testing`, `state-transition-testing`
- File: [skills/06-quality/qa-analyst/design/decision-table-testing/SKILL.md](skills/06-quality/qa-analyst/design/decision-table-testing/SKILL.md)

**Build state transition tests** · `state-transition-testing`

- When: Models an entity or workflow as states, events, guards and actions, then derives tests for all valid transitions, invalid transitions (state-event pairs that must be rejected) and key transition sequences (0-switch and 1-switch coverage). Use when behavior depends on status or history, such as orders, applications, approvals, accounts, sessions or devices, or when someone asks to test a workflow or lifecycle.
- Try: _"Create state transition tests for our purchase request: Draft, Submitted, Approved, Rejected, Cancelled, Ordered. Only the requester can cancel, only before Ordered."_
- Related: `state-model`, `decision-table-testing`, `test-case-writing`, `test-scenarios-from-requirements`, `api-test-design`
- File: [skills/06-quality/qa-analyst/design/state-transition-testing/SKILL.md](skills/06-quality/qa-analyst/design/state-transition-testing/SKILL.md)

**Generate pairwise combinations** · `pairwise-testing`

- When: Generates a reduced set of test combinations that covers every pair of parameter values (or higher strength for critical parameters), respecting constraints between values, and explains the reduction and residual risk. Use when many parameters or configurations (browsers, devices, roles, settings, product options) combine into too many cases to test exhaustively.
- Try: _"Generate pairwise combinations for checkout: 4 browsers, 3 payment methods, 2 user types, 3 delivery options, coupon yes/no. Apple Pay only on Safari."_
- Related: `equivalence-boundary-analysis`, `decision-table-testing`, `test-case-writing`, `risk-based-testing`, `test-data-design`
- File: [skills/06-quality/qa-analyst/design/pairwise-testing/SKILL.md](skills/06-quality/qa-analyst/design/pairwise-testing/SKILL.md)

**Write exploratory test charters** · `exploratory-test-charter`

- When: Writes session-based exploratory test charters with a mission, target areas, resources, risks to probe, test heuristics and oracles, a timebox and a debrief template for notes, bugs and questions. Use when a new or changed feature needs discovery testing, when scripted tests are not yet available or not enough, or when someone asks for exploratory testing ideas.
- Try: _"Write exploratory test charters for the new bulk import of product prices from CSV. We have 2 testers for one afternoon."_
- Related: `test-scenarios-from-requirements`, `risk-based-testing`, `bug-report`, `heuristic-evaluation`, `test-summary-report`
- File: [skills/06-quality/qa-analyst/design/exploratory-test-charter/SKILL.md](skills/06-quality/qa-analyst/design/exploratory-test-charter/SKILL.md)

**Design test data** · `test-data-design`

- When: Designs test datasets that are realistic, privacy-safe and cover partitions, boundaries, states and referential edge cases, with a provisioning and reset approach per environment. Use when tests need specific data, when production data is being considered for testing, when data setup is blocking execution or automation, or when someone asks what data a feature needs to be tested.
- Try: _"Design the test data for our loan application flow: applicants with different income bands, co-applicants, existing customers and blacklisted IDs, for SIT and UAT."_
- Related: `equivalence-boundary-analysis`, `test-case-writing`, `data-classification`, `environment-strategy`, `privacy-impact-assessment`
- File: [skills/06-quality/qa-analyst/design/test-data-design/SKILL.md](skills/06-quality/qa-analyst/design/test-data-design/SKILL.md)

**Write BDD feature files** · `bdd-feature-file`

- When: Writes Gherkin feature files with a business-readable feature description, background, declarative scenarios and scenario outlines with example tables, tagged and traceable to requirements. Use when a team practices behavior-driven development or specification by example, when acceptance criteria must become executable specifications, or when existing Gherkin is imperative, UI-bound or hard to maintain.
- Try: _"Write a feature file for the coupon rule: one coupon per order, minimum basket 250 TL, not combinable with campaign prices, expired coupons rejected."_
- Related: `acceptance-criteria`, `user-story`, `test-scenarios-from-requirements`, `test-automation-script`, `equivalence-boundary-analysis`
- File: [skills/06-quality/qa-analyst/design/bdd-feature-file/SKILL.md](skills/06-quality/qa-analyst/design/bdd-feature-file/SKILL.md)

**Design API tests** · `api-test-design`

- When: Designs API tests per endpoint covering contract and schema, status codes, authentication and authorization, input validation, business rules, idempotency, pagination, concurrency and error format, with negative and security-oriented cases. Use when an API contract (OpenAPI, GraphQL schema, gRPC proto or informal spec) needs a test design, before automating API tests, or when reviewing whether existing API tests are sufficient.
- Try: _"Design API tests for POST /orders and GET /orders/{id}: JWT auth, customers see only their own orders, idempotency key header, 422 on validation errors."_
- Related: `api-contract`, `api-design-review`, `test-automation-script`, `security-requirements`, `integration-test-writing`
- File: [skills/06-quality/qa-analyst/design/api-test-design/SKILL.md](skills/06-quality/qa-analyst/design/api-test-design/SKILL.md)

#### Execution & Defects

**Write a bug report** · `bug-report`

- When: Writes a reproducible, triage-ready bug report with a precise title, environment and build, preconditions, minimal numbered steps, expected versus actual result, reproduction rate, evidence, impact and a proposed severity. Use when a tester, developer or user has found a defect and it must be logged, when an existing report is vague or cannot be reproduced, or when someone pastes observations and asks to turn them into a bug ticket.
- Try: _"Write a bug report: on the iOS app, after changing the delivery address at checkout, the shipping fee still uses the old city. Happens most of the time, build 4.12.0 on staging."_
- Related: `bug-triage`, `bug-reproduction`, `log-analysis`, `test-case-writing`, `ticket-triage`
- File: [skills/06-quality/qa-analyst/execution/bug-report/SKILL.md](skills/06-quality/qa-analyst/execution/bug-report/SKILL.md)

**Triage bugs** · `bug-triage`

- When: Triages a set of bugs by validating completeness, detecting duplicates, separating severity (impact) from priority (order of fixing), assigning owner and target, and flagging release blockers, producing a decision table and follow-up list. Use when new or backlog defects must be reviewed in a triage meeting, when a release is near and open bugs need a blocker decision, or when someone asks which bugs to fix first.
- Try: _"Triage these 14 open bugs before Friday's release: decide severity, priority, duplicates and which ones block the release."_
- Related: `bug-report`, `release-quality-gate`, `defect-trend-analysis`, `risk-based-testing`, `ticket-triage`
- File: [skills/06-quality/qa-analyst/execution/bug-triage/SKILL.md](skills/06-quality/qa-analyst/execution/bug-triage/SKILL.md)

**Select regression tests** · `regression-selection`

- When: Selects a regression test set for a specific change by analyzing what changed, its direct and indirect impact (shared code, data, integrations, configuration), risk and recent defect history, then tiers tests into must-run, should-run and optional with explicit residual risk. Use when a release, hotfix or merge needs regression testing but the full suite is too slow or expensive, or when someone asks what must be retested after a change.
- Try: _"We changed the discount calculation service and upgraded the PDF library. Which regression tests must we run before tomorrow's hotfix?"_
- Related: `impact-analysis`, `risk-based-testing`, `test-summary-report`, `automation-candidate-selection`, `test-gap-finder`
- File: [skills/06-quality/qa-analyst/execution/regression-selection/SKILL.md](skills/06-quality/qa-analyst/execution/regression-selection/SKILL.md)

**Write a test summary report** · `test-summary-report`

- When: Writes a test summary (completion) report that states scope tested and not tested, execution results, coverage against requirements and risks, open defects by severity, deviations from the plan, residual risk and a clear recommendation, aligned with ISO/IEC/IEEE 29119-3 content. Use at the end of a test level, iteration or release cycle, when stakeholders need a decision-ready quality status, or when raw execution numbers must be turned into a report.
- Try: _"Write the test summary report for release 3.4 from these numbers: 412 cases, 389 passed, 11 failed, 12 blocked, 7 open bugs (1 critical), performance test not run."_
- Related: `test-plan`, `release-quality-gate`, `bug-triage`, `defect-trend-analysis`, `executive-summary`
- File: [skills/06-quality/qa-analyst/execution/test-summary-report/SKILL.md](skills/06-quality/qa-analyst/execution/test-summary-report/SKILL.md)

**Evaluate release readiness** · `release-quality-gate`

- When: Evaluates release readiness against agreed exit criteria (tests, defects, coverage, non-functional results, operational readiness, approvals), rates each criterion met, not met or waived with evidence, and produces a go, conditional go or no-go recommendation with conditions and accepted risks. Use before a production release or major deployment, in a go/no-go meeting, or when someone asks whether a build is ready to ship.
- Try: _"Assess release 5.2 against our exit criteria: no open critical/major bugs, 95% pass rate, regression complete, performance p95 under 800 ms, security scan clean."_
- Related: `test-summary-report`, `bug-triage`, `go-no-go`, `deployment-checklist`, `rollback-plan`
- File: [skills/06-quality/qa-analyst/execution/release-quality-gate/SKILL.md](skills/06-quality/qa-analyst/execution/release-quality-gate/SKILL.md)

**Analyze defect trends** · `defect-trend-analysis`

- When: Analyzes defect data over time to expose density, escape (leakage) rate, reopen rate, ageing and root-cause categories, separating real quality signals from reporting noise and ending with evidence-backed improvement actions. Use when a team asks why quality is dropping, prepares a retrospective or quality review, needs to explain production escapes, or has a defect export and wants the trends interpreted.
- Try: _"Here is our defect export for the last 6 releases. Analyze the trends: where are bugs coming from, how many escape to production, and what should we change?"_
- Related: `bug-triage`, `test-summary-report`, `five-whys`, `engineering-metrics-review`, `code-quality-report`
- File: [skills/06-quality/qa-analyst/execution/defect-trend-analysis/SKILL.md](skills/06-quality/qa-analyst/execution/defect-trend-analysis/SKILL.md)

#### User Acceptance

**Plan UAT** · `uat-plan`

- When: Plans user acceptance testing: objectives, business participants and their roles, scenario coverage, environment and data readiness, schedule, defect handling, entry/exit criteria and the formal sign-off route. Use when a release, project phase or vendor delivery needs business acceptance, when someone asks how to organize UAT, or when business users must confirm a solution supports their real work before go-live.
- Try: _"Plan UAT for the new invoicing module: finance and sales users will test for two weeks before the go-live."_
- Related: `uat-scenarios`, `test-plan`, `acceptance-certificate`, `requirements-sign-off`, `release-quality-gate`
- File: [skills/06-quality/qa-analyst/uat/uat-plan/SKILL.md](skills/06-quality/qa-analyst/uat/uat-plan/SKILL.md)

**Write UAT scenarios** · `uat-scenarios`

- When: Writes end-to-end user acceptance scenarios in business language, built from real roles, business events and outcomes rather than screens and clicks, each with realistic data, business-verifiable checkpoints and pass criteria. Use when business users need scenarios to execute in UAT, when requirements or processes must be turned into acceptance walkthroughs, or when existing UAT scripts read like technical test cases.
- Try: _"Write UAT scenarios for the returns process: store staff, warehouse and finance will test the new returns flow end to end."_
- Related: `uat-plan`, `test-scenarios-from-requirements`, `to-be-process`, `acceptance-criteria`, `test-data-design`
- File: [skills/06-quality/qa-analyst/uat/uat-scenarios/SKILL.md](skills/06-quality/qa-analyst/uat/uat-scenarios/SKILL.md)

### Test Automation Engineer

#### Automation

**Select automation candidates** · `automation-candidate-selection`

- When: Selects which tests to automate by scoring candidates on execution frequency, business risk, stability of the feature, determinism, data and environment control, and build/maintenance cost, then placing each at the cheapest reliable test level and returning a ranked backlog with a rough payback estimate. Use when a team asks what to automate next, has a large manual regression suite, needs to justify automation investment, or wants to stop automating low-value UI tests.
- Try: _"We have 350 manual regression cases. Which ones should we automate first, and at which level?"_
- Related: `automation-framework-design`, `test-automation-script`, `regression-selection`, `risk-based-testing`, `flaky-test-analysis`
- File: [skills/06-quality/automation-engineer/automation/automation-candidate-selection/SKILL.md](skills/06-quality/automation-engineer/automation/automation-candidate-selection/SKILL.md)

**Write an automated test** · `test-automation-script`

- When: Writes a maintainable automated test in the team's language and framework using page objects or API clients, independent test data, explicit condition-based waits and precise assertions, and first shows the test failing for the right reason. Use when a manual test case, scenario or Gherkin step must become automated test code, when someone asks for a UI or API test to be written, or when an existing automated test needs to be rewritten to be reliable.
- Try: _"Automate this test case as an API test in our TypeScript suite: creating an order with an expired coupon must return 422 and not reserve stock."_
- Related: `automation-candidate-selection`, `automation-framework-design`, `test-case-writing`, `bdd-feature-file`, `flaky-test-analysis`
- File: [skills/06-quality/automation-engineer/automation/test-automation-script/SKILL.md](skills/06-quality/automation-engineer/automation/test-automation-script/SKILL.md)

**Analyze flaky tests** · `flaky-test-analysis`

- When: Analyzes flaky automated tests by measuring flake rate from run history, classifying the cause (timing and async, shared state and order dependence, test data, environment and infrastructure, external dependencies, concurrency, non-deterministic product behavior), confirming it with one-variable experiments and proposing a root-cause stabilization plus a quarantine policy. Use when tests pass and fail without code changes, when CI reruns are routine, or when the team no longer trusts red builds.
- Try: _"These 6 end-to-end tests fail randomly in CI about once every 10 runs, never locally. Here are the failure logs. Why, and how do we fix them?"_
- Related: `test-automation-script`, `automation-framework-design`, `debugging-hypotheses`, `pipeline-failure-triage`, `log-analysis`
- File: [skills/06-quality/automation-engineer/automation/flaky-test-analysis/SKILL.md](skills/06-quality/automation-engineer/automation/flaky-test-analysis/SKILL.md)

**Design a test automation framework** · `automation-framework-design`

- When: Designs a test automation framework: test levels and their share, layered architecture (tests, business actions, page objects/API clients, drivers), test data and environment management, configuration and secrets, reporting and traceability, CI integration with parallelism and quality gates, and conventions for maintainability. Use when a team starts automation, when an existing suite is slow, brittle or unowned and needs a redesign, or when choosing a structure for UI, API and contract tests.
- Try: _"Design a test automation framework for our web app and its REST APIs; the suite must run on every pull request in under 15 minutes."_
- Related: `test-strategy`, `automation-candidate-selection`, `test-automation-script`, `pipeline-design`, `flaky-test-analysis`
- File: [skills/06-quality/automation-engineer/automation/automation-framework-design/SKILL.md](skills/06-quality/automation-engineer/automation/automation-framework-design/SKILL.md)

### Performance Test Engineer

#### Performance Testing

**Write a performance test plan** · `performance-test-plan`

- When: Writes a performance test plan with objectives tied to measurable acceptance criteria (latency percentiles, throughput, error rate, resource limits), a workload model derived from production data or business forecasts, test types (load, stress, soak, spike, scalability), scenarios, test data, environment and its gap to production, monitoring, entry/exit criteria and risks. Use before a release, migration or expected traffic increase, when non-functional requirements must be verified, or when a performance test must be designed from scratch.
- Try: _"We launch a campaign that may triple checkout traffic. Write a performance test plan for the checkout API and its dependencies."_
- Related: `load-test-analysis`, `capacity-test-report`, `slo-definition`, `test-data-design`, `nfr-to-architecture`
- File: [skills/06-quality/performance-engineer/performance/performance-test-plan/SKILL.md](skills/06-quality/performance-engineer/performance/performance-test-plan/SKILL.md)

**Analyze load test results** · `load-test-analysis`

- When: Analyzes load test results by validating the test run, comparing throughput, latency percentiles and error rates against acceptance criteria, correlating client-side results with server-side resource, pool, queue and database metrics to locate bottlenecks, and recommending evidence-based fixes and retests. Use when a load, stress, spike or soak test has been executed and its report, metrics or charts must be interpreted, or when a test result is disputed and needs a second opinion.
- Try: _"Here are the results of yesterday's checkout load test: summary table, latency chart description and database CPU. Did we pass, and what is the bottleneck?"_
- Related: `performance-test-plan`, `capacity-test-report`, `performance-optimization`, `query-optimization`, `observability-plan`
- File: [skills/06-quality/performance-engineer/performance/load-test-analysis/SKILL.md](skills/06-quality/performance-engineer/performance/load-test-analysis/SKILL.md)

**Write a capacity report** · `capacity-test-report`

- When: Writes a capacity test report that determines the maximum sustainable load within SLOs from stepped or stress test results, identifies the limiting resource, calculates headroom against current and forecast peaks, describes scaling behavior and its limits, and recommends capacity actions with their triggers. Use after capacity, stress or scalability tests, when leadership asks how much growth the system can absorb, or when infrastructure sizing and scaling limits must be justified with test evidence.
- Try: _"We ran a stepped load test on the search service up to failure. Write a capacity report: how much headroom do we have for next year's forecast?"_
- Related: `load-test-analysis`, `performance-test-plan`, `capacity-planning`, `scalability-review`, `finops-review`
- File: [skills/06-quality/performance-engineer/performance/capacity-test-report/SKILL.md](skills/06-quality/performance-engineer/performance/capacity-test-report/SKILL.md)

## DevOps, SRE & Platform

### DevOps / Platform Engineer

#### CI/CD

**Design a CI/CD pipeline** · `pipeline-design`

- When: Designs a CI/CD pipeline end to end: stages, quality and security gates, artifact handling, environments and promotion rules, independent of the CI product. Use when a team sets up a new pipeline, restructures a slow or fragile one, or needs to document how code moves from commit to production.
- Try: _"Design a CI/CD pipeline for our .NET API that deploys to Kubernetes in dev, staging and prod, with a manual approval before prod."_
- Related: `environment-strategy`, `deployment-strategy`, `branching-strategy`, `release-quality-gate`, `secrets-management-plan`
- File: [skills/07-devops-sre/devops-engineer/cicd/pipeline-design/SKILL.md](skills/07-devops-sre/devops-engineer/cicd/pipeline-design/SKILL.md)

**Triage a pipeline failure** · `pipeline-failure-triage`

- When: Analyzes a failed CI/CD run from its logs and context, classifies the failure (code, test, flaky, dependency, infrastructure, configuration, credentials), identifies the most likely cause with evidence and proposes a fix and a prevention step. Use when a build, test, scan or deploy job fails and someone pastes the log or error.
- Try: _"Our main branch pipeline started failing at the Docker build step this morning, here is the log. What is wrong and how do we fix it?"_
- Related: `pipeline-design`, `flaky-test-analysis`, `log-analysis`, `stack-trace-analysis`, `dependency-upgrade`
- File: [skills/07-devops-sre/devops-engineer/cicd/pipeline-failure-triage/SKILL.md](skills/07-devops-sre/devops-engineer/cicd/pipeline-failure-triage/SKILL.md)

**Choose a deployment strategy** · `deployment-strategy`

- When: Recommends a deployment strategy (recreate, rolling, blue-green, canary, shadow, feature flags or a combination) for a specific service by weighing risk, statefulness, database changes, traffic control, cost and rollback speed. Use when a team must decide how a release reaches users, or when current releases cause downtime or risky big-bang cutovers.
- Try: _"We deploy our payment service with a 20-minute maintenance window. Which deployment strategy should we move to so we get zero downtime?"_
- Related: `pipeline-design`, `rollback-plan`, `release-plan`, `schema-migration-plan`, `slo-definition`
- File: [skills/07-devops-sre/devops-engineer/cicd/deployment-strategy/SKILL.md](skills/07-devops-sre/devops-engineer/cicd/deployment-strategy/SKILL.md)

**Define environment strategy** · `environment-strategy`

- When: Defines the environment landscape for a system: which environments exist and why, parity with production, test data policy, access and change rights, lifecycle (persistent vs ephemeral) and ownership. Use when environments multiply without purpose, tests pass in staging but fail in production, or a new platform needs its environment model agreed.
- Try: _"We have dev, test, uat, preprod and prod and nobody knows which one to use for what. Define an environment strategy for us."_
- Related: `pipeline-design`, `test-data-design`, `secrets-management-plan`, `finops-review`, `deployment-strategy`
- File: [skills/07-devops-sre/devops-engineer/cicd/environment-strategy/SKILL.md](skills/07-devops-sre/devops-engineer/cicd/environment-strategy/SKILL.md)

#### Infrastructure & Containers

**Review a Dockerfile** · `dockerfile-review`

- When: Reviews a Dockerfile (or Containerfile) for image size, layer and cache efficiency, security hardening and build reproducibility, and returns prioritized findings with corrected snippets. Use when someone shares a Dockerfile for review, an image is large, slow to build or flagged by a scanner, or before a service's first production release.
- Try: _"Review this Dockerfile for our Node.js service. The image is 1.2 GB and the security scan reports 40 vulnerabilities."_
- Related: `kubernetes-manifest-review`, `pipeline-design`, `secrets-management-plan`, `dependency-vulnerability-review`
- File: [skills/07-devops-sre/devops-engineer/infrastructure/dockerfile-review/SKILL.md](skills/07-devops-sre/devops-engineer/infrastructure/dockerfile-review/SKILL.md)

**Review Kubernetes manifests** · `kubernetes-manifest-review`

- When: Reviews Kubernetes manifests, Helm charts or Kustomize output for resource requests and limits, health probes, security context, availability (replicas, disruption budgets, spread), configuration and secret handling, and operability. Returns prioritized findings with corrected YAML. Use when manifests are submitted for review, pods restart or get evicted, or a workload is being prepared for production.
- Try: _"Review this Deployment and Service YAML for our order API before we go live on the production cluster."_
- Related: `dockerfile-review`, `secrets-management-plan`, `capacity-planning`, `deployment-strategy`, `resilience-review`
- File: [skills/07-devops-sre/devops-engineer/infrastructure/kubernetes-manifest-review/SKILL.md](skills/07-devops-sre/devops-engineer/infrastructure/kubernetes-manifest-review/SKILL.md)

**Review infrastructure as code** · `iac-review`

- When: Reviews infrastructure as code (Terraform/OpenTofu, Bicep, CloudFormation, Pulumi, Ansible and similar) and plan output for security misconfigurations, state and drift risks, destructive changes, modularity, naming/tagging and cost. Use when an IaC pull request or plan needs review, before applying changes to shared or production infrastructure, or when auditing an existing IaC codebase.
- Try: _"Review this Terraform module and plan output. It creates a storage bucket, a database and a VPC for our new service."_
- Related: `secrets-management-plan`, `finops-review`, `environment-strategy`, `threat-model`, `pipeline-design`
- File: [skills/07-devops-sre/devops-engineer/infrastructure/iac-review/SKILL.md](skills/07-devops-sre/devops-engineer/infrastructure/iac-review/SKILL.md)

**Plan secrets management** · `secrets-management-plan`

- When: Produces a secrets management plan: inventory and classification of secrets, central store choice criteria, identity-based access with least privilege, injection into workloads and pipelines, rotation and revocation, audit, and break-glass. Use when a team stores secrets in code, config files or pipeline variables, after a leak, or when designing secret handling for a new platform.
- Try: _"Our database passwords and API keys are in appsettings files and pipeline variables. Write a plan to move to proper secrets management."_
- Related: `iac-review`, `pipeline-design`, `authn-authz-design`, `security-requirements`, `kubernetes-manifest-review`
- File: [skills/07-devops-sre/devops-engineer/infrastructure/secrets-management-plan/SKILL.md](skills/07-devops-sre/devops-engineer/infrastructure/secrets-management-plan/SKILL.md)

**Review cloud cost** · `finops-review`

- When: Reviews cloud or platform spend to find waste, rightsizing opportunities, commitment and pricing-model options, storage and data-transfer savings, and tagging/allocation gaps, and returns a prioritized savings backlog with effort and risk. Use when a cost report, bill export or resource inventory is shared, costs grew unexpectedly, or a periodic cost review is due.
- Try: _"Here is our last three months of cloud cost by service and resource group. Where are we wasting money and what should we do first?"_
- Related: `cloud-cost-estimate`, `capacity-planning`, `iac-review`, `environment-strategy`, `budget-proposal`
- File: [skills/07-devops-sre/devops-engineer/infrastructure/finops-review/SKILL.md](skills/07-devops-sre/devops-engineer/infrastructure/finops-review/SKILL.md)

### Release Manager

#### Release Management

**Write a release plan** · `release-plan`

- When: Writes a release plan that fixes the release contents, schedule with freeze and cut-over points, named owners, dependencies, communication and the rollback decision point. Use when a release spans several teams, components or environments, needs a change window, or when someone asks for a release schedule, cut-over plan or release runbook overview.
- Try: _"Write a release plan for version 4.2: three services, a database migration and a mobile app update, target production date next Thursday night."_
- Related: `deployment-checklist`, `rollback-plan`, `go-no-go`, `release-notes`, `change-request-rfc`
- File: [skills/07-devops-sre/release-manager/release/release-plan/SKILL.md](skills/07-devops-sre/release-manager/release/release-plan/SKILL.md)

**Write release notes** · `release-notes`

- When: Writes release notes from a change list, commits or work items, grouped into new features, improvements, fixes, breaking changes, deprecations and known issues, and written for a named audience (end users, administrators, API consumers or internal teams). Use when a version is about to ship and users, customers or support need to know what changed and what they must do.
- Try: _"Turn this list of 23 merged tickets into release notes for our customers' administrators for version 3.8."_
- Related: `changelog-entry`, `semantic-versioning`, `release-announcement`, `app-store-release-notes`, `release-plan`
- File: [skills/07-devops-sre/release-manager/release/release-notes/SKILL.md](skills/07-devops-sre/release-manager/release/release-notes/SKILL.md)

**Build a deployment checklist** · `deployment-checklist`

- When: Builds a deployment checklist with pre-deployment, execution and post-deployment checks, each with an owner, expected result and a stop condition, tailored to the system's components, data changes and deployment mechanism. Use when a production deployment is scheduled, when deployments keep failing on forgotten steps, or when someone asks for a cut-over or deployment-day checklist.
- Try: _"Create a deployment checklist for tonight's release: two API services on Kubernetes, one SQL migration, a config change in the gateway."_
- Related: `release-plan`, `rollback-plan`, `go-no-go`, `runbook`, `deployment-strategy`
- File: [skills/07-devops-sre/release-manager/release/deployment-checklist/SKILL.md](skills/07-devops-sre/release-manager/release/deployment-checklist/SKILL.md)

**Write a rollback plan** · `rollback-plan`

- When: Writes a rollback plan for a release or change with measurable triggers, decision owner and deadline, component-by-component steps, data and schema considerations, roll-forward alternatives and post-rollback verification. Use before a production change is approved, when a change includes migrations or irreversible steps, or when someone asks how a release would be undone.
- Try: _"Write a rollback plan for our release that upgrades the order service and migrates the order status column from text to an enum table."_
- Related: `deployment-checklist`, `release-plan`, `deployment-strategy`, `schema-migration-plan`, `backup-restore-plan`
- File: [skills/07-devops-sre/release-manager/release/rollback-plan/SKILL.md](skills/07-devops-sre/release-manager/release/rollback-plan/SKILL.md)

**Run a go/no-go decision** · `go-no-go`

- When: Prepares and records a go/no-go decision for a release or cut-over: agreed criteria, evidence per criterion, open risks with owners, conditions for a conditional go, and a decision record with approvers. Use when a release, migration or launch needs a formal decision, when someone asks for a go/no-go meeting pack or checklist, or when the team must document why it shipped or postponed.
- Try: _"Prepare the go/no-go for tomorrow's CRM migration cut-over. Here are the test results, open defects and the rehearsal notes."_
- Related: `release-quality-gate`, `release-plan`, `rollback-plan`, `decision-log`, `test-summary-report`
- File: [skills/07-devops-sre/release-manager/release/go-no-go/SKILL.md](skills/07-devops-sre/release-manager/release/go-no-go/SKILL.md)

**Decide a version number** · `semantic-versioning`

- When: Decides the next version number by applying Semantic Versioning 2.0.0 to a list of changes: classifies each change against the public API, detects hidden breaking changes, and handles 0.x, pre-release and build metadata. Use when a library, API, SDK, package or service is about to be released and someone asks which version it should be, or whether a change requires a major bump.
- Try: _"Current version is 2.4.1. Changes: added optional 'locale' parameter, renamed error code INVALID_TOKEN to TOKEN_INVALID, fixed rounding bug. What is the next version?"_
- Related: `release-notes`, `changelog-entry`, `api-deprecation-plan`, `api-design-review`, `release-plan`
- File: [skills/07-devops-sre/release-manager/release/semantic-versioning/SKILL.md](skills/07-devops-sre/release-manager/release/semantic-versioning/SKILL.md)

### Site Reliability Engineer

#### Reliability

**Define SLIs and SLOs** · `slo-definition`

- When: Defines user-centric SLIs and SLOs for a service: identifies critical user journeys, chooses indicator types (availability, latency, freshness, correctness, throughput), specifies exact good/valid event definitions and measurement points, and sets targets and compliance windows with the resulting error budget. Use when a service needs reliability targets, when alerts are noisy or unrelated to user pain, or when someone asks what an SLO should be.
- Try: _"Define SLIs and SLOs for our checkout API. We have load balancer logs and Prometheus metrics; business says checkout must 'always work'."_
- Related: `error-budget-policy`, `alert-design`, `observability-plan`, `nfr-specification`, `kpi-definition`
- File: [skills/07-devops-sre/sre/reliability/slo-definition/SKILL.md](skills/07-devops-sre/sre/reliability/slo-definition/SKILL.md)

**Write an error budget policy** · `error-budget-policy`

- When: Writes an error budget policy that states, for defined budget consumption thresholds, what the development and operations teams must do (release restrictions, reliability work, postmortem requirements), who decides exceptions, and how disputes are escalated. Use when SLOs exist but have no consequences, when feature pressure keeps overriding reliability, or when someone asks what happens when the error budget is exhausted.
- Try: _"Our checkout SLO is 99.9% over 28 days and we burned 80% of the budget in the first week. Write an error budget policy that the product and engineering leads can sign."_
- Related: `slo-definition`, `alert-design`, `postmortem`, `release-quality-gate`, `go-no-go`
- File: [skills/07-devops-sre/sre/reliability/error-budget-policy/SKILL.md](skills/07-devops-sre/sre/reliability/error-budget-policy/SKILL.md)

**Design alerts** · `alert-design`

- When: Designs a paging and ticketing alert set for a service: symptom-based alerts tied to SLOs, multi-window multi-burn-rate conditions, severity and routing, runbook links and an audit of existing noisy alerts. Use when alerts are missing, noisy, cause-based (CPU, disk) instead of user-impacting, when on-call is burning out, or when new SLOs need alerting.
- Try: _"Design alerts for our payments API. SLO is 99.9% availability over 28 days; today we page on CPU > 80% and get 40 pages a week."_
- Related: `slo-definition`, `error-budget-policy`, `observability-plan`, `runbook`, `incident-response`
- File: [skills/07-devops-sre/sre/reliability/alert-design/SKILL.md](skills/07-devops-sre/sre/reliability/alert-design/SKILL.md)

**Plan observability** · `observability-plan`

- When: Plans observability for one or more services: which metrics, structured logs and distributed traces to emit, correlation and context propagation, cardinality and retention budgets, dashboards per audience and gaps against SLOs and runbooks. Use when a service is being built or onboarded, when incidents take long to diagnose, when telemetry cost is out of control, or when someone asks what to instrument.
- Try: _"Plan observability for our order service: .NET API, Kafka consumer, PostgreSQL. We only have container CPU/memory graphs and unstructured logs today."_
- Related: `slo-definition`, `alert-design`, `logging-instrumentation`, `dashboard-spec`, `runbook`
- File: [skills/07-devops-sre/sre/reliability/observability-plan/SKILL.md](skills/07-devops-sre/sre/reliability/observability-plan/SKILL.md)

**Plan capacity** · `capacity-planning`

- When: Produces a capacity plan for a service or platform: demand forecast from organic growth and known events, per-resource saturation limits from load tests or production data, required capacity with headroom and N+1 redundancy, lead times, scaling triggers and cost impact. Use when a launch, campaign or seasonal peak is coming, when utilization trends toward limits, or when budgeting infrastructure for the next period.
- Try: _"Plan capacity for our checkout for Black Friday. Normal peak is 800 req/s, marketing expects 4x traffic; we run 12 pods and one primary database."_
- Related: `capacity-test-report`, `load-test-analysis`, `scalability-review`, `finops-review`, `observability-plan`
- File: [skills/07-devops-sre/sre/reliability/capacity-planning/SKILL.md](skills/07-devops-sre/sre/reliability/capacity-planning/SKILL.md)

**Design a chaos experiment** · `chaos-experiment`

- When: Designs a controlled chaos experiment: steady-state definition, falsifiable hypothesis, fault to inject, blast radius and progressive scope, abort conditions and rollback, observation plan, prerequisites and a findings record. Use when a team wants to verify resilience claims (failover, retries, timeouts, autoscaling), prepare for a game day, or validate a disaster recovery or degradation design before relying on it.
- Try: _"Design a chaos experiment to check that our order service survives losing one of three Redis replicas without customer-visible errors."_
- Related: `resilience-review`, `dr-plan`, `slo-definition`, `runbook`, `observability-plan`
- File: [skills/07-devops-sre/sre/reliability/chaos-experiment/SKILL.md](skills/07-devops-sre/sre/reliability/chaos-experiment/SKILL.md)

**Write a disaster recovery plan** · `dr-plan`

- When: Writes a disaster recovery plan for a system: business-driven RTO/RPO per service tier, disaster scenarios, recovery strategy and dependency order, step-by-step failover and failback procedures, roles and declaration authority, communication and a test schedule with evidence. Use when a system lacks a DR plan, when RTO/RPO targets must be set or verified, before an audit, or after a DR test or incident revealed gaps.
- Try: _"Write a DR plan for our core banking API and its PostgreSQL database. Business wants RTO 1 hour and RPO 5 minutes; we run in one region with nightly backups."_
- Related: `backup-restore-plan`, `runbook`, `chaos-experiment`, `incident-communication`, `resilience-review`
- File: [skills/07-devops-sre/sre/reliability/dr-plan/SKILL.md](skills/07-devops-sre/sre/reliability/dr-plan/SKILL.md)

#### Incident Management

**Write a runbook** · `runbook`

- When: Writes an operational runbook for one alert or failure mode: symptoms and impact, fast triage, diagnosis branches with exact checks and expected results, safe remediation steps with verification and rollback, escalation and follow-up. Use when a paging alert has no runbook, when on-call relies on tribal knowledge, after an incident showed a missing procedure, or when someone asks how to handle a recurring operational problem.
- Try: _"Write a runbook for the alert OrderQueueLagHigh: Kafka consumer lag above 10k for 10 minutes on the order-events topic."_
- Related: `alert-design`, `incident-response`, `known-error-article`, `postmortem`, `observability-plan`
- File: [skills/07-devops-sre/sre/incident/runbook/SKILL.md](skills/07-devops-sre/sre/incident/runbook/SKILL.md)

**Run incident response** · `incident-response`

- When: Guides a live incident from declaration to resolution: severity assessment, role assignment (incident commander, operations, communications, scribe), a mitigation-first plan with hypotheses and parallel workstreams, a timestamped timeline, update cadence and exit criteria. Use when an outage or degradation is happening or suspected, when someone asks what to do right now about production impact, or to structure an ongoing incident channel.
- Try: _"We have an incident: checkout error rate jumped to 15% ten minutes after the 14:05 deploy. Help me run it."_
- Related: `runbook`, `incident-communication`, `postmortem`, `log-analysis`, `security-incident-response`
- File: [skills/07-devops-sre/sre/incident/incident-response/SKILL.md](skills/07-devops-sre/sre/incident/incident-response/SKILL.md)

**Write incident communications** · `incident-communication`

- When: Writes incident communications for each phase (investigating, identified, monitoring, resolved) and audience: internal stakeholder updates, executive summaries and public status-page posts, with confirmed impact, customer actions, next update time and no speculation on cause. Use during or right after an incident when an update, status-page entry, customer notice or leadership briefing must be written or reviewed.
- Try: _"Write the first status-page update and an internal Slack update: payments failing for about 20% of EU customers since 09:40, cause unknown, team investigating."_
- Related: `incident-response`, `customer-outage-notice`, `postmortem`, `bad-news-delivery`, `status-update`
- File: [skills/07-devops-sre/sre/incident/incident-communication/SKILL.md](skills/07-devops-sre/sre/incident/incident-communication/SKILL.md)

**Write a blameless postmortem** · `postmortem`

- When: Writes a blameless postmortem from incident notes, chat logs, alerts and timelines: summary, customer and business impact, a timestamped timeline, detection and response analysis, contributing factors and root causes traced beyond the trigger, what went well, and prioritized corrective actions with owners and due dates. Use after an incident is resolved, when an SLO breach or near miss needs a formal review, or when a draft postmortem must be made blameless and actionable.
- Try: _"Here are the chat log and alert history of last night's payment outage. Write a blameless postmortem with timeline, root causes and action items."_
- Related: `incident-response`, `incident-communication`, `runbook`, `error-budget-policy`, `alert-design`
- File: [skills/07-devops-sre/sre/incident/postmortem/SKILL.md](skills/07-devops-sre/sre/incident/postmortem/SKILL.md)

**Write an on-call handover** · `on-call-handover`

- When: Writes an on-call handover for the incoming engineer from the outgoing shift's notes, alerts, incidents and change calendar: open incidents and their state, recent and upcoming changes, known risks and degraded components, noisy or silenced alerts, pending follow-ups with owners, and explicit watch items with thresholds and first actions. Use at the end of an on-call shift or rotation, before a holiday or freeze period, or whenever responsibility for a production system passes between people or teams.
- Try: _"My on-call week ends tomorrow. Here are my notes, the alert summary and the change calendar. Write the handover for the next on-call engineer."_
- Related: `incident-response`, `runbook`, `postmortem`, `alert-design`, `incident-communication`
- File: [skills/07-devops-sre/sre/incident/on-call-handover/SKILL.md](skills/07-devops-sre/sre/incident/on-call-handover/SKILL.md)

## Data & AI

### Data Architect

#### Data Modeling

**Build a conceptual data model** · `conceptual-data-model`

- When: Builds a conceptual data model that names the core business entities, their definitions and relationships in business language, independent of any database technology. Use when starting a new domain, platform or integration, aligning stakeholders on vocabulary, or when asked for an entity map, subject-area model or business object model.
- Try: _"Create a conceptual data model for our B2B order-to-cash domain from these workshop notes."_
- Related: `logical-data-model`, `glossary-builder`, `bounded-context-map`, `event-storming`, `data-requirements`
- File: [skills/08-data/data-architect/modeling/conceptual-data-model/SKILL.md](skills/08-data/data-architect/modeling/conceptual-data-model/SKILL.md)

**Build a logical data model** · `logical-data-model`

- When: Turns a conceptual model or requirements into a normalized logical data model with entities, attributes, domains, primary/alternate/foreign keys, constraints and history handling, still independent of a specific database product. Use when preparing physical schema design, validating requirements against data, or when asked for an ERD, 3NF model or attribute-level model.
- Try: _"Derive a logical data model in 3NF from this conceptual model and the attached field list for the claims domain."_
- Related: `conceptual-data-model`, `database-schema-design`, `data-requirements`, `business-rules-catalog`, `data-classification`
- File: [skills/08-data/data-architect/modeling/logical-data-model/SKILL.md](skills/08-data/data-architect/modeling/logical-data-model/SKILL.md)

**Design a dimensional model** · `dimensional-model`

- When: Designs a dimensional (star/snowflake) model from business processes: declares the grain, fact tables and measure additivity, conformed dimensions, SCD type per attribute and handling of late-arriving and unknown members. Use when building a warehouse or lakehouse gold/mart layer, a semantic model for BI, or when asked for a star schema, bus matrix or fact/dimension design.
- Try: _"Design a star schema for retail sales and returns analysis; users need daily store/product KPIs and customer segment history."_
- Related: `metric-definition`, `dashboard-spec`, `report-requirements`, `data-vault-model`, `source-to-target-mapping`
- File: [skills/08-data/data-architect/modeling/dimensional-model/SKILL.md](skills/08-data/data-architect/modeling/dimensional-model/SKILL.md)

**Design a Data Vault model** · `data-vault-model`

- When: Designs a Data Vault 2.0 model: hubs from business keys, links for relationships and transactions, satellites split by source and rate of change, plus hash key, load date, record source and business vault constructs (PIT, bridge, effectivity). Use when building an auditable, source-integrated raw layer over many changing sources, or when asked for hubs, links and satellites.
- Try: _"Design a Data Vault for customer and contract data coming from CRM, core banking and a web onboarding app."_
- Related: `dimensional-model`, `logical-data-model`, `master-data-strategy`, `incremental-load-design`, `data-lineage-doc`
- File: [skills/08-data/data-architect/modeling/data-vault-model/SKILL.md](skills/08-data/data-architect/modeling/data-vault-model/SKILL.md)

**Design a data platform** · `data-platform-architecture`

- When: Designs a vendor-neutral data platform architecture: ingestion, storage and processing layers, serving patterns, governance, security, operating model and the choice between warehouse, lakehouse, mesh or hybrid, with decisions traced to requirements. Use when defining a target data platform, modernizing a legacy warehouse, or when asked for a lakehouse, data mesh or reference data architecture.
- Try: _"Design a target data platform for a manufacturer with SAP, MES and IoT sources, BI and ML consumers, and a small central data team."_
- Related: `target-state-architecture`, `technology-selection`, `adr`, `data-contract`, `cloud-cost-estimate`
- File: [skills/08-data/data-architect/modeling/data-platform-architecture/SKILL.md](skills/08-data/data-architect/modeling/data-platform-architecture/SKILL.md)

**Write a data contract** · `data-contract`

- When: Writes a data contract between a data producer and its consumers: schema, semantics, quality expectations, freshness and availability SLAs, ownership, access and privacy terms, versioning and change/deprecation rules, in a machine-readable-friendly form. Use when publishing a dataset, event stream or data product, onboarding a new consumer, or when asked to formalize producer-consumer expectations.
- Try: _"Write a data contract for the orders event stream that finance and the recommendation team consume."_
- Related: `schema-evolution-plan`, `data-quality-rules`, `api-contract`, `data-catalog-entry`, `data-classification`
- File: [skills/08-data/data-architect/modeling/data-contract/SKILL.md](skills/08-data/data-architect/modeling/data-contract/SKILL.md)

#### Data Governance

**Write a data catalog entry** · `data-catalog-entry`

- When: Writes a data catalog entry for a dataset, table, report or data product: business description, owner and steward, grain, key fields, lineage summary, quality status, freshness, sensitivity and access, and usage guidance. Use when registering or documenting a dataset for discovery, preparing it for self-service, or when asked to describe a table or data product for the catalog.
- Try: _"Write a catalog entry for the table sales.fact_invoice_line using this DDL and the notes from the finance team."_
- Related: `data-lineage-doc`, `data-classification`, `data-quality-rules`, `data-contract`, `glossary-builder`
- File: [skills/08-data/data-architect/governance/data-catalog-entry/SKILL.md](skills/08-data/data-architect/governance/data-catalog-entry/SKILL.md)

**Classify data sensitivity** · `data-classification`

- When: Classifies datasets and fields by sensitivity and privacy category: confidentiality level, personal data, special-category data under KVKK Article 6 and GDPR Articles 9-10, direct vs. indirect identifiers, and derives handling controls such as masking, encryption, access and retention. Use when onboarding data to a platform, preparing a DPIA or access model, or when asked to tag PII or sensitive columns.
- Try: _"Classify the columns of our customer and loan application tables for KVKK and propose masking rules."_
- Related: `privacy-impact-assessment`, `retention-policy`, `data-catalog-entry`, `access-review`, `secrets-management-plan`
- File: [skills/08-data/data-architect/governance/data-classification/SKILL.md](skills/08-data/data-architect/governance/data-classification/SKILL.md)

**Define data quality rules** · `data-quality-rules`

- When: Defines testable data quality rules for a dataset or data product across completeness, validity, uniqueness, consistency, referential integrity, timeliness and volume, each with a threshold, severity, on-failure action and owner. Use when a dataset needs quality checks, a data contract needs its quality section, recurring data issues must be prevented, or someone asks which checks to put on a table or pipeline.
- Try: _"Define data quality rules for the customer and orders tables that feed our monthly revenue report."_
- Related: `data-contract`, `data-catalog-entry`, `pipeline-spec`, `business-rules-catalog`, `pipeline-failure-analysis`
- File: [skills/08-data/data-architect/governance/data-quality-rules/SKILL.md](skills/08-data/data-architect/governance/data-quality-rules/SKILL.md)

**Document data lineage** · `data-lineage-doc`

- When: Documents data lineage from source systems through ingestion, transformations and storage layers to reports, models and other consumers, at dataset and critical-column level, with transformation logic, owners and verification status. Use when someone asks where a number comes from, for impact analysis before a change, for audit or regulatory traceability, or when onboarding people to an unfamiliar data flow.
- Try: _"Document the lineage of the 'net revenue' figure on the finance dashboard back to the source systems."_
- Related: `data-catalog-entry`, `source-to-target-mapping`, `impact-analysis`, `data-quality-rules`, `diagram-as-code`
- File: [skills/08-data/data-architect/governance/data-lineage-doc/SKILL.md](skills/08-data/data-architect/governance/data-lineage-doc/SKILL.md)

**Define master data management** · `master-data-strategy`

- When: Defines a master data management approach for one or more domains (customer, product, supplier, location, etc.): system of record per attribute, golden record and survivorship rules, match/merge logic, implementation style, stewardship roles and workflows, and data distribution to consuming systems. Use when the same entity exists inconsistently across systems, duplicates harm operations or reporting, or a master data or golden record initiative is being scoped.
- Try: _"Define a master data approach for customer data that exists in our CRM, ERP and e-commerce platform."_
- Related: `data-quality-rules`, `logical-data-model`, `data-lineage-doc`, `raci-matrix`, `data-classification`
- File: [skills/08-data/data-architect/governance/master-data-strategy/SKILL.md](skills/08-data/data-architect/governance/master-data-strategy/SKILL.md)

**Define data retention** · `retention-policy`

- When: Defines a data retention policy for datasets or systems: retention periods with their legal or business basis, trigger events, archival tiers, deletion or anonymization methods, legal holds, backup handling and evidence of deletion. Use when data is kept indefinitely by default, a privacy law such as KVKK or GDPR requires storage limitation, storage costs grow, or someone asks how long data may or must be kept.
- Try: _"Define a retention policy for our customer, order and application log data under KVKK and GDPR."_
- Related: `data-classification`, `privacy-impact-assessment`, `backup-restore-plan`, `policy-writing`, `data-catalog-entry`
- File: [skills/08-data/data-architect/governance/retention-policy/SKILL.md](skills/08-data/data-architect/governance/retention-policy/SKILL.md)

### Data Engineer

#### Data Pipelines

**Specify a data pipeline** · `pipeline-spec`

- When: Specifies a batch or streaming data pipeline end to end: sources and extraction, schedule or trigger, dependencies, transformation steps, targets and write mode, load strategy, data quality gates, SLAs, failure handling, backfill, observability, security and ownership. Use before building or changing a pipeline, when handing pipeline work to an engineer, or when someone asks to design or document an ETL/ELT or streaming job.
- Try: _"Write a pipeline spec for loading daily orders from the ERP database into the warehouse for the finance mart."_
- Related: `source-to-target-mapping`, `incremental-load-design`, `data-quality-rules`, `data-contract`, `runbook`
- File: [skills/08-data/data-engineer/pipelines/pipeline-spec/SKILL.md](skills/08-data/data-engineer/pipelines/pipeline-spec/SKILL.md)

**Write a source-to-target mapping** · `source-to-target-mapping`

- When: Writes a column-level source-to-target mapping (STTM) for a data load: target columns with type and nullability, source columns, transformation and business rules, lookups, defaults, key generation, filters, join conditions, rejects handling and test cases. Use when a pipeline, migration or integration load must be built or reviewed, when business rules for derived fields must be pinned down, or when someone asks for a mapping sheet between two schemas.
- Try: _"Create a source-to-target mapping from the CRM customer and address tables into our dim_customer table."_
- Related: `pipeline-spec`, `field-mapping`, `data-lineage-doc`, `dimensional-model`, `test-data-design`
- File: [skills/08-data/data-engineer/pipelines/source-to-target-mapping/SKILL.md](skills/08-data/data-engineer/pipelines/source-to-target-mapping/SKILL.md)

**Design incremental loads** · `incremental-load-design`

- When: Designs an incremental load for a table or stream: change detection method (log-based CDC, timestamp or sequence watermark, snapshot diff), watermark management, idempotent merge, delete propagation, late and out-of-order data handling, reconciliation and full-reload fallback. Use when full reloads become too slow or costly, a source must be replicated with low latency, or someone asks how to load only changed data safely.
- Try: _"Design an incremental load for a 400-million-row transactions table that currently takes 6 hours to reload fully."_
- Related: `pipeline-spec`, `source-to-target-mapping`, `data-vault-model`, `schema-evolution-plan`, `pipeline-failure-analysis`
- File: [skills/08-data/data-engineer/pipelines/incremental-load-design/SKILL.md](skills/08-data/data-engineer/pipelines/incremental-load-design/SKILL.md)

**Analyze a data pipeline failure** · `pipeline-failure-analysis`

- When: Analyzes a failed or silently wrong data pipeline run: reconstructs the timeline, isolates the root cause (source, code, infrastructure, data, dependency), quantifies the data impact on partitions, tables and consumers, and produces a safe, idempotent backfill and prevention plan. Use when a load failed, produced duplicates, missing or late data, a quality check tripped, or a consumer reports numbers that stopped matching.
- Try: _"Last night's orders load succeeded but today's revenue dashboard is 12% low. Here are the run logs and row counts; find out what happened and how to fix the data."_
- Related: `incremental-load-design`, `pipeline-spec`, `data-lineage-doc`, `data-quality-rules`, `postmortem`
- File: [skills/08-data/data-engineer/pipelines/pipeline-failure-analysis/SKILL.md](skills/08-data/data-engineer/pipelines/pipeline-failure-analysis/SKILL.md)

**Plan schema evolution** · `schema-evolution-plan`

- When: Plans a schema change in a data pipeline, event stream or shared dataset: classifies each change as backward, forward or fully compatible or breaking, picks the evolution pattern (additive, expand-contract, versioned dataset or topic, dual write), and sequences producer, pipeline and consumer changes with backfill, validation and deprecation. Use when a source adds, renames, retypes or removes fields, when a data contract must change, or when consumers keep breaking on upstream schema drift.
- Try: _"The CRM team will rename customer_type to segment and change it from free text to an enum next month. Plan the schema evolution for our pipeline and the 6 downstream consumers."_
- Related: `data-contract`, `schema-migration-plan`, `incremental-load-design`, `source-to-target-mapping`, `data-lineage-doc`
- File: [skills/08-data/data-engineer/pipelines/schema-evolution-plan/SKILL.md](skills/08-data/data-engineer/pipelines/schema-evolution-plan/SKILL.md)

### Database Administrator

#### Database Operations

**Optimize a slow query** · `query-optimization`

- When: Diagnoses a slow SQL query from its text, execution plan and statistics, finds the dominant cost (bad cardinality estimate, wrong join order or method, scans, spills, non-sargable predicates, parameter sensitivity, blocking) and proposes ranked rewrites, index or statistics changes with expected effect and verification. Use when a query, report or endpoint is slow, a plan regressed after a release or data growth, or someone shares an execution plan and asks why it is slow.
- Try: _"This order search query went from 200 ms to 9 seconds after last week's data import. Here are the query and the actual execution plan; why is it slow and how do we fix it?"_
- Related: `index-recommendation`, `database-health-check`, `sql-query-writing`, `performance-optimization`, `schema-migration-plan`
- File: [skills/08-data/dba/database/query-optimization/SKILL.md](skills/08-data/dba/database/query-optimization/SKILL.md)

**Recommend indexes** · `index-recommendation`

- When: Recommends indexes for a table or database from its real workload: groups queries by access pattern, designs key column order, included columns, filtered/partial indexes, consolidates overlapping and removes unused indexes, and weighs read gains against write amplification, storage and maintenance cost. Use when designing indexes for a new schema or feature, reviewing an over-indexed or under-indexed table, or acting on missing-index suggestions from the engine.
- Try: _"Our orders table has 14 indexes, inserts are getting slow and some reports are still scanning. Here are the top 20 queries and index usage stats; recommend an index set."_
- Related: `query-optimization`, `database-health-check`, `schema-migration-plan`, `database-schema-design`, `capacity-planning`
- File: [skills/08-data/dba/database/index-recommendation/SKILL.md](skills/08-data/dba/database/index-recommendation/SKILL.md)

**Plan a schema migration** · `schema-migration-plan`

- When: Plans a database schema migration on a live system with zero or minimal downtime: assesses lock and rewrite behavior of each DDL, splits breaking changes into expand-migrate-contract steps aligned with application releases, designs batched backfills, and defines verification, rollback and the point of no return. Use when adding, renaming, retyping or dropping columns, tables, constraints or indexes on production databases, or when a migration script needs a safety review before release.
- Try: _"We need to split the customers.full_name column into first_name and last_name on a 90-million-row PostgreSQL table without downtime. Write the migration plan."_
- Related: `schema-evolution-plan`, `index-recommendation`, `backup-restore-plan`, `deployment-strategy`, `rollback-plan`
- File: [skills/08-data/dba/database/schema-migration-plan/SKILL.md](skills/08-data/dba/database/schema-migration-plan/SKILL.md)

**Plan backup and restore** · `backup-restore-plan`

- When: Designs a database backup and restore plan derived from RPO and RTO: backup types and frequency (full, differential/incremental, log or continuous archiving, snapshots), retention and immutable/off-site copies, encryption and access, restore procedures for each failure scenario, and a scheduled restore-test program with evidence. Use when setting up or reviewing backups for a database, after a failed or slow restore, for audit evidence, or when RPO/RTO targets change.
- Try: _"Design a backup and restore plan for our 2 TB order database: RPO 15 minutes, RTO 2 hours, we must also keep monthly backups for 1 year for audit."_
- Related: `dr-plan`, `retention-policy`, `database-health-check`, `schema-migration-plan`, `runbook`
- File: [skills/08-data/dba/database/backup-restore-plan/SKILL.md](skills/08-data/dba/database/backup-restore-plan/SKILL.md)

**Run a database health check** · `database-health-check`

- When: Runs a structured health check of a database instance from the metrics, views and settings the user provides: wait profile, top resource-consuming queries, locking and blocking, storage growth and bloat/fragmentation, index and statistics health, configuration, replication, backups and security basics, then prioritizes findings with evidence and fixes. Use for periodic database reviews, before peak season or a migration, when a database feels slow overall, or when taking over an unfamiliar database.
- Try: _"Do a health check of our production SQL database. I pasted the top waits, the top 10 queries by CPU, file sizes and the configuration settings."_
- Related: `query-optimization`, `index-recommendation`, `backup-restore-plan`, `capacity-planning`, `alert-design`
- File: [skills/08-data/dba/database/database-health-check/SKILL.md](skills/08-data/dba/database/database-health-check/SKILL.md)

### Data / BI Analyst

#### Analytics & Reporting

**Write an analysis plan** · `analysis-plan`

- When: Writes an analysis plan that fixes the business question, hypotheses, data sources, method, validity checks and deliverable before any query is run. Use when a stakeholder asks \"why did X change\", \"does Y work\" or \"should we do Z\" and the analysis needs scope, method and expectations agreed up front.
- Try: _"Write an analysis plan for this question: marketing wants to know whether the new onboarding email series improved 30-day retention."_
- Related: `metric-definition`, `data-exploration`, `ab-test-analysis`, `insight-summary`, `hypothesis-statement`
- File: [skills/08-data/data-analyst/analytics/analysis-plan/SKILL.md](skills/08-data/data-analyst/analytics/analysis-plan/SKILL.md)

**Specify a dashboard** · `dashboard-spec`

- When: Specifies a dashboard before it is built - audience, decisions it supports, questions, KPIs with definitions, visuals, filters, drill paths, refresh and access rules. Use when someone asks for a new dashboard or report page, wants to rebuild a cluttered one, or needs a spec a BI developer can implement without guessing.
- Try: _"Specify a dashboard for the customer support leadership to track ticket backlog, SLA compliance and agent workload weekly."_
- Related: `metric-definition`, `kpi-definition`, `report-requirements`, `data-requirements`, `insight-summary`
- File: [skills/08-data/data-analyst/analytics/dashboard-spec/SKILL.md](skills/08-data/data-analyst/analytics/dashboard-spec/SKILL.md)

**Write an insight summary** · `insight-summary`

- When: Turns analysis results, query outputs or charts into a short \"so what\" insight summary - headline finding, evidence, confidence, implications and a recommended action. Use when numbers are available but the audience needs to know what they mean and what to do, e.g. after an analysis, a monthly review or a dashboard anomaly.
- Try: _"Write an insight summary from these results: churn rose from 3.1% to 4.0% in Q3, mostly in the SMB segment on monthly plans."_
- Related: `analysis-plan`, `executive-summary`, `ab-test-analysis`, `dashboard-spec`, `presentation-outline`
- File: [skills/08-data/data-analyst/analytics/insight-summary/SKILL.md](skills/08-data/data-analyst/analytics/insight-summary/SKILL.md)

**Define a metric precisely** · `metric-definition`

- When: Defines a business metric precisely enough that two analysts would compute the same number - purpose, formula, numerator/denominator, filters, grain, time logic, edge cases, source fields and owner. Use when a metric is disputed, reported differently across teams, about to be added to a dashboard or OKR, or needs to be documented in a metrics catalog.
- Try: _"Define \"active customer\" precisely; finance and product report different numbers every month."_
- Related: `kpi-definition`, `dashboard-spec`, `north-star-metric`, `data-quality-rules`, `glossary-builder`
- File: [skills/08-data/data-analyst/analytics/metric-definition/SKILL.md](skills/08-data/data-analyst/analytics/metric-definition/SKILL.md)

**Explore a dataset** · `data-exploration`

- When: Guides a structured exploratory data analysis of an unfamiliar dataset - structure, grain, distributions, nulls, duplicates, outliers, time coverage, relationships and quality issues - and reports findings and fitness for use. Use when a new table, extract or file arrives, before building a model, metric or dashboard on it, or when someone asks \"what is in this data?\".
- Try: _"Explore this dataset: a CSV of 250k e-commerce orders with columns order_id, customer_id, order_ts, amount, currency, status, channel. Here is the profile output."_
- Related: `analysis-plan`, `data-quality-rules`, `metric-definition`, `feature-engineering-plan`, `data-catalog-entry`
- File: [skills/08-data/data-analyst/analytics/data-exploration/SKILL.md](skills/08-data/data-analyst/analytics/data-exploration/SKILL.md)

**Analyze an A/B test** · `ab-test-analysis`

- When: Analyzes an A/B or multivariate test end to end - validity checks (sample ratio mismatch, exposure, duration), primary metric effect with confidence interval, guardrail metrics, segments and a ship / iterate / stop recommendation. Use when experiment results are in and a decision is needed, or when someone asks whether a test result is significant or trustworthy.
- Try: _"Analyze this A/B test: control 48,210 users 2.31% conversion, variant 48,950 users 2.52% conversion, ran 14 days; guardrail is refund rate."_
- Related: `experiment-design`, `hypothesis-statement`, `metric-definition`, `insight-summary`, `analysis-plan`
- File: [skills/08-data/data-analyst/analytics/ab-test-analysis/SKILL.md](skills/08-data/data-analyst/analytics/ab-test-analysis/SKILL.md)

### Data Scientist / ML & AI Engineer

#### Machine Learning

**Frame an ML problem** · `ml-problem-framing`

- When: Frames a business need as a machine learning problem - decision supported, prediction target and label, unit and timing of prediction, features available at prediction time, success metrics (offline and business), baseline, data feasibility and go/no-go. Use when someone proposes \"let's use ML/AI to predict X\", before any data work or model selection starts.
- Try: _"Frame this as an ML problem: the collections team wants to predict which customers will not pay their invoice on time so they can call them earlier."_
- Related: `ai-use-case-assessment`, `feature-engineering-plan`, `model-evaluation-report`, `analysis-plan`, `problem-statement`
- File: [skills/08-data/ml-ai-engineer/ml/ml-problem-framing/SKILL.md](skills/08-data/ml-ai-engineer/ml/ml-problem-framing/SKILL.md)

**Plan feature engineering** · `feature-engineering-plan`

- When: Plans the features for a predictive model - candidate features by hypothesis, source and availability at prediction time, point-in-time correctness, leakage checks, transformations, encoding, missing-value strategy and validation approach. Use after the ML problem is framed and before model training, or when a model performs suspiciously well and leakage is suspected.
- Try: _"Plan feature engineering for a churn model on a telecom subscription base; prediction is made monthly for the next 60 days."_
- Related: `ml-problem-framing`, `data-exploration`, `model-evaluation-report`, `source-to-target-mapping`, `data-quality-rules`
- File: [skills/08-data/ml-ai-engineer/ml/feature-engineering-plan/SKILL.md](skills/08-data/ml-ai-engineer/ml/feature-engineering-plan/SKILL.md)

**Write a model evaluation report** · `model-evaluation-report`

- When: Writes a model evaluation report that compares a candidate model against baseline and incumbent - overall metrics with uncertainty, threshold choice, calibration, slice performance, error analysis, fairness and a release recommendation. Use when a model is trained and must be approved for deployment, compared with alternatives, or reviewed after a performance complaint.
- Try: _"Write a model evaluation report for our fraud model v3 vs v2; here are the test-set metrics, confusion matrices and slice results by channel and country."_
- Related: `ml-problem-framing`, `model-card`, `ml-monitoring-plan`, `feature-engineering-plan`, `llm-eval-set`
- File: [skills/08-data/ml-ai-engineer/ml/model-evaluation-report/SKILL.md](skills/08-data/ml-ai-engineer/ml/model-evaluation-report/SKILL.md)

**Write a model card** · `model-card`

- When: Writes a model card documenting a trained model's intended use, out-of-scope uses, training and evaluation data, performance overall and by group, limitations, ethical and privacy considerations, and ownership. Use when a model is released, shared across teams, submitted for governance or audit review, or when users need to know what a model can and cannot be trusted for.
- Try: _"Write a model card for our CV screening ranking model used by HR recruiters; evaluation results and training data summary attached."_
- Related: `model-evaluation-report`, `ml-monitoring-plan`, `ml-problem-framing`, `privacy-impact-assessment`, `ai-use-case-assessment`
- File: [skills/08-data/ml-ai-engineer/ml/model-card/SKILL.md](skills/08-data/ml-ai-engineer/ml/model-card/SKILL.md)

**Plan model monitoring** · `ml-monitoring-plan`

- When: Produces a production monitoring plan for a machine learning model covering data and prediction drift, performance decay with delayed labels, data quality, operational health, alert thresholds, owners and retraining triggers. Use when a model is about to go live, after an incident caused by silent model degradation, or when someone asks how to know if a model is still working.
- Try: _"Write a monitoring plan for our churn model; it scores all customers nightly and we only learn true churn 60 days later."_
- Related: `model-evaluation-report`, `model-card`, `alert-design`, `observability-plan`, `feature-engineering-plan`
- File: [skills/08-data/ml-ai-engineer/ml/ml-monitoring-plan/SKILL.md](skills/08-data/ml-ai-engineer/ml/ml-monitoring-plan/SKILL.md)

#### Generative AI

**Design a prompt** · `prompt-design`

- When: Designs or rewrites a production prompt for a language-model feature with role, task, context, constraints, examples, output format and failure handling, plus a small test set to verify it. Use when building a new LLM-powered feature, when an existing prompt gives inconsistent, verbose or wrongly formatted answers, or when someone asks to improve, structure or harden a prompt.
- Try: _"Design a prompt that classifies incoming support emails into 8 categories and returns JSON with category, confidence and a one-line reason."_
- Related: `llm-eval-set`, `rag-design`, `ai-skill-authoring`, `ai-use-case-assessment`
- File: [skills/08-data/ml-ai-engineer/genai/prompt-design/SKILL.md](skills/08-data/ml-ai-engineer/genai/prompt-design/SKILL.md)

**Build an LLM evaluation set** · `llm-eval-set`

- When: Builds an evaluation set for an LLM feature with categorized test cases, scoring rubrics, grader choice (exact match, programmatic, model-graded, human), pass thresholds and a regression process. Use when an LLM feature, prompt or RAG pipeline needs measurable quality before release, when comparing models or prompt versions, or when someone says \"we don't know if the new prompt is better\".
- Try: _"Build an evaluation set for our contract-summary assistant so we can compare two prompt versions before release."_
- Related: `prompt-design`, `rag-design`, `model-evaluation-report`, `test-strategy`, `ai-use-case-assessment`
- File: [skills/08-data/ml-ai-engineer/genai/llm-eval-set/SKILL.md](skills/08-data/ml-ai-engineer/genai/llm-eval-set/SKILL.md)

**Design a RAG system** · `rag-design`

- When: Designs a retrieval-augmented generation (RAG) system covering corpus and access control, ingestion, chunking, embedding, hybrid retrieval, reranking, grounded answer generation with citations, evaluation and operations. Use when an LLM must answer from company documents or data, when an existing RAG gives wrong or uncited answers, or when choosing between RAG, fine-tuning and plain prompting.
- Try: _"Design a RAG assistant that answers employee questions from 3,000 HR policy PDFs and intranet pages, respecting country-specific access."_
- Related: `prompt-design`, `llm-eval-set`, `ai-use-case-assessment`, `data-classification`, `solution-architecture-document`
- File: [skills/08-data/ml-ai-engineer/genai/rag-design/SKILL.md](skills/08-data/ml-ai-engineer/genai/rag-design/SKILL.md)

**Author a new AI skill** · `ai-skill-authoring`

- When: Writes a new portable, bilingual skill (SKILL.md in English and SKILL.tr.md in Turkish) that follows this library's authoring guide, including catalog line, three-field frontmatter, the nine fixed sections, structural limits and content rules. Use when someone wants to add a skill to the library, turn a repeatable task or checklist into a skill, or review a draft skill for conformance.
- Try: _"Write a new skill for our library that helps a support engineer write a customer outage notice; give me the catalog line and both language files."_
- Related: `prompt-design`, `llm-eval-set`, `document-review`, `technical-translation`, `style-guide-check`
- File: [skills/08-data/ml-ai-engineer/genai/ai-skill-authoring/SKILL.md](skills/08-data/ml-ai-engineer/genai/ai-skill-authoring/SKILL.md)

**Assess an AI use case** · `ai-use-case-assessment`

- When: Assesses a proposed AI or machine learning use case on business value, technical feasibility, data readiness, risk (privacy, fairness, safety, regulatory) and operating cost, and gives a scored go / pilot / no-go recommendation with the smallest next experiment. Use when someone proposes \"let's use AI for X\", when prioritizing a portfolio of AI ideas, or before funding an AI pilot.
- Try: _"Assess this idea: use an LLM to draft first replies to all incoming customer complaints for our call center agents."_
- Related: `ml-problem-framing`, `rag-design`, `privacy-impact-assessment`, `cost-benefit-analysis`, `decision-matrix`
- File: [skills/08-data/ml-ai-engineer/genai/ai-use-case-assessment/SKILL.md](skills/08-data/ml-ai-engineer/genai/ai-use-case-assessment/SKILL.md)

## Security & Compliance

### Security Architect / AppSec Engineer

#### Secure Design

**Build a threat model** · `threat-model`

- When: Builds a threat model for a system or feature by decomposing it into a data flow diagram, applying STRIDE per element and trust boundary, rating each threat and proposing mitigations with owners. Use when designing a new system, adding an integration, changing trust boundaries or data flows, or when someone asks what could go wrong security-wise.
- Try: _"Build a threat model for our new mobile banking API: mobile app, API gateway, .NET backend, PostgreSQL and a third-party KYC provider."_
- Related: `security-requirements`, `authn-authz-design`, `solution-architecture-document`, `pentest-scope`, `it-risk-assessment`
- File: [skills/09-security/security-engineer/design/threat-model/SKILL.md](skills/09-security/security-engineer/design/threat-model/SKILL.md)

**Define security requirements** · `security-requirements`

- When: Defines testable security requirements for a system or feature, aligned to OWASP ASVS levels and chapters, with rationale, verification method and priority. Use when a new application or feature needs security acceptance criteria, when a threat model must be turned into backlog items, or when a customer or regulator asks for a security requirements baseline.
- Try: _"Define security requirements for our new customer self-service portal; it handles personal data and payments are done via a hosted payment page."_
- Related: `threat-model`, `nfr-specification`, `authn-authz-design`, `secure-code-review`, `acceptance-criteria`
- File: [skills/09-security/security-engineer/design/security-requirements/SKILL.md](skills/09-security/security-engineer/design/security-requirements/SKILL.md)

**Design authentication and authorization** · `authn-authz-design`

- When: Designs authentication and authorization for an application or API: identity provider and protocol choice (OIDC, OAuth 2.x, SAML), login and token flows, token lifetimes and storage, roles, claims or attributes, and least-privilege enforcement points. Use when building a new app or API, adding SSO or MFA, opening APIs to partners or machine clients, or redesigning a role model.
- Try: _"Design authentication and authorization for our B2B SaaS: web SPA, public REST API for partners, multi-tenant, customers want SSO with their own Entra ID or Okta."_
- Related: `security-requirements`, `threat-model`, `access-review`, `api-design-review`, `secrets-management-plan`
- File: [skills/09-security/security-engineer/design/authn-authz-design/SKILL.md](skills/09-security/security-engineer/design/authn-authz-design/SKILL.md)

#### Security Assessment

**Review code for security** · `secure-code-review`

- When: Reviews source code or a diff for security weaknesses, mapped to OWASP Top 10 categories and CWE IDs, tracing untrusted input from source to sink and giving severity, evidence and a concrete fix per finding. Use when a pull request touches authentication, authorization, input handling, crypto, file or network access, or when someone asks to check code for vulnerabilities.
- Try: _"Review this ASP.NET Core controller and its repository class for security issues before we merge."_
- Related: `code-review`, `security-finding-report`, `vulnerability-triage`, `security-requirements`, `threat-model`
- File: [skills/09-security/security-engineer/assessment/secure-code-review/SKILL.md](skills/09-security/security-engineer/assessment/secure-code-review/SKILL.md)

**Triage a vulnerability** · `vulnerability-triage`

- When: Triages a reported vulnerability (scanner result, bug bounty report, CVE advisory, pentest finding) by validating it, scoring it with CVSS, adjusting for exploitability (EPSS, known exploited status) and reachability in the actual environment, and producing a prioritized fix plan with SLA and owner. Use when a new vulnerability arrives and the team must decide how urgently to act.
- Try: _"Triage this: our scanner reports CVE in the XML parser used by our invoice import service, CVSS 9.8. How urgent is it for us?"_
- Related: `dependency-vulnerability-review`, `security-finding-report`, `security-incident-response`, `bug-triage`, `it-risk-assessment`
- File: [skills/09-security/security-engineer/assessment/vulnerability-triage/SKILL.md](skills/09-security/security-engineer/assessment/vulnerability-triage/SKILL.md)

**Review dependency vulnerabilities** · `dependency-vulnerability-review`

- When: Reviews software composition analysis (SCA) findings for third-party dependencies and container images, groups them by package, identifies direct versus transitive paths, proposes minimal safe upgrade paths, and documents risk acceptance for what cannot be fixed yet. Use when an SCA, SBOM or container scan report needs to become an actionable upgrade plan, or before a release gate on known vulnerable components.
- Try: _"Here is the SCA report for our Node.js API: 47 findings, 6 critical. Turn it into an upgrade plan and tell me what we can accept for now."_
- Related: `vulnerability-triage`, `dependency-upgrade`, `dockerfile-review`, `security-finding-report`, `release-quality-gate`
- File: [skills/09-security/security-engineer/assessment/dependency-vulnerability-review/SKILL.md](skills/09-security/security-engineer/assessment/dependency-vulnerability-review/SKILL.md)

**Define a penetration test scope** · `pentest-scope`

- When: Defines the scope and rules of engagement for an authorized penetration test: objectives, in-scope targets, exclusions, test type and depth, test windows, accounts and data, communication and stop conditions, legal authorization and reporting expectations. Use when commissioning an internal or external pentest, preparing a statement of work with a testing vendor, or planning a pre-release security test.
- Try: _"Define the pentest scope for our new customer portal and its public API before go-live; an external vendor will do a grey-box test."_
- Related: `threat-model`, `security-finding-report`, `vulnerability-triage`, `audit-preparation`, `statement-of-work`
- File: [skills/09-security/security-engineer/assessment/pentest-scope/SKILL.md](skills/09-security/security-engineer/assessment/pentest-scope/SKILL.md)

**Write a security finding** · `security-finding-report`

- When: Writes a clear, reproducible security finding with title, affected asset, severity and scoring, description, impact, reproduction steps, evidence, remediation and references, suitable for a pentest report, bug bounty response or internal tracker. Use when a confirmed or suspected security issue must be documented for developers, management or auditors.
- Try: _"Write a security finding for this: any logged-in user can download another user's invoice PDF by changing the invoice number in the URL."_
- Related: `vulnerability-triage`, `secure-code-review`, `pentest-scope`, `bug-report`, `security-incident-response`
- File: [skills/09-security/security-engineer/assessment/security-finding-report/SKILL.md](skills/09-security/security-engineer/assessment/security-finding-report/SKILL.md)

#### Security Operations

**Respond to a security incident** · `security-incident-response`

- When: Guides the response to a suspected or confirmed security incident through triage, containment, evidence preservation, eradication, recovery and notification, including KVKK and GDPR personal data breach duties, and produces an incident log and action plan. Use when there are signs of compromise, credential leakage, malware, data exfiltration or unauthorized access and the team needs a structured, defensive response.
- Try: _"We found an AWS access key of our CI user in a public GitHub repo and CloudTrail shows calls from an unknown IP. Help us respond."_
- Related: `incident-response`, `incident-communication`, `postmortem`, `vulnerability-triage`, `security-finding-report`
- File: [skills/09-security/security-engineer/operations/security-incident-response/SKILL.md](skills/09-security/security-engineer/operations/security-incident-response/SKILL.md)

**Run an access review** · `access-review`

- When: Runs a user access review (access recertification) for an application, database, cloud account or directory group: compares entitlements with HR and role data to detect excessive, orphaned, dormant, shared and toxic (separation-of-duties conflicting) permissions, and produces revoke/keep decisions with evidence for auditors. Use for periodic ISO 27001, SOC 2, SOX or BDDK access reviews, after reorganizations, or when privilege creep is suspected.
- Try: _"Here is the export of users and roles from our ERP and the HR active employee list. Run a quarterly access review and flag what should be revoked."_
- Related: `authn-authz-design`, `audit-preparation`, `control-mapping`, `it-risk-assessment`, `raci-matrix`
- File: [skills/09-security/security-engineer/operations/access-review/SKILL.md](skills/09-security/security-engineer/operations/access-review/SKILL.md)

### GRC / Compliance

#### Compliance

**Run a privacy impact assessment** · `privacy-impact-assessment`

- When: Runs a KVKK/GDPR data protection impact assessment (DPIA) for a feature or system: maps processing activities, legal bases, data flows and transfers, rates risks to data subjects and proposes privacy-by-design measures. Use when a new feature or system processes personal or special category data, introduces profiling, monitoring, new recipients or cross-border transfers, or when legal or the DPO asks for a DPIA.
- Try: _"Run a privacy impact assessment for our new customer loyalty app that tracks store visits by location and sends personalized offers."_
- Related: `data-classification`, `threat-model`, `retention-policy`, `security-requirements`, `it-risk-assessment`
- File: [skills/09-security/compliance/compliance/privacy-impact-assessment/SKILL.md](skills/09-security/compliance/compliance/privacy-impact-assessment/SKILL.md)

**Map controls to a standard** · `control-mapping`

- When: Maps an organization's existing controls, processes and evidence to a target standard such as ISO/IEC 27001 Annex A or SOC 2 Trust Services Criteria, and shows coverage, evidence gaps and overlaps with other frameworks. Use when preparing for certification, answering a customer security questionnaire, merging frameworks (ISO 27001, SOC 2, KVKK, PCI DSS) or checking whether a control actually produces audit evidence.
- Try: _"Map our current controls to ISO 27001:2022 Annex A and show which ones have no evidence."_
- Related: `audit-preparation`, `policy-writing`, `it-risk-assessment`, `access-review`, `traceability-matrix`
- File: [skills/09-security/compliance/compliance/control-mapping/SKILL.md](skills/09-security/compliance/compliance/control-mapping/SKILL.md)

**Write a security/IT policy** · `policy-writing`

- When: Writes or revises a security or IT policy with purpose, scope, enforceable rules, roles, exceptions, compliance measurement and review cycle, and separates policy from standards and procedures. Use when a policy is missing, outdated, flagged in an audit, or needed for ISO 27001, SOC 2, KVKK or internal governance (e.g. acceptable use, access control, password, backup, remote work, AI usage).
- Try: _"Write an access control policy for our company; we are preparing for ISO 27001 and use Entra ID and GitHub."_
- Related: `control-mapping`, `audit-preparation`, `it-risk-assessment`, `retention-policy`, `document-review`
- File: [skills/09-security/compliance/compliance/policy-writing/SKILL.md](skills/09-security/compliance/compliance/policy-writing/SKILL.md)

**Prepare for an audit** · `audit-preparation`

- When: Prepares a team for an internal, certification, customer or regulatory audit: confirms scope and criteria, builds an evidence request list with owners and due dates, runs a readiness gap check, and plans the audit week and auditee briefing. Use when an audit date is announced (ISO 27001, SOC 2, KVKK, PCI DSS, BDDK, customer audit), when an auditor sends a PBC/request list, or when previous findings must be closed before the next audit.
- Try: _"Our ISO 27001 surveillance audit is in six weeks. Prepare the evidence list, gaps and plan."_
- Related: `control-mapping`, `access-review`, `policy-writing`, `it-risk-assessment`, `schedule-plan`
- File: [skills/09-security/compliance/compliance/audit-preparation/SKILL.md](skills/09-security/compliance/compliance/audit-preparation/SKILL.md)

**Assess IT risk** · `it-risk-assessment`

- When: Assesses IT and information security risk for a scope of assets or services: identifies assets, threats and vulnerabilities, rates likelihood and impact with existing controls, decides treatment (mitigate, transfer, avoid, accept) and produces a risk register entry per risk. Use when building or refreshing an ISO 27001 risk assessment, evaluating a new vendor, system or change, preparing a risk acceptance, or when management asks how risky something is.
- Try: _"Assess IT risk for moving our on-prem ERP to a hosted cloud provider, including vendor and data risks."_
- Related: `threat-model`, `risk-register`, `control-mapping`, `vulnerability-triage`, `privacy-impact-assessment`
- File: [skills/09-security/compliance/compliance/it-risk-assessment/SKILL.md](skills/09-security/compliance/compliance/it-risk-assessment/SKILL.md)

## UX / UI Design

### UX Researcher

#### User Research

**Write a research plan** · `research-plan`

- When: Writes a user research plan with the decision it informs, research objectives and questions, method choice and rationale, participant criteria and sample, logistics, ethics and consent, timeline and deliverables. Use when a team wants to \"talk to users\", validate a concept, understand a behavior or evaluate a design, and before recruiting participants or booking sessions.
- Try: _"Write a research plan to understand why small business owners abandon our invoicing app during the first week."_
- Related: `screener-survey`, `usability-test-script`, `interview-question-set`, `research-synthesis`, `hypothesis-statement`
- File: [skills/10-design/ux-researcher/research/research-plan/SKILL.md](skills/10-design/ux-researcher/research/research-plan/SKILL.md)

**Write a usability test script** · `usability-test-script`

- When: Writes a moderated or unmoderated usability test script with intro and consent, warm-up, realistic task scenarios, neutral probes, observable success criteria, post-task and post-test measures and a debrief. Use when a prototype or live product must be tested with users, when someone asks for \"test tasks\" or a \"moderator guide\", or before a usability session is scheduled.
- Try: _"Write a usability test script for our new checkout prototype; we want to see if first-time buyers can apply a discount code and pay by card."_
- Related: `research-plan`, `screener-survey`, `research-synthesis`, `heuristic-evaluation`, `interview-question-set`
- File: [skills/10-design/ux-researcher/research/usability-test-script/SKILL.md](skills/10-design/ux-researcher/research/usability-test-script/SKILL.md)

**Synthesize research findings** · `research-synthesis`

- When: Synthesizes raw research data (interview notes, usability observations, open survey answers) into evidence-backed findings, insights and prioritized recommendations through affinity clustering, with frequency, severity and confidence for each. Use after interviews or usability sessions, when someone asks \"what did we learn\", or when notes must become a readout for a decision.
- Try: _"Synthesize these notes from 8 onboarding interviews into key insights and recommendations for the product team."_
- Related: `research-plan`, `usability-test-script`, `interview-notes-analysis`, `feedback-synthesis`, `customer-journey-map`
- File: [skills/10-design/ux-researcher/research/research-synthesis/SKILL.md](skills/10-design/ux-researcher/research/research-synthesis/SKILL.md)

**Write a participant screener** · `screener-survey`

- When: Writes a participant screener that recruits the right users for a study, with behavioral inclusion and exclusion criteria, non-leading questions that hide the qualifying answer, quotas per segment, disqualification logic and consent. Use before recruiting for interviews, usability tests or diary studies, or when someone asks \"who should we talk to\" or \"write a recruitment survey\".
- Try: _"Write a screener to recruit 8 small business owners who send invoices at least monthly and tried a competitor app in the last year."_
- Related: `research-plan`, `usability-test-script`, `questionnaire-design`, `persona`, `interview-question-set`
- File: [skills/10-design/ux-researcher/research/screener-survey/SKILL.md](skills/10-design/ux-researcher/research/screener-survey/SKILL.md)

### UX / UI Designer

#### Interaction & Visual Design

**Design a user flow** · `user-flow`

- When: Designs a user flow for one user goal, covering entry points, screens and steps, decision points, system actions, error and recovery paths, empty and edge states and exit points, as a step table plus a diagram-as-code flowchart. Use when a feature or journey must be designed screen by screen, when someone asks \"what are the steps\" or \"map the happy and unhappy paths\", or before wireframing.
- Try: _"Design the user flow for resetting a forgotten password in our mobile banking app, including errors and lockout."_
- Related: `customer-journey-map`, `wireframe-spec`, `information-architecture`, `edge-case-elicitation`, `diagram-as-code`
- File: [skills/10-design/ux-ui-designer/design/user-flow/SKILL.md](skills/10-design/ux-ui-designer/design/user-flow/SKILL.md)

**Structure information architecture** · `information-architecture`

- When: Structures the information architecture of a product or site, producing a content inventory, organization scheme, sitemap hierarchy, navigation model, labeling system and a card sort or tree test plan to validate it. Use when a product, portal or documentation site is being created or restructured, when users \"can't find things\", or when navigation and menu labels must be decided.
- Try: _"Restructure the navigation of our HR self-service portal; employees can't find leave, payroll and expense pages."_
- Related: `user-flow`, `wireframe-spec`, `docs-information-architecture`, `research-plan`, `persona`
- File: [skills/10-design/ux-ui-designer/design/information-architecture/SKILL.md](skills/10-design/ux-ui-designer/design/information-architecture/SKILL.md)

**Describe a wireframe** · `wireframe-spec`

- When: Describes a wireframe in text for one screen or view, covering purpose, layout regions, components, content priority, interactions, all states (default, loading, empty, error, partial, permission), responsive behavior and accessibility notes. Use when a screen must be defined before or instead of visual mockups, when someone asks \"what goes on this screen\", or when a wireframe must be reviewable by product and engineering in text.
- Try: _"Describe a wireframe for the order history screen of our e-commerce web app, including empty and error states."_
- Related: `user-flow`, `information-architecture`, `screen-requirements`, `design-handoff`, `microcopy`
- File: [skills/10-design/ux-ui-designer/design/wireframe-spec/SKILL.md](skills/10-design/ux-ui-designer/design/wireframe-spec/SKILL.md)

**Run a heuristic evaluation** · `heuristic-evaluation`

- When: Runs a heuristic evaluation of a product, flow or screens against Nielsen's 10 usability heuristics, producing located findings with the violated heuristic, evidence, a 0-4 severity rating and a concrete recommendation, plus a prioritized summary. Use when a quick expert usability review is needed before or instead of user testing, when someone asks \"what's wrong with this UI\", or to audit screenshots, prototypes or a live flow.
- Try: _"Do a heuristic evaluation of our expense submission flow; screenshots of the 4 screens are attached."_
- Related: `usability-test-script`, `accessibility-audit`, `design-critique`, `research-synthesis`, `user-flow`
- File: [skills/10-design/ux-ui-designer/design/heuristic-evaluation/SKILL.md](skills/10-design/ux-ui-designer/design/heuristic-evaluation/SKILL.md)

**Give design critique** · `design-critique`

- When: Gives structured design critique that is anchored in the design's goals, users and constraints, specific about location and effect, separates observations from opinions, and prioritizes feedback into must-fix, should-consider and nits with suggested directions. Use when a designer shares work in progress and asks for feedback, when preparing for a design review or crit session, or when someone asks \"what do you think of this design\".
- Try: _"Critique this dashboard redesign; the goal is to help ops managers spot failing stores within 10 seconds."_
- Related: `heuristic-evaluation`, `accessibility-audit`, `wireframe-spec`, `feedback-sbi`, `review-comment-writing`
- File: [skills/10-design/ux-ui-designer/design/design-critique/SKILL.md](skills/10-design/ux-ui-designer/design/design-critique/SKILL.md)

**Specify a design system component** · `design-system-component-spec`

- When: Specifies a reusable design system component with its purpose, anatomy, variants, sizes, states, design tokens, behavior, content rules, accessibility requirements, usage do's and don'ts, and API/props for implementation. Use when a new component is proposed for the design system, an existing one needs documentation or a breaking change, or teams are building divergent versions of the same pattern.
- Try: _"Write a design system spec for a Toast notification component that web and mobile teams can both implement."_
- Related: `design-handoff`, `wireframe-spec`, `component-design`, `accessibility-audit`, `microcopy`
- File: [skills/10-design/ux-ui-designer/design/design-system-component-spec/SKILL.md](skills/10-design/ux-ui-designer/design/design-system-component-spec/SKILL.md)

**Prepare a design handoff** · `design-handoff`

- When: Prepares a developer-ready design handoff for a screen, flow or feature, covering layout and spacing specs, design tokens, component mapping, interactions and motion, all edge states, responsive rules, accessibility annotations, content and assets, plus open decisions. Use when a design is approved and moves to implementation, when developers ask \"what exactly should this do\", or when a handoff note must accompany mockups or a design file.
- Try: _"Prepare a design handoff for the new checkout payment step so the web team can start building it next iteration."_
- Related: `wireframe-spec`, `design-system-component-spec`, `user-flow`, `microcopy`, `acceptance-criteria`
- File: [skills/10-design/ux-ui-designer/design/design-handoff/SKILL.md](skills/10-design/ux-ui-designer/design/design-handoff/SKILL.md)

### UX Writer / Content Designer

#### Content

**Write microcopy** · `microcopy`

- When: Writes interface microcopy such as button and link labels, form labels, helper text, placeholders, tooltips, empty states, confirmations and success messages, fitted to the user's task, the product's voice, length limits and localization. Use when a screen or flow needs its UI text written or improved, when labels are vague or inconsistent, or when someone asks \"what should this button say\".
- Try: _"Write the microcopy for our new \"invite teammates\" dialog: title, field labels, helper text, buttons and the empty state."_
- Related: `error-message-writing`, `voice-and-tone-guide`, `design-handoff`, `style-guide-check`, `glossary-builder`
- File: [skills/10-design/ux-writer/content/microcopy/SKILL.md](skills/10-design/ux-writer/content/microcopy/SKILL.md)

**Write error messages** · `error-message-writing`

- When: Writes user-facing error, validation and warning messages that say what happened, why if it helps, and what to do next, without blame, jargon or leaking internals, with the right placement, severity and accessibility behavior. Use when error states need copy, when existing messages are vague (\"Something went wrong\") or technical, or when an error catalog must be turned into user-facing text.
- Try: _"Rewrite these five payment error messages so users know what happened and what to do; the current ones just show API error codes."_
- Related: `microcopy`, `voice-and-tone-guide`, `error-scenario-catalog`, `error-handling-review`, `design-handoff`
- File: [skills/10-design/ux-writer/content/error-message-writing/SKILL.md](skills/10-design/ux-writer/content/error-message-writing/SKILL.md)

**Write a voice and tone guide** · `voice-and-tone-guide`

- When: Writes a product or brand voice and tone guide with 3-5 voice principles, each defined by what it is and is not, do/don't example pairs, a tone map that shifts by user context (success, error, onboarding, sensitive moments), grammar and terminology conventions, and a review checklist for writers. Use when a product lacks consistent UI writing, when several teams write copy differently, when entering a new language or market, or when an existing voice guide is too vague to apply.
- Try: _"Create a voice and tone guide for our B2B invoicing app in Turkish and English; our copy currently sounds different on every screen."_
- Related: `microcopy`, `error-message-writing`, `style-guide-check`, `positioning-statement`, `glossary-builder`
- File: [skills/10-design/ux-writer/content/voice-and-tone-guide/SKILL.md](skills/10-design/ux-writer/content/voice-and-tone-guide/SKILL.md)

## Support & IT Operations

### Support Engineer (L1-L3)

#### Ticket Handling

**Triage a support ticket** · `ticket-triage`

- When: Triages an incoming support ticket: classifies it (incident, service request, question, defect, security or privacy report), sets priority from impact and urgency, checks for duplicates or an ongoing outage, identifies missing information and routes it to the right queue or level. Use when a new ticket, email or chat request arrives in a support queue, when a backlog of unclassified tickets needs sorting, or when priority is disputed.
- Try: _"Triage this ticket: 'Since this morning none of our 40 branch users can print invoices from the POS, we are writing them by hand.'"_
- Related: `ticket-response`, `ticket-escalation-summary`, `known-error-article`, `incident-response`, `bug-report`
- File: [skills/11-support-ops/support-engineer/tickets/ticket-triage/SKILL.md](skills/11-support-ops/support-engineer/tickets/ticket-triage/SKILL.md)

**Write a ticket response** · `ticket-response`

- When: Writes a customer-facing reply to a support ticket that acknowledges the issue, states what is known, gives a clear answer or next step with ownership and timing, and asks only for the information that is needed. Use when replying to a new or updated ticket, following up on a pending ticket, delivering a resolution, declining a request, or rewriting a draft reply that is too technical, too long or defensive.
- Try: _"Write a reply to this customer: they cannot log in after the password reset, it is the second time this week and they are frustrated."_
- Related: `ticket-triage`, `ticket-escalation-summary`, `known-error-article`, `tone-rewrite`, `bad-news-delivery`
- File: [skills/11-support-ops/support-engineer/tickets/ticket-response/SKILL.md](skills/11-support-ops/support-engineer/tickets/ticket-response/SKILL.md)

**Summarize a ticket for escalation** · `ticket-escalation-summary`

- When: Condenses a support ticket and its history into an escalation summary for the next support level, engineering or a vendor: business impact, precise symptom, environment, timeline, what was tried with results, evidence and the exact ask. Use when a ticket must move from L1 to L2/L3, to a product team or to a third party, when a long ticket thread needs a handover note, or when a customer pushes for escalation.
- Try: _"Summarize this 30-message ticket for L3: users get 'session expired' every few minutes on the web portal since Tuesday; we cleared caches and reset passwords, no change."_
- Related: `ticket-triage`, `ticket-response`, `log-analysis`, `bug-report`, `problem-management`
- File: [skills/11-support-ops/support-engineer/tickets/ticket-escalation-summary/SKILL.md](skills/11-support-ops/support-engineer/tickets/ticket-escalation-summary/SKILL.md)

**Write a known error article** · `known-error-article`

- When: Writes a known error article for the support knowledge base: searchable symptom, scope and affected versions, confirmed or suspected cause, step-by-step workaround with risks, permanent fix status and linked records. Use when a problem has a documented root cause or workaround, when the same ticket keeps recurring, or when support agents need a consistent answer to give while a fix is pending.
- Try: _"Write a known error article: PDF export fails with 'Error 500' for reports over 10,000 rows since version 7.3; workaround is exporting to CSV; fix planned for 7.4."_
- Related: `problem-management`, `ticket-response`, `ticket-triage`, `how-to-guide`, `faq-builder`
- File: [skills/11-support-ops/support-engineer/tickets/known-error-article/SKILL.md](skills/11-support-ops/support-engineer/tickets/known-error-article/SKILL.md)

**Write a customer outage notice** · `customer-outage-notice`

- When: Writes customer-facing outage notices for each stage of a service disruption (investigating, identified, monitoring, resolved) and planned maintenance: plain-language impact, affected services and regions, status, workaround and next update time, without speculation or blame. Use when customers are affected by an outage or degradation, when a status page or email update is due, or when planned maintenance must be announced.
- Try: _"Write the first status page notice: payments via card fail for about 30% of customers in Turkey since 14:05, cause unknown, team investigating."_
- Related: `incident-communication`, `incident-response`, `ticket-response`, `postmortem`, `known-error-article`
- File: [skills/11-support-ops/support-engineer/tickets/customer-outage-notice/SKILL.md](skills/11-support-ops/support-engineer/tickets/customer-outage-notice/SKILL.md)

### IT Service Management

#### ITSM Processes

**Run problem management** · `problem-management`

- When: Runs problem management for recurring or major incidents: groups related incidents, frames the problem, drives evidence-based root cause analysis, records a known error with workaround, and proposes permanent fixes through change control with verification criteria. Use when the same incident type keeps recurring, after a major incident, when incident trends point to an underlying cause, or when a problem record must be opened, progressed or closed.
- Try: _"Open a problem record: we had 7 incidents in 3 weeks where the nightly batch overran and the morning reports were late; each was fixed by restarting the job."_
- Related: `known-error-article`, `five-whys`, `fishbone-analysis`, `change-request-rfc`, `postmortem`
- File: [skills/11-support-ops/it-service-management/itsm/problem-management/SKILL.md](skills/11-support-ops/it-service-management/itsm/problem-management/SKILL.md)

**Write a change request (RFC)** · `change-request-rfc`

- When: Writes an IT change request (RFC) ready for change approval or a change advisory board: reason, scope and affected configuration items, change type, risk and impact assessment, implementation plan, test evidence, backout plan with trigger, schedule, communication and verification. Use when a production change to infrastructure, applications, configuration or data needs approval, when a CAB submission is due, or when an emergency change must be documented.
- Try: _"Write an RFC to upgrade the production PostgreSQL cluster from 14 to 16 this Saturday night; 3 apps depend on it, we tested on staging last week."_
- Related: `rollback-plan`, `deployment-checklist`, `deployment-strategy`, `technical-risk-review`, `problem-management`
- File: [skills/11-support-ops/it-service-management/itsm/change-request-rfc/SKILL.md](skills/11-support-ops/it-service-management/itsm/change-request-rfc/SKILL.md)

**Analyze SLA breaches** · `sla-breach-analysis`

- When: Analyzes SLA breaches over a period: validates the data and clock rules, measures breach rates by priority, category, team, time and customer, finds patterns and root causes (process, capacity, routing, dependency, measurement), and proposes prioritized improvement actions with owners and target metrics. Use when SLA performance drops, before a service review or contract discussion, when penalties or credits are at stake, or when a team wants to know why tickets miss their targets.
- Try: _"Analyze last quarter's SLA breaches: P2 resolution target is 8 business hours, we met it for 71% against a 90% target; here is the ticket export."_
- Related: `problem-management`, `ticket-triage`, `slo-definition`, `kpi-definition`, `dashboard-spec`
- File: [skills/11-support-ops/it-service-management/itsm/sla-breach-analysis/SKILL.md](skills/11-support-ops/it-service-management/itsm/sla-breach-analysis/SKILL.md)

**Write a service catalog entry** · `service-catalog-entry`

- When: Writes a service catalog entry in customer language: what the service is and is not, who can use it, request offerings and how to request them, approvals, fulfilment steps, service levels and support hours, costs if charged, dependencies, responsibilities and ownership. Use when a new IT or internal service is launched, an existing entry is outdated or unclear, requesters keep asking how to get something, or service levels must be published for users.
- Try: _"Write a catalog entry for our 'Developer VM' service: devs request a Linux VM with 8 vCPU/32 GB, manager approval needed, delivered in 2 business days, deleted after 90 days unless extended."_
- Related: `slo-definition`, `sla-breach-analysis`, `raci-matrix`, `user-guide`, `faq-builder`
- File: [skills/11-support-ops/it-service-management/itsm/service-catalog-entry/SKILL.md](skills/11-support-ops/it-service-management/itsm/service-catalog-entry/SKILL.md)

## Technical Writing

### Technical Writer

#### Product Documentation

**Write a user guide** · `user-guide`

- When: Writes a task-based user guide for a product or feature, organized around what users need to accomplish, with prerequisites, numbered steps, expected results, screenshot placeholders, troubleshooting and cross-links. Use when end users or administrators need documentation for a new or changed feature, when a release needs user-facing docs, or when an existing manual is feature-oriented and hard to follow.
- Try: _"Write the user guide section for our new invoice approval workflow for finance approvers, based on these specs and screen names."_
- Related: `how-to-guide`, `tutorial`, `docs-information-architecture`, `style-guide-check`, `faq-builder`
- File: [skills/12-technical-writing/technical-writer/docs/user-guide/SKILL.md](skills/12-technical-writing/technical-writer/docs/user-guide/SKILL.md)

**Write a tutorial** · `tutorial`

- When: Writes a learning-oriented tutorial in the Diátaxis sense: a single guided path in which a newcomer builds something concrete, with a defined learning outcome, prerequisites, small verifiable steps, visible results after each step and no detours. Use when onboarding new users or developers to a product, API, SDK or platform, when a \"getting started\" or first-project lesson is needed, or when existing getting-started content is a mix of reference and how-to.
- Try: _"Write a getting-started tutorial for our payments API where a developer creates a test payment and handles the webhook, in about 30 minutes."_
- Related: `how-to-guide`, `user-guide`, `docs-information-architecture`, `technical-onboarding`, `readme-writing`
- File: [skills/12-technical-writing/technical-writer/docs/tutorial/SKILL.md](skills/12-technical-writing/technical-writer/docs/tutorial/SKILL.md)

**Write a how-to guide** · `how-to-guide`

- When: Writes a goal-oriented how-to guide in the Diátaxis sense: a focused recipe that takes a reader who already knows the basics from a stated starting point to one real-world result, with preconditions, numbered action steps, decision points, verification and troubleshooting, and no teaching or background detours. Use when users ask \"how do I ...\", when a support ticket or recurring question reveals a task without documentation, or when existing docs mix tutorial, reference and explanation for a practical task.
- Try: _"Write a how-to guide for rotating the API signing key in our platform without downtime, for integration developers."_
- Related: `tutorial`, `user-guide`, `docs-information-architecture`, `style-guide-check`, `runbook`
- File: [skills/12-technical-writing/technical-writer/docs/how-to-guide/SKILL.md](skills/12-technical-writing/technical-writer/docs/how-to-guide/SKILL.md)

**Structure documentation** · `docs-information-architecture`

- When: Designs or restructures the information architecture of a documentation set using the Diátaxis quadrants (tutorials, how-to guides, reference, explanation): audits existing pages, classifies and splits mixed content, defines navigation, naming and page types, and produces a target site map with a migration plan. Use when docs are hard to navigate, when pages mix learning, tasks, reference and concepts, when a new product or portal needs a documentation structure, or before a docs migration or consolidation.
- Try: _"Here is our current docs sidebar with 60 pages; propose a restructure so developers can find setup, tasks and API reference faster."_
- Related: `tutorial`, `how-to-guide`, `user-guide`, `api-reference-docs`, `glossary-builder`
- File: [skills/12-technical-writing/technical-writer/docs/docs-information-architecture/SKILL.md](skills/12-technical-writing/technical-writer/docs/docs-information-architecture/SKILL.md)

**Check against a style guide** · `style-guide-check`

- When: Checks a document against a style guide and terminology list and reports each deviation with location, rule, severity and a concrete rewrite: terminology, voice and tone, grammar and mechanics, formatting conventions, UI and code references, inclusive and accessible language. Use before publishing or reviewing documentation, UI text, release notes or knowledge-base articles, when several authors have produced inconsistent content, or when a team wants to enforce its own or a public style guide.
- Try: _"Check this installation guide against our style guide and terminology list and give me the fixes as a table."_
- Related: `glossary-builder`, `document-review`, `document-simplify`, `user-guide`, `how-to-guide`
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

- When: Turns raw 1:1 notes or a transcript into concise, factual notes with topics discussed, commitments with owners and dates, feedback exchanged and career or wellbeing signals to follow up. Use after a 1:1 with a direct report or mentee, or when building a running 1:1 log that later supports reviews and development plans.
- Try: _"Clean up my notes from today's 1:1 with Emre and pull out what we both committed to."_
- Related: `one-on-one-prep`, `action-item-extraction`, `performance-review`, `career-development-plan`, `meeting-notes`
- File: [skills/13-leadership/engineering-manager/people/one-on-one-notes/SKILL.md](skills/13-leadership/engineering-manager/people/one-on-one-notes/SKILL.md)

**Write a performance review** · `performance-review`

- When: Writes an evidence-based, competency-aligned and balanced performance review for an engineer or other team member, with a calibrated rating rationale, strengths, growth areas and next-period focus. Use when a review cycle is due, when converting 1:1 notes, peer feedback and delivery evidence into a written review, or when checking a draft review for bias and unsupported claims.
- Try: _"Draft Can's annual review from these notes, peer feedback and his goals. Our ladder level is Senior Engineer."_
- Related: `career-ladder`, `goal-setting`, `one-on-one-notes`, `career-development-plan`, `feedback-sbi`
- File: [skills/13-leadership/engineering-manager/people/performance-review/SKILL.md](skills/13-leadership/engineering-manager/people/performance-review/SKILL.md)

**Set individual goals** · `goal-setting`

- When: Drafts 3-5 SMART individual goals for an engineer or team member that connect team outcomes with the person's growth, each with measures, milestones and the support needed. Use at the start of a review period, after a promotion or role change, or when goals are vague, activity-based or disconnected from team priorities.
- Try: _"Help me set H2 goals for Deniz, a mid-level backend engineer. Team OKR is cutting checkout latency and she wants to grow toward senior."_
- Related: `okr-definition`, `performance-review`, `career-development-plan`, `career-ladder`, `one-on-one-prep`
- File: [skills/13-leadership/engineering-manager/people/goal-setting/SKILL.md](skills/13-leadership/engineering-manager/people/goal-setting/SKILL.md)

**Write a career development plan** · `career-development-plan`

- When: Builds a career development plan that compares a person's current level with a target level or path, identifies evidence-based gaps per competency and defines development actions, opportunities, support and checkpoints. Use when someone asks about promotion or a path change (IC vs management, specialization), after a review, or when a manager needs a structured growth conversation.
- Try: _"Create a development plan for Burak, Senior Engineer, who wants to move to Staff within 18 months."_
- Related: `career-ladder`, `goal-setting`, `performance-review`, `one-on-one-prep`, `onboarding-plan-30-60-90`
- File: [skills/13-leadership/engineering-manager/people/career-development-plan/SKILL.md](skills/13-leadership/engineering-manager/people/career-development-plan/SKILL.md)

**Write a performance improvement plan** · `underperformance-plan`

- When: Drafts a fair, evidence-based performance improvement plan (PIP) with specific expectation gaps, measurable success criteria, the support provided, milestone reviews and clearly stated consequences, ready for HR review. Use when informal feedback has not resolved a sustained performance gap, or when a manager needs to check whether a situation is ready for a formal plan.
- Try: _"Draft a 60-day improvement plan for a developer whose PRs repeatedly fail review and who missed three sprint commitments despite feedback since April."_
- Related: `performance-review`, `feedback-sbi`, `one-on-one-notes`, `bad-news-delivery`, `goal-setting`
- File: [skills/13-leadership/engineering-manager/people/underperformance-plan/SKILL.md](skills/13-leadership/engineering-manager/people/underperformance-plan/SKILL.md)

**Write a recognition message** · `recognition-message`

- When: Writes a specific, impact-focused recognition message for an individual or team, naming the concrete behavior, the result it produced and why it matters, adapted to channel (private, team, company-wide). Use when a manager or peer wants to thank someone for work, highlight invisible contributions, or celebrate a launch, incident response or mentoring effort.
- Try: _"Write a team-channel thank-you for Selin, who spent the weekend untangling the data migration rollback and wrote a clean postmortem."_
- Related: `feedback-sbi`, `announcement`, `tone-rewrite`, `performance-review`
- File: [skills/13-leadership/engineering-manager/people/recognition-message/SKILL.md](skills/13-leadership/engineering-manager/people/recognition-message/SKILL.md)

#### Hiring

**Write a job description** · `job-description`

- When: Writes an inclusive, accurate job description for a software role with the role mission, first-year outcomes, responsibilities, must-have versus nice-to-have requirements, team context and practical details, and checks it for biased or exclusionary language. Use when opening a new position, rewriting an outdated posting, or when a posting attracts the wrong candidates or too few diverse applicants.
- Try: _"Write a job description for a Senior Data Engineer in our Istanbul platform team, hybrid, working on streaming pipelines with Kafka and Spark."_
- Related: `role-definition`, `interview-plan`, `career-ladder`, `onboarding-plan-30-60-90`, `tone-rewrite`
- File: [skills/13-leadership/engineering-manager/hiring/job-description/SKILL.md](skills/13-leadership/engineering-manager/hiring/job-description/SKILL.md)

**Design an interview loop** · `interview-plan`

- When: Designs a structured interview loop for a role, mapping each competency to exactly the stages that assess it, with stage formats, durations, interviewer profiles, rubrics, candidate communication and decision rules that reduce bias. Use when opening a role, when an existing loop is slow, inconsistent or has low offer acceptance, or when interviewers assess overlapping things and miss others.
- Try: _"Design an interview loop for a mid-level frontend engineer. We can afford at most four hours of candidate time."_
- Related: `job-description`, `technical-interview-questions`, `interview-scorecard`, `candidate-debrief`, `career-ladder`
- File: [skills/13-leadership/engineering-manager/hiring/interview-plan/SKILL.md](skills/13-leadership/engineering-manager/hiring/interview-plan/SKILL.md)

**Prepare technical interview questions** · `technical-interview-questions`

- When: Prepares level-calibrated technical interview questions with follow-up probes and a behaviorally anchored scoring rubric for one interview stage. Use when an interviewer needs a question set for coding, system design, debugging or domain stages, when calibrating questions to a level, or when replacing trivia and puzzle questions with job-relevant ones.
- Try: _"Prepare a 60-minute system design question set for a senior backend engineer, with rubric. We work on event-driven order processing."_
- Related: `interview-plan`, `interview-scorecard`, `career-ladder`, `job-description`, `candidate-debrief`
- File: [skills/13-leadership/engineering-manager/hiring/technical-interview-questions/SKILL.md](skills/13-leadership/engineering-manager/hiring/technical-interview-questions/SKILL.md)

**Write an interview scorecard** · `interview-scorecard`

- When: Turns an interviewer's raw notes into a scorecard with verbatim evidence per competency, a rubric-based score, and an independent hire recommendation with rationale. Use right after an interview, when notes must be written up before the debrief, or when checking a scorecard for missing evidence, bias or impressions presented as facts.
- Try: _"Here are my notes from the system design interview with candidate B. Turn them into a scorecard against our senior rubric."_
- Related: `technical-interview-questions`, `candidate-debrief`, `interview-plan`, `bias-check`
- File: [skills/13-leadership/engineering-manager/hiring/interview-scorecard/SKILL.md](skills/13-leadership/engineering-manager/hiring/interview-scorecard/SKILL.md)

**Summarize a candidate debrief** · `candidate-debrief`

- When: Consolidates interview scorecards into a structured debrief summary with a competency coverage matrix, conflicting signals, resolved and unresolved questions, and a documented hire decision with level. Use when preparing or running a candidate debrief, when interviewers disagree, or when a hiring decision must be recorded with its evidence and rationale.
- Try: _"Summarize the debrief for candidate B from these four scorecards and give me a decision draft for the senior level."_
- Related: `interview-scorecard`, `interview-plan`, `decision-log`, `onboarding-plan-30-60-90`, `bias-check`
- File: [skills/13-leadership/engineering-manager/hiring/candidate-debrief/SKILL.md](skills/13-leadership/engineering-manager/hiring/candidate-debrief/SKILL.md)

**Write a 30-60-90 day onboarding plan** · `onboarding-plan-30-60-90`

- When: Writes a 30-60-90 day onboarding plan for a new hire with outcomes per phase, concrete first tasks, people to meet, access and learning milestones, and check-in points. Use when someone joins or moves into a new team or role, when a buddy or manager needs a structured ramp-up, or when an existing plan is only a list of documents to read.
- Try: _"Write a 30-60-90 day plan for a mid-level backend engineer joining our payments team next month."_
- Related: `technical-onboarding`, `onboarding-guide`, `goal-setting`, `one-on-one-prep`, `job-description`
- File: [skills/13-leadership/engineering-manager/hiring/onboarding-plan-30-60-90/SKILL.md](skills/13-leadership/engineering-manager/hiring/onboarding-plan-30-60-90/SKILL.md)

#### Team & Org Design

**Design team topology** · `team-topology`

- When: Designs or reviews a team topology using stream-aligned, platform, enabling and complicated-subsystem team types and their interaction modes, based on value streams, cognitive load and dependencies. Use when forming or splitting teams, when handoffs and cross-team dependencies slow delivery, when a platform team is being considered, or when team boundaries do not match the architecture.
- Try: _"We have 5 teams and 40 engineers, every feature needs 3 teams. Propose a team topology for our e-commerce platform."_
- Related: `bounded-context-map`, `service-decomposition`, `role-definition`, `cross-team-dependency-board`, `org-change-communication`
- File: [skills/13-leadership/engineering-manager/team/team-topology/SKILL.md](skills/13-leadership/engineering-manager/team/team-topology/SKILL.md)

**Define a role** · `role-definition`

- When: Defines a role with its mission, outcomes, responsibilities, decision rights, interfaces with other roles, and what the role is not accountable for. Use when creating a new role (e.g. staff engineer, tech lead, platform product owner), when two roles overlap or conflict, or when decision rights are unclear and work falls between roles.
- Try: _"Define the tech lead role in our teams; people confuse it with the engineering manager and the architect."_
- Related: `raci-matrix`, `career-ladder`, `job-description`, `team-topology`, `governance-framework`
- File: [skills/13-leadership/engineering-manager/team/role-definition/SKILL.md](skills/13-leadership/engineering-manager/team/role-definition/SKILL.md)

**Build a career ladder** · `career-ladder`

- When: Builds or revises a career ladder for a job family with levels, scope and impact per level, competency expectations with observable examples, and parallel individual contributor and management tracks. Use when an organization needs consistent levelling for promotions, hiring and reviews, when levels are vague or inconsistent across teams, or when adding a staff/principal or management track.
- Try: _"Build a career ladder for our software engineers from junior to principal, with a separate management track from team lead to director."_
- Related: `role-definition`, `performance-review`, `career-development-plan`, `job-description`, `interview-plan`
- File: [skills/13-leadership/engineering-manager/team/career-ladder/SKILL.md](skills/13-leadership/engineering-manager/team/career-ladder/SKILL.md)

**Review engineering metrics (DORA/SPACE)** · `engineering-metrics-review`

- When: Reviews engineering delivery metrics using DORA (deployment frequency, lead time for changes, change failure rate, time to restore) and SPACE dimensions, interprets trends with context, detects gaming and data-quality issues, and proposes improvement experiments. Use when preparing a metrics review for a team or organization, when leadership asks for productivity numbers, or when metrics are being misused to compare individuals.
- Try: _"Here are our DORA numbers for the last two quarters for four teams. Review them and tell me what to discuss with the teams."_
- Related: `cycle-time-analysis`, `team-health-check`, `kpi-definition`, `metric-definition`, `velocity-analysis`
- File: [skills/13-leadership/engineering-manager/team/engineering-metrics-review/SKILL.md](skills/13-leadership/engineering-manager/team/engineering-metrics-review/SKILL.md)

### CTO / VP / Director

#### Technology Strategy

**Write a technology strategy** · `technology-strategy`

- When: Writes a technology strategy structured as diagnosis, guiding policy and coherent actions, linked to business goals, with explicit trade-offs, what will not be done, and measures of progress. Use when a CTO or technology leader needs a multi-year direction, when existing plans are wish lists without choices, or when aligning architecture, platform, talent and investment decisions with business strategy.
- Try: _"Write a 3-year technology strategy for our insurance company; we have a legacy core, slow releases and a new digital sales goal."_
- Related: `target-state-architecture`, `architecture-principles`, `product-strategy-one-pager`, `tech-radar`, `budget-proposal`
- File: [skills/13-leadership/executive/strategy/technology-strategy/SKILL.md](skills/13-leadership/executive/strategy/technology-strategy/SKILL.md)

**Run quarterly planning** · `quarterly-planning`

- When: Runs a quarterly planning cycle for a technology organization, turning strategy and demand into a capacity-backed set of commitments, stretch items and explicit trade-offs, with dependencies and risks visible. Use when a CTO, VP or director has to decide what the teams commit to next quarter, when demand exceeds capacity, or when previous quarters overcommitted and underdelivered.
- Try: _"Help me plan Q3 for our 6 engineering teams; we have 40 requests from the business, a platform migration and 20% of capacity already lost to support."_
- Related: `technology-strategy`, `capacity-planning`, `okr-definition`, `portfolio-prioritization`, `cross-team-dependency-board`
- File: [skills/13-leadership/executive/strategy/quarterly-planning/SKILL.md](skills/13-leadership/executive/strategy/quarterly-planning/SKILL.md)

**Write a budget proposal** · `budget-proposal`

- When: Writes a technology budget proposal that separates investment (change) from run costs, ties each line to a business outcome, shows the cost of not funding, and offers funding scenarios with their consequences. Use when a technology leader must request or defend an annual or project budget, justify headcount, licenses or cloud spend, or present options to finance or the executive team.
- Try: _"Draft our IT budget proposal for next year; run costs grow 12% from cloud and licenses, and we want funding for a data platform and 4 more engineers."_
- Related: `technology-strategy`, `cost-benefit-analysis`, `cloud-cost-estimate`, `budget-plan`, `board-update`
- File: [skills/13-leadership/executive/strategy/budget-proposal/SKILL.md](skills/13-leadership/executive/strategy/budget-proposal/SKILL.md)

**Evaluate vendors (RFP)** · `vendor-evaluation`

- When: Evaluates vendors or products for a technology purchase, from requirements and knock-out criteria through a weighted scoring model fixed before responses are read, evidence-based scoring, total cost of ownership and risk, to a documented recommendation. Use when selecting a software product, platform, cloud or service provider, preparing or scoring an RFP, or when a vendor choice must be defensible to procurement, audit or leadership.
- Try: _"We have 3 responses to our RFP for an API management platform; build the evaluation model and recommend a vendor."_
- Related: `decision-matrix`, `build-vs-buy`, `fit-gap-analysis`, `vendor-status-review`, `it-risk-assessment`
- File: [skills/13-leadership/executive/strategy/vendor-evaluation/SKILL.md](skills/13-leadership/executive/strategy/vendor-evaluation/SKILL.md)

**Write an executive/board update** · `board-update`

- When: Writes a concise executive or board update on technology: what changed since last time, a few outcome metrics against targets, top risks with trend and mitigation, and explicit asks or decisions needed. Use when a CTO, CIO or technology director reports to the board, executive committee or investors, or when a long technical status must be condensed for non-technical senior readers.
- Try: _"Write my quarterly technology update for the board; cloud migration is 60% done, we had two major outages, and I need approval for a security investment."_
- Related: `executive-summary`, `status-update`, `technology-strategy`, `budget-proposal`, `risk-register`
- File: [skills/13-leadership/executive/strategy/board-update/SKILL.md](skills/13-leadership/executive/strategy/board-update/SKILL.md)

**Communicate an org change** · `org-change-communication`

- When: Plans and writes the communication of an organizational change (reorganization, new teams, reporting line changes, role changes, office or process changes): why, what changes, what does not, who is affected, timeline, support and where to ask, sequenced so affected people hear first and privately. Use when a leader announces a reorg or team change, when rumors must be addressed, or when a change needs a message set for different audiences.
- Try: _"We are merging the mobile and web teams into product-aligned teams next month; write the announcement and a plan for who hears what, when."_
- Related: `team-topology`, `announcement`, `bad-news-delivery`, `faq-builder`, `communication-plan`
- File: [skills/13-leadership/executive/strategy/org-change-communication/SKILL.md](skills/13-leadership/executive/strategy/org-change-communication/SKILL.md)

## Presales & Consulting

### Presales / Solution Consultant

#### Bids & Proposals

**Analyze an RFP** · `rfp-analysis`

- When: Analyzes a client RFP/RFQ/tender document from the bidder's side, extracting mandatory and scored requirements, evaluation criteria, commercial and legal terms, deadlines, hidden expectations and risks, and produces a compliance matrix and a reasoned bid/no-bid recommendation. Use when a new RFP or tender arrives, before committing presales effort, or when the team must decide whether and how to bid.
- Try: _"Analyze this 80-page RFP for a core banking integration project and tell me whether we should bid."_
- Related: `rfp-response`, `effort-estimate-for-bid`, `proposal-writing`, `requirements-gap-analysis`, `risk-register`
- File: [skills/14-presales-consulting/presales-consultant/bid/rfp-analysis/SKILL.md](skills/14-presales-consulting/presales-consultant/bid/rfp-analysis/SKILL.md)

**Write an RFP response** · `rfp-response`

- When: Writes compliant, benefit-led answers to RFP/RFI/tender requirements, one per requirement, stating the compliance level first, then how the solution meets it, the evidence and the client benefit, in the client's format and within limits. Use when drafting or improving answers to an RFP questionnaire or compliance table, when answers are too generic or feature-led, or when partial compliance must be stated honestly.
- Try: _"Write our answers for requirements R-10 to R-25 in this RFP; our product covers most of them, two need customization."_
- Related: `rfp-analysis`, `proposal-writing`, `effort-estimate-for-bid`, `statement-of-work`, `traceability-matrix`
- File: [skills/14-presales-consulting/presales-consultant/bid/rfp-response/SKILL.md](skills/14-presales-consulting/presales-consultant/bid/rfp-response/SKILL.md)

**Write a proposal** · `proposal-writing`

- When: Writes a client-centric proposal covering executive summary, understanding of the client's situation and goals, proposed solution, delivery approach, plan and milestones, team, assumptions, and commercial summary, with win themes and proof points traced to the client's own priorities. Use when responding to a client request or RFP with a narrative proposal, when a solution must be presented for a buying decision, or when a draft proposal reads as a generic capabilities brochure.
- Try: _"Write a proposal for modernizing a logistics company's legacy dispatch system; here are the discovery notes and our estimate."_
- Related: `rfp-analysis`, `rfp-response`, `effort-estimate-for-bid`, `statement-of-work`, `executive-summary`
- File: [skills/14-presales-consulting/presales-consultant/bid/proposal-writing/SKILL.md](skills/14-presales-consulting/presales-consultant/bid/proposal-writing/SKILL.md)

**Estimate effort for a bid** · `effort-estimate-for-bid`

- When: Builds an effort estimate for a bid or proposal by combining a bottom-up estimate from a work breakdown with a top-down or analogy check, making every assumption and exclusion explicit, adding risk-based contingency, and turning effort into a role-based staffing profile. Use when a presales team must price a fixed-price or time-and-materials bid, when an RFP asks for effort or team size, or when an existing bid estimate needs a sanity check.
- Try: _"Estimate the effort for our bid to build a B2B customer portal with SSO, order tracking and ERP integration; they want a fixed price."_
- Related: `rfp-analysis`, `proposal-writing`, `statement-of-work`, `estimation-three-point`, `wbs`
- File: [skills/14-presales-consulting/presales-consultant/bid/effort-estimate-for-bid/SKILL.md](skills/14-presales-consulting/presales-consultant/bid/effort-estimate-for-bid/SKILL.md)

**Write a statement of work** · `statement-of-work`

- When: Writes a statement of work (SOW) that defines objectives, in-scope and out-of-scope work, deliverables with acceptance criteria and procedure, milestones, roles and responsibilities of both parties, assumptions, dependencies, change control, and commercial references, in testable, unambiguous language. Use when a proposal is accepted and scope must be contractually fixed, when a project or phase needs a SOW under a master agreement, or when an existing SOW must be reviewed for ambiguity and scope-creep risk.
- Try: _"Draft a SOW for phase 1 of the customer portal project: SSO, order tracking and ERP order sync, fixed price, 4 months."_
- Related: `proposal-writing`, `effort-estimate-for-bid`, `scope-statement`, `acceptance-certificate`, `change-control`
- File: [skills/14-presales-consulting/presales-consultant/bid/statement-of-work/SKILL.md](skills/14-presales-consulting/presales-consultant/bid/statement-of-work/SKILL.md)

#### Consulting

**Run a client discovery workshop** · `discovery-workshop`

- When: Designs and documents a client discovery workshop for an early engagement, with objectives, participant mix, pre-work, a timeboxed agenda, question bank by topic, breakout and note-and-vote convergence mechanics, and a structured output (goals, pain points, current landscape, requirements themes, constraints, risks, next steps). Use when starting a new client engagement or presales pursuit, when a vague client need must be shaped into scope, or when workshop notes must be turned into a discovery summary.
- Try: _"Plan a one-day discovery workshop with a retail client who wants to \"modernize their e-commerce platform\" and has not shared details."_
- Related: `workshop-plan`, `facilitation-guide`, `current-state-assessment`, `stakeholder-map`, `interview-question-set`
- File: [skills/14-presales-consulting/presales-consultant/consulting/discovery-workshop/SKILL.md](skills/14-presales-consulting/presales-consultant/consulting/discovery-workshop/SKILL.md)

**Assess a client's current state** · `current-state-assessment`

- When: Assesses a client's current state across business process, applications, data, technology, organization and delivery practices, producing evidence-backed findings, a maturity rating per dimension with a stated scale, root-cause-linked pain points, and prioritized recommendations with quick wins and a high-level roadmap. Use when a client asks \"where do we stand\", before a transformation or modernization proposal, or when discovery outputs, interviews and documents must be consolidated into an assessment report.
- Try: _"Assess the current state of a mid-size insurer's claims platform from these interview notes and system inventory, and recommend where to start."_
- Related: `discovery-workshop`, `fit-gap-analysis`, `modernization-assessment`, `capability-map`, `client-steering-report`
- File: [skills/14-presales-consulting/presales-consultant/consulting/current-state-assessment/SKILL.md](skills/14-presales-consulting/presales-consultant/consulting/current-state-assessment/SKILL.md)

**Run a fit-gap analysis** · `fit-gap-analysis`

- When: Runs a fit-gap analysis that compares requirements against the standard capabilities of a package, platform or reference process, classifies each as fit, fit with configuration, gap or not applicable, proposes a resolution per gap (process change, configuration, extension, integration, third-party, workaround, defer) with effort band and risk, and summarizes the fit ratio and decisions needed. Use when evaluating or implementing an ERP, CRM, SaaS or other packaged solution, when a client asks how much customization a package will need, or when requirements must be aligned to a standard process.
- Try: _"Do a fit-gap of these 40 order-to-cash requirements against a standard cloud ERP sales module and tell us where customization is unavoidable."_
- Related: `requirements-gap-analysis`, `build-vs-buy`, `vendor-evaluation`, `current-state-assessment`, `effort-estimate-for-bid`
- File: [skills/14-presales-consulting/presales-consultant/consulting/fit-gap-analysis/SKILL.md](skills/14-presales-consulting/presales-consultant/consulting/fit-gap-analysis/SKILL.md)

**Write a client steering report** · `client-steering-report`

- When: Writes a client-facing steering committee report for a consulting or delivery engagement, covering overall status against plan with an explicit rating rule, progress on milestones, value delivered against the agreed outcomes, budget and effort burn, top risks and issues, change requests, and the decisions the client steering group must take. Use before a client steering committee or executive review, when a periodic engagement report is due, or when delivery data must be turned into a decision-oriented client update.
- Try: _"Write the monthly steering report for our client's CRM rollout: phase 2 is two weeks late, budget is on track, we need a decision on the data migration scope."_
- Related: `steering-committee-pack`, `project-status-report`, `benefits-realization`, `raid-log`, `bad-news-delivery`
- File: [skills/14-presales-consulting/presales-consultant/consulting/client-steering-report/SKILL.md](skills/14-presales-consulting/presales-consultant/consulting/client-steering-report/SKILL.md)
