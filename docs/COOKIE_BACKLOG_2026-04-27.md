---
from: geo
to: owner + viktor
type: cookie compliance backlog
created: 2026-04-27
priority: P2 — defer Apr 30+ revisit
disk-channel: cross-agent BI_C-Suite/docs
---

# Cookie Compliance Backlog — Apr 27

## Status

**Closed Apr 27 cookie sprint with partial resolution.** Site reverted to CookieYes baseline. Real-fix path identified but requires owner / theme-dev / paid-plugin gate.

## Goals scoreboard final

| Goal | State Apr 27 | Achieved? |
|------|--------------|-----------|
| #1 Pre-consent tracker firing block (compliance) | LinkedIn × 3 + GA4 × 2 wire-captured fires pre-consent | ❌ NO |
| #2 Multi-language banner KA+EN | English-only CookieYes free | ❌ NO (paid feature) |
| #3 Clean branding ("Powered by CookieYes" hidden) | branding visible | ❌ NO (paid feature) |
| #4 Auto-categorization (uncategorized cookies blocked pre-consent) | 1 uncategorized (`cookies.js`) — CookieYes can't block without script URL pattern | ❌ NO |

## Root cause analysis

### Why Complianz attempt failed
- BeVision custom theme blocks Complianz JS injection (likely missing `wp_footer()` / `wp_head()` hooks OR custom output filter)
- LSWS plugin disconnected from server ("LSCache caching functions on this page are currently unavailable")
- Reinstall + cache purge + .htaccess touch all ineffective
- [EP1: HYPOTHESIS] — single-failure sample, theme-block thesis not yet confirmed via second plugin (Termly) attempt

### Why CookieYes manual categorize insufficient for Goal #1
- LinkedIn `bcookie` already in Advertisement category with script URL pattern `.linkedin.com|licdn.com` ✓
- BUT pre-consent firing observed `px.ads.linkedin.com/wa` POST + GA4 `google-analytics.com/g/collect` POST
- Reason: trackers fire from **GTM-KLWN32H3 container inline JavaScript**, not from external script URL loads
- CookieYes script-URL-blocking can't intercept GTM-inline-fired tags
- Real-fix paths require GTM container modification OR Google Consent Mode V2

## Real-fix path options (defer Apr 30+ revisit)

### A. GTM container consent gate (recommended)
- Owner login tagmanager.google.com → GTM-KLWN32H3
- Per-tag (LinkedIn Insight + GA4) → set Consent Initialization trigger to "after Marketing/Analytics consent given"
- Tags fire ONLY post-Accept All click
- Effort: 1-2 hr owner work
- Cost: $0
- Solves: Goal #1 ✓ definitively

### B. Google Consent Mode V2 plugin
- Complianz Premium ($9/mo) OR free alternative with GCM v2 support
- Auto-handles consent gate for Google + Microsoft tags
- Effort: 1 hr install + config
- Cost: $9-15/mo OR theme-dev fix to make plugin load

### C. BeVision theme dev investigation (gates Multi-lang #2 + Branding #3)
- Theme developer audit — ensure `wp_footer()` + `wp_head()` standard hooks present
- Re-test Complianz / Termly / other multi-lang plugin install
- If theme fix succeeds → Goals #1+#2+#3 all solvable via plugin
- Effort: 2-4 hr unknown (depends theme code)
- Cost: dev rate × hours

### D. Manual `cookies.js` script URL pattern
- 1 uncategorized cookie identified via CookieYes Cookie Manager
- Add script URL pattern manually (need source identification first — appears to be theme-bundled)
- Effort: 10-15 წთ if source identifiable; deeper if obscure
- Solves: partial Goal #4 only

## Recommended path

**A first (GTM gate)** — solves real GDPR exposure (Goal #1) without plugin churn or theme dev block. Then C (theme dev) when capacity allows for Goals #2+#3.

## Apr 30+ revisit triggers

- Owner GTM access + 1-2 hr block
- BeVision theme dev availability (დათო/გაბო or Mari Mik handover scope)
- Phase A v3 SEO sprint completion (ROI compare)

## What stays as-is until revisit

- CookieYes free active baseline
- 1 uncategorized cookie (`cookies.js`) — non-critical for Goal #1 (real exposure = LinkedIn + GA4 from GTM)
- Multi-lang gap (English-only banner)
- Branding visible

## Memory rules applied

- `feedback_visibility_not_urgency.md` — Apr 30+ revisit per visibility-not-urgency rule
- `feedback_result_over_bureaucracy.md` — plugin churn skipped, real-fix path documented
- `feedback_no_fabrication.md` — facts wire-verified, hypothesis tagged [EP1]
- `feedback_enforcement_protocol_apr27.md` — counter-audit cycle Geo↔Viktor working

## Status

CLOSED current sprint. Open Apr 30+ revisit. Owner triage path A/B/C.

Memory rules applied: [EP0 ✓ / readable-Georgian where applicable ✓ / 4-block ✓ / no-fabrication ✓ / probe-discipline ✓ / verify-before-trust ✓ / visibility-not-urgency ✓ / enforcement-protocol-apr27 ✓ / EP1-tagging ✓]
