---
name: execution-pipeline
description: task → script → deploy pipeline. Analysis-დან action-მდე.
tools: [WebSearch, WebFetch, Read, Write, Grep, Glob, Bash]
---

# Execution Pipeline Skill

## წესი #1: ყოველი output = deliverable, არა analysis

## Output Types (prioritized)
1. **Call script** — ვის, 3 კითხვა, if/then, 1 გვერდი max
2. **Contact ID** — სახელი + თანამდებობა + LinkedIn + email
3. **Draft** — pricing, email, message, proposal — copy-paste ready
4. **Deploy spec** — developer-ისთვის: რა შეიცვალოს, სად, როგორ
5. **Analysis** — მხოლოდ როცა 1-4 შეუძლებელია data-ს გარეშე

## Self-Challenge (ყოველი output-ის ბოლოში)
```
## Self-Challenge
ყველაზე სუსტი assumption: [რა]
Source: [URL/file/date]
რა შეიძლება ცდომიერი: [რა]
Replicable?: [yes/no — C-Suite as Product pattern?]
```

## Anti-Patterns (აკრძალულია)
- ❌ Analysis რომელიც deliverable-ით არ მთავრდება
- ❌ "ოუნერმა დარეკოს" script-ის გარეშე
- ❌ 8 parallel task, 0 done-to-impact
- ❌ Framework doc execution-ის ნაცვლად
- ❌ ვიქტორის/გურაფას task breakdown-ის ლოდინი

## Daily Output Standard
minimum 1 deliverable/დღე (type 1-4). analysis = bonus, არა substitute.
