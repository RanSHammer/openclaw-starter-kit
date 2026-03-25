# Voice Notes — OpenAI TTS Setup

Generate audio voice notes and send them as voice messages via Telegram.

## Why Voice?

Some content hits differently as audio:
- Morning briefings feel like a real briefing
- Story summaries are more engaging than walls of text
- Quick status updates you can listen to while making coffee

## Setup

### 1. OpenAI API Key

You need an OpenAI API key with access to the Audio API.

```bash
# Store alongside your other OpenAI config
echo "sk-..." >> ~/.config/openai/api_key
```

Or if you already have `OPENAI_API_KEY` in your environment, you're set.

### 2. Install ffmpeg (for opus conversion)

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg
```

### 3. Test It

```bash
curl -s -X POST https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"tts-1-hd","voice":"nova","input":"Hello, this is Alpha. Testing voice notes."}' \
  -o /tmp/test.mp3

# Convert to opus (smaller, Telegram-native)
ffmpeg -i /tmp/test.mp3 -c:a libopus /tmp/test.opus

# Play it
afplay /tmp/test.opus  # macOS
```

## Generating Voice Notes

### Basic TTS Call

```bash
curl -s -X POST https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1-hd",
    "voice": "nova",
    "input": "YOUR TEXT HERE",
    "response_format": "opus"
  }' \
  -o /tmp/voice-note.opus
```

### Models & Voices

| Model | Quality | Speed | Cost |
|-------|---------|-------|------|
| `tts-1` | Good | Fast | Cheap |
| `tts-1-hd` | Great | Slower | ~2x |

| Voice | Character |
|-------|-----------|
| `nova` | Warm, friendly — good default ✅ |
| `alloy` | Neutral, clear |
| `echo` | Male, smooth |
| `fable` | British, storytelling |
| `onyx` | Deep, authoritative |
| `shimmer` | Soft, gentle |

Stick with `nova` unless you have a reason to change.

## Sending via Telegram

```javascript
// In your message tool call:
{
  filePath: "/tmp/voice-note.opus",
  asVoice: true
}
```

**Important:** Use `filePath` + `asVoice: true` — NOT the `MEDIA:` path syntax. The latter sends it as a file, not a voice note.

## Use Cases

### Morning Briefing

```
Generate a voice briefing for [User]. 
Cover: calendar, key emails, weather, 1 interesting news item.
Keep it under 90 seconds when spoken.
Warm, upbeat tone. Start with "Good morning!"
Generate as voice note and send to [channel].
```

Script tip: ~130 words ≈ 60 seconds at normal pace. Aim for 200-250 words for a ~2 min briefing.

### Story Time

```
Summarize this article/thread as an engaging 2-minute audio story.
Use narrative structure — hook, context, key points, takeaway.
Generate as voice note.
```

### Quick Status Update

```
Generate a 30-second voice update:
"Here's what I found: [summary]"
Send as voice note.
```

### End-of-Day Digest

```
Summarize today's key events, decisions, and open items.
60-90 second voice note. Conversational tone.
Send to [channel].
```

## Cron Example

```json
{
  "name": "morning-briefing-voice",
  "schedule": "30 6 * * 1-5",
  "prompt": "Generate a 90-second morning briefing voice note for [User]. Check calendar, top emails, weather in London. Warm tone, start with 'Good morning!' Convert to opus and send to [channel] as voice note.",
  "model": "claude-opus-4-6"
}
```

## Tips

- **Keep it conversational** — write for ears, not eyes. Short sentences. Active voice.
- **Avoid lists** — bullet points don't work in audio. Use "first... second... and finally..."
- **Test length** — ask the agent to estimate word count before generating. 200 words ≈ ~90 seconds.
- **File cleanup** — voice files pile up. Add cleanup to your cron: `find /tmp -name "*.opus" -mtime +1 -delete`
- **Emotion beats facts** — start with energy, not data. "Big day ahead!" lands better than "You have 7 meetings."
