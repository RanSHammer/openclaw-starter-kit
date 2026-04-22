# infra.md — Machines, Models & Tooling

_Where your agent lives and what it can use. Loaded on demand._

## Machines
_(Mac/PC/servers your agent runs on; when each is used)_
- Primary: _(e.g. Mac Studio M3 Ultra — always-on)_
- Secondary: _(e.g. MacBook Pro — travel)_
- Mobile: _(iPhone — paired via OpenClaw mobile app)_

## Model Configuration
_(Which model runs where)_

| Use Case | Model | Notes |
|---|---|---|
| Main conversation | `anthropic/claude-opus-4-7` | Best reasoning + personality |
| Research | `openai/gpt-5.4` | Web-grounded, source-aware |
| Cron / background | `anthropic/claude-sonnet-4-6` | Cheap, fast enough |
| Local / private | `ollama/qwen3.5:122b-a10b` | Free, no data leaves machine |
| Image generation | `openai/gpt-image-1.5` | Latest quality |

## Integrations
_(Which services are connected, how, and where credentials live)_
- Email
- Calendar
- Voice (TTS)
- Transcription (Whisper / Granola)
- Messaging channels
- Browser automation

## Cron Jobs
_(Named jobs, schedules, purpose)_
- morning-brief · 07:00 daily
- weekly-intel · Sunday 18:00
- contact-staleness · Monday 10:00

## Skills Installed
_(Which skills from clawhub or custom are loaded)_

## Computer Use
_(Screen control tools: cliclick, playwright, screencapture)_
- Accessibility permission granted? _(yes/no)_
- Screen Recording permission granted? _(yes/no)_

## Known Quirks
_(Edge cases and undocumented behaviors you've discovered)_
