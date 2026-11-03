---
kind: curated
last-reviewed: 2026-10-01
---

# AI-era offer patterns

Read when the product is AI-first, or when a pre-AI anchor in [offer-examples.md](offer-examples.md) doesn't fit. The shapes below tend to be durable; named products, prices, valuations and revenue figures date fast. **Figures as publicly reported up to October 2026; original sources weren't recorded** — re-verify any figure with a web search before quoting it, and cite what you found.

## Customer wedges that are working

- **Vertical AI for regulated professionals** — legal (Harvey-shape), medical scribing, tax and accounting, compliance. Highest ceiling; defended by workflow depth and regulatory posture.
- **AI coding and developer tools** — Cursor, Lovable, Bolt shape. The biggest breakouts of 2025–2026; defended by editor integration and multi-model routing.
- **Prosumer creator tools with a sharp visual demo** — HeadshotPro, PhotoAI, Submagic shape. Spread through TikTok and X; defended by audience and fine-tuned models.
- **Job-to-be-done agents** — Granola (meeting notes), Fin (support resolutions), AI outbound, code-review agents. Defended by workflow integration and outcome-based pricing.
- **"Boring back office" agents** — invoices and payables, audit, compliance documents. Outperform flashy consumer wrappers; defended by integration depth.
- **An expert's judgment, packaged** — the member's own method run by an agent (as a skill, plugin, assistant or service). Defended by proprietary method and data, and by the member's audience; dies when the method is something any model already knows.

## Wedges that struggle

- Horizontal "AI assistant for everyone" — eaten by ChatGPT, Claude and Gemini.
- Thin wrappers on a single prompt — replaced by the next foundation-model release.
- Consumer chat without a defended channel — saturated.
- Generic productivity wrappers competing with native model features.

## Mechanism patterns that signal real moat

"AI-powered" or "uses the latest model" is a feature label every wrapper claims. **The diagnostic: could a horizontal ChatGPT user replicate this in one prompt?** If yes, there's no mechanism yet. A credible AI-era mechanism layers at least one of:

- Proprietary data, with retrieval (RAG) over it.
- Vertical fine-tuning.
- Multi-model routing — so a model retirement is a config change, not a rebuild.
- Deterministic + probabilistic hybrids — rules wrapped around model calls for accuracy-critical work.
- Agentic loops with checkpoints.
- Integration depth into the customer's workflow.
- Audience or distribution as the moat.

For a member productizing their own skill, the strongest layers are usually the first and last: their method and data, and the people who already trust them.

## Guarantee patterns for AI buyer fears

The fears, by name: **hallucination** ("what happens when it's wrong?"), **model deprecation** ("what if the provider retires the model?"), **regulatory exposure** (HIPAA, GDPR, SOC2), **unbounded cost** ("can a power user run up a $5K bill?"). A guarantee should defuse one explicitly:

- Outcome-based pricing — Fin's $0.99 per resolved ticket.
- Bring your own key (BYOK), no markup.
- A named compliance posture in the service terms.
- Soft caps with visible overage.
- Replay and audit logs.
- A human check on every output, for a service.

## AI-specific failure modes to flag

- **Foundation-model absorption** — Jasper-shape risk: the next model release eats the feature. Ask whether the next release could kill this in one feature drop; if "probably", go back to the mechanism (more layers) or the customer (a narrower wedge).
- **Model deprecation churn** — without a routing layer, every retirement is an engineering hit (in 2026 alone OpenAI retired GPT-4o, 4.1, 4.1-mini, o4-mini and the Assistants API).
- **Hallucination tax** — survivors invest in verification, confidence scoring and human checkpoints.
- **Regulatory exposure** — healthcare, legal and tax products without a compliance posture stall at procurement.
- **Trust collapse** — the category is already credibility-shaky; misreported revenue or capability is punished faster than in traditional software. AI proof needs a higher bar: public revenue dashboards, named logos with usage, benchmark or eval scores against a plain model, store and review counts.

## Calibration examples

- **Cursor.** Customer: working engineers. Pain: switching out of the editor to use models. Outcome: AI in the editor. Mechanism: deep editor integration + multi-model routing. Proof: reported ~$2B annual revenue, ~$50B valuation talks.
- **Granola.** Customer: people in back-to-back meetings. Pain: bot note-takers are intrusive. Outcome: rough notes made excellent. Mechanism: no-bot capture + MCP integrations. Proof: reported $1.5B valuation, $125M raise.
- **Harvey.** Customer: lawyers at large firms. Pain: associate-hour document work. Outcome: agents that draft, review and research. Mechanism: vertical legal retrieval + workflow depth + compliance posture. Proof: reported 1,300 firms, ~100K lawyers, ~$190M annual revenue.
- **Fin (Intercom).** Customer: support teams. Outcome: deflected tickets. Mechanism: an agent on top of the helpdesk. Guarantee: pay only per resolution ($0.99). Proof: reported 8,000 companies, ~2M resolutions a week.
- **HeadshotPro.** Customer: knowledge workers needing a LinkedIn photo. Outcome: professional headshots without a studio. Mechanism: fine-tuned image models + delivery UX. Proof: $3.6M annual revenue on the founder's public revenue dashboard, solo.
