---
name: build-plan
description: >-
  Step 6. Turns the offer, brand, design system and flows into the one plan a coding agent builds
  from — stack, key choices, architecture, data model, core logic, and numbered build phases that
  each end in a test a person can run — and writes docs/6-BUILD-PLAN.md. For an existing codebase
  it baselines the repo and plans current → target, including a move off Lovable, Bolt or Replit.
  Use when the member says "plan the build", "I'm ready to build", or "plan the rebuild of my app".
  Not for building it — work the plan's phases; not for a UX teardown — use product-audit.
---

# Build plan

The step that turns everything decided so far into something a coding agent can build without guessing. Modern models plan software well on their own; what they lack is the member's decisions and a shape that keeps the plan buildable. This skill supplies both: the inputs, the document's sections, a handful of rules, and a real plan to calibrate against. There is no separate spec or roadmap — the plan is both.

It has two modes. **New build** plans from the step documents. **Existing code** baselines what's there first and plans the gap from current to target — the same document, with current → target rows, a keep-or-remove list and a "safe to change" phase 0.

Take the voice of a senior technical lead who ships with coding agents:

- **Cut toward the journeys.** Anything not on a flow in `docs/5-FLOWS.md` is out of version 1, or an open question.
- **Be specific on the page.** Real package names, table and field names, screen references — never "handle auth".
- **Recommend one option**, with the reason tied to this product, and the alternative it beat.
- **Check what changes.** Provider SDKs, integrations and prices are verified live, not remembered.

## Inputs

- `docs/2-OFFER.md` — the customer, the offer, `## Product shape` (`Shape: <slug>`) and pricing. Pricing decides whether there's a payments phase and what it enforces (plans, trial, free tier).
- `docs/3-BRAND.md` — the product name and voice.
- `docs/4-DESIGN.md` — the tokens and components. The plan builds them in its design-catalogue phase and refers to them by name; it never restates a value. Lite mode (brand tokens only) is enough for screenless shapes.
- `docs/5-FLOWS.md` — the journeys, the magic moment, every flow's screens with canvas links, and the copy rules. Every screen lands in a phase.
- The shape's row and notes in [../product-offer/references/shapes.md](../product-offer/references/shapes.md) — its **Build plan** line lists what this plan must cover.
- **Existing products:** the codebase, `docs/0-PATH.md` (the path that sent the member here), and `docs/audit/REPORT.md` when a teardown ran — its `## For the build plan` fixes become phases.
- `docs/5-FLOWS.md` → `## Design-system gaps`: if it lists anything, offer a `design-system` re-run first so the catalogue phase builds the missing values instead of inventing them.

If `2-OFFER.md`, `4-DESIGN.md` or `5-FLOWS.md` is missing or still `Draft`, stop and run that step (`product-offer`, `design-system`, `prototype-flows`); never invent a flow or a price to plan against. The exception is an existing product whose `docs/0-PATH.md` ticks that step as Done: read the product itself for what the document would have said. A `Done` `docs/6-BUILD-PLAN.md` means a re-run: show what would change and ask before overwriting; never untick a box that's ticked.

## Workflow

### 1. Pick the mode and protect the code

**Existing code** applies when there's product source beyond `docs/`, or the app lives on a prompt-to-app platform (Lovable, Bolt, v0, Base44, Replit). Say which mode in one line.

Version history must be on before anything else — the build commits at every phase. No git repository yet: turn it on as `start` → *Version history* says, and tell the member in one line that every change can now be undone.

In existing-code mode, read [references/existing-codebase.md](references/existing-codebase.md) now and run its baseline. On a prompt-to-app platform, also read [references/platform-migration.md](references/platform-migration.md): the move becomes phase 0.

**Done when:** git is on, and the mode is named — with, for existing code, a baseline the member has seen.

### 2. Name the core loop and the cut

Read every input in full before asking anything. Then state the **core loop** in one sentence — the journey from first use to the magic moment in `5-FLOWS.md` — and list what's in and what's out of version 1. Pull the in-list from the flows' screens and the offer's promises; anything on the landing page or listing that version 1 won't do is flagged, because the copy and the product must agree.

Ask the member to confirm the loop and the cut, one question at a time. Never re-ask what the documents answer; state it back.

**Done when:** the member owns one sentence for the loop, and every promise in the copy is either in a phase or in Open questions.

### 3. Choose the stack

Follow [references/stack-options.md](references/stack-options.md): the shape decides the layers; for each, recommend one choice with a reason tied to this product, check it live, and let the member decide anything contested. "No database", "no accounts" and "no payments yet" are real answers. In existing-code mode, start from the current stack and change a layer only for a reason the member agrees with.

Then pick the **key choices** — the two or three decisions that shape everything else (how auth and data fit together, offline or online, where payments are checked). Each gets how it works and the alternative considered.

**Done when:** every layer has a choice with a one-line why, and the member has agreed the key choices.

### 4. Design the parts an agent would get wrong

Write the architecture (one diagram, one paragraph), the data model (every table or collection, key fields, storage and access rules) and the core logic. Core logic covers only what a capable agent would get wrong without being told: state machines, scheduling, entitlement states, sync and retries, ownership rules, anything date-dependent. Leave out what any agent does well unprompted.

Read [references/example-build-plan.md](references/example-build-plan.md) for the depth to aim at. Show the member a short summary of these sections, not the whole text.

**Done when:** every table has an access rule, and every subsystem in Core logic names its edge cases.

### 5. Phase it

Number phases from 0. Each is a checklist of boxes ending in **Done when:** — one test a person can run, on the device the customer uses. The rules:

- **Every phase ends runnable.** Nothing is left half-wired between phases.
- **Phase 0 sets up:** accounts, projects and an empty app that runs where the customer will run it. In existing-code mode phase 0 is "safe to change" instead (see the reference).
- **Phase 1 is the design catalogue** for shapes with screens: the tokens and components from `4-DESIGN.md`, on one hidden screen, checked side by side against the canvas. Features come after. Screenless shapes skip it and apply the Lite brand tokens where they show (a README, emails, a sales page) in the phase that builds them.
- **The core loop next, as simply as it can run** — offline, no account, free — so it's proven before accounts and payments add complexity.
- **Payments get their own phase**, tested end to end in the provider's test or sandbox mode.
- **Settings only the member can set** — accounts, keys, store records, dashboards, DNS — are marked **You:** in their phase and listed again under Only you can set. The agent never invents or hardcodes a secret.
- **The last phase is launch:** beta, the launch requirements, submission or release.
- A phase an agent can't finish in a day or two of sessions is two phases.

Show the phase outline — titles and each Done when — and get the member's approval before writing the boxes.

**Done when:** the member has approved the outline, and every screen in `5-FLOWS.md` appears in a phase.

### 6. Write it, then offer a mirror

Write the document (below). Then offer to mirror it as a Claude Doc for easier reading and comments, if the Claude Docs connector is available; the markdown file in the repo stays the source of truth the agent ticks.

**Done when:** the verify list passes.

## Write docs/6-BUILD-PLAN.md

```markdown
# Build plan: <product name>

Status: Draft
Updated: <YYYY-MM-DD>

<One paragraph: what it is, the platform, the stack in a clause, how many phases, where the screens live (canvas links in docs/5-FLOWS.md).>

## Stack
| Layer | Choice | Why |
<Existing code: | Layer | Current | Target | Keep / change / remove | Why |>

## Key choices
### <Choice>
<The choice, how it works, the alternative considered and why it lost.>

## Architecture
<One diagram (mermaid), one paragraph.>

## Data model
| Table | Key fields | Notes |
<Existing code: current → target with keep / change / remove. Then storage and access rules.>

## Core logic
<One short section per subsystem an agent would get wrong.>

## Keep or remove
<Existing code only: each existing feature against the step 5 flows, with the member's decision.>

## Build phases
<One line on the order and why.>
### 0. <Title>
- [ ] <task>
- [ ] **You:** <a setting only the member can set>
Done when: <a test a person can run>

## Only you can set
- [ ] <account, key or dashboard setting> — needed in phase <N> — <where it's done>

## Launch requirements
<The platform's rules for this shape, built in rather than fixed at submission, then a test checklist.>

## Open questions
- [ ] **<Question>.** <What's undecided, and what decides it.>
```

Set `Status: Done` once the member approves the plan. Building it then shows as ticked boxes; the status stays `Done`.

## Verify before delivering

- [ ] Every section is present (Keep or remove only in existing-code mode), and nothing in the stack contradicts `2-OFFER.md` pricing or the shape's Build plan line.
- [ ] Phases are numbered from 0, each ends in a Done when a person can run, phase 1 is the design catalogue for screen shapes (or phase 0 is "safe to change" for existing code), and payments have their own phase.
- [ ] Every screen in `5-FLOWS.md` appears in a phase; every copy promise is built or in Open questions.
- [ ] Every **You:** box is also under Only you can set, and no secret value appears anywhere.
- [ ] Every provider fact that changes (SDK support, an integration, a price) was checked live and is cited or marked unverified.
- [ ] No design token value is restated; components are named as in `4-DESIGN.md`.
- [ ] The member can say in one sentence what version 1 is and what it isn't.

## Next

**Build it.** The member tells their coding agent to work the plan; the root guidelines `start` wired in tell it how. The essentials:

- Work the phases in order, and the boxes top to bottom. Never start a phase before the previous Done when passes.
- Build each box, run it where the customer would, run the tests, then tick it — the plan always shows the truth.
- At the end of a phase: run its Done when, review the phase's changes (`/review` in Claude Code, or the tool's equivalent; a security review too if it touched sign-in, payments or customer data), fix what it finds, tell the member how to try it in a line or two, and commit with the phase's name.
- Ask for each **You:** setting at the moment it's needed, with exact steps.
- If the plan turns out wrong, stop, say what was found, and change the plan with the member before carrying on. New work goes in as boxes.
- Existing code: if a phase can't be made to pass, go back to the last phase commit (or the baseline tag) after telling the member; never leave the app broken.

When every phase is ticked, the next step is the **security audit** — `security-audit`.
