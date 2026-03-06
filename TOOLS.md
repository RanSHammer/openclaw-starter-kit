# TOOLS.md — Environment Notes

_Skills define how tools work. This file is for YOUR specifics — quirks, workarounds, and lessons learned._

## What Goes Here
- API quirks you've discovered
- Platform-specific workarounds
- Device names, SSH hosts, voice preferences
- Anything environment-specific

## Known Quirks

### OpenAI API
- GPT-5.x models require `max_completion_tokens` NOT `max_tokens`
- Image model: `chatgpt-image-latest`

### OAuth Re-Auth Trick
- If user is on a different machine from yours:
  1. They open the OAuth link in their browser
  2. Approve access
  3. Copy the failed localhost redirect URL
  4. Send it to you — extract the `code` param and exchange manually

### TTS (Telegram)
- Use `filePath` param for audio, NOT `message` with MEDIA: path
- `asVoice: true` + `filePath: /path/to/file.opus` = works ✅

### Browser Automation
- Always accept cookie popups before interacting
- Pass `targetId` to keep the same tab across actions
- Use `snapshot` for navigation, `screenshot` for sending to user

### Contacts
- Check `contacts.md` before searching emails blind

---

_Update this whenever you discover something. Future-you will thank you._
