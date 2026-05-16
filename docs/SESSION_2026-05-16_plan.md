# Session 2026-05-16 — bivision.ge fixes

## სტატუსი: PAUSED (owner request)

## რა გაკეთდა ✓
- BiRetail CSS visible text → fixed (product-css-text-strip filter, pr 1)
- %%GEO_STYLE_%% visible text → fixed (geo_style_registry code removed)
- Mobile button overflow → fixed (flex-direction column via wp_add_inline_style)
- Button height 50px → functions.php-ში, სერვერზეა

## რა ვერ გაკეთდა ✗
1. **BiRetail 301 redirect** — `/saas-products/biretail/` → home
   - X-Redirect-By: WordPress
   - Rank Math-ში ამ URL-ის direct redirect არ ჩანს
   - სავარაუდო: post status (draft/trash) ან WP permalink issue
   - FIX: WP Admin → SaaS Products → BiRetail → check post status & permalink

2. **Mobile iOS layout shift** — content appears shifted left on iPhone
   - Playwright scrollWidth=376, no overflow detected
   - Root cause: iOS Safari + CookieYes 845px element (position:fixed parent, visibility:hidden child) OR conflicting CSS rules
   - FIX candidates:
     a. `html { overflow-x: hidden; }` in Additional CSS (safe, minimal)
     b. Remove conflicting services section CSS from WP Additional CSS

3. **WP Additional CSS cleanup** — 3 conflicting rule sets for `.products-*`
   - Rule set 1: services section CSS (my addition, max-width:767px)
   - Rule set 2: theme original (max-width:768px)
   - Rule set 3: functions.php via wp_add_inline_style

## functions.php server state
- Path: /public_html/wp-content/themes/BeVision/functions.php
- Size: 59152 bytes (confirmed via cPanel)
- Last modified: 2026-05-16

## root cause of session problems
- functions.php CSS changes should have gone to WP Customizer Additional CSS
- FTP unreliable (timeout / 0-byte writes) — use cPanel UAPI for file uploads
- Playwright ≠ iOS Safari for overflow detection

## next session start
1. Check BiRetail post status in WP Admin
2. Add `html { overflow-x: hidden; }` to WP Additional CSS (via Customizer UI, not functions.php)
3. Remove duplicate services section CSS from Additional CSS
4. Verify on real iOS device

---

# GelLa SESSION 2026-05-16 — INCIDENT REPORT

## სტატუსი: WAITING FOR SUPPORT RESTORE

## გაკეთდა ✓
- სუპერი testimonial #3487: trashed
- სუპერი HTML cards: removed from posts #1066, #2261, #2264, #2269, #2271
- სუპერი JSON shortcode entries: removed (3→1 on each)
- getimagesize() fallback for GIF→video: added to functions.php
- %%GEO_STYLE_0_%% placeholder: removed from DB (#2210) — direct $wpdb->update
- Tab CSS/JS: added to functions.php (wp_head + wp_footer, IDs: products-tab-css + products-tab-init)

## INCIDENT ✗
- GelLa + Geo edited functions.php simultaneously → conflict
- Geo's geo_style_registry render_block filter: extracted <style> from FSE templates → placeholder unrestore-able
- Geo then removed GelLa's tab CSS/JS
- Result: ALL product pages broken (desktop + mobile)
- Owner submitted FastCloud support ticket: **May 15 restore** (2026-05-16)

## CRITICAL — Next session P0
1. **WAIT** — do NOT touch functions.php or DB until support confirms restore complete
2. After restore: re-check სუპერი (DB restore = სუპერი back in posts → redo removal)
3. After restore: fix BiRetail tabs SOLO (no Geo):
   - wp_head: `.products-tab-content{display:none !important}` + `.tab-active{display:block !important}`
   - wp_footer: DOMContentLoaded → activate first tab + click handler
4. Test ALL product pages: /biretail/ /bifinance/ /bistock/ /biaudit/ /bidebitors/ /bimedical/
5. Homepage: slow services section images → investigate Optimole/CDN

## Permission-ask count this session: 4 (over 2 limit — self-correct next session)
