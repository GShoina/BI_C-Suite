---
from: geo
to: viktor
type: cross-project playbook brief
created: 2026-04-27
priority: P2 — reference for other projects
source: bivision.ge sprint Apr 25-27
---

# SEO + Site Technical Playbook — Bivision Sprint Reusable

## Purpose

Owner directive Apr 27: ბივიჟენზე გასაკეთებელი → დაიმახსოვრე; ვიქტორმა სხვა პროექტებზე გამოიყენოს. ეს ბრიფი = playbook სხვა WordPress/SEO პროექტებისთვის (ICR Trade, Geocord, Nutrimax, Mardaleishvili, Engurhesi და სხვ.)

## Stack baseline (Bivision LIVE confirmed)

- **WordPress** + **Rank Math PRO** (SEO plugin)
- **Custom theme** (BeVision — blocks some plugin JS injection)
- **FastCloud LSWS hosting** (LiteSpeed Web Server)
- **CookieYes free** (cookie consent — works baseline)
- **Wordfence** (security)
- **Optimole** (image lazy-load + alt auto-fill hypothesis)
- **GTM container** (GA4 + LinkedIn Insight tracking)

## SEO playbook — works (verified)

### 1. Title optimization (V2 pattern)
**Format:** `[Primary keyword] [outcome promise] | [Brand] [tech]`
**Bivision example:** `ბიზნეს ანალიტიკა 3 კვირაში | Bivision Qlik`
**Tool:** Rank Math homepage SEO settings → Page Title field
**Why works:** focus keyword first (SEO weight), outcome quantified (CTR boost), brand+tech tail (recognition)
**Reusable:** ICR Trade `[ცემენტი დისტრიბუცია] [SLA promise] | ICR Trade`; Mardaleishvili soft

### 2. Focus keyword + secondary list (Rank Math)
**Path:** Rank Math homepage → Focus Keyword field
**Format:** `★ [primary keyword]` + 9 secondary comma-separated
**Verify:** save → `curl -s [URL] | grep -A1 "rank-math-yoast-content"` (or check page source)
**Reusable:** every site needs 1 ★ primary + 5-10 secondary; AI bot signal

### 3. Organization schema sameAs (social profile signal)
**Path:** Rank Math → Titles & Meta → Social Meta → Additional Profiles textarea
**Add:** LinkedIn URL + Facebook URL + YouTube URL (each on new line)
**Verify:** `curl -s [URL] | grep -oE '"@type":"Organization"[^}]+sameAs[^]]+\]'`
**Result:** `"sameAs":["https://www.facebook.com/...","https://www.linkedin.com/..."]`
**Why works:** AI search citation signal; Google entity recognition
**Reusable:** every B2B site

### 4. Legacy 301 redirects
**Path:** Rank Math → Redirections → Add New
**Pattern:** old broken URL → current canonical
**Why works:** preserves backlink equity, fixes 404s
**Reusable:** post-redesign cleanup, junk URL 410'ing

### 5. GSC URL Inspection submit (post-update re-crawl request)
**URL:** `https://search.google.com/search-console?resource_id=https://[domain]/`
**Path:** URL Inspection input → paste full URL → Enter → wait live test → Request indexing
**Result:** "URL was added to a priority crawl queue"
**Limit:** ~10-15 URLs/day quota
**Reusable:** post-Title V2 / sameAs / focus keyword update — always re-submit affected URLs

## SEO playbook — failed (skip these)

### 1. SoftwareApplication schema for SaaS without testimonial data
**Reason:** Rank Math Software template requires aggregateRating; Google rich result invalid without it; fake rating banned
**Alternative:** Service schema (default Rank Math, valid without rating)
**Re-eval trigger:** real testimonial collection process exists OR owner-decide proceed-without-rating

### 2. SoftwareApplication via Display Conditions to CPT
**Reason:** Service schema overlap risk + form-required field conflict
**Backlog:** `BI_C-Suite/docs/SOFTWAREAPPLICATION_BACKLOG_2026-04-27.md`

## Site technical playbook — works

### 1. Security headers (.htaccess)
**5 headers:**
```
Header always set Permissions-Policy "geolocation=(), camera=(), microphone=()"
Header always set X-Frame-Options "SAMEORIGIN"
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header unset X-Powered-By
```
**Verify:** `curl -I https://[domain]/`
**Reusable:** every WP site

### 2. HSTS staged rollout
- **Phase 1 test:** `Header always set Strict-Transport-Security "max-age=300"`
- **Phase 2 prod:** `max-age=86400` (24h)
- **Phase 2.5:** `max-age=86400; includeSubDomains` (cautious before preload commit)
- **Phase 3 preload:** `max-age=31536000; includeSubDomains; preload` + submit `hstspreload.org`
**Why staged:** subdomain conflicts caught before 1-year commit irreversible
**Reusable:** every HTTPS site; never skip to Phase 3 directly

### 3. .htaccess backup before edit
**Pattern:** `cp .htaccess .htaccess.bk-pre-[change]-[date]`
**Reusable:** every .htaccess change; rollback inline

### 4. 4-step protocol (cross-cutting)
1. Backup
2. Action
3. Verify ≤5 min
4. Revert if fail
**Reusable:** ALL site changes (plugin install, .htaccess, SEO settings)

## Site technical playbook — failed (skip these or theme-dev gate)

### 1. Complianz cookie banner on custom theme
**Reason:** BeVision missing standard `wp_footer()` / `wp_head()` hooks → Complianz JS not injecting; only `cmplz-general-css` link in DOM, no `<script>`
**Diagnostic:** `curl -s [URL] | grep -i complianz`
**Pattern likely repeats:** any custom theme without standard hooks
**Pre-test:** verify hooks before plugin install — `grep -r "wp_footer\|wp_head" [theme-folder]/`
**Alternative:** theme dev fix OR Cookiebot/Termly free trial

### 2. .htaccess Anti-Spam RewriteRule on LSWS
**Reason:** LSWS environment didn't fire any of 3 variants (`[G,L]` / `RedirectMatch 410` / `[R=410,L]`)
**Diagnostic:** apply rule + LiteSpeed Cache → Toolbox → Purge All + curl test
**Alternative:** Wordfence Firewall block rule OR FastCloud support ticket

### 3. GTM consent gate via plugin script-URL-pattern blocking
**Reason:** trackers fire from GTM-inline JavaScript, not external script URLs; CookieYes/Complianz can't intercept inline-fired tags
**Real fix:** GTM container per-tag consent trigger (Consent Initialization → Marketing/Analytics consent given) OR Google Consent Mode V2

## Indexation cleanup playbook

### Junk URL 410 process
1. Identify via GSC Coverage report (Excluded → 404 errors)
2. Add 410 redirect (Rank Math Redirections → Type 410)
3. Submit URL Inspection → Validate Fix
4. Wait Google refresh ~7-14 days

## Pre-execute checklist (4-step protocol expand)

1. **Verify** — disk-state + memory check; risk known?
2. **Challenge** — value > cost? OKR/KR trace?
3. **Factcheck** — preconditions met? (testimonial data / theme hooks / required fields)
4. **3/3 pass** → priority list candidate
5. ❌ ერთიც fail → backlog file, არა priority list (`feedback_pre_priority_gate.md`)

## What Viktor should reuse vs. skip

**REUSE:**
- 5 security headers + HSTS staged rollout (universal)
- Title V2 pattern + focus keyword (any SEO project)
- Organization schema sameAs (B2B sites)
- 4-step protocol (every site change)
- Pre-priority gate 3-question (every priority list)
- GSC URL Inspection re-crawl post-update

**SKIP / theme-dev gate first:**
- SoftwareApplication schema (until testimonial data)
- Complianz on custom theme (verify hooks first)
- .htaccess RewriteRule on LSWS (test alternatives)
- Plugin script-URL consent gate (use GTM container instead)

## References on disk

- `outputs/2026-04-25 *` — HSTS Phase 1, baseline
- `outputs/2026-04-26 *` — Title V2, redirects, HSTS Phase 2
- `outputs/2026-04-27 *` — Phase A v3 corrections, owner ACK, GSC submits
- `BI_C-Suite/docs/COOKIE_BACKLOG_2026-04-27.md` — cookie compliance gap
- `BI_C-Suite/docs/SOFTWAREAPPLICATION_BACKLOG_2026-04-27.md` — schema deferred
- Memory: `project_bivision_sprint_apr25_27.md`

Memory rules applied: [EP0 ✓ / no-fabrication ✓ / verify-before-trust ✓ / risk-gate Apr 25 ✓ / pre-priority gate Apr 27 ✓ / readable-Georgian ✓]
