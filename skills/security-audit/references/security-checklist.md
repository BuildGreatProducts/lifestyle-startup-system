---
kind: checklist
last-reviewed: 2026-11-03
---

# Security checklist

Every category `security-audit` classifies, in the order it audits them. The tiers are ordered by what actually takes down apps built fast by solo founders, not by OWASP — but tag each finding with its OWASP Top 10 ID (latest edition; Tier 4: the OWASP Top 10 for LLM Applications) for reference. Confirm provider specifics (key formats, dashboard settings, rotation steps) in current docs.

## Contents

- [Tier 1 — the five that took down real apps](#tier-1--the-five-that-took-down-real-apps)
- [Key identity](#key-identity)
- [Tier 2 — High](#tier-2--high)
- [Tier 3 — Medium and Low](#tier-3--medium-and-low)
- [Tier 4 — Agent tools](#tier-4--agent-tools)
- [Never report](#never-report)
- [Always report](#always-report)
- [Stack notes](#stack-notes)

## Tier 1 — the five that took down real apps

Always audited first, whatever the stack.

- [ ] **Secrets exposure** — `.env` or key files tracked in git now or ever (`git ls-files`, then `git log --all --full-history -- '*.env*'`); keys hardcoded in source; secrets behind a public prefix (`NEXT_PUBLIC_`, `VITE_`, `EXPO_PUBLIC_`, `REACT_APP_`) or bundled into a mobile app or extension — customers can read every byte they download.
- [ ] **Database access control** — every table has a rule that scopes it to its owner. Supabase: RLS on *every* table, policies on `auth.uid()`, no `USING (true)` on private data. Firebase: rules require auth and match the owner. Convex: no row-level rules, so every public query and mutation must check identity and ownership itself. Self-hosted: not listening publicly without auth.
- [ ] **Unprotected routes and functions** — from the surface map, every handler where auth doesn't demonstrably run first; admin routes that check sign-in but not role.
- [ ] **Broken ownership checks (IDOR)** — anything taking a resource ID verifies the caller *owns* it, separately from being signed in, on reads **and** writes. The most common real vulnerability in agent-built apps.
- [ ] **Secret keys reachable by the client** — see Key identity. A service-role or live secret key anywhere client-reachable is Critical.

## Key identity

The rules that prevent the worst false positive and the worst miss:

- **Public by design — not a finding:** the Supabase anon key (`SUPABASE_ANON_KEY`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`), Stripe `pk_live_*` / `pk_test_*`, the Firebase web `apiKey`, a Convex deployment URL, Clerk's publishable key `pk_*`, RevenueCat's public SDK key, a PostHog project key.
- **Secret — Critical if the client can reach it:** `SUPABASE_SERVICE_ROLE_KEY`, Stripe `sk_live_*` and restricted `rk_live_*`, Clerk `sk_*`, a Convex deploy key, RevenueCat secret keys, any model-provider API key (OpenAI, Anthropic…), webhook signing secrets.
- **The anon key is safe only because of the access rules.** When RLS is off, the finding is never "anon key exposed" — it's "RLS disabled on table X, so the (correctly public) anon key lets anyone read and write it." Name the real problem.
- A leaked secret is compromised the moment it's committed, whatever the code says now: rotation goes in **Do this right now**, before the code fix.

## Tier 2 — High

- [ ] **Injection** — SQL or NoSQL queries built from input (f-strings, template literals, string concatenation).
- [ ] **XSS through the escape hatches only** — `dangerouslySetInnerHTML`, `innerHTML`, `v-html`, `{@html}`. React, Vue, Svelte and Angular escape everything else by default.
- [ ] **Unverified webhooks** — payment, auth and platform webhooks check the signature or shared secret, and handle retries idempotently (the same event twice doesn't grant twice).
- [ ] **CORS** — wildcard or reflected origins, especially with credentials.
- [ ] **SSRF** — user input controls the **host or protocol** of a server-side request. Path-only is not a finding.
- [ ] **Command injection, `eval`, unsafe deserialization.**
- [ ] **Dependencies** — packages that don't exist on the registry (agent-hallucinated names) or carry known critical advisories. Run `npm audit`, `pip-audit` or the ecosystem's tool; otherwise check the lockfile by hand and say so.
- [ ] **No rate limit on sign-in, sign-up, password reset or one-time codes** — credential stuffing and code guessing are trivial to script. N/A when a managed provider (Clerk, Supabase Auth, Firebase Auth) handles those endpoints — say so.
- [ ] **JWT flaws** — `alg: none`, signatures not verified, no expiry. N/A for provider-verified tokens.
- [ ] **Paid features enforced only in the client** — a paywall the app shows but the server never checks, where the paid thing is server-side (an AI call, an export, storage). Client-only checks are fine for features that live entirely on the device.

## Tier 3 — Medium and Low

Category checks, not per-file findings.

- [ ] CSRF protection and `SameSite` cookie settings, for cookie-based sessions.
- [ ] Security headers on web apps: CSP, HSTS, `X-Frame-Options` or `frame-ancestors`, `X-Content-Type-Options`.
- [ ] File uploads: type checked server-side (not by extension), a server-side size limit, not served from the app's own domain with an executable type.
- [ ] Verbose errors, stack traces or debug mode reachable in production.
- [ ] Personal data (emails, names, payment details, recordings) written to logs or sent to analytics.

## Tier 4 — Agent tools

For agent skills and plugins, MCP servers, chat assistants, and any app where a model calls tools — audited straight after Tier 1. The six categories and how to judge them are in [agent-tools-tier.md](agent-tools-tier.md).

## Never report

- Denial-of-service and resource exhaustion; theoretical race conditions.
- Missing hardening with no concrete exploit ("should add a CSP" is a Tier 3 category line, not a finding).
- Missing auth checks in *client* code — the server owns authorization.
- XSS in React, Vue, Svelte or Angular outside the escape hatches.
- Attacks that need control of environment variables or command-line flags — those are trusted.
- Missing audit logs.
- Findings in docs or test-only files. (For skills and plugins, SKILL.md files, references and prompts are product code.)

## Always report

Enterprise tools often skip these because enterprises have other systems for them; a solo founder doesn't.

- Committed or exposed secrets, in any file, in git history too.
- No rate limiting on the member's own sign-in or code endpoints.
- Vulnerable or non-existent dependencies.

## Stack notes

- **Convex** — check every exported `query`, `mutation` and `action` reads `ctx.auth.getUserIdentity()` (or the app's helper) and filters by owner; functions the client must never call are `internalQuery` / `internalMutation` / `internalAction`. File URLs handed out only after an ownership check. HTTP actions for webhooks verify the signature.
- **Supabase** — RLS per table and per operation (select, insert, update, delete); storage buckets have their own policies; edge functions using the service-role key must check the caller themselves.
- **Firebase** — Firestore and Storage rules both; `allow read, write: if true` anywhere private is Critical.
- **Next.js** — server actions are public endpoints and need their own auth check; middleware matchers that skip API routes; `NEXT_PUBLIC_` on anything secret.
- **Mobile apps** — anything in the bundle is public; model and paid-API calls go through the backend; purchases validated by the store or RevenueCat, entitlements re-checked server-side for server-side features.
- **Browser extensions** — bundled code is public; host permissions as narrow as possible; no remotely hosted code; messages from web pages to the extension validated.
