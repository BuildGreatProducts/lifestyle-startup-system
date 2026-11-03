---
kind: curated
last-reviewed: 2026-11-03
---

# Pricing models

How to shape a price once the business model is chosen ([business-models.md](business-models.md)): the billing unit, the plans, the entry route, the cadence and extra use; then how to set the number and say it. Read only the rows that match the unit and entry under discussion. All amounts are illustrative planning examples before tax, not market benchmarks.

## Contents

- [Keep the layers separate](#keep-the-layers-separate)
- [Fast path or full path](#fast-path-or-full-path)
- [The five decisions](#the-five-decisions)
- [The mechanics, by layer](#the-mechanics-by-layer)
- [Three worked combinations](#three-worked-combinations)
- [Setting the launch price](#setting-the-launch-price)
- [Presenting plans](#presenting-plans)
- [Discounts and guarantees](#discounts-and-guarantees)
- [Pricing failure patterns](#pricing-failure-patterns)

## Keep the layers separate

| Layer | Question | Examples |
|---|---|---|
| Shape | What does the customer use? | Web app, agent skill, productized service |
| Business model | Who pays, for what relationship? | Subscription, commission, software + services |
| Billing unit | What does the price multiply by? | Account, seat, document, location, accepted outcome |
| Packaging | What's included? | Tiers, add-ons, bundles, capacity bands |
| Entry | How does someone start? | Upfront, free tier, trial, paid pilot |
| Cadence and entitlement | When do they pay, and what do they keep? | Monthly, annual, one-time version licence, lifetime |
| Price setting | How is the amount chosen and shown? | Value, cost, anchors, presentation |

Freemium is an entry route. Seats are a unit. Annual is a cadence. None of them is a business model.

## Fast path or full path

- **Fast path** — one continuous or bounded outcome sold to an individual or small team: subscription or one-time, one obvious unit (account or seat), one or two plans. The five decisions become one-line confirmations: "subscription, per account, one plan, 14-day trial — agree?" Most solo and prosumer products, and most digital products, go this way.
- **Full path** — anything usage- or AI-heavy, a marketplace, ads or affiliate, B2B with procurement, a service, open core, or outcome-based. Walk every decision; the unit and the entry are where these products win or lose money.

If any full-path trigger applies, take the full path — a product can meet every fast-path test and still lose money on its unit.

## The five decisions

| Decision | The test |
|---|---|
| **Billing unit** — what the price multiplies by, and what's excluded | Does the customer already count in it? Could they explain it to their boss? |
| **Plans** — one, two or three, with a named default | Does each plan have a real buyer, or is the third column there because pricing pages have three? |
| **Entry** — upfront, free tier, trial, demo, paid pilot | Why this route? Does a free tier introduce buyers the paid plan never could? |
| **Cadence** — monthly, annual, one-time, per job | Does it match how often the value recurs? |
| **Extra use** — charge, top up, pause or upgrade at the limit | What happens to the heaviest customer? |

Then the whole offer in one sentence, with the price blank: *"For ___, [product] delivers ___ for $___ per ___, including ___; extra ___ costs ___."* If it doesn't read as a sentence, the model is too complicated.

## The mechanics, by layer

**Billing units**

| Mechanic | Fits when | Watch for |
|---|---|---|
| Flat rate per account | Simple tools; account costs don't vary much | Averages hide loss-making heavy accounts; "unlimited" on a low fee |
| Per seat | More people means more value (collaboration, CRM) | Automation whose value rises as operators fall; charging for every guest kills collaboration |
| Per active user | Big groups with occasional users | Obscure activity rules; bill variability |
| Metered usage | APIs, transcription, document processing — variable workloads | Exposing internal units (tokens); say whether retries and failures count; give spend alerts and a cap |
| Prepaid credits | Occasional jobs; buyers who want spending control | Show job equivalents, not just credits; unused balances are still owed work |
| Transaction fee / take rate | Marketplaces, payments-enabled software | Fee revenue isn't order value; a high take rate invites bypassing |
| Per resource (location, project, client, device) | Vertical and agency tools where seats misrepresent value | Per-project pricing discourages history — set an archive rule |

**Packaging and quantity**

| Mechanic | Fits when | Watch for |
|---|---|---|
| Feature tiers | Individual, team and organisation needs genuinely differ | Arbitrary limits that break the entry plan's promise |
| Add-ons and bundles | Customers need different extensions | Charging extra for a step the base promise needs |
| Volume (all units at the band's rate) | Bulk buyers who understand thresholds | A total that *drops* at a boundary: 100 units at $1 = $100, 101 at $0.80 = $80.80 |
| Graduated (each band at its rate) | Usage-heavy tools wanting smooth bills | Customers assume the lowest rate applies to everything: 100 × $1 + 50 × $0.80 = $140 |
| Blocks / stairsteps | Buyers who prefer predictable bands | One extra item forcing a big jump |
| Base plus overage | AI and automation with account-level value and variable cost | So many units nobody can estimate the bill; $29 incl. 500 docs, then $0.05 each → 800 docs = $44 |

**Terms, timing and entitlement**

| Mechanic | Fits when | Watch for |
|---|---|---|
| Custom quotes, commitments, minimums | Enterprise, white-label, large variable accounts | Custom isn't a reason to leave the unit undefined |
| One-time, perpetual, lifetime, paid upgrades | Offline tools and durable utilities | "Lifetime" on a hosted product priced from today's server bill; write the entitlement in plain words |
| Monthly / annual / instalments | Monthly lowers commitment; annual fits proven value | Annual cash isn't proof of renewal; show the total due beside any monthly equivalent |

**Other payers and outcomes**

| Mechanic | Fits when | Watch for |
|---|---|---|
| CPM / CPC / sponsorship | Audience products, niche media, newsletters | Ad load that damages retention; sponsor concentration |
| Per lead / referral / affiliate | Comparison and matching tools | Pay is for an *accepted* action, not a raw email |
| Hourly / project / retainer | Services, implementation, managed automation | Unlimited retainers sell more work than one person can deliver; count every revision |
| Per outcome / success fee | Repeatable, verifiable results the seller controls | Define the qualifying result, reversals and the baseline; price the failed attempts |

**Entry routes**

| Mechanic | Fits when | Watch for |
|---|---|---|
| Paid pilot | B2B setup, migration or stakeholder buy-in | Open-ended custom work called a trial; name the decision-maker first |
| Pay what you want | Community and creator resources | Forecasting every user as a donor |
| Freemium | Low free-user cost, broad distribution, a natural upgrade need | 1,000 free users at $0.20 each = $200/mo before anyone pays |
| Free trial / reverse trial / demo | Value is felt inside a bounded evaluation | Copying a competitor's 14 days instead of matching time-to-value; trial signups don't validate a price |

## Three worked combinations

Shapes, not answers — never retrofit the member onto one.

| Product | Business model | Pricing and entry |
|---|---|---|
| Local photo-cleanup utility | One-time purchase | $49 for a defined version; demo before purchase |
| Supplier-document workflow | Subscription plus usage | $29/month incl. 500 documents, $0.05 extra; guided trial |
| Agency client-reporting tool | White-label plus software + services | $500 setup, $30 per client per month; paid pilot |

## Setting the launch price

Build three lines, then commit **one number** for the default plan.

**Value ceiling** — what the outcome is worth to this buyer: the Customer section's willingness to pay, or an estimate the buyer would recognise:

- Time released: hours saved × what their time is worth, **halved** if the time can't actually be redeployed. Five hours a month at $30/hour is $150 of time value; if only half is reusable, ~$75; a $25 price is worth testing.
- Extra contribution: extra sales × profit per sale, not × revenue.
- A cost they can actually remove, or a credible cut in expected loss.
- For personal value (confidence, progress, enjoyment), ask about trade-offs; don't invent a financial return.

"10% of the value" is a hypothesis, not a formula.

**Cost floor** — direct cost to deliver one billing unit to a **heavy** customer. An order of magnitude is enough; tag each figure `[working assumption]` until real invoices replace it, and check today's figures with [pricing-research.md](pricing-research.md).

| Cost | Planning figure | Applies to |
|---|---|---|
| Card processing | ~3% + a few cents per charge | Every direct sale |
| App-store commission | 15–30% | iOS / Android digital goods |
| Creator storefront | ~10% all-in | Gumroad, Lemon Squeezy and similar |
| Deal-site revenue share | Often ~70/30 in the marketplace's favour | Lifetime-deal launches |
| AI inference, small model | Fractions of a cent per job | Classification, extraction, short generation |
| AI inference, frontier model | Cents to tens of cents per job; more for long documents, images, agents | Drafting, analysis, multi-step agents |
| Storage | A few cents per GB-month | Uploads, generated media |
| Email / auth | Fractions of a cent; often free at low volume | Every account |
| Human time | Planning rate × minutes per job or client | Services, review, high-touch onboarding |

Cost the heavy customer, not the average, and count failed attempts — an export that takes three tries costs three tries.

**Anchor position** — where the number sits against the 2–3 anchors, and why.

**Starting bands** — hypotheses the market argues with next week:

| Product | Starting band | Typical ladder |
|---|---|---|
| Consumer mobile subscription | $5–15/mo | Free → $9.99/mo or $59.99/yr |
| Prosumer / solo tool | $9–29/mo | One plan, or $9 / $19 |
| B2B starter SaaS | $19–99/mo | $19 / $49 / $99 |
| Team / agency SaaS | $99–700/mo | $99 / $299 / $700 |
| One-time / perpetual licence | $29–199 | Free → $69 → $149 |
| Lifetime-deal launch | $59–299, seats capped | $79 / $199 / $299 |
| Usage / credits | Per unit at 3–5× delivery cost | Base plan + overage |
| Paid pilot / productized service | $500–5,000 fixed scope | Pilot → retainer |

**Sanity line:** plan price − (cost per unit × heavy-use quantity for the period) = $___. It must be positive; if not, change the unit, add a cap, or raise the price now. Base plus overage runs it twice: at the included allowance, and at heavy use with the overage counted.

**Price line:** the DM version — *"I'm building X for Y — it'll be around $29/month, about half what [anchor] charges. Would that be worth it for you?"* The full version is the five-decisions sentence with the number in. A message with a price gets an honest signal; "sounds cool" is free, "I'd pay $29" is data.

## Presenting plans

- Design individual, team and organisation packages, then delete any without a real buyer. One or two clear plans often beat three.
- Show the full charge, included limits and billing period. Label a plan "most popular" only with purchase data; otherwise "For teams".
- Anchor against something the buyer can verify — their current process cost, a real higher plan, an annual total. An invented $999 "normal price" isn't evidence.
- A decoy (a $20 plan with 40 exports beside a $20 plan with 60) can shift choices in studies; it doesn't guarantee uplift. Prefer plans that serve distinct customers.

## Discounts and guarantees

- **A discount needs a job** — an annual commitment, an eligible group, a referral, a bounded launch test — with eligibility, duration and renewal price stated. A 20% discount on $20 with $6 direct cost cuts contribution from $14 to $10 — 29% — so it needs 40% more customers to break even.
- **A guarantee reduces one named risk.** Define what's promised, what the customer must do, the timeframe and the remedy. "Refund the setup if the agreed import can't be completed from supported inputs" is scoped; "guaranteed growth" isn't. A money-back guarantee is a remedy, not outcome billing.
- **Retention shows value, it doesn't trap.** Progress summaries, reports of time saved or money recovered, pausing instead of cancelling. A cancellation discount that keeps the account but not the value hides the problem.

## Pricing failure patterns

Name each the moment it appears, and propose the fix in the same breath.

- **The Blank Cheque.** "Everyone" as the buyer. A price needs a budget to come out of — name the buyer and the budget bucket.
- **The Layer Blur.** Freemium, annual, "AI-powered" or "with a guarantee" offered as the business model. Entry, cadence, capability and risk reduction — none says who pays for what.
- **The Two-Model Trap.** Subscription *and* one-time *and* services, "to maximise revenue". Two models mean two cost structures and two sales motions. Pick one primary.
- **The Invisible Unit.** Billing in tokens or API calls when the buyer thinks in documents, minutes or clients.
- **The Unlimited Promise.** Unlimited AI, storage or support on a low fixed fee. The heaviest customer sets your cost.
- **The Unexamined Flat Price.** One plan chosen without asking whether a second has a real buyer — or three columns because pricing pages have three.
- **The Freemium Dodge.** "Free for now, we'll monetise later." A free tier is fine when it introduces paying buyers — write down why, or don't.
- **The Ten-Percent Rule.** "The outcome is worth $1,000, so $100." A value estimate finds a ceiling; it doesn't prove anyone pays a fixed share.
- **The Negotiable Range.** "$20–50 depending" is a price already agreed to lower. One number.
- **The Free-Tool Anchor.** Anchoring against free products is a race to zero. Anchor against what the customer pays for.
- **The Launch-Cash Mirage.** Lifetime-deal or annual-prepay cash treated as recurring revenue. Cash now is a delivery obligation later.
- **The Hourly Anchor.** A member productizing a service prices the product from their old hourly rate × hours. AI makes delivery fast; price the outcome's value to the client, not the member's time saved.
- **The Unspoken Number.** A price the member has never said out loud. Make them type the price line and read it back.
