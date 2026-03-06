# HEARTBEAT.md — What to Do When Polled

## Quick Checks (every heartbeat)
1. Read TASKS.md — any monitoring items need attention?
2. Any urgent unread emails? (if email integration is set up)
3. Calendar: anything in next 2 hours?
4. Did any cron jobs fail recently?

## Memory Maintenance (every 3rd heartbeat, ~2x/day)
1. Read today's + yesterday's daily memory file
2. Promote important items to MEMORY.md if missing
3. Update TASKS.md with any new items or completions
4. Check TOOLS.md — any undocumented quirks from recent sessions?

## Proactive (when idle, ~1x/day)
1. Review MEMORY.md for stale/outdated entries
2. Check if any "Pending" items in TASKS.md can be resolved
3. Look for something useful to surface to your human

## Rules
- Late night (23:00-08:00): HEARTBEAT_OK unless genuinely urgent
- Just checked <30 min ago: HEARTBEAT_OK
- Track last check times in memory/heartbeat-state.json
- If alerting: skip HEARTBEAT_OK, send the alert directly
