---
date: 2026-05-21
agent: GelLa (this session)
status: DONE
---

## Done this session

### GTM — Clarity trigger fix
- Created "Window Loaded" trigger (GTM trigger ID in workspace 15)
- Clarity tag (tag 17): removed "All Pages", assigned "Window Loaded"
- Published as Version 15: "Clarity → Window Loaded"
- **Result: Mobile 57 → 71 (+14pts), TBT 800ms → 370ms (-54%)**

### Crisp finding
- Tag 24 (Custom HTML Tag) = UTM cookie tracker, NOT Crisp
- Crisp loads via WP plugin directly — not in GTM
- Cannot reduce Crisp TBT via GTM trigger change
- To defer Crisp: would need to either (a) move Crisp load to GTM, or (b) use WP hook to defer Crisp script

### LiteSpeed JS Delay (REVERTED — do not retry)
- Earlier session: added crisp+clarity to optm-js_delay_inc → score dropped 57→36, TBT 800→2180ms
- Immediately reverted. optm-js_delay_inc = "" (empty)
- DO NOT re-add crisp/clarity to LiteSpeed delay

---

## Where we stopped
- GTM V15 published ✅
- PageSpeed tested: Mobile 71, TBT 370ms ✅
- Owner asked to /clear after status saved

---

## Next session priorities

| # | Item | Owner | Notes |
|---|---|---|---|
| P0 | BiFinance Meta kill check | Gurafa+Owner | May 21 — CTR <0.3% at $5 → pause |
| P0 | GA4 Key Events toggle | Owner | phone_call/whatsapp_click/contact_form_submit |
| P1 | Crisp deferral (optional) | Geo | If TBT 370ms still flagged: move Crisp to GTM or WP defer hook |
| P1 | Energy email → Mailchimp | GelLa/Mariam | Campaign #17994061 audience fix + send |
| P1 | BiRetail tabs (B-01) | Geo | Needs owner "შეიტანე" |

---

## PageSpeed baseline (post-GTM-V15)
| Metric | Before | After |
|---|---|---|
| Mobile score | 57 | **71** |
| TBT mobile | 800ms | **370ms** |
| Desktop TBT | unknown | 360ms |
| FCP mobile | ~2.1s | 2.1s |
| LCP mobile | ~4.3s | 4.3s |

Next target: 80+ mobile → requires LCP improvement (images/video) + remaining TBT (Crisp)
