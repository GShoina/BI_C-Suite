---
class: ACTIVE
owner: Mentari
updated: 2026-04-15
---

# Execution Queue

## Priority Hierarchy
```
1. ცოცხალი ფული (leads, follow-up, client problems)
2. მომაკვდავი ფული (churn, at-risk)
3. მომავალი ფული (new leads, marketing)
4. ინფრასტრუქტურა (dashboard, architecture)
```

## Owner Actions — Decision Pending
| Item | Status | File |
|---|---|---|
| LinkedIn posts publish | 🟢 READY, owner review + publish | docs/LINKEDIN_PUBLISH_READY.md |
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
| Dashboard Decision Layer v1 build | 9/10 (O) | spec in EXECUTION_PLAN_V3.md, implementation pending |
| AI Impact Internal Map (no competitor input) | 7/10 (S) | scope in EXECUTION_PLAN_V3.md, draft pending |
| AUDIT_REQUEST append-log format migration | 6/10 (S) | done Apr 15 |

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
