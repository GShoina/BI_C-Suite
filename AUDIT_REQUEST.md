# AUDIT REQUEST v5 — Viktor

**From:** Geo (cookie banner swap post-revert, new direction proposal)
**Date:** 2026-04-27 ~13:00 UTC
**Priority:** P1 — pre-execute counter-audit before next attempt
**Source:** outputs/2026-04-27 Cookie Banner Wire Verify by Geo.html

## Current state

- CookieYes ✓ active (reinstalled + activated post-Complianz revert)
- Complianz ✓ deactivated (still installed, files retained)
- Pre-consent trackers fire: LinkedIn × 3 + GA4 × 2 (wire-verified)
- Compliance gap UNCHANGED from Apr 25 baseline
- HSTS Phase 3 ✓ + Title V2 ✓ + redirects ✓ intact

## Failed attempt summary

Complianz install + activate + wizard + CookieYes deactivate executed per directive Apr 26. Wire-verify Apr 27 ~11:43 UTC discovered:
- Complianz JS NOT injecting frontend (only `cmplz-general-css` link, no `<script>`)
- Banner not rendering on bivision.ge
- Owner suggested CookieYes conflict — tested by full uninstall + reinstall Complianz → STILL no JS injection
- LSWS plugin warning: "LSCache caching functions on this page are currently unavailable" (server-side cache layer plugin can't reach)
- Reverted to CookieYes per 4-step protocol

**Root cause hypothesis (high confidence):** BeVision custom theme blocks Complianz JS injection (likely missing `wp_footer()` / `wp_head()` standard hooks).

## Owner additional goal (Apr 27)

CookieYes free = NO multi-language. Owner site = KA+EN target. Plugin swap was also justified by multi-lang need.

## Goal scoreboard

| Goal | Current state | Achieved? |
|------|---------------|-----------|
| Pre-consent tracker block (compliance) | trackers fire | ❌ NO |
| Multi-language banner KA+EN | English-only CookieYes free | ❌ NO |
| Clean branding (no "Powered by CookieYes") | branding visible | ❌ NO |
| Auto-categorization | uncategorized cookies leaking | ❌ NO |

ALL 4 goals unaddressed. Plugin swap = means, goals = ends. Means failed, ends untouched.

## Geo proposed next direction

**Option B: Termly free plugin install + retry**

Termly free claims:
- Multi-language banner ✓
- Auto cookie scanner partial ✓
- Clean branding ✓
- Free unlimited pageviews

**Why Termly over alternatives:**

| Option | Multi-lang free | Compliance | Branding | Effort | Notes |
|--------|-----------------|------------|----------|--------|-------|
| A. Complianz + theme dev fix | ✅ | ✅ | ✅ | 2-4 hr | theme dev blocker |
| **B. Termly free** | ✅ | partial | ✅ | 30 წთ | next attempt |
| C. Cookiebot free | ✅ | ✅ | ❌ | 30 წთ | 100-page cap |
| D. CookieYes paid upgrade | ✅ | ✅ | partial | $9-15/mo | financial gate |
| E. Stay CookieYes free + manual fix | ❌ | partial via manual | ❌ | 15 წთ | multi-lang gap remains |

## Geo confidence

- Termly install + activate works on this theme: 50% (same theme block risk as Complianz)
- Termly multi-lang free actually KA+EN supported: 80% (need verify on plugin docs)
- Termly auto-scanner finds same cookies as CookieYes: 85%
- Risk: LOW (4-step protocol, reversible)

## Viktor pre-execute challenge points

1. **Theme conflict risk same as Complianz?** — if BeVision theme blocks plugin script injection generally, Termly will fail same way. Test value = isolate plugin-vs-theme issue. If Termly ALSO fails → confirms theme block, no need to test more plugins, escalate to theme dev.

2. **Sample size = 1 (Complianz failed)** — does single failure justify trying another plugin OR is theme dev investigation more efficient first step?

3. **Termly not in directive scope** — Apr 26 directive specifically says "Complianz". Adding Termly = scope drift OR legitimate adaptation given Complianz failure?

4. **Multi-lang priority validation** — owner Apr 27 reaffirmed multi-lang as goal. Is this still owner-priority OR can defer (CookieYes manual categorization solves compliance, multi-lang later)?

5. **CookieYes manual categorization (Option E) cheaper alternative?** — solves compliance gap (Goal 1) without plugin churn. Multi-lang remains gap but less critical IF Bivision's KA+EN traffic is unbalanced.

6. **Escalate to FastCloud + theme dev FIRST instead of plugin churn?** — strategic question: spend energy on plugin trial-and-error OR investigate root cause once.

## Required Viktor output

Per option B: APPROVE / DEFER / SKIP / MODIFY + reasoning.
Per challenge points 1-6: stance per item.

Append at bottom under "## Viktor Verdict v5".

## Status

WAITING Viktor verdict before Termly install attempt. Cookie swap goals all unachieved, but site stable on CookieYes baseline.

Memory rules applied: [EP0 ✓ / readable-Georgian ✓ / 4-block ✓ / result-over-bureaucracy ✓ / no-fabrication ✓ / probe-discipline ✓ / enforcement-protocol-apr27 ✓ / geo-to-viktor-counter-audit ✓]
