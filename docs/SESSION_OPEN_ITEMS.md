---
class: OPEN ITEMS (always-on tracker)
updated: 2026-05-19 (Geo — bihub-v8 landing page)
owner: Mentari
---

## Geo open items — 2026-05-19 (bihub-v8 session)

| Item | Priority | Next |
|---|---|---|
| **Mobile overflow — hero-text1** | P1 | `white-space:nowrap` may overflow 375px — add clamp fallback or overflow:hidden on mobile |
| **bihub-v8 production deploy** | P1 | Owner approves → upload to bihub.ge WP or replace static HTML via WinRM |
| **UpdraftPlus file backup** | P1 carry-forward | Add themes+plugins to bihub.ge backup schedule |
| **bihub.ge off-server backup** | P2 | Download bihub_fullbackup_20260518.zip locally |

**Shipped 2026-05-19 (Geo):**
- ✅ bihub-v8.html — new hero (Text1/Text2/no-card), footer single-row, Bivision logo restored
- ✅ Notify strip → HubSpot CRM (PHP proxy mu-plugin deployed server-side)
- ✅ Copy: 3 global replacements (რეგისტრაცია უფასოდ, წვდომა უფასოდ, footer tagline)
- ✅ Lock flag consistency: 4 cards fixed
- ✅ v6/v7 deleted from repo

## Geo open items — 2026-05-18 (backup session)

| Item | Status | Next |
|---|---|---|
| **bihub.ge off-server backup** | ⚡ P0 — backup on server only | Download bihub_fullbackup_20260518.zip locally OR FastCloud panel |
| **UpdraftPlus file backup** | ⛔ DB-only since May 7 | Add themes+plugins to backup schedule |
| **bivision.ge DKIM Brevo auth** | ⏳ DNS live, Brevo "Authenticate" not clicked | app.brevo.com → senders/domain/list → Authenticate (2 min) |
| **www.bivision.ge 301 redirect** | ⏳ owner-gate | Owner: "შეიტანე" |
| **functions.php reconstruction** | ⚠️ 2,434/9,673 bytes recovered | Low priority if site works |

**Shipped 2026-05-18 (Geo):**
- ✅ Full server backup: `C:\wamp\bihub_fullbackup_20260518.zip` (191.9MB) on server 185.229.111.201
- ✅ WinRM compress method: .NET ZipFile (Compress-Archive fails — pre-1980 timestamps)
- ✅ PHP warning fixed (front-page.php:79 error_reporting)

## GelLa open items — 2026-05-18

| Item | Status | Next |
|---|---|---|
| bihub.ge weekly backup | ⏳ approved, not built | WinRM Scheduled Task — 30 min job |
| Morning deals analysis (10:30) | ⏳ incomplete | Pull Meta+Mailchimp → unified HTML |
| Elgromotors follow-up | ⚡ HOT — close May 31, 60% | გელა: პირადი კონტაქტი |
| რუსთავის ავტოდრომი follow-up | ⚡ HOT — close May 31, 40% | გელა: პირადი კონტაქტი |
| 0llivander + ნუტრიველი | ⏳ overdue | Owner confirm closedlost? |
| FB Lead Gen campaign | ⏳ pending | Mariam 6Q gate → launch |
| LinkedIn Community Management API | ⏳ pending (submitted 2026-05-17) | Check email → li_oauth2.py |
| Construction email follow-up | ⏳ 7-10 days | Mailchimp open rate → non-openers |

**Shipped 2026-05-18:**
- ✅ **bihub.ge RECOVERED** — style.css restored, cards visible, CPT registered. WinRM method confirmed.
- ✅ WinRM access established (185.229.111.201:5985, ntlm) — canonical edit path for bihub.ge
- ✅ GA4 SA setup (bivision-analytics → property 302944682)
- ✅ GA4 real data: 194 sessions, BiRetail #1, Organic Search=5 (critical SEO gap)
- ✅ CEO Brief updated with GA4 channel + page breakdown
- ✅ Analytics Admin API + OAuth client (shining-courage-493721-v5)
- ✅ ga4_query.py script (token cached — no browser next time)

**Social media state (2026-05-18):**
- Meta: 1 active campaign paused (B*Product_Traffic, 0 leads, $24.84 spent). No active paid campaigns.
- LinkedIn: 842 followers, Community Management API pending review (submitted 2026-05-17).
- FB Lead Gen: Mariam 6Q gate not yet done. Not launched.
- Mailchimp construction blast: 7-10 day window, open rates not yet checked.

## GelLa open items — 2026-05-17 (attribution + CEO brief session)

| Item | Status | Next |
|---|---|---|
| Elgromotors follow-up | ⚡ HOT — close May 31, 60% | გელა: პირადი კონტაქტი |
| რუსთავის ავტოდრომი follow-up | ⚡ HOT — close May 31, 40% | გელა: პირადი კონტაქტი |
| FB Lead Gen campaign (ახალი) | ⏳ pending | Mariam 6Q gate → launch |
| LinkedIn Community Management API | ⏳ pending review (1-5 days) | Check email → run li_oauth2.py |
| Construction email follow-up | ⏳ 7-10 days after send | Check Mailchimp open rate first |
| GA4 MCP → settings.json | ⏳ next session | GelLa implement |
| HubSpot deals: 0llivander + ნუტრიველი | ⏳ overdue | Owner: closedlost? |

**Shipped 2026-05-17:**
- ✅ FB→HubSpot Ads integration (Lead forms auto-sync)
- ✅ HubSpot tracking code live (bivision.ge/mu-plugins/bivision-hubspot-tracking.php, portal 147341634)
- ✅ Attribution audit HTML: `outputs/2026-05-17 Marketing Attribution Audit by GelLa.html`
- ✅ CEO Brief: `outputs/2026-05-18 CEO Brief by GelLa.html`
- ✅ Meta campaign PAUSED (B*Product_Traffic, 0 leads, $24.84)
- ✅ LinkedIn Developer App setup (Client ID: 77sf2r5iq6osvn, Community Management API submitted)
- ✅ SoftwareApplication schema × 6 + Organization patch + llms.txt (all live on bivision.ge)

---

## Gurafa open items — 2026-05-19 (updated)

| Item | Status | Next |
|---|---|---|
| **May 19 competitor scan** — Dastafe + DataStudio.ge | ⏳ P0 TODAY | `/competitor-ads-watch` — Gurafa |
| **Academy build** — bivision.ge/academy | 🟢 UNBLOCKED — domain+pricing DECIDED | Owner "შეიტანე" → GelLa builds |
| **Mentari: keep-awake script** | ℹ️ OBSOLETE — Claude Code Routines replaces | Mentari close item |
| **Oris ERP financial statements** | ⛔ BLOCKED — owner sends ZIP | Owner action |
| **ნინო გორგაძე monitoring** | 🔄 ONGOING | Monthly note to Mariam |
| **GURAFA_INDEX_v2.html** | ✅ CANONICAL — commit 8c5ed10 | — |

**Gurafa shipped 2026-05-19:**
- ✅ ctx-upgrade v1.0.135 → v1.0.136 (better-sqlite3 ABI 137 fixed, plugins reloaded)
- ✅ bihub-v6/v7/v8 review + 7-dimension challenge (parallel window)
- ✅ bihub design brief compiled (hero structure, ticker labels, empty state lead capture)

**Academy — DECIDED (2026-05-19):**
- Domain: `bivision.ge/academy` ✅
- Pricing: M01 free / M02-06 700-800 GEL ✅
- Build: no blockers remain — owner "შეიტანე" triggers GelLa

**Gurafa deliverables shipped 2026-05-17:**
- ✅ Hub Identity + Mission section (tasks/principles/limits/questionnaire)
- ✅ 18+ ephemeral/superseded files deleted from outputs/
- ✅ GURAFA_INDEX v1 + gurafa-panel.html deleted (superseded)
- ✅ Apr22 cards inlined, 4 dead Apr21 cards removed
- ✅ GitHub Pages commit 8c5ed10

---

## Viktor open items — 2026-05-18

| Item | Status | Next |
|---|---|---|
| **Daily HTML deliverable** | ❌ 4 consecutive FAIL (May 13, 15, 17, 18) — chat analysis only, no disk artifact | Viktor P0 next session |
| **BiSchema verify — GelLa** | ⏳ 4 open questions before schema ship | GelLa: BiStock reorder / BiMedical patient flow / BiAudit "all" / ERP naming |
| **gap-checklist HSTS claim** | ⚠️ CONFLICT: checklist ✅, open items OPEN | Playwright verify before regression section updated |
| **updateActiveCard P2→P1** | Viktor recommendation | GelLa: 85% JS errors = conversion impact, promote severity |
| **fewer-permission-prompts** | ❌ NOT completed — 2nd carry-forward | Viktor next session |
| **Permission allowlist** | ✅ DONE — 53 Playwright+context-mode MCP added to settings.json | — |
| **WAMP bivision.local** | ⏳ deferred — GelLa next session | GelLa implements |
| **BiFinance mp4 duplicate** | ⏳ template fix needed | GelLa |
| **Optimole OBJECTS-3.webp dimensions** | ⏳ owner action: width=357 height=267 | Owner (WP Admin → Optimole) |
| **LiteSpeed Compress HTML = ON** | ⏳ owner action | Owner (WP Admin 1-click) |
| **iOS Safari real device verify** | ✅ DONE — owner iPhone verified | — |
| **SoftwareApplication schema ×6** | ✅ DONE live | — |
| **Organization foundingDate+areaServed** | ✅ DONE live (custom block, duplicate minor) | — |
| **llms.txt updated** | ✅ DONE ASCII-safe | — |
| **Menu სერვისები URL** | ✅ DONE → /saas-products/ | — |
| **AI-3 Case study blog post** | ⏳ pending | Owner: sector + results needed |
| **Organization schema clean (1 block)** | ⏳ next session | Rank Math Local SEO native fields |
| **Redirect /saas-products/bifinance-2/** | ⏳ next session | Rank Math Redirections |
| **LiteSpeed Compress HTML = ON** | ⏳ owner action | WP Admin 1-click |
| **OG image branded 1200×630** | ⏳ P1 | GelLa |
| **hreflang ka + x-default** | ⏳ P1 | Rank Math Sitemap |
| **H1 keyword gap** | ⏳ P1 | GelLa |
| **wp-json restrict** | ⏳ P1 | .htaccess |
| **Performance: total load 6.7s** | ⏳ new finding | LiteSpeed Page Optimization |
| **Audit v4 HTML (updated scores)** | ⏳ next session | Viktor |

**Viktor audit delivered May 17:**
- Geo v1 vs Mentari challenge adjudicated → Geo v2 accepted (68/100 confirmed)
- Dev practice: LocalWP + git spec → shared with GelLa
- Permission allowlist: 53 entries added to global settings.json

## Geo / Nikacho — 2026-05-17 update

## Geo / Nikacho — 2026-05-17 update

Issue #3 (project pages) = ✅ DONE V24. live. all 200. git clean.

| item | სტატუსი |
|---|---|
| Calculator Iter 2 | ⛔ BLOCKED — owner spec |
| GA4 Key Events (geometri.ge) | ⏳ owner action — GA4 Admin → phone_call / whatsapp_click / contact_form_submit |
| bivision.ge AUDIT_REQUEST (www+BOM) | ⛔ BLOCKED — FastCloud restore pending |
| Nikacho launch: use PowerShell `Nikacho` shortcut | info — auto-loads CLAUDE.md, no "nikacho" trigger needed |

---

## 🚨 CRITICAL — RESTORE IN PROGRESS (2026-05-16)
- FastCloud support ticket: May 15 full site restore submitted by owner
- Status: **WAITING** — do NOT touch bivision.ge functions.php or DB until support confirms
- After restore: ALL today's DB changes lost (სუპერი removal, etc.) — must redo
- Contact: check FastCloud support ticket status before starting next session

## GelLa P0 — after restore confirmed
1. Re-do სუპერი testimonial removal (posts #1066, #2210, #2261, #2264, #2269, #2271)
2. Fix BiRetail tabs SOLO — no Geo coordination: wp_head CSS + wp_footer JS init
3. Test all 6 product pages mobile + desktop (Playwright)
4. Homepage services section slow images: Optimole/CDN investigation
5. getimagesize() fallback: re-add to functions.php (restore overwrites it)

---

## Geo open items — May 16 (bivision.ge fixes)

### ✅ Done this session
- Chrome GPU artifact fix: `transform:translateZ(0)` on hero video
- Products video: `height:360px !important; object-fit:cover; object-position:left center`
- BiRetail CSS corruption (wpautop `<br />` in `<style>`): `the_content` filter priority 99 — ALL CLEAN
- BIVISION_SITE_AUDIT.md updated with May 16 section

### P0 (next Geo session)
| Item | Method | Blocker |
|---|---|---|
| BiRetail tabs fix | functions.php JS: add `id` to `.products-tab-content` panels + click handler | none — can do without browser |
| "სუპერი" testimonial card delete | WP Admin | browser needed |
| Hero video switching speed | Investigate JS/animation in theme | — |

### P1 (next Geo session)
| Item | Notes |
|---|---|
| BiMedical GIFs verify | 2 img.gif — check if replaced after regex fix |
| bihub.ge GIF filter | Separate WP install — own render_block filter |
| Cleanup gif_convert/ | `C:\Users\gela.shonia\AppData\Local\Temp\gif_convert\` |

### agent-teams check
GelLa ran `agent-teams:team*` review on bivision.ge. Await findings before next site action.

## Geo — bihub items (2026-05-17)
| Item | Status | Blocker |
|---|---|---|
| bihub-v5.html a11y fixes | ✅ DONE — commit f1584a6 pushed | — |
| bihub follow-up email plugin | ✅ ACTIVE on bihub.ge | — |
| Brevo SPF + DKIM | ✅ DONE 2026-05-17 | SPF fixed CF DNS; DKIM CNAMEs live; spam risk LOW |
| bihub-v5.html deploy to server | ⛔ pending | browser session method |
| CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 | ⛔ not set | owner runs: [Environment]::SetEnvironmentVariable("CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS","1","User") |

# Open Items — Mentari

## Mentari deliverables shipped May 14–15

- ✅ 96 contacts added to Mailchimp IVF-Medical
- ✅ Campaign 17993958 subject updated + scheduled May 19
- ✅ Calendly links in Email 3+4, GitHub push
- ✅ bivision.ge SEO audit — 2 P1 issues found + fixed by Geo (www redirect + PHP BOM)

## Mentari carry-forward P0 — May 15+

| Item | Blocker | Action |
|---|---|---|
| Campaign 17993958 — set send time 10:00 AM | **owner action** | Edit send time in Mailchimp, change from 7:30 PM → 10:00 AM AZT, then Schedule |
| BiMedical Email 2–4 follow-up flow | after Email 1 sends May 19 | Non-openers flow: E2 day 3-5, E3 day 8-10, E4 day 12-15 |
| Keep-awake script | not completed this session | `powercfg /change standby-timeout-ac 0` or WScript.Shell background job |
| Meta B*Product_Traffic — monitor delivery | none | Check spend/CTR; kill if CTR<0.3% day3 |
| Construction HubSpot campaign — confirm recipients | unresolved | check HubSpot campaign 17751009 recipient count |
| Meta Lead Gen rebuild | after May 19 | `Bivision — Lead Gen Calendly — 2026-05-19`, OUTCOME_LEADS |
| Gemini paid API key | owner action | add to .bivision-creds.env |
| BiAudit campaign | after BiMedical launch | next vertical |
| Contact enrichment workflow | not built | company name + tax ID → contact lookup → Mailchimp import |
| Meta App Live mode | owner action | developers.facebook.com |

---

## Viktor open items — May 16

| Item | Status | Next |
|---|---|---|
| F4 Dastafe | Viktor REJECT, Gurafa no counter-evidence → stays REJECT | Gurafa confirm or close |
| bivision.ge TTFB 1.79s | Viktor flag only → Geo execute | Geo |
| bivision.ge CSP missing | Viktor flag → Geo execute | Geo |
| HSTS 86400→31536000 | Viktor flag → Geo execute | Geo |
| Daily HTML deliverable | ❌ 0 shipped May 13, 0 shipped May 15 — 2 consecutive FAIL | Viktor P0 next session |
| fewer-permission-prompts | Skill loaded, NOT completed (interrupted by /clear) | Viktor next session |
| **Staging recommendation** | Viktor rec May 17: Local WP (Flywheel) + risk gate + rollback SLA | Geo: review + add to WEBSITE_STANDARD.md |

**HSTS current state (for Gurafa):** max-age=86400 + includeSubDomains. Target: max-age=31536000. Upgrade pending.

---

## Geo open items — bivision.ge performance (May 14 late)

### Done this session
- ✅ 21 GIFs → WebM+MP4 converted + uploaded (ffmpeg VP9+H.264 local pipeline)
- ✅ render_block filter priority 5: GIF→video, Optimole CDN URL + Georgian filename handled
- ✅ Mobile panel overflow fix (products-mobile-image)
- ✅ Smart video preload JS (active tab=auto, hidden=none)
- ✅ Hero video border-radius: 16px added (was missing on video vs img)
- ✅ Cache purged, verified on live site

### P0 (next Geo session — bivision.ge perf)
| Item | Notes |
|---|---|
| Owner confirm hero fix on real device | Playwright OK, need owner eyes |
| BiMedical page GIF → video verify | 2 img.gif noted earlier — recheck after regex fix |
| Site-wide GIF audit | Fresh scan for any missed GIFs after all fixes |
| bihub.ge GIF filter | Separate WP install — needs own render_block filter copy |
| Cleanup gif_convert/ temp files | `C:\Users\gela.shonia\AppData\Local\Temp\gif_convert\` |

---

## Geo open items — May 14 (evening, updated)

### Done this session (May 14 evening)
- ✅ bihub-v4.html gate/timer fully removed (HTML+CSS+JS) — v3+v4
- ✅ Footer space-between layout (logos left, texts right) — v3+v4
- ✅ Bivision footer logo: 13px → 18px
- ✅ Ticker bg light theme (v4): dark → rgba(107,99,181,0.06)
- ✅ CTA + sticky btn: green → purple (v4)
- ✅ Nav logo opacity 0.72 → 1.0 (v3+v4)
- ✅ Footer CSS grid → flex space-between (v3+v4)
- ✅ Dead CSS removed (v3+v4)
- ✅ Pushed 3 commits to GShoina/bivision-shares
- Live: gshoina.github.io/bivision-shares/bihub-v4.html

### Done earlier (May 14)
- ✅ bihub-v3.html H1 responsive: mobile=Qlik Sense BI only, desktop=Qlik Sense BI პლ.ატფ.
- ✅ Stats mobile: one row (flex-wrap:nowrap + clamp gap)
- ✅ Pushed to GitHub Pages commit 1e335a6

### P0 (next Geo session)
| Item | Notes |
|---|---|
| bihub-v4.html → bihub.ge root | Browser: WP File Manager → fetch gshoina.github.io/bivision-shares/bihub-v4.html → blob → POST admin-ajax.php (same method as v3) |
| Verify JS on bihub.ge | CF Rocket Loader re-enables scripts — card flip + filters must work |
| ticker-data.php proxy | 5-line PHP proxy for tarifebi.ge exchange+fuel API |

### P1 (owner action — bihub.ge)
| Item | Notes |
|---|---|
| bihub.ge root file (v3→v4) | Replace bihub-v3.html at root with bihub-v4.html |

---

## Geo open items — May 13

### P1 (owner action needed)
| Item | Notes |
|---|---|
| IVF Email 4 → HubSpot 138-contact send | Owner confirm before send |
| Calendly postMessage GTM tag | fires only on dead /thank-you-booking; postMessage tag = missing piece |
| 197 developer contacts HubSpot import | file: Downloads/Developers-email.xlsx |
| Mariam carousel launch | Canva eval shipped; launch pending owner |
| LinkedIn Lead Gen Form | not yet created |
| GSC 7-day SEO check | baseline May 6 → check May 13 |

### P2 (owner-gated: bivision.ge = "შეიტანე" required)
| Item | Notes |
|---|---|
| CF_BIVISION_API_TOKEN | needed: Brevo DKIM (bihub) + CF security headers. Script: AppData/Temp/bihub-cf-headers.ps1 |
| bivision.ge missing theme CSS | language-dropdown.css, testimonial-mobile-fix.css — mobile UI bugs |
| bivision.ge missing images | qlik-in-finance-1.png, qlik-in-finance-3.png |
| bivision.ge old URL redirects | /direction/*, /media/*, /contact, /about-us/who-we-are |
| bihub WP Application Password | REST API blocked — needs App Password |
| bihub PHP 7.3→8.2 | blocked on bank API dev approval |
| ACF PRO license | blocked on Gabo |

### Confirmed NOT done (May 13 check)
- hreflang ka: NOT implemented on bivision.ge. RankMath did NOT auto-add. P3 backlog — low impact for mono-language site.
- /doctor context-mode skills path = false positive. Path exists. No fix needed.

### Deliverables shipped May 11-13 (Geo)
- ✅ bihub.ge Audit → v3 HTML: `outputs/2026-05-03 bihub.ge Audit by Geo.html`
- ✅ bivision.ge Audit → v3 HTML: `outputs/2026-05-03 bivision.ge Audit by Geo.html`
- ✅ bivision-gap-checklist.html → v5: gshoina.github.io/bivision-shares/bivision-gap-checklist.html
- ✅ BIVISION_SITE_AUDIT.md updated: `~/.claude/standards/BIVISION_SITE_AUDIT.md`
- ✅ project_bihub_audit.md memory: May 11/12 findings, elFinder technique, bcrypt, SQL injection fixes
- ✅ bihub-v3.html v4 preview: `outputs/2026-05-13 bihub Landing v4 logo fix by Geo.html` (owner approved)
- ✅ BIVISION_ARCHITECTURE.md: `~/.claude/standards/BIVISION_ARCHITECTURE.md` (Viktor draft + Geo additions)

### ⛔ Pending next Geo session
| Item | Blocker | Method |
|---|---|---|
| bihub-v3.html v4 → server | Browser session needed | Upload `C:\Users\gela.shonia\bihub-v3-raw.html` via WP File Manager UI |
| ticker-data.php proxy | — | 5-line PHP, upload to bihub.ge web root |
| Live ticker JS block | needs proxy first | fetch /ticker-data.php?t=exchange + ?t=fuel, update #tick-usd #tick-eur #tick-fuel |
| Nikacho runbooks/ | deferred | deploy checklist, cache purge, Decap workflow |

---

## Gurafa open items — May 12

| Item | Status | Owner |
|---|---|---|
| **video-use install** | Prerequisites OK (ffmpeg✅ Python✅ uv❌). ElevenLabs free tier unverified. Owner: video = critical | Gurafa next session |
| **Meta Ads 0 active gap** | Bivision 0 active in Library (verified May 11). Calendlyy status unverified. | Owner: Meta BM check → reactivate |
| **Gegidze counter** | Apr 29 FRESH, A/B, 3 platforms. Counter: construction-specific copy | Mariam + Owner |
| **MEMORY batch (12 del + 8 merge)** | ✅ 3 Qs resolved 2026-05-13 (Viktor). UNBLOCKED. | Gurafa next session — execute |
| **Claude daily scout** | Deferred from May 12 | Gurafa next session |

---

## Gurafa open items — May 9

| Item | Status | Owner |
|---|---|---|
| `/sales icp` run (Bivision description) | Ready, not yet run | Gurafa next session |
| Oris cookbook | **BLOCKED** — owner must send Oris CSV column headers | Owner |
| GURAFA_INDEX.html — 0507 entry | Ready, P3 | Gurafa |
| Higgsfield free tier test | Ready, P1 (gate for Meta MCP) | Gurafa |
| Viktor: Amadeo Apricot/FMG update | ✅ CLOSED May 11 — VICTOR_COMPETITOR_INTEL.md updated | Viktor |
| Apricot — what is it? ICP overlap? | Open — Gurafa research needed | Gurafa |
| FMG blocks Amadeo too? | [UNVERIFIED] — owner or Gurafa verify | Owner/Gurafa |
| Monday May 11: Meta Ads Library scan | Scheduled | Gurafa |

---

## BLOCKED on owner action

| Item | Why blocked | ETA |
|---|---|---|
| Gmail OAuth scope | Disconnect/Reconnect + Google Read checkbox ✅ | owner 2-min action |
| Drive Read-only tier | Connectors → Drive → Read-only dropdown → "Always allow" | owner 30-sec action |
| Apr 20 Marketing KPI Scenario A/B/C pick | Mentari rec = B (1,500₾/mo concentrated burst) | owner decision |
| OKR2 scope refine accept | Proposal: "2 vertical Power BI templates + SaaS wrapper" (NOT generic Power BI products) | owner ack |
| Mariam directive v3 KPI gates re-embed | Apr 22 directive missed v3 precision, needs ship-again | Mentari P1 next session |
| **Mari Mik account list (11) + exit motive** | Surfaced Apr 27 risk HTML; step 1 (account list) + step 2 (exit conversation) owner-side | owner 1h total — ASAP, 35-day window |
| GA4/GSC access verification | Viktor Apr 25 brief ask: 30-day baseline pull blocked on Mentari-side access | owner confirm Mentari has GA4 read |
| FB Policy 12-day stale (Apr 15→Apr 27) | LTV/CAC inputs received Apr 20, threshold not confirmed, owner final approve pending | owner approve/reject |

## Mentari next-session P0-P3

| P | Item | OKR trace |
|---|---|---|
| P0 | Gmail retest after scope fix + Drive toggle pull | — infrastructure |
| P0 | ~~bivision.ge P0 audit fix~~ — Apr 25 SUPERSEDE (Geo-only execute), Mentari role = analysis only | — |
| ~~P0~~ | ~~Audit V2 copy-fix ship~~ ✅ SHIPPED Apr 27 | OKR3.4 |
| P1 | Billings sheet auto-read → ARR breakdown + Salary:ARR ratio | OKR1.KR1 + KR3 |
| P1 | Marketing tracker dashboard v1 scaffold | OKR3 all KR |
| P1 | Mari Mik handover skeleton draft (gated on owner step 1) | OKR4.KR5 |
| P2 | Qlik Cloud client list → AI use-case map → Gurafa handoff | OKR4.KR2 |
| P2 | Mariam directive v2 re-ship with v3 gates | OKR3 |
| P3 | Playwright LinkedIn admin session baseline | OKR3.1/3.2 |

## Shipped Apr 27 → Apr 29 morning

- ✅ Mari Mikurt Departure Risk Surface — `outputs/2026-04-27 Mari Mikurt Departure Risk Surface by Mentari.html` (OKR4.KR5; off-priority drift)
- ✅ Apr 25 Viktor Hardening Brief ACK — AUDIT_REQUEST.md entry Apr 27
- ✅ Bivision Site Audit V2 Copy-Fix — `outputs/2026-04-27 Bivision Site Audit V2 Copy-Fix by Mentari.html` (OKR3.4, 5/6 Viktor calibrations)
- ✅ status-2026-04-27.html v2 (canonical OKR + done + plan + owner-pending + delegation; 1480px layout + nowrap KR tables)
- ✅ Marketing KPI Scenario B LOCKED Apr 27 (1,300₾/mo × 3: FB 1000 + LinkedIn 200 + Mailchimp 100)
- ✅ MENTARI_CROSS_AGENT_RESPONSES_2026-04-27 (11 thread closures consolidated)
- ✅ MENTARI_AUDIT_GURAFA_2026-04-27 (GitHub Repos counter-audit, PARTIAL PASS)
- ✅ Dashboard cleanup conservative (C-Suite Decision tab removed, status v2 link, MRR 66.7→67.3K, stale warnings)
- ✅ Cross-agent scans 4 (evening Apr 27 + late Apr 27 + Apr 28 morning + Apr 29 morning)
- ✅ Memory: `feedback_destructive_action_verify_target.md` + `feedback_bivision_shares_remote_canonical.md` saved
- ✅ Questionnaire restoration (5 files restored after Apr 27 mistaken delete)
- ✅ WebSearch lead-gen research delivered (Apollo/Lemlist/Expandi/Waalaxy/LGM verified pricing + 2026 LinkedIn safe limits + Khoshtaria framework industry-aligned)
- ✅ session-close.md §6a — standard pre-/clear command added (cross-agent canonical)
- ✅ bivision-shares re-cloned after Apr 28-29 temp wipe

## Retired items

- HubSpot MCP connector — ✅ full access confirmed Apr 23, retire "3 self-fix path"
- Readout v2 — deprioritized per OKR filter (meta-work ban in trust-deficit window)

## Weekly cadence (starting Mon)

- Mon AM: CEO brief HTML (right / wrong / missing / resource redirect) — weekly rhythm
- Daily session-start: Mariam OKR3 delta check (Reels count, post count, ban-list, FB Leads >24h pending)

## Viktor 2026-05-01 — Token Optimization protocol open items

**Pending owner action:**
- Layer 2 Anthropic console "Active sessions" / login activity check (Gabo blind-spot verification on Solo plan)
- Dispatch 4 agent prompts (Gurafa account ToS, Geo local audit, Agent A self-audit, Agent B self-audit) — paste-ready in Viktor session scrollback
- /clear after this snapshot, switch `/model claude-sonnet-4-6` for execution-tier work
- PowerShell `$PROFILE` functions (viqtor/gurafa/Nikacho/mentari) verify cd-to-project-root works (or fix with template in Token Audit HTML)

**Pending Viktor (next session):**
- Receive 4 outputs → consolidation HTML "Token Usage Final Audit + Migration Decision Input"
- 5-task benchmark suite definition for Migration Assessment Phase 1 parallel trial (Bivision Q&A / Multi-file SSOT / Audit task / Research scout / Cross-agent coord)
- MEMORY.md prune (currently 25.5KB > 24.4KB limit, truncated load)
- F4 Dastafe — Apr 28 Gurafa brief "ACTIVE-WATCH Balance ERP overlap" vs Viktor REJECT (DataFest conf misID) — cross-confirm owner-instructed reject

**Pending DonotUseMe:**
- Data-source connection protocol document creation (T1 browser → T2 CSV → T3 OAuth → T4 API key → T5 SA fallback)
- GA4 Service Account workspace-policy blocker resolution path (T1/T2 fallback per protocol)

**Pending Geo:**
- F4 Bivision local Claude state audit (PowerShell + settings.json + processes + credentials existence)

**Pending Gurafa:**
- Account ToS research (Solo Max multi-device, Sonnet quota share)
- Claude Managed Agents deep-dive 1.5hr (re Mentari re-eval per Apr 28 brief)
- F1 verification: BiPriceMonitoring = Retail Info rename? BiDistribution source?

## Added 2026-05-02

**Owner action:**
- GA4 Key Events: Admin → Events → mark `whatsapp_click`, `phone_call`, `contact_form_submit` as key; unmark `close_convert_lead`, `purchase`, `qualify_lead`

**Pending Geo (next session):**
- Execute Issue #3 plan: `Nikacho/docs/superpowers/plans/2026-05-02-projects-pages.md` (6 tasks: list page + 3 project pages + homepage links + deploy + changelog V20)

**Pending Mentari/Viktor:**
- bivision.ge TTFB regression: 1.35s (Apr 23) → 1.79s (May 2) — LiteSpeed cache miss investigation needed
- bivision.ge CSP still missing — implementation needed
- bivision.ge HSTS upgrade: 86400 → 31536000

**All agents:**
- superpowers plugin now global (v5.0.7). Use `writing-plans` before multi-step tasks, `subagent-driven-development` for parallel execution. Skills at `~/.claude/plugins/cache/claude-plugins-official/superpowers/5.0.7/skills/`
