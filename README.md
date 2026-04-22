# OpenClaw Starter Kit — The Alpha Setup

A proven workspace architecture for building a personal AI assistant that actually works.

**v3.0.0 — April 2026** · [Changelog](CHANGELOG.md)

## What's Inside

```
├── BOOTSTRAP.md          ← First-run guide (delete after setup)
├── SOUL.md               ← Agent personality & values
├── AGENTS.md             ← Operating manual (memory, safety, groups, heartbeats)
├── USER.md               ← Template for learning about your human
├── IDENTITY.md           ← Agent identity (name, vibe, emoji)
├── MEMORY.md             ← Core long-term memory (index + essence, always loaded)
├── memory/               ← Daily logs + topic files (loaded on demand via search)
│   ├── README.md          ← How the memory architecture works
│   ├── work.md            ← Company/business context
│   ├── deals.md           ← Active deals & legal
│   ├── travel.md          ← Trips & logistics
│   ├── personal.md        ← Personal preferences & life
│   ├── infra.md           ← Machines, models, cron, skills
│   └── archive.md         ← Completed items
├── GOALS.md              ← Goals & objectives tracker (quarterly)
├── TASKS.md              ← Active monitoring & task tracker
├── HEARTBEAT.md          ← Heartbeat checklist (not just "nothing to do")
├── TOOLS.md              ← Environment notes & discovered quirks
├── contacts/             ← Tiered CRM with staleness tracking
│   └── contacts.md        ← People database
├── design-systems/       ← Brand DESIGN.md files per brand you work on
│                           (not included — you add them)
└── skills-setup/         ← Integration guides
    ├── EMAIL.md           ← Gmail API (read-only) setup
    ├── CALENDAR.md        ← Google Calendar setup
    ├── CRON-TEMPLATES.md  ← Real cron job prompts (briefings, reviews)
    ├── BROWSER.md         ← OpenClaw browser automation
    ├── NOTION.md          ← Notion API integration
    ├── TWITTER.md         ← Twitter/X posting (draft-first)
    ├── VOICE.md           ← TTS voice notes via OpenAI/ElevenLabs
    ├── GITHUB.md          ← GitHub workflows (PRs, forks)
    ├── SUBAGENTS.md       ← Parallel work & multi-model workflows
    ├── GRANOLA.md         ← Meeting recording + auto-sync (NEW v3)
    ├── COMPUTER-USE.md    ← Screen/keyboard/mouse control (NEW v3)
    ├── CLAUDE-DESIGN.md   ← AI-generated decks & landing pages (NEW v3)
    ├── DESIGN-SYSTEMS.md  ← DESIGN.md spec for brand-aware AI (NEW v3)
    └── granola-sync/      ← Auto-sync script + launchd plist (NEW v3)
```

## How to Use

1. Copy these files into your OpenClaw workspace (`~/.openclaw/workspace/`)
2. Set your model to Claude Opus 4.7 (or best available — see infra.md for matrix)
3. Start a conversation — the agent reads BOOTSTRAP.md and guides you through setup
4. Follow the week-by-week integration plan in BOOTSTRAP.md

## Architecture Overview

- **Split-file memory:** `MEMORY.md` stays small (always loaded), topic files get searched on demand. Unlimited knowledge without bloating context.
- **Daily logs + curated memory:** raw notes in `memory/YYYY-MM-DD.md`, distilled wisdom in `MEMORY.md` + topic files.
- **Goals tracking:** quarterly `GOALS.md` checked during heartbeats — deadlines surface automatically.
- **Proactive heartbeats:** background work during idle polls (email, calendar, goals, contacts).
- **Cron jobs:** scheduled tasks (briefings, email review, tweet drafts, weekly briefs).
- **Contact CRM:** tiered `contacts/` with staleness tracking — never lose touch.
- **Task tracking:** persistent across sessions, checked during heartbeats.
- **Subagents:** spawn parallel agents on different models for research + synthesis.
- **Meeting auto-sync:** Granola records meetings, a watcher exports every summary to `memory/granola/` automatically.
- **Computer use:** screen/keyboard/mouse tools installed (cliclick, playwright, tesseract) — human-in-the-loop checkpoints before every action.
- **Design systems:** per-brand DESIGN.md files so AI design tools output on-brand work every time.
- **Error correction loop:** every user correction gets logged, preventing repeat mistakes.

## Model Recommendations

| Use Case | Model | Notes |
|----------|-------|-------|
| Main conversation | `anthropic/claude-opus-4-7` | Best reasoning + personality |
| Heavy analysis / research | `openai/gpt-5.4` | Web-grounded research |
| Cron jobs | `anthropic/claude-sonnet-4-6` | Cheaper, fast enough |
| Local / private | `ollama/qwen3.5:122b-a10b` | Free, runs locally |
| Image generation | `openai/gpt-image-1.5` | Latest quality |

## Credits

Created by Alpha (Claude) with input from GPT.
Iterated through ~3 months of real daily use by Ran Hammer — every file reflects something that actually worked (or broke and got fixed) in production.

## License

MIT — copy, fork, adapt. If you ship something built on this, let me know — I'd love to see.
