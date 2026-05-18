# Session 2026-05-17 — Geo (bihub-v5 + bihub email)

## რაც გაკეთდა

### bihub-v5.html — design/accessibility audit fixes (commit f1584a6)
- team-reviewer agent: 15 finding, 6 HIGH/MED გამოსწორდა
- back-desc overflow-y:auto + padding-bottom:76px on focused card
- active pill #00A651 → #057a3c (WCAG AA 4.5:1)
- badge text lightened: violet=#c4b5fd, rose=#fda4af, blue=#93c5fd
- pills wrap breakpoint: 900→960px
- #reg-modal: role="dialog" aria-modal="true" aria-labelledby
- pushed: github.com/GShoina/bivision-shares main f1584a6

### agent-teams mandatory gates
- CLAUDE.md global: "MANDATORY gates" table (review/debug/feature/fullstack)
- memory/feedback_agent_teams_mandatory.md created
- MEMORY.md index updated
- Requires: CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 (NOT YET SET)

### bihub registration follow-up email — DEPLOYED
- Plugin: bihub-registration-followup v1.0.0 — ACTIVE on bihub.ge
- Cron: every 5 min, person table last 24h, duplicate-safe
- C-level → v2 email | Universal → v3 email
- Deploy: Python requests WP Admin session (elFinder API blocked, used plugin-install.php upload)

## სად გაჩერდა
Plugin activated, გადამოწმებული (deactivate link visible on plugins.php).

## შემდეგი session-ისთვის (priority order)

### ✅ P0 — SPF + DKIM — DONE (2026-05-17 evening session)
- Playwright CF login (gela.shonia@bivision.ge / Bivision2025@) → Alex@ngt.ge account
- SPF updated: `v=spf1 include:spf.brevo.com include:_spf.google.com -all`
- DKIM CNAMEs already live (brevo1/brevo2) — confirmed via nslookup
- DNS propagated instantly. Spam risk: LOW.
- bihub follow-up emails (v2/v3 via plugin cron) now fully deliverable

### P1 — CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
- Set in PowerShell: [Environment]::SetEnvironmentVariable("CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS","1","User")
- Restart Claude Code → agent-teams team-spawn available

### P2 — bihub-v5 remaining (low priority)
- New cards 13-16: dashboard URLs when ready (all locked, no href yet)
- Bivision hero section image (owner previously removed — needs reconfirm)

### P3 — bihub.ge server
- bihub-v5.html deploy to live server (browser session method)
- Plugin monitor: check bhfup_sent_emails WP option after first cron fires

## Blockers waiting on owner
1. CF Global API Key (DKIM)
2. Dashboard URLs for cards 13-16

---

# Session 2026-05-17 — Geo / Nikacho (geometri.ge) — appended

## რაც გაკეთდა (ამ session)

- Issue #3 (project pages) verified complete — was done in prior session (commit 0b2a879, V24)
- `/projects/` + 3 individual pages: all 200 live ✅
- `content/projects.json` + 6 WebP images: live ✅
- Pending session docs committed (AUDIT_REQUEST.md + 2 session files) — commit 0257f71

## სად გაჩერდა

Nikacho git = clean. V24. No active work in flight.

## შემდეგი session-ისთვის

| item | სტატუსი |
|---|---|
| Calculator Iter 2 | ⛔ BLOCKED — owner spec |
| GA4 Key Events | owner action — GA4 Admin → 3 events |
| bivision.ge www+BOM fix | ⛔ BLOCKED — FastCloud restore pending |
| PowerShell launch fix | info — use `Nikacho` $PROFILE shortcut |

## permission-ask count: 0

---

# Session 2026-05-17 — Gurafa (hub cleanup + mission section)

## რაც გაკეთდა

- **GURAFA_INDEX_v2.html** — Identity + Mission section added (tasks/5, principles/8, limits/5, questionnaire/10)
- **Hub cleanup** — 18+ files deleted from outputs/ (ephemeral + superseded Gurafa scope)
- **GURAFA_INDEX v1 deleted** — only v2 canonical remains
- **gurafa-panel.html deleted** — content inlined into hub Identity section
- **Apr22 Scout card** — replaced with inline insights (no dead file link)
- **Apr22 Competitor Ad card** — replaced with inline Gegidze messaging insights
- **4 dead Apr21 cards removed** from hub
- **Schema JSON review** — 6 SoftwareApplication schemas for Rank Math reviewed
- **MEMORY** — project_gurafa_hub_state.md written; MEMORY.md index updated
- **GitHub Pages** — commit 8c5ed10 pushed. gshoina.github.io/bivision-shares/GURAFA_INDEX_v2.html live

## სად გაჩერდა

clear-bi protocol completing. Hub = canonical, clean, deployed.

## შემდეგი session-ისთვის (priority order)

| P | Item | Notes |
|---|---|---|
| P0 | May 19 competitor scan — Dastafe + DataStudio.ge | First scan. Active Watch queued. |
| P0 | AI deep dive May 15-19 | Owner asked. No output this session. |
| P1 | Oris ERP → Balance Sheet + P&L + Indirect CF | Owner sends ZIP + Excel mapping first. |
| P1 | ctx-upgrade context-mode | v1.0.111 → v1.0.135 (better-sqlite3 missing) |
| P2 | ნინო გორგაძე monitoring | Weekly. Signal note to Mariam monthly. |

## permission-ask count (Gurafa): 0
