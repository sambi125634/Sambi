---
name: ai-context-engineering-profiles
description: Build a persistent, structured context profile (business intelligence + ICP psychology + platform-native intelligence + identity programming), then scale it into a single orchestration project (one unified context base + trigger-activated "cognitive architecture" files + stackable enhancement overlays) instead of one Claude Project per content type — usable for content, embedded directly into automation/SDR/chatbot workflows (e.g. n8n), or as a curated "AI advisor" knowledge base. Trigger when the user wants AI-generated content to stop "sounding like AI", wants an AI agent/automation/chatbot to "understand the business" instead of giving generic answers, wants to build an ICP profile from sales-call or support-ticket transcripts, wants an AI ghostwriter trained on their voice, is juggling too many separate AI projects/prompts and wants to consolidate them, or wants to train a team using AI + curated frameworks. Also trigger on Polish phrasing like "profil kontekstowy AI", "AI piszący moim głosem", "baza wiedzy dla AI jako doradcy", "profil ICP z rozmów sprzedażowych", "orkiestracja promptów AI".
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
- **Other profile types worth building the same way**: product strategy,
  a marketing-frameworks profile distilled from campaigns that actually
  converted (not generic playbooks), and a customer-success/support
  profile mined from historical support tickets (patterns in what breaks,
  what gets asked, what resolves fastest) — this last one is what makes an
  e-commerce support chatbot handle edge cases like a senior agent instead
  of a generic FAQ bot.

**Fastest bootstrap for the ICP/support profiles specifically**: don't
hand-write them. Paste raw, unedited call-recording transcripts (sales
calls or support tickets — thousands of lines is fine, this doesn't need
pre-cleaning) directly into the model and ask for a structured JSON output
covering aspirations, pain points, fears/beliefs, lifestyle traits, buying
motivations and frequency, tools currently used, objection patterns
(word-for-word customer quotes are gold here), common questions, budget/
timeline expectations, and success metrics they stated themselves. This
one-shots a usable profile straight from raw operational data — no
separate "generator project" step is required for this specific profile
type (contrast with the more general bootstrap workflow below for
profiles that don't come from a transcript corpus).

**Treat it as a living document, not a one-time artifact.** After each new
sales call or support interaction, feed the new transcript back in and ask
whether it changes the existing profile — this keeps the ICP/support
profile current as the market and product evolve, instead of decaying
into a stale snapshot from whenever it was first built.

**This generalizes past content generation.** The same JSON context
profile can be embedded directly into automation workflows (e.g. n8n),
AI SDR/outbound systems, and customer-facing chatbots — not just a
Claude Project for writing. That's the actual differentiator between an
amateur automation and one that "understands the business": the same
profile object that makes a ghostwriter sound authentic is what makes an
SDR agent's objection-handling sound senior and a support chatbot's
escalation judgment sound experienced.

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

**Never describe voice with adjectives — show examples instead.**
"Be casual, be direct, be punchy" is close to useless as an instruction:
five different writers (or five different model runs) execute "direct"
five different ways. Skip the adjective entirely and instead hand the
model a small curated library of your own best posts *segmented by type*
(e.g. a spreadsheet/doc column per type: lead-magnet posts, long
value/educational posts, short punchy posts, tweets), exported as
Markdown so line breaks, dividers, and structure survive intact — Markdown
specifically (not plain text) is what lets the model actually parse your
formatting rather than guess at it. Ask it to reverse-engineer sentence
rhythm, structure, and formatting choices from those examples rather than
be told what your voice is like in adjectives. The mental model: **you're
not asking the AI to be creative, you're asking it to be a pattern-
matching machine that fills a proven structure with fresh input** —
structure first, content second, same as how a human ghostwriter studies
a client's back catalog before writing a single new word.

## Layer 3 — Identity programming

Don't just describe a role ("you are a copywriter"). Give the model an
identity with backstory/framing ("lore") plus the proven frameworks it
should apply — identity + frameworks produces more consistent, less
generic output than a bare role description. This generalizes past
content: the same three-layer stack (business intelligence → channel-
native intelligence → identity) works for sales copy, newsletters, YouTube
scripts, blog posts, and AI-SDR follow-up messages — anywhere you need
output that's specifically *yours*, not generic AI output.

**Concrete contrast, to calibrate how specific "specific" needs to be**:
- Weak: "You are a LinkedIn expert copywriter/ghostwriter." → Wikipedia-
  level generic advice, because it only touches the shallowest, most
  common region of the model's training distribution for that role.
- Strong: "You are a LinkedIn conversion obsessive who spent 3 years
  reverse-engineering lead magnets that get 50,000 responses while others
  get ignored. You discovered LinkedIn psychology runs on different
  triggers than other platforms, and you're borderline maniacal about the
  specific cognitive patterns that make B2B decision-makers stop
  mid-scroll — especially the intersection of professional status anxiety
  and FOMO in [your specific niche]."

The mechanism: a model trained on millions of expert conversations and
case studies holds most of that depth behind specificity, not behind
politeness or clarity of instruction. Giving it *achievements, a
backstory, a narrow obsession, and explicit constraints* (e.g. a hard
word-count cap) is what routes the generation toward that deeper,
narrower knowledge instead of the median "AI content" region — prompting
is less about instruction-clarity and more about *who* inside the model
you're addressing.

**Layer 3 prompts work well as stackable add-ons**, not just base system
prompts: a short "make this a high-converting lead magnet" identity block
can be applied *on top of* content already generated by the base
ghostwriter setup (per the boost/enhancement pattern in the orchestration
section below), narrowing generic output into a specific conversion-
optimized format without re-deriving the whole piece from scratch.

## Scaling past Layer 3: one orchestration system, not N projects

The naive way to apply Layers 1-3 is one Claude Project per content type
(a LinkedIn-thought-leader project, a LinkedIn-lead-magnet project, a
Twitter project, a newsletter project...). This works initially but
creates its own bottleneck at volume: you have to remember which project
to open, manually keep every project's context profiles in sync whenever
you update your ICP or brand voice, and re-paste content between projects
to repurpose it. N projects means N copies of your context to maintain.

**The fix is architectural, not just organizational: collapse to one
project that orchestrates, instead of many projects that each embed an
identity.**

- **One unified cognitive base** — your context profiles (business
  context, ICP, brand voice, product strategy, personal profile) exist
  in exactly one place, in the knowledge base of a single project. Update
  them once; every content type immediately sees the update.
- **Cognitive architectures, not per-project system prompts** — what used
  to be each separate project's system prompt (the identity-based
  ghostwriter prompt, per Layer 3) becomes instead a *knowledge-base file*
  inside the one project, one per content type/platform (LinkedIn thought
  leader, LinkedIn lead magnet, Twitter lead magnet, newsletter, YouTube
  script, etc.). Each is still a full identity+framework prompt, just
  stored as data the orchestrator can select, not as the live system
  prompt.
- **The project's actual system prompt becomes a thin router**, with no
  content identity of its own. Its job is only: identify which knowledge-
  base files a given request needs, extract constraints from the request
  (word count, tone, platform), pull the relevant example/formatting file
  to study, execute against those exact constraints, and never ask
  clarifying questions or guess when a trigger word is ambiguous — do the
  file-selection reasoning internally, then just produce the content.
- **Explicit activation tiers**: (1) a small set of "core" files that are
  *always* loaded regardless of request (business context, ICP, brand
  voice) — the non-negotiable foundation; (2) cognitive-architecture files
  loaded only when their trigger phrase appears in the request (e.g. "make
  a LinkedIn lead magnet post" only loads the LinkedIn-lead-magnet
  cognitive file + its matching example file); (3) optional "enhancement/
  boost" files — small, separately-triggered overlays (e.g. a
  "persuasion amplifier" or "authority builder" JSON) invoked by phrases
  like "make it more conversion-driven" or "build more authority" *after*
  a draft exists, layered on top rather than baked into the base
  generation. Treat these boosts as composable modifiers, not
  replacements — you can stack "dumb it down" and "build more authority"
  in sequence on the same draft.
- **This is what makes true one-input, multi-platform repurposing cheap**:
  because every content type draws from the same unified context, turning
  one podcast/video transcript into a LinkedIn post, a Twitter thread, and
  a newsletter is just invoking three different cognitive-architecture
  files against the same underlying content and context — no manual
  re-pasting of profiles between separate projects.
- **Team scaling payoff**: give every team member (not just
  marketing/content) access to the same orchestrated project. Every
  employee's LLM conversation then starts already knowing the business
  instead of starting from zero in a fresh ChatGPT/Claude tab each time —
  this is the mechanism, not just a nice-to-have, behind teams that seem
  to get dramatically more out of AI than teams issued the same tools with
  no shared context.

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
   data. A purpose-built scraper-plus-analyzer tool (e.g. an MCP connector
   that pulls a Twitter/X account's or a website's recent content and
   returns an already-structured JSON profile — tone, hooks, posting
   patterns, top-performing content, audience/ICP inferred from
   engagement, and for a website its brand DNA: colors, fonts, layout,
   content hierarchy) collapses the scrape→analyze→structure steps into
   one call, and is worth using over raw scraping when available — the
   website-brand-DNA variant is detailed enough to hand directly to a
   website/design builder for a redesign brief, not just for content
   style-matching.
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
- Trigger-word activation: name the profile files so their filenames/topics
  match the words you'd naturally use when asking ("LinkedIn thought
  leadership", "Twitter lead magnet") — a well-organized project activates
  only the relevant subset of files per request instead of dumping
  everything into context every time.
- **Bootstrapping the profile set the first time**: rather than writing
  every context document from scratch, use a "context profile generator"
  — a system-instructions document plus a couple of example/template files
  — as its own small Claude Project. Load that generator project, then
  have a conversation dumping everything you know about your business,
  ICP, and past posts into it; it interviews/organizes that into the
  actual ICP/business/product-strategy/brand-voice documents you then move
  into your real content project's knowledge base. This turns "write four
  structured profile documents" from a blank-page problem into a
  conversation.
- **Only feed it content that already converted or that you explicitly
  want replicated.** Uploading mediocre or non-converting past posts as
  "brand voice" examples trains the system to reproduce mediocrity — curate
  the training examples as carefully as you'd curate a portfolio.
- **Understand the underlying model before trying to push it further.**
  Treating the LLM as a black box and stacking prompt templates you don't
  understand caps how far you can take this — knowing roughly how the
  model actually uses context (why organization, file separation, and
  curation matter mechanically) is what lets you debug or extend the setup
  yourself instead of cargo-culting someone else's prompts.
- **Expected result magnitude, to calibrate expectations**: one previously
  dormant LinkedIn account (25K existing followers, 1-2 likes/post) saw
  roughly a 30x (3,000%) engagement increase within a week of deploying a
  properly-trained context system (business intelligence + platform
  patterns + identity programming, per Layers 1-3 above) — a sign this is
  a step-change technique, not a marginal prompting tweak, when the
  profile documents are done properly.
- This complements [[ai-ops-dependency-audit]] and
  [[ai-agent-system-blueprints]] — those are about *what* systems to build
  in a business; this is the technique for making any one of those AI
  systems sound like the business instead of like generic AI output.
