---
name: ai-context-engineering-profiles
description: Build a persistent, structured context profile (business intelligence + ICP psychology + platform-native intelligence + identity programming) that turns a generic LLM into an AI that writes/thinks like a specific business — plus how to curate an external knowledge base of world-class frameworks and use the same setup as a personal/team "AI advisor". Trigger when the user wants AI-generated content to stop "sounding like AI", wants to set up a Claude Project / persistent context for content or business advice, wants an AI ghostwriter trained on their voice, or wants to train a team using AI + curated frameworks. Also trigger on Polish phrasing like "profil kontekstowy AI", "AI piszący moim głosem", "baza wiedzy dla AI jako doradcy".
---

# Context engineering: AI that thinks like your best employee

Core principle: AI is an amplifier, not a creator — input in, output out.
"Write me a LinkedIn post about X" on a bare model produces generic,
robotic output because the model has no context to amplify. The fix isn't
better prompting per message, it's building a **persistent context
profile** once, so every future request already carries it.

## Layer 1 — Business intelligence profile

Build once, store as structured files (JSON reads most reliably to the
model; markdown works too) in a persistent project/knowledge base:

- **ICP psychology profile** — not demographics. Capture: trust triggers,
  buying motivations, objection patterns, past automation/tool
  disappointments, what they've tried and failed at, "lies they've been
  told" (bad advice/myths common in their situation), untried-but-
  interested items, common questions, content/engagement preferences,
  lifestyle traits. Mine this from real sales-call transcripts — that's
  the actual voice of the customer, not guesswork.
- **Business context** — strategic positioning, competitive advantages,
  product strategy, current offers.
- **Personal/brand profile** — your own background, communication style,
  the way you personally articulate ideas (so output doesn't just sound
  correct, it sounds *like you*).
- **Brand voice** — a distinct document describing tone/vocabulary/style,
  separate from the ICP and business docs so it can be reused across every
  content type.

## Layer 2 — Platform-native intelligence

A single "brand voice" isn't enough — every platform has its own culture,
and content that works on one reads wrong on another (LinkedIn's
hook/rehook/image structure with a professional register vs. Twitter's
punchier, more entertainment-driven register for the same underlying
idea). Maintain, per platform:

- A small library of your own best-performing posts as style exemplars.
- Platform-specific formatting and conversion patterns.
- What specifically drives engagement/action on that platform.

Ghostwriter prompt pattern that works: tell the model to act as a *senior
ghostwriter* whose specialty is mirroring someone's vocabulary, diction,
post structure, and content approach so precisely nobody could tell it's
written by someone else; explicitly instruct it to study vocabulary
patterns, line spacing, visual breaks, and how ideas build and flow in the
example posts — formatting cues get missed by the model unless you name
them explicitly. Set hard constraints (e.g. "max 300 words") in the
prompt itself.

## Layer 3 — Identity programming

Don't just describe a role ("you are a copywriter"). Give the model an
identity with backstory/framing ("lore") plus the proven frameworks it
should apply — identity + frameworks produces more consistent, less
generic output than a bare role description. This generalizes past
content: the same three-layer stack (business intelligence → channel-
native intelligence → identity) works for sales copy, newsletters, YouTube
scripts, blog posts, and AI-SDR follow-up messages — anywhere you need
output that's specifically *yours*, not generic AI output.

## Layer 4 — Curated external knowledge base (AI as advisor)

The same context-engineered setup can act as a personal or team business
advisor, not just a content generator — but only if its knowledge base is
curated, not generic:

1. **Source world-class, proprietary frameworks**, not generic advice —
   transcripts of specific experts' content (a transcript-download tool
   for YouTube; an actor/scraper platform for Twitter/LinkedIn/Instagram
   profiles or hashtags), paid course transcripts, competitor positioning.
   Export only the fields you actually need (e.g. post text, not internal
   IDs/metadata) — dumping raw scraped JSON wastes context and increases
   hallucination risk; condensed, relevant data performs better than bulk
   data.
2. **Let the model digest before applying.** Two-step, not one-shot: first
   ask it to read/understand the new source document on its own; only in a
   follow-up turn ask it to apply those frameworks to a specific piece of
   your own content (a post draft, an offer, a proposal). Asking it to
   "read this and immediately rewrite that" in one shot performs worse
   than the same two steps separated — same as it would be harder for a
   person.
3. **Use it as a business ceiling-raiser.** A founder's business can only
   execute at the level the founder personally understands the underlying
   skill (copy, systems thinking, negotiation) — you can't judge or hire
   for a skill you can't evaluate. Feed the profile real frameworks (e.g.
   a named negotiation framework, a named value-equation framework) and
   ask it to audit your own real artifacts (a call transcript, a live
   post, a proposal) against them, candidly, including telling you when
   there's nothing new to apply — a generic model will just flatter you,
   a properly-seeded one gives specific, sourced critique.
4. **Extend it to team training.** Upload your own best sales-call
   transcripts (or any exemplary internal work) as the reference standard;
   give a team member the same context-engineered assistant to practice
   against or get QA'd by. This scales coaching without the
   founder/manager doing 1:1 review every time, and compounds — the whole
   team's skill floor rises with the knowledge base, not just the
   founder's.

## Practical setup notes

- Keep each concern in its own file/document (ICP ≠ business context ≠
  brand voice ≠ platform examples) so the model can be pointed at the
  relevant subset per task rather than always loading everything.
- Prefer a model with strong instruction-following and extended/deliberate
  reasoning for this kind of synthesis work over a bare fast-mode model.
- This complements [[ai-ops-dependency-audit]] and
  [[ai-agent-system-blueprints]] — those are about *what* systems to build
  in a business; this is the technique for making any one of those AI
  systems sound like the business instead of like generic AI output.
