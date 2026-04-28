---
from: viktor
to: geo
type: P0 security probe — recurring scam attempt
created: 2026-04-26
trigger: owner Apr 26 — pashagaming reappears in Bivision context, scam attack vector, recurring pattern (matches earlier incident)
risk-tier: HIGH (security)
disk-channel: owner-bypass authorized
---

# Pashagaming Security Probe — Bivision.ge

## Context

Owner Apr 26: pashagaming = scam attack attempt against Bivision.ge. Recurring pattern (one prior incident). Owner observed pashagaming reference associated with Bivision (likely Google search index OR WP-side residual).

External wire-probe Apr 26 13:45 (Viktor):

- `/pashagaming/`, `/pasha-gaming/`, `/PashaGaming/`, `/pasha/` → ALL 404 ✓
- Sitemap 31 URLs → 0 match
- Site source HTML → 0 "pasha" mention
- Blog HTML → 0 "pasha" mention
- Spam keyword scan (casino/betting/loan/pharmacy/viagra) → 0 occurrences
- wp-admin → 302 (login-protected, healthy)

**External attack surface = clean.** Internal WP probe required for full clearance.

## Action — Geo execute

### 1. Wordfence full scan (priority)

WP Admin → Wordfence → Scan → "Start New Scan"

Watch for:
- File changes (modified core / theme / plugin files)
- DB injection (suspicious posts/pages/options)
- Backdoor PHP files
- Spam comments

If scan flags compromise → **STOP, owner notify immediate.** No remediation by Geo without owner direction.

### 2. WP DB search

WP Admin → Posts → All Posts → Search "pasha" → expected 0 result
WP Admin → Pages → All Pages → Search "pasha" → expected 0 result
WP Admin → Comments → Search "pasha" → expected 0 result

If any match → flag in deliverable, do NOT delete without owner confirm.

### 3. Google Search Console URL removal

WP Admin → Site Kit → Search Console → URL Inspection → check `https://bivision.ge/pashagaming/`

If indexed → "Request Removal" tool (immediate Google deindex 1-3 day).

### 4. .htaccess hardening — 410 Gone for pashagaming pattern

Add to `.htaccess` after `# END WordPress`:

```apache
# BEGIN Anti-Spam Pattern
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteRule ^pasha[^/]*/?$ - [G,L]
</IfModule>
# END Anti-Spam Pattern
```

`[G,L]` returns 410 Gone (stronger deindex signal than 404). `^pasha[^/]*/?$` matches any URL starting with "pasha".

4-step protocol:
- backup `.htaccess.bk-pre-pasha-apr26`
- edit insert
- save
- verify: `curl -sI https://bivision.ge/pashagaming/` → expect `410 Gone`

### 5. Wordfence Country Block — optional

If repeated attack source identifiable (likely Azerbaijan IP range or VPN), Wordfence → Blocking → Country Blocking. Owner discretion.

## Risk gate

- If Wordfence scan flags compromise → SKIP fix, escalate to owner
- If WP DB search returns results → flag, await owner direction
- 410 Gone .htaccess change = LOW risk (backup-revertible)
- GSC URL removal = zero-risk, owner-side action OR Site Kit access

## Deliverable

`outputs/2026-04-26 Pashagaming Security Audit by Geo.html`

Sections:
- Wordfence scan result (clean/flagged)
- WP DB search result per Posts/Pages/Comments
- GSC URL removal status (submitted/pending/declined)
- .htaccess hardening deploy state (deployed/skipped reason)
- Wire verify post-deploy: `curl -sI https://bivision.ge/pashagaming/` → 410 expected

## Memory rules

- `feedback_bivision_site_dev_only_execution.md` — Geo execute Apr 25 supersede, 4-step protocol
- `feedback_visibility_not_urgency.md` — owner-flagged security ≠ visibility-driven, legitimate trigger
- `feedback_no_idle_on_owner_yes.md` — proceed without "Yes", risk-gate intact
- `feedback_geo_to_viktor_counter_audit.md` — symmetric audit on Viktor directives

## Reporting back

Append to existing AUDIT_REQUEST.md (Apr 26 row) — security audit result. Notify Viktor + Owner via deliverable URL.

## Change log
- 2026-04-26 created — Viktor → Geo P0 security probe per owner-flagged scam recurrence
