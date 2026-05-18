# SESSION 2026-05-18 — bivision.ge AI SEO sprint

## სად გაჩერდა
Viktor session. AI-2 Schema complete. Menu fix done. llms.txt updated.

## დღეს გაკეთდა
- llms.txt: ASCII-safe ვერსია (encoding bug fixed, Georgian removed)
- AI-2 Schema: SoftwareApplication 6/6 live (BiFinance/BiRetail/BiStock/BiDebitors/BiAudit/BiMedical)
- Organization foundingDate=2015 + areaServed=Georgia live (custom block — duplicate exists, non-blocking)
- Menu "სერვისები" URL: /saas-products/bifinance/ → /saas-products/ ✅
- CookieYes confirmed removed, JS errors 0, iOS verified
- Gap checklist v6.3 live on GitHub Pages

## ახალი findings
- Total load time 6.7s (curl) — TTFB 1.7s. Performance P1.
- Organization schema duplicate (2 blocks on homepage) — minor, non-blocking
- SEO notice: /saas-products/bifinance-2/ trashed — redirect needed

## გაგრძელება შემდეგ სესიაში
1. AI-3: Case study blog post (sector + results needed from owner)
2. Organization schema clean (1 block only) — Rank Math Local SEO native
3. Redirect: /saas-products/bifinance-2/ → /saas-products/bifinance/ (Rank Math Redirections)
4. Performance: LiteSpeed Compress HTML = ON explicit
5. OG image branded 1200×630
6. hreflang ka + x-default (Rank Math Sitemap)
7. H1 keyword gap
8. wp-json restrict (.htaccess)
9. Audit v4 HTML (scores updated after all May 17-18 fixes)

## შენიშვნა
Viktor = second opinion only. GelLa = site execution. Dev freeze active.
permission_asks this session: 0

---

# GelLa SESSION 2026-05-18 (continuation)

## გაკეთდა
1. ✅ CEO Brief 2026-05-18 → `outputs/2026-05-18 CEO Brief by GelLa.html`
2. ✅ GA4 SA setup — bivision-analytics@shining-courage-493721-v5.iam.gserviceaccount.com → property 302944682
3. ✅ Analytics Admin API enabled, OAuth client created
4. ✅ GA4 real data: 194 sessions, BiRetail #1 (187 views), Organic Search=5 (critical gap)
5. ✅ GA4 section added to CEO Brief
6. ✅ HubSpot 16 deals pulled — morning analysis interrupted by session end

## სად გაჩერდა
- Morning deals analysis (10:30 deadline) — NOT completed. HubSpot data pulled, Meta/Mailchimp NOT pulled.
- EMERGENCY: bihub.ge down (Geo mistake)

## შემდეგ session-ში
1. bihub.ge restore — URGENT P0
2. Morning brief deals analysis completion
3. Overdue deals (ნუტრიველი Apr 7, 0llivander Apr 30) → closedlost?
4. LinkedIn API check inbox
5. FB Lead Gen campaign (Mariam 6Q gate)
6. Construction email open rates → Mailchimp

## permission_asks GelLa session: 0

---

# Gurafa SESSION 2026-05-18

## გაკეთდა
1. ✅ AI Deep Dive May 15-17 → `BI_gurafa/outputs/2026-05-17 AI Deep Dive May 15-17 by Gurafa.html`
   - Signal 1 (HIGH): Claude Code Routines — automates Monday competitor scan + daily CEO brief. Mentari keep-awake script = obsolete.
   - Signal 2 (POSITIVE): Claude Code limits doubled May 6. Not tightened for Bivision sequential sessions.
   - Signal 3: MCP → Linux Foundation (AAIF). Long-term investment validated.
2. ✅ Competitor analysis: aiworkshop.ge — 990 GEL × ~100 registrations (UNVERIFIED). Market signal confirmed.
3. ✅ Bivision Academy concept + page plan developed (see memory: project_bivision_academy.md)
   - Module 6 ADDED: Autonomous Systems / Claude Code Routines
   - Module 04 upgraded: Notion/Airtable → MCP connectors
   - Page structure agreed: Hero + Self-learning + Chat (Claude API) + Workshop + Payment

## სად გაჩერდა
Academy page build NOT started — plan only. Owner requested /clear before build.

## შემდეგ session-ში — Gurafa P0
1. **May 19 competitor scan** — Dastafe + DataStudio.ge (Monday, QUEUED)
2. **ctx-upgrade** — `npm install -g context-mode@latest` (broken: better-sqlite3, v1.0.111)
3. **Bivision Academy page** — domain decision needed from owner first
4. **Mentari inform**: Routines = keep-awake replacement. Test CEO brief automation.

## owner-pending (Academy)
- Domain: bivision.ge/academy OR academy.bivision.ge?
- Module pricing: M01 free / M02-06 at what GEL?

## permission_asks Gurafa session: 0

---

# Geo SESSION 2026-05-18 (bihub.ge backup)

## გაკეთდა
1. ✅ Full server backup: `C:\wamp\bihub_fullbackup_20260518.zip` (191.9MB) — server 185.229.111.201
   - Method: .NET ZipFile::CreateFromDirectory (Compress-Archive fails on pre-1980 timestamps)
   - Source: C:\wamp\www (408MB uncompressed)
   - Location: ON server only — no off-server copy yet

## key finding
- `Compress-Archive` = BROKEN on server 201 (timestamp bug). Use .NET ZipFile. Saved to memory.
- WinRM background jobs don't persist across sessions (each call = new shell). Poll via file existence.

## owner feedback this session
- "რატომ არ გამოიყენე გელას გზა?" — should have used WinRM directly from start, not elFinder/browser
- "წესების შედგენით ეფექტური არ ხდები" — action > protocol writing

## სად გაჩერდა
Backup created. /clear triggered.

## შემდეგ session-ში — Geo P1
1. **UpdraftPlus** — add themes+plugins to backup schedule (currently DB-only). P0 risk mitigation.
2. **Off-server backup** — download bihub_fullbackup_20260518.zip locally OR set up FastCloud panel backup
3. **bivision.ge DKIM** — Brevo "Authenticate this email domain" button (2-min, DNS already live)
4. **www.bivision.ge 301** — waiting owner "შეიტანე" (owner-gate, not Geo-blocked)
5. **functions.php** — current reconstruction 2,434 bytes; original 9,673 bytes; ~7,239 unknown. Low priority if site works.

## permission_asks Geo session: 1 (backup target: server vs local — clarified by owner)
