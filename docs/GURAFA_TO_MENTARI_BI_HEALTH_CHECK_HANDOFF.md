---
from: Gurafa
to: Mentari
type: asset handoff — owner-approved activation
created: 2026-04-23
asset: BI Health Check lead-magnet (Apr 20 Gurafa, owner-rediscovered Apr 23, OWNER APPROVED)
status: ownership transfer — activation + iteration now Mentari
hosted-url: https://gshoina.github.io/bivision-shares/bi-health-check.html
source-files: outputs/2026-04-20 BI Health Check by Gurafa.html + outputs/2026-04-21 BI Health Check Deployment Plan by Gurafa.html
---

# BI Health Check — Gurafa → Mentari Handoff

## Owner signal (Apr 23)

"ძალიან მაგარი იდეა. გამოყენება ბევრი მიმართულებით: email კამპანია, საიტზე CTA, LinkedIn."

Approve + scale. Activation blocker: 2 unknowns.

## Open gaps — Mentari scope

### Gap 1 — Email capture destination
Lead gate ამოიღებს email-ს, **სად ინახება ?**
- HubSpot form API? (Mentari-ს HubSpot connector awaiting setup per AI_IDEAS_TRACKER 1.1)
- Mailchimp audience? (bounce-rate 11.1% cleanup saqarho, separate concern)
- Google Sheet interim? (quick, no automation)
- Bivision DB table? (custom, needs Dato)

**Decision:** Mentari pick + wire. Recommend interim Google Sheet → HubSpot after connector setup.

### Gap 2 — Question revision
Owner flagged: "**კითხვებსაც შეცვლიდი**". 12 Qs current draft, need refinement.
- ICP-fit (SME 1M-70M₾ CFO) re-validate
- Georgian accounting vocabulary naturalness
- Score logic (12 → 3 recommendations) accuracy
- Owner preference: რას ჯობია დაემატოს / ამოირიცხოს?

**Action:** Mentari redraft v2 with owner 5-min review before publish.

## Distribution channels (owner-stated)

1. **Email კამპანია** — Mailchimp send + CTA button → URL
2. **Site CTA** — bivision.ge hero button "იცოდე შენი BI score" → URL
3. **LinkedIn** — personal + business posts, soft-CTA + DM trigger
4. **FB ad creative** (if budget authorized) — 15-წმ teaser → landing

## Asset state

- HTML live: https://gshoina.github.io/bivision-shares/bi-health-check.html
- Deployment plan draft: `outputs/2026-04-21 BI Health Check Deployment Plan by Gurafa.html` (Apr 21, stale — Mentari review + activate)

## Ownership

- **Gurafa** done: ideation + HTML + hosting
- **Mentari** now owns: email pipe, question v2, channel activation, CTA integration
- **Owner** review: Q v2 + channel CTA copy before go-live

## Validation Master Prompt gate

Even on approved asset — before scale, 3-slot check:
- **Build:** HTML + hosted ✅ / pipe TBD
- **Measure:** baseline conversion = 0 (never deployed). Target gate: ≥5% quiz-start rate per visitor, ≥40% completion, ≥30% email gate conversion — Mentari set on deploy
- **Learn:** pass → scale channels. Fail → Qs revision or gate friction reduce

## Deadline
No fake date. Token-limit only per owner directive.

## Change log
- 2026-04-23 created, owner approval signal + 2 gap scope + ownership transfer
