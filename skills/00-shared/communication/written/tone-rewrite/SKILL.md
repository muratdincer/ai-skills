---
description: Rewrites an existing message to a target tone (clearer, softer, firmer, more formal, more concise, more neutral) while preserving its facts, commitments and asks, and explains the key changes. Use when someone has a draft email, chat message, review comment or reply that sounds too harsh, too vague, too long, too informal or too passive, or asks to "make this sound better", "soften", "be more assertive" or "make it professional".
related: stakeholder-email, feedback-sbi, bad-news-delivery, document-simplify, technical-translation
prompt: Make this reply to a customer firmer but still polite: "Sorry, we might not be able to do the custom report this month, maybe next month if possible?"
---

# Rewrite for Tone

## Purpose
Change how a message lands without changing what it says, so the reader responds to the content instead of reacting to the wording, and the sender keeps the relationship and their credibility.

## When to use
- A draft is emotionally charged (frustrated, defensive, sarcastic) and must be neutralized before sending.
- A message is too hedged or apologetic and needs to be firmer.
- The register must change: internal to external, peer to executive, chat to formal letter.

## When not to use
- There is no draft yet and the purpose is unclear. Use `stakeholder-email`.
- The message is feedback on someone's behavior. Use `feedback-sbi` to restructure it first.
- The text is long documentation to be simplified. Use `document-simplify`.

## Inputs
Required:
- The original text.
- The target tone or the problem with the current tone.

Optional:
- Recipient and relationship, channel, language/culture, sender's constraints (what cannot be promised).

If the target tone is not given, ask one question offering 3-4 options (e.g. "firmer, softer, more formal, or shorter?"). Do not add facts, promises, apologies or dates that are not in the original.

## Process
1. Extract the invariant content: facts, numbers, commitments, asks, deadlines, refusals. These must survive the rewrite unchanged.
2. Diagnose the tone problems with evidence from the text: hedges ("maybe", "just", "if possible"), blame ("you failed to"), absolutes ("always", "never"), sarcasm, passive voice hiding the actor, over-apology, jargon, length.
3. Set the target: register (formal/neutral/informal), directness (low/high) and warmth (low/high), adjusted to the recipient and culture. In Turkish, decide "siz" vs "sen" explicitly.
4. Restructure if needed: put the key message or ask first, then reasons, then next step.
5. Rewrite sentence by sentence: remove hedges for firmness; replace "you" accusations with "I/we" statements or neutral descriptions for softness; use active voice with clear actors; cut filler.
6. Keep one sincere acknowledgement or apology at most, and only if something went wrong on the sender's side.
7. Compare the rewrite against the invariant list; if any fact, ask or commitment changed, restore it. If making the tone work requires a new promise, flag it instead of adding it.
8. Offer one alternative variant if the target was ambiguous (e.g. firm-formal vs firm-warm).
9. List the 3-5 most important changes and why, so the sender learns the pattern.
10. If the user's goal continues, suggest `bad-news-delivery` if the message is really a refusal or delay, or `stakeholder-email` to rebuild the message around a clearer purpose.

## Output format
```markdown
**Rewritten (<target tone>):**
<message>

**Alternative (<variant>):** <optional>

**Key changes**
- <change> – <why>

**Preserved:** <facts/asks/commitments kept>
**Flags:** <anything the sender must decide, e.g. a promise the tone suggests but the original did not make>
```

## Quality checklist
- [ ] All facts, numbers, asks and commitments from the original are preserved, and none are added.
- [ ] The target tone is audible: hedges removed for firm, blame removed for soft, register matches the recipient.
- [ ] The main message or ask is in the first two sentences.
- [ ] The rewrite is not longer than needed; typically equal or shorter than the original.
- [ ] Changes are explained briefly.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- "Softening" by adding vagueness, which hides the ask. Soft tone, clear content.
- "Firming" by adding aggression or capital letters. Firmness comes from certainty and specificity, not volume.
- Adding corporate filler ("As per my previous email", "Please do not hesitate") that makes the text longer and colder.

## Example
Input (firmer, still polite): "Sorry, we might not be able to do the custom report this month, maybe next month if possible?"

Weak rewrite: "Unfortunately, due to various constraints, the custom report may potentially be delayed. We will try our best."

Strong rewrite: "We cannot deliver the custom report this month. We can deliver it in `[month – TBD]`; please confirm by `[date]` if that works for you."
Key changes: removed "might/maybe" to state the fact; replaced the question with a concrete option and a decision request. Flag: the original did not commit to next month; confirm before sending.
