---
from: viktor (relay owner Apr 26 directive)
to: geo
type: P1 plugin swap — cookie consent banner
created: 2026-04-26
trigger: owner Apr 26 reverse Apr 25 defer — execute swap now
risk-tier: LOW (plugin swap, reversible)
disk-channel: owner-bypass authorized
---

# CookieYes → Complianz Swap

## Owner directive

Apr 25: defer (risk-aversion).
Apr 26: **execute now.** Reverse decision authorized.

## Why

- ICP fit: Bivision = Georgian SME, English banner = mismatch (memory `feedback_georgian_market_reality.md`)
- Compliance gap: CookieYes free auto-scanner ineffective (uncategorized cookies fire pre-consent per Geo Apr 25 verify)
- Brand: "Powered by CookieYes" footer = outsourced look on B2B trust site
- Sprint coherence: Apr 25 hardening trajectory expects Georgian banner

## Action

### 1. Backup CookieYes config

Document current state (in case rollback):
- Banner text (English/Georgian, position, color)
- Tracker categorization (Clarity/FB/LinkedIn assignments)
- Active settings (regulation: GDPR, targeting: worldwide)

### 2. Install Complianz (free)

WP Admin → Plugins → Add New → search "Complianz | GDPR/CCPA Cookie Consent" → Install + Activate

### 3. Configure Complianz

- Wizard: select GDPR + Georgia (data law equivalent)
- Language: Georgian primary, English secondary
- Banner position: bottom (less intrusive)
- Buttons: Accept All + Reject All **equal-prominent** (mandatory per memory `feedback_visibility_not_urgency.md` cookie banner discussion)
- Auto-scan: run Complianz tracker scanner (key Complianz advantage over CookieYes free)
- Tracker categorization (post-scan):
  - Essential: WP/LiteSpeed/Wordfence cookies (always on)
  - Analytics: clarity.ms (Microsoft Clarity)
  - Marketing: connect.facebook.net (FB Pixel), snap.licdn.com + px.ads.linkedin.com (LinkedIn)
- Privacy Policy link → existing footer PDF URL
- Brand: skip Navy/Gold styling (Apr 26 owner deferred styling = polish, not core)

### 4. Functional verify (mandatory)

Incognito browser test:
- Banner appears on first visit ✓
- Banner = Georgian primary ✓
- Reject All click → DevTools Network → 4 tracker domains DON'T fire ✓
- Accept All click → trackers fire normally ✓
- Privacy Policy link works ✓

If ANY fail → revert: deactivate Complianz, reactivate CookieYes.

### 5. CookieYes deactivate (NOT delete)

Keep CookieYes installed-but-deactivated 24h as fallback. After 24h Complianz stable verify → delete CookieYes.

### 6. Wire verify

```bash
curl -s https://bivision.ge/ | grep -ic "complianz\|cookieyes"
```

Expected: complianz=1+ match, cookieyes=0 (post-deactivate).

## Risk gate

- Plugin swap = LOW (reversible 30-second)
- 4-step protocol mandatory: backup CookieYes config → install Complianz → verify ≤5 წთ → revert if fail
- If Complianz wizard requests payment for tracker auto-scan → use free version manual categorization (don't escalate to paid without owner approve)

## Deliverable

`outputs/2026-04-26 Cookie Banner Complianz Swap by Geo.html`

Sections:
- Pre-swap CookieYes state (backup snapshot)
- Complianz install + configure steps
- Auto-scan tracker categorization result
- Functional verify (4 trackers reject test)
- Wire verify post-deploy
- HTML mirror to bivision-shares GitHub Pages

## Memory rules

- `feedback_bivision_site_dev_only_execution.md` — Geo execute Apr 25 supersede
- `feedback_no_idle_on_owner_yes.md` — owner directive received, proceed
- `feedback_visibility_not_urgency.md` — owner-asked = legitimate trigger (NOT visibility-driven)
- `feedback_georgian_market_reality.md` — Georgian primary banner

## Change log
- 2026-04-26 created — owner Apr 26 reverse Apr 25 defer, execute swap
