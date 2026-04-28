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

**5-Stage Cascading Funnel Framework — owner-approved 2026-04-20, pending Viktor/Gurafa challenge before final lock.**

| Stage | Metric | Gate | Check at | On fail |
|---|---|---|---|---|
| 1. Traffic | CTR (click-through rate) | ≥ 0.5% | 1,000 impressions | pause creative/targeting |
| 2. Landing | bounce rate < 70%, time on page > 30s | (both) | 50 ad-sourced visits | fix page or ad |
| 3. Lead | CPL (cost per lead) | ≤ **50₾/lead** | 100 visits OR 7 days | pause, investigate |
| 4. SQL | CPD (cost per demo booked) | ≤ **150₾/demo** | 10 leads OR 14 days | review qualification |
| 5. Deal | CPA (cost per acquisition) | ≤ **650₾/deal** | 30-90 day cohort | sales process audit |

**Note on 650₾ CPA (owner-tightened from Mentari's proposed 1,200₾):** aggressive target, enforces LTV:CAC ≥ 18:1 on first contract. Evidence needed (3 deals minimum) before considering loosen.

**Total monthly digital budget = 300₾** covering ALL channels combined: Facebook ads + LinkedIn ads + Mailchimp email. Single budget pool — elastic upward only with proven unit economics.

**Daily cap = 10₾/day total** (300 ÷ 30) across all channels. Enforced at Meta Ads Manager + LinkedIn Ads + Mailchimp billing settings.

**Elastic budget logic:**
- 0 deals attributed → freeze at 300₾/mo max
- 1 deal with CPA ≤ 650₾ → 2× scale (600₾/mo)
- 3+ deals consistent → 10× scale OK (3,000₾+/mo if LTV:CAC holds)

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
