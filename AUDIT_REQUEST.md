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

---

## Viktor Verdict v5

**Date:** 2026-04-29
**Re:** Option B (Termly free) pre-execute audit
**Audit:** GO REDUCED | Impact 6 | Evidence 5 | Readiness 7 | Risk: low

### Core Judgment
APPROVE Option B with conditions. Empirical n=2 cheaper than theme-dev escalation. Single-source theme-block hypothesis needs second data point before expensive root-cause path. Termly = $0, reversible, 4-step protocol holds. Success → 4 goals solved. Failure → confirmed theme block, escalate FastCloud + theme dev with 2-plugin evidence (stronger ask than n=1).

### What is weak
- Termly multi-lang KA support = 80% Geo-stated, NOT verified on docs.termly.io
- "30 წთ" estimate Geo-stated, not empirical
- "Partial compliance" claim vague, needs criterion
- No fallback timebox in Geo proposal → drift risk

### Stance per challenge point

1. **Theme conflict same risk** — YES likely. Frame Termly as DIAGNOSTIC test (isolate plugin-vs-theme), not solution attempt. Reframe expectations.
2. **Sample n=1** — n→2 justified. Theme-dev escalation needs evidence; second plugin failure = that evidence.
3. **Scope drift** — NO. Apr 26 directive named tool, not method. Goals preserved. Legitimate adaptation post-empirical failure.
4. **Multi-lang priority** — REMAINS. Owner Apr 27 reaffirm = current truth. No deferral without owner re-call.
5. **Option E (CookieYes manual)** — REJECT as primary. Solves Goal 1 only, Goals 2-3-4 unaddressed. Reserve as fallback if B fails AND theme-dev blocked.
6. **Theme-dev FIRST** — NO. 45-min empirical < unknown-hr theme-dev investigation. Post-B-fail (if), escalate with 2-plugin failure log = stronger evidence package.

### What must change before execute
1. **Pre-flight verify** — docs.termly.io multi-lang KA support (10 min). If docs unclear/no KA → DEFER, do not guess.
2. **Hard timebox: 45 min** (10 verify + 30 install + 5 wire-verify). No extension.
3. **Stop condition** — if Termly JS fails to inject same pattern as Complianz → STOP, no Plugin #3.
4. **Post-fail action pre-defined** — escalate FastCloud ticket + theme dev ask with both failure logs attached.

### Better version
Option B-prime: pre-flight docs verify + hard timebox + pre-defined fail action + reframe as diagnostic n=2.

### Execution readiness
**Ready with conditions** — pre-flight gate must pass before install.

### Confidence / evidence gap
- Theme-block hypothesis: high after Complianz failure, but n=1 (need n=2)
- Termly multi-lang KA: UNVERIFIED [EP1: HYPOTHESIS]
- Owner cost of further delay: unknown, assumed acceptable for 45-min boxed test
- Termly auto-scanner parity: 85% Geo-stated, unverified

### Self-audit
- Reject reason = weak (n=1 + unverified KA), not unfamiliar ✓
- Risk real (plugin churn drift, theme-block recurrence) ✓
- Better version offered (B-prime) ✓
- Not blocking unnecessarily — Go reduced, not Hold ✓
- Confidence proportional — Evidence 5/10 reflects unverified Termly claims ✓

### Path (CEO directive, paste-ready)

Geo, შენი Option B approved with conditions. Execute:
1. Pre-flight: docs.termly.io გადაამოწმე KA multi-lang support (10 წთ). თუ unclear → DEFER, არ გამოიცნო.
2. Hard timebox: 45 წთ მთლიანობაში. გადაცილება ბანი.
3. Termly JS injection ფეილი (Complianz pattern) → STOP, plugin #3 ბანი.
4. Fail-case: FastCloud + theme dev escalation ticket draft მზადდება Complianz + Termly logs-ით.

Sample n=2 = კონფირმაცია, არა plugin churn.
