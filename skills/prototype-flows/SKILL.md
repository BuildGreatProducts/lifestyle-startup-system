---
name: prototype-flows
description: >-
  Step 5. Names the magic moment, maps the 3–5 user journeys that matter, then designs the key
  flows on a canvas in the brand and design system — front door (landing page or store listing),
  onboarding to the magic moment, core loop, paywall and checkout, settings — with real copy.
  Screenless shapes get journeys and first-use steps instead. Writes docs/5-FLOWS.md with the
  journeys, screens per flow with canvas links, and copy rules. Use when the member says "design
  my screens", "prototype the app", "what happens after signup". Not for tokens or colours — use
  design-system; not for a teardown of built screens — use product-audit.
---

# Prototype flows

The step where the product becomes something the member can walk through. It starts with the journeys — the few paths a customer takes from first hearing about the product to coming back for more — and the one moment on those paths where the product proves it's worth keeping. Then it draws the key flows as real screens, in the chosen brand and the design system's tokens, with the words a customer will actually read. The build plan turns every screen here into a phase, so a flow that isn't drawn usually isn't built, and copy that isn't written gets written by a coding agent in marketing English.

Take the voice of a senior product designer running a design sprint:

- **Journeys before screens.** No screen gets drawn until it sits on a journey and has a job.
- **Speed to the magic moment.** Every extra screen costs completions. The question on each one is "could this go, or merge with the next?"
- **Real copy, never lorem.** Every headline, button, error and empty state in the brand's voice — the words are half the design.
- **Pattern-led.** Every flow follows a named pattern from the references, and you say which ("this is the try-before-signup pattern Lovable uses").

## Inputs

- `docs/2-OFFER.md` — required: the customer, the offer (pain, outcome, mechanism, proof, guarantee), `## Product` (`Shape: <slug>`) and the pricing. Read the shape's row and its "Prototype flows" note in [../product-offer/references/shapes.md](../product-offer/references/shapes.md).
- `docs/3-BRAND.md` — required: the tone of voice (and its "we say / we don't say"), the chosen visual direction, the canvas link.
- `docs/4-DESIGN.md` — required for screen shapes: the tokens every screen uses. Lite mode needs only its brand tokens.
- `docs/5-FLOWS.md` if it exists — a re-run. Carry over what's settled, show what would change, and ask before overwriting a `Done` document.

If `2-OFFER.md` or `3-BRAND.md` is missing or still `Draft`, stop and run that step (`product-offer`, `brand-identity`); for a screen shape without `4-DESIGN.md`, run **design-system** first. Never invent a price, a voice or a palette to design against.

## Workflow

### 1. Set the mode

From the shape, decide three things and tell the member in two sentences:

- **Full or lite.** Full for shapes with screens: web-app, mobile-app, desktop-app, browser-extension, website, and a digital-product that is itself a visual template. Lite for the rest: agent-skill, agent-plugin, mcp-server, chat-assistant, developer-tool, productized-service, digital-product — journeys and first-use steps, no product screens. A lite shape that ships one screen (a developer tool's key dashboard, a service's intake form) draws just that.
- **The front door.** Whatever the shape's Front door column in shapes.md names: a website (landing, sales or download page), a store or marketplace listing, a directory listing plus README, or a mix.
- **The flows.** Full mode's default five: front door → onboarding to the magic moment → core loop → paywall and checkout → settings and account. Drop one only with a reason ("no paywall — it's a one-off purchase; checkout lives on the sales page").

**Done when:** the member has confirmed the mode, the front door and the list of flows.

### 2. Name the magic moment

Read [references/magic-moment-benchmarks.md](references/magic-moment-benchmarks.md). Research 2–3 named comparables in the member's category live (their documented aha, the category's time-to-value), then draft **three candidates** from different aha shapes, each with the seven fields. Recommend a primary ("I'd go with B: it's the fastest, and Granola proved the shape") and keep the other two as alternates. Say plainly that it's a hypothesis the first customers will test. If web search isn't available, say so, ask the member for comparables, and mark them unverified.

**Done when:** the member has picked a primary with a position, a time-to-aha target and a metric.

### 3. Map the journeys

Draft the **3–5 journeys that matter** — typically: discover → sign up → magic moment; come back and use it again (the core loop); decide to pay; and one recovery journey (a failed payment, a returning lapsed user, cancelling). Each journey is a line of steps with the touchpoint at each step (search result, landing page, store, email, the product), and the magic moment marked on the one it belongs to.

Show them as a diagram (a Mermaid flowchart in the doc, or the first artboard on the canvas) plus a short numbered list. Cut any journey the first version doesn't need — "invite your team" waits until a team buys.

**Done when:** the member agrees these are the journeys, and every flow from step 1 sits on at least one.

### 4. Write the copy rules

Before drawing, settle the words so every screen speaks one language. Read [references/ux-writing.md](references/ux-writing.md) and, with the tone of voice from `3-BRAND.md`, draft:

- **The lexicon** — the product's 8–15 core nouns and verbs (Concept / We say / Never say), from the offer's mechanism.
- **Rules with good/bad pairs** for buttons, errors, empty states, confirmations, toasts and notifications, in this product's nouns and voice. Lite shapes use the screenless surfaces table instead (descriptions, commands, tool text, client emails).
- **The banned list** — the universal LLM-isms plus the brand's "we don't say".

**Done when:** the member has approved the lexicon, and each surface has at least one good/bad pair in their product's words.

### 5. Plan the screens

For each flow, list the screens in order with their job, the states worth drawing (first run and empty, populated, loading, error, free vs paid) and the pattern behind it:

- **Front door** — a page from [references/landing-page-best-practice.md](references/landing-page-best-practice.md) (pattern, then the sections with real copy, the hero above all); a store listing from [references/store-listing-best-practice.md](references/store-listing-best-practice.md) (icon, title, subtitle, the screenshot sequence with captions, description). Confirm the store's current limits and rules live.
- **Onboarding** — the member's shape section in [references/onboarding-best-practice.md](references/onboarding-best-practice.md). It ends **at** the magic moment, never at a dashboard short of it. Estimate the time from first screen to the moment; if it's more than 20% over the target, merge or cut.
- **Core loop** — the screen they'll use most, populated with realistic data, plus its empty first-run state.
- **Paywall and checkout** — placed where the shape and pricing say (a mobile onboarding paywall, a web-app upgrade at a usage limit, a sales page checkout); plans and prices exactly as `2-OFFER.md` has them.
- **Settings and account** — only what version 1 needs: account, plan and billing, cancel, delete account, and the settings the core loop depends on.

Present one flow at a time and fold in "merge these two" or "this needs a step" before moving on.

**Done when:** every flow has its screen list confirmed, and the onboarding's time-to-magic-moment estimate is within target.

### 6. Draw the flows on the canvas (full mode)

Find and drive the canvas with [../brand-identity/references/design-tools.md](../brand-identity/references/design-tools.md) — `/design` first, then a connected design tool, then the HTML fallback at `docs/flows/canvas.html`. Push the `4-DESIGN.md` tokens into the tool where it accepts them, and run the one-artboard test first.

The brief: one row per flow, top to bottom in journey order; screens left to right, each labelled `<flow> · <NN> <screen>`, sized for the primary device (390×844 phone, 1440×900 desktop; the landing page at both); alternate states stacked beneath their screen; the magic-moment screen marked. Every value from the tokens, every word from step 4's rules, realistic data in every populated state. In the HTML fallback, link each primary button to the next screen's anchor, so the member can click through.

Check every artboard against [references/design-heuristics.md](references/design-heuristics.md) (its last table says which heuristics dominate which screen) and against the tokens: a value the tokens don't have is a **design-system gap** — note it, don't invent it. Generated screens drift: check hexes, fonts and copy before showing the member.

**Done when:** every planned screen and state is on the canvas in the brand, and you have a link to each flow's row.

### 6 (lite). Write the first-use steps

For a lite shape, write the steps from purchase or install to the magic moment instead, from its section in [references/onboarding-best-practice.md](references/onboarding-best-practice.md): each step's medium (terminal, chat, email, file, call), the exact words the customer meets, and its drop-off risk with the fix. The front door goes in as copy — the page sections or the listing fields — and on the canvas only if the member asks.

**Done when:** a stranger could follow the steps from first touch to the magic moment, and every step has its exact words.

### 7. Walk it through

Walk the member through each flow as the customer, once for the experience and once reading the copy aloud. Fix anything that trips: a screen without a clear next action, a promise on the front door the onboarding doesn't keep, copy that could belong to another brand.

**Done when:** the member has walked every flow and said it's right.

## Write docs/5-FLOWS.md

```markdown
# Flows: <product name>

Status: Done
Updated: <YYYY-MM-DD>

## Summary
<Shape, full or lite, the front door, how many flows and screens, the canvas link.>

## Magic moment
<The primary in one sentence. Where it sits · time-to-aha target · metric. A line each on the two alternates.
A note that it's a hypothesis the first customers test.>

## Journeys
<A Mermaid flowchart, then a numbered list: each journey's steps and touchpoints, the magic moment marked.>

## Flows
### 1. <Front door> — <canvas link>
| # | Screen | States | Job | Key copy |
<…one table per flow. Lite: a First-use steps table instead — # | Step | Medium | Exact words | Drop-off risk and fix.>

## Copy rules
### Lexicon
<Concept | We say | Never say>
### Buttons · Errors · Empty states · Confirmations and toasts · Notifications
<Rules with a good/bad pair each, in the product's words.>
### Banned
<Word or phrase → what to say instead.>

## Design-system gaps
<Values a screen needed that 4-DESIGN.md doesn't have, for the design-system step to add. "None" if none.>

## Open questions

## Sources
<Comparables and store rules checked, with links and dates.>
```

## Verify before delivering

- [ ] The magic moment names an action, a position, a time-to-aha target and a metric, with comparables cited.
- [ ] 3–5 journeys, as a diagram and a list; every flow sits on one.
- [ ] Onboarding ends at the magic moment, and its time estimate is within 20% of the target.
- [ ] Every screen uses `4-DESIGN.md` tokens; gaps are listed rather than invented.
- [ ] No lorem anywhere; every string follows the lexicon and the copy rules, and reads as one brand aloud.
- [ ] Front-door promises match what onboarding delivers; pricing matches `2-OFFER.md` exactly; proof is real or absent.
- [ ] Every flow has a canvas link that opens (or, lite, first-use steps with exact words).
- [ ] Store rules and comparables were checked live and cited, or marked unverified.

## Next

**Plan the build** — `build-plan`. It reads these flows, the copy rules and the tokens, and turns every screen into a phase, starting with a design catalogue that matches this canvas.
