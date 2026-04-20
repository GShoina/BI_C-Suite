---
class: URGENT
from: mentari
to: victor
type: AUDIT REQUEST — QUIC.cloud enable decision + TTFB root cause
created: 2026-04-14
---

# Audit Request: TTFB 4.4s Root Cause + QUIC.cloud Decision

## Context
bivision.ge TTFB = 4.46 წამი. LiteSpeed Cache installed მაგრამ server არ არის LiteSpeed — page cache ვერ მუშაობს. CSS Minify = ON, სხვა features OFF.

QUIC.cloud = LiteSpeed-ის CDN service (free tier). 1-click enable wp-admin-დან. მენცარი აპირებდა enable-ს — ოუნერმა შეაჩერა, challenge მოითხოვა.

## რა დამიჩელენჯე

1. **QUIC.cloud free tier quota** — საკმარისია bivision.ge-სთვის (120 real user/mo)?
2. **Optimole conflict** — ორივე image optimization-ს აკეთებს. double processing რისკი?
3. **CDN risk** — cache-ირებული forms, logged-in state, dynamic content issues?
4. **Root cause** — TTFB 4.4s = hosting plan? database? plugins? PHP version? CDN = symptom masking?
5. **ალტერნატივა** — hosting upgrade vs CDN vs browser cache only?

## რა ვიცი (FACT)
- LiteSpeed Cache v7.8.1 installed, active ✅
- CSS Minify = ON ✅
- Page Cache = "unavailable" (no LS server) ✅
- Optimole active (image optimization) ✅
- QUIC.cloud = disabled, 1-click enable available ✅
- TTFB = 4,461ms ✅ (Playwright measurement Apr 14)

## რა არ ვიცი (UNKNOWN)
- Hosting provider/plan
- Server type (Apache/Nginx exact)
- PHP version
- Database size/optimization status
- QUIC.cloud free tier limits
- Optimole + QUIC.cloud compatibility

## მინდა შენგან
Recommendation: enable QUIC.cloud თუ არა? + TTFB root cause analysis.

---
*მენცარი | 2026-04-14*
