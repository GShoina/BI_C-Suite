---
class: ACTIVE
owner: Mentari
updated: 2026-04-15
---

# Execution Queue

## Freeze Window — ACTIVE

- **Start:** 2026-04-15 (owner greenlight timestamp)
- **Review date:** 2026-04-29 (start + 14 calendar days)

### Success criteria (all 3 required)
1. Dashboard Decision Layer v1 scaffold delivered on disk — ✅ met 2026-04-15
2. Zero tripwire fires during window
3. Zero governance drift return

### Tripwires (any one = freeze-fail signal)
- HIGH-severity audit miss
- Live data integrity risk
- Owner-reported silent drift

### Warnings (tracked, not freeze-fail)
- New shared-core file proposal
- New ADR proposal
- New dashboard tab / section

### Movement indicators (tracked separately, NOT freeze-fail criteria)
- LinkedIn posts published count (target ≥1)
- FB policy approved + executed count (target ≥1)

### Dashboard v1 definition (locked)
- scaffold delivered = freeze success criterion
- live-wiring = separate post-freeze milestone

### Carve-outs (freeze-compatible, pre-committed work)
- AI Impact Internal Map v1 — Layers 1–3 on disk; Layers 4–5 + synthesis = in-scope completion, target 2026-04-20; no scope expansion beyond 5-layer structure
- Capacity audit — გაბო + ინგა, 10 working days inside freeze window; readout 2026-04-29; structural decisions deferred to post-freeze
- Team interview response absorption — remaining 5 responses append into existing `docs/TEAM_INTERVIEW_RESPONSES.md`; no new analysis artifact

### გაბოს CTO-protected days
- 4 blocks total (2 days/week × 2 weeks), all inside freeze window [2026-04-15, 2026-04-29]
- Owner books specific dates at greenlight — recommended pattern: Tue + Thu of each week
- No block may fall outside freeze window

---

## Priority Hierarchy
```
1. ცოცხალი ფული (leads, follow-up, client problems)
2. მომაკვდავი ფული (churn, at-risk)
3. მომავალი ფული (new leads, marketing)
4. ინფრასტრუქტურა (dashboard, architecture)
```

## Owner Actions — Decision Pending

**RULE (sprint 14-day):** Viktor spot-check = parallel, non-blocking. Owner can act without waiting Viktor on spot-check tier. Mandatory tier only = gate.

| Item | Status | File |
|---|---|---|
| ~~Questionnaire V3 send~~ | ❌ SUPERSEDED — V3 generic, Team Real Picture analysis delivered instead | outputs/2026-04-19 Team Real Picture Analysis by Mentari.html |
| LinkedIn 2 posts publish (Gela personal LinkedIn) | 🟢 READY Apr 14, owner publish → Viktor post-factum | docs/LINKEDIN_PUBLISH_READY.md |
| FB Operating Policy — **LTV/CAC baseline CONFIRMED 2026-04-20 (v2 realistic)** | 🟢 threshold locked **1,200₾/deal** (revised from 750 after realistic allocation model). Remaining: (a) overall thresholds approve, (b) executor = Mariam confirm | docs/FB_OPERATING_POLICY.md |
| Waalaxy decision (A/B/C) | ⚠️ REC delivered: ხელით outreach | docs/WAALAXY_DECISION_BRIEF.md |
| HubSpot deals update | Owner calling clients | — |
| FB Operating Policy approve/reject | ⚠️ REC delivered Apr 15 | docs/FB_OPERATING_POLICY.md |
| LinkedIn ICP segments confirm/correct | ⚠️ REC delivered Apr 15 | docs/LINKEDIN_BATTLE_PLAN.md |
| FB lead threshold: 500₾/deal vs LTV assumption | awaiting answer | docs/FB_OPERATING_POLICY.md |
| LinkedIn Seg 2 test scope: 10/5/5 vs Balance-only | awaiting answer | docs/LINKEDIN_BATTLE_PLAN.md |
| Top-5 at-risk clients list | awaiting list | — |
| Balance-type new partner (1-2 names) | awaiting input | — |

## Active — Mentari
| Item | EP0 | Status |
|---|---|---|
| Dashboard Decision Layer v1 — live data wiring | 9/10 (O) | scaffold done 2026-04-15 (dashboard.html, 🎯 Decision Layer tab, placeholder data labeled). Awaiting HubSpot update to plug live numbers. |
| AI Impact Internal Map | 7/10 (S) | DRAFT (docs/AI_IMPACT_INTERNAL_MAP.md). Layers 1–3 populated 2026-04-15. Layers 4–5 pending. v1 target 2026-04-20 |
| Team interview analysis | 8/10 (S) | 2 of 7 received + analyzed (docs/TEAM_INTERVIEW_RESPONSES.md). H1 confirmed, H4 expanded. Awaiting Mari Magh/Mik/Luka/Mariam. |

## Blocked — Waiting Viktor
| Item | Tier | Filed | Waiting Since |
|---|---|---|---|
| Site speed TTFB recommendation | Spot-check | docs/AUDIT_REQUEST_SITE_SPEED.md | Apr 14 (approaching 24h timeout) |
| Waalaxy brief review | Spot-check | docs/WAALAXY_DECISION_BRIEF.md | Apr 15 |
| Marketing Pareto audit | Spot-check | docs/MARKETING_PARETO_AUDIT.md | Apr 15 |
| Execution Plan v2 + FB Policy + LinkedIn ICP | Spot-check | docs/EXECUTION_PLAN_V3.md (supersedes v2) | Apr 15 |

## Queued (EP0 ≥5, prioritized)
| # | Item | EP0 | Depends On |
|---|---|---|---|
| 1 | LinkedIn outreach post-publish tracking | 7 | Owner publishes posts |
| 2 | Competitor monitoring signal report | 6 | Gurafa (task sent Apr 14) |
| 3 | Churn top-5 proactive contact scripts | 7 | Owner top-5 list |
| 4 | HubSpot pipeline dashboard section | 8 | Owner HubSpot update |

## Closed / Archived
- AUDIT_REQUEST append-log format migration — done Apr 15
- Dashboard Decision Layer v1 scaffold — done Apr 15 (dashboard.html 🎯 Decision Layer tab with placeholder data; live-wiring remains in Active)
- Marketing Pareto audit — delivered Apr 15 (docs/MARKETING_PARETO_AUDIT.md)
- Waalaxy decision brief — delivered Apr 15 (docs/WAALAXY_DECISION_BRIEF.md)
- LinkedIn posts publish-ready format — delivered Apr 15 (docs/LINKEDIN_PUBLISH_READY.md)
- 3-cycle adoption validation — passed Apr 15 (session; ⚠️ INFERENCE, no standalone disk artifact; reflected in updated role discipline)
- საგა იმპექსი — archived, owner low priority
- C-Suite Final Decision — archived, relevance TBD
- Site audit — complete (docs/site-audit-instructions.html)
- Plugin fixes (QM, Yandex, CMP, Smush, menu) — done
- ენერგეტიკის კამპანიის ანალიზი — done, on dashboard
- Social media weekly report — done (docs/SOCIAL_MEDIA_WEEKLY_REPORT.md)
