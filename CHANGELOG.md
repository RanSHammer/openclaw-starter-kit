# Changelog

## v2.0.0 — March 25, 2026

Major update based on 3 months of production use. Added integrations, real cron examples, and new workspace primitives.

### New Files

- `GOALS.md` — Quarterly goals tracker with status tracking and heartbeat integration
- `contacts/` — Contact CRM directory with tier-based staleness tracking
- `skills-setup/BROWSER.md` — OpenClaw browser automation guide (snapshot, click, form fill, screenshots)
- `skills-setup/NOTION.md` — Notion API integration (internal integration, read/write pages, block types)
- `skills-setup/TWITTER.md` — Twitter/X skill setup (post, reply, search, like; always draft-first workflow)
- `skills-setup/VOICE.md` — OpenAI TTS voice notes (tts-1-hd, nova voice, Telegram delivery)
- `skills-setup/GITHUB.md` — GitHub workflows via gh CLI (fork, branch, PR, awesome list submissions)
- `skills-setup/SUBAGENTS.md` — Parallel subagent workflows and multi-model task delegation
- `CHANGELOG.md` — This file

### Updated Files

- `README.md` — Updated file tree, new integration descriptions, updated model recommendations table
- `HEARTBEAT.md` — Added goals check, contact staleness check, heartbeat counter, memory maintenance rotation
- `skills-setup/CRON-TEMPLATES.md` — Replaced placeholder templates with real working examples (morning briefing, email review, tweet suggestions, weekly brief, contact staleness)

### Model Recommendations (Updated)

| Use Case | Model | Notes |
|----------|-------|-------|
| Main conversation | `claude-opus-4-6` | Best reasoning + personality |
| Heavy analysis / research | `gpt-5.4` | Strong web-grounded research |
| Cron jobs | `claude-sonnet-4-6` | Cheaper, fast enough |
| Local / private | `ollama/qwen3.5` | Free, runs locally |
| Image generation | `chatgpt-image-latest` | Best quality |

---

## v1.0.0 — March 2026

Initial release. Core workspace architecture:
- SOUL.md, AGENTS.md, USER.md, IDENTITY.md
- Two-tier memory system (daily logs + MEMORY.md)
- TASKS.md, HEARTBEAT.md, TOOLS.md
- skills-setup: EMAIL.md, CALENDAR.md, CRON-TEMPLATES.md
