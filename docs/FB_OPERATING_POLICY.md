---
from: mentari
to: owner
type: ⚠️ REC — Facebook Paid Operating Policy
ep0: 9/10 (O)
tier: spot-check
status: awaiting owner approval
created: 2026-04-15
audit: docs/AUDIT_REQUEST.md (filed 2026-04-15, Viktor post-factum)
evidence-source: docs/MARIAM_CAMPAIGN_ANALYSIS.md (FB diagnosis Apr 9 — text reach, Reel performance, engagement rates), docs/MARKETING_PARETO_AUDIT.md (winners/losers ranking)
---

# Facebook Paid — Operating Policy (draft for owner approval)

## Thresholds — with source and category

| Threshold | Category | Source / Logic |
|---|---|---|
| Text post boost = ban | Historical learning (permanent) | ✅ FACT (Playwright Apr 10-14): 5 text boosts, reach 29-66, CPC avg 40₾+. Boost ვერ ცვლის format quality-ს. |
| CPC > 50₾ → same-day pause | Temporary operating rule | ⚠️ INFERENCE (M): ენერგეტიკის 128₾/click outlier. Need 4-week data to calibrate. Revisit 2026-04-30. |
| Interaction rate < 0.3% at 24h → pause + review | Temporary operating rule | Georgian B2B FB benchmark ❓ UNKNOWN. 0.3% = conservative floor. Revisit after 3 campaigns. |
| Spend ≥50₾ with 0 clicks → pause | Historical learning (permanent) | ✅ FACT: 3 Apr campaigns hit this pattern — all creative/audience mismatch. |
| Bounce > 70% from ad traffic → pause | Historical learning (permanent) | ✅ FACT GA4 Apr 8-14: organic bounce 52%, ad-traffic 74-81%. Landing mismatch. |
| Interest-only targeting = ban | Historical learning (permanent) | ✅ FACT: ენერგეტიკა campaign = interest-only = 128₾/click. |

## Lead objective — exact measurement

FB-ის native "leads" column არ ვიყენებ (misattribution risk). ნაცვლად:

- **Primary metric:** HubSpot deal with `source = Facebook` (UTM-tagged link → form → HubSpot). Countable, attributable.
- **Secondary metric:** GA4 `form_submit` event with `source=facebook`, `medium=paid`.
- **Tertiary (soft):** Messenger DM within 48h of ad view — manual tag in HubSpot by Mariam.
- **NOT a metric:** FB Ads Manager native "leads" count. Reach. Impressions. Engagement (except Reel organic amplification test).

**Success threshold (LOCKED 2026-04-20, revised):** cost per HubSpot-attributed deal < **1,200₾**.

Derivation (owner-validated 2026-04-20):
- LTV baseline = 800₾/თვე × 15 თვე pilot+mandatory contract = 12,000₾ minimum first-contract
- 2-year retention LTV = 19,200₾
- CAC realistic (2 pilot concurrent + existing client load): Inga 15% + Developer 25% × pilot 3 თვე ≈ **8,000₾** internal labor per new pilot
- First-contract margin = 12,000 – 8,000 = 4,000₾
- FB ad threshold = margin / 3 = ~1,300₾ → conservative lock **1,200₾/deal**
- Alt scenarios: 2-year margin 11,200₾ → 3,700₾/deal max; 3-year margin 20,800₾ → 6,900₾/deal max. Start conservative (1,200), widen with retention + deal data.
- Recalibrate after 3 campaigns.

## Audience logic

**Keep:**
- Custom audience from 29 existing clients (lookalike)
- Balance email list contacts
- Website visitors (GA4 retargeting)

**Kill:**
- Generic interest targeting ("ენერგეტიკული კომპანიები" type)
- Age/gender-only
- Broad demographic without behavioral signal

## Red lines

- არასდროს boost text-only post
- არასდროს spend > 100₾/campaign without 24h performance check
- არასდროს ახალი audience ძველი creative-ით (ორივე ახალი ან არცერთი)

## Redirect rules

- არსებული boost budget → მხოლოდ Reel/Video format
- Reel organic 26K reach ✅ FACT → boost = amplification, not life support
- Partnership content (Balance-type) = boost #1 candidate

## Budget recommendation

⚠️ REC — 0₾ ახლა, სანამ Reel/Video content არ გამოჩნდება. პირველი Reel → 30₾ test boost → 24h check → continue ან stop.

## Owner decision needed

1. Approve threshold set as operating policy?
2. LTV assumption 5000₾ → confirms 500₾/deal target?
3. Who executes pause/kill actions in real time — Mariam with policy doc, or Mentari with Meta access?
