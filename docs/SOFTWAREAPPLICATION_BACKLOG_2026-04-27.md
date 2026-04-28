---
from: geo
to: owner
type: SEO schema backlog
created: 2026-04-27
priority: P3 — gated on testimonial data
---

# SoftwareApplication Schema Deploy — Backlog

## Status

**SKIPPED Apr 27 per risk-gate.** Bivision-ს არ აქვს რეალური testimonial data → SoftwareApplication template-ის სავალდებულო `aggregateRating` ველის შევსება შეუძლებელია სიცრუის გარეშე.

## Risk-gate logic (Apr 25 protocol)

`feedback_bivision_site_dev_only_execution.md` — risk-uncertain tasks SKIPPED. SoftwareApplication aggregateRating gap = Google rich-result invalid → marginal value over current valid Service schema. Risk მაღალი (Service schema override / დუპლიკატი / form validation block / fake rating fabrication), value მცირე.

## Why SoftwareApplication wanted

- AI-bot structured data signal გაძლიერება (BiFinance/BiRetail/BiStock/BiDebitors/BiAudit/BiHR = 6 SaaS pages)
- Google rich result eligibility (price + applicationCategory + rating)
- Schema.org SoftwareApplication > Service for SaaS-specific signals

## Re-eval triggers

1. **Real testimonial data collected** — min 5 ratings per SaaS product, owner-verified
2. **Owner-decide proceed without rating** — accept invalid rich result, ship for AI-bot signal only
3. **Theme dev confirms no Service schema conflict** — display conditions safely scoped to bevision_product CPT

## What's live now

- Service schema (Rank Math default) — valid JSON-LD ✓
- Organization schema sameAs Facebook + LinkedIn (Apr 27 fix) ✓
- BreadcrumbList schema ✓ (11 valid items per GSC)

## Next step

Defer until testimonial collection process exists OR owner directive proceed without rating.

Memory rules applied: [EP0 ✓ / readable-Georgian ✓ / no-fabrication ✓ / risk-gate Apr 25 ✓ / result-over-bureaucracy ✓]
