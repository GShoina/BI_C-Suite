---
class: SESSION SNAPSHOT (pre-/clear)
created: 2026-04-23
owner: Mentari
trigger: owner directive "შეინახე ყველაფერი რომ ახალ ფანჯარაში გავხნა"
---

# Session Snapshot — Apr 22-23 (Mentari)

## Active state — რა ხდება ახლა

**Active task:** Gmail/Drive connector scope fix.
- Gmail: owner added, OAuth scope still insufficient → session token cached, needs Claude Code window restart
- Drive: Read-only tier "Needs approval" → change to "Always allow" (per `drive.png` screenshot)
- HubSpot ✅ full read+write verified

**Blocking owner's immediate next move:** new Claude Code window launch → retest Gmail + fix Drive toggle.

---

## Shipped Apr 22-23

### Apr 22
- OKR Framework v1 HTML `outputs/2026-04-22 Bivision OKR Framework Draft by Mentari.html`
- OKR Alignment Bundle HTML
- Viktor directive `docs/MENTARI_TO_VIKTOR_2026-04-22.md`
- Gurafa directive `BI_gurafa/docs/MENTARI_TO_GURAFA_2026-04-22.md`
- Mariam directive `docs/MARIAM_DIRECTIVE_2026-04-22.md`
- Memory: `feedback_mariam_tracking_scope.md`, `feedback_path_laconic_bullet.md`

### Apr 23
- OKR1.KR1 corrected: 950K → **95K** (1.4x, +40%) on 2 files + memory index. Commit `41612cd` pushed
- BiFinance email share: `https://gshoina.github.io/bivision-shares/bifinance-email-v2.html` (commit `eed5408`)
- 12-point owner directive absorbed (Apr 23)
- Path → **Next** rename locked in 4-block shell (output-format feedback memory)
- Memory updates: Path→Next rename, MEMORY.md index refresh

---

## Owner directive Apr 23 — 12 points (absorbed, state after each)

1. **ARR 68K → 95K** ✅ fixed disk + hosted
2. **Access verification** ✅ done:
   - HubSpot ✅ full (gela.shonia@bivision.ge, accountId 147341634, full CRM r/w)
   - Gmail ❌ OAuth scope insufficient even after connector add
   - Drive ❌ same scope issue + UI tier "Needs approval"
   - Mailchimp 🟡 MCP = campaign edit/generate only, no analytics
   - Qlik Cloud 🟡 no MCP, REST API path available
   - LinkedIn Company admin 🟡 Playwright session path
   - GA4/SC/GTM 🟡 Playwright session path
3. **Power BI McKinsey assessment** — captured in main chat:
   - a) AI first, Power BI = commodity/vendor-agnostic requirement
   - b) IP = connector stack + vertical template + ongoing data pipeline (SaaS wrapper on top of Microsoft layer)
   - c) Edge = vertical + ERP integration, NOT generic Power BI consulting. In-team (Luka/Mari Mag), NOT outsource
   - **OKR2 scope refine proposed:** "2 Power BI product" → "2 vertical Power BI TEMPLATE (BiFinance-energy + BiMedical) SaaS wrapper"
4. **Claude Connect status** ✅ HubSpot, ⚠️ Gmail/Drive scope pending
5-6. skipped in directive
7. **Billings 2026 sheet** pending Drive scope fix → ID `1krlXbidEyk_KLzdLvDFGTRpmTmyhYsgdiyss6Bvurfc` → auto ARR breakdown + Salary:ARR ratio
8. **Qlik+Claude MCP protocol** understood — don't ask. Plan: existing Qlik Cloud client list → AI use-case mapping (Gurafa OKR4)
9. skipped in directive
10. **LinkedIn Company admin** — Playwright session with owner-opened admin tab piggyback
11. **GA4 + Search Console + GTM** — Playwright session, SEO focus per bivision.ge audit
12. **bivision.ge audit review** — absorbed, see below

---

## bivision.ge Audit Absorbed — Apr 23 alternative research

**Source:** `https://gshoina.github.io/bivision-shares/bivision-audit-2026-04-23.html`

**Findings Mentari agrees:**
- TTFB 1.35s → 0.6s target (LiteSpeed Mobile off = free uplift)
- Rank Math 76/100 underused (Content AI + Instant Indexing unused)
- Schema missing 6 product page → AI Overview + rich snippet blocker
- 2FA off both admin + info@bivision.ge public exposure
- 0 HTTP security headers

**Mentari action plan (OKR3.4 + OKR3.3 trace):**
- **P0 today/next session, 2-3h:** LiteSpeed Cache Mobile ON + Rank Math Instant Indexing + Schema (Service + Product) 6 pages + Content AI top-5 rewrite
- **P1:** 2FA both admin + security headers via .htaccess + /llms.txt
- **P2:** Redis/Memcached (Luka/Gabo Playwright verification)

---

## Open Items

### Blocking (need owner action)
- **Gmail OAuth scope** — Disconnect + Reconnect, Google consent-ზე Read ✅
- **Drive UI tier** — Connectors → Google Drive → Read-only dropdown → "Always allow"
- **Scenario A/B/C pick** — Apr 20 Marketing KPI v3 (Mentari rec = B 1,500₾/mo concentrated burst), owner ack pending

### Mentari backlog (parallel)
- FB Policy Apr 15 6-day stale (now 8-day) → owner-surface HTML
- HubSpot connector 3 self-fix path — now resolved? HubSpot MCP ✅ full access confirmed Apr 23 → retire this item
- Mari Mikurt 2026-06-01 departure + 11-account handover → risk surface HTML
- Readout v2 (EP0 + EP1 + overlay SSOT consolidation) — deprioritized per OKR filter
- Marketing tracker dashboard v1 scaffold — OKR3-mapped, v3 gates color-coded, source per metric
- Mon first CEO brief HTML — weekly cadence start

### Quick wins (can execute immediately next session)
- bivision.ge P0 audit fix (OKR3.4 trace, 2-3h)
- Billings sheet auto-read (once Drive scope ok) → ARR breakdown + Salary:ARR
- v3 gates re-embed into Mariam directive (Apr 22 directive missed v3 precision)
- Qlik Cloud client list → AI use-case map (send to Gurafa OKR4)

---

## Power BI strategy — my recommendation to owner (summary)

**AI concentrate, NOT Power BI.**

Reasoning chain:
1. Power BI = Microsoft commodity viz layer — no IP possible at viz level
2. SaaS survival requires IP layer — IP at connector stack (Fina/Oris/1C/Balance) + vertical template (energy/retail/medical) + ongoing pipeline service, NOT viz
3. Generic Power BI consulting = losing race (DataStudio, BDO, freelancers flood Georgian market)
4. 2-year-late penalty can be skipped IF bet = vertical template, not generic BI
5. Outsource hire = generic skill, NO. In-team (Luka, Mari Magh) ship vertical template

**OKR2 scope refine proposal:**
- Before: "2 Power BI products launched in 2 months"
- After: "2 vertical Power BI TEMPLATES (BiFinance-energy + BiMedical) + SaaS wrapper (connector + template + ongoing support)"

**Pending owner decision:** accept OKR2 scope refine? or keep original generic wording?

---

## Memory updates this session (Apr 22-23)

- `feedback_mariam_tracking_scope.md` — NEW, Mentari = continuous OKR3 tracker + CEO brief
- `feedback_path_laconic_bullet.md` — NEW/REPURPOSED: Path → Next rename, 1-line bullet rule
- `feedback_output_format_default.md` — UPDATED: "Path / Artifact Confirmation" → "Next (The following must be completed)"
- `project_bivision_okrs_2026.md` — UPDATED: KR1 95K (was 950K), Apr 23 correction note
- `MEMORY.md` index — 2 entries updated

---

## Self-violations caught this session

1. Mariam directive Apr 22 missed v3 KPI gates (Apr 20 precision dropped) — caught by owner's memory prompt
2. "გავაგრძელო?" permission question — caught, `feedback_no_permission_questions.md` applied
3. Multi-line Path with rationale/caveats inline — caught, Path → Next + 1-line bullet rule

---

## Sprint state

- Day 5/14 of 14-day execution proof sprint (Apr 19 → May 3)
- Daily MUST Apr 22: ✅ OKR Framework + Alignment Bundle shipped
- Daily MUST Apr 23: in progress — bivision.ge P0 audit fix planned

---

## Safe to /clear

Next session first reads:
1. This file (`SESSION_2026-04-23_plan.md`)
2. `CLAUDE.md` (Mentari identity)
3. `OWNER_DIRECTIVE_APR19.md` (sprint ultimatum)
4. `EXECUTION_QUEUE.md` (active priorities)
5. `AUDIT_REQUEST.md` (Viktor feedback queue)
6. Memory MEMORY.md index
