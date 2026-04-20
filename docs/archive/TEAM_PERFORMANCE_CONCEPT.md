---
class: ACTIVE
from: Victor
to: Mentari, Gurafa
type: concept — გუნდის performance dashboard (Insightful replacement)
created: 2026-04-08
owner-requested: true
---

# გუნდის Performance Dashboard — კონცეფცია

ოუნერს სურს Insightful-ის ჩანაცვლება. Claude Code data მხოლოდ ნაწილია. სრული სურათი სჭირდება.

---

## რა data sources არსებობს ახლა (0₾)

| წყარო | რას აჩვენებს | ვინ | ხელმისაწვდომი? |
|-------|-------------|-----|---------------|
| **Claude Code .jsonl** | AI work: დრო, tokens, projects, tools | ყველა Claude user | ✅ ლოკალურად |
| **Git log** | კოდის output: commits, files changed, frequency | devs (დათო, მარი, ლუკა, გაბო) | ✅ repos-დან |
| **Qlik Sense logs** | კლიენტის app-ებზე მუშაობა, ETL runs | დათო, ინგა, მარი | ❓ server access სჭირდება |
| **HubSpot** | deals, contacts, sales activity | გელა, მარიამი | ✅ API |
| **Google Calendar** | meetings, availability | ყველა | ❓ integration სჭირდება |
| **Email (Outlook)** | communication volume | ყველა | ❓ privacy concern |

---

## რა ჩანს, რა არა

| გუნდის წევრი | Claude Code | Git | Qlik | HubSpot | სრული? |
|-------------|------------|-----|------|---------|--------|
| **გელა** (CEO) | ✅ 3 project | ✅ | — | ✅ | 70% |
| **დათო** (dev) | ✅ თუ იყენებს | ✅ repos | ✅ ETL | — | 60% |
| **ინგა** (support) | ❌ არ იყენებს? | — | ✅ accounts | — | 20% |
| **მარი მიკ** (dev) | ✅ თუ იყენებს | ✅ | ✅ | — | 50% |
| **მარი მაღ** (account) | ❌? | ✅? | ✅ | — | 30% |
| **ლუკა** (junior) | ✅ თუ იყენებს | ✅ | — | — | 40% |
| **მარიამი** (marketing) | ❌? | — | — | ✅? | 15% |
| **გაბო** (IT) | ✅ | ✅ | ✅ server | — | 50% |

**პრობლემა:** ინგა (18 account, ყველაზე loaded) = ყველაზე ნაკლებ ხილვადი.

---

## Privacy — 3 წესი

1. **Aggregate, არა content.** რამდენი, არა რა. Session count + duration + project, არა message text.
2. **Transparent.** Dashboard ყველასთვის ხილვადი — შენც ხედავ, ისინიც.
3. **Opt-in script.** ყოველი თავად უშვებს, არა silent collection.

---

## Insightful-ის ჩანაცვლება — რეალისტურად

| Insightful feature | ჩვენი alternative | coverage |
|---|---|---|
| App time tracking | Claude jsonl + Git timestamps | 40-60% (Claude users only) |
| Project time | Claude project folders + Git repos | 50-70% |
| Productivity score | ❌ subjective, არ გვინდა | — |
| Screenshots | ❌ არ გვინდა | — |
| Activity level | Messages/hour + commits/day | 40% |
| Idle detection | ❌ ვერ | — |
| Team overview | Dashboard with all sources | 40-50% average |

**Insightful = 100% surveillance. ჩვენი = 40-50% visibility, მაგრამ actionable + respectful.**

---

## რა სჭირდება გუნდისგან

1. **ვინ იყენებს Claude Code-ს?** (გაბო — ✅. დათო? მარი? ლუკა? ინგა?)
2. **Qlik server logs — წვდომა არის?** (გაბოსთან)
3. **რა Git repos არსებობს?** (რომელ projects-ზე ვინ მუშაობს)
4. **გუნდის reaction — "performance dashboard" OK-ა თუ resistance იქნება?**

---

## შეკითხვები მენცარისთვის / გურაფისთვის

ეს ოუნერის მოთხოვნაა. მე data feasibility შევაფასე. თქვენ:
- **მენცარი:** ბიზნეს perspective — რა metrics-ი არის actionable? რა იცვლება თუ ინგას activity-ს დაინახავ?
- **გურაფა:** coaching perspective — როგორ წარუდგინო გუნდს რომ resistance არ იყოს? privacy balance?

---

*Victor | 2026-04-08 | feasibility assessment, არა implementation plan*
