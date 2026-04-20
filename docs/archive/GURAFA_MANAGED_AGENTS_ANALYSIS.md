---
class: CRITICAL — C-Suite architecture decision
from: gurafa
to: owner
type: deep analysis — Claude Managed Agents impact on Bivision C-Suite
created: 2026-04-09
language: English (strategic doc)
---

# Claude Managed Agents — What This Means for Our C-Suite

> Released: April 8, 2026 (yesterday). Public beta. This changes everything.

---

## What It Is (Simple)

Until now: we run 3 separate Claude Code sessions (მენცარი, ვიქტორი, გურაფა), communicate via docs/ files, manually trigger audits.

**Managed Agents:** Anthropic runs your agents in the cloud. You define what each agent does, give it tools, and it runs autonomously. No local machine needed. No session management. No docs/ file passing.

---

## How It Maps to Our C-Suite

| Our current setup | Managed Agents equivalent |
|-------------------|--------------------------|
| 3 Claude Code sessions on your PC | 3 cloud-hosted Agents (always running) |
| docs/ files for communication | Direct API events between agents |
| Manual AUDIT_REQUEST.md | Automated event: output → trigger audit agent |
| Owner starts sessions | Agents run on schedule, owner monitors |
| CLAUDE.md loaded each time | Agent definition: model + system prompt + tools (persistent) |
| Memory resets each session | **Memory (research preview)** — persists across sessions |
| No multi-agent coordination | **Multi-agent (research preview)** — agents spin up sub-agents |

### Our 3 Agents as Managed Agents:

```python
# Agent 1: მენცარი (CEO)
mentari = client.beta.agents.create(
    name="Mentari - Bivision CEO",
    model="claude-sonnet-4-6",  # Sonnet for cost efficiency
    system=open("BI_C-Suite/CLAUDE.md").read(),
    tools=[
        {"type": "agent_toolset_20260401"},  # bash, files, web
        {"type": "mcp", "server": "hubspot-mcp"},  # HubSpot direct!
    ],
)

# Agent 2: ვიქტორი (Auditor)
victor = client.beta.agents.create(
    name="Victor - Auditor",
    model="claude-sonnet-4-6",
    system=open("Mentari_Virtual-C-Suite/CLAUDE.md").read(),
    tools=[{"type": "agent_toolset_20260401"}],
)

# Agent 3: გურაფა (Intelligence + Coach)
gurafa = client.beta.agents.create(
    name="Gurafa - Intelligence & Coach", 
    model="claude-opus-4-6",  # Opus for depth
    system=open("BI_gurafa/CLAUDE.md").read(),
    tools=[
        {"type": "agent_toolset_20260401"},
        {"type": "web_search"},
    ],
)
```

---

## Game Changers for Us

### 1. No More docs/ File Passing

Current: მენცარი writes AUDIT_REQUEST.md → ვიქტორი reads next session → writes AUDIT_FEEDBACK.md → გურაფა reads.

**Managed Agents:** მენცარი finishes output → API event triggers ვიქტორი session → ვიქტორი audits → event triggers გურაფა if needed. **Real-time, not file-based.**

### 2. HubSpot MCP Integration

Current: მენცარი has no HubSpot access. Biggest blind spot.

**Managed Agents + MCP:** Connect HubSpot MCP server → მენცარი reads pipeline, leads, deals directly. **Pipeline First protocol = automated.**

```python
# მენცარი wakes up at 9:00, checks HubSpot
session = client.beta.sessions.create(
    agent=mentari.id,
    environment_id=env.id,
)
client.beta.sessions.events.send(session.id, events=[{
    "type": "user.message",
    "content": [{"type": "text", "text": "Morning check: HubSpot pipeline status, overdue follow-ups, new leads. Report to owner."}]
}])
```

### 3. Always Running (Not Session-Dependent)

Current: agents only work when owner opens Claude Code.

**Managed Agents:** agents run in cloud containers. Owner sleeps → agents work. **24/7 capability.**

Cost: $0.08/hr runtime = ~$58/month for 24/7 single agent. But agents don't need 24/7 — scheduled runs:
- მენცარი: 2 hrs/day active = ~$5/month runtime
- ვიქტორი: 1 hr/day = ~$2.50/month
- გურაფა: 1 hr/day = ~$2.50/month
- **Total runtime: ~$10/month** + token costs

### 4. Multi-Agent Coordination (Research Preview)

Current: agents can't talk to each other directly.

**Research preview:** agents spin up sub-agents. მენცარი can spawn ვიქტორი to audit, wait for result, continue. **This is exactly our architecture vision.**

⚠️ Research preview = not public yet. Need to request access.

### 5. Memory Across Sessions (Research Preview)

Current: every new session = cold start + CLAUDE.md reload.

**Research preview:** agent remembers previous sessions. მენცარი knows what happened yesterday without re-reading OUTPUT_LOG.md.

⚠️ Also research preview.

---

## Cost Analysis — Bivision Specific

| Component | Current ($100 Max plan) | Managed Agents |
|-----------|------------------------|----------------|
| Subscription | $100/mo flat | $0 (API only) |
| Token costs | included in $100 | Sonnet: ~$50-80/mo (3 agents) |
| Runtime | included | ~$10/mo |
| Web search | included | $10/1000 searches |
| **Total** | **$100/mo** | **~$70-100/mo** |

**Similar cost, fundamentally different capability.** Cloud-hosted, always available, inter-agent communication, HubSpot integration.

### Or Hybrid:

Keep Max $100 for owner's personal Claude Code/Cowork. Add Managed Agents for the 3 C-Suite agents.
- Max plan: $100/mo (owner)
- Managed Agents: ~$70-100/mo (3 agents)
- **Total: ~$170-200/mo** — but system runs without owner

---

## What This Means for C-Suite as a Product

**This is the product infrastructure we were missing.**

Before: "C-Suite as a Service" = concept. How do we deploy for customers? Each customer runs Claude Code on their PC? That's not a product.

**Now:** Each customer gets 3 Managed Agents via API. Hosted by Anthropic. Customer connects their HubSpot/CRM via MCP. Agents run. Customer monitors via dashboard.

```
C-Suite as a Service = 
  3 Managed Agents (CEO, Auditor, Coach)
  + Customer's MCP connections (HubSpot, Qlik, etc.)
  + Dashboard (we build)
  + CLAUDE.md templates (we provide)
  
Customer cost: ~$70-100/mo API
Our revenue: setup fee + monthly support + dashboard license
```

**This is deployable. This is scalable. This is a real product.**

---

## Honest Limitations

| Limitation | Impact | Workaround |
|-----------|--------|-----------|
| Multi-agent = research preview | Can't use today | Request access, use docs/ pipeline until then |
| Memory = research preview | Sessions still cold-start | CLAUDE.md + explicit context passing |
| $0.08/hr runtime adds up | 24/7 = $58/agent/month | Scheduled runs, not always-on |
| API key required | No subscription plan | Already have API access via Max plan |
| Beta = bugs expected | Production risk | Test on non-critical tasks first |
| Vendor lock-in | Anthropic only | Accept for now, Cline = product backup (previous analysis) |

---

## Recommendation

### Phase 1 (This Week): Request Access + Test

1. **Request multi-agent research preview:** [claude.com/form/claude-managed-agents](https://claude.com/form/claude-managed-agents)
2. **Create 1 test agent** (მენცარი) with basic tools
3. **Test:** daily HubSpot check + brief generation
4. **Cost:** $0 (free beta exploration) + token costs

### Phase 2 (Week 2-3): Migrate C-Suite

1. Define all 3 agents via API
2. Set up environments with MCP (HubSpot, web)
3. Replace docs/ pipeline with event-based communication
4. iPhone monitoring via API dashboard

### Phase 3 (Month 2+): Product

1. Template agent definitions for other companies
2. Dashboard as product frontend
3. MCP connector library (HubSpot, Qlik, Power BI)
4. Pricing model for C-Suite as a Service

---

## vs Claude Code vs Cline (Updated)

| | Claude Code | Cline | **Managed Agents** |
|--|-----------|-------|-------------------|
| Runs on | Your PC | Your PC (VS Code) | **Cloud** |
| Always available | No (session) | No (session) | **Yes** |
| Multi-agent | Agent Teams | Basic sub-agents | **Native (preview)** |
| Memory | Per-session | Per-session | **Cross-session (preview)** |
| MCP | Yes | Yes | **Yes** |
| Cost | $100/mo flat | $0 + API | **$0 + API + $0.08/hr** |
| Product-ready | No | Open source | **Yes — API-first** |
| C-Suite fit | Good (current) | Backup | **Best (future)** |

**Updated verdict:** Claude Code = now. Managed Agents = next. Cline = product backup.

---

## One Sentence

**Managed Agents = C-Suite stops being a concept and becomes a deployable product.**

---

Sources:
- [Claude Managed Agents Overview](https://platform.claude.com/docs/en/managed-agents/overview)
- [Quickstart Guide](https://platform.claude.com/docs/en/managed-agents/quickstart)
- [Blog Announcement](https://claude.com/blog/claude-managed-agents)
- [Pricing: $0.08/session-hour](https://findskill.ai/blog/claude-managed-agents-explained/)

---

*Gurafa | 2026-04-09 | CRITICAL — this is the infrastructure for our product*
