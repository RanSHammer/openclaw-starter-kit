# HEARTBEAT.md — What to Do When Polled

## Quick Checks (every heartbeat)
1. Read TASKS.md — any monitoring items need attention?
2. Any urgent unread emails? (if email integration is set up)
3. Calendar: anything in next 2 hours?
4. Did any cron jobs fail recently?

## Goals Check (every heartbeat)
1. Skim GOALS.md — any deadlines approaching this week?
2. Any goal milestones that should be surfaced to your human?
3. If a tracked goal looks stuck or overdue, mention it (don't silently skip)

## Contact Enrichment (every other heartbeat)
1. Check contacts/ directory for entries with `last_contact` > 30 days
2. If a Tier 1 contact hasn't been touched in 30+ days, flag it
3. If a Tier 2 contact hasn't been touched in 60+ days, mention it
4. Don't spam — surface at most 2-3 stale contacts at a time

## Memory Maintenance (every 3rd heartbeat, ~2x/day)
1. Read today's + yesterday's daily memory file
2. Promote important items to MEMORY.md if missing
3. Update TASKS.md with any new items or completions
4. Check TOOLS.md — any undocumented quirks from recent sessions?
5. If MEMORY.md is getting long, prune stale entries

## Proactive (when idle, ~1x/day)
1. Review MEMORY.md for stale/outdated entries
2. Check if any "Pending" items in TASKS.md can be resolved
3. Look for something useful to surface to your human

## Heartbeat Counter

Track which heartbeat number you're on in `memory/heartbeat-state.json`:

```json
{
  "count": 0,
  "lastChecks": {
    "email": null,
    "calendar": null,
    "weather": null,
    "contacts": null,
    "goals": null
  }
}
```

Increment `count` each heartbeat. Do memory maintenance when `count % 3 === 0`.

## Rules
- Late night (23:00-08:00): HEARTBEAT_OK unless genuinely urgent
- Just checked <30 min ago: HEARTBEAT_OK
- If alerting: skip HEARTBEAT_OK, send the alert directly
- Don't surface the same stale contact twice in a row
