# Cron Job Templates

Real, working examples based on 3 months of production use.
Replace `[bracketed values]` with your own. Deliver to your actual Telegram/Discord channel ID.

## How Cron Works in OpenClaw

Add jobs to your `openclaw.json` config under `cron`:

```json
{
  "cron": {
    "jobs": [
      {
        "name": "morning-briefing",
        "schedule": "30 6 * * 1-5",
        "prompt": "...",
        "model": "claude-opus-4-6",
        "delivery": "none"
      }
    ]
  }
}
```

- `schedule` — standard cron syntax (min hour day month weekday)
- `model` — use Opus for analysis, Sonnet for simple checks
- `delivery: none` — required when your prompt uses the message tool directly
- Each job is isolated — no shared context with your main session

---

## Morning Briefing (6:30 AM, weekdays)

```json
{
  "name": "morning-briefing",
  "schedule": "30 6 * * 1-5",
  "model": "claude-opus-4-6",
  "delivery": "none",
  "prompt": "Morning briefing for [User]. Today is {date}, {day}.\n\n1. Check today's Google Calendar events (ranh@orbs.com + personal)\n2. Check overnight emails — flag urgent, batch the rest\n3. Weather in [City] today\n4. Top 2 news stories relevant to [industry/topic]\n\nFormat with emoji section headers. Keep it punchy — this is a briefing, not an essay.\n\nEnd with:\n🔍 Currently Monitoring:\n(Pull 3-5 active items from TASKS.md)\n\nSend via message tool to [CHANNEL_ID]. Deliver the full thing — never truncate."
}
```

**Tips:**
- Weekdays only (`1-5`). Add `0 0 * * 6` for a lighter weekend version if you want.
- Opus is worth the cost here — it writes well and synthesizes better.
- Include your Telegram channel ID as a literal number, e.g. `-1002381931352`.

---

## Email Review (9 AM + 6 PM)

```json
{
  "name": "email-morning",
  "schedule": "0 9 * * 1-5",
  "model": "claude-sonnet-4-6",
  "delivery": "none",
  "prompt": "Check both email inboxes ([work@domain.com] + [personal@gmail.com]) for messages in the last 16 hours.\n\nCategorize:\n🔔 Urgent — needs reply today (sender, subject, 1-line summary)\n📋 FYI — no action needed (list format)\n🗑️ Noise — newsletters, automated, spam (just count them)\n\nIf nothing urgent: say so and stop. No need for a long report.\nSend via message tool to [CHANNEL_ID]."
}
```

```json
{
  "name": "email-evening",
  "schedule": "0 18 * * 1-5",
  "model": "claude-sonnet-4-6",
  "delivery": "none",
  "prompt": "Check both email inboxes for messages since 9 AM today.\n\nSame format: 🔔 Urgent / 📋 FYI / 🗑️ Noise\nIf nothing actionable, just say 'Inbox clear — nothing urgent.'\nSend via message tool to [CHANNEL_ID]."
}
```

**Tips:**
- Sonnet is plenty for email triage — save Opus for things that need nuance.
- The 16-hour window on morning review catches anything since the previous evening check.

---

## Tweet Suggestions (9 AM + 3 PM)

```json
{
  "name": "tweet-suggestions-am",
  "schedule": "0 9 * * 1-5",
  "model": "claude-sonnet-4-6",
  "delivery": "none",
  "prompt": "Search Twitter for trending topics in [your niche/industry].\nCheck recent news about [company/project].\n\nDraft 2-3 tweet options with different vibes:\nA) Strong opinion / thought leadership\nB) Question or conversation starter\nC) [Company/project] angle\n\nFor each: include the text (count chars), suggested @mentions, best time.\n\n⚠️ These are DRAFTS ONLY. Never post without explicit approval.\nSend via message tool to [CHANNEL_ID]."
}
```

```json
{
  "name": "tweet-suggestions-pm",
  "schedule": "0 15 * * 1-5",
  "model": "claude-sonnet-4-6",
  "delivery": "none",
  "prompt": "Check what's been engaging on Twitter in [niche] today.\nDraft 1-2 afternoon tweet options — more casual, engagement-focused.\nInclude any hot threads worth jumping into.\n⚠️ Drafts only — send to [CHANNEL_ID] for approval."
}
```

---

## Weekly Intelligence Brief (Monday 8 AM)

```json
{
  "name": "weekly-brief",
  "schedule": "0 8 * * 1",
  "model": "claude-opus-4-6",
  "delivery": "none",
  "prompt": "Weekly intelligence brief for [User]. Week of {date}.\n\nCover:\n1. 📰 [Industry] news from the past 7 days — top 5 developments\n2. 🏢 [Company/Project] mentions, sentiment, notable activity\n3. 🔀 What competitors/peers are up to\n4. 📊 Market/metrics snapshot — [crypto/stocks/KPIs relevant to you]\n5. 📅 Key events or deadlines this week\n6. ✅ Recommended actions — 3 concrete things to focus on\n\nThis one can be thorough — it's a weekly read, not a quick alert.\nSend via message tool to [CHANNEL_ID]."
}
```

**Tips:**
- Use Opus for the weekly brief — it's worth it for the synthesis quality.
- If you want it as a voice note instead, add: `Then generate a 3-minute audio summary using TTS (tts-1-hd, nova voice) and send as a voice note.`

---

## Contact Staleness Check (Sunday 10 AM)

```json
{
  "name": "contact-check",
  "schedule": "0 10 * * 0",
  "model": "claude-sonnet-4-6",
  "delivery": "none",
  "prompt": "Read contacts/ directory. Check last_contact dates.\n\nFlag:\n- Tier 1 contacts not touched in 30+ days\n- Tier 2 contacts not touched in 60+ days\n\nFor each: name, days since contact, what I know about them, suggested re-engagement angle.\nMax 5 contacts surfaced. Short and actionable.\nSend via message tool to [CHANNEL_ID]."
}
```

---

## Design Principles

1. **`delivery: none` + message tool** — always explicitly deliver to your channel. Default delivery often doesn't format well.
2. **Cheaper model = more frequent checks** — Sonnet for email/tweets, Opus for analysis/briefs.
3. **Each job is isolated** — no main session context. Be explicit in prompts about what to check and how to format.
4. **Start small** — add 2-3 jobs first. Evaluate after a week before adding more.
5. **Weekdays only** — most jobs use `1-5`. Run lighter versions on weekends if at all.
6. **Time zones** — cron runs in server time. If your server is UTC and you're in a different zone, adjust the hour.
