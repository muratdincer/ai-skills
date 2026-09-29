---
description: Designs a retrieval-augmented generation (RAG) system covering corpus and access control, ingestion, chunking, embedding, hybrid retrieval, reranking, grounded answer generation with citations, evaluation and operations. Use when an LLM must answer from company documents or data, when an existing RAG gives wrong or uncited answers, or when choosing between RAG, fine-tuning and plain prompting.
related: prompt-design, llm-eval-set, ai-use-case-assessment, data-classification, solution-architecture-document
prompt: Design a RAG assistant that answers employee questions from 3,000 HR policy PDFs and intranet pages, respecting country-specific access.
---

# Design a RAG System

## Purpose
Produce a design where answers are grounded in the right, permitted sources, retrieval quality is measurable, and every design choice (chunking, retrieval, reranking, prompting) is justified by the corpus and the questions, not by defaults.

## When to use
- An assistant, search or support feature must answer from internal knowledge.
- An existing RAG hallucinates, misses obvious documents, or cites the wrong sources.
- The team must decide whether RAG, fine-tuning or long-context prompting fits the problem.

## When not to use
- The task needs no external knowledge; the issue is instruction quality. Use `prompt-design`.
- The business case and risk are not yet assessed. Use `ai-use-case-assessment`.

## Inputs
Required:
- Corpus description: document types, formats, volume, languages, update frequency.
- Typical user questions (10+ real examples if possible) and who the users are.

Optional, improves quality:
- Access rules and data classification, latency and cost targets, existing search or vector infrastructure.
- Known failure examples from a current system.

If sample questions are missing, ask for them; retrieval design depends on them. Other gaps become open questions.

## Process
1. Classify the questions: fact lookup, procedural, comparison, aggregation across documents, or requires reasoning over tables; note which are unanswerable by RAG (e.g. counts over all records need a query tool).
2. Define the corpus boundary and access model: sources, owners, classification, and how permissions are enforced at retrieval time (document-level ACL filter, never post-generation redaction only).
3. Design ingestion: parsing per format (tables, scanned PDFs, headings), cleaning, deduplication, metadata (source, section, date, language, access tags), and incremental refresh with deletion handling.
4. Choose chunking from document structure: section- or heading-aware chunks sized to the answer unit, with overlap and parent-document or small-to-big retrieval where context matters; justify size against question types.
5. Choose embeddings on stated criteria: languages covered, domain vocabulary, dimension and cost; plan an offline comparison on the sample questions rather than picking by reputation.
6. Design retrieval: hybrid lexical (BM25) plus vector search, metadata filters, top-k, and query rewriting or decomposition for multi-part questions.
7. Add reranking (cross-encoder or model-based) when precision in the top few results matters; state the latency cost.
8. Design generation: grounding instructions, citation format per claim, "not found in sources" behavior, conflict handling between sources (prefer newest or authoritative), and context window budget.
9. Define evaluation: retrieval metrics (recall@k, MRR on a labeled question-to-passage set) separately from answer metrics (faithfulness, answer relevance, citation accuracy); link to an eval set.
10. Plan operations and safety: freshness SLA, index rebuild, monitoring of no-answer and low-similarity rates, feedback capture, prompt injection from documents, masking of personal data in logs.
11. Record key decisions with alternatives and mark untested choices `[ASSUMPTION]`.
12. List open questions; suggest `llm-eval-set` to build the evaluation set and `prompt-design` for the generation prompt.

## Output format
```markdown
# RAG Design: <system name>
Users: <who> · Corpus: <types, volume, languages> · Freshness: <SLA>

## Question Types
| Type | Share | Example | RAG-suitable? |
|---|---|---|---|

## Architecture
<ingestion → index → retrieval → rerank → generation → feedback; diagram optional>

## Design Decisions
| Area | Choice | Rationale | Alternative | Status |
|---|---|---|---|---|
| Chunking | ... | ... | ... | [ASSUMPTION] until tested |
| Embeddings | ... | ... | ... | ... |
| Retrieval | ... | ... | ... | ... |
| Reranking | ... | ... | ... | ... |

## Access Control and Privacy
<ACL enforcement point, classification, log masking>

## Generation Contract
<grounding rules, citation format, no-answer behavior, conflict rule>

## Evaluation
- Retrieval: <metrics, labeled set>
- Answer: <metrics, eval set link>

## Operations
<refresh, monitoring signals, feedback loop>

## Risks and Open Questions
- ...
```

## Quality checklist
- [ ] Access control is enforced at retrieval, before content reaches the model.
- [ ] Chunking and retrieval choices are justified by question types and document structure.
- [ ] Retrieval quality and answer quality are evaluated separately.
- [ ] There is a defined "not found in sources" behavior and a citation format.
- [ ] Question types RAG cannot answer are identified with an alternative.
- [ ] Freshness, deletion and injection-from-documents are covered.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Tuning the prompt when retrieval is the problem. Check whether the right passage was in the top-k before touching generation.
- Fixed-size chunks that split tables and procedures. Use the document's own structure.
- Treating stale or deleted documents as a minor issue. Outdated policy answers are often worse than no answer.

## Example
Input: "HR assistant over 3,000 policy PDFs and intranet pages, country-specific access."

Excerpt of output:
- Access: each chunk carries `country` and `employee_group` tags; retrieval filters by the user's claims before search.
- Chunking: heading-aware sections, tables kept whole; parent section returned for context `[ASSUMPTION: validate on 50 labeled questions]`.
- Out of RAG scope: "How many vacation days do I have left?" needs a call to the HR system, not document retrieval.
