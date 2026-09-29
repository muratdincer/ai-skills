# Usage Guide

How to install and use the skills in any AI tool. For the list of skills with example requests see [GUIDE.md](GUIDE.md); for the full tree see [CATALOG.md](CATALOG.md).

## 1. What a skill is

A skill is a plain Markdown file (`SKILL.md`) with a short YAML header. The header's `description` tells the AI **when** to use the skill; the body tells it **how**: steps, output template, quality checklist. Nothing in a skill depends on a specific vendor, so the same file works as:

- an auto-discovered skill in tools that support the open Agent Skills format,
- a rule or instruction file in editors that use rules,
- a knowledge file or system prompt in chat assistants,
- a prompt you paste into any chat.

Every skill exists in English (`SKILL.md`) and Turkish (`SKILL.tr.md`). Both have the same ID, structure and output.

## 2. Pick an export format

All formats are produced by `scripts/export.py` (Python 3.8+, no dependencies). Use `--lang tr` for Turkish content and filter with `--category`, `--role` or `--skill` to install only what you need.

| Your tool supports… | Format | Command |
|---|---|---|
| Agent Skills folders (`<skills-dir>/<id>/SKILL.md`) | `skills` | `python3 scripts/export.py skills --dest <skills-dir>` |
| Uploading skills as zip files in a web/desktop app | `zip` | `python3 scripts/export.py zip --dest dist/zips` |
| Rule files with a description (e.g. `.mdc`) | `cursor-rules` | `python3 scripts/export.py cursor-rules --dest .cursor/rules` |
| An `AGENTS.md` (or similar) context file | `agents-md` + `skills` | see 3.3 |
| Custom assistants, projects, knowledge files, system prompts | `bundle` | `python3 scripts/export.py bundle --role business-analyst --dest dist/ba.md` |
| Nothing special (any chat) | copy/paste | paste the skill file, then your request |

## 3. Tool setup

Skill folder locations change between versions. The paths below are typical as of 2026; confirm them in your tool's current documentation.

### 3.1 Tools with native Agent Skills support
Coding agents and chat apps that implement the Agent Skills format load a skill automatically when your request matches its `description`.

| Tool family | Typical project location | Typical personal location |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| GitHub Copilot (agent mode / coding agent) | `.github/skills/` | per tool docs |
| OpenAI Codex | per tool docs (skills directory) | `~/.codex/skills/` |
| Other Agent Skills compatible agents | their skills directory | their skills directory |

```bash
# Example: all business analysis skills in Turkish into a project
python3 scripts/export.py skills --lang tr --category 01-business-analysis --dest .claude/skills
```

For web/desktop apps that accept uploaded skills (for example Claude.ai), export zips and upload the ones you need:

```bash
python3 scripts/export.py zip --role product-owner --dest dist/zips
```

### 3.2 Editors with rule files
Export one rule per skill. Rules are "agent requested" (not always applied), so the editor includes a skill only when its description matches.

```bash
python3 scripts/export.py cursor-rules --role developer --dest .cursor/rules
```

### 3.3 Agents that read AGENTS.md (or a similar context file)
Put the skills in a folder and give the agent an index that tells it which file to open for which task.

```bash
python3 scripts/export.py skills   --lang en --dest .agent-skills
python3 scripts/export.py agents-md --lang en --dest AGENTS.md --skills-root .agent-skills
```

If your tool uses a different context file name (for example `GEMINI.md`), use that name as `--dest` or configure the tool to read `AGENTS.md`.

### 3.4 Chat assistants (custom assistants, projects, GPTs, Gems)
Create an assistant per role and give it a bundle as its knowledge or instructions:

```bash
python3 scripts/export.py bundle --lang tr --role business-analyst --dest dist/is-analisti.md
```

Suggested instruction for the assistant: "You have a set of skills in the attached file. For each request, pick the matching skill by its description, follow its Process and answer in its Output format. If required inputs are missing, ask for them first."

Bundles of a whole category can be large; prefer one bundle per role.

### 3.5 Direct API use
Use the skill body as (part of) the system prompt and the user's request as the user message. To let the model choose among many skills, put the index from a bundle (IDs + descriptions) in the system prompt, let the model name the skill it needs, then load that file on the next call.

## 4. Using skills

**Let the tool choose.** Describe the task naturally: "Here are my notes from today's workshop, turn them into action items." A skill-aware tool picks `action-item-extraction`.

**Name the skill** when you want certainty: "Use request-completeness-check on the request below."

**Provide the required inputs.** Each skill's *Inputs* section lists them. If something is missing, the skill asks for it or marks it `[UNKNOWN]` / `[ASSUMPTION]` rather than inventing.

**Chain skills.** Skills are small on purpose. Typical chains:

| Goal | Chain |
|---|---|
| New demand to ready backlog | `request-intake-document` → `request-clarification-questions` → `request-completeness-check` → `brd-writing` → `epic-breakdown` → `user-story` → `acceptance-criteria` → `invest-check` |
| Meeting to follow-up | `meeting-agenda` → `meeting-notes` → `decision-log` → `action-item-extraction` → `meeting-follow-up` |
| Idea to architecture decision | `problem-statement` → `technology-selection` → `trade-off-analysis` → `adr` → `architecture-review` |
| Story to merged code | `task-breakdown` → `implement-from-story` → `unit-test-writing` → `commit-message` → `pull-request-description` → `code-review` |
| Requirement to release | `testability-review` → `test-scenarios-from-requirements` → `test-case-writing` → `bug-report` → `test-summary-report` → `release-quality-gate` → `release-notes` |
| Incident to learning | `incident-response` → `incident-communication` → `postmortem` → `lessons-learned` |

Each skill lists its neighbours under `related` in its header.

**Language.** Install the Turkish files to get Turkish output and Turkish templates. You can also install English skills and ask for the answer in Turkish; the structure stays the same.

## 5. Customizing

- Copy a skill and adapt the *Output format* to your organization's template; keep the ID or create a new one in the catalog.
- Add company rules (naming, mandatory fields, approval steps) to *Process* or *Quality checklist*.
- To add a new skill follow [AUTHORING.md](AUTHORING.md), or use the `ai-skill-authoring` skill itself.

## 6. Good practice

- Remove or mask personal data, credentials and confidential figures before sending content to any AI tool.
- Treat outputs as drafts: the quality checklist reduces errors but a human owns the decision.
- Install only the roles you need; fewer, relevant skills are selected more reliably.
