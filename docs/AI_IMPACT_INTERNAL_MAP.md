---
from: mentari
to: owner
type: ⚠️ REC — AI Impact on Bivision, internal threat/opportunity map
ep0: 7/10 (S)
tier: spot-check
status: Ready · v1 complete 2026-04-19 · Layers 1-5 populated + interview data integrated
created: 2026-04-15
scope: internal-only (no competitor/market layer — deferred to Gurafa wave, enhancer not blocker)
audit: docs/AUDIT_REQUEST.md (filed at completion, Viktor post-factum)
canonical-status: canonical (AI Impact internal map). References: docs/EXECUTION_PLAN_V3.md §AI Impact scope, docs/MARKETING_AI_PLAN.md (adjacent, marketing automation focus).
---

# AI Impact on Bivision — Internal Threat & Opportunity Map

## Why this, why now

- ✅ FACT: competitors built AI narrative (DataMind AI-first, Amadeo scale play, Dastafe Power BI + AI WhatsApp assistant) — source: `docs/STATUS.md` row 4
- ✅ FACT: Bivision AI narrative = 0, AI product feature = 0, AI content = 0 — source: `docs/MARKETING_AI_PLAN.md`
- ⚠️ INFERENCE (H): 6-12 month window before AI reshapes BI delivery economics. Cost of inaction = margin compression + DIY client defection.

Scope: internal-only. Gets 70% of decision-usefulness without waiting on competitor/market layer.

---

## Layer 1 — Threat: AI replaces what Bivision sells

**Sharp hypothesis:** Bivision's 8 products split into 3 tiers by LLM-replaceability. The **dashboard surface of every product** is LLM-compressible once clean data exists. The **Georgian ERP connector layer** is not. Revenue is extracted via the combined package, so the moat holds only as long as clients don't separate the two.

### Product classification (source: BIVISION_CONTEXT.md §3, §5)

| Product | Moat-protected component | Compressible component | Tier |
|---|---|---|---|
| BiFinance | Fina/Oris/Balance/1C connectors + consolidation + accounting rules | P&L / Cash Flow / Balance Sheet viz | **Moat-strong** |
| BiRetail | ERP integration + SKU-level data pipeline | Sales analytics dashboards | **Moat-strong** |
| BiStock | ERP integration + stock reconciliation | Inventory dashboards | **Moat-strong** |
| BiDebitors | ERP integration | Receivables dashboards | **Moat-strong** |
| BiMedical | HIS connector + hospital-specific schema | Hospital dashboard surface | **Moat-medium** (narrower market, specialized) |
| BiAudit | Audit framework + Georgian compliance domain | Audit output surface | **Moat-medium** (domain, not integration) |
| Retail Info | Scraper maintenance + cross-source nomenclature matching | Price comparison output | **Moat-weak** (scraping degrades, LLM+browser automation closes gap) |
| BiHub | — (free) | Everything | **No moat** (loss-leader by design) |

### What this says

- **6 of 8 products sit on Georgian ERP integration moat.** This is real, not marketing. DataMind's "Unistream universal connector" (STATUS.md row 4) is the direct threat — if they crack Fina/Oris/Balance/1C, moat erodes.
- **Dashboard surface alone = compressible.** Once a client has clean integrated data, LLM + Qlik Answers reproduces most visualizations in hours, not weeks.
- **Revenue extraction depends on bundled delivery.** If a client separates "integration" (pay Bivision) from "dashboarding" (DIY with LLM), Bivision loses 40-60% of project value. ⚠️ INFERENCE (H) — split estimate needs Layer 3 hours breakdown to confirm.

### What's uncertain (needs owner input to sharpen)

- Actual % of billable hours by phase (integration vs dashboarding vs training) — 1h owner/Inga workshop
- Competitor ERP connector progress (DataMind Unistream coverage of Georgian ERPs) — Gurafa task, not blocking
- Qlik Answers capability on Georgian data — 30min internal test

---

## Layer 2 — Threat: clients build DIY with LLM

**Sharp hypothesis:** DIY-LLM is NOT Bivision's near-term churn driver. Ecosystem decisions (TBC-style Power BI migration) and champion departure are. The DIY threat is a 12–24 month horizon risk that emerges when client-side analyst + LLM fluency reaches the level where a mid-tier employee can reproduce a dashboard in a weekend.

### Account classification (source: BIVISION_CONTEXT.md §7, §9, §11, §15 + OUTPUT_LOG.md Apr 5)

| Tier | Pattern | Named accounts | Count | Near-term DIY risk |
|---|---|---|---|---|
| A. Exiting / structural | Ecosystem or company-level decision | TBC Pay (exits Jun-26), TBC Leasing (likely follows), Reffix (ends Mar-26) | 2–3 | N/A — already leaving |
| B. Champion-dependent flagged | Low usage OR CFO/champion risk | Nutrimax/SmartAgro, Mardaleishvili | 2 | HIGH — but cause is champion, not DIY-LLM |
| C. Moat-protected (active ERP integration) | BiFinance/BiRetail/BiStock + connector work | IG Development, ICR Trade, Aversi Pharma, Orbita, Engadi, NRG Holding, GCT, MMC, Geocord, არსი | ~10 | LOW — tether structural |
| D. RO / service-based | Staff augmentation, not product replacement | Fortune Jack (RO), BOG (RO queue analytics), NGT Group (internal) | 3 | VERY LOW — not dashboard-substitutable |
| E. License-only / perpetual | No ongoing delivery relationship | Chirina, SuperStore, Leaderbet, Fortune Jack (license), DGA, GNERC | ~6 | N/A — no recurring engagement to compress |

**Coverage:** ~24 of 29 named from disk sources. 5 accounts unknown/unnamed in current context.

### What this says

- **~3 near-term at-risk** (Tier B + ambiguous Tier A). None driven by DIY-LLM — all driven by ecosystem shifts or champion dynamics.
- **~10 structurally tethered** (Tier C). Moat holds as long as Georgian ERP connector advantage holds (see Layer 1, DataMind Unistream threat).
- **~9 service/license relationships** (Tier D + E) that aren't DIY-LLM substitutable in the same sense.
- **Owner directive reversal check:** "არსებულებზე ნაკლები რესურსი, მთავარი აქცენტი ახალი ლიდები" (NEW_LEADS_STRATEGY Apr 8) is sound on the Tier C/D/E base (stable-ish). But Tier B (2 accounts, ~85K₾/year combined) is the cheapest retention dollar per revenue defended.

### What's uncertain

- 5 of 29 accounts unidentified in current disk context — full client list needed from Billings 2026 tab of Google Sheet (§16)
- Tier B "champion risk" classification uses Apr 5 data — may have shifted if owner has called these clients since
- DIY-LLM timeline (12 vs 24 months) is a range, not a forecast — depends on Georgian market LLM adoption rate (Gurafa layer)

---

## Layer 3 — Opportunity: compress our own delivery

**Sharp hypothesis:** AI compression is UNEVEN — highest on dashboard authoring / training / support (40–60%), lowest on ERP connector work (5–15%). This paradoxically defends Bivision's moat: AI accelerates our non-moat work (commodity surface) more than it threatens our moat work (Georgian ERP integration). Net effect = margin lift without moat erosion, if we invest the reclaimed hours into product tier (Layer 4) rather than price cuts.

### Phase-by-phase compression (source: BIVISION_CONTEXT.md §4 contract model + §7 team workload + session Apr 10–14 evidence)

| Phase | LLM leverage | Compression | Rationale |
|---|---|---|---|
| Discovery / requirements | Call summarization, auto-spec draft | 20–30% | Bounded by client conversation pace, not AI |
| ERP connector setup | Auth, schema work | 5–15% | Structural data work — LLM helps with SQL/mapping scaffolds only |
| Data model + transformations | SQL / DAX generation assist | 30–40% | Strong LLM zone, but validation still human |
| Dashboard / report authoring | LLM + screenshot → viz code | 40–60% | Highest AI leverage — template → production fast |
| Testing / QA | Edge case generation | 20–30% | LLM weak on domain-specific acceptance criteria |
| Training / handoff | LLM-drafted runbooks, FAQs | 50%+ | Content generation = LLM native |
| Ongoing support / change management | LLM-assisted ticket + spec drafts | 30–40% | Repetitive patterns across 29 accounts |

**Composite estimate:** 25–35% delivery cost compression at constant quality. ⚠️ INFERENCE (M) — needs actual phase hour allocation to refine.

### Anchor evidence

✅ FACT (session Apr 10–14): Playwright + Claude extraction replaced ~8h manual data pull with 45min = 90% compression in that specific task. Not representative of whole project (extraction is one narrow task), but proves the upper bound is real, not theoretical.

### What this says

- **Capacity unlock > cost cut.** If Inga (18 accounts) + Davit (21 accounts) each save 25–35% on support/change work, that's 1 additional senior FTE worth of capacity without a hire. ⚠️ INFERENCE (M).
- **Where to spend reclaimed hours:** build Layer 4 product tier (NL-query add-on) with the same team. Not: cut prices, not: take on more RO work.
- **Margin math (rough):** at 647K salary + 25% delivery compression on the ~60% of time spent in delivery (vs admin/sales), net salary-adjusted margin lift ≈ 10–15% of revenue = 95–140K₾/year. ⚠️ INFERENCE (L) — crude, needs real hour allocation.

### What's uncertain

- Actual phase hour allocation per project type (RO vs SaaS vs Reselling) — 1h owner/Inga workshop
- Whether reclaimed hours reinvest into product (Layer 4) vs absorb into sales activity — owner strategic choice
- Quality floor: how much compression before client-perceived quality drops? ❓ UNKNOWN until measured on one pilot project

---

## Layer 4 — Opportunity: AI-wrapped product tier

**Hypothesis:** "Ask your data" natural-language layer on top of BiFinance = add-on SKU, incremental revenue at low marginal cost.

### Candidate productized features

| Feature | Complexity | Pricing | Blocker |
|---|---|---|---|
| NL-query on existing dashboards | Medium | +170-255₾/mo (20-30% of 850₾ base) | Qlik MCP Georgian validation |
| Auto-anomaly commentary (weekly email) | Low | bundled or +85₾ | template + 1 pilot |
| Forecasting module (LLM + time-series) | High | separate SKU | dev capacity |
| Voice interface (Georgian) | Very high | pilot only | tech maturity |

### Pilot status

- ✅ FACT: Qlik MCP + Claude IG pilot approved (STATUS.md row 11)
- ⚠️ INFERENCE (M): Qlik MCP Georgian language coverage = ❓ UNKNOWN. გაბო: "ქლიქში ვერ ვიყენებ AI-ს, არ იცის ქლიქის ენა კარგად" (interview Apr 8). ეს validation gap-ია — NL-query add-on-ის პროდუქტიზაცია ვერ მოხდება სანამ ქართულ data-ზე ტესტი არ ჩატარდება.
- ✅ FACT: გაბოს 6-თვიანი tech risk = "გადაწყვეტილებების კონკურენტულობის დაკარგვა" — ეს ადასტურებს Layer 1 thesis-ს შიგნიდან.

### Recommended first launch

NL-query add-on, 170-255₾/თვე. 3 ნაბიჯი:
1. Qlik MCP + ქართული data ტესტი (გაბო, 1 დღე)
2. IG pilot-ზე 2-კვირიანი beta
3. თუ მუშაობს → BiFinance add-on pricing + 2 client rollout

### რა ვიცით გუნდიდან

- **გაბო:** "კონკურენტულობის დაკარგვა" = #1 risk. AI-ს იყენებს ყოველდღე coding-ში. Qlik-ში AI-ის ინტეგრაცია = ენობრივი ბარიერი.
- **ინგა:** AI daily user (Excel, coding, docs). ბუნებრივი AI integration lead.
- **მარიამი:** AI-ს ვიდეო content-ში გამოიყენებდა პირველ რიგში.

---

## Layer 5 — Capability gap: internal team AI fluency

**Hypothesis:** Sustained AI leverage requires team-wide fluency, not just owner + a few power-users.

### რა ვიცით (interview data, Apr 7-8)

| ადამიანი | AI usage | fluency level | gap |
|---|---|---|---|
| **გელა (owner)** | Claude Code daily, C-Suite project driver | High | არა fluency, არამედ delegation |
| **გაბო (CTO)** | AI coding daily, მაგრამ "Qlik ენას არ იცის" | Medium-High | Qlik-AI integration gap |
| **ინგა** | AI daily: Excel, coding, docs | Medium-High | არ აქვს დრო strategic AI use-ისთვის (ops overload) |
| **მარიამი** | AI = ვიდეო content-ისთვის გამოიყენებდა | Low-Medium | tool access ❓, training needed |
| **მარი მაღლ** | ❓ UNKNOWN | ❓ | interview pending |
| **მარი მიკ** | ❓ UNKNOWN | ❓ | interview pending |
| **ლუკა** | ❓ UNKNOWN (junior, AI-native generation hypothesis) | ❓ | interview pending |

### რა ჩანს

1. **Top tier (გელა, გაბო, ინგა):** AI-ს იყენებენ, მაგრამ tactical level-ზე (coding assist, doc writing). Strategic AI use (product tier, client-facing AI) = 0.
2. **Gap:** 3/7 ❓ UNKNOWN — skills audit incomplete.
3. **Blocker:** ინგა + გაბო = ops overload. AI fluency-ს ვერ იყენებენ strategic capacity-ად რადგან ყოველდღიურობამ ჩაჭამა (interview confirmed).

### Action

Skills audit form (TEAM_AI_SKILLS_AUDIT.md) 3 pending ადამიანისთვის ⊂ V3 კითხვარის ნაწილი (Q6: "AI გიცდია სამუშაოში ან პირადად?"). ცალკე form არ სჭირდება — V3 კითხვარის პასუხებიდან ამოვა.

---

## Deferred to Gurafa wave (not blocking this map)

- Layer 6: competitor AI moves (beyond baseline `STATUS.md` row 4)
- Layer 7: Georgia AI adoption rate, B2B market timing
- Layer 8: global BI+AI vendor moves (Microsoft Fabric, Qlik Staige etc.)

These arrive as enhancer signals for Layers 1–5 projections.

---

## Synthesis — რა ამბობს 5 ფენა ერთად

**ერთი მთავარი დასკვნა:** ბივიჟენის moat = ქართული ERP კონექტორები. Dashboard surface = compressible. სტრატეგია = ERP+AI positioning, არა "AI BI" (DataMind-ის ტერიტორია).

**კონკრეტულად:**

1. **Moat = integrations.** 6/8 პროდუქტი ERP integration-ზე დგას. DataMind Unistream = პირდაპირი საფრთხე ამ moat-ისთვის. ✅ FACT.

2. **Compression = margin lift.** 25-35% delivery cost compression ⚠️ INFERENCE (M). ეს = ~95-140K₾/წელი ⚠️ INFERENCE (L). რეალური ციფრი owner/ინგას phase hour data-ს ელოდება.

3. **Product tier = NL-query add-on.** პირველი AI product. 170-255₾/თვე. Blocker: Qlik MCP ქართული ტესტი (გაბო, 1 დღე). გაბო თავად ამბობს ენობრივი ბარიერი არსებობს.

4. **გუნდი = tactical AI users.** ტოპ 3 (გელა, გაბო, ინგა) AI-ს იყენებს, მაგრამ ops overload-ის გამო strategic AI use = 0. 3/7 interview pending.

5. **Near-term risk ≠ DIY.** 3 at-risk account = champion/ecosystem, არა AI-DIY. 10 account = moat-protected. DIY horizon = 12-24 თვე.

---

## Owner decisions (3)

1. **Qlik MCP ქართული ტესტი** — გაბოს 1 დღე დასჭირდება. ანიჭებ?
2. **Phase hour data** — შენი ან ინგას 1 საათი. Compression estimate-ს ამყარებს.
3. **NL-query add-on pricing** — 170-255₾/თვე მისაღებია? IG pilot-ზე ტესტი?

---

## სტატუსი
**Ready** — v1. Layers 1-5 populated. Interview data integrated (ინგა, გაბო, მარიამი). 3 owner decisions pending.

## ფაილი
`docs/AI_IMPACT_INTERNAL_MAP.md`

## ოპერაციული შენიშვნა
ვიქტორის spot-check AUDIT_REQUEST.md-ში ემატება. 3 interview pending (მარი მაღლ, მარი მიკ, ლუკა) — Layer 5 ამით გაძლიერდება, მაგრამ v1 blocking არ არის.
