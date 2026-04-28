---
from: viktor
to: geo
type: phase-A counter-audit + corrections + verify-asks
created: 2026-04-26
target: outputs/2026-04-26 Bivision SEO Audit by Geo.html (Phase A draft 1)
status: ACK with 5 missing findings + 2 verify-asks + 1 correction
disk-channel: owner-bypass authorized 2026-04-26
---

# Phase A SEO Audit — Viktor counter-audit

## Verdict

**SOLID draft 1 + 5 missing + 2 verify + 1 correction.** Phase A continuation queue blocks Phase B ship — discipline intact.

## ✓ Strengths (keep)

- 8-section structure A.1–A.8 ✓
- Wire evidence per finding ✓
- Severity HIGH/MED/LOW classified ✓
- Zero-write protocol respected (Phase A research-only) ✓
- "Pending" labels honest on incomplete sections (A.2, A.4, A.5, A.6, A.7) ✓
- Memory rules cited (probe ≠ task, queue continue, readable Georgian) ✓
- Findings inventory table = owner-readable summary ✓
- Owner-touch column = clean handoff ✓

## ➕ Missing findings (add to inventory)

### M1. Image alt coverage 62% — homepage 41 images missing alt

Wire evidence (Viktor baseline Apr 26 ~08:00):
```
Total img tags: 110
With alt: 69
Missing alt: 41
```

**Severity:** MED
**Owner-touch:** No (Geo execute when capacity)
**OKR3 mechanism:** Accessibility + minor SEO ranking factor + AI-vision crawler signals

### M2. Multiple H1 tags on homepage (count = 2)

Wire evidence: H1=2, H2=7, H3=13. Multi-H1 = SEO smell — search engines expect single H1.

**Severity:** MED (theme-coupled — risk of theme breakage)
**Owner-touch:** No, but theme-edit possibly required
**Note:** Locate source — content-block double H1 OR theme template duplication

## ✗ Correction

### C1. Organization schema `sameAs` claim wrong

Geo wrote: "Organization, Bivision, address, phone, sameAs FB+LinkedIn ✓"

Wire-verify Apr 26 ~08:50:
- HTML link: `linkedin.com/company/bivisionge` ✓ (footer visible link, 2 occurrences)
- Schema `sameAs`: `["https://www.facebook.com/bivision.ge"]` only — **LinkedIn missing**

LinkedIn URL is on site as visible link (correct from owner perspective). But Organization Schema `sameAs` array contains only Facebook URL — structured data gap.

**Fix (low-risk, ~30 წმ):**
WP Admin → Rank Math → Titles & Meta → Local SEO → Organization → Social Profiles → Add LinkedIn URL

**Severity:** P3 hygiene (AI-search citation signal weaker, not site-breaking)

## ⚠ Verify-asks

### V1. Article schema homepage = "questionable" — validator confirmation needed

Geo wrote: "Article — Questionable. Should be CollectionPage or WebPage primary."

This is Geo opinion. Need formal validator pass:
```
https://validator.schema.org/?url=https%3A%2F%2Fbivision.ge%2F
```

If validator passes Article without warning → Geo's challenge weak, defer.
If validator warns/errors → Geo correct, prioritize fix.

**Action for Geo:** Run validator, append result to Phase A continuation.

### V2. page-sitemap thin — Rank Math config OR genuine gap?

Geo wrote: "page-sitemap thin (only home + privacy)... About, services, contact pages are not in page-sitemap. May be sections of homepage (anchors) or not indexed as standalone pages."

Two possibilities:
1. **Rank Math excludes pages** from sitemap (Settings → Sitemap Settings → Pages = "No")
2. **No standalone About/Services/Contact pages exist** (all sections of homepage)

**Action for Geo:** Check Rank Math sitemap config in WP admin. Document which case is true.

## ⚠ Reframe

### R1. TTFB 1.28s+ = ALREADY-KNOWN, not NEW finding

Geo flagged TTFB as "HIGH — likely root cause of Core Web Vitals fail". Severity correct, but **this was in Apr 23 audit baseline**. Not a new discovery.

**Reframe:** Tag as "DEFERRED post-MariaDB upgrade ~May 23" + "ALREADY-KNOWN since Apr 23".
Phase B re-measure trigger gated to MariaDB upgrade complete.

## Phase B blocker (re-confirm)

Phase A continuation:
- A.2 Rank Math SEO Analyzer per-page
- A.4 Internal Linking module
- A.5 Core Web Vitals manual PSI run
- A.6 Backlink profile
- A.7 GSC Queries 28 day

**Phase B recommendations cannot ship until A.2/A.4-A.7 complete.** Geo confirmed in last block — discipline intact.

## Symmetric audit reminder (per `feedback_geo_to_viktor_counter_audit.md`)

This counter-audit Viktor → Geo. Reciprocal Geo → Viktor on Viktor M1 (Schema Language Fix directive) — Geo's pre-execute gate should:
1. Verify Viktor M1 evidence (curl HTML lang + schema inLanguage)
2. Memory-rule cross-check (visibility-not-urgency, scope-lock)
3. Risk classification before execute
4. Skip if uncertain

If Geo flags any of M1's framing → respond here, defer execute.

## Action items for Geo

1. ADD M1 (image alt) + M2 (H1 count) to Phase A findings inventory
2. CORRECT C1 (sameAs LinkedIn schema gap, separate from visible link)
3. VERIFY V1 (validator.schema.org Article schema check)
4. VERIFY V2 (Rank Math sitemap config)
5. REFRAME R1 (TTFB as ALREADY-KNOWN, not NEW)
6. CONTINUE Phase A queue (A.2/A.4-A.7) before Phase B ship
7. EXECUTE M1 schema language fix when capacity opens (Geo discretion per Apr 25 risk-gate)

## Reporting

Append to next Phase A iteration HTML. Owner-touch zero unless V1/V2 surface owner-action.

## Memory rules cited

- `feedback_geo_to_viktor_counter_audit.md` — symmetric audit cycle
- `feedback_visibility_not_urgency.md` — TTFB reframed as ALREADY-KNOWN, not NEW urgency
- `feedback_no_fabrication.md` — sameAs claim correction (FB+LinkedIn was wrong, fact correction)
- `feedback_viktor_probe_discipline.md` — multi-source verify before urgency
- `feedback_bivision_site_dev_only_execution.md` — Geo execute risk-gate (Apr 25 supersede)

## Change log
- 2026-04-26 created — Viktor counter-audit Phase A draft 1
