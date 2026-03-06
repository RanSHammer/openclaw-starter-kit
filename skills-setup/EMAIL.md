# Email Integration (Gmail API — Read Only)

## Setup Steps

1. **Create Google Cloud Project**
   - Go to console.cloud.google.com
   - Create new project (e.g., "My Assistant")
   - Enable Gmail API

2. **Create OAuth2 Credentials**
   - APIs & Services → Credentials → Create Credentials → OAuth client ID
   - Application type: Desktop app
   - Download JSON → save as `credentials.json`

3. **Create Auth Script** (`auth-gmail.js`)
   - Use `googleapis` npm package
   - Scope: `https://www.googleapis.com/auth/gmail.readonly` (READ ONLY!)
   - Listen on localhost for OAuth callback
   - Save refresh token to `token-oauth-[account].json`

4. **Create Check Script** (`check-email.js`)
   - Search with Gmail API: `gmail.users.messages.list()`
   - Support flags: `--search`, `--limit`, `--all` (All Mail vs Inbox)
   - Format output for readability

## Key Decisions
- **Start READ-ONLY.** Build trust before adding send.
- **Always search All Mail** — most people archive everything.
- **Support multiple accounts** — work + personal, separate token files.

## OAuth Re-Auth Trick
If user is on a different machine:
1. They open OAuth link, approve
2. Copy the failed localhost redirect URL
3. You extract the `code` param and exchange via script
