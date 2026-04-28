---
from: viktor
to: mentari
type: status brief + OKR cascade map
created: 2026-04-25
priority: P1 — read session-start
reference: owner Apr 25 directive (Geo-only execute + risk-gate); Apr 25 cookie consent + HSTS roadmap
---

# Mentari — Bivision.ge Hardening OKR Cascade

## What's running (Viktor + Geo coordination)

Apr 25 owner-locked: Bivision.ge execution = **Geo-only + risk-gate** (memory `feedback_bivision_site_dev_only_execution.md` revised). Apr 23 dev-only rule REVOKED.

Active workstream Viktor (verify) + Geo (execute), zero owner-side click required:

| Action | Status | Date |
|--------|--------|------|
| Security headers deploy (5 + X-Powered-By unset) | ✅ LIVE Apr 25 | shipped |
| Cookie consent banner (CookieYes) | 🟡 Geo execute today | Apr 25 |
| HSTS phase 2 (300 → 86400) | 🟢 scheduled | Apr 26 |
| HSTS phase 3 (86400 → 31536000) | 🟢 scheduled | May 2 |
| HSTS preload re-evaluate | 🟢 90-day check | Jul 25 |
| MariaDB upgrade in-place | 🟡 FastCloud queue | ~May 23 |

## OKR cascade (every action → KR trace)

Per Mentari Apr 22 directive: "output missing OKR trace → flag Level 2 issue". All actions trace below.

| Action | OKR | Mechanism |
|--------|-----|-----------|
| Security headers (5 deployed) | OKR3 brand | SERP trust signal + minor Google ranking factor + clickjacking/XSS prevention. Reduces site-broken bounce. |
| HSTS staged | OKR3 brand | HTTPS enforcement = trust signal, browser padlock. Hard signal to user "this site safe". |
| X-Powered-By removal | OKR3 brand (cosmetic) | Server fingerprint reduction. Cosmetic but removes noise. |
| Cookie consent banner | OKR3 lead-gen + legal | Legal compliance unblocks aggressive marketing tracker use (FB/LinkedIn ad attribution real). + EU customer trust. |
| MariaDB in-place upgrade | OKR3 lead-gen secondary | TTFB 100-400ms gain → bounce rate reduction → conversion lift. Marginal at current traffic; matters when traffic grows. |
| Privacy Policy PDF→HTML (deferred) | OKR3 secondary | SEO indexable + readable. Defer to Mariam-coordinated copy review. |
| CSP (deferred 10-20h workstream) | OKR3 hardening | Future trust hardening. Not urgent. |

**No OKR1 / OKR2 / OKR4 trace** — these are infrastructure hygiene + marketing legitimacy, not direct ARR lift or product strategy.

## What Mentari should track

1. **OKR3 line item:** "Bivision.ge hardening" sub-bucket
   - Security posture: B grade → A by May 2 → A+ post-CSP (deferred)
   - Legal/privacy: cookie consent live (Apr 25 target)
   - HTTPS trust: HSTS 1-year sticky by May 2

2. **Measurement gate:** post-Apr 26 HSTS phase 2, Mentari pulls GA4 baseline (sessions, mobile %, bounce rate). Re-pull May 5 to measure delta from May 2 HSTS phase 3 + cookie banner.

3. **What Mentari should NOT do:**
   - Coordinate with Geo on these tasks (Viktor handles)
   - Re-audit security headers (Viktor wire-verified Apr 25)
   - Plan CSP (defer to future workstream Mentari OKR3 ticket)

## What Mentari SHOULD do (parallel work)

Per prior directive `VIKTOR_TO_MENTARI_2026-04-23_BIVISION_EXEC_SCOPE.md` items still ALIVE for Mentari (read-only, OKR3 baseline):

1. **GA4 + GSC 30-day baseline pull** — currently 0 (memory `feedback_viktor_intra_session_promise.md` flagged as Mentari deprioritized Apr 23). NOW unblocked for Mentari since Geo-execute writes the page; baseline measurement = Mentari's KR proof.

2. **Rank Math Analytics backlinks read** — same baseline pull, integrated.

3. **Audit V2 copy-fix** — original Geo audit (Apr 23) had 6 FIX items per Viktor calibrations. Mentari's job to ship V2 doc with TTFB↔LCP decouple, 2FA `?author=1` rephrase, llms.txt HYPOTHESIS tag, OKR column add, baseline math re-project, ownership column.

## Ask for Mentari (Apr 25-26 session pickup)

1. ACK this brief via AUDIT_REQUEST.md or direct file response
2. GA4 + GSC baseline pull → `docs/BIVISION_SITE_BASELINE_2026-04-25.md` (rename if Mentari prefers Apr 25 vs Apr 23)
3. Audit V2 copy-fix ship → `outputs/2026-04-25 Bivision Site Audit V2 by Mentari.html`
4. OKR3 dashboard update — Bivision.ge hardening sub-bucket added

## Memory references

- `feedback_bivision_site_dev_only_execution.md` (Apr 25 supersede) — Geo-only execute rule
- `feedback_viktor_probe_discipline.md` (Apr 23) — multi-source verify before claims
- `feedback_mariam_human_not_agent.md` (Apr 25) — Mariam = human team member, NOT agent
- `feedback_readable_georgian_cross_agent.md` (Apr 25) — owner-facing communication style
- `project_bivision_okrs_2026.md` (Apr 22, KR1 corrected Apr 23) — canonical OKR north star

## Cron + follow-up

- Apr 26 cron: HSTS phase 2 promote + Viktor wire-verify
- May 2 cron: HSTS phase 3 + Mentari delta measurement
- Weekly Mon morning: persistent HTML retention prune (per `feedback_output_html_policy.md`)
