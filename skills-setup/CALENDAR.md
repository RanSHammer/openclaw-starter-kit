# Google Calendar Integration

## Setup Steps

1. **Same Google Cloud Project as Email**
   - Enable Google Calendar API

2. **OAuth2 Scopes**
   - `https://www.googleapis.com/auth/calendar.readonly`
   - `https://www.googleapis.com/auth/calendar.events` (for creating events)

3. **Create Two Scripts**
   - `check.js` — Fetch events (supports --today, --week, --month, per account)
   - `create.js` — Create events with title, time, location, description

4. **Multiple Accounts**
   - Separate tokens: `token-orbs.json`, `token-gmail.json`
   - Pass account as CLI arg: `node check.js gmail 7`

## Why This Matters
Calendar awareness transforms your agent from reactive to proactive:
- "You have 3 meetings tomorrow but no lunch blocked"
- "Your 2pm call is in 15 minutes"
- Morning briefings include today's schedule automatically
