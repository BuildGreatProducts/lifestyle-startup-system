---
kind: curated
last-reviewed: 2026-11-03
---

# Measurement

The minimum setup that makes every "Working =" and "Win =" line a number the member can actually read, and tells them which channel produced it. It goes in as the first actions of Strategy, before any channel starts — about 30 minutes. An untagged link is a win nobody can repeat.

## Contents

- [The funnel and what counts](#the-funnel-and-what-counts)
- [The 30-minute setup](#the-30-minute-setup)
- [Tagged links](#tagged-links)
- [Attribution: keep it cheap](#attribution-keep-it-cheap)
- [The number to read, by channel](#the-number-to-read-by-channel)
- [Failure patterns](#failure-patterns)

## The funnel and what counts

**Reach → Click → Signup → Activated → Paid.** Set every bar as far down as the member can measure.

| Stage | Means | Weight |
|---|---|---|
| Reach | Views, impressions, opens | A leading signal only — never a "Working =" line |
| Click | A tagged click to the product | Proves the hook |
| Signup | An account, trial, booking request or enquiry | A real lead |
| Activated | Reached the magic moment (from `docs/5-FLOWS.md`) | Predicts who stays |
| Paid | A payment | The number that never lies |

"100K views" is a reach result; "20 paying users from one community in 30 days" is a paid one. For a productized service, signup is a booked call and paid is a signed client; for a digital product, signup is often skipped — click to purchase.

## The 30-minute setup

One of each layer. Tools here are examples of the kind, not a recommendation — check what the member already has, and pick current options with [ai-distribution-tools.md](ai-distribution-tools.md).

| Layer | Example (free tier) | Answers |
|---|---|---|
| Web analytics | GA4, Plausible | Which channel and tagged link sent the visit |
| Product analytics (products with screens) | PostHog | Whether signups reach the magic moment |
| Payments | The Stripe, Lemon Squeezy, RevenueCat or store dashboard | Real revenue |
| "How did you hear about us?" | One question at signup, checkout or the booking form | What tags miss: word of mouth, "saw you on TikTok then googled you" |
| Store console (native channel) | The store's own analytics | Impressions → listing views → installs, ratings |
| The tracker | The table in `docs/9-GO-TO-MARKET.md` | What worked and what was decided |

Escalate beyond this only when volume earns it.

## Tagged links

Every link the member posts, sends or pays for carries UTM tags and points at the feature or magic moment, never the homepage.

| Tag | Answers | Example |
|---|---|---|
| `utm_source` | Which platform | `reddit`, `tiktok`, `newsletter-swap` |
| `utm_medium` | Which kind of channel | `community`, `short-form`, `outreach`, `ads` |
| `utm_campaign` | Which channel action or experiment | `founder-story-post`, `ltd-launch` |
| `utm_content` | Which variation | `hook-v1`, `story-v2` |
| `utm_term` | The keyword (search and ads only) | `invoice-template-for-photographers` |

Example: `yoursite.com/record?utm_source=reddit&utm_medium=community&utm_campaign=founder-story-post&utm_content=v1`

Keep one convention (lowercase, hyphens, the same source names every time) in a note or sheet. A creator or partner gets a unique code or link instead.

## Attribution: keep it cheap

Two tools cover a first product: **tags** on everything the member controls, and the **"How did you hear about us?"** question for everything they don't — reconciled weekly on review day. First touch (what first brought them) is enough to decide where to spend more. A multi-touch model before 100 customers is procrastination dressed as rigour.

## The number to read, by channel

| Channel | The number | Read it in |
|---|---|---|
| Short-form | 3-second retention → link clicks → tagged signups | The platform's analytics plus the tagged link in bio |
| Long-form | Watch time or reads → tagged signups | Platform analytics; Search Console for videos and posts that rank |
| Communities | Tagged signups per post | One tag per community — upvotes are a proxy, not the metric |
| Search | Impressions → clicks → position; named in AI answers | Google Search Console; asking the AI engines the category question |
| Native channel | Listing views → installs or sales; ratings | The store console |
| Launch platforms | Launch-day tagged signups; backlinks | The tagged launch link; the 48-hour spike |
| Outreach | Reply → call → close rate | The sending tool or a simple sheet |
| Creators | Installs or sales per creator → cost per install | A code or link per creator |
| Partnerships | Signups per partner | A code or link per partner |
| Email | Opens and clicks → tagged conversions and reactivations | The email tool plus tagged links |
| Referrals | Referred signups as a share of new | Referral codes; the affiliate dashboard |
| Ads | Cost per customer, and whether those customers stay | The ad dashboard **and** your own analytics — platforms over-report their own results |

## Failure patterns

- **The Untagged Link.** The result is real but unrepeatable.
- **The Vanity Metric.** Reach and likes instead of signups, activation and revenue.
- **The Homepage Link.** Tagged traffic dropped on the homepage, so a click means little.
- **Attribution Obsession.** A model before there are customers to model.
- **Measuring Everything.** Fifty dashboards nobody reads. The funnel and one north-star number.
- **Scaling on Guesses.** Scale reads the tracker; a tracker of guesses automates a guess. Every logged result is a measured number with its source.
