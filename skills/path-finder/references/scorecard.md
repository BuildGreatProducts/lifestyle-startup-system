---
kind: curated
last-reviewed: 2026-11-03
---

# Path finder scorecard

Score each criterion **0–3** with cited evidence: **0** missing · **1** exists but weak · **2** solid with gaps · **3** strong. A step's score is the average of the criteria that apply to the shape, rounded to one decimal. Criteria marked *(screens)* apply only to shapes with screens (see `has screens` in [../../product-offer/references/shapes.md](../../product-offer/references/shapes.md)).

## Contents

- [2. Offer](#2-offer)
- [3. Brand identity](#3-brand-identity)
- [4. Design system](#4-design-system)
- [5. Prototype flows](#5-prototype-flows)
- [6. Build plan](#6-build-plan)
- [7. Security audit](#7-security-audit)
- [8. Go live](#8-go-live)
- [9. Go to market](#9-go-to-market)
- [Stages](#stages)
- [Leverage by stage](#leverage-by-stage)

## 2. Offer

| Criterion | 3 looks like | 0 looks like |
| --- | --- | --- |
| Offer clarity | One sentence names a specific customer, an urgent pain, a measurable outcome and a mechanism; the site or listing says the same thing | No written offer, or "AI tool for everyone" |
| Customer | A specific person with named tools, communities and a reason to pay | "Small businesses" |
| Pricing | A decided model and launch price, live at checkout, with a reason | Free by default, or "we'll figure it out" |
| Shape fit | The shape matches where the customer already works | The shape is whatever got built |

## 3. Brand identity

| Criterion | 3 looks like | 0 looks like |
| --- | --- | --- |
| Identity | Name, point of view, voice and visual style are consistent across product, site and listing | Default template look, inconsistent voice |
| Voice in the copy | Consistent words for the same things; errors and empty states sound like the brand | Lorem ipsum, mixed terms, "Something went wrong" |

## 4. Design system

| Criterion | 3 looks like | 0 looks like |
| --- | --- | --- |
| Tokens *(screens)* | One token set for colour, type, spacing and radius, used everywhere | Hardcoded hex values everywhere, competing styles |
| Components *(screens)* | Shared components reused across screens | Every screen styled by hand |

## 5. Prototype flows

| Criterion | 3 looks like | 0 looks like |
| --- | --- | --- |
| Magic moment | A named first-value moment, reached in the first session by a guided path | The user lands on an empty screen (or an install with no first command) |
| Front door | The landing page or store listing converts: clear promise, real proof, one call to action | No public page, or one that lists features, not outcomes |
| Core loop and paywall | The loop the customer repeats is short and obvious; the paywall sits after value | The loop is buried; payment is asked before any value |

## 6. Build plan

| Criterion | 3 looks like | 0 looks like |
| --- | --- | --- |
| Plan | A current build plan the code matches | No plan; the code is the only documentation |
| Code health | Clear structure, tests that pass, runs locally | Untestable, generated sprawl, nothing runs locally |

## 7. Security audit

| Criterion | 3 looks like | 0 looks like |
| --- | --- | --- |
| Security | A recent clean audit, secrets out of the repo, access rules enforced | Committed keys, open database rules, unprotected routes |

## 8. Go live

| Criterion | 3 looks like | 0 looks like |
| --- | --- | --- |
| Live and reliable | Live by the shape's "live means" bar, with error tracking | Not live, or live with no idea when it breaks |

## 9. Go to market

| Criterion | 3 looks like | 0 looks like |
| --- | --- | --- |
| Channels | A chosen channel with a working playbook, including the shape's native channel | "We posted it once" |
| Experiments | Experiments with win conditions and logged results | No measured experiments |
| Activation | Most new users reach the magic moment, and it's measured | Unknown — no tracking |
| Retention and revenue | Users return and pay; churn is measured | No returning users, no revenue |

## Stages

- **Prototype** — something runs, but it isn't live by the shape's bar.
- **Live, no users** — live, but nobody outside the member's circle uses it.
- **Users, no revenue** — people use it; nobody pays yet.
- **Revenue** — people pay.

(No product at all is not a stage here: send the member to `idea-finder` or `product-offer`.)

## Leverage by stage

After the fixed rules (security before go live; go to market always on the path), order the path so the stage's weakest link comes first:

- **Prototype** — get it live: offer (fast-track) → brand and front door if they score low → product audit → build plan (existing-code mode) → security audit → go live → go to market.
- **Live, no users** — distribution: offer (fast-track) and go to market's strategy stage first, in parallel; then the front door and onboarding flows if they score low.
- **Users, no revenue** — money and activation: pricing (in the offer), product audit with conversion and retention in focus, a build plan for the paywall and onboarding fixes, then go to market's experiments.
- **Revenue** — growth and robustness: go to market experiments on the best channel, the security audit if it's stale, product audit for conversion, then scale and automate.

Within a stage, a score of 0–1 on a criterion the stage depends on outranks everything else.
