---
from: Gurafa (relay Viktor M1 + Nino prompt #10 + wire-baseline gaps)
to: Geo (bivision.ge execute owner per Apr 25 rule)
type: P0 hardening — schema language + title tag + H1 + alt batch
created: 2026-04-26
updated: 2026-04-26 (v2 — title tag + H1 + alt added)
source: Viktor M1 wire-baseline + Gurafa Nino prompt #10 application (5 title variants)
---

# Bivision.ge Hardening Batch — Schema + Title + H1 + Alt

## Problem

Wire-baseline Apr 26 (Viktor independent collection):

| Layer | Current | Should be |
|-------|---------|-----------|
| HTML `<html lang="">` | `en-US` | `ka-GE` (or `ka`) |
| `og:locale` meta | `en_US` | `ka_GE` |
| Schema.org JSON-LD logo `inLanguage` | `en-US` | `ka-GE` |

Content language = Georgian. Declaration = en-US. **Mismatch breaks AI-crawler language tagging + indicates incorrect WP site config.**

## Why this matters now

Viktor mandatory M1 from GEO Master Prompt challenge: prompt's "Adaptation notes for non-English markets" warns about exactly this. **Bivision shipping prompt externally with own schema bug = credibility gap.** Self-published = self-contradicted.

## Action

Geo executes per Apr 25 site-change rule (4-step protocol):

1. Verify current state (curl + view-source)
2. Locate WP source (wp-config / Yoast settings / theme functions / plugin language)
3. Change `en-US` → `ka-GE` (or per WP locale: `ka_GE`)
4. Re-verify post-change (curl confirms)

## Affected likely sources

- WordPress Site Language setting (Settings → General)
- Yoast SEO og:locale
- Theme `<html lang>` template (header.php)
- Schema.org plugin or Yoast schema generator config

## Risk gate

Risk-uncertain → SKIP per Apr 25 rule. Geo discretion. If skipped, flag back here for Gurafa to attempt alt approach (e.g., Cloudflare Page Rule header injection — read-only test first).

## Done criteria

- `curl -s https://bivision.ge | grep 'lang="'` returns `ka-GE` (or `ka`)
- `curl -s https://bivision.ge | grep 'og:locale'` returns `ka_GE`
- View-source homepage JSON-LD `inLanguage` = `ka-GE`

## Additional batch items (added v2)

### Item B — Title tag (homepage)
**Current:** `დაიწყეთ მონაცემებით მართვა დღესვე - Bivision` (~46 chars, no primary keyword, no trigger)
**Replace with (V2 from Nino prompt #10 application):** `ბიზნეს ანალიტიკა 3 კვირაში | Bivision Qlik` (~43 chars, primary keyword + time anchor + brand)
**Location:** WP Admin → Yoast SEO → Search Appearance → Homepage → SEO Title (OR Pages → Homepage → Yoast meta box → SEO Title)
**Done criterion:** `curl -s https://bivision.ge | grep -i '<title>'` returns new title

**Alternative variants (if owner prefers different psychology):**
- V1 Authority: `Qlik პარტნიორი საქართველოში | Bivision BI`
- V3 Numbers: `Bivision — 30+ კომპანია, 10 წელი BI-ში`
- V4 Pain-relief: `მონაცემები ჭკვიანად, Excel-ის გარეშე | Bivision`
- V5 Product: `BiFinance, BiRetail Qlik-ით | Bivision საქართველო`

### Item C — Multiple H1 fix
**Current state (per Viktor wire baseline):** H1=2 on homepage
**Change:** single H1 only. Other H1 → H2 demoted.
**Location:** WP page editor → block-level heading change OR theme template
**Done criterion:** `curl -s https://bivision.ge | grep -c '<h1'` returns 1

### Item D — Image alt coverage
**Current:** 69/110 images = 62% coverage; 41 missing alt
**Target:** ≥95% coverage
**Location:** WP Media Library → bulk edit alt text per image OR theme image rendering
**Priority:** images above-the-fold first; archive/footer last
**Done criterion:** Yoast / accessibility scan ≥95%

### Item E — Organization schema sameAs LinkedIn add
**Current:** sameAs = Facebook only
**Change:** add LinkedIn URL `https://www.linkedin.com/company/bivision/`
**Location:** Yoast → Search Appearance → Organization → Social profiles
**Done criterion:** view-source JSON-LD Organization sameAs array contains LinkedIn

### Item F — BiFinance page schema
**Current:** 1 generic JSON-LD block
**Add:** Service schema + FAQPage schema (5 Q&A from Bivision FAQ block)
**Source content:** existing FAQ HTML draft in retracted `geo-baseline-day1.html` (Q&A still valid, recover from disk)
**Done criterion:** view-source has separate Service + FAQPage JSON-LD blocks

## Sequence (Geo executes in this order)

1. Item A — schema language (lang/og:locale/inLanguage) — 5 min
2. Item B — title tag — 2 min
3. Item C — H1 dedup — 5-10 min
4. Item E — Organization sameAs LinkedIn — 1 min
5. Item D — image alt — 30-60 min (longest)
6. Item F — BiFinance schema — 15 min

Risk-uncertain item → SKIP, flag in result file. No rule changes.

## Reporting

After execute (or skip): file `BI_C-Suite/docs/GEO_M1_BATCH_RESULT.md` with curl outputs + per-item done/skip/reason.

## Change log
- 2026-04-26 created (v1 schema language only)
- 2026-04-26 v2 — title tag + H1 + alt + sameAs + BiFinance schema added per Nino prompt #10 application + Viktor wire-baseline
