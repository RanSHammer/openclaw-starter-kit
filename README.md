# OpenClaw Starter Kit — The Alpha Setup

A proven workspace architecture for building a personal AI assistant that actually works.

## What's Inside

```
├── BOOTSTRAP.md          ← First-run guide (delete after setup)
├── SOUL.md               ← Agent personality & values
├── AGENTS.md             ← Operating manual (memory, safety, groups, heartbeats)
├── USER.md               ← Template for learning about your human
├── IDENTITY.md           ← Agent identity (name, vibe, emoji)
├── MEMORY.md             ← Long-term memory template (organized by topic)
├── TASKS.md              ← Active monitoring & task tracker
├── HEARTBEAT.md          ← Heartbeat checklist (not just "nothing to do")
├── TOOLS.md              ← Environment notes & discovered quirks
├── contacts.md           ← People database
├── memory/               ← Daily log directory
└── skills-setup/         ← Integration guides
    ├── EMAIL.md           ← Gmail API (read-only) setup
    ├── CALENDAR.md        ← Google Calendar setup
    └── CRON-TEMPLATES.md  ← Ready-to-use cron job prompts
```

## How to Use

1. Copy these files into your OpenClaw workspace (`~/.openclaw/workspace/`)
2. Set your model to Claude Opus (or best available)
3. Start a conversation — the agent will read BOOTSTRAP.md and guide you through setup
4. Follow the week-by-week integration plan in BOOTSTRAP.md

## Architecture Overview

- **Two-tier memory:** Daily logs (raw) + MEMORY.md (curated)
- **Semantic search:** Agent searches memory before answering context questions
- **Proactive heartbeats:** Background work during idle polls
- **Cron jobs:** Scheduled tasks (briefings, email review, monitoring)
- **Contact management:** Lookup before searching blind
- **Task tracking:** Persistent across sessions, checked during heartbeats
- **Error correction loop:** Every user correction gets logged, preventing repeat mistakes

## Recommended Model Config

| Use Case | Model | Why |
|----------|-------|-----|
| Main conversation | Claude Opus 4 | Best reasoning + personality |
| Heavy analysis | Opus or GPT-5 | Deep research |
| Simple cron jobs | Claude Sonnet | Cheaper, fast enough |
| Local/private | Qwen/Llama via Ollama | Free, no data leaves machine |
| Image analysis | GPT-4o+ | Strong vision |

## Credits

Created by Alpha (Claude Opus 4) + GPT-5.4, March 2026.
Architecture guide: See the companion Notion page for the full detailed breakdown.

OpenClaw docs: https://docs.openclaw.ai
Community: https://discord.com/invite/clawd
