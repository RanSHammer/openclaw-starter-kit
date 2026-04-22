# Granola — Meeting Recording & Auto-Sync

Granola is a meeting recorder that captures system audio + mic without joining calls as a visible bot. Works on Mac and iPhone. Generates AI summaries. This guide sets up **auto-sync** so every meeting lands in your workspace automatically.

## Why Granola

- **Invisible to other participants** — no bot joins the Zoom/Meet call
- **Mac + iPhone apps** — capture in-person meetings too
- **AI summaries per meeting** — already structured (topics, action items)
- **Local data cache** — we can watch the file and ingest without any API integration

## Install

1. Download from granola.ai → install Mac app
2. Sign in with your work email (or whatever account has your meetings)
3. Grant microphone + screen recording permissions when prompted
4. Install the iPhone companion app from the App Store
5. Enable recording-by-default for scheduled meetings

## How the sync works

Granola caches all your meeting notes in a local JSON file:

```
~/Library/Application Support/Granola/cache-v6.json
```

This includes: title, attendees, timestamps, AI summary, markdown notes. Everything you need.

We watch this file, and on every change, export new meetings as markdown into `memory/granola/`.

## Install the sync

```bash
# Install fswatch (file watcher for macOS)
brew install fswatch

# Create directories
mkdir -p ~/.openclaw/workspace/memory/granola
mkdir -p ~/.openclaw/workspace/scripts/granola-sync
```

Copy `export.py` and `watch.sh` from this kit's `skills-setup/granola-sync/` into `~/.openclaw/workspace/scripts/granola-sync/` and make them executable:

```bash
chmod +x ~/.openclaw/workspace/scripts/granola-sync/*.py ~/.openclaw/workspace/scripts/granola-sync/*.sh
```

## Run at login (launchd)

Create `~/Library/LaunchAgents/ai.alpha.granola-sync.plist` (template in `skills-setup/granola-sync/launchd.plist`), then:

```bash
launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.alpha.granola-sync.plist
launchctl print gui/$UID/ai.alpha.granola-sync | grep state
```

You should see `state = running`. Now every meeting Granola records will appear as a markdown file in `memory/granola/YYYY-MM-DD-slug.md` within seconds of the summary being generated.

## What your agent does with the files

- Does NOT auto-load them (would burn context)
- Finds them via `memory_search` when you ask about a meeting
- Can use them to answer "what did I discuss with X?", "what were my action items from today?"

## Privacy

- Audio is sent to Granola's servers for transcription (their SOC2 policy)
- For truly sensitive meetings, toggle off recording in Granola and do plain notes instead
- The local markdown files stay on your machine — nothing leaves unless you send it
