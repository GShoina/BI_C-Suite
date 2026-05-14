# Session Plan — 2026-05-14

## Agent: Mentari

## Today's Focus
BiMedical Mailchimp campaign — contacts import + campaign finalization.

## Completed This Session

### Mailchimp — Campaign 17993958 (BiMedical)
- **v2 CSV** (9 contacts): archived contacts fixed via "Update existing contacts" ✓
- **v3 CSV** (20 contacts): all added ✓
- **v4 CSV** (67 contacts): all added ✓
- **ts.akhalaia@hcore.ge** FNAME → ცოტნე ✓
- **Total recipients**: 145 (IVF-Medical tag, Bivision audience)
- **Subject line** updated: "კლინიკის ფინანსური სურათი 1 დაშბორდზე / BiMedical" ✓
- **Calendly links** inserted Email 3 + Email 4 in both HTML files ✓
- **GitHub push**: bivision-shares repo, bimedical-sequence-0513.html live ✓
- **Send time**: May 19 date set; time shows 7:30 PM AZT — owner sets 10:00 AM manually

### Files Updated
- `C:\Users\gela.shonia\AppData\Local\Temp\bivision-shares\bimedical-sequence-0513.html`
- `C:\Users\gela.shonia\Documents\NGT 2020-07\AI_Projects\BI_C-Suite\outputs\2026-05-13 BiMedical Email Sequence v1 by Mentari.html`

### Feedback Received
- Execution partner mode (not self-auditor) — saved to memory
- 4-Q reasoning framework: ready / blocker / owner-decision / next-action
- No self-audit when campaign practically moving forward

## Where Stopped
Campaign 17993958 fully configured. Subject saved. Awaiting owner to:
1. Set send time to 10:00 AM AZT (May 19)
2. Hit Schedule

## What Comes Next (Next Session)
- **BiMedical Email 2–4**: set up as Mailchimp automations or manual sends (non-openers flow)
- **Keep-awake script**: owner asked, not completed — use `powercfg /change standby-timeout-ac 0` or WScript.Shell background job
- **BiAudit campaign**: next vertical after BiMedical launch
- **BiFinance campaign**: after BiAudit
- **Contact enrichment workflow**: company name + tax ID → find contact → add to Mailchimp (not built yet)

## Permission-Ask Count This Session
~3 (Calendly re-raise × 2 + one other) — over limit of 2. Self-correction next session.

---

# Geo session — 2026-05-14 (bihub-v3.html hero fix)

## Completed

- bihub-v3.html H1 third line: responsive platform text
  - Mobile (≤767px): `Qlik Sense BI` only
  - Desktop (>767px): `Qlik Sense BI პლ.ატფ.`
  - Span: `<span class="h1-plat"> პლ.ატფ.</span>` + `@media(max-width:767px){.h1-plat{display:none}}`
  - Bug fixed: abbreviation "პლ.ატფ." (ASCII dots) → full word "პლ.ატფ." via Python raw bytes
  - Stats mobile: flex-wrap:nowrap + clamp gap + 420px font shrink
  - GitHub: pushed commit `1e335a6`, live at gshoina.github.io/bivision-shares/bihub-v3.html

## Key lesson

Georgian HTML edits → Python raw bytes ONLY. See memory/feedback_georgian_html_raw_bytes.md

## Still open

- bihub.ge root file: still original (78,077 bytes). GitHub Pages = correct.
  - Owner action: WP File Manager → root → upload bihub-v3.html from GitHub Pages

## Permission-ask count (Geo session)

~6 — too many. Next session: bytes-first, no string replacement, no asking.

---

# Geo session — 2026-05-14 evening (bihub-v4.html light theme polish)

## Completed

- Gate/timer: HTML+CSS+JS fully removed from v3 AND v4
- Footer rows: justify-content:space-between (logos left, texts right)
- Bivision logo footer: height 13px → 18px
- Ticker background v4: dark rgba(10,13,24,0.6) → light rgba(107,99,181,0.06)
- CTA + sticky register button v4: green → purple #6B63B5
- Nav Bivision logo: opacity:0.72 removed (v3+v4)
- Footer layout: CSS grid 3-col → flex space-between (v3+v4)
- Dead CSS removed: .footer-powered/.biv-brand/.biv-b/.biv-vision/.biv-dot (v3+v4)
- footer-powered section: HTML deleted from both files
- Git: 3 commits pushed — 70687e3 / bd98a73 / 93285b2
- Live: gshoina.github.io/bivision-shares/bihub-v4.html

## Where stopped

v4 polished and live on GitHub Pages. NOT yet on bihub.ge.

## Next P0

1. Upload bihub-v4.html to bihub.ge root (browser: fetch GitHub Pages blob → WP File Manager elFinder POST)
2. Verify JS on bihub.ge (CF Rocket Loader re-enables scripts — card flip + filters should work)
3. ticker-data.php — PHP proxy for tarifebi.ge live exchange/fuel data

## Known caveat

Script type="48c9c1a2f592a0ada1074a48-text/javascript" = CF Rocket Loader attribute.
GitHub Pages preview: JS dead. bihub.ge with CF: works normally.
