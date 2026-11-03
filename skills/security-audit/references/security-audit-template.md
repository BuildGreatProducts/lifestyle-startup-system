---
kind: curated
last-reviewed: 2026-11-03
---

# The security audit document

The exact shape of `docs/7-SECURITY-AUDIT.md` — one file, rewritten on each full run, updated in place when fixes are re-checked. Fill every bracket; leave out **Do this right now** when no credential leaked. Every fix's **Verify** line is an assertion an agent can check mechanically — never "improve validation".

```markdown
# Security audit: [product name]

Status: Done
Updated: [YYYY-MM-DD, from `date`]

Scope: [whole product | changes since <commit>]. Stack: [detected, one line]. Build plan: [all phases ticked | phases N–M not built yet].

## Verdict
**[Ready | Ready after fixes | Not ready]** — [one line a founder can act on, e.g. "two problems let any signed-in customer read every other customer's orders."]

[Critical: N · High: N · Medium: N · Low: N]

## Do this right now
[Only when a credential leaked. Each key: where to rotate it, what to update after, how to confirm the old one is dead. Before any code fix.]

## Findings
| # | Severity | Category (OWASP) | Location | What an attacker can do |
|---|---|---|---|---|
[One row per verified finding, severity-ordered. Mark fixed rows "Fixed [date]" rather than deleting them.]

## What's already secure
[Evidence-backed credit, one line each: "Sign-in: Clerk, with the session checked server-side in `middleware.ts:8`." Shows what was checked and passed, and why each N/A is N/A.]

## Attack surface
[The map from step 2, compact: routes and functions with their auth, tables with their rules, public vs secret variables, webhooks, upload paths, agent tools.]

## Agent fixes
> Work top to bottom. Tick each fix only when its Verify line passes.

- [ ] **SEC-001 — [title]** ([severity])
  Files: `path/to/file.ts`
  Change: [the specific change and why].
  Verify: [a checkable assertion — "an unauthenticated GET /api/orders returns 401"; "`git ls-files .env` prints nothing"; "user B's call to `getClip` with user A's id throws".]

## Only you can do this
- [ ] [Rotation, dashboard, hosting or store setting an agent can't do — where to go, what to click, what to update after.]
- [ ] Test it yourself: sign in as customer A, open one of their records and copy its link or ID. Sign in as customer B in a private window and try to open and delete it. Both should be refused.

## Not covered
[What was out of scope (infrastructure, providers' own internals) and what was deliberately not reported (denial of service, theoretical races, hardening with no exploit) — omissions are decisions, not gaps.]
```

## Calibration

> Good verdict: "**Not ready** — the `orders` table has no access rule, so anyone who signs up can read every customer's address."
> Bad verdict: "Several security issues were identified that should be addressed before launch."

> Good finding row: `| 1 | Critical | A01 Broken Access Control | convex/orders.ts:14 getOrder | Any signed-in user passes another user's order id and gets its address and items |`
> Bad finding row: `| 1 | High | Security | orders | Authorization could be improved |`

> Good Verify: "Calling `getOrder` as user B with user A's order id throws `Not found`; the new test in `orders.test.ts` covers it."
> Bad Verify: "Ownership checks are in place."
