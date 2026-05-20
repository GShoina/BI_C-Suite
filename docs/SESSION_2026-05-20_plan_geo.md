# SESSION 2026-05-20 — Geo (bivision.ge analytics + audit)

## რა გაკეთდა

1. **Audit v4** — `outputs/2026-05-20 bivision.ge Audit v4 by Geo.html` (score 68→72/100)
   - v3 open items updated: OG ✅, GA4 double-fire ✅, bifinance-2 301 ✅, Schema ✅, B-03 H1 ✅
   - New findings: B-01 BiRetail tabs P0, B-02 old pixel P2, B-04 hreflang P2, B-05 H1 keyword P2

2. **GA4+GSC Analysis v2** — `outputs/2026-05-20 bivision.ge GA4 + GSC Analysis by Geo.html`
   - Live Playwright data pull + GA4 API (bivision-ga4-sa.json)
   - Spam-filtered: pashagaming 282 imp excluded → 337 clean impressions, 3.86% CTR, pos 9.7
   - Double-fire quantified: May 14-18 = 2.4× ratio → ~12% inflation → real ≈360 sessions
   - 10-day section added (May 10-20 via API)
   - GelLa critique applied: GA4 Key Events P1→P0, FB LP = HYPOTHESIS, BiRetail alt = hack remnant hypothesis
   - SEO spam hack alert moved to bottom (owner preference)

## სად გაჩერდა

/clear-ზე. ყველა deliverable disk-ზეა.

## მომდევნო session-ისთვის (priority order)

### P0 — Owner actions (blocking)
1. **Wordfence full scan** — backdoor source unknown. hack re-injection risk. TODAY.
2. **GA4 Key Events** — GA4 Admin → Events → phone_call/whatsapp_click/contact_form_submit → Key Events. 5 min.

### P0 — Geo lane (needs "შეიტანე")
3. **BiRetail tabs fix** — mu-plugin: `.products-tab-content` sequential IDs + click handler. ~30min.

### P1 — monitoring
4. **fb/paid LAL audience** — May 19 change → monitor May 22+ engagement rate. If still <35% → dedicated /demo LP.
5. **GSC Removals** — 411 spam URL batch request (Owner/Geo).

### P2 — Geo lane
6. B-02: old Meta pixel 495329725412052 in BeVision theme wp_head — remove
7. B-04: hreflang ka + x-default (Rank Math Sitemap)
8. B-05: H1 keyword gap

### Open owner question
- April baseline comparison (Apr 1-30 vs May 1-20) — owner said "საინტერესო" — Geo can pull via API if requested.
