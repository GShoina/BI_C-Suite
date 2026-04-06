# Claude Code — სერვერზე ინსტალაციის ინსტრუქცია

**გამგზავნი:** გელა შონია, Bivision
**მიმღები:** IT ადმინისტრატორი
**თარიღი:** 2026-04-06

---

გამარჯობა,

გთხოვთ Qlik სერვერზე დააინსტალიროთ Claude Code (Anthropic-ის AI CLI ინსტრუმენტი). ქვემოთ დეტალური ინსტრუქციაა.

---

## რა არის Claude Code

CLI (command-line) ინსტრუმენტი რომელიც Anthropic-ის AI API-ს იყენებს კოდის ანალიზის, ფაილების დამუშავებისა და ავტომატიზაციისთვის. ინსტრუმენტი მსუბუქია (~200MB), ძირითადი გამოთვლები Anthropic-ის cloud-ში ხდება.

---

## 1. სისტემური მოთხოვნები

| კომპონენტი | მოთხოვნა |
|-----------|---------|
| OS | Windows Server 2019+ (WSL2 საჭიროა) |
| Node.js | v20.x LTS |
| RAM | min 4 GB თავისუფალი |
| Disk | ~200 MB |
| ქსელი | outbound HTTPS (api.anthropic.com:443) |

---

## 2. ინსტალაციის ნაბიჯები

### ნაბიჯი 1: WSL2 ინსტალაცია (თუ არ არის)

PowerShell-ში (ადმინისტრატორის უფლებებით):
```powershell
wsl --install -d Ubuntu-22.04
```
სერვერის restart საჭიროა.

### ნაბიჯი 2: Node.js ინსტალაცია (WSL-ში)

WSL Ubuntu terminal-ში:
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
node --version   # v20.x უნდა აჩვენოს
```

### ნაბიჯი 3: Claude Code ინსტალაცია

```bash
npm install -g @anthropic-ai/claude-code
claude --version   # ვერსია უნდა გამოჩნდეს
```

### ნაბიჯი 4: API Key კონფიგურაცია

API key-ს მე მოგაწვდით ცალკე. ჩაწერეთ:
```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-KEY_HERE"' >> ~/.bashrc
source ~/.bashrc
```

### ნაბიჯი 5: ტესტი

```bash
claude -p "Hello, confirm you are working"
```
თუ პასუხი მოვიდა — მუშაობს.

---

## 3. Docker კონტეინერი (რეკომენდებული)

უკეთესი იზოლაციისთვის Docker-ში გაშვება სასურველია.

### Dockerfile შექმენით:

ფაილი: `/opt/claude-code/Dockerfile`
```dockerfile
FROM node:20-slim

RUN npm install -g @anthropic-ai/claude-code

RUN useradd -m -s /bin/bash claudeuser
USER claudeuser
WORKDIR /home/claudeuser/workspace

ENV ANTHROPIC_API_KEY=""

ENTRYPOINT ["claude"]
```

### docker-compose.yml:

ფაილი: `/opt/claude-code/docker-compose.yml`
```yaml
version: "3.8"

services:
  claude-code:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: claude-code
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    volumes:
      - ./workspace:/home/claudeuser/workspace
    deploy:
      resources:
        limits:
          memory: 2G
          cpus: "2.0"
```

### გაშვება:

```bash
cd /opt/claude-code
docker compose build
docker compose run --rm claude-code
```

---

## 4. ⚠️ უსაფრთხოება — კრიტიკულად მნიშვნელოვანი

**Claude Code-ით დამუშავებული ყველა ფაილი იგზავნება Anthropic-ის cloud-ში.** ამიტომ:

### სავალდებულო:

1. **არ მიაბათ Qlik-ის data დირექტორიები** Claude Code-ის workspace-ს ან Docker volume-ს
2. **შექმენით იზოლირებული workspace:**
   ```bash
   mkdir -p /opt/claude-workspace
   chmod 750 /opt/claude-workspace
   ```
3. **Claude Code-ის user-ს არ უნდა ჰქონდეს წვდომა** Qlik-ის data ფოლდერებზე
4. **API key** — არ ჩაწეროთ git-ში, `.env` ფაილი `chmod 600`
5. **ფინანსური მონაცემები** პირდაპირ არ გააანალიზოთ Claude Code-ით — მხოლოდ მეტამონაცემები და სტრუქტურა

### იზოლაციის სქემა:

```
┌─────────────────────────────────┐
│       Windows Server            │
│                                 │
│  ┌──────────┐  ┌─────────────┐ │
│  │Qlik Sense│  │Docker/WSL2  │ │
│  │Port 443  │  │┌───────────┐│ │
│  │Financial │  ││Claude Code││ │
│  │Data      │  ││Container  ││ │
│  │          │  │└───────────┘│ │
│  │ არ აქვს  ◄─X─► ცალკე     │ │
│  │ კავშირი  │  │  workspace │ │
│  └──────────┘  └─────────────┘ │
└─────────────────────────────────┘
```

---

## 5. ქსელის კონფიგურაცია

### Firewall — გახსენით outbound:

| მიმართულება | დანიშნულება | პორტი | პროტოკოლი |
|------------|-----------|-------|-----------|
| ALLOW OUT | api.anthropic.com | 443 | HTTPS |
| ALLOW OUT | registry.npmjs.org | 443 | HTTPS (ინსტალაციისთვის) |

### Proxy (თუ გაქვთ):

```bash
export HTTPS_PROXY=http://your-proxy:8080
export HTTP_PROXY=http://your-proxy:8080
```

### inbound პორტები: არ სჭირდება — Claude Code მხოლოდ outbound კავშირს იყენებს.

---

## 6. Checklist

```
[ ] WSL2 + Ubuntu 22.04 დაინსტალირდა
[ ] Node.js 20.x დაინსტალირდა WSL-ში
[ ] npm install -g @anthropic-ai/claude-code
[ ] ცალკე user შეიქმნა (არა admin)
[ ] იზოლირებული workspace შეიქმნა
[ ] ANTHROPIC_API_KEY დაყენდა
[ ] Firewall: api.anthropic.com:443 ALLOW OUT
[ ] Claude Code user-ს Qlik data dirs-ზე წვდომა არ აქვს
[ ] Optional: Docker container-ით გაშვება
[ ] ტესტი: claude -p "Hello" — პასუხი მოვიდა
```

---

## 7. მრავალმომხმარებლიანი გამოყენება

თუ რამდენიმე ადამიანი გამოიყენებს:

- ერთი global install, ყველა OS user-ისთვის
- თითოეულს საკუთარი API key (~/.bashrc-ში)
- ან ცალკე Docker container per user (უკეთესი იზოლაცია)

---

თუ კითხვები გაქვთ — დამიკავშირდით.

გელა შონია
Bivision
