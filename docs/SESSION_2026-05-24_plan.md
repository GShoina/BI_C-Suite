# Session 2026-05-24 — Plan & State

## დღეს გაკეთდა (DONE)

| # | Task | Result |
|---|---|---|
| 1 | BiFinance_Phase1_v2 campaign launch | DONE — ID: 120246759167590598, $20 lifetime, ends Jun 1 |
| 2 | ძველი campaigns პაუზა | DONE — 120246426703320598 + others paused |
| 3 | AdSet checklist verify | DONE — LAL only, Advantage+ OFF, pixel correct |
| 4 | GSC sitemap resubmit | DONE — all pages indexing requested via Playwright |
| 5 | Lead Gen Form v3 შექმნა | DONE — BiFinance_Demo_v3_Calendly (ID: 1495634402063502), 3 fields + Calendly |
| 6 | Form apply to ad | DONE — Playwright in Ads Manager, published successfully |

## სად გაჩერდა

Form `1495634402063502` applied to ad `120246759350130598`. API-ით დადასტურდა:
`call_to_action.value.lead_gen_form_id = "1495634402063502"` ✓

## Open Items → გადადის SESSION_OPEN_ITEMS.md

1. **[P0] 2026-05-27 checkpoint** — CTR/impressions/leads review for Phase1 v2
2. **[P1] Meta app dev mode → Live** — Meta Developer Console → App Settings → Live mode (1-3 day review). Blocks API creative creation.
3. **[P1] GA4↔Meta analytics gap** — Lead Gen Form = users stay on Facebook → no GA4 events. Fix: switch CTA to website URL + UTM after app goes Live, OR accept FB-only metrics for now.
4. **[P2] bihub.ge migration** — `~/.claude/scripts/bihub_migration.ps1` still pending
5. **[P2] Search Console API enable** — project 690459787742 → enable `searchconsole.googleapis.com`

## Key Facts (don't re-derive)

- Meta app ID: 1506392834274245 — **DEVELOPMENT MODE** (blocks new adcreative via API)
- Playwright workaround for Ads Manager checkboxes: `dispatchEvent(mousedown+mouseup+click)` — `.click()` alone doesn't work
- Form old: 990562330546376 (5 fields, 0/10 completions) → replaced
- Form new: 1495634402063502 (3 fields: name+phone+email, follow_up → Calendly)
- AdSet targeting: LAL_1pct_GE_PixelSeed (120245324443150598) only — no HubSpot seed cross-contamination

## Next Session Start

1. Check Phase1 v2 performance (if ≥72h since May 24)
2. Decision: keep Lead Gen Form OR switch to website CTA for GA4 tracking
3. If Meta app still dev mode: use Playwright for any creative changes

---

## GEO SESSION APPEND — 2026-05-22/24 (bivision.ge SEO deep-dive)

### Deliverables shipped

| File | Status |
|---|---|
| `outputs/2026-05-22 Geo Dashboard by Geo.html` (133KB, srcdoc 3-tab) | ✅ |
| `outputs/2026-05-22 bivision.ge GA4 + GSC Analysis by Geo.html` (May 22 banner) | ✅ |
| `outputs/2026-05-20 bivision.ge Audit v4 by Geo.html` (May 22 progress banner) | ✅ |
| `outputs/2026-05-22 bivision.ge SEO Brief by Geo.html` (14KB lean agent brief) | ✅ |

### Key insight

11m42s engagement + 0 non-branded = visibility broken, not quality. Content = P0 for SEO growth. Blue ocean: "BI dashboard GE" / "ფინანსური ანალიტიკა ERP" = 0 competitors.

### Open (Geo lane, next session)

- Verify TTFB fix applied (LiteSpeed Preload All — GelLa should do this, just check)
- bihub.ge V11: Viktor audit v3 P1 open: B-02 logo href, B-03 Terms/Privacy (owner-pending)
- Nikacho/Geo-Metri: no work done this session — backlog
