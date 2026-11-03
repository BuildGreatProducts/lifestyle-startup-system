---
kind: curated
last-reviewed: 2026-10-01
---

# Onboarding best practice

> Read the section for the member's shape plus [Rules for every shape](#rules-for-every-shape); nothing else is needed. The sequences and failure patterns are durable; the named examples and figures are not. **Numbers last reviewed October 2026** and are founder- or vendor-reported (the source is named beside each): re-verify any figure with a web search, and note the source, before quoting it to the member. Figures marked *working target* are targets to design to, not measured benchmarks. Platform rules (store review, permission prompts, manifest versions, plugin and connector formats, skill-description limits) change often: confirm them live against the platform's current docs before writing them into the flows doc.

## Contents

- [Rules for every shape](#rules-for-every-shape)
- [Web app (`web-app`)](#web-app-web-app)
- [Mobile app (`mobile-app`)](#mobile-app-mobile-app)
- [Desktop app (`desktop-app`)](#desktop-app-desktop-app)
- [Browser extension (`browser-extension`)](#browser-extension-browser-extension)
- [Website (`website`)](#website-website)
- [Digital product (`digital-product`)](#digital-product-digital-product)
- [Productized service (productized-service)](#productized-service-productized-service)
- [Developer tool (`developer-tool`)](#developer-tool-developer-tool)
- [Chat assistant (`chat-assistant`)](#chat-assistant-chat-assistant)
- [Agent skill (`agent-skill`)](#agent-skill-agent-skill)
- [Agent plugin (`agent-plugin`)](#agent-plugin-agent-plugin)
- [MCP server (`mcp-server`)](#mcp-server-mcp-server)

## Rules for every shape

- **Time to the magic moment is the metric.** Users who reach "aha" in under 3 days are 90% more likely to become active (Chameleon); top B2B products deliver value in under 8 minutes (ProductLed) against a 1 day 12 hour median (Userpilot 2026).
- **Show value before you ask for anything.** Lovable builds a working app from the homepage prompt box and asks for signup only when the user wants to save it; a website answers the question, then asks.
- **Ask only what the first output needs.** Each signup field above three costs roughly 10% of completions (B2B AI SaaS teardowns). The one exception is the mobile goal quiz, where the questions *are* the personalization — see [Mobile app](#mobile-app-mobile-app).
- **Never open on an empty state.** Linear ships three starter issues; Stripe's test mode ships sample customers; Designjoy's board opens with pre-built cards. Empty workspaces convert at roughly half the rate of pre-populated ones. Label sample content as sample.
- **The first output lands on the customer's own work.** Cursor's first completion is on the user's own repo; PhotoRoom removes the background from the user's own photo. A demo proves it runs; their own data proves it's worth keeping.
- **Name the one next action.** A printed first prompt, 4–6 suggested prompts, or a 3–5 item checklist. Checklists beat tours: 30–82% churn drops (Userpilot); tours are skipped 60–80% of the time.
- **Ask for permissions, payment, and reviews at the moment of value.** Pre-permission screens lift iOS tracking opt-in to ~65% from a 25–35% baseline; behavior-triggered upgrade prompts convert 15–30% vs 2–5% for timed ones (B2B AI SaaS teardowns); review prompts go after a peak-positive event, never on day 0.
- **Say what you read, keep, and send before you ask for access.** Microphone, page content, accounts, files, or pasted documents: one plain statement up front removes the main reason careful users decline.

## Web app (`web-app`)

Pick the sub-variant first:
- **Horizontal / AI tool** — one job that people in many industries do (write, summarize, build, analyze), the buyer is usually the user, and one session can prove it. Default.
- **Vertical / industry tool** — built for one trade or profession, runs a workflow on their business records (jobs, patients, matters, menus), and speaks their vocabulary. Under ~$5K/year per customer run it self-serve and templated; above ~$10K it becomes implementation-led (kickoff plan, data discovery, parallel run, go-live), which is rarely a first product.
- **Creator tool** — a platform where creators publish to an audience (newsletter, community, course, membership). Activation is two-stage: the creator ships, then the audience shows up.

**The sequence (horizontal / AI tool)**
1. Landing page with a live input (prompt box, upload, paste) that produces a real output before signup, when the output can be made without their account data.
2. Signup gate at "save", "export", or "keep building" — SSO (Google; GitHub for developers) above the email field.
3. One routing question ("just you, or your team?"); never more than two before the product.
4. Workspace opens on the artifact they just made, or pre-populated with at least three realistic items.
5. Suggested prompt rail (4–6, each pre-tested to produce a strong answer) → first AI output on their data, showing its sources.
6. The output is saved as a named artifact; a 3–5 item checklist stays visible (connect your data, invite a teammate, run it again).

**The sequence (vertical / industry tool)**
1. Landing page in the trade's vocabulary plus a time-saved calculator with labor-cost defaults pre-filled.
2. Signup → pick your trade or practice → a workspace templated in their terms ("work orders", not "tickets").
3. Import their existing records: CSV templates and importers for the top three tools they're leaving (ServiceTitan ships QuickBooks importers; Toast imports from Aloha, Micros, and Square).
4. First real workflow on their own data — one job scheduled, one invoice sent, one matter summarized.
5. Show the labor saved (hours, steps removed) inside the first 30 days; payments or the adjacent module come after.

**The sequence (creator tool)**
1. Land directly in the editor or creation surface, pre-filled with a placeholder title or a "Welcome" post — no profile wizard.
2. First publish inside 10 minutes (Substack's first post takes 5–7; Skool's first community post under 3).
3. Day 1: import the existing audience (CSV, Mailchimp, ConvertKit) and share buttons on every post.
4. First 10 subscribers inside 7 days; payments are one toggle, and identity checks wait until the first payout.

**Patterns that work**
- **Try before signup.** Lovable went from $0 to $200M ARR with no paid acquisition and reports 85% day-30 retention among paying users (founder interviews); v0 and Bolt run the same pattern. Gate copy reads "Save your work", never "Sign up".
- **Seeded workspace.** Linear's first starter issue contains the keyboard shortcut it teaches; Attio pre-seeds a sample CRM with example deals.
- **Pre-tested prompt rail.** Cursor's "Ask about this file", Granola's "Summarize last week". The first prompt is the highest-stakes prompt; a blank box invites a bad one.
- **Show the work, keep the artifact.** Citations to source documents (Glean), "worked on these 12 files" (Cursor) — trust is decided on the first answer. Gamma drafts a deck, Granola writes a CRM record: something named and kept beats a chat reply that scrolls away.
- **Invite as step two.** 30–50% of activated users of collaborative tools invite someone in week one (OpenView); pre-fill teammates from the email domain; invited users land on the thing they were invited to, not the inviter's onboarding.
- **Card at the value moment.** Card-required trials convert at 31.4% vs 8.9% opt-in (ChartMogul 2026); the middle path asks for the card at a behavior (third invite, usage limit). Reverse trials (premium free for 7–14 days, then downgrade) are used by only 7% of B2B SaaS (ProductLed). Cursor converts 36% of free users vs a 2–5% norm (Sacra), with a visible usage counter and the upgrade at the free limit.
- **Vertical: create a champion.** Harvey reached 80% adoption inside law firms in 45 days by naming an "AI Champion" in each practice group (Harvey case studies). Regulated trades expect compliance badges on the landing page.
- **Creator: the platform brings audience.** Substack delivered 32M new subscribers from in-app discovery in one quarter (Substack metrics); Skool's top communities start with a paid challenge to skip the months of audience-building.

**Why it fails**
- **The tour carousel and the empty dashboard** — the two biggest sources of trial death (see the rules above).
- **The "connect Salesforce first" wall** — an integration before any value; make it a step after sample data, not a gate.
- **The demo-booking wall** — for deals under ~$25K a year, a required sales call loses most signups.
- **The answer without receipts** — no sources, no confidence; buyers are scanning for hallucinations from the first second.
- **Vertical: horizontal vocabulary** — calling a work order a "ticket" tells the buyer you're not from their industry.
- **Vertical: the free trial nobody finishes** — in an import-heavy category, trials create half-set-up accounts; run a short paid pilot with a named success criterion instead.
- **Creator: setup before publishing** — profile wizards and payout forms before the first post lose the most enthusiastic creators.

**On the canvas**
- Landing with the live input (if try-first) and the signup gate at "save".
- The routing question, then the first-run workspace with sample data — draw the empty state as it really appears.
- Prompt rail → first output with sources → saved artifact; checklist, invite with pre-filled teammates, usage meter, behavior-triggered upgrade.
- Vertical: trade picker, import and field-mapping screen with validation errors, first workflow on imported data.
- Creator: editor → publish → import list → share → first-subscriber state.

## Mobile app (`mobile-app`)

**The sequence (goal-first quiz, the default)**
1. Screen 1 is a question, not a splash ("What's your goal?") — the user taps within 5 seconds.
2. 15–25 tappable questions (Cal AI runs ~33, Noom 113), mixed roughly 40% hard data, 30% aspiration, 30% pain ("What's stopped you before?"); progress bar starts at ~10%; at least three visible branches.
3. Permission pre-screen only where the value is already clear, then the OS prompt.
4. "Analyzing your answers" loading screen, 5–15 seconds, with a user count and rotating testimonials.
5. The personalized plan reveal: at least two numbers or artifacts specific to them (daily targets, a timeline).
6. A yes/no commitment screen ("Ready to start today?").
7. Paywall: a review matched to their goal at the top, annual-with-trial selected by default, a weekly or monthly anchor, a trial toggle.
8. On dismissal, one materially different win-back offer.
9. Home screen: the first core action within 60 seconds, and "Day 1" of a streak already showing.

Pick a different opening when: the AI shows a result in under 10 seconds on their own photo, voice, or sentence → **live magic demo**, paywall straight after the first result; the value is tied to an event they're anxious about → **urgency quiz**, weekly plan first (Rizz asks which dating app you use); they're switching from a known competitor → ask which app they're leaving, then show what's better; the value is experiential → run a 60–180 second session inside onboarding (Headspace); it's a utility where a quiz would insult them → three-step demo on their real data, no paywall until session 2.

**Patterns that work**
- **The onboarding is the paywall.** 89.4% of trial starts happen on day 0 (RevenueCat 2026). Hard paywalls convert a 12.11% median install-to-paid vs 2.18% for freemium (RevenueCat 2026).
- **AI apps must earn the trial harder.** Install-to-trial is 5.31% for AI apps vs 10.92% non-AI, but annual-with-trial 1-year LTV is higher, $66.70 vs $49.92 (RevenueCat 2026).
- **A trial on the weekly plan.** Adding one took 12-month LTV from $7.40 to $54.50 (RevenueCat 2026).
- **Screen count follows personalization.** Each screen above five costs 10–15% completion (Adapty) — unless it changes the output, which is why Noom's 113 screens still convert. Ghost found users who completed its progress bar were 10x more likely to pay.
- **The loading screen as social proof.** One productivity app saw +8.5% trial starts, +17% paying conversion, and +22% ARPU from adding it (mobile teardowns).
- **Review above the price.** +72% install-to-trial in RevenueCat case studies.
- **Win-back.** Recovers 15–20% of decliners (Superwall); Cal AI falls back to a $20/year offer.
- **Many trigger points.** Cal AI reached $40M ARR with 46 paywall trigger points and 123 experiments (Superwall case study) — the locked feature, the streak break, the share moment.
- **Review prompt at peak joy** — after the third workout logged or the first milestone; store ranking weights review velocity and recency.

**Why it fails**
- **The three-screen feature tour** — they came from the listing; they already know what it does.
- **The email wall** — signup before value; Blinkist removed theirs and conversion rose. Use Apple/Google sign-in at or after the paywall.
- **The permission prompt on screen 2** — lower opt-in, and it teaches them the app takes before it gives.
- **The reverse anchor** — a weekly price that's cheaper per day than the annual breaks the default.
- **The five-plan paywall** — one default, one anchor, one toggle; never more than three options.
- **The review prompt on day 0** — nothing to anchor it on, and it spends a limited prompt.
- **The hard paywall with no trial** on an AI app — users don't trust the AI until they've seen it work on them.

**On the canvas**
- Question 1, quiz screens showing a visible branch and the progress bar; permission pre-screen and its denied state.
- Loading screen, plan reveal, commitment screen.
- Paywall (default, anchor, toggle, review) and the win-back offer.
- Home with the first core action and the streak seed.
- Confirm current App Store and Google Play rules on subscription disclosure, trial terms, and the restore-purchases control live before drawing the paywall.

## Desktop app (`desktop-app`)

**The sequence**
1. Download page → a signed and notarized Mac build (universal binary), a code-signed Windows installer.
2. First launch to an interactive surface in under a second.
3. SSO sign-in that inherits the web workspace, if there is one.
4. The one setup that makes it the default: set the global hotkey (Raycast offers to replace Cmd+Space), grant the microphone with an explainer (Granola), or point at the menu-bar icon.
5. Every other permission requested individually at the moment of need, each behind an in-app explainer before the OS dialog.
6. First real action → a kept artifact inside 5 minutes; if it completes while they're away (a transcript, a processed file), notify them.
7. In the first session: auto-launch on login, and "make this the default" where an OS default competes.

Pick the opening by type: launcher or command bar → **replace the default**; AI meeting notes or dictation → **microphone first**; inbox or keyboard-driven client → first shortcut action in 5 minutes; wrapper around a web product → existing workspace opens, then the native-only features; menu-bar utility → menu-bar pointer, then first invocation; local AI → model download showing size and progress, then the privacy reassurance.

**Patterns that work**
- **One permission.** Granola asks only for the microphone and gets a first recorded meeting inside 10 minutes; it reached a $1.5B valuation in March 2026 (TechCrunch).
- **The hotkey is the activation event.** Raycast's onboarding *is* rebinding Cmd+Space; if they don't, they've installed an app they'll never open.
- **Local vs cloud is a trust decision.** Local transcription is a privacy pitch (Talat), cloud a speed pitch (Granola) — say which in the permission explainer.
- **Footprint is felt.** Tauri bundles run 2–10MB vs 80–200MB for Electron (Tauri benchmarks); a 200MB download for a small utility reads as "not worth keeping".
- **Their data on first launch.** Notion and Linear desktop open the existing workspace; Superhuman imports Gmail.
- **Permissions reset.** macOS Sequoia re-asks for screen recording roughly monthly and on reboot (Apple support), and microphone access can't be pre-granted by IT — design the re-grant state.

**Why it fails**
- **The unsigned download** — Gatekeeper's warning loses ~30% of installs (desktop teardowns).
- **"Allow all permissions now"** — accessibility, mic, screen recording, and disk access at once, with no context.
- **The slow cold start** — slower than the web version reads as "why did I install this".
- **Hidden shortcuts** — they mouse around for a week and decide it's no faster.
- **The lost menu-bar app** — the main window closes and they can't find it again.
- **The forgotten auto-launch** — opened twice, then forgotten.
- **Manual updates** — users stuck on old versions with bugs already fixed; auto-update on by default.

**On the canvas**
- Download page, first-run window (or the menu-bar popover), sign-in, and the hotkey or default-replacement step.
- A permission explainer for each permission, plus its denied state and the re-grant state.
- Menu-bar pointer; first result and the "your first transcript is ready" notification.
- Auto-launch prompt; the update and what's-new state.

## Browser extension (`browser-extension`)

**The sequence**
1. Install from the member's own site (web-driven), with a plain-language explainer of each permission *before* the store's dialog.
2. Within seconds of install, a welcome tab opens with a screenshot or short clip showing exactly where to pin the icon.
3. SSO sign-in, with "try without an account" where the free tier allows it.
4. A live demo inside the welcome tab — Grammarly opens a text field pre-filled with a typo so the underline fires at once; Honey shows a demo checkout.
5. They open the main host site → the first in-page action (the reply drafted, the page summarized) — the magic moment happens on the host site, not in the extension's UI.
6. Free-tier counter visible in the popup and badge; upgrade prompt on a usage behavior.

Pick the pattern: passive utility (typing, checkout, login) → **silent activation**, no tutorial, react only to detected context; invoked utility (record, capture, save) → **pin, then first invocation within 5 minutes**; page-aware AI agent → **trust disclosure first**, first command on the current page, command budget visible; keyboard power tool → hotkey set-up, first command in 60 seconds.

**Patterns that work**
- **The decision window is minutes.** 86% of users decide within the first few minutes whether to keep an extension (ExtensionBooster 2026).
- **Web-driven install** converts 3–5x cold store browsing (browser-extension teardowns); bounce them back to the page they came from with install detected.
- **Silent detection.** Grammarly activates only in text fields at least 38px tall (Grammarly support); 1Password only on known login pages.
- **Defuse the permission shock.** Loom needs "read and change all your data on the websites you visit" and leads with a "why we need this" page (Atlassian support). Request optional permissions at the moment of need where the platform allows — confirm live.
- **Visible limits, upgrade before the cliff.** HARPA gives 100 free commands and prompts around 75; Loom caps free at 25 videos and prompts at 23; Grammarly prompts premium after the user accepts about 10 free suggestions.
- **The icon is a status surface** — badge counts and active/dormant color, not a static logo.
- **AI extensions** ship a "what we see and what we don't" page linked from the permission explainer and the welcome tab.
- **Reviews and exits.** Ask for a review only after 5+ successful core uses; reply to every store review within 48 hours (Chrome Web Store best practices cite a 50% retention lift); register an uninstall URL with a one-question survey — the only exit feedback the browser gives.

**Why it fails**
- **Permission shock with no explainer** — they read "all your data" and decline.
- **The unpinned icon** — hidden behind the puzzle piece, forgotten within a week.
- **The 20-step tour** — wastes the entire decision window.
- **Global UI injection** — a floating button on every page reads as malware.
- **The hidden free-tier counter** — a surprise paywall produces uninstalls, not upgrades.
- **The premature review prompt** — low ratings and a ranking penalty.

**On the canvas**
- Install page with the permission explainer (and, for AI, the data page).
- Welcome tab: pin visual, sign-in, the live demo.
- Popup or side panel first-run, including signed-out and no-context (dormant) states.
- The first in-page injected state on the main host site.
- Counter near the limit and the upgrade state; the uninstall page. Confirm the store's current manifest version and permission-warning wording live.

## Website (`website`)

**The sequence** — pick by type:
1. **Newsletter with a site — read, then subscribe.** Entry article → inline subscribe box after the value, with a specific promise → confirmation page that delivers a best-of → welcome email at once → the next issue on the promised day. Default when unsure.
2. **Directory or resource library — search first.** Search and filters above the fold → results → detail page with related items → save, alert, or submit as the return mechanism.
3. **Community — read, join, post.** Threads readable without an account → join with minimal fields → an introduction prompt → every first post gets a reply within a day.
4. **Paid content or membership — metered preview.** A few free pieces or a partial article → paywall at a natural break naming what members get → the first members-only piece delivered at once.

**Two-sided marketplace or directory** (suppliers list, buyers find and transact or contact) — the magic moment is the first match on both sides:
1. Pick the harder side (almost always supply) and one tight slice: one city, one category.
2. Hand-onboard the first 100 suppliers; each conversation updates the self-serve flow.
3. Supplier's first listing in under 5 minutes, pre-filled from what you can infer, with a quality pass (rewritten title, better photo) before it goes live, and a demand signal shown at listing time ("12 people searched for this near you this week").
4. New listings get a search boost for their first 7–14 days; buyers with a matching saved search get an alert.
5. Buyer search never returns empty (curated picks, nearby alternatives); the listing page shows the trust signals (verification, reviews, refund or dispute terms); first checkout or contact in under 90 seconds.
6. Review prompt within 48 hours of each transaction; any supplier without a first transaction by day 7 gets a personal message from the founder.

**Patterns that work**
- **Every top entry page is a landing page** — most visitors arrive deep, from search or a shared link; each entry page says what the site is, why to trust it, and where to go next.
- **A trust line and a specific promise.** Worked example (composite): a directory of AI tools for architects whose category page opens with eight tested tools and "Curated by a practicing architect · updated every Tuesday · sponsored listings are labeled"; after the list, "One tested tool for architects, every Tuesday" with an email-only field; the confirmation page shows the year's three most-saved tools.
- **One return mechanism**, one field, asked inline after the content.
- **The confirmation and welcome email deliver something** — the best-of, the starter pack — not just "check your inbox".
- **Marketplace liquidity.** Airbnb's tipping point was 300 listings with 100 reviewed per city (Jonathan Golden, ex-Airbnb); pro photos lifted bookings 40% (Airbnb growth team). Get 50–70% of the core slice matched before expanding (Reforge). Buyers who transact in week one retain 2–4x better than browsers (marketplace teardowns).

**Why it fails**
- **The entry pop-up** — a signup modal before they've read a line.
- **The homepage assumption** — all the effort on a page most visitors never see.
- **The vague promise and the ask pile-up** — "join for updates", plus subscribe, follow, download, and share on one page.
- **The dead-end search** — zero results and nothing else.
- **The ghost town** — first posts with no reply.
- **The stale site** — no update date, or an old one, or a missed cadence.
- **Marketplace: both sides self-serve from day one, or "go national"** — listings everywhere, liquidity nowhere.
- **Marketplace: slow supply onboarding** — document uploads and a review queue before the first listing; verify at first transaction instead.
- **Marketplace: one funnel for both sides** — suppliers and buyers need different copy, milestones, and success metrics.

**On the canvas**
- One top entry page (a deep article or listing, not the homepage): answer above the fold, trust line, next-best link, inline ask.
- Search with filters and the zero-results state.
- Subscribe or join form, confirmation page, welcome email; community introduction prompt; the paywall at a natural break.
- Marketplace: supplier listing flow with the demand signal, buyer search results, listing detail with trust signals, checkout or contact, review prompt.
- Working targets: zero asks before value, a one-field form, welcome email within minutes.

## Digital product (`digital-product`)

**The sequence**
1. Product page with a requirements box beside the buy button (tools and versions, plan level, file formats, skill level, set-up time) and previews of the real contents, including the start-here page.
2. Thank-you page: download or "Duplicate to my [tool]" is the only primary button, with the first win and how long it takes; no upsell above it.
3. Delivery email: subject names the product, the access link sits in the first lines, and it says how to get the link again.
4. One clean download with a top-level "Start here".
5. Start-here page: one first task and its time, a 3–5 item checklist, sample content labeled as sample.
6. The swap: the last checklist item puts the buyer's own data, photo, text, or project into the product — the magic moment.
7. Day 3: an email naming the next win, with the start-here link again; review ask only to buyers who finished the checklist; everyone on the update list.

Pick the opening by type: a template in a host app (Notion, Figma, Framer, Sheets, Airtable) → **duplicate and swap**; a file pack (presets, prompts, fonts, assets) → **install and apply**, install steps per tool, then one item applied to their own file with a before/after; a course or ebook → **first-lesson win**, short enough for one sitting and ending in an exercise that produces something real; a bundle of several pieces → **guided path**, a numbered path with only day one's task visible. Default to the guided path.

**Patterns that work**
- **Worked example (composite):** a Notion finance system for freelancers. Requirements box: "Works on Notion's free plan · desktop or web · 20 minutes to set up". Thank-you page: one button, "Duplicate to my Notion", and "Your first win: log your next invoice — about 10 minutes". Checklist: delete the sample client, add your biggest client, log one real invoice, check the tax set-aside it calculates — the last item is the magic moment.
- **Plain licensing.** One paragraph: client work, reselling outputs, team sharing.
- **Help beside the step** — a short clip or note at the field where people stall, not a long manual.
- **Updates as re-onboarding** — a v2 or bonus pack is a second chance to reach buyers who stalled.

**Why it fails**
- **The expiring link** with no self-serve re-send; **the zip maze** — nested folders, versioned filenames, no entry point.
- **The blank template** — the buyer has to imagine the result.
- **The 90-minute welcome video** before any action.
- **The hidden requirement** — the paid plan or app version revealed after purchase; it becomes a refund.
- **The upsell ambush** — the thank-you page leads with an offer and buries the download.
- **The premature review ask** in the delivery email.

**First-use steps to write**
- The requirements box and preview list; thank-you page copy; delivery email subject, first line, and re-send path.
- File and folder names, starting with "Start here".
- The start-here page: first task, time, checklist, the swap prompt, and the help note for each step.
- Day-3 email, review ask, and update announcement.
- Draw screens only when the product is itself a visual template (its start-here and key pages).
- Working targets: access instant, first use in the same sitting, quick win in 10–20 minutes.

## Productized service (productized-service)

**The sequence**
1. Sales page: delivered-work gallery, price, delivery promise ("first draft in 48 hours"), and "pause anytime, cancel anytime" above the fold.
2. Self-serve checkout, no call (calls only above a deliberate price threshold, around $10K a month).
3. Workspace (Trello, ClickUp, Notion, or a portal) provisioned automatically on payment, invite sent within the hour.
4. Welcome email with a 3–5 minute founder-on-camera walkthrough of the board, plus one personal line about the client's business.
5. Intake brief: multi-step, no more than three questions a step, only what the work uses — brand files, colors, references they like, things to avoid; under 15 minutes.
6. A pre-filled first-request card with three starter options.
7. Acknowledgment with plan and ETA within four working hours.
8. First deliverable on or before the promise; revisions async on the same card, inside the same turnaround.
9. Day-5 personal check-in; a Friday recap of everything shipped.

Pick the opening by service type: a recurring creative asset → **queue** (above); needs access to the client's accounts (SEO, ads, analytics) → **access first**, connect the accounts, audit delivered in 5 days; AI does the draft and a human polishes → AI draft in minutes, polished version within 24 hours; strategy or research → single-page intake, 5-day async audit, 10-minute recorded walkthrough, retainer offer.

**Patterns that work**
- **Designjoy:** one person, ~$2M ARR, ~25 clients at $5,995/month, no calls, no Slack; Trello board within about an hour of payment, first design in ~48 hours (Brett Williams interviews).
- **One active request at a time** — what makes "unlimited" sustainable and turnaround predictable.
- **Structure pays.** Structured onboarding cuts churn 53.5% (Rocketlane 2026); multi-step intake forms lift completion from ~45% to 70%+ (Wayfront); a personalized welcome lifts renewal 65% (OnboardFlow).
- **Quick win in week one.** If the main deliverable takes longer, send something smaller first: an audit summary, a first concept, a recorded "here's what I see".
- **Pause.** 79% of buyers say a pause option affects whether they sign up (Chargebee); 25% of would-be churners pause when offered (Recurly); pause flows save 9.6–15%. ManyPixels charges $10 a month to pause and keep files.
- **The brief compounds.** Add notes after each request ("likes serif headers, no mascots"); with AI in the loop, the brief becomes that client's system prompt.
- **Usage at billing.** "12 deliverables this month" with the receipt; an annual offer with two months free at month 3.

**Why it fails**
- **The mandatory kickoff call** — it turns the product back into an agency.
- **The 7-day ramp** — a week of paying with nothing to show.
- **The empty board** — no "How this works", "Submit a request", or "Brand brief" cards; **the 14-field intake** — "describe your brand journey in three paragraphs".
- **The quiet first week** — silence after payment reads as a black box.
- **Unlimited and concurrent** — destroys turnaround and burns out the founder.
- **The cancel-only flow** — no pause offered before cancel.
- **Slack as the queue** — requests get lost and deadlines slip silently.

**First-use steps to write**
- Sales-page promises (turnaround, scope, pause), checkout confirmation, the provisioning automation and pre-built cards.
- Welcome email and the walkthrough script.
- Intake questions, step by step; the pre-filled first request.
- Templates for acknowledgment, delivery note, revision rules, day-5 check-in, and Friday recap.
- The pause-first cancel flow.
- Draw only the intake form and the portal, if one is built.

## Developer tool (`developer-tool`)

**The sequence**
1. Homepage with working code above the fold in at least three language tabs (cURL first, then JS/TS and Python), and a pricing page with the free tier listed first.
2. Signup with GitHub OAuth above the email field; two fields at most.
3. A working test key on signup — no email verification or KYC gate; verify at the first billing action.
4. Dashboard first-run: their key pre-injected into a runnable sample with a Copy button. If the key is shown once, make saving it unmissable and pre-fill it everywhere it's needed.
5. A pre-populated sandbox, so the first call returns at least three realistic objects, not `[]`.
6. First successful call on their own input → the next step (webhook tester, going-live checklist).
7. Usage dashboard with month-to-date cost and a forecast; upgrade prompt at 75% of the free tier.

Pick the opening: a pure API → **code on the homepage**, test key, first response in under 60 seconds; a platform with a dashboard → provisioned project with a working endpoint (Supabase does this in ~60 seconds); a CLI or local tool → **one install command**, works on their existing repo, first useful output in under 2 minutes; runs in a sandbox → first run in the browser, signup gates save or deploy.

**Patterns that work**
- **Time to first hello world is the metric** — under 5 minutes is the bar, under 60 seconds best-in-class (Moesif, Nordic APIs).
- **Test mode first.** Stripe's `sk_test_` / `sk_live_` prefixes make the environment obvious in code; 80%+ of Stripe integrations finish with no support contact (Stripe DX team).
- **Branch by use case.** Twilio's 2025 redesign (use-case branching, tutorial inside the console, a milestone tracker) lifted first-message activation 62% and production launches within 7 days 33% (Twilio launch post).
- **One-click into a client.** "Run in Postman" gets 2–3x more developers to a working call than raw docs (Postman case studies).
- **Errors that teach.** A stable code, a readable message, the offending param, and a docs URL in every error (Stripe, Twilio).
- **Webhooks solved.** A dashboard "send test event" button plus a CLI forwarder (`stripe listen`).
- **Starter credit** for AI APIs: Anthropic issues ~$5 on new accounts; OpenAI dropped its free credit in July 2025 (console pages, re-verify).
- **Docs for agents.** 40%+ of documentation traffic now comes from AI coding assistants (Daily Dev 2026): ship an OpenAPI spec and `llms.txt`, and test every doc example in CI.
- **Forecast in words.** "At current pace, you'll hit $48 by month-end."

**Why it fails**
- **"Talk to sales"** instead of signup, or **an email-verification pause** before the key.
- **The empty sandbox** — `{"data": []}` reads as broken.
- **One language only** — the Python developer leaves.
- **`{"error": "bad request"}`** with no context.
- **The 30-page quickstart** — first code on screen 12; **hidden pricing** — assumed expensive.
- **Live keys only** — testing against real money or real users.
- **Docs that lie** — the copied example fails, and trust goes with it.

**On the canvas**
- The dashboard first-run: key display, the pre-injected sample, the first-call success state, and an error state with its docs link.
- Usage and billing with the forecast; the upgrade at 75%.

**First-use steps to write**
- The quickstart per language (install, auth, first call, expected response).
- The error catalog; the going-live checklist (webhook signatures, retries, idempotency, rate limits).
- For a CLI: the install line, `--help` text, and the first command's output.

## Chat assistant (`chat-assistant`)

**The sequence**
1. Profile that names the job and the user ("Contract review for freelance designers"), not the technology.
2. 3–4 starters (or the host's limit), each a distinct core use case, written the way users type, tested to produce a strong answer.
3. Greeting under ~40 words: scope, one example, the data line (what's kept and who sees it).
4. At most one question before value — two or three only when personalization is the product and each answer changes the reply.
5. The specific first answer: uses their input and something a general assistant wouldn't produce without heavy prompting — the magic moment.
6. One to three follow-ups; one unprompted capability mention by turn 5.
7. Memory statement (what carries to next time), an opt-in return trigger (digest, reminder), and a designed hand-off (upgrade, booking, human) that says where they're going and what happens to the conversation.

Pick the flow by host: an assistant store → **starter-led** (the default); a Slack, Teams, or Discord workspace bot → the bot DMs the installer a short intro with one try-it command, then the first answer in a real channel, then teammates; WhatsApp, Telegram, or SMS → a link or QR code opens the chat with a pre-filled first message, then opt-in, one question, first answer; needs their documents or accounts → connect, prove it read them by summarizing one real item, then their first question; paid with free turns → useful free answers, then the paywall at a natural break naming what comes next.

**Patterns that work**
- **Worked example (composite):** contract review for freelance designers. Greeting: "Paste a contract or a clause. I'll flag what's risky for a freelancer and suggest wording you can send back. Nothing you paste is used to train models." One question ("fixed-fee or hourly?"), then the three riskiest clauses, each with the risk in plain language and a rewrite, ending "Want a polite email to send these changes to the client?" Asked about tax, it redirects to the payment clauses it does cover.
- **Redirect, don't refuse** — every out-of-scope reply names an in-scope alternative in the brand's voice.
- **Group channels** need brevity and explicit invocation; one-to-one chats can be warmer and longer.
- **The system prompt lists what it can't do** (browse, remember, send) as clearly as what it can.
- Working targets: first useful answer in 1–2 turns; at most one question before value.

**Why it fails**
- **The wall-of-text greeting** — skipped, and the first question comes out generic.
- **The intake interrogation** — five questions before any value.
- **The generic first answer** — indistinguishable from the general assistant one tab away.
- **The dead end** — an answer with no next step; **the wall refusal** — "I can't help with that", and the conversation ends.
- **Persona overload** — jokes and catchphrases before help.
- **The unsolicited ping** — muted or reported in messaging apps.
- **The hidden limit** — the free tier ends mid-answer.

**First-use steps to write** — a sample conversation script:
- Profile name and description; the starters; the greeting, the one clarifying question, and a model first answer for each starter.
- Follow-up suggestions; out-of-scope redirect lines.
- The memory and data statements; limit, upgrade, and hand-off messages.
- Draw screens only for an embedded web chat or an admin dashboard.

## Agent skill (`agent-skill`)

Skills, plugins, and MCP servers share this core; the [agent plugin](#agent-plugin-agent-plugin) and [MCP server](#mcp-server-mcp-server) sections cover only what differs. Every one is onboarded twice: the **human** reads the README, listing, and install message; the **agent** reads the description, command names, and tool schemas, and picks the extension from those words alone. A flawless install is wasted if the agent never loads it.

**The sequence**
1. README or listing: the install line in the first screenful, a before/after on the same request, and the access statement (what it reads, writes, and sends off the machine).
2. One tested install block per supported host, each ending in how to confirm it worked; any runtime (Node, Python, Docker) named before the install line.
3. Zero required settings before the first output — or exactly one credential, asked for in the conversation.
4. The install success message prints the first prompt: *Try: "rewrite docs/launch.md in our voice."*
5. The customer types it (or a natural variant) → the agent loads the skill → the first output lands on their own file.
6. The output names the skill, writes to a file they can open, and ends with one next step.

**Patterns that work (shared)**
- **The before/after is the product shot.** Worked example (composite): a brand-voice skill whose README shows a launch announcement drafted by the agent alone (generic, exclamation-heavy) beside the same draft with the skill (the brand's cadence, banned words gone).
- **Trigger-tested description.** The starter prompt plus at least five natural variants load it; near-misses don't. The brand-voice skill fires on "make this sound like us", "brand voice check", "tone pass" — and not on "translate this". The description says what it does, when to use it, when not to, and what comes back.
- **The description has a budget.** Agent Skills caps the name at 64 characters and the description at 1,024 (format spec, October 2026 — confirm live).
- **A self-check.** One command or tool that reports installed, connected, credentials OK, ready — and names the fix for each failure.
- **Errors both readers can use** — what failed, why, what to try; never a raw stack trace in the agent's context.
- **Slot into an existing loop** — a hook on commit, an end-of-day command, a scheduled report; stable names, a changelog linked from the README.
- Working targets: install to first useful output in under 1–3 minutes, 2–3 steps, the starter prompt triggering correctly 10 times out of 10 in your evals.

**Why it fails (shared)**
- **The README novel** — architecture before the install line.
- **The config maze** — environment variables, a JSON file to hand-edit, and a restart before anything happens.
- **The silent install** — no first prompt, so they type something vague, the agent ignores the extension, and they conclude it doesn't work.
- **The invisible skill** — a description so generic ("helps with writing") it's never chosen, or so broad it hijacks unrelated requests.
- **The demo-only first run** — the first prompt runs on bundled sample text, not their work.
- **The host fight** — custom text "interfaces", or instructions to turn off the host's safety prompts.
- **The breaking update** — a renamed command breaks both the customer's habit and the agent's.

**First-use steps to write (shared)** — the README quickstart, with no wireframe:
- Install block per host and how to confirm; the access statement.
- The first prompt, the expected output, and where it lands.
- The next-step line; the self-check and troubleshooting notes.
- The description text and the list of trigger and near-miss phrasings it's tested against.

## Agent plugin (`agent-plugin`)

Everything in [Agent skill](#agent-skill-agent-skill) applies. What differs:

- **Sequence:** install → configure (keys, MCP auth, required CLIs) → one starter command → magic moment → a help command that lists the rest.
- **Lead with one starter command.** The post-install message names a single command; never open with the full list. The magic moment is the first command whose output shows the whole workflow working — a full PR review posted, a whole spec written.
- **A setup or status command** checks every dependency the plugin needs and names the fix for each one missing; credentials are still asked for in the conversation.
- **Namespace and keep names stable.** Commands sit under the plugin's name and don't collide with common commands; agents, skills, and commands don't overlap in what they claim to do (overlap makes the agent call the wrong one).
- **Hooks are part of the access statement** — say what each hook runs and when, before install.
- **Platform (October 2026 — confirm live):** Claude Code and Cowork plugins come from marketplaces (a git repository with a marketplace manifest); the customer adds the marketplace, then installs with the host's `/plugin` commands. Codex and Cursor have their own manifests and install paths.
- **Extra failure:** **the command menu as onboarding** — twelve commands listed and no starting point.
- **First-use steps to write:** the marketplace-add and install lines per host; the setup command's output for each missing dependency; the starter command and its expected output; the help command's text.

## MCP server (`mcp-server`)

Everything in [Agent skill](#agent-skill-agent-skill) applies. What differs:

**The sequence**
1. Sign up, if the server needs an account.
2. Connect. Local: one tested config snippet (or one-click install link) per client, in tabs, then restart or reload. Remote: add the server URL, then OAuth in the browser — no pasted keys when OAuth is available.
3. The first suggested prompt calls one read-only tool.
4. The answer comes from the customer's own system and cites the records it touched — the magic moment.

**Patterns that work**
- **Read-only first.** Request read scopes first and leave write tools off until the customer enables them; separate read and write tools, annotated read-only or destructive. Curated connector directories have asked for exactly this — confirm current rules live.
- **A first prompt that can't come back empty.** Worked example (composite): a CRM server whose first prompt is "Which of my deals haven't been touched in 14 days?" — read-only, returns results on any active account, cites deal names with links. On an empty account it answers from a labeled demo dataset and says so.
- **Tool descriptions are the agent's onboarding** — fewer, distinct tools with one naming pattern; merge near-duplicates (twenty overlapping tools means the agent picks the wrong one or calls three).
- **A status tool** reports connection, granted scopes, and rate-limit headroom.
- **Account-linked install.** For a companion to an existing product, a "Connect to your agent" button inside the product with credentials pre-filled; the first output names their workspace.
- **API key and dashboard** steps follow [Developer tool](#developer-tool-developer-tool): key issued instantly and pre-filled into the config snippet, usage visible from the first call.
- Working target: remote server with OAuth to first useful output in under 2–5 minutes.

**Why it fails**
- **The over-permissioned first run** — write and delete access before a single useful read.
- **The tool soup** — overlapping names and descriptions.
- **The empty-account first call** — nothing back, which feels like failure.

**First-use steps to write**
- Per-client setup: snippet or one-click link, where it goes, how to confirm.
- OAuth consent copy and the scopes requested, in plain language.
- Two or three starter prompts (read-only first) with the expected results.
- Status tool output and the agent-readable error messages.
- Draw the account dashboard (keys, usage, billing) only if one ships.
