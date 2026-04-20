---
from: mentari
to: owner
type: ⚠️ REC — Marketing Truth & Action Layer, Execution Plan v3
ep0: 9/10 (O)
tier: spot-check
status: v3 pending owner final approval (v1 + v2 superseded, session-only)
created: 2026-04-15
supersedes: Marketing Truth & Action Layer v1, Execution Plan v2 (both session-only)
audit: docs/AUDIT_REQUEST.md (filed 2026-04-15, Viktor post-factum)
---

# Marketing Truth & Action Layer — Execution Plan v3

## Priority Order

| # | Task | EP0 | When | Standalone file |
|---|---|---|---|---|
| 1 | LinkedIn 10K Battle Plan | 9 | today-tomorrow | docs/LINKEDIN_BATTLE_PLAN.md |
| 2 | Facebook Operating Policy | 9 | today | docs/FB_OPERATING_POLICY.md |
| 3 | Marketing Dashboard = Decision Layer | 9 | tomorrow 17:00 | spec below; dashboard.html edit |
| 4 | Competitor Intelligence (signal-only) | 6 | next wave | Gurafa-owned |
| 5 | AI Impact Assessment | 7 | next wave | scope below |
| 6 | Dashboard cleanup | — | folded into #3 | — |
| 7 | Owner performance groundwork | 5 | low priority | data collection |

## Ownership Map

| Area | Mentari | Gurafa | Mariam | Owner |
|---|---|---|---|---|
| LinkedIn segmentation + scripts | builds | — | — | approves, publishes, does outreach |
| Facebook policy + forensic | writes policy, extracts data | — | executes approved policy | approves policy |
| Dashboard Decision Layer | builds, maintains | — | reads Mariam view | reads, decides |
| Competitor monitoring | coordinates | owns: daily scan, weekly signal report | — | reads signals |
| AI impact | structures | research + analysis (next wave) | — | decides |
| HubSpot pipeline | structures dashboard section | — | — | owns: calls, deal updates |
| Content (posts, reels) | drafts, calendar | — | visuals, publishes | approves CEO posts |
| Churn protection | flags at-risk, scripts | — | support contact | proactive top-5 contact |

## Dashboard Decision Layer v1 — thin scope

**New tab:** "Decision Layer" — 4 sections on one screen.

```
┌─ WEEKLY TRUTH (Mon-Sun) ──────────────────────────┐
│ Leads in: X  |  Deals closed: Y  |  Pipeline Δ: Z │
│ Top channel: [name]   Waste flag: [name if any]   │
└───────────────────────────────────────────────────┘

┌─ WHAT WORKED ──────┬─ WHAT FAILED ──────────────┐
│ • 2-3 items        │ • 2-3 items                │
│ • with evidence    │ • with evidence + why      │
└────────────────────┴────────────────────────────┘

┌─ WHAT NEXT (this week) ─────────────────────────────┐
│ Owner action:   [item + deadline]                    │
│ Mentari action: [item + deadline]                    │
│ Mariam action:  [item + deadline]                    │
│ Blocked:        [item + blocker]                     │
└──────────────────────────────────────────────────────┘

┌─ OKR SNAPSHOT ──────────────────────────────────────┐
│ Q2 targets: 3 rows, % progress, color               │
└─────────────────────────────────────────────────────┘
```

- **Owner view:** all 4 sections
- **Mariam view:** "What Failed" + "What Next (Mariam action)" only
- **Update cadence:** Monday 09:00 — Mentari auto-compiles from HubSpot + FB + LinkedIn + GA4 of prior week
- **NOT in v1:** deal attribution by channel (waiting HubSpot update), campaign-level detail, historical trending. → v2
- **Effort:** ~4h — one HTML tab + weekly data pull script

## AI Impact — what can start without competitor input

**Internal-only, Mentari-driven:**

| Layer | Startable now | Source |
|---|---|---|
| Threat: AI replaces what Bivision sells | ✅ | BiFinance/BiMedical/BiRetail feature inventory × GPT-4/Claude capability map |
| Threat: clients build DIY with LLM | ✅ | 29-account contract analysis — dashboards (at risk) vs integrations (moat) |
| Opportunity: compress delivery | ✅ | Current project hours/cost → AI-accelerated estimate; margin lift |
| Opportunity: AI-wrapped product tier | ✅ | "Ask your data" layer on BiFinance — scoped as add-on SKU |
| Capability gap: team AI fluency | ✅ | Skills audit (self-reported) |
| Competitor moves | ❌ | Needs Gurafa |
| Market AI adoption Georgia | ❌ | Needs Gurafa + market research |

**First deliverable (target 2026-04-20):** AI Impact — Internal Map. 70% of decision-usefulness without market/competitor layer. Gurafa input = enhancer later, not blocker.

## Underestimated leverage (flagged)

Churn protection > new leads, short-term.

- ✅ FACT: Revenue 1M → 942K declining; churn = champion dependency (4/9)
- ⚠️ REC: One retained client = 3-5 new lead value. Outbound focus correct for growth, but top-5 existing account protection = higher immediate leverage.
- Concrete insertion: parallel to LinkedIn outreach, one proactive contact/month to top-5 — not support, but "რას ვგეგმავთ თქვენთვის". Churn insurance, 0₾.

## Owner decisions needed (consolidated)

1. FB Policy: approve threshold set? LTV assumption 5000₾ confirms 500₾/deal? Executor = Mariam or Mentari?
2. LinkedIn: ICP segments 1-3 confirm? Seg 2 test = full 20 (10/5/5) or Balance-only first? Outreach by owner or delegated?
3. Top-5 at-risk clients: which 5?
4. Balance-type new partner: 1-2 names?
5. HubSpot calls: update when ready → unblocks dashboard v1 + pipeline section
6. Waalaxy A/B/C choice
