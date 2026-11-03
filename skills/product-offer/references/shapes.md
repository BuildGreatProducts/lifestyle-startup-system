---
kind: curated
last-reviewed: 2026-10-01
---

# Product shapes

A product's **shape** is how the customer receives and uses it: the surface it lives on, what "live" means, and what a first sale looks like. `product-offer` picks it and writes it to `docs/2-OFFER.md` → `## Product` as a line `Shape: <slug>`. Later steps read that line and this file: brand identity and design system (full or lite), prototype flows (which flows exist, what the front door is), build plan, go live (what "live" means and the route), and go to market (native channels).

> Shapes are durable; platform fees, review times and store rules are not. **Fee and policy notes last reviewed October 2026** — re-check each one live before quoting it to the member.

## Contents

- [Picking a shape](#picking-a-shape)
- [One primary, secondary, sequenced](#one-primary-secondary-sequenced)
- [The twelve shapes](#the-twelve-shapes)
- [How each shape adapts the later steps](#how-each-shape-adapts-the-later-steps)
  - [web-app](#web-app) · [mobile-app](#mobile-app) · [desktop-app](#desktop-app) · [browser-extension](#browser-extension)
  - [agent-plugin](#agent-plugin) · [agent-skill](#agent-skill) · [mcp-server](#mcp-server) · [chat-assistant](#chat-assistant)
  - [developer-tool](#developer-tool) · [productized-service](#productized-service) · [website](#website) · [digital-product](#digital-product)

## Picking a shape

Ask in this order and stop at the first clear yes:

1. Does the customer pay for an **outcome someone delivers to them**, rather than a tool they operate? → productized-service.
2. Do they **buy it once and download it**? → digital-product.
3. Does it run **inside an AI agent or AI tool** they already use? One capability → agent-skill; a bundle of skills, commands, agents or hooks → agent-plugin; a connection to a system's tools and data → mcp-server; a conversation partner → chat-assistant.
4. Do **developers integrate it** into their own code? → developer-tool.
5. Is the **content, directory or community** the product? → website.
6. Otherwise it's software with a screen. Where is it used — browser (web-app), phone (mobile-app), computer (desktop-app), or on top of other websites (browser-extension)?

Pick by **where the value is delivered**, not how it's built: a web app with an agent behind it is still a web-app; an MCP server with a settings page is still an mcp-server. A shape that asks the customer to leave where they already work needs a reason.

**For a member productizing their own skill**, the honest first shape is often productized-service: deliver the outcome by hand with AI help, learn what clients pay for, then move the proven process into software. The second most common is digital-product or agent-skill, when the member's judgment can be written down.

## One primary, secondary, sequenced

- **One primary shape, always.** It's where the first paying customer gets the value, and it sets every later step's route.
- **Secondary shapes** support the primary (a web-app with an mcp-server so agents can use it; a mobile-app with a one-page website). Each adds its own front door and go-live steps. Add one only when the first version genuinely ships it — "maybe a Slack bot later" is a wish, not a shape.
- **Sequenced products** start as one shape and become another. Record the next shape and its trigger ("move to web-app once 10 clients pay and the process is stable"). The later steps follow the current shape until the trigger fires; then re-run `product-offer` for the shape section.

## The twelve shapes

| Slug | What it is | Has screens? | Live means | First sale looks like | Front door | Native channels |
|---|---|---|---|---|---|---|
| web-app | Software they sign in to in a browser | Yes | Deployed on the member's domain over HTTPS; a fresh account signs up and reaches the magic moment on production | A real customer pays through live checkout (Stripe, or a merchant of record) and the paid plan unlocks | Landing page with price and signup | Search and AI answers, problem communities, Product Hunt / Show HN, AI tool directories, alternatives sites, integration marketplaces |
| mobile-app | An app from the App Store or Google Play | Yes | Approved and publicly downloadable on at least one store; install from the listing and reach the magic moment on a real phone | A real in-app purchase or subscription shows in App Store Connect / Play Console | Store listing, plus a one-page site (badges, privacy and support URLs) | Store search (ASO), store featuring, short-form video, creators |
| desktop-app | An installed Mac / Windows / Linux application | Yes | A signed (and notarized) installer installs on a clean machine without warnings; reaches the first result; the updater finds a newer build | A licence or subscription bought and unlocked (licence-key checkout, store purchase, or a Setapp payout) | Download page with price; store listings if used | "[task] app for Mac" search, OS communities and newsletters, launch platforms, lifetime-deal sites, Setapp, roundups and setup videos |
| browser-extension | An add-on that works on top of sites they already use | Yes (popup, side panel, injected UI) | Approved in the Chrome Web Store (or the persona's browser store); a clean profile installs and reaches the magic moment on a real host site | A paid tier bought through the member's own checkout unlocks features (stores don't take payments) | Store listing, plus a landing page for pricing and upgrade | Store search, the host site's communities, "best extensions for X" roundups, Product Hunt |
| agent-plugin | A bundle of skills, commands, agents, hooks or connectors for an AI agent or coding tool | No | A stranger installs from a public marketplace or repo link and the first documented command produces its output on a clean machine | Paid access (private repo, API key, hosted backend) bought through the member's own checkout and used in the agent | Marketplace listing and README; landing page if paid | Host tools' plugin directories, GitHub "awesome" lists, host tools' Discords and forums, developer X / Reddit / HN |
| agent-skill | One skill or a small pack an agent loads to do a job well | No | A stranger installs from a public link and the documented request produces the first output in a clean session | A paid pack, private-repo invite or download bought through the member's checkout and installed | Directory listing and README; landing page if paid | Skill directories, GitHub, the agent's communities, the persona's professional communities, before/after posts |
| mcp-server | A connector giving AI agents tools and data from a system | No (optional account page) | A stranger connects it to a mainstream MCP client, completes auth, and a clean session finishes the first task against production | A subscription or usage plan paid; the customer's agent makes authenticated calls on it | Registry and directory listings, plus a docs-led landing page | Official MCP Registry, client directories, community directories, the connected system's own communities |
| chat-assistant | An assistant people talk to in a chat surface (custom GPT, Claude Project, Slack / Discord / WhatsApp / Telegram bot) | No (optional web chat) | A stranger opens or installs it from its public link or listing and a fresh conversation reaches the magic moment | Paid access through the member's checkout or the platform's payments, and continued use on the paid plan | Platform directory or bot profile, plus a landing page for pricing | Platform directories, communities already on the platform, short-form video of real exchanges |
| developer-tool | A paid API, SDK or CLI other developers build on | No (optional dashboard) | A stranger signs up, gets a key or installs the package, and the quickstart's first call succeeds against production in the time promised | A subscription, credits or paid usage invoice, and their key making calls on the paid plan | Docs-led landing page, code sample above the fold; registry README | Show HN, GitHub, language communities, technical SEO, package registry search, API / cloud marketplaces |
| productized-service | A fixed-scope outcome for a fixed price, AI behind the scenes | No (optional client portal) | A booking or checkout page is public with price and scope, and one real client has been delivered the outcome end to end through the documented process | A real client pays the stated price (payment link, paid invoice, first retainer charge, or released marketplace funds) | Sales page with scope, price, examples and a booking or checkout button | Warm network and referrals, direct outreach, before/after content on LinkedIn / X, recommendation threads, adjacent providers, freelance marketplaces |
| website | A site whose content, directory or community is the product | Yes | Public on the member's domain with enough content to deliver the promise on day one; a visitor finds what they came for and subscribes, joins or reaches the paid offer | A paid membership, featured listing, paid sponsorship invoice, or first affiliate payout | The homepage itself, plus the subscribe / join / "list your product" page | Search and AI answers, communities asking the questions it answers, newsletter recommendation networks, listed vendors sharing their listing |
| digital-product | A file or package bought once and downloaded or duplicated | No (yes when the product is a visual template) | A public sales page; a live purchase delivers automatically and the buyer reaches the quickstart's first win with no manual step | A real purchase through a storefront, payment link or marketplace, money in the member's balance | Sales page (storefront or own site); marketplace listings | The creator's own audience, the tool's own marketplace (Notion, Figma, Framer), Gumroad Discover / Etsy, "[tool] template for [job]" search, affiliates |

"Has screens?" decides whether the **design system** runs **full** (a token set and components for real screens) or **lite** (brand tokens only, for a README, listing, sales page or deliverables). **Brand identity** follows each shape's own note below: it runs full for some screenless shapes (a chat assistant, a productized service, a digital product), because the brand is the product there.

## How each shape adapts the later steps

Each note covers pricing (what `product-offer` writes) and how brand identity, design system, prototype flows, build plan, go live and go to market adapt. "Watch" is the shape's own trap.

### web-app

- **Pricing:** subscription tiers by default; seats for team tools; usage or credits when each AI action has a real cost; a trial or reverse trial over a permanent free plan unless the product spreads by sharing. Separate the user from the buyer for anything sold to teams. A merchant of record (Paddle, Lemon Squeezy, Polar) costs more per sale but handles sales tax and VAT; with Stripe alone, tax stays the member's job.
- **Brand identity / design system:** full; the name check includes the domain.
- **Prototype flows:** landing page → signup → first screen → magic moment (one in-app event that can be logged) → core loop → paywall and checkout → settings. Front door: landing page.
- **Build plan:** ownership rule for every table, plans and webhooks, AI cost per action and per-plan quotas, transactional email, the magic-moment analytics event.
- **Go live:** host deploy, domain and HTTPS, production database with access rules, payments in live mode with the webhook on production, sending domain verified (SPF/DKIM), error tracking, privacy and terms, smoke test as a real customer. No platform review; the security audit is the gate.
- **Go to market:** warm-network invites set up on a call, answers in live problem threads with a demo clip, a free single-purpose tool page, directory submissions; Product Hunt only once ten real users can vouch.
- **Watch:** settings built before the core loop works; unbounded AI cost on a free plan; test keys in production; "it's just a ChatGPT wrapper".

### mobile-app

- **Pricing:** subscription with a trial behind an onboarding paywall dominates consumer AI apps; weekly plans are common; lifetime unlocks and consumable credits are alternatives. Ads rarely fund AI costs. The store is seller of record and takes 15–30% on digital goods (Apple's Small Business Program and Google's first $1M are 15%); Apple Developer is $99/year, Google Play $25 once. Web-checkout rules differ by region and have been changing. Price minus the store's cut minus AI cost per user is the real margin.
- **Brand identity / design system:** full; the name check covers store search and the 30-character store title; tokens include touch targets, safe areas, dynamic type, dark mode.
- **Prototype flows:** value screens → personalisation questions → permission pre-prompts → paywall → magic moment, all in the first session. Front door: store listing (screenshots and copy), plus a one-page site.
- **Build plan:** every AI and paid-API call through the backend (nothing secret in the bundle); account deletion; in-app purchases via StoreKit / Play Billing, often wrapped by RevenueCat.
- **Go live:** developer accounts (the member, with identity checks) → app records and in-app products → privacy labels / Data safety → listing assets → submit for review → manual release. A new personal Play account must run a closed test before production.
- **Go to market:** ASO, short-form video, creators and UGC; paid installs only once unit economics are known.
- **Watch:** review as a launch-day surprise (submit two or three days early); a paywall before any taste of value; a website in a wrapper.

### desktop-app

- **Pricing:** one-time licence with paid major upgrades (utilities), annual licence with a year of updates, subscription for AI-heavy apps, or free with a Pro unlock. Lifetime deals suit utilities. Direct sale via a merchant of record keeps margin; the Mac App Store trades margin for one-click trust; Setapp pays by usage share.
- **Brand identity / design system:** full; the icon must read at menu-bar and dock sizes; follow platform conventions for menus, window chrome and system fonts.
- **Prototype flows:** download → install → OS permission grants, each explained on the app's own screen first → first result (often automatic). Front door: download page with the price.
- **Build plan:** licence service, auto-updater in version 1, and the channel decided up front (the Mac App Store sandbox forbids some features).
- **Go live:** Apple Developer ID and a Windows signing option (the member) → signed, notarized builds → installers and update feed hosted → download page with checkout → store submissions if used → smoke test on a clean machine of each OS. An unsigned macOS build is effectively unshippable.
- **Go to market:** own download page plus "[task] app for Mac" search, OS communities, launch and lifetime-deal platforms, roundups and setup videos.
- **Watch:** signing left to launch week; raw permission prompts; building three operating systems at once instead of the persona's one.

### browser-extension

- **Pricing:** freemium with a monthly cap on the AI action is the norm; paid plans unlock volume; credits for generation-heavy extensions; lifetime deals for utilities without running costs. The Chrome Web Store charges a one-time $5 registration and takes no payments, so checkout is always the member's own, on a web page the extension opens.
- **Brand identity / design system:** full but scoped: tokens for the popup, side panel and options page, plus injected UI that sits politely on host pages it doesn't control. The icon must read at 16px; the name must not imply the host site's endorsement.
- **Prototype flows:** install → welcome tab → pin prompt → open the host site → first action in the page. The magic moment happens on the host site. Front door: store listing, plus a landing page for pricing and the upgrade checkout.
- **Build plan:** Manifest V3, no remotely hosted code, narrowest host permissions, the account and entitlement backend.
- **Go live:** developer account (the member) → package, listing, privacy disclosures and policy URL → review (days; every update is re-reviewed) → publish, then Edge and Firefox.
- **Go to market:** store search and ratings, the host site's power-user communities, "best extensions for X" roundups, "[host site] + [task]" search.
- **Watch:** permission creep; the host site redesigning overnight; platform dependency — collect emails on install.

### agent-plugin

- **Pricing:** usually a free, open plugin as distribution for a paid product; or paid access to a private repo or marketplace (one-time or annual with updates); or a free plugin whose connectors call a paid hosted backend; or bundled into a coaching or service offer. Price the maintained workflow, not the files — files can be copied. At the last review the main plugin marketplaces charged no listing fee and had no checkout.
- **Brand identity / design system:** lite. The name becomes the install name and command namespace.
- **Prototype flows:** no screens. The flow is install → configure (keys, auth, required tools) → first command → magic moment, written as the README quickstart. The copy rules cover command names, descriptions (the text that decides when the agent triggers them) and every output's shape. Front door: marketplace listing and README; a landing page if paid.
- **Build plan:** one lead workflow and its one command; trigger evals; declared hooks.
- **Go live:** repository with plugin and marketplace manifests → install tested from the marketplace link on a clean machine → official directories that accept submissions → community directories. Any hosted backend follows its own web-app or mcp-server route.
- **Go to market:** host tools' directories, GitHub lists, host tools' Discords and forums, walkthrough videos.
- **Watch:** fifteen skills and no first command; colliding triggers; host-format churn between releases.

### agent-skill

- **Pricing:** a free skill as the top of a funnel (to a paid app, service or community) is most common; a paid pack with updates; a team licence; or a free skill calling a paid API for the part that can't be copied. Expertise-heavy skills (finance, legal, brand) carry higher prices because they encode scarce judgment — this is the natural shape for a member whose skill is a way of thinking.
- **Brand identity / design system:** lite — name, worldview and voice; tokens only for the README and listing, or full if the skill outputs visual documents.
- **Prototype flows:** no screens. Install → the exact first sentence to type → first output, shown as a before/after against the agent without the skill. Front door: directory listing and README; a landing page if paid.
- **Build plan:** the description that triggers it, the structure of every output, dated facts, evals re-run on each major model release.
- **Go live:** skill folder in a repository (private for paid, access granted on purchase) → README with install commands per agent → fresh-install test in a clean session of each → directory listings.
- **Go to market:** skill directories, GitHub, the agents' communities, the persona's professional communities, before/after posts.
- **Watch:** a description that never fires; instructions the agent already follows ("be thorough"); copyable value with nothing behind it.

### mcp-server

- **Pricing:** subscription tiers by call volume or seats, usage per call or record, a free tier with a call cap, or a free connector inside a paid SaaS (then it's a secondary shape). Every tool call has a cost, so the unit should track the costly call. A company buying a connector to its own systems brings security review and SSO into the sale.
- **Brand identity / design system:** lite — tokens for the docs, landing page, consent screen and account page.
- **Prototype flows:** sign up → connect (URL or install, then authorise) → the first prompt to try → an answer only this server could give. Copy rules cover tool names and descriptions (the model reads them) and errors the agent can recover from. Front door: registry and directory listings plus a docs-led landing page.
- **Build plan:** tools designed around the user's tasks, not every upstream endpoint; OAuth; usage limits; no destructive tool triggered by returned data without confirmation.
- **Go live:** remote server over HTTPS with OAuth → signup, billing and limits → tested in at least two clients → official MCP Registry → client and community directories → a local package if supported.
- **Go to market:** the registry and directories, the connected system's own forums and partner ecosystem, developer channels.
- **Watch:** too many tools; prompt injection through returned content; the vendor shipping an official server that eats a thin wrapper.

### chat-assistant

- **Pricing:** per person (coaches, expert assistants), per workspace or seat (team bots), per conversation volume (support bots), or a setup fee plus monthly for an assistant built on a client's knowledge. Custom GPTs and Claude Projects can't be sold per user — treat them as a demo or delivery format. Telegram requires Stars for digital goods; WhatsApp bills per message. Price against cost per active user.
- **Brand identity / design system:** brand full (the name, personality and voice are the interface); design system lite unless there's an embedded web chat.
- **Prototype flows:** no screens. Open or install → greeting → two or three questions that collect the context → the first reply that beats a general chatbot, written as a sample conversation. Front door: the platform directory or bot profile, plus a landing page for pricing.
- **Build plan:** choose the family first — hosted builder (no code, no billing) or bot (a backend, accounts, billing); out-of-scope answers in the evals.
- **Go live:** for bots, backend over HTTPS → platform app registered (the member's developer accounts, a verified WhatsApp number, BotFather) → webhooks on production → billing → install from a clean account → directory submission.
- **Go to market:** platform directories, communities already on the platform, short videos of real exchanges.
- **Watch:** no moat in a prompt that can be extracted; platform policy changes; confidently wrong answers.

### developer-tool

- **Pricing:** usage per call, record or minute with a free monthly allowance; prepaid credits; tiers with included usage and overage; open core with a paid hosted service; per-seat CLIs. The engineer chooses, the lead approves spend; a self-serve card checkout must exist even if big deals are invoiced. Registries take no cut; API and cloud marketplaces do.
- **Brand identity / design system:** lite — tokens for docs, landing page and dashboard; terminal colour conventions for a CLI. The name check covers package names and the CLI command.
- **Prototype flows:** sign up → key shown once → copy-paste quickstart in the persona's language → first useful response (not a hello-world), with its time-to-first-call. Copy rules cover error messages, CLI help and field names. Front door: a docs-led landing page with a code sample above the fold.
- **Build plan:** versioning from day one, the persona's one language first, tight limits or a card on file for expensive endpoints.
- **Go live:** API on the member's domain → dashboard with keys, usage and billing → docs site → packages published from CI (registry accounts with two-factor auth) → quickstart run on a clean machine by someone who didn't build it → status page.
- **Go to market:** Show HN, GitHub, language communities, "how to [task] in [language]" tutorials, docs that coding agents cite.
- **Watch:** docs as an afterthought; breaking changes; free-tier abuse.

### productized-service

- **Pricing:** fixed price per deliverable ("one deck, 48 hours, $X"), a monthly subscription with a capacity limit ("unlimited requests, one at a time"), tiered packages, or a paid diagnostic into the main package. Price on the outcome's value, never on hours — AI makes hours a bad anchor. Payment upfront or a deposit. The margin check is delivery hours × the member's rate + AI and tool costs per client. Freelance marketplaces take a fee on earnings (Fiverr's was 20%).
- **Brand identity / design system:** brand full (a service sells trust); design system lite — tokens for the sales page, proposals and deliverables.
- **Prototype flows:** the client journey, not screens: payment → welcome email → intake form → kickoff → first deliverable → revision → handover and upsell. Front door: a sales page with scope, price, process, examples and a booking or checkout button.
- **Build plan:** the SOP and the tooling behind it (forms, AI workflows, QA checklist, delivery workspace); a portal only if clients need one.
- **Go live:** sales page → payment link or invoice template in live mode → booking link → intake form and welcome email automated → delivery workspace and QA checklist → simple service agreement linked at checkout → the first real client taken through every step.
- **Go to market:** warm network and referrals first, a tight outreach list, before/after posts, recommendation threads, adjacent providers, marketplaces for the first reviews.
- **Watch:** scope creep one favour at a time; custom work in disguise (every client a different process means consulting); never sequencing — hold the member to the trigger, and don't build the app before it fires.

### website

- **Pricing:** paid membership (communities, premium newsletters, libraries), featured or paid listings (directories), sponsorships once there's an audience, affiliate commissions, or a one-time access fee. Define the visitor and, for listing- or sponsor-funded sites, the payer — a directory's first sale usually comes from the listed side. Name the audience size at which sponsorship turns on. Substack takes 10% of paid subscriptions; Ghost and beehiiv charge plans instead.
- **Brand identity / design system:** full; for content and community the brand is the product and the worldview sets the editorial line. Skip what a site builder's theme already fixes.
- **Prototype flows:** arrive → find the thing they came for → subscribe or join → welcome email or post → first return visit; the homepage and the core template (listing, issue, resource page). Front door: the homepage and the subscribe / join page.
- **Build plan:** the content seed (an empty directory fails the first visit) and the update pipeline the member can sustain.
- **Go live:** domain and HTTPS → platform configured → content seed published → subscribe, join or listing purchase in live mode → welcome email and verified sending domain → analytics and Search Console with sitemap → privacy and terms → smoke test as a visitor.
- **Go to market:** search and AI answers, communities asking its questions, newsletter swaps and recommendation networks, listed vendors sharing their pages.
- **Watch:** a rented audience — own the email list; thousands of thin AI pages; monetising a tiny audience.

### digital-product

- **Pricing:** one-time price by default; tiered bundles (basic / pro / with extras); pay-what-you-want with a minimum; a free lead-magnet version with a paid full one; a membership for an ongoing library. Team or commercial licences as a higher tier. A merchant-of-record storefront handles VAT on sales abroad; plain Stripe leaves it to the member. Storefront fees at the last review: Gumroad 10% + a per-sale fee direct (30% via Discover), Lemon Squeezy 5% + a per-sale fee.
- **Brand identity / design system:** brand full (often the creator is the brand); design system lite, or full when the product is itself visual (a Figma kit, a slide template).
- **Prototype flows:** purchase → delivery email → download or duplicate → a "start here" page → first win → day-3 follow-up. Front door: the sales page, plus each marketplace listing.
- **Build plan:** the files tested by someone who didn't make them, the quickstart, the licence terms.
- **Go live:** storefront account with payouts and tax settings (the member) → product uploaded with price, covers and licence → delivery email and "start here" page → sales page → marketplace listings → a real purchase end to end, then refunded.
- **Go to market:** the creator's own audience first, the tool's marketplace, "[tool] template for [job]" search, communities around the tool, affiliates.
- **Watch:** a thin product the buyer could make with one prompt; launching to no audience; one-and-done revenue with no next product.
