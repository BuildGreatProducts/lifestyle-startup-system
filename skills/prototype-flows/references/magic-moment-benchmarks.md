---
kind: curated
last-reviewed: 2026-10-01
---

# Magic moment benchmarks

The magic moment is the action that separates customers who stay from customers who leave. Before there's retention data it's a hypothesis grounded in named comparables, so the flows doc says so. Use this file to pick the aha shape, place it in the shape's medium, set a time-to-aha target, and calibrate three candidates. The shapes are durable; the figures and named examples are not — **figures last reviewed October 2026**: re-verify any number with a web search, and note its source, before quoting it to the member.

## Contents

- [The seven aha shapes](#the-seven-aha-shapes)
- [Where the moment happens, by product shape](#where-the-moment-happens-by-product-shape)
- [Benchmarks](#benchmarks)
- [Documented aha moments by category](#documented-aha-moments-by-category)
- [Writing a candidate](#writing-a-candidate)
- [Why candidates fail](#why-candidates-fail)

## The seven aha shapes

Every product rhymes with one or two of these. Name which, and why. The three candidates should come from **different** shapes where the product allows — three flavours of one idea isn't a choice.

| Aha shape | What happens | Comparables | Fits |
|---|---|---|---|
| **Volume-of-use** | A usage threshold flips "trying" to "living in it" | Slack 2,000 messages per team; Facebook 7 friends in 10 days; Twitter 30 follows | Habit, social, communication, content |
| **Collaboration trigger** | Sharing or inviting reveals multi-player value | Dropbox first file uploaded *and shared*; Notion first page shared; Calendly first link sent | Collaborative tools, sharing-driven products, marketplaces |
| **First-output** | The product makes a real artifact the user keeps or builds on | Lovable first working app from a prompt; Cursor first completion accepted; Granola first meeting transcribed | AI products, generators, creative tools |
| **Time-saved** | Minutes or hours become seconds | Superhuman Inbox Zero in session one; Calendly first meeting booked without email; Stripe first test payment in 7 lines | Productivity, infrastructure, replacement-for-X |
| **Personalization-reveal** | Their input comes back as something that feels built for them | Cal AI plan at the end of the quiz; Spotify Discover Weekly; Headway reading queue | Health, wellness, discovery, recommendations |
| **First-win** | One outcome they can point to | Duolingo first lesson and streak; Strava first run logged; Whoop first sleep score | Goals, tracking, fitness, learning |
| **Pre-signup** | Real value before an account; signup becomes "save what I made" | Lovable's homepage prompt box; Perplexity search with no login; Airbnb browse without login | High-friction signups, viral utilities, strong demos |

Speed bias: if a candidate lands on day 3, ask whether a variant could land on day 1, and whether day 1 could move before signup.

## Where the moment happens, by product shape

| Shape | What the magic moment usually looks like | Positions to use |
|---|---|---|
| web-app, mobile-app, desktop-app, browser-extension | An in-product event on a screen: the first output, reveal or win. Mobile must land in the first session; a browser extension's lands on the host site, not in its popup; a desktop app's is often automatic, while the user isn't looking | pre-signup / first 60 seconds / first session / day 1 / day 7 |
| website | The first visit that delivers what the visitor came for, then the return visit or subscription | first visit / first return / first issue |
| digital-product | The first downloaded asset in use on their own material: the template filled with their data, the preset on their photo, lesson one's result | purchase / first open / first win / day 3 |
| productized-service | The first deliverable in the client's hands, ideally before the first invoice is due ("first draft in your inbox within 48 hours") | booking / intake / first delivery / renewal |
| agent-skill, agent-plugin | The first agent output on the member's own work that's clearly better than the agent without it — best shown as a before/after on the same request | pre-install / first command / first session / day 7 |
| mcp-server | The first tool call that returns the customer's real data and lets the agent act on it ("it just answered from my CRM") | connect / first prompt / first session |
| chat-assistant | The first answer specific to their situation where a general chatbot would be generic | first message / first session |
| developer-tool | The first successful call or command with a meaningful response from their own input, in their own environment — not hello-world. Name the time-to-first-call | signup / first call / first integration |

For screenless shapes, the metric comes from what the shape can measure — install-to-first-run rate, first tool call success, download-to-first-open, booking-to-first-delivery time. Name the instrument when there's no product analytics.

## Benchmarks

| Benchmark | Figure | Source |
|---|---|---|
| Time-to-aha, B2B SaaS | median ~1 day 12 hours; top quartile under 5 minutes | Userpilot time-to-value report — verify the current edition |
| Time-to-aha target, AI products | under 60 seconds | Lovable's first-app-from-prompt flow as the reference point — verify |
| Time-to-aha target, mobile | under 5 minutes, inside the first session | working target; no recorded source |
| Product-tour length | 3-step tours complete at ~72%; 7-step at ~16% | Chameleon benchmark (other editions report ~66% for 3-step) |
| Slack threshold | 2,000 messages per team → 93% of those teams retained | Stewart Butterfield, widely cited by Reforge |
| Facebook threshold | 7 friends in 10 days | Chamath Palihapitiya, Facebook growth team |
| Early aha and paid conversion | aha within 48 hours ≈ 3.4× more likely to convert | no primary source traced — directional only, don't quote as fact |

The direction holds even when the figures move: the bar for time-to-aha keeps dropping, and an AI-augmented incumbent in most categories now reaches it faster than the pre-AI norm. Research that incumbent live.

## Documented aha moments by category

Publicly documented or widely attributed. Refresh with live research for the member's category.

- **Consumer / mobile** — Snap: 3 snaps to 3 friends in week one. WhatsApp: first message sent and replied to. Duolingo: first lesson, streak started. Cal AI: plan revealed at the end of the quiz. Spotify: guest play, then Discover Weekly in week one.
- **B2B SaaS** — Dropbox: the share, not the upload. Linear: first issue created with a keyboard shortcut (the speed reveal). Superhuman: Inbox Zero in a concierge first session. HubSpot: segmented by job — sales reps log a deal, marketers build a form.
- **AI products** — Lovable: working app in ~60 seconds, pre-signup. Cursor: AI line accepted in the user's own repo. Granola: first meeting transcribed with no bot in the call. Perplexity: first cited answer, no login.
- **Marketplaces** — Airbnb: first booking (for new hosts, a booking inquiry within two weeks). Etsy: first sale for sellers, first favourite for buyers. Uber: first ride within 5 minutes of request.
- **Productized services** — Designjoy: first deliverable back in under 48 hours. Penji, ManyPixels: first request fulfilled inside the SLA on day one.

Frameworks worth naming to the member: Sean Ellis ("the moment the utility really clicks", paired with the 40% "very disappointed" PMF survey); Reforge's setup → aha → habit, where the aha is the wedge between the setup and the habit.

## Writing a candidate

Each candidate gets seven fields, as bullets:

- **Action** — what the user does, 5–10 words.
- **Wow** — what they see, feel or unlock in that instant.
- **Where** — the earliest position it can realistically happen, not where it's convenient to build.
- **Time-to-aha** — a concrete bound ("under 60 seconds from landing on the homepage"), never "as fast as possible".
- **Comparable evidence** — at least two named products whose documented aha rhymes with it.
- **Risk** — what could go wrong. No named risk means it hasn't been pressure-tested.
- **Metric** — a threshold the shape can measure ("40% of new accounts publish a first report within 10 minutes").

Pick the primary on **speed** first (fastest from first contact), then **evidence** (strongest comparables in the same category), then **fit** (closest to the offer's mechanism in `2-OFFER.md`). The other two stay as alternates if the primary fails its test in 4–6 weeks.

> Good: "The user pastes last month's invoices and sees which three clients are paying late, ranked by days overdue — under 90 seconds from signup. Comparables: Granola (first output from their own meeting), Stripe (time-saved on their own data). Metric: 35% of signups see the ranked list in session one."
>
> Bad: "The user gets value from the dashboard and feels more in control of their finances." — no action, no position, no number, no comparable.

## Why candidates fail

- **The trendy aha.** "First AI output" is the default for AI products, but if the value is reliability over weeks, the real aha is on day 3 — say so and design for it.
- **The setup moment mistaken for the aha.** Connecting an account or finishing a profile is setup. The aha is what that setup pays for.
- **The upload, not the share.** Dropbox's lesson: the action that reveals *why* the product matters is often one step past the obvious one.
- **The imagined screen.** A chat assistant's or agent skill's moment drawn as a dashboard. Place it in the medium the customer actually uses.
- **Unmeasurable.** "Users feel delighted." If it can't be counted in analytics, logs, a store dashboard or delivery records, it can't be tested.
