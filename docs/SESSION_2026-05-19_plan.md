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

---

# GelLa SESSION 2026-05-19 — bivision.ge Audit Fixes

## გაკეთდა — GelLa continuation (post-compaction)

7. ✅ Meta targeting fix — AdSet_A + AdSet_B: job titles ამოღებული (work_positions=0 verified), LAL audiences დამატებული
   - AdSet_A: Construction LAL (120246077003560598) + HubSpot LAL (120245324868600598)
   - AdSet_B: HubSpot LAL + Pixel 90d LAL (120245324443150598)
   - Reason: GE job title pool ~3-8K → CPM spike; LAL = ICP signal from real data

8. ✅ Construction Follow-up Email 1 — `outputs/2026-05-19 Construction Follow-up Email 1 by GelLa.html`
   - Universal version (not segmented)
   - Subject: "ერთი კითხვა — BiFinance Health Check-ის შემდეგ"
   - CTA: Calendly 15 წთ

9. ✅ WP→HubSpot auto-sync mu-plugin: `bivision-lead-hubspot.php` deployed server-side
   - Hooks `save_post_lead`, pushes contact to HubSpot CRM on new submission

10. ✅ B-05 Organization schema duplicate: bivision-org-patch.php fixed (rank_math/json_ld filter, schemas 2→1)

---

## გაკეთდა — ადრე ამ სესიაში

1. ✅ Meta Pixel ID fixed — GTM V14: `495329725412052` → `24993373220352719`
   - Tag "Meta Pixel – Base" (tag ID 19): fbq('init') + noscript src — ორივე გასწორდა
   - CodeMirror setValue() + Space+Backspace Angular dirty-state trick
   - Published as GTM Version 14
   - Graph API confirmed `24993373220352719` = real pixel ID; `495329725412052` = ad account ID (wrong)

2. ✅ GA4 2× fire fixed
   - Site Kit → "Place Google Analytics code" = OFF (Snippet is not inserted)
   - GTM = sole GA4 source. 1× page_view confirmed in network.
   - LiteSpeed cache purged.

3. ✅ /saas-products/bifinance-2/ redirect — 301 live
   - Rank Math Redirections → 301 Permanent Move → /saas-products/bifinance/
   - Verified: `{"status":301,"location":"https://bivision.ge/saas-products/bifinance/"}`

4. ✅ B-04 OG image 1200×630
   - PNG created: PIL + Sylfaen (Georgian) + brand colors (#1e1b4b bg, #6B63B5 bar, #00A651 accent)
   - Uploaded: WP Media ID 3883 — `wp-content/uploads/2026/05/bivision-og-1200x630-1.png`
   - Set in Rank Math Social tab on homepage (page ID 432). Page saved.
   - Verified: og:image:width=1200 live. Optimole CDN: w:1200/h:630/q:mauto/f:best

5. ✅ B-03 Empty H1 hidden
   - mu-plugin bivision-fixes.php: `wp_add_inline_style` → `.analytics-hero__main-title{display:none!important}`
   - Verified: visible=false live

6. ✅ B-05 Organization schema duplicate fixed
   - Source: mu-plugin bivision-org-patch.php outputting standalone Organization script
   - Fix: replaced wp_head echo with `rank_math/json_ld` filter — injects foundingDate/areaServed/numberOfEmployees INTO Rank Math's @graph Organization node
   - Result: schemas 2 → 1; @graph Organization has foundingDate:2015, areaServed:Georgia, numberOfEmployees:7 ✅

## სად გაჩერდა

Meta targeting fix ✅ done (session continuation after compaction).

## ვერ გასწორდა / Deferred

| Issue | სიტუაცია |
|---|---|
| Old pixel 495329725412052 in theme | BeVision theme inline script. ob_start approach broke Rank Math — deferred. Low priority (pixel fires but silently dropped by FB). |
| N-01 wp-json/users call | Did NOT reproduce on public frontend (admin-only?) |

## შემდეგ სესიაში — GelLa

**P0 (Email campaigns):**
- Energy email → Mailchimp: "BiFinance — ენერგეტიკა — 2026-05-18", paste v1 HTML
  `outputs/2026-05-18 BiFinance Energy Email v1 by GelLa.html`
- BiMedical #17993958: fix BiAudit URL bug + assign audience before send
- Construction follow-up send: 52 openers → Mailchimp bulk, clickers → personal from info@bivision.ge
  File ready: `outputs/2026-05-19 Construction Follow-up Email 1 by GelLa.html`

**P1 (Meta):**
- BiFinance kill check May 21 (72h): CTR <0.3% at $5 → pause
- Verify LAL audience delivery started (check spend after 24-48h)

**P1 (WP):**
- Verify bivision-lead-hubspot.php on next real form submission (check error_log)

**P2 (SEO):**
- hreflang ka + x-default (Rank Math Sitemap)
- H1 keyword gap
- wp-json restrict (.htaccess)
- LiteSpeed Compress HTML = ON (1-click WP Admin)

## permission_asks GelLa session: 0
