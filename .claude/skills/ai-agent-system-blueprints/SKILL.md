---
name: ai-agent-system-blueprints
description: Concrete architecture blueprints for five enterprise AI agent systems — ad creative intelligence, finance/board-report automation, sales outbound intelligence, an enterprise AI-adoption dashboard, and product/solution-matching intelligence for complex catalogs — covering their inputs, pipeline steps, and output artifacts. Trigger when the user wants to design or scope an AI system for marketing creative testing, automated financial reporting, personalized sales outbound at scale, tracking AI agent ROI/adoption across an organization, or matching the right product/service from a large catalog to a specific enterprise prospect. Also trigger on Polish phrasing like "system do generowania kreacji reklamowych AI", "automatyzacja raportów finansowych AI", "system do outboundu sprzedażowego AI", "dashboard adopcji AI w firmie", "system dopasowania produktu do klienta enterprise".
---

# AI agent system blueprints (four enterprise patterns)

Four concrete, already-deployed system architectures. Use these as
starting blueprints when scoping a similar build — each lists what data
it ingests, what the pipeline actually does step by step, and what it
outputs.

## Blueprint 1 — Ad creative intelligence platform (marketing)

**Problem it solves**: teams spend large ad budgets testing creative
blind, with no visibility into what's proven to convert (their own history
or competitors').

**Pipeline**:
1. Track all internally-running ads (Facebook/Instagram/TikTok) plus
   competitor ads continuously.
2. Analyze the corpus to extract winning patterns: hooks, visual angles,
   emotional triggers.
3. Feed the AI full brand context: persona, product line, current offers/
   promotions, brand colors/fonts/style.
4. Auto-generate platform-ready creative from proven patterns: static
   images (in multiple aspect ratios, e.g. 9x16 for Stories), AI UGC
   avatars, product-animation video, short (5-8s) B-roll/demo clips.

**Output**: dozens of ad variations per day (vs. ~2/week manually) across
image, text-overlay, and video formats, replacing paid competitive-
intelligence subscriptions.

**Generation engine detail**: treat creative generation as an entropy/
combinatorics system, not a single prompt. Maintain explicit dimensions to
sample from and recombine: campaign type (problem-agitate-solution,
lifestyle, product-hero), persona, emotional tone, visual angle,
setting/lighting, plus a product database (colors, variants, price points)
and a live offer database (current promo, e.g. "buy 2 get 1 free",
Black Friday pricing) so text overlays stay accurate without manual
updates. Constrain the sampling space to what the actual audience
resonates with (e.g. common pet breeds for a pet-product brand) rather
than generating uniformly across every possible value — an unconstrained
system wastes generation budget on combinations nobody buys. Once a still
is approved, auto-derive format variants (e.g. a square hero shot →
9:16 Stories crop) instead of regenerating from scratch. For video, don't
aim for full 30-40s ads — current image/video models are strongest at
5-8s B-roll/A-roll product clips; generate a library of these short clips
and let a human editor assemble the final cut.

## Blueprint 2 — Finance / board-report automation

**Problem it solves**: finance teams spend tens of hours/month manually
building board earnings reports — pulling data, building charts,
formatting — time not spent on actual strategic analysis.

**Pipeline**:
1. Ingest raw financial data: revenue, expenses, customer metrics.
2. Auto-generate the standard chart set: revenue vs. forecast, expense
   breakdown, customer acquisition metrics.
3. Beyond charts — write the analysis: automated variance deep-dive (root
   cause of what changed and why), strategic market insights and
   competitive positioning, updated forecast + assumptions, strategic
   priorities, risk assessment and mitigation, appendix/reference data.
4. Assemble into a complete, presentation-ready deck: executive summary →
   charts → written analysis → recommendations.

**Output**: a board-ready deck generated in minutes instead of tens of
hours, freeing the finance lead to work on strategy rather than
formatting. Same pipeline generalizes to investor pitch decks and
stakeholder-specific reports.

## Blueprint 3 — Sales outbound intelligence (deep personalization at scale)

**Problem it solves**: manual prospect research doesn't scale; generic
outreach gets ignored; SDR headcount is expensive and inconsistent.

**Pipeline**:
1. **Lead sourcing** — two modes: (a) on-demand structured query against a
   B2B data provider (Apollo/Explorium/Cognism-style) with filters
   (geography, title, headcount, revenue, industry, tech stack), or
   (b) continuous signal monitoring across a target company list (new
   hires, funding rounds, expansions, tech-stack changes) that triggers
   research automatically when a signal fires.
2. **Company research** — revenue range, employee count, industry code,
   recent news (via a search/answer API), latest quarterly results, key
   challenges *reframed specifically in terms of what your own
   offer solves* (train the model on your company's positioning, not
   generic pain points), competitors, timing triggers, current tech
   stack.
3. **Decision-maker research** — don't stop at a name: scrape their public
   history (career path, education, skills), analyze their content/
   network for what they post about and care about, and find genuine
   alignment topics between them and whoever is sending the outreach
   (their own background/expertise).
4. **Message generation with a self-critique loop** — one model drafts the
   outreach angle and copy; a second model audits it against a quality
   bar; if it fails, it goes back with feedback for revision. This
   draft→critique→revise loop is the mechanism that keeps personalization
   from reading generic.
5. **Follow-up sequencing** — 4-6 follow-ups over a set cadence (e.g. every
   7 days), each pulling a *different* relevant case study from a vector
   database of your case studies/proof points, matched to the specific
   research gathered on that prospect — never a bare "just following up."
6. **Multi-channel send + CRM sync** — email and LinkedIn, checked against
   CRM (Salesforce/HubSpot/GoHighLevel) to avoid duplicate/already-contacted
   leads, with an ICP-fit score used to prioritize send order.
7. **Email verification before send** — a scraped/enriched email is not
   guaranteed live: someone who changed jobs often still shows an email
   tied to their *previous* employer's domain, which will bounce and can
   also degrade your sending domain's deliverability/reputation score.
   Run every address through a verification tool (e.g. Anymail Finder)
   before it enters a send queue, not after bounces show up in analytics.

Typical tool stack for this pipeline: Explorium/Apollo/LinkedIn Sales
Navigator for company+contact data, Perplexity for market intelligence/
recent news, Apify for LinkedIn profile/activity scraping, an email
verifier for deliverability, and a vector database over your own case
studies/proof points for the follow-up personalization in step 5.
7. **Reply handling** — replies are logged to CRM automatically and routed
   to a human for anything requiring judgment.

**Output**: dozens of qualified sales calls per month replacing multiple
SDR hires, running continuously across time zones/languages/markets.
Generalizes to e.g. private-equity portfolio monitoring (watch for
C-suite changes across portfolio companies, auto-generate a pitch deck
tailored to the new executive's background).

## Blueprint 4 — Enterprise AI-adoption dashboard

**Problem it solves**: leadership invests heavily in AI systems but can't
answer "is it working" — no visibility into which agents are used, by
whom, how often, or with what impact.

**Pipeline / what it tracks**:
- Every AI agent deployed org-wide, in real time: count active, deployment
  velocity (new agents shipped per period), total automated tasks
  completed.
- Adoption broken down by department/practice area and by geography —
  surfaces which teams are actually using what's been built.
- Per-agent detail: what each one actually does and its measurable output
  (e.g. "monitors C-suite changes across N portfolio companies and
  auto-generates a pitch deck on trigger").
- Weekly operational summary and full deployment timeline across agents.

**Output**: a live answer to "are we ahead or behind on AI," and the basis
for a build/kill decision rule — double down on high-usage agents, kill or
diagnose adoption failure on idle ones. This is the correct way to measure
AI ROI at enterprise scale: usage/adoption metrics on a dashboard, not
anecdotes.

## Blueprint 5 — Product/solution-matching intelligence (complex catalogs)

**Problem it solves**: enterprise sellers with large, complex catalogs
(100-200+ SKUs/services/API offerings) can't reliably match the right
offering to a given prospect — even senior sales engineers guess. This is
a different problem from Blueprint 3's outreach personalization: the hard
part here isn't writing a compelling message, it's computing *which
product fits this specific prospect's operational reality* at all.

**Pipeline**:
1. **Lead acquisition at low cost** — scrape via a pay-per-use actor
   platform (e.g. an Apollo-scraping Apify actor) rather than a full CRM/
   data-provider seat when volume and unit economics matter; cap batch
   size (e.g. 200 records) so downstream processing stays stable.
2. **Dedup/validate against CRM** before spending research budget on a
   contact/company already known.
3. **Research at the company level, not individual level**, for enterprise
   sales with complex catalogs — surface-level individual personalization
   ("saw your LinkedIn post") doesn't move sophisticated enterprise buyers
   the way it does in Blueprint 3's outbound context; what matters is
   operational fit: manufacturing capabilities, partnership structure,
   funding stage, regulatory environment, technology stack, competitive
   position.
4. **Guided deep research, not a bare question** — a research prompt
   (e.g. run through a research-capable model/API) needs explicit
   guidance on *where* to look (investor relations pages, regulatory
   filings, industry-specific publications) and *what dimensions* to
   extract, not just "tell me if they're funded." The more sophisticated
   the classification, the more the research strategy itself has to be
   specified in the prompt.
5. **Define classification dimensions collaboratively with the client** —
   these are not generic; they encode that specific business's sales
   logic (e.g. a biotech client's dimensions: primary/secondary molecular
   modality, development stage, company type, manufacturing signals). This
   step requires an actual conversation with the client's sales team
   about how they currently reason about fit — it's the proprietary part
   of the system, not a template.
6. **Structure raw research into a consistent schema via a prompt chain**
   — scrape data → enrich via deep research → a separate structuring pass
   converts free-text research into the fixed JSON schema (the
   classification dimensions from step 5) that the rest of the pipeline
   and any dashboard/CRM view depends on.
7. **Attach a confidence score to every classification** and set a
   threshold below which a record is filtered out of outreach entirely —
   never send derived recommendations at low confidence; this is a hard
   gate, not a soft signal.
8. **Generate the final product recommendation with rationale** — a
   dedicated prompt combines the structured prospect profile with your
   own product/service catalog context and outputs both the recommended
   offering *and* the reasoning, so a sales rep deep into a long enterprise
   sales cycle (calls 3, 4, 5+) has a durable justification to reference,
   not just a black-box suggestion.
9. **Route by operational metadata** — e.g. match territory/geography to
   the correct account executive's signature and sending address; match
   funding status to campaign aggressiveness. Small, mechanical rules, but
   they're what makes the system fit the client's actual sales SOPs
   instead of being a generic bolt-on.

**Output**: for each prospect company, a structured profile (funding
status, territory, business-fit dimensions), a confidence-scored product
recommendation, and a written rationale — the kind of enterprise-sales
research judgment that doesn't scale by hiring more sales engineers.
Generalizes to any vertical with a large, non-obvious product/service
catalog (SaaS with many API products, manufacturing, professional
services), not just biotech.

## When to use which

Pick the blueprint that matches the function under pressure (marketing
creative velocity → Blueprint 1, finance reporting cycle time →
Blueprint 2, outbound/SDR cost and inconsistency → Blueprint 3,
"prove AI is working" from leadership → Blueprint 4, "which of our many
products/services should we even pitch this prospect" → Blueprint 5).
These compose: a company can run several at once per [[ai-ops-dependency-audit]]'s
per-function design principle.
