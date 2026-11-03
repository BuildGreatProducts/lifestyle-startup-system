# CLAUDE.md

<!-- BEGIN LIFESTYLE STARTUP SYSTEM -->
## This product runs on the Lifestyle Startup System

- The system takes the product through nine steps, each run by one skill and each writing one document to `docs/`: `1-IDEA.md`, `2-OFFER.md` (customer, offer, product, pricing), `3-BRAND.md`, `4-DESIGN.md` (+ `4-DESIGN.html`), `5-FLOWS.md`, `6-BUILD-PLAN.md`, `7-SECURITY-AUDIT.md`, `8-GO-LIVE.md`, `9-GO-TO-MARKET.md`. An existing product's path is `docs/0-PATH.md`; a product teardown lives in `docs/audit/`. These documents are the source of intent — don't guess at product decisions they already answer.
- Each document's `Status:` line (Draft, Done, Extracted) says where that step stands. The product's shape is in `docs/2-OFFER.md` → `## Product`; it decides what "live" means.
- Not sure what's next? The member can just say **"continue"**: the `start` skill reads where they are and runs the next step.
- **Talk to the member in plain English** — many members aren't technical. Say what a step does for them, not its number or skill name. Explain a technical term in a few words the first time it comes up. Show commands, file paths and skill names only when the member asks or has to act on them. Do the mechanical work yourself — git, moving files, running scripts — and say what you did in one line.
- **When a session opens with no task in hand** ("hi", "where was I?", "what's next?"), tell the member in two or three lines where they are and what saying "continue" will do.

### Building from the plan

- `docs/6-BUILD-PLAN.md` is the build plan. Work its phases in order from 0; never start a phase before the previous one's **Done when** test passes.
- Within a phase, work the unticked boxes top to bottom: build it, run it where the customer would, run the tests, then tick it in the plan straight away, so the plan always shows the truth.
- Use the plan's stack and the design tokens. Never swap a provider or invent a colour, font or spacing value.
- A **You:** box is a setting only the member can set (accounts, keys, dashboards): ask for it when it's needed, with exact steps. Never ask for a secret in chat; never invent or hardcode one.
- At the end of each phase: run its **Done when** test, review the changes (plus a security review if the phase touched sign-in, payments or customer data), fix what the review finds, tell the member how to try it in one or two lines, and commit as `Phase N: <title>`.
- If building shows the plan is wrong or work is missing, stop, say what you found, and update the plan with the member's agreement before carrying on. New work goes in as boxes in the plan, not as side tasks.
- Existing code: the plan's keep-or-remove decisions are final. If a phase can't pass, tell the member and offer to reset to the last phase commit (or the `pre-rebuild-<date>` tag).
- When every box is ticked, the next step is the security audit (`docs/7-SECURITY-AUDIT.md`), then go live.
Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## 5. Design Fidelity

**The design system is law. Reference `docs/4-DESIGN.md` for every frontend change.**

Before writing or changing any UI code:
- Read the relevant sections of `docs/4-DESIGN.md` — token YAML and component specs — and the screen's design in `docs/5-FLOWS.md` (its canvas link).
- Every color, font, size, spacing, and radius comes from a token. Never hardcode visual values.
- Reuse existing components before creating new ones. New components are built from the tokens.
- If a design need isn't covered by `docs/4-DESIGN.md`, flag the gap and ask - don't invent styling.

## 6. Secure by Default

**Insecure code that works is not done. These are not optional.**

- Never hardcode or commit secrets — environment variables only, and never behind a public prefix (`NEXT_PUBLIC_*`, `VITE_*`, `EXPO_PUBLIC_*` ship to every browser).
- Authorization lives server-side: check *ownership* of the resource, not just that someone is logged in. Client-side checks are UX, not security.
- Every database table gets access rules from day one — RLS policies scoped to the user in Supabase, auth-required rules in Firebase. A table without rules is public.
- Parameterized queries only — never build SQL from user input.
- Verify webhook signatures (Stripe, Clerk, GitHub) before trusting the payload.
- `service_role` and `sk_live_` keys never reach the client. The anon key / `pk_live_` are public by design — that's fine *because* the rules above hold.

## 7. Copy Fidelity

**The brand voice and copy rules are law. Reference `docs/3-BRAND.md` and `docs/5-FLOWS.md` for every user-facing string.**

- Before writing or changing UI text, read the voice in `docs/3-BRAND.md` and the copy rules in `docs/5-FLOWS.md`; use the screen's copy from the canvas where it exists.
- Use the product's own words for its things. Never introduce a synonym for an existing concept.
- The mechanical rules are fixed: sentence case, no terminal periods on labels or buttons, active voice, second person, present tense, numerals.
- Errors say what happened, why, and what to do next. Buttons say what they do ({Verb} {noun}). Never "Are you sure?", never bare "OK" on consequential actions.
- If a copy need isn't covered, flag the gap and ask — don't invent voice.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, clarifying questions come before implementation rather than after mistakes, no hardcoded style values appear in any diff, and no off-brand terms or banned phrases appear in UI strings.
<!-- END LIFESTYLE STARTUP SYSTEM -->
