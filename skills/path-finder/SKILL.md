---
name: path-finder
description: >-
  For a product that already exists — code, a prototype, an AI-generated app, a live service or
  store listing. Scores it against the nine steps with evidence, marks each step Do, Fast-track or
  Done, writes extracted drafts where the product already answers a step, and writes the path to
  docs/0-PATH.md. Use when the member says "I already have a product", "audit my project", "where
  do I start with my existing app", or after start on an existing project. Not for a new idea —
  use idea-finder or product-offer; not for a UX teardown of the screens — use product-audit.
---

# Path finder

Most members with an existing product don't need all nine steps from scratch — they need the two or three that are weakest, in the right order. This skill reads everything that exists, scores it step by step with evidence, and writes the path: which steps to do in full, which to fast-track from what's already there, and which are done. From then on, `start` follows the path.

It never edits the product's code. The only files it writes are `docs/0-PATH.md` and, for fast-tracked steps, extracted drafts of that step's document.

## Inputs

- **The code** — stack, size, structure, whether tests pass, deploy config, payments, analytics, error tracking, obvious security smells (committed secrets, open database rules).
- **The live product** — the URL, store listing or marketplace page. Read it with a fetch or browser tool if one is connected; otherwise ask the member to paste the page copy and pricing.
- **Existing docs** — README, anything in `docs/`, pitch decks, notes. When what the member wrote and what the product does disagree, the product wins.
- **Platform** — whether it lives on a prompt-to-app platform (Lovable, Bolt, v0, Base44, Replit…).
- An existing `docs/0-PATH.md` means a re-run: keep finished steps as Done, show the changes, and ask before overwriting.

## Workflow

### 1. Inventory the evidence

Read everything above before scoring anything. Note each item with a one-phrase assessment ("Stripe checkout live, one $29/mo plan"; "landing page names no customer").

**Done when:** you can say what the product is, who it seems to be for, how it makes money, and where it lives.

### 2. Settle the shape

Name the product's shape from [../product-offer/references/shapes.md](../product-offer/references/shapes.md) and confirm it with the member — every later step adapts to it. It goes into the extracted `## Product` section in step 6.

**Done when:** the member has confirmed one shape slug.

### 3. Ask only what the evidence can't answer

At most five questions, in one message: users and revenue (real numbers), the goal for the next 90 days, hours a week they can put in, which coding agent they build with, and any deadline.

**Done when:** you have the answers, or the member has said they don't know.

### 4. Score and stage

Score each step against [references/scorecard.md](references/scorecard.md). Every score cites its evidence; a missing artefact scores 0, never a guess. Then name the **stage** — prototype, live with no users, users with no revenue, or revenue — because the stage decides where the leverage is.

**Done when:** every step that applies to the shape has a score with evidence, and the stage is named.

### 5. Mark and order the path

Give each step a mark, with one line of why:

- **Do** — missing or weak (score 0–1): run the step in full.
- **Fast-track** — the product already answers it but nobody wrote it down, or it needs sharpening (score 1–2): write an extracted draft now (step 6), and the step's skill reviews it with the member instead of starting blank.
- **Done** — good enough to build on (score 3, or 2 where the stage doesn't depend on it).

Step 1 (idea) is Done for any existing product unless the member is pivoting. Step 6 (build plan) runs in existing-code mode whenever later steps change the product. Security (7) comes before go live (8). Go to market (9) is always on the path — only its timing varies.

Where the product has screens the member can run, add **product audit** before the build plan, so the plan's phases fix what the teardown finds.

Then order the path by the stage's leverage — [references/scorecard.md](references/scorecard.md) → *Leverage by stage*. Present the scores in a few lines and the first five steps with their reasons; fold in the member's corrections.

**Done when:** the member agrees with the path's first three steps.

### 6. Write the extracted drafts

For each Fast-track step whose document can be pulled from the product:

- **Offer** → write `docs/2-OFFER.md` following [references/extract-offer.md](references/extract-offer.md), with `Status: Extracted`.
- **Design system** → hand to `design-system` in its from-code mode, which writes `docs/4-DESIGN.md` with `Status: Extracted`.
- **Brand** → write `docs/3-BRAND.md` with what the product already shows (name, voice from the copy, colours and type from the site), with `Status: Extracted`. `brand-identity` reviews it and runs the visual exploration only if the member wants a new direction.

Never overwrite a step document that isn't `Extracted` without showing the diff and asking.

**Done when:** every Fast-track step that has an extraction route has its draft, marked `Extracted`.

## Write docs/0-PATH.md

```markdown
# Path: <product name>

Status: Done
Updated: <YYYY-MM-DD>

## Where it stands
Shape: <slug> · Stage: <stage>
<Two or three sentences: what exists, what's strongest, what's weakest.>

## Scores
| Step | Score (0–3) | Evidence |
|---|---|---|
| 2. Offer | … | … |
…

## The path
- [x] 1. Idea — **Done** — <one line of why>
- [ ] <N>. <Step name> — **Do** / **Fast-track** — <one line of why>
- [ ] Product audit — **Do** — <one line of why>
…

## Sources
<Files, URLs and listings the scores came from.>
```

List the path in working order, not step order. Start each line with the step's number and name exactly as in the steps table (`2. Offer`, `6. Build plan`), or `Product audit`, so `start` can match it. Write **Done** steps as ticked `- [x]` lines — they have no document of their own, and later steps treat a ticked line as done. `start` ticks a line once that step's document reaches `Status: Done` (product audit: once `docs/audit/REPORT.md` exists), and runs the first unticked one.

## Verify before delivering

- [ ] Every score cites evidence; nothing scored from assumption.
- [ ] The shape is a valid slug, confirmed with the member.
- [ ] Security comes before go live; go to market is on the path.
- [ ] Every Fast-track step with an extraction route has its `Extracted` draft.
- [ ] The path's first step is something the member can start today.
- [ ] No product code was changed.

## Next

The first step on the path. Tell the member what it is and why it comes first, in plain words, then run it — or let them say "continue" next time and `start` will.
