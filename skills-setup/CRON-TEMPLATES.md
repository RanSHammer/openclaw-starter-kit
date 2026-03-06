# Cron Job Templates

## Morning Briefing (Daily, 6:30 AM)

```
Morning briefing for [User]. Today is [day, date].

1. Check today's calendar events (all accounts)
2. Check overnight emails — flag urgent, suggest archive for spam
3. Market data relevant to user (crypto, stocks, etc.)
4. Top 3 news stories relevant to [industry]
5. Weather for [city]

Format: Clean sections with emoji headers.
End with "🔍 Currently Monitoring:" section from TASKS.md.
Deliver FULL — never summarize.
Send via message tool to [channel].
```

## Email Review (Daily, 9 AM + 6 PM)

```
Check [email accounts] for messages in the last [8-12] hours.
Categorize as: 🔔 Urgent / 📋 FYI / 🗑️ Archive.
For urgent: include sender, subject, 1-line summary.
For archive: batch into a simple list.
Send via message tool to [channel].
```

## Tweet Suggestion (Daily, 9 AM + 3 PM)

```
Search for trending topics in [industry].
Check recent [company] news and announcements.
Draft 2-3 tweet options with different vibes (thought leadership, engagement, promotion).
Include engagement suggestions (accounts to reply to, threads to join).
Send drafts to [channel] for approval. Never auto-post.
```

## Weekly Intelligence Brief (Monday, 9 AM)

```
Comprehensive weekly brief for [User] covering:
1. [Industry] news and trends from the past week
2. [Company] mentions and sentiment
3. Competitor activity
4. Market performance
5. Key events/conferences coming up
6. Recommended actions for the week

Format as a detailed report. This one can be long.
Send via message tool to [channel].
```

## Design Principles
- Use `delivery: none` + explicit message tool for formatted output
- Each job is self-contained — no main session context
- Use cheaper models (Sonnet) for simple checks
- Use expensive models (Opus) for analysis/briefs
- Don't over-schedule — start with 3-4 jobs
