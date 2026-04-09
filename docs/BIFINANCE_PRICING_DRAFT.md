---
class: ACTIVE
from: mentari
to: owner — REVIEW + devs deploy
type: BiFinance pricing page draft
created: 2026-04-09
status: 48hr overdue per Victor. DONE NOW.
for: bivision.ge/saas-products/bifinance/ — pricing section
---

# BiFinance Pricing — Draft

## პრინციპი
- ფასი გამჭვირვალე = trust
- 3 tier = choice architecture
- CTA = demo, არა "იყიდე"
- ₾, არა $

## 3 Tier Structure

### STARTER — 500₾/თვე
- 1 კომპანია
- BiFinance Core dashboards
- 5 user
- Email support
- **CTA: "სცადეთ 14 დღე უფასოდ"**

### BUSINESS — 1,000₾/თვე ⭐ რეკომენდებული
- 1 კომპანია
- Full BiFinance + custom dashboards
- 15 user
- ERP integration (Fina, Oris, Balance, 1C)
- Priority support
- Quarterly Business Review
- **CTA: "მოითხოვეთ დემო"**

### ENTERPRISE — ინდივიდუალური
- მრავალი კომპანია/ფილიალი
- Full BiFinance + BiRetail/BiStock
- Unlimited users
- Custom integrations
- Dedicated account manager
- **CTA: "დაგვიკავშირდით"**

## ⚠️ SELF-CHECK
- ფასები ⚠️ INFERENCE — ოუნერმა უნდა დაადასტუროს
- HubSpot-ში $1,000 avg deal = ~1,000₾. ეს BUSINESS tier-ს ემთხვევა
- კონკურენტი Amadeo = 100₾ (IV კატეგორია). ჩვენი 500₾ starter = II-III კატეგორია
- "14 დღე უფასოდ" — ოუნერმა უნდა გადაწყვიტოს trial policy

## HTML (devs-ისთვის)

```html
<section class="pricing">
  <div class="tier">
    <h3>Starter</h3>
    <p class="price">500₾<span>/თვე</span></p>
    <ul>
      <li>1 კომპანია</li>
      <li>Core dashboards</li>
      <li>5 user</li>
      <li>Email support</li>
    </ul>
    <a href="#lead-popup" class="cta">სცადეთ 14 დღე უფასოდ</a>
  </div>
  <!-- BUSINESS + ENTERPRISE similar -->
</section>
```

---

*მენცარი | 2026-04-09 | ფასები = INFERENCE, ოუნერის validate სჭირდება*
