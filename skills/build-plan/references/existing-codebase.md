---
kind: curated
last-reviewed: 2026-11-03
---

# Existing-code mode

When the product already exists, `build-plan` writes the same `docs/6-BUILD-PLAN.md` — but from a baseline of what's there, as a plan from **current** to **target**. The target is what steps 2–5 now say the product should be; the gap is the build.

## Contents

- [1. Protect the working version](#1-protect-the-working-version)
- [2. Baseline the repo](#2-baseline-the-repo)
- [3. Find the differences](#3-find-the-differences)
- [4. Decide each one with the member](#4-decide-each-one-with-the-member)
- [5. Write current → target](#5-write-current--target)
- [6. Phase the gap](#6-phase-the-gap)
- [Verify](#verify)

## 1. Protect the working version

Before anything is read closely, make sure the member can always get back:

1. Uncommitted changes → ask the member to let you commit them first, so the baseline is the version that works today.
2. Get the date with `date +%Y-%m-%d`. Branch and tag: `git switch -c rebuild/<date>` and `git tag pre-rebuild-<date>`.
3. Tell the member in one line: "Your working version is saved; I can put it back at any time."

On a prompt-to-app platform, do this on the first export instead — [platform-migration.md](platform-migration.md) owns that order.

## 2. Baseline the repo

Read before judging. Record a short **Baseline** in conversation (it goes into the plan's opening paragraph and Stack table, not a separate file):

- **What's there** — structure, stack and versions from the dependency files, data model from the schema or migrations, screens or commands from the routes, integrations (auth, payments, email, analytics, error tracking), deploy config.
- **What works** — run it locally and walk the core loop. Run the tests and note how many pass. "Builds but sign-up fails on a fresh account" is a baseline fact; "looks fine" is not.
- **What the docs say** — `docs/0-PATH.md` (why the member is here) and `docs/audit/REPORT.md` (the teardown's verdict and top fixes), when they exist.

> Good: "Next.js 14 + Supabase. 11 routes, 6 tables, RLS on 4 of them. Stripe checkout works in test mode; no webhook, so cancelled plans stay active. 23 of 31 tests pass. Runs locally after adding 3 env vars that aren't in `.env.example`."
> Bad: "A Next.js app with Supabase and Stripe. Mostly working."

## 3. Find the differences

Compare the baseline with the target — `2-OFFER.md` (pricing and shape), `4-DESIGN.md` (tokens), `5-FLOWS.md` (journeys and screens) — and sort every difference:

| Kind | Means | Example |
|---|---|---|
| **Missing** | The flows need it; the code doesn't have it | The paywall in the onboarding flow; a magic-moment analytics event |
| **Divergent** | Both have it, differently | Onboarding has 7 screens, the flow has 4; colours hardcoded instead of tokens; a different auth provider than the target stack |
| **Extra** | The code has it; no flow needs it | A team-invite feature with no users; an abandoned AI chat page; three unused packages |

Each with its evidence (file paths) and a one-line cost. Fold in the audit's top fixes: each becomes a Missing or Divergent item, tagged with its severity from the report.

## 4. Decide each one with the member

One at a time, never a wall: what was found, what the flows say, a recommendation (keep / change / remove / later) and what each option costs. Group trivially related items. Every **Extra** needs an explicit keep-or-remove; every **Divergent** says which side wins, the code or the step document. If the member keeps something no flow covers, say that `5-FLOWS.md` should gain it and offer to re-run `prototype-flows` afterwards — don't edit that document yourself.

Write decisions into `docs/6-BUILD-PLAN.md` as they're made — the Keep or remove section, `Status: Draft` — so an interrupted session loses nothing. To resume, read that section and carry on from the first undecided item.

Calibrate "remove" honestly. Features with real users or revenue behind them are rarely removed in one step — hide them from new customers first, remove later.

## 5. Write current → target

**Stack** and **Data model** carry both sides:

| Layer | Current | Target | Decision | Why |
|---|---|---|---|---|
| Database | Supabase, RLS on 4 of 6 tables | Supabase, RLS on every table | Change | Two tables are readable by any signed-in user |
| Payments | Stripe Checkout, no webhook | Stripe Managed Payments + webhook | Change | Cancellations never reach the app |
| AI chat page | `app/chat/*` | — | Remove | No flow uses it; 0 sessions in 30 days |
| Email | Resend | Resend | Keep | Works; sending domain verified |

**Keep or remove** lists each existing feature against the flows, with the member's decision and one line of why:

```markdown
## Keep or remove
| Feature | In the flows? | Decision | Why |
|---|---|---|---|
| Team invites | No | Remove | No team plan in 2-OFFER pricing; 2 invites ever sent |
| CSV export | Settings flow, screen 5.3 | Keep | Promised on the pricing page |
```

## 6. Phase the gap

**Phase 0 is "safe to change"**, every time:

- [ ] Version history on; baseline branch and tag exist.
- [ ] The app runs locally from a clean clone, with every needed variable named in `.env.example` (names only, no values).
- [ ] A smoke test of today's core loop passes — written down so later phases can re-run it.
- [ ] Existing tests run; the ones that fail today are listed, not silently fixed.

Done when: a fresh clone runs, and the smoke test passes.

Then, in this order, each phase still ending in a Done when:

1. **Removals** — what was decided Remove goes first, cleanly, so later work isn't built around dead code.
2. **Foundations** — stack changes and data-model changes, with a migration for live data and a way back.
3. **Design catalogue** — the `4-DESIGN.md` tokens and components replacing hardcoded styles, checked against the canvas.
4. **The gap, by journey** — Missing and Divergent items grouped by the flow they serve, the core loop's first; the audit's Critical and Major fixes before its Minor ones.
5. **Launch** — as in a new build.

Rules for every phase: the app stays runnable; existing tests keep passing, and a deliberate behaviour change updates its tests in the same box; decisions already made aren't relitigated during the build.

## Verify

- [ ] Baseline branch and tag exist, and the member knows how to get back.
- [ ] Every Extra has keep-or-remove; every Divergent says which side wins; no item is left undecided.
- [ ] Stack and Data model show current → target with a decision on every row.
- [ ] Phase 0 is "safe to change"; removals come before rebuilds; every phase leaves the app runnable.
- [ ] The audit's top fixes (when there was an audit) each appear in a phase.
