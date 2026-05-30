---
class: DECISIONS LOG (system of record for owner decisions)
created: 2026-05-30 (Viktor) — none existed; created per owner directive
governs: Constitution §4.8 (permission-ask) + canonical_viktor §7 (propose-not-decide)
---

# DECISIONS LOG

System of record for **owner decisions only**. Agents PROPOSE; the owner DECIDES.

## Header logic (read before writing an entry)

1. **An entry belongs here ONLY if it cites the owner's verbatim chat authorization.**
   No owner quote → it is still a PROPOSAL → it lives in `SESSION_OPEN_ITEMS.md`, NOT here.
   (canonical_viktor §7: agents never author a decision; they record the owner's conversion of a proposal.)

2. **Permission-ask filter (Constitution §4.8) — before asking "გავუშვა?" check the 5 triggers:**
   money · customer-facing · irreversible · business priority/direction · owner-authority.
   Hits a trigger → ask, and on owner's "yes" log the decision here.
   Hits none (reversible + internal + in-lane, direction already given) → **execute + report, do NOT log here.**
   Test: *"Do I actually hold information the owner lacks, and is this their call to make?"* No → just do it.

3. **One row per decision.** Owner-verbatim authorization is the proof. Keep it short.

| Date | Decision (owner verbatim) | What it changes | Rule / § affected | Logged by |
|---|---|---|---|---|
| 2026-05-30 | "New rule for everything you produce going forward… You PROPOSE; you do not DECIDE." | Viktor never writes DECISION/override/approved for owner-authority items; labels PROPOSAL + 4 fields; retroactive re-label | `canonical_viktor.md §7` (new) | Viktor |
| 2026-05-30 | "Add this to the Constitution (§5 behavior, alongside the session-start sequence)… then execute perfectly." | Permission-ask discipline: ask only on money / customer-facing / irreversible / priority / owner-authority; else execute+report | `OPERATING_CONSTITUTION.md §4.8` (new) + §5 pointer | Viktor |
| 2026-05-30 | "v3 micro-test was already STOPPED in our prior session — full hold = everything OFF." | BiFinance v3 micro-test = STOPPED/paused, all OFF. Never re-offer a run ("let it spend to $10" is dead). | operational — lead-gen / Meta | GelLa |
| 2026-05-30 | "paid/organic spend stays OFF until the full lead-ready gate passes." | No paid OR organic spend until the 6-dim lead-ready gate PASSES. "organic-first vs paid-now" + MQL realism = POST-gate questions, not pre-gate. | §2.1 budget gate | GelLa |
| 2026-05-30 | "owner money-decision, confirmed: STOP v3 now… explicit authorization to halt spend." | **CORRECTS the D-001 row above (does not rewrite it):** D-001 recorded the owner's turn-1 belief that v3 was "already STOPPED"; live Meta pull this session showed v3 was in fact ACTIVE and still spending — D-001 was premature/incorrect at write time. Owner then authorized the actual stop. v3 (campaign `BiFinance_Phase1_v3` / form `BiFinance_Demo_v3_Calendly`) paused 2026-05-30, **live-verified PAUSED** (effective_status PAUSED), final spend **$8.21**, lifetime native lead-form leads = **1**. Channel verdict: FB native lead-gen PAUSED pending a future scale decision. **Sync-config status = UNVERIFIED** (connected-apps not API-exposed; 1 paid-social-attributed HubSpot contact, ambiguous) — explicitly NOT asserted as "no sync built". | operational — lead-gen / Meta · supersedes D-001 framing | GelLa |
| 2026-05-30 | "დადასტურებულია" (confirming §2.7 Verification-Before-Conclusion as proposed in Viktor's 2026-05-30 handoff) | New abort-class red line: no diagnosis/verdict/severity claim without live data shown in-response; absence triggers a discriminator not a verdict; drama barred from FACT; limitation-honesty mandatory | `OPERATING_CONSTITUTION.md §2.7` (new, extends §2.2) — landed as §2.7 (§2.7 Governance-Lane not yet on disk; numbering resolved at write time) | GelLa |
| 2026-05-30 | "დადასტურებულია" (confirming the Governance-File Lane Rule §2.8 as proposed in Viktor's 2026-05-30 handoff; owner basis: "ONLY GelLa writes to governance / live files… Viktor… PROPOSE… GelLa EXECUTES… I confirm it now") | Sole governance-file writer = GelLa; Viktor propose-only; mechanism propose→confirm→GelLa-writes; Geo writes own-lane live files only | `OPERATING_CONSTITUTION.md §2.8` (new) — landed as §2.8 (§2.7 taken by Verification-Before-Conclusion; numbering resolved at write time) | GelLa |
| 2026-05-31 | "დადასტურებულია" (confirming the Standardized Session-Handoff Protocol v1 from Viktor's 2026-05-31 proposal). Owner decisions: **D1** = router-only (do NOT create Viktor/Geo launcher dirs); **D2** = `GELLA_HANDOFF.md` = SSOT for GelLa session-state, `SESSION_OPEN_ITEMS.md` = cross-agent bridge, `contracts/queue.md` + `charter.md` = static inputs; **D3** = lightest binding (router block + one §5 line, NO new §4.9). | Standardized handoff: `BI_C-Suite/docs/handoffs/` + 4 fixed `<AGENT>_HANDOFF.md` + `archive/`; global-router auto-read/auto-save block (Handoff Protocol v1); Constitution §5 session-start line; `clear-bi` extended to 4 agents (step 4b); GelLa two-state collapse; fixed naming. | global router `~/.claude/CLAUDE.md` + `OPERATING_CONSTITUTION.md §5` line (NO new §) + `clear-bi` command + launchers (GelLa step-0 DONE; **Gurafa step-0 PENDING** — launcher UTF-16 LE w/ mojibake, not blind-edited per §2.6) | GelLa |
| 2026-05-31 | "დადასტურებულია" (correcting the stale single-agent framing in `BI_DonotUseMe/CLAUDE.md`). Owner: the 2026-05-01 single-agent / "Viktor+Gurafa lanes ABSORBED" / "Gela only" / "others SUPERSEDED" directive is **SUPERSEDED as of 2026-05-31** — current live model = 4 maximally-independent agents (GelLa / Viktor / Gurafa / Geo), each own lane + handoff, shared AWARENESS via `SESSION_OPEN_ITEMS` + `DECISIONS_LOG` + router; nothing ships without Viktor's challenge layer. | GelLa launcher de-staled: removed "absorbed / superseded / only-agent / single-agent posture"; **preserved lane-isolation** (GelLa keeps own identity, reads others for DATA only, no cross-identity bleed); Mentari stays genuinely deprecated. Historical 2026-05-01 directive NOT deleted — superseded-by-append. | `BI_DonotUseMe/CLAUDE.md` (identity-override + identity-routing sections) | GelLa |

## Open — NOT decisions (pending owner, do not treat as settled)

These are PROPOSALS awaiting the owner's word. Tracked in full in `SESSION_OPEN_ITEMS.md`.

- **§2.3 "override" (GelLa as LinkedIn copy source, Mariam bypassed) — ✅ DISCARDED 2026-05-30, NOT pending.** Owner verbatim: *"treat it as INVALID and discard it — §2.3 stands unchanged, Mariam remains primary copy source."* §2.3 Reputation Risk Gate is live & unchanged on disk (Constitution §2.3, lines 45–49). *Correcting note (history preserved): this entry previously read "CONSTITUTION CHANGE, owner approval required… Owner must approve or revert" — that framing was STALE; the owner had already discarded it. Now matches SESSION_OPEN_ITEMS.*
- **MQL target realism (20-30/mo)** — organic caps ~5-8; owner picks organic-first vs. commit paid budget (→ §2.1 gate).
