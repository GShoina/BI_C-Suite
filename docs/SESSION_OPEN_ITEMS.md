---
class: OPEN ITEMS (always-on tracker)
updated: 2026-05-25 — GelLa session (Operating Constitution complete)
owner: GelLa
---

## 2026-05-25 — GelLa session (memory cleanup COMPLETE)

| Item | Owner | Status |
|---|---|---|
| **Mentari_Virtual-C-Suite/ folder archive** | GelLa | ⏳ P0 next session — missed in Phase 1 |
| **Owner Phase 4.3 checklist** | Owner | ⏳ P1 — Constitution readability confirm |
| **BI_C-Suite/CLAUDE.md** | GelLa | ⏳ P2 — still references Mentari; fix after folder archive |
| ctx-upgrade v1.0.151 | GelLa | ✅ done (already shown in Viktor session) |

**Memory system status:** ✅ COMPLETE
- 10 canonicals + OPERATING_CONSTITUTION.md + CLAUDE.md thin-loader
- 141 archived, 90 active, MEMORY.md = 128 lines
- All 6 patches applied (A/B/C/D/E/F)

---

## 2026-05-25 — Viktor session carry-forwards

| Item | Owner | Status |
|---|---|---|
| ctx-upgrade v1.0.151 | GelLa | ⏳ `/ctx-upgrade` next session |
| GTM Key Events (phone_call / whatsapp_click / form_submit) | Owner | ⏳ P0 |
| Mailchimp billing | Owner | ⏳ P0 |
| Energy #17994061 segment filter | GelLa (after billing) | ⏳ P1 |
| Constitution §3 Viktor launcher text | GelLa | P3 — "(Mentari session / standalone)" → "standalone" |
| 7 project files future archive | GelLa monthly | P3 |

**Memory system status:** ✅ COMPLETE — 10 canonicals + Constitution live. 141 archived. CLAUDE.md thin loader.

---

## GelLa P0 execution — 2026-05-24 evening

| Task | Status | Notes |
|---|---|---|
| LiteSpeed Preload All (TTFB) | ✅ DONE | Crawler ON, async running, cache warming |
| MariaDB upgrade check | ⏳ FastCloud pending | Current: 10.5.29-MariaDB-cll-lve. Owner: "არ ვიცი როდის" |
| Redis object cache | ⏳ blocked on MariaDB confirm | Option available in LiteSpeed Cache settings |
| Mailchimp billing | ⏳ owner fixing | Payment declined = root cause of 6-day email stall |
| Energy #17994061 audience filter | ⏳ after billing | "All subscribed contacts" → needs Energy segment |
| BiMedical #17993958 URL fix | ℹ️ already sent May 20 | Open 41.3% ✅, Bounce 13.1% ⚠️ — clean list before next send |
| GTM Key Events | ⏳ pending | phone_call / whatsapp_click / form_submit = unmeasured |
| ctx-upgrade v1.0.136→v1.0.150 | ⏳ git timeout | Hooks fixed. Retry when network clear: `/ctx-upgrade` |
| Memory/file cleanup session | ⏳ paused | Resumed after today's P0s done |

## BiFinance Phase1 v2 — 2026-05-24 ✅ LIVE

| # | Item | Status |
|---|---|---|
| ✅ | Campaign `BiFinance_Phase1_v2_2026-05-22` (120246759167590598) | ACTIVE, $20 lifetime, ends Jun 1 |
| ✅ | AdSet LAL_PixelSeed only, Advantage+ OFF, age 28-55 | VERIFIED via API |
| ✅ | Form swap: old 990562330546376 (5 fields, 0 leads) → **1495634402063502** (3 fields + Calendly) | PUBLISHED via Playwright |
| ✅ | GSC sitemap resubmit + all pages indexing requested | DONE 2026-05-24 |
| ⏳ | **2026-05-27 checkpoint** (72h) — CTR/impressions/leads | Owner check |
| ⏳ | Meta app dev mode → Live (1-3 day review) | Owner → Meta Developer Console |
| ⏳ | GA4↔Meta gap: Lead Gen Form = no website visit = no GA4 | Decision: keep form OR switch to website CTA |
| ⏳ | bihub.ge migration | `~/.claude/scripts/bihub_migration.ps1` READY |
| ⏳ | Search Console API enable | project 690459787742 → `searchconsole.googleapis.com` |

---

## bihub.ge — Viktor Audit v3 (2026-05-24, score 82/100)

| # | Priority | Bug | Status | Fix |
|---|---|---|---|---|
| ~~B-01~~ | ✅ FIXED | ~~forgot-password → 404~~ | FIXED | — |
| ~~REG~~ | ✅ FIXED | ~~Fatal error db.php:29~~ | FIXED | — |
| ~~N1~~ | ✅ FIXED | ~~Path disclosure~~ | FIXED | — |
| ~~N2~~ | ✅ FIXED | ~~favicon.ico 404~~ | FIXED | — |
| ~~B-04~~ | ✅ FIXED | ~~Security headers (5/6)~~ | FIXED | — |
| HSTS | ✅ UPGRADED | — | max-age=31536000 + preload | — |
| **B-02** | **P1** | Logo href="#" on homepage | **PARTIAL** — inner pages fixed, homepage still "#" | Homepage template header href → "/" |
| **B-03** | **P1** | Terms/Privacy dead links | **OWNER PENDING** | Owner provides content |
| **B-05** | **P2** | Rocket Loader ON | **NOT FIXED** | CF → Speed → Rocket Loader → OFF |
| **N3** | **P2** | CSP header missing | **NOT FIXED** | CF Transform Rules → Add CSP |
| **N4** | **P2** | Maps API key not domain-restricted | **UNVERIFIED** [EP1] | Google Cloud Console → Credentials → *.bihub.ge/* |
| NOTE | — | /tbc/.htaccess | DO NOT DELETE | — |

## bihub.ge carry-forwards (2026-05-24 v3)
- Backup: `C:\wamp\bihub_fullbackup_20260523.zip` — 184.7MB / 17,063 entries / wp-config.php ✅
- P0 open: 0 — both cleared by Geo ✅
- P1 remaining: B-02 (partial), B-03 (owner-pending)
- P2 remaining: B-05, N3, N4 — ~1-2h Geo work
- mail-tester.com deliverability score — still pending
- Playwright visual regression baseline — still pending
- bihub.ge strategic Q: registration conversion rate unknown — owner check GA4 `/register-me/` completion

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

---

## bivision.ge SEO — Open items (Geo 2026-05-22)

**Brief:** `outputs/2026-05-22 bivision.ge SEO Brief by Geo.html` — agent handoff for reputation/content strategy.

| P | Item | Lane |
|---|---|---|
| P0 | TTFB 1.49s → LiteSpeed Preload All (10 min fix now) + Redis post-MariaDB | GelLa |
| P0 | Key Events: phone_call / whatsapp_click / form_submit → GTM | Owner / GelLa |
| P0 | Content: first post targeting "ფინანსური რეპორტინგი ავტომატიზება" (blue ocean) | Gurafa + Mariam |
| P1 | B-03 Empty H1 homepage | GelLa (theme) |
| P1 | B-06 Privacy Policy = PDF → WP page + 301 | GelLa |
| P1 | B-07 legalName "bevision" → "Bivision" (Rank Math Organization) | GelLa |
| P2 | B-08 Cache-Control inconsistency | GelLa |
| P2 | hreflang ka + x-default | GelLa |
| monitor | FB paid eng.rate — if <35% → build /demo LP | Mariam |
