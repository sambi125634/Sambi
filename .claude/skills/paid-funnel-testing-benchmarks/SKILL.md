---
name: paid-funnel-testing-benchmarks
description: Benchmark ranges for each stage of a cold-traffic paid funnel (CPM, link click-through, opt-in rate, show rate, retention, pitch-to-booking, call show rate, close rate) plus a bottleneck-analysis method and a disciplined test-then-scale protocol (test budget sizing, scaling trigger after consecutive wins). Trigger when the user is launching or diagnosing a webinar/VSL/call funnel, wants to know if a specific funnel-stage number is good or bad, needs to decide a test budget, or wants a repeatable process for turning ad spend tests into a scaling decision. Also trigger on Polish phrasing like "jaki dobry współczynnik zapisu na webinar", "jaki budżet testowy na kampanię", "analiza wąskiego gardła w lejku sprzedażowym".
---

# Cold-traffic funnel benchmarks and testing protocol

## Stage-by-stage benchmark ranges (cold audience, paid traffic)

Use these as a first-pass diagnostic to locate which stage of a funnel is
underperforming, not as guarantees — they vary by vertical and price
point, but are a reasonable starting reference:

| Stage | Metric | Good | Average | Below average |
|---|---|---|---|---|
| Ad delivery | CPM | ~$30-50 | ~$50-80 | $80+ |
| Ad → page | Link click-through rate | ~2%+ | — | well under 2% |
| Page → lead | Opt-in rate | 35-50% | 20-35% | under 20% |
| Overall | Cost per lead | $10-15 | $15-25 | $25-30+ (above ~$30, the funnel likely doesn't pencil out) |
| Lead → live attendee | Show rate (webinar) | ~30%+ | ~20% | 10-15% or below (signals something is broken, not just mediocre) |
| Attendance | Retention to the pitch | 80%+ | — | well under 80% |
| Pitch → booked call | Booking rate | ~30%+ | — | — |
| Booked → call attended | Call show rate | 70%+ | — | — |
| Call → close | Close rate | 35%+ | — | — |

**How to use this table**: don't average these into one "the funnel is
bad" conclusion. Isolate which single stage is most contracted relative
to its benchmark, fix only that stage, re-test, and repeat — a
bottleneck-analysis approach. Fixing a healthy stage further doesn't move
overall throughput; fixing the actual bottleneck does.

## Sizing a test budget

A practical way to size a test rather than guessing: pick a total test
budget that's a small, deliberately-bounded fraction of current monthly
profit — small enough that a total loss wouldn't be financially
damaging, large enough that a win would feel meaningful enough to justify
continuing. Split that total across a fixed number of test runs (e.g. a
handful of weekly webinar/funnel runs) so each individual run has enough
spend behind it to produce a real signal rather than statistically noisy
data from an underfunded test.

**Pre-flight check before committing to a number**: run the proposed
budget through the stage-by-stage benchmark table above using
*conservative* assumptions at every stage (cost per lead, show rate,
retention, booking rate, call show rate, close rate, and your actual
AOV) and see whether the resulting math can plausibly produce a
worthwhile return at all. If conservative assumptions show the proposed
budget is mathematically too small to reveal anything — not enough leads
generated to reach statistical signal, or too small to cover the
occasional bad run — increase the budget or extend the timeline before
running it, rather than spending on a test that can't produce a
meaningful read either way.

**Match test cadence to audience temperature.** A warm-audience funnel
(your own list/existing audience) saturates faster and is typically best
run on a monthly-ish cadence to avoid audience fatigue. A cold-audience
funnel targeting genuinely new people can and should run far more
often — weekly at minimum, and twice a week or more once it's dialed in —
since a new pool of cold prospects exists every cycle. Once a cold funnel
is proven, it can be converted to an always-on, on-demand format (an
"evergreen" webinar/presentation a prospect can watch any time) while
still presenting as a scheduled, live-feeling event to preserve the
urgency that gets people to actually show up.

## Reading the result of a test run

- Expect most single test runs to roughly break even or produce a small
  loss — that's normal and still valuable, because the point of a test
  run is the *diagnostic data* it produces (which stage was weak), not
  necessarily profit on the first attempt.
- A genuinely good result is a return meaningfully above break-even (e.g.
  a 3:1 return) — treat that as the signal to move from testing to
  scaling, not a fluke to repeat cautiously forever.
- **Scaling trigger rule**: require at least two consecutive positive-ROI
  test runs before increasing budget meaningfully — a single good run
  could be variance; two in a row is a much stronger signal the
  combination (offer, messaging, funnel) actually works. Once triggered,
  increase spend deliberately (e.g. roughly doubling or more per step)
  rather than inching up, so you find the real scale ceiling faster.

## The two-lever mental model for a call-funnel business

For any business whose funnel ends in a booked sales call, nearly every
operational problem reduces to one of exactly two levers, which makes
triage much faster:

1. **Filling the calendar** — generating enough qualified booked calls
   (traffic, messaging, funnel conversion, show-rate).
2. **Sales capacity** — having enough trained closers to handle the
   calendar being filled.

The growth loop is simply: scale spend to fill calendars past current
capacity → hire/train more closers → fill their calendars too → repeat.
When diagnosing a stuck business, first classify which of the two levers
a given symptom actually belongs to (a "we don't have enough good leads"
problem is lever 1; a "reps are maxed out and follow-up is slipping"
problem is lever 2) before looking for a more exotic explanation — most
day-to-day friction is a sub-symptom of whichever lever is currently
behind.

## Execution discipline while testing

- **Give a new funnel/channel a full commitment window (roughly a month
  of genuine, consistent effort) before judging it**, not just one or two
  attempts. Anything brand new lacks the operational muscle memory to run
  efficiently yet, which makes early results look worse than the
  channel's real potential — killing a channel after one weak run
  conflates "this doesn't work" with "we haven't practiced this yet."
- **Run one new growth bet at a time.** Launching several new channels or
  funnel types simultaneously compounds the learning curve and the
  perceived difficulty of all of them at once, making it hard to tell
  which change caused which result. Pick the option you have the highest
  confidence in first, get it dialed in and routine, then add the next
  one.
- Once a funnel is profitable and stable, that's the point to diversify
  into a second funnel type or audience — not before, and not by
  replacing the working one, but by adding alongside it.
- **A single funnel's efficiency ceiling tends to fall as absolute scale
  rises**, even without any obvious external cause — the same underlying
  audience pool simply gets more expensive to keep drawing from at higher
  volumes (see [[meta-ads-scaling-mechanics]]'s finite-vs-replenishing
  messaging-pocket model for why). At meaningful scale, treat rising
  cost-per-result on a previously-efficient funnel as an expected signal
  to add a genuinely different funnel structure or audience source, not
  just evidence that the current funnel needs fixing.
- **Leaving a working funnel untouched is sometimes correct, not
  negligent.** If a funnel or ad asset is still converting acceptably,
  it's fine to deprioritize testing/optimizing it further while attention
  goes elsewhere (new channels, new offers) — a funnel doesn't need
  constant iteration to keep producing results, and "we haven't touched
  this in months and it still works" is a legitimate state, not
  automatically a missed opportunity.
