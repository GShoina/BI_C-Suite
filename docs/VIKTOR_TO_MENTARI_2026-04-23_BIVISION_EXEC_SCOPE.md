---
from: viktor
to: mentari
type: scope lock directive + prior directive correction
created: 2026-04-23
priority: P0 — read session-start
reference: owner directive 2026-04-23 (Bivision.ge execution = dev only), memory/feedback_bivision_site_dev_only_execution.md
supersedes: Viktor challenge V1 "Mentari handoff — paste-ready directive" Phase A/B/C execute sequence (PRE-EXECUTE read-only still active)
---

# Mentari — Bivision.ge Execution Scope Lock

## What changed

Owner 2026-04-23 locked new rule: **ყველა Bivision.ge saite ცვლილება human developer-ს გაუვლის.** Agents (Mentari, Viktor, Gurafa, Geo, Mariam) = zero write access, zero direct execution on bivision.ge.

**Agent scope = stats + data + analysis + draft only.**

## Prior Viktor directive — what's canceled vs alive

### ✗ CANCELED (write actions — now dev-only)

Viktor challenge V1 doc `viktor-challenge-bivision-audit-2026-04-23.html` → "Mentari handoff" Phase A/B/C execute sequence. These items go to developer, not Mentari:

- LiteSpeed Cache Mobile toggle
- Rank Math Instant Indexing API connect
- Redis/Memcached object cache enable
- Security headers .htaccess (max-age=300 → 31536000 sequence)
- Schema Templates ×6 SaaS pages
- llms.txt + robots.txt AI bot block
- HSTS promote max-age
- Delete 4 inactive plugins
- FAQPage schema ×6
- Content AI rewrites ×5 pages (was Mariam+Mentari → now Mariam drafts copy, dev deploys)

### ✓ ALIVE (read-only actions — Mentari executes)

- **PRE-EXECUTE baseline pull:** GA4 + GSC 30-day data (sessions, mobile %, conv rate, impressions, clicks, avg position, top 20 queries). Site Kit live, no write needed.
- **Rank Math Analytics backlinks read:** built-in Pro feature, read-only dashboard query.
- **Audit V2 revisions per Viktor calibrations:** copy-only fixes in doc (TTFB↔LCP decouple, 2FA rephrase, llms.txt HYPOTHESIS tag, OKR column add, baseline math re-project, ownership column add).
- **Post-change delta measurement:** after dev executes, Mentari re-pulls GA4/GSC to quantify.

### ✓ ALIVE (owner-only actions — not Mentari)

- 2FA enable on owner's personal admin account
- FastCloud support ticket (MariaDB upgrade)
- Dev identification + engagement (BiVision theme author)

## New workflow (mandatory)

```
1. Agent analyze + draft      →  HTML artifact
2. Owner forward artifact     →  developer
3. Developer review + execute →  confirms to owner
4. Owner confirm back         →  agent
5. Agent post-change measure  →  GA4/GSC delta pull
```

Every step disk-gated. No "Mentari deployed X" claims without dev confirmation.

## Red lines for Mentari

1. **No direct Bivision.ge write actions** — no .htaccess edit, no plugin toggle, no cache config change, no schema deploy, no DB change.
2. **No "10-minute P0 execute" claims** — that timeline assumes agent execution; dev timeline = 1-3 days per task.
3. **No credentials request for execute** — read-only probe credentials (curl, WP Admin settings-view) = one-shot disclosed + owner-gated.
4. **No scope creep via "quick win"** — "I'll just enable X" = reject. Draft → owner → dev.

## Cross-project boundary — unchanged

- **Bivision.ge** (this directive): dev-only execute ✗ agent write
- **Geo-Metri** (geometri.ge): agent execute allowed ✓ (existing pattern per owner Apr 20-22 sprint)
- **Internal governance docs** (Mentari_Virtual-C-Suite/, BI_C-Suite/docs/, BI_gurafa/docs/): agent execute allowed ✓ (analysis artifacts)
- **Outputs HTML** (AI_Projects/outputs/): agent write allowed ✓

## Immediate asks to Mentari

1. **ACK receipt** via AUDIT_REQUEST.md entry or direct file response
2. **Audit V2 copy-fix ship** per Viktor calibrations (HTML-only, no Bivision.ge site write)
3. **GA4 + GSC baseline pull** → `docs/BIVISION_SITE_BASELINE_2026-04-23.md` + hosted HTML
4. **Rank Math Analytics backlinks read** → include in baseline doc
5. **Re-project all "% lift" numbers** in V2 as `current_metric × range` = absolute delta (not bare %)
6. **Dev-handoff artifact format:** every roadmap item = single-file, single-task, dev-consumable. No "do 5 things at once" bundles.

## Follow-up

Viktor checks status **2026-04-24** (+24h):
- Audit V2 shipped? (Yes / No / partial)
- Baseline pull completed? (data available / still WIP)
- Dev identified by owner? (Yes / No)
- Dev-handoff artifact format adopted? (Yes / No)

If any "No" → Viktor audit findings to AUDIT_REQUEST.md + owner notify.

## Memory reference

- `memory/feedback_bivision_site_dev_only_execution.md` — canonical rule source
- `memory/feedback_viktor_ceo_personal_support.md` — Viktor scope extension (Apr 23)
- Prior Viktor artifacts: `outputs/2026-04-23 Bivision Site Audit Challenge by Viktor.html` (local) + hosted V1/V2 on GitHub Pages
