---
kind: checklist
last-reviewed: 2026-11-03
---

# Pre-flight code review

`go-live`'s review of what's about to ship, before anything is deployed. A correctness and release-readiness pass, not a security audit — that's step 7, already done. The output is a short report in conversation and one line in `docs/8-GO-LIVE.md` → Pre-flight.

## 1. Scope

- [ ] `git status --porcelain` — anything uncommitted is either committed or deliberately left out, with the member's say-so.
- [ ] `git ls-files --others --exclude-standard` — read every untracked file. They never appear in a diff, and they're where stray `.env` files land.
- [ ] Review the changes since the security audit's commit in full; skim the rest of the release for the blockers below. If the diff is huge (a formatter pass), scope to what matters.

## 2. Run the repo's own checks

- [ ] Typecheck, lint and tests, from `package.json` scripts, a `Makefile`, `pyproject.toml` or the root guidelines. A failure the release causes is must-fix; one that was already failing is listed as pre-existing. None defined → say so in one line; don't invent a suite.
- [ ] **The production build succeeds** (`next build`, `eas build --profile production`, the archive build, the package build) — not just the dev server.

## 3. Release blockers

- [ ] No test or sandbox keys hardcoded where production needs live ones; every variable the code reads is named in `.env.example` (names only).
- [ ] No secret in the diff, untracked files, manifests or bundled config.
- [ ] No debug flags, verbose logging of customer data, dev-only routes, seeded admin accounts or "skip paywall" switches reachable in production.
- [ ] No TODO stubs returning fake data on the core loop or the payment path.
- [ ] Database migrations needed for production exist and run in order; nothing assumes seeded data.
- [ ] Auth redirect URLs, webhook URLs and API base URLs come from config, not `localhost`.
- [ ] Version number and build number bumped where the platform requires it (stores, registries, plugin manifests).
- [ ] The security audit's carried Medium items: fixed, or deferred with the member's say-so and a reason.

## 4. Five lenses over the release

One pass per lens, gathering candidates before reporting anything:

1. **Correctness** — does the core loop do what `docs/5-FLOWS.md` says, on every path it touches?
2. **Regressions and contracts** — changed signatures with un-updated callers, removed exports still imported, schema changes against the queries that hit them, API changes against the screens that read them.
3. **Edge cases and errors** — failure paths, and loading, empty and error states on customer-facing screens.
4. **Security, thin** — only the two commit-blockers: a hardcoded secret, a new route or function with no auth check. Anything deeper → note it for a re-run of the security audit.
5. **Consistency** — the codebase's own patterns, leftover debug output, commented-out blocks; UI values that bypass `docs/4-DESIGN.md` tokens.

## 5. Prove, then report

- [ ] Every behavioural claim cites `file:line` in real source — never an inference from a name. Confirm the broken caller exists and is reached.
- [ ] Real but pre-existing issues are labelled pre-existing, not blamed on this release.
- [ ] Cut anything you wouldn't raise on a colleague's pull request. Never flag what a linter or CI already enforces.

Report: a one-line tally first ("2 must-fix, 1 consider"); **must fix**, numbered, each with what, why a customer would hit it, `file:line` and the specific fix; **consider**, at most five; **pre-existing**; one line of genuine credit; and the verdict — **Ready to ship** or **Not ready — fix the N must-fix items first**. Always explicit.

Re-reviews converge: after fixes, re-check the must-fix items only, no new nits. A clean release getting a fast "Ready to ship" is a normal outcome.
