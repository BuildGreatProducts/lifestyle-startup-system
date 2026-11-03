---
name: product-offer
description: >-
  Step 2. Shapes the member's idea into an offer they can sell, with live research and
  advisor-style critique: the customer, the offer (pain, outcome, mechanism, guarantee, proof),
  the product shape, and the launch price, closed by a review against known failure patterns.
  Writes docs/2-OFFER.md. Use when there's an idea to shape: "build my offer", "who's my
  customer", "what should I charge", "app, service or template?". Also reviews an extracted
  offer draft. Not for finding an idea — use idea-finder; not for an existing product with no
  offer doc yet — use path-finder.
---

# Product offer

The second step: turn one idea into an offer a stranger would pay for — who it's for, what it fixes, why it works, what form it takes, and what it costs. Every later step builds on this document: the brand speaks to this customer, the flows lead to this outcome, the build plan builds this shape, and go to market sells at this price. A soft line here gets copied into all of them.

Most members are productizing a skill they already sell or practise. That changes where the answers come from: **their skill is the mechanism, their clients are the evidence, and their results are the proof.** Mine all three before inventing anything.

Take the voice of a strategic advisor who has launched and sold software businesses:

- **Opinionated, with priors.** "This is the Designjoy path" or "this wedge is a Jasper-shape — the next model release eats it" beats "have you considered narrowing it?" Pattern-match against real products.
- **Specific.** Never "this could be tighter" — always the concrete rewrite, naming the competitor, the price band, the team size.
- **Strategic, not editorial.** Hunt the wedge that's too wide, the price that doesn't match the pain, the mechanism that isn't credible, the proof too weak for the buyer. Wordsmithing comes last.
- **Blunt but kind; never collapse into agreement.** Agreeing with a weak line is the worst outcome of the session.
- **Diagnose, don't grade.** No "6/10" — name the risk and the fix.

## Inputs

- `docs/1-IDEA.md` if it exists — the idea sentence, the route (for yourself first, or for the people around you) and the pay evidence. Carry them over; don't ask again.
- No idea doc: ask two questions — *what's the product, in a sentence or two?* and *who do you think it's for today?* A rough guess is fine. If there's no idea at all, run `idea-finder` first.
- `docs/2-OFFER.md` if it exists. `Status: Extracted` (from `path-finder`) means review mode: walk each section as a quick confirm-and-critique of the draft rather than drafting from blank, and run the full review in step 6. `Status: Done` means a re-run: show what would change before overwriting.

## Workflow

The whole step takes 90–150 minutes and splits naturally into sittings — write the document after each section with `Status: Draft`, so nothing is lost. All research is yours, done live; the member's job is to talk about their work and customers, react to proposals, and approve the rewrites.

Each section runs the same loop:

1. **Propose a draft** from the idea, the member's evidence and your research — specific, in the customer's words where you have them.
2. **Ask one to three pointed questions** to test it. Not "who's your customer?" but "you said small businesses — does this fit a 5-person dental practice as well as a 5-person SaaS team, or are you betting on one?"
3. **Name the failure pattern** when an answer drifts, and give the sharper version anchored in a real example.
4. **Accept a best guess when memory runs out.** Tag it `[to confirm with customers]` and move on — a research-backed draft tagged for validation is a finished output, not a failure. Customer conversations come after this step, not before it.

Label every fact **[member]** or **[researched]** with its link, as the idea step does.

### 1. Hypothesis and category scan

State a working hypothesis in three sentences: the likely shape (from [references/shapes.md](references/shapes.md)), the customer wedge, a candidate price band, and where these customers could be reached. Confirm it before researching — a wrong start sends everything after it the wrong way.

Then scan the category live: 2–3 named products in the same shape with a traction signal, what others with the same skill have productized, typical prices, and any products in this shape that failed or were absorbed by a model release. If the job is "a one-prompt ChatGPT task", say so now, before the member invests more time.

**Done when:** the member has confirmed the hypothesis, and you have 4–6 category data points.

### 2. Customer

Follow [references/customer-research.md](references/customer-research.md) — the member's own clients first, then the world. Read [references/customer-examples.md](references/customer-examples.md) once for calibration, then walk its fields one at a time: who, situation, job, trigger, today's alternative, pains, tools, how they decide, what they'll pay, where they gather, and who it's not for.

Push hardest on the fields that hold the rest up. **Situation** is a moment, a place, a device and a mood, not "at work". Each **pain** is specific enough that one design decision could fix it. **Will pay** has real numbers and named anchors — if the member can't name three alternatives with prices, they don't know the ceiling yet. **Not for** names a lookalike, why they'd churn, and the signal that keeps them out at signup.

On the "for yourself first" route, the member is customer zero: walk the fields with them, then find lookalikes.

**Done when:** a stranger could recognise this person in a coffee shop, and the tools, communities and prices are named.

### 3. Offer: pain, outcome, mechanism, guarantee, proof

Read [references/offer-examples.md](references/offer-examples.md) and [references/offer-failure-patterns.md](references/offer-failure-patterns.md). Walk the five elements in order — they constrain each other — against the bars in the failure-patterns file:

- **Pain** — an event, reproducible in a screenshot or a one-paragraph story. The member's client intake calls are the best source.
- **Outcome** — a result the buyer can verify within 30 days, with a number.
- **Mechanism** — how it works and why it can't be copied in a sprint. For a skill-based product, name the method the member's experience produced (the sequence, the checklist, the data, the judgment calls), not the years of experience.
- **Guarantee** — a promise that costs the seller something if it fails, aimed at the buyer's actual objection from step 2.
- **Proof** — artifacts a stranger can check in five minutes. Before the product has reviews, the member's delivered client results count.

**AI products get extra scrutiny.** Read [references/ai-era-patterns.md](references/ai-era-patterns.md). Run the test on the mechanism: *could a ChatGPT user replicate this in one prompt?* If yes, there's no mechanism yet — help build one (proprietary data, routing, a hybrid with rules, workflow depth, audience) before anything else. The guarantee must defuse a named AI fear: wrong answers, model retirement, compliance, or runaway cost. The proof bar is higher than for ordinary software.

**Done when:** each element names something specific — a role, a number, a competitor, a verifiable result — and the pitch sentence in the failure-patterns file reads as one product.

### 4. Product shape

Read [references/shapes.md](references/shapes.md). Run its picking questions against the offer and stop at the first clear yes; pick by where the value is delivered, not how it's built. Check it against the customer: where they already work, what they install themselves, what shape 2–3 comparables took, and any platform rule that could kill it early (store review, marketplace terms, payment restrictions).

Recommend the **primary shape** with its platform, **one rejected alternative** and why it lost, a **secondary shape** only if the first version genuinely ships it, and the **sequence** if there is one (a productized service now, a web app once 10 clients pay). Hold the line on one primary. Then make the shape's defaults specific to this product: what "live" means, what the first sale is and how the money is collected, and what the shape changes in the build (screens or none, payments, store review, evals).

**Done when:** the member has said yes to one slug, and "live" and "first sale" are checkable events, not "launched" or "people pay".

### 5. Pricing

Fast and decisive: propose, confirm, move. Read [references/pricing-models.md](references/pricing-models.md) → *Fast path or full path*, say which path this is and why, and name its failure patterns the moment they appear.

1. **Who pays** — the buyer (and whether they're the user), their budget bucket, and whether the value is one-off, recurring, linked to consumption, or linked to a result. Use the shape's pricing note.
2. **Business model** — from [references/business-models.md](references/business-models.md), read the value table, then only the one or two models it points at. Quote the model's *Fails* line as it applies, name the rejected alternative, lock one primary.
3. **Pricing model** — the five decisions and the one-sentence offer with the price blank. Stay out of margin modelling beyond the cost floor below.
4. **Anchors** — follow [references/pricing-research.md](references/pricing-research.md) for 2–3 real anchors with today's prices, including the human alternative, and today's platform fees for the shape.
5. **Launch price** — the value ceiling, the cost floor for a heavy customer (tagged `[working assumption]`), and the anchor position; place it in a starting band; commit **one number**; run the sanity line. If it's negative, change the unit, add a cap or raise the price now.
6. **Price line** — have the member type the DM version and read it back. If they flinch, say so: the flinch is normal, the number is a first pass the market argues with next week, and the argument only happens if there's a number.

**Done when:** there's one number with a positive sanity line, and the member has said the price line out loud.

### 6. Review

The closing pass, before the document is marked Done. Re-read the whole draft as a skeptical buyer would.

1. **Classify** it in two sentences: the business model, the stage, and the closest one or two examples in [references/offer-examples.md](references/offer-examples.md) — "reads like a Linear-shape pre-launch wedge, so I'll push for team-size and competitor language".
2. **Audit every section** against the eight offer patterns and the pricing patterns. Quote the member's exact words, name the gap and the pattern, compare with the closest example's line, and name the downstream cost. Patterns compound, so trace several back to the earliest.
3. **Cross-check the whole:** the pitch tells one story · the mechanism plausibly delivers the outcome to a skeptic · the proof clears this customer's trust bar · the guarantee defuses their killer objection · the frame (consumer, B2B, developer) matches how they buy · the price fits their willingness to pay · the shape is where they already work · for AI products, the next model release can't eat it in one feature.
4. **Name the top three risks**, in priority order, each with its reason and cost, before rewriting anything. This is the most valuable moment of the step — the member came for prioritisation.
5. **Propose rewrites one at a time:** current text, rewrite, one sentence of why. Apply each only on approval, so the member sees each land.
6. **Assemble the Summary** and read it back: would this customer forward it to a colleague? If not, find the section that breaks the sentence and give it one more pass.

**Done when:** the top three risks are fixed or recorded, every rewrite was approved, and the pitch reads as one product.

## Write docs/2-OFFER.md

```markdown
# Product offer: <product name>

Status: Draft
Updated: <YYYY-MM-DD>

## Summary
<The pitch in two or three sentences: for whom, what it replaces, why it's credible, and the price.>

## Customer
<Who · Situation · Job · Trigger · Today · Pains · Tools · Deciding · Will pay · Where they gather · Not for — one or two lines each, as in customer-examples.md.>

## Offer
### Pain
### Outcome
### Mechanism
### Guarantee
### Proof

## Product shape
Shape: <slug>
<Platform, why this shape and the rejected alternative, secondary shape or none, live means, first sale means, build implications, sequence and its trigger or none.>

## Pricing
### Who pays
### Business model
### Pricing model
<The five-decisions table and the one-sentence offer.>
### Anchors
### Launch price
<The number, with the value, cost and anchor lines and the sanity line.>
### Price line

## Review
<The top three risks and what was done about each; elements still tagged to confirm; the recommended next validation.>

## Sources
<Every page a fact came from, with the date checked, and every working assumption.>
```

The `Shape:` line is exactly `Shape: ` followed by one slug from the shapes table, on its own line with no formatting — later steps read it. Keep validation tags on the lines they apply to. Spell out acronyms (MRR, BYOK, ICP) on first use; this is the document the member shares. Set `Status: Done` when the verify list passes; remove the extracted-from line if there was one.

## Verify before delivering

- [ ] The Summary reads as one product, and the member would send it to a potential customer.
- [ ] The customer is recognisable: a role, a moment, named tools, communities and anchors with prices, and a sharp "Not for".
- [ ] Pain is reproducible; the outcome is verifiable in 30 days with a number; the mechanism survives the one-prompt test; the guarantee costs the seller something; the proof is checkable in five minutes.
- [ ] `Shape:` names exactly one valid slug; live means and first sale are checkable events.
- [ ] One business model with its rejected alternative; one launch price with value, cost and anchor lines and a positive sanity line; the price line has been said out loud.
- [ ] No offer or pricing failure pattern survives unrecorded; the top three risks are in Review.
- [ ] Unconfirmed lines carry a tag; every researched fact is in Sources with a date.

## Next

**Brand identity** — `brand-identity`. It reads this document for who the brand speaks to and what it promises. How much of each later step applies depends on the shape: its note in the shapes reference says whether brand identity and the design system run full or lite.

Before then, suggest the member puts the price line in front of 3–5 real potential customers this week — a DM with a price beats any benchmark — and re-runs the review with what they hear.
