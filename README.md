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
├── GOALS.md              ← Goals & objectives tracker (quarterly)
├── TASKS.md              ← Active monitoring & task tracker
├── HEARTBEAT.md          ← Heartbeat checklist (not just "nothing to do")
├── TOOLS.md              ← Environment notes & discovered quirks
├── contacts/             ← Contact CRM with tiers and staleness tracking
│   └── contacts.md       ← People database (tier 1/2/3, last contact date)
├── memory/               ← Daily log directory
└── skills-setup/         ← Integration guides
    ├── EMAIL.md           ← Gmail API (read-only) setup
    ├── CALENDAR.md        ← Google Calendar setup
    ├── CRON-TEMPLATES.md  ← Ready-to-use cron job prompts (with real examples)
    ├── BROWSER.md         ← OpenClaw browser automation
    ├── NOTION.md          ← Notion API integration
    ├── TWITTER.md         ← Twitter/X posting skill
    ├── VOICE.md           ← TTS voice notes via OpenAI
    ├── GITHUB.md          ← GitHub workflows (PRs, forks, submissions)
    └── SUBAGENTS.md       ← Parallel work & multi-model workflows
```

## How to Use

1. Copy these files into your OpenClaw workspace (`~/.openclaw/workspace/`)
2. Set your model to Claude Opus (or best available)
3. Start a conversation — the agent will read BOOTSTRAP.md and guide you through setup
4. Follow the week-by-week integration plan in BOOTSTRAP.md

## Architecture Overview

- **Two-tier memory:** Daily logs (raw) + MEMORY.md (curated)
- **Goals tracking:** Quarterly GOALS.md checked during heartbeats — deadlines surface automatically
- **Proactive heartbeats:** Background work during idle polls (email, calendar, goals, contacts)
- **Cron jobs:** Scheduled tasks (briefings, email review, tweet drafts, weekly briefs)
- **Contact CRM:** Tiered contacts/ directory with staleness tracking — never lose touch
- **Task tracking:** Persistent across sessions, checked during heartbeats
- **Subagents:** Spawn parallel agents on different models for research + synthesis workflows
- **Error correction loop:** Every user correction gets logged, preventing repeat mistakes

## Recommended Model Config

| Use Case | Model ID | Why |
|----------|----------|-----|
| Main conversation | `claude-opus-4-6` | Best reasoning, best personality |
| Heavy analysis / research | `gpt-5.4` | Deep research, web-grounded |
| Cron jobs & simple tasks | `claude-sonnet-4-6` | Cheaper, plenty fast |
| Local / private | `ollama/qwen3.5` (Qwen 3.5 397B) | Free, no data leaves your machine |
| Image generation | `chatgpt-image-latest` or `dall-e-3` | Best quality images |

## Credits

Created by Alpha (Claude Opus 4) + GPT-5.4, March 2026.
Architecture guide: See the companion Notion page for the full detailed breakdown.

OpenClaw docs: https://docs.openclaw.ai
Community: https://discord.com/invite/clawd
