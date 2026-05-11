# Token Audit Dispatch Prompts — 2026-05-01

Authored by Viktor session a1a1afcf. Paste-ready for owner to dispatch to 4 agents.

Context: Token Usage Audit (`outputs/2026-05-01 Token Usage Audit by Viktor.html`) revealed D30 7.06B token usage, 100% Opus / 0% Sonnet, Solo Max plan, weekly 39% used Tue with Wed reset. Cross-agent optimization protocol = `feedback_token_optimization_canonical.md`.

---

## 1. Gurafa prompt — Anthropic account architecture research

```
EP0 prerequisite — research only, output HTML 30 min.

Task: Anthropic Claude Code account architecture research.

რას მინდა ვიცოდე:
1. Solo plan vs Team plan — feature diff (per-user usage, member tab, billing)
2. Solo Max ($100/mo, 5x) → Team plan upgrade ღირებულება + per-seat
3. Solo plan login ToS — multiple devices same account = OK ან violation?
4. Solo plan rate-limit shared across all logins YES/NO
5. Sonnet 4.6 vs Opus 4.7 — token quota share OR separate? Documentation extract
6. Daily routines feature — რა არის, როგორ მუშაობს, რა ღირს
7. /model toggle — Opus → Sonnet runtime switch?

Output: BI_gurafa/outputs/2026-05-01 Anthropic Plan Architecture by Gurafa.html
EP1 tags mandatory (FACT/HYPOTHESIS/UNVERIFIED).
Time cap: 30 min. Sources: docs.anthropic.com, claude.ai/docs, pricing page.
```

---

## 2. Geo prompt — Local machine audit

```
EP0: local machine audit, 0 risk, 20 წთ.

Task: ამ კომპიუტერის Claude Code state ფიქსირება.

1. Get-Content $PROFILE → PowerShell functions list (gurafa/viqtor/Nikacho/mentari)
2. ~/.claude/settings.json — model field არსებობს? რა არის value?
3. ~/.claude/projects/ → ყოველი folder size (du -sh ან PowerShell equivalent)
4. ~/.claude/projects/*/last-modified.jsonl — top-5 active sessions
5. Process scan: Get-Process | Where-Object {$_.Name -match "claude|node"} → active processes
6. tasklist /v | grep claude (active sessions running now)
7. ~/.claude/.credentials.json — file size + last-modified (DO NOT READ content)
8. PowerShell: $PROFILE-ი მუშაობს? Test viqtor-ფუნქციის CWD output:
   function viqtor.toString() ან Get-Command viqtor

Output: Nikacho/outputs/2026-05-01 Local Claude Audit by Geo.html
Strict: credentials არ წაიკითხო, ფაილების content არ exfiltrate-ი.
```

---

## 3. Agent A prompt — Active engagement self-audit + optimization adoption

```
EP0 prerequisite — self-audit + optimization adoption.

Context: Owner-მა გადაგვცა Token Usage Audit (Viktor, 2026-05-01). Findings:
- D30: 7.06B token, 100% Opus, 0% Sonnet — 5x rate-limit headroom locked
- Owner Solo Max plan, weekly 39% used Tue, Wed reset
- Playwright/Read/Bash dominate tool-use
- Subagent (Explore) under-used

Task ANT შენთვის (Agent A):

PART 1 — Self-report (15 წთ):
1. ახლანდელი session-ის თემა + ბოლო 5 task list
2. რომელი ფაილები წაიკითხე ბოლო 24 საათში (full path)
3. Tool-use frequency self-estimate: Read/Edit/Bash/Playwright/Grep/Subagent
4. Identification: რომელი task-ი იყო yallaze ძვირი (estimate)?
5. Owner-ს რომ ხშირად aprovs სიტუაცია — რა იყო მიზეზი (deep analysis vs simple ack)?

PART 2 — Optimization rules adoption:

შენ ხარ Agent A (active engagement). მიიღე და ცხოვრობდე:

A1. Model switch by task:
- Strategic / multi-file architecture / audit → Opus 4.7
- Edit / Grep / Read / Write / format → Sonnet 4.6 (`/model claude-sonnet-4-6`)
- List / count / quick-extract → Haiku 4.5

A2. Read discipline:
- Default offset+limit (არა full read 2000-line files)
- Big files → Grep/Glob first, Read precise lines after
- Subagent (Explore) > 3 file searches

A3. Playwright cap:
- Max 3 snapshot per task
- Screenshot only verification (არა debug-loop)
- Browser_evaluate > browser_snapshot when possible

A4. /clear discipline:
- Task done → /clear (არა multi-day session)
- /compact მინიმუმ
- Snapshot pre-/clear (memory + open items)

A5. HTML output policy (already canonical):
- Owner-facing = HTML, არა MD
- Path: AI_Projects/outputs/YYYY-MM-DD [Topic] by [Agent].html
- Chat = terse summary + path

PART 3 — Output:

File: outputs/2026-05-01 Agent A Self-Audit by [shen-agent-name].html
EP0 first line, 4-block format, EP1 tags.
Include:
- Self-report data (Part 1)
- Confirmation: optimization rules adopted (Part 2 each rule yes/no + objection if any)
- Op note: რა ცდიხარ ცვალო, რა ცდი არ ცდიხარ
Time cap: 30 წთ.
```

---

## 4. Agent B prompt — Plan mode autonomous self-audit + optimization adoption

```
EP0 prerequisite — self-audit + optimization adoption.

Context: Owner-მა გადაგვცა Token Usage Audit (Viktor, 2026-05-01). Findings:
- D30: 7.06B token, 100% Opus, 0% Sonnet
- Plan mode autonomous = Agent B-ის unique signature
- Owner Solo Max plan, weekly 39% used, Wed reset
- Plan mode efficiency-ი თეორიულად მაღალი (single decision, less exec churn) — ვერიფიკაცია საჭირო

Task შენთვის (Agent B):

PART 1 — Self-report (Plan mode lens, 15 წთ):

1. ბოლო 5 plan რომელიც დაწერე — Plan mode-ში რა შეფასე
2. Plan mode session-ის ტოკენ-პროფილი:
   - რამდენი თვითმდე plan-ი (Plan mode entries)
   - საშუალო plan-ის ზომა (lines / tokens estimate)
   - Plan-დან exec-ზე გადასვლის % (ExitPlanMode → actual exec)
3. რა ფაილებს კითხულობ Plan mode-ში გადაწყვეტილებამდე?
4. Plan-rejection-ი ხშირად? რა მიზეზებით?
5. Plan mode vs Direct mode self-comparison:
   - Plan-შემდეგ exec → token cost
   - Direct exec → token cost
   - Quality difference observed?

PART 2 — Optimization rules adoption:

შენ ხარ Agent B (Plan mode autonomous). მიიღე და ცხოვრობდე:

B1. Plan mode trigger discipline:
- Multi-file (≥3 files) ცვლილება → Plan mode worth
- Architectural / irreversible / unknown-blast-radius → Plan mode
- Single-file edit / known-fix / lookup → Direct mode (Plan mode overhead waste)

B2. Model switch (same as Agent A):
- Strategic plan / architecture → Opus 4.7
- Plan execution (Edit/Read/Write) → Sonnet 4.6 switch post-ExitPlanMode
- Quick lookup → Haiku 4.5

B3. Plan compactness:
- Plan ≤500 word normally
- Numbered steps, არა narrative
- Risk callout dedicated section
- Rollback path mandatory

B4. Read discipline (same as Agent A A2)

B5. /clear discipline (same as Agent A A4)

B6. HTML output policy (same as Agent A A5)

PART 3 — Output:

File: outputs/2026-05-01 Agent B Self-Audit by [shen-agent-name].html
EP0 first line, 4-block format, EP1 tags.
Include:
- Self-report (Part 1) — ფოკუსი Plan mode efficiency data
- Optimization adoption (Part 2 — each rule yes/no + Plan mode-specific notes)
- Comparison table: Plan mode vs Direct mode token-profile self-estimate
Time cap: 30 წთ.
```

---

## Sync / consolidation

After 4 outputs return → Viktor (next session) consolidates into single HTML "Token Usage Final Audit + Migration Decision Input" combining:
- Gurafa account architecture research
- Geo local machine audit
- Agent A self-audit + adoption confirmation
- Agent B self-audit + adoption confirmation
- Viktor original D30 audit + tool-use deep dive

Decision input for migration: Agent A vs Agent B vs Mentari token-efficiency comparison.
