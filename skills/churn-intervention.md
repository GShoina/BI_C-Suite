---
name: churn-intervention
description: at-risk client intervention — data → script → call → save
tools: [WebSearch, WebFetch, Read, Write, Grep]
---

# Churn Intervention Skill

## Pipeline
```
1. IDENTIFY: at-risk signals (usage drop, no contact, champion left)
2. RESEARCH: client context (contract, revenue, history, champion)
3. SCRIPT: call script for ოუნერი (1 page, 3 questions, if/then)
4. PREP: contact info, talking points, follow-up template
5. HAND OFF: ოუნერი calls
6. FOLLOW UP: result → update portfolio risk map
```

## Call Script Template
```
ვის ურეკავს: [name, role — არა generic "კომპანია"]
მიზანი: [1 sentence]
Opener: [warm, არა sales]
3 კითხვა:
  1. [service quality check]
  2. [usage/team stability]  
  3. [active usage confirmation]
If negative → [save offer / intervention]
If positive → [renewal conversation]
Follow-up: [email draft, 24სთ-ში]
```

## GCT Rule
კლიენტის სტატუსზე ყოველი statement → data source required.
"კლიენტი აქტიურია" = სად წერია? Qlik usage? ინგას info? contract date?
ASSUMPTION without source = FAIL.

## Priority: revenue × risk
42K₾ at-risk > 10K₾ at-risk. ყოველთვის.
