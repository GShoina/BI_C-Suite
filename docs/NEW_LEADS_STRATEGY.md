---
class: ACTIVE
from: mentari
to: owner
type: STRATEGY — new leads focus
created: 2026-04-08
owner-directive: "არსებულებზე ნაკლები რესურსი, მთავარი აქცენტი ახალი ლიდები, LinkedIn, email კამპანია, გრძელვადიანი = ტექნოლოგიები"
canonical-status: mixed — Email + long-term tech sections CANONICAL; LinkedIn section SUPERSEDED 2026-04-15 by docs/LINKEDIN_BATTLE_PLAN.md
---

# ახალი ლიდების სტრატეგია

## 3 არხი — პრიორიტეტით

### 1. LinkedIn (842 followers, +200% ზრდა ბოლო კვირაში)

**რა გვაქვს:**
- Company page: Bivision Ltd, 842 followers
- Last 7 days: 3 new followers, 545 impressions
- Page visitor: 1 (ძალიან დაბალი)
- Boost available: "60K impressions" suggestion

**რა უნდა გაკეთდეს:**
- გელას personal LinkedIn = #1 არხი (personal > company page)
- კვირაში 2-3 post: case study + insight + CTA
- Content: "როგორ გადაჭრა [კომპანიამ] [პრობლემა] BI-ით" ფორმატი
- გელას connections target: CFO/Finance directors ქართულ კომპანიებში
- LinkedIn outreach: Dripify/Expandi ($59/mo) + Claude API personalization
- Sales Navigator: target list II-III კატეგორიის კომპანიები

**ტექნოლოგია (გრძელვადიანი):**
- Apify + Claude: target company scraping → personalized message → LinkedIn outreach pipeline
- AI avatar (HeyGen): ვიდეო content LinkedIn-ისთვის

### 2. Email კამპანია (Mailchimp active, HubSpot contacts)

**რა გვაქვს:**
- Mailchimp account (active)
- HubSpot contacts: 15+ (ახლად დარეგისტრირებული)
- Click rate: 0.37% (industry avg 2.5%)
- 0 active campaigns

**რა უნდა გაკეთდეს:**
- Welcome sequence: 3 email (intro → value → demo CTA)
- Monthly newsletter: BI insights + case study
- HubSpot → Mailchimp sync (contacts auto-flow)
- Segmentation: Financial, HoReCa, Construction, Medical

**ტექნოლოგია:**
- Claude API: personalized email generation per segment
- Auto-trigger: HubSpot deal stage change → email sequence

### 3. Demo Funnel Fix (59 users/month → 0 conversion)

**რა გვაქვს:**
- Fix spec ready (Playwright verified)
- Copy კარგია, funnel გატეხილია
- 59 BiFinance page visitors/month

**რა უნდა გაკეთდეს:**
- Spec devs-ს გადაცემა (blocker: ვის?)
- Crisp → HubSpot chat swap
- WhatsApp CTA → form CTA
- Calendly integration
- Target: 59 × 5% = 3 demo/month

## Pipeline First იერარქია (updated)

```
1. ცოცხალი ფული = existing deals autopilot (Gemini follow-up)
2. ახალი ლიდები = LinkedIn + Email + Demo funnel (მთავარი ფოკუსი)
3. გრძელვადიანი = AI automation pipeline (Apify, Claude, HeyGen)
```

## ვინ რას აკეთებს

| არხი | ვინ | როდის |
|------|-----|-------|
| LinkedIn content | გელა (posts) + მენცარი (drafts, research) | ამ კვირიდან |
| LinkedIn outreach tool | მენცარი (setup Dripify/Apify) | ოუნერის approve |
| Email campaign | მენცარი (setup) + მარიამი (content) | ამ კვირაში |
| Demo funnel | devs (deploy) | spec ready, ვის? |
| AI pipeline | მენცარი + გაბო | Apr 10 SWOT-ის შემდეგ |

---

*მენცარი | 2026-04-08 | ოუნერის დირექტივა: ახალი ლიდები = #1*
