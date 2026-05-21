---
date: 2026-05-21
agent: GelLa + Mentari (multiple sessions)
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

---

## Viktor audit session (2026-05-21 afternoon) — Mentari/Geo lane

### Done

| Task | Result |
|---|---|
| .gitignore audit (all repos) | All 4 repos already had canonical credential block ✅ |
| B-02 pixel fix | `495329725412052` removed from functions.php wp_head via fetch POST to WP Admin. LiteSpeed purged. Only correct pixel `24993373220352719` fires. ✅ |
| B-01 tab JS | FALSE POSITIVE — JS already correct (`.products-tab-item`), all 6 tabs work ✅ |
| GTM malware flag | UI artifact from hack period. Tags fire normally. GA4 confirmed via network. ✅ |
| PageSpeed recheck | Mobile 67, TBT 780ms — suspect LiteSpeed cold cache after purge. Recheck May 22. |

### Where stopped
- B-03 (empty H1) → backlog, owner deferred to May 22
- PageSpeed TBT needs recheck May 22 (cold cache suspect)

### May 22 priorities

| # | Item | Notes |
|---|---|---|
| P0 | bihub.ge migration | Script ready: `~/.claude/scripts/bihub_migration.ps1` |
| P0 | PageSpeed recheck | Mobile 67 → confirm 71 recovery or investigate TBT 780ms |
| P1 | B-03 empty H1 | PHP template edit — owner to decide approach |
| P1 | Crisp + render-blocking scripts | If TBT still high after cache warm |

---

## bihub.ge session (2026-05-21 evening) — Geo lane

### Done

| Task | Result |
|---|---|
| Forgot password live test | Flow works, email lands in spam |
| DKIM verify | Already live since May 17 ✅ |
| SPF added to CF DNS | `v=spf1 include:spf.brevo.com ~all` ✅ |
| DMARC verify | `p=none` live ✅ |
| Accidental migration + rollback | .htaccess clean ✅ |
| Migration DEFERRED | Owner: 2026-05-22 night |
| FastCloud panel pass updated | creds ✅ |

### Backups on server (185.229.111.201)

- `C:\wamp\bihub_fullbackup_20260520.zip` — 180MB
- `C:\wamp\bihub_db_20260520.sql` — 19MB

### Tomorrow (2026-05-22)

1. SPF spam retest — forgot password → inbox?
2. Migration: `powershell -File ~/.claude/scripts/bihub_migration.ps1`
3. Post-migration tests: bihub.ge/ → v10, /cards/ → WP, /wp-admin/ → login
4. SweetAlert fix (post-migration) — forgot form AJAX + "შეამოწმეთ სპამი"
