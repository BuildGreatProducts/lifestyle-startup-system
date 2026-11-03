---
kind: curated
last-reviewed: 2026-10-01
---

# Landing page best practice

How to design the front-door page for any shape with a web presence: the pattern to pick, the sections in order, the copy budgets, and what kills conversion. A landing page has one job — turn a stranger who clicked a link into someone who takes the next step — and most visitors decide in under 7 seconds whether to scroll or close. **Figures last reviewed October 2026**; they come from vendor and practitioner studies named beside each. Re-verify a figure with a web search before quoting it to the member.

## Contents

- [Numbers that set the stakes](#numbers-that-set-the-stakes)
- [Pick the pattern](#pick-the-pattern)
- [The CTA and hero visual by shape](#the-cta-and-hero-visual-by-shape)
- [The sections, in order](#the-sections-in-order)
- [The hero gets extra scrutiny](#the-hero-gets-extra-scrutiny)
- [Worked heroes](#worked-heroes)
- [Why landing pages fail](#why-landing-pages-fail)
- [What good looks like](#what-good-looks-like)

## Numbers that set the stakes

| Metric | Number | Source |
|---|---|---|
| Single-goal page vs multi-CTA | 13.5% vs 10.5% conversion | Landing Page Conversion Study 2026 (2,000 pages) |
| Above-fold CTA + ~10-word value-prop headline | +96% engagement, 11.3% session-to-conversion | Hotjar 2026 |
| Sticky CTA | +11% (with an above-fold CTA too: +12% — sticky absorbs most of it) | LP Study 2026 |
| First-person CTA ("Start my trial") vs second-person | +90% CTR | ContentVerve |
| Winning CTA length | 3.4 words on average | AdEvolver (90 CTAs) |
| Video hero vs static hero (B2B SaaS) | −7% — video lost | LP Study 2026 |
| Best-in-class heroes with social proof above the fold | 81% (vs 41% baseline) | LP Study 2026 |
| Best-in-class heroes with a risk reducer near the CTA | 65% (vs 42% baseline) | LP Study 2026 |
| Outcome + timeframe headline vs feature-led | up to +67.8% | KlientBoost |
| Pricing hidden behind "Contact us" for deals under ~$25K/year | 90%+ conversion loss | practitioner estimate — no primary study traced |
| B2B SaaS visitor-to-lead | average 1.5–2.5%; top 10% at 8–15% | SaaS Hero 2026 |

## Pick the pattern

Stop at the first yes.

1. **Can a visitor feel the product in 30 seconds in the browser?** → **Try-before-signup hero** (Lovable, v0). The hero is a working input; signup is "save what you just made".
2. **Is it an API, SDK or CLI?** → **Code-in-the-hero** (Stripe, Resend). Runnable code with language tabs and a copy button.
3. **Is it collaborative or workflow software with a UI?** → **Product-visual hero** (Linear, Notion). The real product, or a loop under 4 seconds showing it working.
4. **Is the value the AI's output on the user's own data, sold to consumers?** → **Outcome-first hero** (Cal AI, Headway). The outcome they want; store badges for an app.
5. **Is it a productized service?** → **Gallery + price hero** (Designjoy). Delivered work, the price on the page, self-serve checkout or booking.
6. **Enterprise or sales-led?** → **Customer-logo hero**, "Book a demo". Rarely right for a first product; push back.

Stuck: product-visual if there's a UI, outcome-first if not.

## The CTA and hero visual by shape

One CTA, the same words everywhere — header, hero, sticky bar, final block. Where the CTA leaves the page (a store, a booking calendar, checkout), name the destination so the hand-off screen's copy matches.

| Shape | Primary CTA (first person where it isn't a badge) | Hero visual |
|---|---|---|
| web-app | "Start my free trial" / "Try it free" | the product working, or a try-before-signup input |
| mobile-app | the official App Store / Google Play badges | the app in a phone frame on the magic moment |
| desktop-app | "Download for Mac" (detect the OS, link the others) | the app window mid-task |
| browser-extension | "Add to Chrome" (detect the browser; the store's own wording) | the extension working on a real host page |
| agent-plugin, agent-skill | "Install the plugin" + the copy-paste install command | a terminal or chat frame showing the first output |
| mcp-server | "Connect <product>" + the install or config snippet per client | a chat frame with one tool call and its result |
| chat-assistant | "Start chatting" / "Add to Slack" | a real conversation |
| developer-tool | "Get my API key" or the install command | a working code sample |
| productized-service | "Book my call" / "Start my project" | the deliverable the client receives |
| website | "Subscribe" / "Browse the directory" | the content itself |
| digital-product | "Get it for $<price>" | the inside of the product, in use |

An install command is the CTA: it must be copy-paste correct, with a copy button.

## The sections, in order

Six to eight sections usually beat eleven; cut any section that has no job. Each has a goal, exact copy, a visual, what it proves, and its drop-off risk.

| # | Section | Job and budget | Pass when |
|---|---|---|---|
| 1 | **Header** | Logo, ≤5 nav links (Pricing among them), the CTA | Sticky; header CTA = hero CTA |
| 2 | **Hero** | Headline ≤12 words (aim ~10), one-sentence sub, 3–5-word CTA, demonstrative visual, one proof fragment | A stranger can say what it does from the headline alone |
| 3 | **Proof bar** | 5–8 real logos, same weight, no "Trusted by" tagline — or a rating with its count and source | Visible at the fold on a 1366×768 screen; omit until real |
| 4 | **Problem** | The pain in the customer's own words, with a cost (hours, money, missed chances) | Uses verbatim customer language from `2-OFFER.md` |
| 5 | **How it works** | Three steps, ~5-word headline + ≤20 words each, a visual fragment per step | The visitor can mentally simulate using it |
| 6 | **Benefits** | ≤6 blocks, benefit-led headlines ("Know the moment a client churns", not "Slack integration") | No block starts with the product's name |
| 7 | **Deep proof** | ≥3 named results with a number each; rating + count + source above a repeated CTA | Every claim is real |
| 8 | **Pricing** | Mirrors `2-OFFER.md` exactly — plans, prices, inclusions, the plan it steers buyers to highlighted, annual/monthly toggle if both exist | No tier the offer doesn't have |
| 9 | **FAQ** | 4–6 real objections: plan changes, what happens at trial end, refunds, data export, the guarantee | Each answer is 1–2 sentences |
| 10 | **Final CTA** | Large headline, the same CTA, one low-friction alternative (newsletter, demo clip) | Same words as the hero |
| 11 | **Footer** | Privacy, terms, contact; only certifications actually held | Nothing claimed that isn't true |

**Proof is real or absent.** Logos, ratings, counts, testimonials and badges come only from `2-OFFER.md` → proof or from the member. A pre-launch page leaves those slots out and leans on the demonstrative visual, the guarantee or the founder's story.

## The hero gets extra scrutiny

- **Headline = the magic moment framed as a benefit**, and deliverable in the first session. If the moment is "notes ready 60 seconds after the call", the headline can promise "Meeting notes in 60 seconds" — not "Your team's most productive year".
- **Outcome + timeframe or ease** beats naming a feature: "Ship a feature in one afternoon", "Cut your reporting time by 80%".
- **Sub-headline does one job:** names the customer, the specific outcome, or the time — not all three.
- **CTA is first person and names the benefit:** "Start my free trial", "Get my plan".
- **The visual shows the real product working.** No stock photos, abstract gradients or "AI brain" art.
- **Test:** read the headline to someone in the customer group and ask what the product does. If they can't answer in one sentence, rewrite.

## Worked heroes

- **Stripe** — "Financial infrastructure for the internet" (6 words); runnable cURL with language tabs; CTA "Start now"; public pricing linked from the nav. The reference for code-in-the-hero.
- **Lovable** — "Build software products, using only a chat interface" (9 words); the hero *is* the prompt box; the send button is the CTA; signup fires on save; a gallery of user-built apps as proof. Reported ~$200M ARR in 12 months with no paid acquisition (founder-reported — verify).
- **Linear** — "The issue tracking tool you'll enjoy using"; sub "purpose-built for planning and building products"; a real UI screenshot with subtle motion; CTA "Start building"; logos within the first scroll; three visible tiers.
- **Designjoy** — a gallery of delivered work, the monthly price on the page, self-serve checkout. The page sells reliability, not a pitch.

## Why landing pages fail

- **The stock-illustration hero.** Lowest-converting hero pattern in the 2026 data; removing it entirely beat keeping it (+4%). Show the product.
- **The multi-CTA hero.** "Start free trial", "Book a demo", "Talk to sales" above the fold — decision fatigue. One CTA, repeated.
- **The "Submit" button.** Generic one-word CTAs lose to benefit copy by up to 60%. "Submit" → "Get my pricing".
- **Hidden pricing.** "Contact us" reads as expensive and drops the highest-intent visitors.
- **The autoplay video hero.** Motion delays comprehension; if there's a video, put it below the hero, under 30 seconds.
- **Animate-everything scroll.** One or two tuned reveals per page. Motion that doesn't teach gets cut.
- **The wall of logos** (30 of them reads as desperate) and **"Trusted by" with no logos**.
- **The feature list** — six bullets starting with the product's name.
- **The form wall** — name, company, phone, role, team size before anything. Email only; capture the rest through use.
- **The promise onboarding can't keep** — a hero that outruns the magic moment turns a conversion win into a churn loss.
- **The 30-section page.** The visitor is gone by section 8.

## What good looks like

| Metric | Floor | Good | Best |
|---|---|---|---|
| Visitor → next action (B2B SaaS) | 1.5% | 4% | 8–15% |
| Visitor → free-trial signup | 3% | 7% | 15%+ |
| Hero CTA click-through | 3% | 8% | 15%+ |
| Scroll past the hero | 50% | 70% | 85%+ |
| Largest Contentful Paint | <3 s | <2 s | <1 s |

Below the floor, the fix is almost never the layout — it's the headline, the CTA copy or the hero visual. Plan a first A/B test (headline or CTA) within 45 days of launch; top-quartile SaaS teams refresh hero copy on about that cadence (SaaS Frame).
