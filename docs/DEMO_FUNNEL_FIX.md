---
class: ACTIVE
owner: CEO
created: 2026-04-07
for: საიტის დეველოპერები — implementation spec
priority: 🔴 URGENT — 0% demo conversion-ის #1 მიზეზი
verified: Playwright audit 2026-04-07, bivision.ge/saas-products/bifinance/
---

# BiFinance Demo Funnel — Fix Spec (დეველოპერებისთვის)

## სიტუაცია
BiFinance გვერდზე 59 user/თვეში მოდის (GA4), 0 demo request. Funnel გატეხილია.

## გადამოწმებული ფაქტები (Playwright, 2026-04-07)

| # | პრობლემა | გადამოწმება | მტკიცებულება |
|---|---------|-----------|-------------|
| 1 | **Page load = 7.2 წამი** | ✅ Playwright `performance.navigation` | loadEventEnd: 7203ms |
| 2 | **Page size = 1,486 KB (1.5MB HTML alone)** + 97.4MB total resources | ✅ Playwright + WP Debug Bar | docSize: 1486KB, Debug: 97.4MB / 124 queries |
| 3 | **Crisp chat = dead 5+ თვე**, mobile-ზე ეკრანს ფარავს | ✅ Playwright: crisp element present, "Last active 10/25/2025" |  |
| 4 | **ბოლო CTA "დაგვიკავშირდი" = WhatsApp** (wa.me/593255385) | ✅ Playwright: `a[href*="wa.me"]` found, text = "დაგვიკავშირდი" | 0 tracking, 0 CRM |
| 5 | **3 in-page "მოითხოვე დემო" link** (#lead-popup) — visible | ✅ Playwright: 3 links, all `visible: true` | anchor-based popup trigger |
| 6 | **Header "მოითხოვე დემო" button — მუშაობს** | ✅ Playwright click → popup opens | screenshot: bifinance-header-demo-click.jpeg |
| 7 | **Lead form = WordPress popup, `form` element NOT found in DOM** | ✅ Playwright: `querySelector('#bevision-new-popup form')` = null | ❓ ფორმის data სად მიდის? |
| 8 | **Calendly/scheduling = არ არის** | ✅ Playwright: 0 Calendly elements | |

## 🔴 P1 — დაუყოვნებლივ

### 1. Crisp chat — გამორთე
- **ფაქტი:** dead 5+ თვე. Mobile-ზე ეკრანს ფარავს, გვერდი unusable ხდება.
- **Fix:** Crisp plugin deactivate (WordPress → Plugins → Deactivate). 2 წუთი.
- **ალტერნატივა:** HubSpot free chat (CRM-ში ჩავარდება).

### 2. ბოლო CTA — WhatsApp → ფორმა
- **ფაქტი:** "დაგვიკავშირდი" href = `https://wa.me/593255385`. ვიზიტორი WhatsApp-ში ვარდება, 0 tracking, 0 CRM.
- **Fix:** href შეცვალე → `#lead-popup` (popup ფორმა). ან Calendly booking link.

### 3. Lead form audit
- **ფაქტი:** Playwright `form` element ვერ იპოვა popup-ში. Header button ხსნის popup-ს, მაგრამ form element = null.
- **კითხვა დეველოპერებისთვის:** ფორმის data სად მიდის? email? database? CRM? **თუ არსად → ეს არის 0 conversion-ის მთავარი მიზეზი.**

## 🟡 P2 — ამ კვირაში

### 4. Page speed — 7.2 წამი, 97.4MB
- **ფაქტი:** industry standard < 3 წამი. 7.2 წამი = 53% bounce rate increase (Google data).
- **Fix:** image compression, lazy loading, caching, unnecessary plugins audit.
- **124 DB queries per page load** (WP Debug Bar) — query optimization.

### 5. HubSpot form integration
- **ფაქტი:** HubSpot account არსებობს, მაგრამ ფორმა WordPress-ის custom popup-ია.
- **Fix:** HubSpot embedded form → ლიდი pipeline-ში + auto-notification.

### 6. Calendly
- **ფაქტი:** არ არის. ვიზიტორი ვერ ჯავშნის demo-ს.
- **Fix:** Calendly free → გელას calendar sync → thank you page-ზე link.

## არ შეეხოთ
- **Copy/value proposition — კარგია.** 7 testimonial, ERP connectors, clear messaging.
- **Design — OK.** ფუნქციონალი გატეხილია, არა ვიზუალი.

## მოსალოდნელი შედეგი
59 user/თვე × 5% conversion = **3 demo/თვე.** ახლა = 0.
Fix cost = 0₾. დრო = 4-8 საათი.

---

*მენცარი | 2026-04-07 | Playwright-ით verified. Screenshots available.*
