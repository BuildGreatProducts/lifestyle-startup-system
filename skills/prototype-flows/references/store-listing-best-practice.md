---
kind: curated
last-reviewed: 2026-10-01
---

# Store listing best practice

> These are curated patterns. Every store's rules, character limits, image sizes, review times and fees change without notice — confirm them live on the store's own developer docs before writing the listing, and cite what you checked (URL and date) in the flows doc. If you can't check, mark every count *unverified*. Figures marked "(Oct 2026 — confirm live)" and the conversion numbers below are re-verified before quoting to the member.

## Contents

- [The rule](#the-rule)
- [Listing anatomy](#listing-anatomy)
- [Screenshot sequence](#screenshot-sequence)
- [App Store and Google Play](#app-store-and-google-play)
- [Browser extension stores](#browser-extension-stores)
- [Agent plugin and skill marketplaces](#agent-plugin-and-skill-marketplaces)
- [MCP directories](#mcp-directories)
- [Chat assistant directories](#chat-assistant-directories)
- [Other marketplaces](#other-marketplaces)
- [Why listings fail](#why-listings-fail)

## The rule

A listing is read as one row in a results list before it is read as a page. Icon, name and one line decide the click; the first visuals decide the install; the store's reviewer decides whether the listing exists at all. On agent surfaces a fourth reader matters: the agent or index matching the listing's text to a request. Write for all of them, inside the exact limits.

Numbers that set the stakes (App Store / Google Play; re-verify before quoting):

| Figure | Number | Source |
| --- | --- | --- |
| Install decisions made on screenshots + video alone | 70%+ | AppTweak 2026 |
| Search-result taps driven by the first screenshot alone | >50% | AppScreenshotStudio, 2,000 pages tested in 2026 |
| Time spent evaluating a listing | 5–10 seconds | AppTweak |
| Conversion lift from a good preview video | +20–35% | Gummicube 2026 |
| Conversion lift from Custom Product Pages | +6.6% non-gaming, +8% gaming | MobileAction |
| 4.6+ rating vs 3.9 in the same category | converts 30–50% better | App Store data |

Both stores now treat listing-view-to-install conversion as a primary ranking signal, and Google Play weights retention. A listing that converts qualified intent outranks one that chases volume — and promising a first result the product doesn't deliver costs ranking twice.

## Listing anatomy

Every listing has these parts, whatever the store calls them. Fill each from the offer doc (customer, outcome, proof, price) and the brand doc (voice, visual style); product nouns match the copy rules in the flows doc.

**Icon.** One bold mark, readable at the store's smallest rendered size (32×32 in App Store search). No fine detail, no text (Apple disallows it). Visibly different from the top five competitors' icons.
- Good: Cal AI's plate with a number; Duolingo's owl.
- Bad: an abstract gradient blob that matches half the category.

**Name / title.** The most heavily indexed field in most stores. Pattern: `Brand: primary keyword` or `Brand — job`, inside the limit and the store's naming rules (no host trademarks where barred).
- Good: "Cal AI - Calorie Tracker" (24/30). "Headway: Books in Minutes". "Clause — contract review for freelancers".
- Bad: "Clause AI Pro" (no job, no search term). "ChatGPT Contract Helper" (borrows a barred trademark).

**Subtitle / short description / one-liner.** The ad in the results row. Names who it's for and the outcome — the magic moment as a benefit — in plain words, with a secondary keyword. Never repeats words already in the name.
- Good: "Just snap. We count." (Cal AI, 21/30). "Flags the clauses that cost freelancers money — before you sign."
- Bad: "An AI-powered assistant that helps with all your legal needs." (no customer, no outcome, category-default words).

**Screenshots or preview.** The strongest proof, and on iOS the first three appear in search before anyone taps. Show the product working inside the host the buyer knows, on realistic content, with a short benefit caption. See [Screenshot sequence](#screenshot-sequence).
- Good: the extension's panel open on a real web page, caption "Every risky clause, highlighted".
- Bad: the logo on a gradient; a stock laptop photo; an empty UI with no caption.

**Long description.** Most stores truncate behind "more", so the first two or three lines must stand alone as the pitch: outcome, mechanism, how fast the first result arrives. Then short scannable sections: what it does, who it's for, how it works, what it accesses, pricing, support. Use only formatting the store renders.
- Bad: a pasted landing page cut off mid-sentence; Markdown shown as raw asterisks.

**Keywords, category, tags.** Put the buyer's own search words in the indexed fields, once each. Pick the category buyers actually browse, not the broadest one. Each tag slot is a distinct real search term.

**Install and first run** (plugins, servers, packages, templates, assistants). The listing is the onboarding entry: exact install line or button text, the first thing to do, what they should see, one troubleshooting line — matching the onboarding flow and tested on a clean setup.
- Good: `/plugin install clause@clause-tools`, then "Try: review contracts/acme.pdf".
- Bad: "Install the usual way and configure as needed."

**Access and data statement.** What it reads, writes and sends, with a one-line justification per permission or scope, matching the privacy policy and the store's disclosure form.

**Pricing.** Shown the way the store shows it — native price field, or a free listing that says plainly where payment happens. Mirrors the offer doc exactly; the store's fee is in the pricing math.

**Proof.** Real ratings, installs, testimonials, press — or the slot is omitted. Pre-launch, lean on the demo visual, the guarantee and the maker's credibility. Never invent a number, a review or a logo.

## Screenshot sequence

This is what the canvas draws: the frames in order, each with its caption above a clean product surface. Write the captions first — they are the story — then the visual for each.

Caption rules:
- 3–7 words, benefit-led, one benefit per frame. "Lose Weight Without Counting Calories", not "Photo Recognition".
- Bold sans-serif, high contrast, at least 36pt at full size so it reads on a 5.4-inch phone (AppScreenshotStudio / App Launchpad guidance). Check legibility at thumbnail size.
- Apple OCRs caption text for keyword indexing, so captions are keyword fields too — feature-led captions rank for the wrong queries.
- No "Easy to use", "The best app ever", "AI-powered", "Modern and intuitive".

**The arc.** Frames 1–3 carry the sale and tell Problem → Solution → Outcome on their own; everything after recovers the buyer who tapped through to evaluate fit.

| Frame | Job | Caption shape | Example (Cal AI) |
| --- | --- | --- | --- |
| 1 — Hook | The outcome the buyer wants; must match the magic moment exactly | Outcome, ≤7 words | "See your calories in one tap" over photo recognition |
| 2 — Mechanism | How the product delivers frame 1's outcome | Mechanism, ≤7 words | "Get your custom plan" over the plan reveal |
| 3 — Proof | Real result evidence: rating, count, before/after, result number | Result, ≤7 words | "Lose 12 lbs in 6 weeks" over a chart + 4.8 rating |
| 4–5 — Depth | One distinct feature each that justifies the install | Benefit per feature | Macro tracking; integrations |
| 6 — Credibility | Press, award, user count or hero testimonial — or swap for a feature until real proof exists | Proof line | "Featured in..." |
| 7 — Next step | Preview of paid value, or "ready to start" — not a paywall | Next-step value | Premium preview |

Ship 5–7 strong frames, not all 10 slots (Apple allows 10, Google 8 — Oct 2026, confirm live). For stores with 3–5 slots (browser extensions, marketplaces), keep frames 1–3 and drop the rest: magic moment in the host → mechanism → proof or result.

**Pick the pattern first** (stop at the first match):

| Product | Pattern | Frames 1–3 show |
| --- | --- | --- |
| Consumer subscription with a personalized AI outcome (Cal AI, Headway) | Outcome-story | problem → personalization → result |
| Creative or generative tool (Lensa, PhotoRoom) | Before/after | input → output, speed as the wow |
| Habit utility (Duolingo, Strava) | Streak / goal | hook → activity → reward (streak, XP, leaderboard) |
| Productivity tool (Granola, Linear mobile) | Workflow | real surfaces with realistic data, named use cases |
| B2B / vertical | Persona-targeted | default page for the main customer; variant pages for adjacent segments |
| Game | Gameplay-first | real gameplay, not menus; the video carries most of the load |
| Stuck | Workflow if it has a UI; outcome-story if the value is AI output on the user's data | |

**Preview video** (where the store has one): ≤30 seconds; auto-plays silently in search, so the first 3 seconds carry it. Open on the wow, not the logo; real product footage only, no lifestyle B-roll; on-screen text on every frame; end on one CTA frame. Cal AI: 22 seconds, photo → recognition → daily total inside 3 seconds. Duolingo: 18-second lesson loop showing instant feedback.

## App Store and Google Play

**Rewards.** Listing-view-to-install conversion (both); retention (Google Play). Title and subtitle are the most weighted fields on Apple; ratings velocity and recency matter more than absolute score (4.6 with 12,000 reviews beats 4.8 with 200).

**Patterns.**
- Title `Brand: keyword`; subtitle a benefit with a second keyword; Apple's hidden keyword field takes the long tail, comma-separated, no spaces, no words repeated from title or subtitle (Apple penalizes duplication).
- Two descriptions. Apple doesn't index the long description, so iOS copy is pure conversion: 3-line hook, 5–7 benefit bullets, one real proof line, premium summary, support contact. Google Play fully indexes it: same structure, primary keyword 3–5 times and secondaries 2–3 times, in natural sentences.
- Custom Product Pages: one per paid campaign whose creative matches the ad; keyword-bound pages for the top 3–5 organic keywords (Apple, since mid-2025). Default page is for branded traffic. Worked example: a finance app with pages for "budget app for students", "freelancer expense tracker", "family budget planner" — reported +10–15% overall conversion across 5 pages.
- Review prompt (`SKStoreReviewController` / Google in-app review API): after 3+ sessions, immediately after a positive event (lesson done, goal hit). Never in onboarding, after an error, or on a timer — timer prompts drag ratings to ~3.5. Draw this moment in the flow.
- Localize creative, not just captions, for the top 5 markets: US-style screenshots in Japan lose 20–40% conversion.
- Refresh every 30–60 days with Apple Product Page Optimization / Google Store Listing Experiments; first test target is frame 1 or the video opener.

**Calibration** (listing-view-to-install): iOS floor 15%, good 25%, best 40%+; Google Play floor 12%, good 22%, best 35%+; first-screenshot impression-to-tap floor 8%, good 15%, best 25%+. Below the floor, the fix is frames 1–3 or the video, almost never the description.

**Why this one fails.** Same text pasted into both stores (loses Android ranking and iOS conversion). Keyword stuffing on Google Play. All 10 slots filled with redundant features. Silent video with no on-screen text. Paid traffic sent to the default page.

**Confirm live:** title, subtitle, keyword field, short and long description limits (Oct 2026: 30 / 30 / 100 / 80 / 4,000 — confirm live); screenshot count and device sizes; preview video length and specs; CPP count (70 per app since Oct 2025) and keyword binding; review guidelines and current review time; developer program fees.

## Browser extension stores

**Rewards.** Clear single purpose, narrow permissions, keyword relevance in name and summary without spam. Review speed itself depends on permissions: broad host access, sensitive permissions and large or minified code slow it down.

**Patterns.**
- Write Chrome first; Edge and Firefox reuse it, re-fitted to their limits. The manifest `name` and `description` are the name and summary, so the listing copy ships in code.
- Frame 1 is the extension's panel or overlay open on a real page doing the job. 1–5 screenshots on Chrome, so frames 1–3 only.
- Every permission gets a one-line justification in the privacy fields; ask for the narrowest set (activeTab over all-sites host access).
- Edge gives up to 7 search terms — each a distinct buyer phrase.

**Store specifics (Oct 2026 — confirm live).**
- Chrome Web Store: name ≤75; summary ≤132 plain text; icon 128×128 PNG with 96×96 artwork and 16px transparent padding; screenshots 1280×800 or 640×400, 1–5, full bleed, square corners; small promo tile 440×280 required, marquee 1400×560 optional; one-time registration fee (commonly $5 — secondary source). Manifest V3 bans remotely hosted code; Limited Use policy; repeating one keyword more than a handful of times counts as spam. Review: days, sometimes weeks.
- Firefox Add-ons: name ≤50 (secondary source); summary ≤250; screenshots 1280×800 recommended, no count limit; no fee. Source code plus exact build instructions required when bundled or minified; obfuscation banned; `data_collection_permissions` required in the manifest for new extensions (`"none"` if nothing is collected).
- Edge Add-ons: description 250–10,000; search terms up to 7, ≤30 chars each, ≤21 words total; logo 300×300 recommended; tiles 440×280 and 1400×560; up to 6 screenshots, 640×480 or 1280×800; free registration; certification up to 7 business days.

**Why this one fails.** Permission surprise (broad scopes with no rationale — rejected or abandoned at the prompt). Logo-on-gradient screenshots that never show a web page. One keyword repeated through the description. Minified code submitted without source.

**Confirm live:** name and summary limits; icon, screenshot and tile sizes and counts; permission-justification and data-disclosure fields; remote-code and source-submission rules; registration fee; current review time per store.

## Agent plugin and skill marketplaces

**Rewards.** A name and description an agent can match to a request, an install that works first time, and a README a developer trusts. In community directories the README is the listing.

**Patterns.**
- Print the exact install lines first. Claude Code: `/plugin marketplace add owner/repo`, then `/plugin install plugin@marketplace`. Then the first prompt to try and what they should see.
- The skill or plugin description is both the one-liner and the text agents match to decide when to load it: what it does, when to use it, when not to. Command, tool and skill descriptions are listing copy too.
- Frame 1 is the agent's real output in the terminal or chat on a realistic task, not a diagram.
- List for every host the product supports (Claude Code / Cowork, Codex, Cursor), each adapted to its manifest fields.

**Store specifics (Oct 2026 — confirm live).**
- Claude Code / Cowork: `plugin.json` needs only `name` (kebab-case); optional display name, version, description, author, homepage, repository, license, keywords. A marketplace is a repo with `marketplace.json` (`name`, `owner`, `plugins[]` with `name` and `source`). Names beginning `claude-` or `anthropic-` are rejected. Anthropic's directory validator has blocked on: README under 40 words, no license, name over 64 chars or not unique, unpinned `npx`/`uvx` versions, embedded credentials. Every version is security-scanned; large repos and binaries go to manual review.
- Codex / ChatGPT plugins: `plugin.json` `interface` block (display name, short and long description, developer, category, capabilities, default prompt, brand colour, icons, screenshots, website / privacy / terms URLs). Same limits as ChatGPT apps: display name ≤30, subtitle ≤30, long description ≤4,000, up to 3 starter prompts ≤128. Plugins with lifecycle hooks can't go in the public directory.
- Cursor: `.cursor-plugin/plugin.json` (only `name` required); must be open source; every update reviewed manually, reported up to ~2 weeks (secondary source).
- Agent Skills format: `name` 1–64 chars, lowercase, digits, hyphens, matching the folder; `description` 1–1,024 chars; optional `license`, `compatibility` (≤500), `metadata`, `allowed-tools`; body under ~500 lines. Skills usually ship inside a plugin marketplace or repo; sold as a download, add a storefront listing.

**Why this one fails.** An untested install line that fails on a clean machine. A vague description the agent never matches ("helps with productivity"). README that opens with badges and philosophy instead of the install line. A name that borrows the host's trademark.

**Confirm live:** required manifest files and fields (`plugin.json`, `marketplace.json`, skill frontmatter); name length and reserved prefixes; directory validator checks; README and license requirements; hook and binary restrictions; review time per host.

## MCP directories

**Rewards.** Clear tool names and descriptions (clients and agents choose tools from them), proven ownership, consistent text across registry, package and README.

**Patterns.**
- List in order: the official MCP Registry → the package registry it installs from (npm, PyPI, container) → client directories (Claude connectors, ChatGPT apps) → community directories.
- One description everywhere: `server.json`, the package description, the README's first line.
- README first screen: one-liner, install / config snippet per client, one example request and its result.
- Separate read and write tools with honest annotations; reviewers check them.

**Store specifics (Oct 2026 — confirm live).**
- Official MCP Registry: `name` 3–200 chars in `namespace/server` form (e.g. `io.github.user/server`); `description` 1–100; `title` ≤100; `version` required, plus `packages[]`, `remotes[]`, `repository`, `websiteUrl`. Namespace proven by GitHub login in `mcp-publisher`, or DNS TXT / HTTP well-known for domains. Package ownership proven in the package: `mcpName` in npm's manifest, an `mcp-name:` line in the PyPI README, a label on container images.
- Claude connectors directory: every tool needs a `title` and `readOnlyHint` or `destructiveHint`; reads and writes are separate tools (no catch-all method parameter); tool names ≤64; no prompt-injection patterns in descriptions; test credentials for a fully populated account; public docs by publish date. Money transfer and AI image / video / audio generation have not been accepted. Listed as community connectors after automated scanning; verification later.
- ChatGPT apps: see [Chat assistant directories](#chat-assistant-directories).

**Why this one fails.** Registry, package and README descriptions that disagree. Ownership proof missing from the package, so publish fails. One mega-tool with a `method` parameter. A test account with an empty workspace, so the reviewer sees nothing.

**Confirm live:** registry schema fields and limits; namespace and package-ownership proof methods; client directory tool-annotation rules, banned categories and test-account requirements; review or scan time.

## Chat assistant directories

**Rewards.** Starter prompts that produce a good answer on the first try, reviewer-ready test accounts, honest AI disclosures. The starters or example commands double as the screenshots.

**Patterns.**
- Frame 1 is a real conversation: the starter prompt and the assistant's answer.
- Write starters as the customer would type them, each a different job.
- Give reviewers a test account, a demo video and positive and negative test cases before they ask.

**Store specifics (Oct 2026 — confirm live).**
- ChatGPT apps directory: verified organization and domain; https privacy, terms, support and website URLs; square icon ≥48px; test account without MFA; 5 positive and 3 negative test cases; video walkthrough. Display name ≤30, subtitle ≤30, long description ≤4,000, up to 3 starter prompts ≤128, up to 20 capabilities ≤120.
- GPT Store: up to 20 knowledge files of 512 MB; instructions ≤8,000 (secondary source); description and starter limits undocumented — check the builder. Reported Aug 2026: personal accounts can no longer create or publish new GPTs (Business, Enterprise, Edu only); builder revenue has been a limited pilot (secondary sources — confirm before planning a GPT Store launch).
- Slack Marketplace: short description ≤10 words; screenshots 1600×1000, under 2 MB; video 30–90 seconds on YouTube; needs 10+ active workspaces or 10 weekly active users before submitting. AI rules: say output may be inaccurate, disclose model, retention and residency, no training on Slack data, human review for consequential decisions, assistant overview ≤25 words. Review time unpublished.
- Discord App Directory: description ≤400, summary ≤200, Markdown expanded description, 1–5 tags; verified app with privacy policy and terms; unverified bots capped at 100 servers. Premium apps: 85% to developer on the first $1M, 70% after (secondary source).
- Microsoft Teams Store: `name.short` ≤30, `name.full` ≤100, `description.short` ≤80, `description.full` ≤4,000, developer name ≤32; Partner Center validation.

**Why this one fails.** Starters that produce a weak or generic first answer. Missing AI disclosures (Slack). Submitting a Slack app before it has 10 workspaces. Planning on the GPT Store from a personal account.

**Confirm live:** eligibility and verification rules; name, subtitle, description and starter limits; screenshot and video specs; test-account and test-case requirements; AI disclosure rules; revenue share; review time.

## Other marketplaces

**Rewards.** For templates and digital products: the preview images and the requirements box (tools, versions, plan level) carry the sale. For developer tools: the README's first screen. Delivery email and thank-you page belong to the onboarding flow.

**Store specifics (Oct 2026 — confirm live).**
- Notion Marketplace: 8% + $0.40 per paid template sale (some localized pages show 10%); sellers apply and are approved first.
- Framer Marketplace: creators keep 100% of paid-template revenue; manual review up to ~21 days; templates must be original.
- Gumroad: 10% + $0.50 per direct sale, 30% via its Discover marketplace; merchant of record; covers ≥1280×720, up to 8; thumbnail 600×600 (secondary source).
- Lemon Squeezy: 5% + 50¢ per sale, merchant of record; sellers being pointed toward Stripe's managed payments (secondary source).
- Etsy (all secondary sources): title ≤140; 13 tags ≤20 chars; up to 20 photos; $0.20 listing fee per four months; 6.5% transaction fee; AI use must be disclosed; selling AI prompts banned.
- Editor marketplaces: VS Code — README is the listing, CHANGELOG beside it, ≤30 keywords, PNG icon ≥128×128 (no SVG), https images only; publish to Open VSX too to reach Cursor, VSCodium, Windsurf. JetBrains — name ≤30, no "Plugin" or JetBrains product names; first 40 chars of the description are the card summary; 40×40 SVG logo; 15% commission on paid plugins; every update reviewed manually.
- Package registries: npm, PyPI, crates.io, Homebrew — README first screen holds the one-liner, install line and a minimal working example; `description` and `keywords` feed search. Publishing is effectively permanent (npm versions can't be reused; `cargo yank` deletes nothing). Homebrew core needs notability (30 forks, 30 watchers or 75 stars; triple if self-submitted) — ship your own tap first.
- API marketplaces: RapidAPI takes 25% since Nov 2025 — price plans with the fee included. Postman API Network: a public workspace; verified badge needs domain verification.
- Shopify App Store, Figma Community, Upwork, Fiverr: not covered by this reference — research fields, fees and review live.

**Why this one fails.** Preview images that hide what's inside. Missing requirements (template needs a paid Notion plan the buyer doesn't have). Price set without the store's cut. Undisclosed AI use (Etsy).

**Confirm live:** fees and revenue share; seller approval; image sizes and counts; title and tag limits; review time; AI and originality rules.

## Why listings fail

- **The name-only one-liner.** Repeats the name or says "the best tool for X" — name the customer and the outcome.
- **The stock UI screenshot.** Empty surface, no caption — the buyer can't tell what it does.
- **The feature caption.** "Photo Recognition" instead of "Just snap, we count" — loses on every test and ranks for the wrong queries.
- **The generic caption.** "Easy to use", "AI-powered" — says nothing, ranks for nothing.
- **Frame 1 isn't the magic moment.** The promise doesn't match the first run; installs churn and ranking drops.
- **The pasted listing.** Same text everywhere, truncated where limits are shorter — count every field per store.
- **The logo-on-gradient visual.** Branding instead of the product working in the host.
- **The untested install line.** Fails on a clean machine and turns a willing buyer into a one-star review.
- **The keyword pile.** Repeated terms in tags and descriptions — stores penalize it, buyers distrust it.
- **The permission surprise.** Broad scopes without a rationale — rejected by reviewers, abandoned at the prompt.
- **The invented proof.** Placeholder ratings or logos of customers who never bought — real or absent.
- **The policy afterthought.** No privacy policy, test account or demo video, found at rejection — build the checklist before the copy.
- **The badly timed review prompt.** During onboarding or after an error — 1–2 star reviews.
- **Microscopic captions.** Sized for a desktop canvas, unreadable on a phone.
- **The stale listing.** Screenshots three versions old, changelog stopped — refresh every meaningful release and at least every 60–90 days.
