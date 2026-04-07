---
class: ACTIVE
owner: CEO
created: 2026-04-07
for: გაბო/დათო — implementation spec
priority: 🔴 URGENT — 0% demo conversion-ის #1 მიზეზი
---

# BiFinance Demo Funnel — Fix Spec

## სიტუაცია
BiFinance გვერდზე 59 user/თვეში მოდის, 0 demo request. Funnel 5 ადგილას გატეხილია.

## 🔴 P1 — დაუყოვნებლივ (1-2 დღე)

### 1. Crisp chat — გამორთე ან გააცოცხლე
- **ახლა:** dead 5+ თვე, "Last active 10/25/2025". Mobile-ზე ეკრანს ფარავს.
- **Fix:** გამორთე plugin (2 წუთი). თუ გვინდა chat — HubSpot free chat-ით ჩაანაცვლე (CRM-ში ჩავარდება).
- **ვინ:** გაბო

### 2. In-page CTA buttons — გაასწორე
- **ახლა:** "მოითხოვე დემო" buttons (#lead-popup) არ მუშაობს. მხოლოდ header button-ი ხსნის ფორმას.
- **Fix:** #lead-popup anchor-ის JavaScript trigger შეამოწმე. ან ყველა CTA-ს მიეცი header button-ის onclick.
- **ვინ:** გაბო/დათო

### 3. ბოლო CTA — WhatsApp → ფორმა
- **ახლა:** "დაგვიკავშირდი" = wa.me/593255385. 0 tracking.
- **Fix:** WhatsApp link → #lead-popup (იგივე demo form). ან Calendly link.
- **ვინ:** გაბო (WordPress edit)

## 🟡 P2 — ამ კვირაში (3-5 დღე)

### 4. Lead form → HubSpot
- **ახლა:** WordPress popup form, GET method. ლიდები სად მიდის? ❓
- **Fix:** HubSpot free form embed. ლიდი → HubSpot pipeline → notification → გელა.
- **ვინ:** გაბო (HubSpot account უკვე არსებობს)

### 5. Calendly integration
- **ახლა:** არ არის. ვიზიტორი ვერ ჯავშნის demo-ს.
- **Fix:** Calendly free account → გელას calendar-თან sync → link in form confirmation + thank you page.
- **ვინ:** გელა (Calendly setup) + გაბო (embed)

## 🟢 P3 — შემდეგი კვირა

### 6. Thank you page + tracking
- Form submission → thank you page (GA4 event = "demo_request"). ახლა 0 tracking.

### 7. Site speed
- 2.26s / 97.5MB BiFinance page. Image compression + caching.

## არ შეეხოთ
- **Copy/value proposition — კარგია.** 7 testimonial, ERP connectors, clear messaging. ნუ შეცვლით.
- **Design — OK.** ფუნქციონალი გატეხილია, არა ვიზუალი.

## მოსალოდნელი შედეგი
59 user/თვე × 5% conversion (industry avg) = **3 demo request/თვე.** ახლა = 0.
P1 fix = 0₾. P2 = 0₾ (free tools). დრო = 4-8 საათი total.

---

*მენცარი | 2026-04-07 | O2: პირველი real intervention. 0₾ cost, 4-8 საათი work.*
