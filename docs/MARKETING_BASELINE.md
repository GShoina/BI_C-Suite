---
class: ACTIVE
owner: CEO + CMO
updated: 2026-04-06
source: GA4, GSC, HubSpot, Meta Business Suite, Clarity, Mailchimp, WordPress — Playwright extraction
period: March 8 - April 6, 2026 (28 days unless noted)
---

# Marketing Baseline — ბივიჟენი

## მისია

ყველა digital არხის ფაქტობრივი სურათი → SWOT → Level 4 Minimum Viable System მარკეტინგისთვის.
მარიამის deadline: მაისის დასაწყისი. ეს baseline = გადაწყვეტილების საფუძველი.

---

## 1. Platform Data (✅ FACT — extracted 2026-04-06)

### GA4 (28 days, bivision.ge)

| მეტრიკა | Value | შეფასება |
|----------|-------|---------|
| Active users | 262 | |
| New users | 254 (97%) | 🔴 თითქმის 0 returning |
| Avg engagement time | 55 sec | 🔴 ძალიან დაბალი |
| Event count | 2.2K | |
| Key events (conversions) | 6 | 🔴 0% conversion rate |

**ტრაფიკის წყაროები (Active users):**

| Source | Users | % | შეფასება |
|--------|-------|---|---------|
| (direct) / (none) | 211 | 80.5% | 🔴 უატრიბუციო — არაფერი მუშაობს |
| google / organic | 34 | 13.0% | 🟡 ნორმალური B2B-სთვის |
| Facebook (all referrals) | 13 | 5.0% | 🟡 დაბალი, მაგრამ არის |
| bihub.ge / referral | 3 | 1.1% | 🟢 BiHub-დან ტრაფიკი |
| linkedin / paid_social | 1 | 0.4% | 🟡 organic UTM, არა paid |

**Sessions by source:**

| Source | Sessions |
|--------|----------|
| (direct) / (none) | 284 |
| google / organic | 64 |
| l.facebook.com / referral | 21 |
| search.google.com / referral | 11 |
| m.facebook.com / referral | 8 |
| linkedin / paid_social | 7 |
| bihub.ge / referral | 4 |

**Top pages:**

| Page | Views | Users | Bounce Rate |
|------|-------|-------|-------------|
| მთავარი (Home) | 333 | 163 | 53.3% |
| პარტნიორები (Partners/Blog) | 120 | 30 | 7.5% |
| BiFinance | 75 | 59 | 31.6% |
| Balance პარტნიორობა | 61 | 24 | 41.3% |
| **Page Not Found** | **31** | **26** | **70.0%** |
| BiRetail | 20 | 13 | 15.0% |
| ICR ტრეიდი | 13 | 9 | 16.7% |

**Cities (Active users):**

| City | Users | შეფასება |
|------|-------|---------|
| Tbilisi | 104 | 🟢 real Georgian traffic |
| Singapore | 36 | 🔴 bot/crawler |
| Boardman | 13 | 🔴 AWS bot |
| Dublin | 10 | 🔴 cloud bot |
| Amsterdam | 7 | 🔴 bot |
| Moscow | 4 | 🟡 |
| Ashburn | 3 | 🔴 bot |

**⚠️ INFERENCE (H):** 262 active users-დან real Georgian = ~110-120. დანარჩენი ~140 = bots/crawlers. **რეალური ტრაფიკი = ~120 user/28 days = ~4 user/day.**

---

### GSC — Google Search Console (3 months: Jan 5 - Apr 4, 2026)

| მეტრიკა | Value | შეფასება |
|----------|-------|---------|
| Total clicks | 3,940 | |
| Total impressions | 295,000 | |
| Average CTR | 1.3% | |
| Average position | 5.5 | |
| Total queries | 317 | |

**🔴 CRITICAL — Top queries:**

| Query | Clicks | Impressions | რა არის |
|-------|--------|-------------|---------|
| **pashagaming** | **3,368** | **101,378** | 🔴 SEO POISONING |
| pasha gaming | 103 | 156 | 🔴 SEO POISONING |
| **bivision** | **36** | **115** | ბრენდი |
| pashagaming giriş | 33 | 8,541 | 🔴 SEO POISONING |
| pasagaming | 31 | 99 | 🔴 SEO POISONING |
| pasha gaming giriş | 17 | 25 | 🔴 SEO POISONING |
| pashagamin | 16 | 48 | 🔴 SEO POISONING |
| paşagaming | 14 | 53 | 🔴 SEO POISONING |
| pashagaming güncel | 10 | 103 | 🔴 SEO POISONING |
| pashagaming güncel giriş | 9 | 149 | 🔴 SEO POISONING |

**✅ FACT: GSC-ში pashagaming queries = 3,621/3,940 clicks (91.9%) — მაგრამ ეს ისტორიული data-ა.**

✅ FACT (ოუნერი validated 2026-04-06): 3 კვირის წინ საიტი დაჰაკეს. აღდგენილია ძველი ვერსია, კოდიდან წაშლილია, უსაფრთხოების plugin დაყენებულია, დეველოპერები ჩართულნი იყვნენ. **საიტი ახლა სტაბილურია.**

GSC data = ძველი period-ის ჩანაწერები. ოუნერი ფილტრავს. data არარელევანტურია — თანდათან გაქრება Google-ის recrawl-ით.

⚠️ INFERENCE (M): GSC URL Removal Tool-ით შეიძლება ძველი URL-ების დაჩქარებული წაშლა. ასევე sitemap resubmit = recrawl-ის ტრიგერი.

---

### HubSpot — Sales Pipeline

**სულ: 10 deals. Active pipeline value: $0 (ყველა $1,000 placeholder).**

| Deal | Stage | Amount | Close Date | Status |
|------|-------|--------|------------|--------|
| Rampoletx BI | SQL | $1,000 | Apr 30, 2026 | 🟢 Active, email 3d ago |
| რუსთავის ავტოდრომი / საგა | SQL | $1,000 | Apr 30, 2026 | 🟢 Active, meeting 2d |
| 0llivander | SQL | $1,000 | Apr 30, 2026 | 🟢 Active, note 3d ago |
| ევროპული ჰოსპიტალი | Messaged | -- | Apr 30, 2026 | 🟡 No response, email 1mo ago |
| არსი | Closed Won | $1,000 | Mar 5, 2026 | ✅ Won |
| Connect | SQL | $1,000 | Feb 28, 2026 | 🔴 STALE — expired 37 days |
| გრეიდი | Replied | $1,000 | Feb 28, 2026 | 🔴 STALE — expired 37 days |
| ნუტრიველი | Decision maker | $1,000 | Dec 31, 2025 | 🔴 STALE — expired 96 days |
| ჯეო ჯგუფი (ბათუმი) | Closed Lost | $1,000 | Jan 20, 2026 | ❌ Lost |
| Music House | Closed Lost | $1,000 | Jan 20, 2026 | ❌ Lost |

**Pipeline status (✅ CORRECTED 2026-04-06, owner validated):**
1. ✅ $1,000 = ~1,000₾ საშუალო ფასი, **არა placeholder.** HubSpot free version-ში currency $ ჩანს, real = ₾. Pipeline value = real.
2. 🔴 3 stale deal: Connect (37d), გრეიდი (37d), ნუტრიველი (96d) — close ან archive
3. 🔴 0 deals Proposal/Contract სტადიაში — pipeline gap
4. 🟡 ევროპული ჰოსპიტალი — 1 თვეა პასუხი არ მოსულა
5. 📋 TODO: HubSpot currency config → GEL (მენცარი Playwright-ით)

---

### Meta Business Suite — Facebook (Mar 8 - Apr 4, 2026)

| მეტრიკა | Value | Change | შეფასება |
|----------|-------|--------|---------|
| Views | 35,800 | ↑ 51.7% | 🟡 spike, probably 1 reel |
| Viewers | 26,261 | ↑ 48.9% | |
| From followers | 1.3% | ↓ 32.7% | 🔴 followers ვერ ხედავენ |
| From non-followers | 98.7% | ↑ 0.6% | vanity views |
| **Content interactions** | **32** | **↓ 87.2%** | 🔴 35.8K views = 32 interactions |
| From followers interactions | 16 | ↓ 82.4% | |
| From non-followers interactions | 16 | ↓ 89.9% | |
| Page visits | 236 | ↓ 30.6% | |
| New follows | 7 | ↓ 46.2% | |
| Unfollows | 1 | | |
| Net follows | 6 | ↓ 45.5% | |
| Content published (last week) | 1 | | 🔴 1/week < target 1/2week |

**⚠️ INFERENCE (H):** 35.8K views / 32 interactions = **0.09% interaction rate.** ეს ნიშნავს content ადამიანებს არ აინტერესებთ — vanity reach. მარიამის OKR target 35-40 engagement/post vs actual ~3-5/post.

**Views spike pattern:** 14 დღე = 14-66 views/day. 4 დღე = 4,400-5,400/day (96% views). **1 viral reel ქმნის ილუზიას, მაგრამ 0 engagement.**

---

### Clarity — Microsoft Clarity (28 days)

| მეტრიკა | Value | შეფასება |
|----------|-------|---------|
| Sessions | 254 | |
| Bot sessions excluded | 115 (31%) | 🔴 1/3 = bots |
| Unique users | 179 | |
| Pages per session | 2 avg | 🔴 ძალიან დაბალი |
| Scroll depth | 55.32% avg | 🟡 საშუალო |
| Active time | 1.5 min | 🔴 7.9 min total-დან 1.5 = 81% inactive |
| Dead clicks | 8 sessions | 🟡 UX issue |
| Rage clicks | 0 | 🟢 |
| Quick backs | 35 sessions (13.8%) | 🔴 landing page problem |
| Excessive scrolling | 0 | 🟢 |

**Top pages by sessions:** Home 187, BiFinance 51, Partners 25, Balance 21, BiRetail 15, BiStock 15

---

### Mailchimp (✅ FACT from CLAUDE.md, owner validated)

| მეტრიკა | Value | შეფასება |
|----------|-------|---------|
| Click rate | 0.37% | 🔴 industry avg ~2.5% |
| Crisp chat | Dormant 5 months | 🔴 dead channel |
| Campaign list | Empty (no recent campaigns visible) | 🔴 |

---

### WordPress / bivision.ge

| მეტრიკა | Value | შეფასება |
|----------|-------|---------|
| Blog posts | 0 educational content | 🔴 მხოლოდ partner success stories |
| Success stories | 20+ partners listed | 🟢 social proof |
| Page load time | 6.20s / 95.1MB | 🔴 ძალიან ნელი |
| JS errors on site | ✅ FACT from CLAUDE.md | 🔴 broken |
| "მოითხოვე დემო" button | ✅ exists | 🟢 CTA present |
| Blog tab | exists but empty | 🔴 no content marketing |
| English version | ❌ none | 🟡 only Georgian |
| Rank Math SEO | ✅ installed | 🟢 tool available |
| Site Kit (Google) | ✅ installed | 🟢 |

**✅ FACT: Page Not Found = 31 views, 70% bounce = broken links driving traffic away.**

---

## 2. SWOT ანალიზი

### STRENGTHS (ძლიერი)
1. **20+ success story page** — social proof არსებობს, პარტნიორების გვერდი 7.5% bounce = ყველაზე ჩართული გვერდი
2. **BiFinance page** — 59 unique users, 31.6% bounce — ყველაზე საინტერესო პროდუქტი visitors-ისთვის
3. **BiHub.ge → bivision.ge referral** — free product-დან paid-ზე funnel მუშაობს (მცირედ)
4. **ბრენდი Google-ში** — "bivision" query-ზე position ≤5.5
5. **HubSpot + Rank Math + Site Kit** — ინფრასტრუქტურა არსებობს
6. **3 active SQL deals** — pipeline ცარიელი არ არის
7. **Net +6 Facebook followers/month** — ბუნებრივი ზრდა (მინიმალური, მაგრამ არსებობს)

### WEAKNESSES (სუსტი)
1. 🟢 **SEO POISONING — RESOLVED.** საიტი გასუფთავებულია. GSC data = ისტორიული, თანდათან გაქრება
2. 🔴 **0% demo conversion** — ✅ FACT from CLAUDE.md. 6 key events/28 days = თითქმის 0
3. ✅ CORRECTED: **LinkedIn ads არ არსებობს.** Digital ad spend = ~69₾/თვე actual (1,037₾/15 months). "950₾/თვე" იყო budget estimate, არა fact.
4. 🔴 **97% new users, 0 returning** — არანაირი retention / remarketing / email nurture
5. 🔴 **Facebook engagement 0.09%** — 35.8K views = 32 interactions. Vanity metrics
6. 🔴 **0 educational content (blog)** — SEO-ს ვერ აშენებ partner stories-ით
7. 🔴 **Site speed 6.2s / 95MB** — Google penalizes slow sites
8. 🟡 **HubSpot pipeline** — ~1,000₾ real avg price (არა placeholder), მაგრამ 3 stale deal + 0 Proposal stage
9. 🔴 **Mailchimp 0.37% click** — email marketing dead
10. 🔴 **Crisp chat dormant 5mo** — customer touchpoint abandoned
11. 🟡 **Real traffic = ~4 users/day** — 140/262 = bots

### OPPORTUNITIES (შესაძლებლობები)
1. **pashagaming cleanup** → Google SEO recovery → organic traffic x2-3
2. **BiFinance landing page optimization** — 59 users/mo, 31.6% bounce — improve = demos
3. **Blog/content marketing** — 0 competition for Georgian BI content, Rank Math installed
4. **BiHub → BiFinance funnel** — free → paid path already working, amplify
5. **Email nurture** — Mailchimp exists, HubSpot contacts exist — just need campaigns
6. **Facebook reels** — 1 reel = 20K+ views. სტრატეგიული content = engagement
7. **WordPress speed optimization** — technical fix, big SEO impact
8. **Partner success stories → case study blog posts** — content already exists, reformat

### THREATS (საფრთხეები)
1. 🟢 ~~Google manual action risk~~ — RESOLVED. საიტი clean, GSC data ისტორიული
2. 🔴 **DataMind AI narrative** — podcast blitz, $700K investment, ტექნოლოგიური ლიდერობა
3. 🔴 **Amadeo BOG partnership + 100₾ pricing** — IV კატეგორიას იჭერს, scale effect
4. 🟡 **Power BI free perception** — ✅ FACT: ოუნერმა თქვა #1 გამოწვევა
5. 🟡 **მარიამის potential exit (მაისი)** — სოციალური აქტივობა = 0 მის გარეშე

---

## 3. Level 4 Minimum Viable System — მარკეტინგი

### LEVEL CHECK: L4 — ეს რეკომენდაცია system-ია, არა "გელა/მარიამი გააკეთე"

### Level 4 Ideal (North Star)
ავტომატური funnel: content → organic traffic → demo request → HubSpot pipeline → ინგას qualification → გელას closing. მარკეტინგი = system, არა 1 ადამიანის ეფორტი.

### Grounded Reality Check
- **ფსიქოლოგიური ბარიერი:** მარიამის motivation დაბალია (2,500₾, role overload). ჩანაცვლება = ადამიანურად რთული
- **რესურსის სიმცირე:** 2,500₾/თვე ბიუჯეტი + 950₾ ads = 3,450₾ სულ. ახალი hire ≈ 3,500-5,000₾
- **ტექნიკური ბერკეტი:** WordPress + Rank Math + HubSpot + Mailchimp + Clarity = ყველა tool უკვე აქვს

### Minimum Viable System — 3 ფაზა

---

#### ფაზა 1: EMERGENCY (კვირა 1-2) — 0₾ additional cost

**1.1 SEO Poisoning — ✅ RESOLVED**
- [x] საიტი აღდგენილი ძველი ვერსიიდან
- [x] კოდიდან წაშლილი
- [x] Security plugin დაყენებული
- [x] დეველოპერები ჩართულნი
- [ ] GSC URL Removal Tool — ძველი spam URL-ების წაშლა (ისტორიული data-ს გაწმენდა)
- [ ] Sitemap resubmit — recrawl trigger
- **ვინ:** მენცარი (GSC cleanup)

**1.2 Broken links fix**
- [ ] Page Not Found (31 views, 70% bounce) — identify broken URLs, setup 301 redirects
- [ ] JS error fix (CLAUDE.md-ში validated)
- **ვინ:** გაბო/დათო (30 წუთი max)

**1.3 Ad spend audit**
- [ ] ✅ CORRECTED: LinkedIn ads არ არსებობს. Digital ad spend = 1,037₾ სულ 15 თვეში (~69₾/თვე)
- [ ] GA4 "linkedin/paid_social" = organic post UTM, არა paid campaign
- [ ] მარკეტინგის ხარჯის 83% = მარიამის ხელფასი (3,189₾/თვე)
- **Level 4:** ad budget allocation system — თუ boost-ს აკეთებ, CPA tracking mandatory

**1.4 HubSpot cleanup**
- [ ] ნუტრიველი (96d expired) → archive ან close lost
- [ ] Connect (37d expired) → გელას 1 follow-up email, მერე archive
- [ ] გრეიდი (37d expired) → გელას 1 follow-up email, მერე archive
- [ ] ევროპული ჰოსპიტალი → გელას follow-up (1 month silence)
- [ ] **ყველა deal-ს real amount** — გელა 10 წუთში ავსებს
- **Level 4:** HubSpot rule: deal > 30 days in stage without activity → auto-alert

---

#### ფაზა 2: FOUNDATION (კვირა 2-4) — minimal cost

**2.1 Content system (0₾ additional)**
- [ ] 4 blog post/month — partner stories reformat → "როგორ გამოიყენა [კომპანია] BiFinance-ი"
- [ ] SEO keywords: "ფინანსური რეპორტინგი", "გაყიდვების ანალიტიკა", "BI საქართველო"
- [ ] ყოველი post = 1 social share (Facebook + LinkedIn organic)
- **ვინ:** მარიამი (ან ჩამნაცვლებელი) + AI-ის დახმარებით. **Template system = Level 4**
- **Template:** Title, Problem, Solution, Result (ციფრით), CTA → demo
- **Level 4 test:** template-ით ნებისმიერმა შეავსოს, არა მხოლოდ მარიამი

**2.2 Email nurture setup (0₾ — Mailchimp free tier)**
- [ ] Welcome sequence: 3 email (company intro → product value → demo CTA)
- [ ] Monthly newsletter: 1 email/month ყველა contact-ისთვის
- [ ] HubSpot contacts → Mailchimp sync
- **Level 4:** automation sequence, არა manual send ყოველ თვეს

**2.3 Facebook content strategy**
- [ ] Reels 2/month (OKR target) — short, educational, BI/data tips
- [ ] Partner testimonial video quotes (15-30 sec)
- [ ] Stop: generic content → Start: educational + case study content
- [ ] 950₾ (LinkedIn-დან) → Facebook boost top-performing posts
- **Level 4:** content calendar template, ყოველ თვეს 8 post pre-scheduled (Canva + Meta Business Suite)

**2.4 Website speed optimization**
- [ ] Image compression (95.1MB → target <20MB)
- [ ] Caching optimization (WP cache plugin)
- [ ] Target: <3s load time
- **ვინ:** გაბო/დათო (2-3 საათი ერთჯერადი)

---

#### ფაზა 3: GROWTH (კვირა 4-8) — მარიამის გადაწყვეტილების შემდეგ

**3.1 Demo funnel optimization**
- [ ] BiFinance dedicated landing page (ახლა generic product page)
- [ ] Demo request form → HubSpot auto-create deal
- [ ] Thank you page → Calendly integration (გელას calendar)
- **Level 4:** visitor → demo request → auto deal → auto calendar invite. გელას involvement = მხოლოდ meeting

**3.2 SEO foundation**
- [ ] 10 target keywords researched (Rank Math + GSC data)
- [ ] 1 pillar page: "რა არის BI?" — full guide, 2000+ words
- [ ] Monthly: 4 blog posts → internal linking → pillar page
- **Level 4:** keyword tracking automated (Rank Math), monthly report auto-generated

**3.3 Competitor monitoring (მენცარი)**
- [ ] DataMind, Amadeo, Dastafe — LinkedIn/Facebook monthly scan
- [ ] Content gap analysis: რას აქვეყნებენ, რას არა
- **Level 4:** web scraping alerts, არა manual checking

---

## 4. მარიამის გადაწყვეტილება — 3 ვარიანტი (ranked)

### ვარიანტი A: მარიამი რჩება + scope შეცვლა (რეკომენდებული)
- Role: content creator only (არა designer, არა email, არა analytics)
- 2,500₾ → შესაბამისი workload
- System: template-based content, AI-assisted, მენცარი monitors
- **რატომ #1:** 0₾ transition cost, continuity, მარიამი იცნობს ბიზნესს
- **რისკი:** motivation არ აიწევს role change-ით

### ვარიანტი B: ჩანაცვლება — AI-first marketer
- Profile: junior, AI-native, 2,000-3,000₾
- System: templates + AI tools + მენცარის oversight
- **რატომ #2:** fresh energy, AI-first approach
- **რისკი:** 1-2 თვე onboarding, content gap

### ვარიანტი C: სრული ავტომატიზაცია (0 marketer)
- მენცარი + AI tools + გელას 2hr/week content review
- Social media: Buffer/Hootsuite auto-schedule
- **რატომ #3:** 0₾ marketing salary, Level 4 purest form
- **რისკი:** 0 ადამიანური touchpoint, visual quality ეცემა, გელას 2hr/week = Level 2

**CFO NOTE:** მარიამის 2,500₾/თვე = 30,000₾/წელი. თუ ეს 30K-მ 1 ახალი client-ი მოიყვანა წელიწადში = ROI+. თუ 0 client = waste. ✅ FACT: 0% demo conversion, 0 qualified leads from digital (CLAUDE.md). **⚠️ INFERENCE (H): ამჟამად ROI ≤ 0.**

**რეკომენდაცია:** ვარიანტი A სცადე 2 თვე (მაისი-ივნისი) ახალი scope-ით + OKR-ებით. ივნისის ბოლოს: OKR met → გააგრძელე. Not met → ვარიანტი B.

---

## 5. KPI Dashboard — Marketing (monthly tracking)

| მეტრიკა | Baseline (Apr 2026) | Target (Jun 2026) | Target (Sep 2026) |
|----------|---------------------|--------------------|--------------------|
| Real organic traffic (Georgian) | ~120 users/mo | 200 | 400 |
| Demo requests | ~0 | 3/mo | 8/mo |
| Blog posts | 0 | 4/mo | 4/mo |
| Email subscribers | ❓ UNKNOWN | 100 | 300 |
| Email click rate | 0.37% | 2% | 3% |
| Facebook engagement/post | ~3-5 | 20 | 35 |
| Facebook reels | 0 | 2/mo | 4/mo |
| HubSpot pipeline value (real) | $0 (placeholder) | real values | growing |
| Site load time | 6.2s | <3s | <2s |
| GSC: non-spam clicks | ~36/3mo | 100/3mo | 300/3mo |
| Digital ad spend | ~69₾/mo actual | strategic allocation | ROI-based |

---

## 6. Owner Rating

[1]ვიცოდი [2]საინტერესო/არა-actionable [3]ახალი+actionable [4]game-changer [skip]

---

*Last updated: 2026-04-06 | Source: Playwright data extraction*
