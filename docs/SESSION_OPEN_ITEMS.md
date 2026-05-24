---
class: OPEN ITEMS (always-on tracker)
updated: 2026-05-24 Viktor audit v2 (live Playwright test post-upload)
owner: Mentari
---

## bihub.ge — Viktor Audit v2 (2026-05-24, carry to Geo)

| # | Priority | Bug | Fix |
|---|---|---|---|
| ~~B-01~~ | ✅ FIXED | ~~forgot-password → 404~~ | Modal works, no 404 |
| **REG** | **P0** | /register-me/ → Fatal error: `Cannot redeclare bihub_mail()` in db.php:29 | Wrap in `if (!function_exists('bihub_mail'))` OR find duplicate include |
| **N1** | **P0 Security** | Path disclosure — server path `C:\wamp\www\...` visible in browser on 500 | `wp-config.php`: `WP_DEBUG_DISPLAY=false` |
| B-02 | P1 | Logo href="#" | Change to href="/" |
| B-03 | P1 | Terms/Privacy dead links | Need page content from owner |
| ~~B-04~~ | ✅ FIXED (5/6) | ~~Security headers~~ | HSTS✅ X-Frame✅ X-Content✅ Referrer✅ Permissions✅ — CSP missing → N3 |
| N2 | P1 | favicon.ico 404 — `themes/qlik/assets/img/favicon.ico` missing | Upload favicon.ico to that path |
| B-05 | P2 | Rocket Loader still ON — Wordfence script blocked (MIME error) | CF Dashboard → Speed → Rocket Loader → OFF |
| N3 | P2 | CSP header missing (Content-Security-Policy) | CF Transform Rules → Add header |
| N4 | P2 | Google Maps API key in URL — not domain-restricted | Google Cloud Console → Credentials → restrict to *.bihub.ge/* |
| ~~B-06~~ | ✅ N/A | ~~noscript display:none~~ | GTM noscript not found. Content noscript = acceptable SEO pattern |
| NOTE | — | /tbc/.htaccess | DO NOT DELETE — needed |

## bihub.ge carry-forwards (2026-05-24)
- Backup verified: `C:\wamp\bihub_fullbackup_20260523.zip` — 184.7MB / 17,063 entries / wp-config.php ✅
- P0: mail-tester.com deliverability score — still pending
- P1: Playwright visual regression baseline — still pending

---

## BiMedical IVF — Follow-up P0 (2026-05-22) ⏰ OWNER REMINDER

| # | Item | Detail |
|---|---|---|
| P0 | g.metreveli@vivomedical.ge — follow-up | Clicked BiMedical IVF email 2026-05-20. Mariam → personalized outreach |
| P0 | paatachikovani@gmail.com — follow-up | Clicked BiMedical IVF email. Unknown clinic. Mariam → personalized outreach |
| NOTE | davit.dgebuadze@vbc.ge | Clicked but excluded from follow-up per owner rule |

---

## BiFinance Leads Campaign — ✅ PUBLISHED 2026-05-22

| # | Item | Detail |
|---|---|---|
| ✅ | **Lead Gen TOS** | Accepted 2026-05-22 session |
| ✅ | **Creative** — "New Leads Ad" | BiFinance image + Georgian CFO copy + headline done. Published. |
| ✅ | **Campaign published** | `BiFinance_Phase1_Leads_2026-05-22` → In review (Meta). Score 100. |
| ✅ | **Pause old Traffic** | `BiFinance_Phase0_AB_Traffic_2026-05-18` → PAUSED 2026-05-22. Status: Off. |
| ✅ | **Image fix: B→A** | `New Leads Ad` creative swapped to `BiFinance single post A.jpeg` (CFO/Ad_A_CFO_GelLa). Re-published 2026-05-22. |
| ✅ | **End date set — June 1** | AdSet end_time=2026-06-01T00:00:00+0400 via Meta API (UI blocked start date, API bypass). Start=May 22 unchanged. |

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
| **Academy M03 brief** | Brief DONE (`BI_gurafa/docs/ACADEMY_M03_BRIEF.md`). Prompt templates + sample Georgian data → Gurafa next session | Gurafa | ⏳ partial |
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
