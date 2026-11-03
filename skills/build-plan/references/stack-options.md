---
kind: research
last-reviewed: 2026-11-03
---

# Choosing and verifying a stack

How `build-plan` picks the stack: which layers the shape needs, how to choose each, and what to check live before it goes in the plan. Tools, SDKs and prices change monthly, so this holds a method and a few starting points, not a catalogue. Run the checks fresh every time and cite what you found in the plan.

## Contents

- [1. The layers, by shape](#1-the-layers-by-shape)
- [2. How to choose](#2-how-to-choose)
- [3. Verify live](#3-verify-live)
- [4. Starting points by shape](#4-starting-points-by-shape)

## 1. The layers, by shape

| Shapes | Layers to decide |
|---|---|
| web-app, mobile-app, desktop-app, browser-extension | UI framework · backend and database · auth · payments · file storage if needed · analytics · transactional email · error tracking · hosting / build and release |
| agent-skill, agent-plugin | skill format · plugin manifests per host · distribution (marketplace repo, directory, private repo for buyers) · any hosted backend |
| mcp-server | SDK · transport (local stdio or remote HTTP) · hosting · auth · billing and limits |
| chat-assistant | platform (hosted builder or bot) · model API · backend · knowledge · access and payments |
| developer-tool | language and registry · release pipeline · docs · API keys, metering and billing |
| website | builder or framework · content source · hosting · memberships or checkout |
| digital-product | where it's made · storefront and delivery · licence keys if any |
| productized-service | booking · payments · intake · client records · delivery automation · the AI tools the work runs on |

A shape that also runs code on a server (a remote MCP server, a bot, a paid API) takes the app layers for that server too. "None" is a real answer for database, accounts and payments — say so rather than adding a service.

## 2. How to choose

- **Keep what the member already owns and knows.** An existing Stripe, Supabase or domain registrar beats a better tool they'd have to learn. In existing-code mode, every layer starts as Keep.
- **One choice per layer, with the reason tied to this product** ("offline first, so the phone is the source of truth and the server only backs up"). Give the alternative you'd pick if one fact were different.
- **Fewer services.** A backend that is also the database, file store and server functions beats four providers. Each service is another account, bill, key and outage.
- **Managed over self-hosted** for a solo builder, until a bill or a rule says otherwise.
- **Chosen pieces must fit each other.** The integration between two choices (auth ↔ database, payments ↔ backend webhooks) is where plans fail. Prefer pairs with an official, documented integration for this platform.
- **Agents build what they know.** Prefer tools with current docs an agent can read (an MCP server, a docs index such as `llms.txt`, or Context7) and wide use in recent code.
- **Payments by shape:** stores take in-app payments for mobile digital goods; web products need a checkout and someone handling sales tax — a merchant of record does that for a higher fee. The offer's pricing decides plans, trial and free tier; the stack only implements them.

## 3. Verify live

Before a choice goes in the plan, check and bring back, each with a link:

| Check | Where | Bring back |
|---|---|---|
| It supports this platform today | The provider's docs and SDK repo (latest release date, supported platform versions) | The SDK name and minimum OS or runtime version |
| The integration between two choices exists | Both providers' integration docs | The package or guide name (e.g. Chatterbox's `clerk-convex-swift`) |
| Cost at the member's expected volume | Current pricing pages | The free-tier limit and the monthly cost at the plan's launch target |
| Platform rules that constrain it | Store and marketplace guidelines | The rule and its date (e.g. in-app purchase required for digital goods) |
| Data region, if customers are in the UK or EU | The provider's region docs | Which regions it offers |

If web search isn't available, say so, use the starting points below, and mark those rows unverified in the plan's Open questions.

## 4. Starting points by shape

Defaults that were sound at the last review. Treat each as the first candidate, then verify it.

| Shape | Starting point |
|---|---|
| web-app | Next.js · Convex (backend, database, files, functions) · Clerk or Convex Auth · Stripe Managed Payments (merchant of record), or Polar for a simpler developer-first setup · PostHog · Resend · Sentry · Vercel |
| mobile-app | Expo / React Native, or SwiftUI when it's iPhone-only and native feel or offline matters · Convex · Clerk · RevenueCat over StoreKit and Play Billing · PostHog · Sentry · EAS for builds |
| desktop-app | Electron, or Tauri when size and memory matter · a licence-key checkout from a merchant of record · signed and notarized builds with an auto-updater from day one |
| browser-extension | Manifest V3 with a current extension build framework · the web-app backend for accounts and entitlements · checkout on the member's own page (stores take no payments) |
| agent-skill, agent-plugin | SKILL.md folders · a manifest per host the customer uses · a marketplace in a GitHub repo (private, access granted on purchase, when paid) |
| mcp-server | Official TypeScript SDK · remote over Streamable HTTP with OAuth · Cloudflare Workers or Vercel; a local stdio package only when it needs the user's machine |
| chat-assistant | A bot on the platform the customer already uses (Slack for work, Telegram for consumers) on the member's own backend calling the model API; a Custom GPT or Claude Project only to prototype |
| developer-tool | TypeScript on npm (PyPI for Python users) · releases from CI with trusted publishing · Mintlify docs · Stripe usage-based billing for a paid API |
| website | Astro with content in the repo on Netlify or Vercel; Ghost when the newsletter is the product |
| digital-product | Gumroad for storefront and delivery; Lemon Squeezy or Polar when it needs licence keys; a course platform for a course |
| productized-service | Cal.com · Stripe Payment Links · Tally · a Notion client board · Zapier, with the process's prompts versioned in the repo |
