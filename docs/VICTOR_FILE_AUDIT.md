---
class: URGENT
from: mentari
to: victor
type: TASK — ფაილების და არქიტექტურის audit + optimization
created: 2026-04-09
owner-requested: true
---

# ფაილების Audit + Optimization

ოუნერის დავალება: არსებული ფაილები და არქიტექტურა — რაც წასაშლელია წაშალე, რაც დასაოპტიმიზებელია დააოპტიმიზე. token-wise და space-wise.

## რა სჭირდება

1. **docs/ ფოლდერის audit** — რამდენი ფაილია, რამდენი outdated, რამდენი duplicate
2. **წასაშლელი** — outdated versions (v1, v2 თუ v3 არის), duplicate info, ძველი specs რომლებიც შესრულდა
3. **გასაერთიანებელი** — მსგავსი თემის ფაილები ერთ ფაილში
4. **token optimization** — CLAUDE.md, BIVISION_CONTEXT.md — ზედმეტი ტექსტი, redundancy
5. **space** — .playwright-mcp/ logs და snapshots — ძველი წასაშლელია
6. **არქიტექტურა** — docs/ სტრუქტურა ლოგიკურია? naming convention?

## მენცარი + ვიქტორი ერთად

ვიქტორი: audit + რეკომენდაციები
მენცარი: execution (წაშლა, merge, optimization)

---

*მენცარი | 2026-04-09 | ოუნერის request*
