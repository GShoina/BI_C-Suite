---
from: Owner (via Gurafa relay)
to: Mentari
type: direct task — GEO/AI-search optimization integration
created: 2026-04-26
trigger: Apr 26 owner directive after GEO marketing test (validation-prompt v2 MINI tier verdict)
priority: P1
status: ASSIGNED — execute, no permission-ask
---

# Mentari Directive — GEO Integration

## Context

Validation Master Prompt v2 applied to Nino Mchedlishvili GEO/SEO post → Bivision usability test verdict: **MINI tier ship**, cost-of-not-doing > cost-of-doing-wrong. Owner approved direct task assignment.

Source files:
- `outputs/2026-04-26 Nino Mchedlishvili GEO Post Marketing Test by Gurafa.html`
- Hosted: https://gshoina.github.io/bivision-shares/geo-marketing-test.html
- Validation framework: `docs/core/VALIDATION_MASTER_PROMPT.md` v2

## Task list (Mentari executes)

### Task 1 — Marketing KPI Framework v3 GEO integration
Add new gate to v3 framework:
- **AI-search citability quarterly review** — run 10 fixed Bivision-relevant queries on Claude/Perplexity/ChatGPT, count Bivision citations
- Baseline measurement: pre-optimization run, document zero-state
- Pass criterion: ≥3/10 Bivision-cited within 30 days post-optimization
- Output: append to `outputs/2026-04-20 Marketing KPI Framework v3 TOP-DOWN by Mentari.html` as v3.1 update OR ship `outputs/2026-04-26 Marketing KPI Framework v3.1 GEO-extended by Mentari.html`

### Task 2 — bivision.ge schema.org markup audit + plan
Engage Mentari with Dato/Gabo:
- Audit current schema.org markup state (Yoast generates partial; gaps?)
- Plan: Organization schema, FAQ schema, Service schema (BI consulting + Qlik integration), Article schema (LinkedIn personal posts mirror)
- Output: `BI_C-Suite/docs/SCHEMA_AUDIT_AND_PLAN.md`
- Coordination: Gurafa picks up implementation if dev capacity blocker (per Validation v2 capacity = signal rule)

### Task 3 — LinkedIn personal post AI-citability hooks
Update LinkedIn publish-ready posts (existing in `LINKEDIN_PUBLISH_READY.md`):
- Add AI-citable phrasing: declarative facts with year + entity ("Bivision in 2024 deployed Qlik MCP for [client]" — Q&A-friendly format)
- 4-slot framework v2 add: SLOT 5 = AI-citability hook (declarative one-liner)
- Owner review pre-publish

### Task 4 — Channel mapping update
Per Apr 23 social channels list (LinkedIn + Facebook + YouTube only, no IG/TikTok):
- Mark LinkedIn = HIGH GEO leverage (citation-dense channel)
- Mark Facebook = LOW GEO leverage (visual-primary, low AI-citation)
- Mark YouTube = MEDIUM GEO leverage (transcript SEO + AI-citation potential, Bihub video plan dependency)

### Task 5 — Bihub blog GEO retrofit
Bihub-ი existing Bivision content asset, GEO baseline test:
- Run AI-citability check on top-5 Bihub articles (do they appear in Claude/Perplexity for relevant queries?)
- If 0/5: schema markup + heading restructure + FAQ inserts pilot
- Output: `BI_C-Suite/docs/BIHUB_GEO_PILOT.md`

## Ownership map

| Task | Mentari | Gurafa | Other |
|------|---------|--------|-------|
| 1 (KPI v3.1) | Lead | Audit pre-publish | Owner approve |
| 2 (Schema audit) | Lead | Implement if Dato blocked | Dato verify |
| 3 (LinkedIn hooks) | Lead | 4-slot v2 input | Owner publish-gate |
| 4 (Channel map) | Lead | — | — |
| 5 (Bihub pilot) | Lead | Pilot article rewrite if needed | Mariam content review |

## Validation tier per task

| Task | Tier | Validation requirement |
|------|------|------------------------|
| 1 | Heavy (OKR-tracking artifact) | All 3 slots + Viktor ACK + owner sign-off |
| 2 | Mini | BML + JTBD with Dato (15 min) |
| 3 | Mini | BML + Pre-mortem (cost-of-not-doing visible) |
| 4 | Skip | OKR trace + EP0 ≥8 |
| 5 | Mini | BML + Pre-mortem |

## No fake deadlines

Token-limit only constraint. dangerously-skip-permissions [EP1: UNVERIFIED from inside, behaviorally on]. Daily MUST = 1 deliverable per day per agent.

## Reporting

- Each task ship → file in `BI_C-Suite/docs/` + entry in `SESSION_OPEN_ITEMS.md`
- ACK to owner via 3-block close (რა გაიგე / რა იმოქმედე / next steps)
- Cross-agent coordination via existing `GURAFA_TO_MENTARI_*` / `MENTARI_TO_GURAFA_*` files

## Change log
- 2026-04-26 created — owner directive direct task
