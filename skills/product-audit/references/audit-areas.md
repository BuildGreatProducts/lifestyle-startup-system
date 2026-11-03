---
kind: checklist
last-reviewed: 2026-11-03
---

# Audit areas

Work every area for every product with screens. Each item says what to look for in the **screenshots** and, where a screenshot can't show it, in the **code** (read only — never change it). Mark an area N/A with a one-line reason when it doesn't apply (no paywall on a free open-source tool, no SEO on a browser extension's popup). The thresholds behind each flag, with sources, are in [conversion-benchmarks.md](conversion-benchmarks.md); the activation and retention areas are in [activation-retention.md](activation-retention.md). Confirm current store and platform rules live before citing one.

## Contents

- [A. Speed and Core Web Vitals](#a-speed-and-core-web-vitals)
- [B. Front door: hero and CTA](#b-front-door-hero-and-cta)
- [C. Signup and forms](#c-signup-and-forms)
- [D. Trust and proof](#d-trust-and-proof)
- [E. Pricing](#e-pricing)
- [F. Mobile and touch](#f-mobile-and-touch)
- [G. Paywall and subscription](#g-paywall-and-subscription)
- [H. Analytics](#h-analytics)
- [I. Experiments](#i-experiments)
- [J. Search and discoverability](#j-search-and-discoverability)
- [K. Store listing](#k-store-listing)
- [L. Design-system adherence](#l-design-system-adherence)
- [M. Copy](#m-copy)
- [Quick wins that almost always turn up](#quick-wins-that-almost-always-turn-up)

## A. Speed and Core Web Vitals

- [ ] Measure LCP, INP and CLS on the front door and the core-loop screen if a browser or PageSpeed tool is connected; otherwise estimate from the code and say so.
- [ ] Screenshots: layout jumps between the loading and loaded captures; images that pop in late.
- [ ] Code: hero images without dimensions or modern formats; render-blocking scripts in the head; fonts without `font-display: swap`; one bundle over ~500 KB; heavyweight libraries for small jobs.

## B. Front door: hero and CTA

- [ ] Headline over 12 words, or naming a feature instead of an outcome.
- [ ] More than one primary-styled CTA above the fold; CTA wording that changes between header, hero and footer.
- [ ] Generic CTA ("Submit", "Sign up", "Get started") where a first-person benefit CTA fits.
- [ ] Stock or abstract hero art instead of the product working; an autoplay video hero.
- [ ] No proof above the fold; logos with a "Trusted by" tagline and no logos.
- [ ] The hero's promise against what onboarding actually delivers.

## C. Signup and forms

- [ ] More than three fields on the main signup; any required field past email that the first output doesn't need.
- [ ] No SSO (Google; Apple on iOS; GitHub for developers) on the main signup.
- [ ] Placeholder-as-label; password rules shown only after an error; validation only on submit.
- [ ] CAPTCHA on every signup rather than on abuse triggers.
- [ ] Multi-step forms with no progress indicator.
- [ ] Code: missing email input type, autocomplete and mobile keyboard hints.

## D. Trust and proof

- [ ] Real proof (named results, a rating with its count and source) near the decision points, not only in the footer.
- [ ] The offer's guarantee visible where the customer decides.
- [ ] Privacy, terms and contact linked; only certifications actually held.
- [ ] Any proof that can't be traced to a real customer — flag it as a trust risk.

## E. Pricing

- [ ] Price visible without "Contact us" for anything self-serve.
- [ ] More than three plans; no plan highlighted as the one to pick.
- [ ] Plans and prices on screen match `docs/2-OFFER.md` exactly.
- [ ] Each plan's CTA matches the front door's CTA wording.
- [ ] Answers near the table to the real objections: trial end, refunds, plan changes, cancelling.

## F. Mobile and touch

- [ ] Phone captures: horizontal scroll, clipped text, overlapping elements at 390 px wide.
- [ ] Primary actions under 44×44 px or outside the thumb zone.
- [ ] Modals that don't fit the phone screen; sticky bars covering content.
- [ ] Code: missing viewport meta tag; inputs under 16 px (iOS zooms on focus).

## G. Paywall and subscription

- [ ] Where the paywall fires: before or after the first taste of value.
- [ ] Trial visible and clear about when the charge happens; annual + trial preselected where the pricing intends it.
- [ ] A visible way out — close, continue free, or restore purchases.
- [ ] A real review or rating above the plans on a consumer paywall.
- [ ] What happens on dismiss: nothing, or an alternate offer.
- [ ] Usage-based plans show a meter before the limit hits.

## H. Analytics

- [ ] Code: an analytics library present; page views; CTA clicks; signup started and completed; trial started; paid; the **magic-moment event** from `docs/5-FLOWS.md` actually fired.
- [ ] Error tracking present.
- [ ] Any tracking that runs before consent where consent is required — flag as a trust and legal risk.

## I. Experiments

- [ ] Code: a feature-flag or experiment tool present, or none — note it; without one, the go-to-market experiments run on copy swaps and dates.

## J. Search and discoverability

- [ ] Code: title ≤60 characters and description ≤160 on the front door; social share image set; structured data for the product; robots and sitemap; canonical URLs.
- [ ] An `llms.txt` or clean docs for developer tools and MCP servers that agents read.

## K. Store listing

For shapes whose front door is a store (mobile-app, browser-extension, agent and MCP marketplaces, chat-assistant directories).

- [ ] Capture the live listing as it shows in search results and on its page.
- [ ] Check it against [../../prototype-flows/references/store-listing-best-practice.md](../../prototype-flows/references/store-listing-best-practice.md): icon at small size, title and subtitle, the first two or three screenshots carrying the sale, captions as benefits.
- [ ] The listing's promise against what the first session delivers.

## L. Design-system adherence

Skip if there's no `docs/4-DESIGN.md`; say so, and note that every colour and size in the report is unchecked against a system.

- [ ] Parse the tokens: colours, type levels, radii, spacing, components, and the prose rules (elevation model, do's and don'ts).
- [ ] Screenshots: colours, type sizes, radii and spacing that don't match a token; components that look different on two screens.
- [ ] Code: hardcoded hex values, font names and pixel sizes where a token exists.
- [ ] Classify every hit as one of three, no fourth:
  - **Inconsistency** — a raw value where a token exists, or a documented rule broken. Give the token to use.
  - **New pattern** — something the system doesn't cover yet (a new shade, a new component variant). Verdict: *Promote* (fills a real gap; propose the token), *Refactor* (real gap, wrong value), or *Defer* (single use).
  - **Aligned** — count it by screen so the report credits the work.
- [ ] The same raw value in twelve places is one finding with twelve locations.

## M. Copy

- [ ] Every screen against [../../prototype-flows/references/ux-writing.md](../../prototype-flows/references/ux-writing.md): buttons as verb + noun, errors with what/why/fix, empty states with a reason and one CTA, confirmations without "Are you sure", quiet toasts.
- [ ] The named failures: marketing bleed, apology loop, enthusiasm overdose, developer leak, synonym shuffle, blame shift, permission ambush.
- [ ] Against `docs/5-FLOWS.md` → copy rules and lexicon, and `docs/3-BRAND.md` → tone of voice and "we don't say", when they exist.

## Quick wins that almost always turn up

- [ ] **One field too many** on signup. Name it.
- [ ] **A CTA that doesn't match where it goes** — "Try it free" landing on a card form.
- [ ] **Body text too small to read** — a fashionable 13–14 px body on a phone.
- [ ] **The untested dark mode** — something invisible in one theme. Capture both if there's a toggle.
- [ ] **The cookie banner over the hero** — covering more than ~30% of the first screen.
- [ ] **The magic moment nobody counts** — no event, so activation can't be measured.
