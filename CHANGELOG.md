# Changelog

## v3.1.0 — April 22, 2026

Agent-led onboarding. New users no longer read setup docs — the agent drives first-run experience through conversation + proactive nudges.

### New Files

- `ONBOARDING.md` — behavior spec the agent reads at the start of every session until onboarding is complete. Four phases: first contact (naming + avatar), situational awareness, quick win, connection. Philosophy: a relationship, not a checklist.
- `memory/.onboarding.json` — state file tracking onboarding progress (phase, what's been learned, nudge history)
- `skills-setup/onboarding-nudges.md` — five conditional cron templates for proactive outreach during the first ~4 weeks. Guard rails prevent spammy behavior; every nudge must deliver real value or skip the run.

### Key Design Decisions

- **Phase 0 always starts with naming.** First interaction must ask the user what to call the agent.
- **Avatar generation in Phase 0.** Agent offers to generate 2–4 profile pic options via the image generation API, or accepts the user's own image.
- **Nudges are conditional, not scheduled.** A cron fires hourly but most runs produce no output. Nudges only happen when there's a real moment.
- **Silence is respected.** Three consecutive ignored nudges → switch to reactive-only mode for 7 days.
- **Onboarding completes itself.** Agent sets `onboarding_complete: true` when the user has received real value 5+ times, corrected the agent 3+ times, and connected 3+ integrations organically.

### Updated Files

- `AGENTS.md` — added "read ONBOARDING.md if onboarding not complete" to session start routine
- `README.md` — added onboarding to architecture overview and file tree

---

## v3.0.0 — April 22, 2026

Major architectural refresh based on another month of production use. Key changes: split-file memory, Granola auto-sync, computer use, design systems.

### New Files

- `memory/README.md` — explains the split-file memory architecture
- `memory/work.md`, `memory/deals.md`, `memory/travel.md`, `memory/personal.md`, `memory/infra.md`, `memory/archive.md` — topic file templates (searched on demand, not auto-loaded)
- `skills-setup/GRANOLA.md` — meeting recording + auto-sync guide
- `skills-setup/granola-sync/export.py` — Granola cache → markdown exporter
- `skills-setup/granola-sync/watch.sh` — file watcher script
- `skills-setup/granola-sync/launchd.plist` — launchd template to run on login
- `skills-setup/COMPUTER-USE.md` — screen/keyboard/mouse control stack (cliclick + playwright + tesseract)
- `skills-setup/CLAUDE-DESIGN.md` — AI-generated decks and landing pages (Anthropic Labs' Claude Design)
- `skills-setup/DESIGN-SYSTEMS.md` — DESIGN.md spec for brand-aware AI tooling

### Architectural Changes

#### Split-file memory

`MEMORY.md` was getting long. v3 splits it into an **index + essence** file that stays loaded, and topic files (`memory/work.md`, etc.) that live in the `memory/` directory and are only found via `memory_search` when relevant. Benefits:

- Smaller context window, faster responses
- More total knowledge (topic files can be long without cost)
- Cleaner curation

Migration from v2: any section of your old `MEMORY.md` longer than ~15 lines should be promoted to a topic file.

#### Design systems

Added top-level `design-systems/` directory. Each brand you work on gets its own folder with a `DESIGN.md` file. Drop that file into Claude Design / Stitch / Cursor to get on-brand output automatically.

#### Meeting auto-sync

Granola caches meeting data locally. The new `granola-sync` watcher picks up every new meeting note and writes it to `memory/granola/YYYY-MM-DD-slug.md` within seconds. No manual forwarding.

#### Computer use

Installed: `cliclick` (mouse/keyboard), `playwright` (browser), `tesseract` (OCR), `screencapture` (built-in). Rule: agent always asks before acting on screen.

### Updated Files

- `README.md` — full file tree, new integrations, v3 architecture notes
- `AGENTS.md` — updated memory section to explain split-file approach
- `MEMORY.md` — reformatted as index + essence; topic files take the detail
- `skills-setup/*` — no breaking changes, but model recommendations updated to Opus 4.7

### Model Recommendations (v3)

| Use Case | Model | Notes |
|---|---|---|
| Main conversation | `anthropic/claude-opus-4-7` | Opus 4.7 launched Apr 16, 2026 |
| Heavy analysis / research | `openai/gpt-5.4` | Strong web-grounded |
| Cron jobs | `anthropic/claude-sonnet-4-6` | Cheaper, fast enough |
| Local / private | `ollama/qwen3.5:122b-a10b` | Free, local |
| Image generation | `openai/gpt-image-1.5` | Latest quality |

---

## v2.0.0 — March 25, 2026

Major update based on 3 months of production use. Added integrations, real cron examples, and new workspace primitives.

### New Files

- `GOALS.md` — Quarterly goals tracker with status tracking and heartbeat integration
- `contacts/` — Contact CRM directory with tier-based staleness tracking
- `skills-setup/BROWSER.md` — OpenClaw browser automation guide
- `skills-setup/NOTION.md` — Notion API integration
- `skills-setup/TWITTER.md` — Twitter/X skill setup (always draft-first workflow)
- `skills-setup/VOICE.md` — OpenAI TTS voice notes
- `skills-setup/GITHUB.md` — GitHub workflows via gh CLI
- `skills-setup/SUBAGENTS.md` — Parallel subagent workflows
- `CHANGELOG.md` — This file

### Updated Files

- `README.md` — Updated file tree, new integration descriptions, updated model recommendations
- `HEARTBEAT.md` — Added goals check, contact staleness check, heartbeat counter, memory maintenance rotation
- `skills-setup/CRON-TEMPLATES.md` — Real working examples (morning briefing, email review, tweet suggestions, weekly brief, contact staleness)

---

## v1.0.0 — March 2026

Initial release. Core workspace architecture:
- SOUL.md, AGENTS.md, USER.md, IDENTITY.md, MEMORY.md
- TASKS.md, HEARTBEAT.md, TOOLS.md
- BOOTSTRAP.md for first-run
- skills-setup/EMAIL.md, CALENDAR.md, CRON-TEMPLATES.md
