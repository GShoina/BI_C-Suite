---
class: OPEN ITEMS (always-on tracker)
updated: 2026-05-21 session-close (Geo — bihub.ge SPF + migration prep)
owner: Mentari
---

## bihub.ge — P0 open (2026-05-22)

| # | Item | Status |
|---|---|---|
| P0 | bihub.ge migration execute | READY — script at `~/.claude/scripts/bihub_migration.ps1` |
| P0 | SPF spam retest | Send fresh forgot-password → inbox? If spam: Gmail headers or mail-tester.com |
| P1 | SweetAlert forgot form (post-migration) | AJAX submit + "შეამოწმეთ სპამი" UI |

---

## Deliverables shipped 2026-05-21 ✅
- GTM V15 published: "Clarity → Window Loaded" — Clarity tag trigger All Pages → Window Loaded
- bivision.ge PageSpeed Mobile: 57 → **71** (+14pts), TBT: 800ms → **370ms** (-54%)
- Note: Crisp not in GTM (tag 24 = UTM cookie tracker). Crisp loads via WP plugin — deferred separately if needed.
- **B-02 DONE**: Wrong Meta pixel `495329725412052` (Ad Account ID) removed from `functions.php` wp_head hook. Only correct pixel `24993373220352719` now fires. LiteSpeed purged + verified.
- **B-01 FALSE POSITIVE**: Viktor audit said `.products-tab-btn` broken — JS already uses `.products-tab-item`. All 6 tabs verified working.
- **PageSpeed recheck** (after B-02 purge): Mobile 67, TBT 780ms — suspect LiteSpeed cold cache. Recheck May 22.

## Deliverables shipped 2026-05-20 ✅
- `outputs/2026-05-20 bivision.ge Audit v4 by Geo.html` (score 72/100) — Geo session
- `outputs/2026-05-20 bivision.ge GA4 + GSC Analysis by Geo.html` (v2, spam-filtered) — Geo session
- `outputs/2026-05-20 Bivision Academy V9 by Gurafa.html` (designer V9 + text fixes)
- `outputs/2026-05-20 Bivision Academy Curriculum by Gurafa.html` (M01-M06, 37 lessons, ~21.5h)
- `outputs/2026-05-20 Competitor Ads Watch by Gurafa.html` (Amadeo BDO signal, 3 counter-moves)
- `outputs/2026-05-20 Qlik + Power BI AI Weekly Analysis by Gurafa.html` (weekly BI watch #1)

---

## P0 — BLOCKING (owner action required)

| Item | Action | Who | Status |
|---|---|---|---|
| GA4 Key Events | GA4 Admin → Events → phone_call/whatsapp_click/contact_form_submit → toggle Key Event | Owner | ⏳ TODAY |
| BiRetail tabs P0 (B-01) | mu-plugin: `.products-tab-content` IDs + click handler | Geo | ⏳ needs "შეიტანე" |
| **BiFinance CTR kill check** | May 21 (72h). CTR <0.3% at $5 spent → kill. | Gurafa+Owner | ⏳ TODAY |
| **Amadeo BDO counter** | Approach Deloitte/GT/RSM Georgia within 2 weeks — accounting firm channel | Owner | ⏳ NEW May 20 |

---

## P1 — This week

| Item | Action | Who | Status |
|---|---|---|---|
| fb/paid LAL monitoring | Check eng.rate May 22+. If still <35% → /demo LP | Mariam+Geo | ⏳ monitor |
| UTM on email campaigns | Mailchimp UTM template + WhatsApp links | GelLa/Mariam | ⏳ |
| **BOG payment link** | Academy payment setup: merchant agreement + link details | Owner | ⏳ needs owner |
| **Academy WP deploy** | bivision.ge/academy — brief Geo | Owner → Geo | ⏳ blocked |
| **Academy M03 brief** | Claude Finance agent templates → lesson brief draft | Gurafa | ⏳ next session |
| **"Power BI Q&A deprecating" post** | LinkedIn + email draft → Mariam. Dec 2026 deprecation = lead gen. | Gurafa | ⏳ next session |
| **BiFinance AI roadmap confirm** | Claude API + Qlik MCP = feasible. Owner confirm P0? | Owner | ⏳ needs owner |

---

## P2 — Backlog (Geo lane, needs "შეიტანე")

| Item | Details |
|---|---|
| ~~B-02: old Meta pixel~~ | ✅ DONE 2026-05-21 |
| B-03: Empty H1 | backlog — owner deferred, recheck May 22 with PageSpeed |
| B-04: hreflang | ka + x-default → Rank Math Sitemap settings |
| B-05: H1 keyword gap | H1 keyword alignment |
| 38 empty alt="" | Gutenberg inline blocks |

---

## Academy known issues (carry-forward)

| Issue | Status |
|---|---|
| Quiz (4 old roles) ↔ #whom (5 new personas) | Intentional status quo (option A) |
| Mobile 375px hero-marketing gap | Unverified — test needed |
| Registration backend (email → HubSpot) | Not built — blocked on platform decision |

---

## Carry-forward from May 19-20

- GelLa May 19 fixes confirmed: OG ✅, GA4 1× ✅, bifinance-2 301 ✅, Schema ✅, H1 ✅
- iOS Safari verified by owner ✅
- Meta LAL audiences active May 19 — monitor 72h (check May 22)
- Competitor scan: Amadeo BDO Georgia partnership = accounting firm channel hostile. Counter-move pending.
- Power BI MCP research complete — `memory/project_powerbi_mcp_research.md`

---

## Owner questions open

- April M/M comparison (Apr 1-30 vs May 1-20) — API ready, owner said "საინტერესო"
- BiRetail tabs: say "შეიტანე" to unblock Geo
- ნინო გორგაძე monthly signal note — Gurafa → Mariam next session
- BiFinance CTR: confirm kill or continue (May 21)
- Power BI MCP service — შემოვთავაზო Power BI Pro კლიენტებს?
