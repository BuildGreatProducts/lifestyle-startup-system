---
kind: curated
last-reviewed: 2026-11-03
---

# Extracting the offer from an existing product

How `path-finder` writes an extracted draft of `docs/2-OFFER.md` from what already exists, so `product-offer` can review it instead of starting blank. Extraction gets the member to the valuable conversation in an hour instead of a day; it doesn't replace that conversation.

## Where the evidence is

Read all of it before drafting, in this order of trust:

1. **The live product, landing page or store listing** — the strongest evidence of what the product actually promises today: which customer it addresses, which pain it names, what price it dares to show.
2. **The code** — features that demonstrably work, the core flow, payment integrations (a Stripe product or a RevenueCat offering is pricing evidence), copy strings and empty states (offer language hides in UI copy).
3. **Existing docs** — README, decks, notes. When these disagree with the product, the product wins.
4. **The member** — who really uses it, how they found it, what they say, what anyone has paid. Ask; never infer user counts from code.

## What to draft

Follow the section order `product-offer` uses, so its review can work section by section:

- **Summary** — the pitch in two or three sentences, assembled from the parts below.
- **Customer** — who the product is *actually built for*, per the evidence. Flag loudly where that differs from who the member says it's for: that gap is one of the most valuable things extraction surfaces.
- **Offer** — customer, pain, outcome, mechanism, guarantee, proof; each one or two sentences, each traceable to evidence. Where the evidence is silent (usually guarantee, often proof), write the honest gap — *"No guarantee anywhere on the current site — decide one in the review"* — never an invention.
- **Product** — `Shape: <slug>` as confirmed in path-finder's step 2, with one line on why.
- **Pricing** — what's charged today (from the site, payment code or listing, or "currently free — no price has ever been asked"), the model and billing unit the evidence implies, and who pays.
- **Sources** — the files, URLs and listings each section came from.

## Marking it

- The header is `Status: Extracted`.
- Under the title, one line: *"Extracted from the existing product on <YYYY-MM-DD>. Review it with `product-offer` before building on it."*
- Before writing, confirm the two or three inferences that would change everything if wrong (who the customer is, what the core pain is, what the price is) with short questions — *"The site sells to freelancers but onboarding assumes a team — which is it?"* This is a quick confirmation pass, not the full offer conversation.
