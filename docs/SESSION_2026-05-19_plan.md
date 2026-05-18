# SESSION 2026-05-19 — Geo agent / bihub-v8

## Completed today
- [x] bihub-v7 → v8 migration (docx spec applied)
- [x] Hero: H1 + Qlik pill kept; Text1 (social proof, 20px bold) + Text2 (sources, nowrap) added
- [x] CTA: "წვდომა უფასოდ →", "ბარათის მიბმის გარეშე" below
- [x] Footer: single row, Bivision logo restored (img from bivision.ge)
- [x] Notify strip: real HubSpot CRM write via PHP proxy on bihub.ge (mu-plugins deployed)
- [x] Copy: 3 global text replacements (რეგისტრაცია უფასოდ, წვდომა უფასოდ, footer tagline)
- [x] Lock flag consistency: 4 cards fixed (ავტოპარკი, ეროვნული გამოცდები, ენერგეტიკა, უცხოური ინვესტიციები)
- [x] v6/v7 deleted from repo
- [x] HubSpot portal ID confirmed: 147341634

## Stopped at
bihub-v8.html shipped at commit 4365e86. Owner reviewing.

## Next session — P1
1. **Mobile test** — hero-text1 `white-space:nowrap` on 375px may overflow; add `overflow-x:hidden` on hero OR switch to `font-size:clamp(0.85rem,3.5vw,1.25rem)` on mobile
2. **Production deploy** — if owner approves v8, upload to bihub.ge WP theme or replace static HTML
3. **UpdraftPlus** — backup schedule for bihub.ge server (P1 deferred from May 18)

## Files changed this session
- bivision-shares/bihub-v8.html (new canonical)
- bivision-shares/bihub-v6.html (deleted)
- bivision-shares/bihub-v7.html (deleted)
- bihub.ge server: C:\wamp\www\wp-content\mu-plugins\bihub-subscribe.php (new)

## Permission asks this session: 0
