---
name: ai-ops-dependency-audit
description: Diagnose where a company's operations still depend on a single founder/leader and design an AI operating layer (per-department AI systems connected to existing tools, with clear decision-ownership and escalation rules) to remove that bottleneck. Trigger when the user wants to audit founder/leadership bottlenecks, reduce founder hours, build "AI systems" or an "AI operating layer" for a business, decide where to add AI/automation in a company, or design SOPs that both a team and an AI agent can execute. Also trigger on Polish phrasing like "gdzie firma zależy ode mnie", "audyt zależności od założyciela", "system AI dla firmy".
---

# AI operations dependency audit & system design

Core idea: most companies don't have a software problem — they have already-good
tools (CRM, Slack, email, accounting, calendar, call recorder, project
management) whose information is siloed. The founder/leader becomes the single
point of contact that stitches these tools together in their head. The fix is
not one giant AI that "runs the company" — it's several narrow AI systems, one
per business function, each wired into the existing tools and taught the
company's actual decision rules.

## Step 1 — Run the dependency audit

Before proposing any automation, answer these questions (interview the
founder/leader, or reverse-engineer from their calendar/inbox/Slack history):

1. What does your team keep asking you that they should already know?
2. What did you hire someone to own that still comes back to you every time?
3. What kind of work reaches you at night / outside hours?
4. Where does the company visibly slow down when you're unavailable?
5. What % of revenue depends on your personal availability / involvement?
6. What do you personally check every time before trusting a task is done
   (QA checks you perform manually)?
7. Which client promises are most likely to get lost between tools/people?
8. Which report requires someone to manually collect info from several
   places?
9. What would visibly change if this were fixed — more sales calls, faster
   delivery, better margins, fewer escalations? (This tells you what to build
   first — let the answer come from data, not from "the fancy AI tool of the
   month".)

Don't start with "where should I add AI?" — that produces random automations
nobody needed that collect dust in 3 months. Start with "where does the
company still depend on me?" and let the audit answer point at the first
system to build.

## Step 2 — Design per-function systems, not one mega-AI

Split the operating layer by business function (adapt to the company's
actual functions, these four are the common ones):

- **Sales** — calls get reviewed, next steps get an owner, proposals get
  drafted from the conversation, pricing/follow-ups stay visible until closed.
- **Delivery** — every client conversation starts with the latest info;
  at-risk work surfaces before the client has to chase; status updates are
  generated from what actually happened, not from memory.
- **Finance** — payments, invoices, costs, subscriptions, margins stay
  current; anything unusual routes back to whoever manages the money.
- **Operations** — routine work keeps moving on its own; only the small
  number of decisions that genuinely need leadership get surfaced.

## Step 3 — Give the AI two things, not just data access

1. **Access**: connect the tools the work already lives in — calls,
   messages, invoices, documents, task owners, current work status,
   customers. Don't force a 6-month tool migration; wire into what exists.
2. **Decision context**: the AI also needs the company's actual rules —
   what the team can decide without leadership, what changes require
   escalation (pricing, scope, contract terms, promises to a client), what
   missing information should halt a task, and who owns the next step when
   something needs routing. Access without decision context just moves data
   around; it doesn't remove the founder as bottleneck.

## Step 4 — Map one process end-to-end before building

For the first function you pick (from Step 1's answer), map the work from
start to finish and answer, per step:

- Who starts it?
- What information is needed to do it well?
- What does "good" output look like?
- Who owns this specific task?
- When can the team act without asking anyone?
- When must a leader/founder decide instead?
- What are the guardrails — what should stop the work entirely if missing?

Write this as clear, executable instructions/SOPs — not an 80-page policy
doc nobody reads. The output should be something both a human teammate and
an AI agent can follow directly while work is happening.

## Step 5 — Ship narrow, watch, expand

Start with one function. Let the AI system watch that function's work
24/7, handle the routine parts, and surface only the decisions that need a
human. Fix what breaks. Only then expand to the next function. The
commercial/pricing/final decisions stay human — the system's job is to
remove the busywork around gathering context and routing information, not
to automate judgment itself.

## What "success" looks like (calibrate expectations, not a guarantee)

Framed correctly, this shows up as: founder/leader hours dropping
substantially (one case: 60-70h/week → 30h/week), % of work completing
without being routed through the founder rising sharply, median response
time to clients dropping from ~24h to minutes, and delivery reviews
becoming an exception-handling job instead of a full-time one. These are
outcome signals to track, not universal numbers to promise.
