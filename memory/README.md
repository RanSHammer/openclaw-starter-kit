# memory/ — Topic Files + Daily Logs

This directory holds two kinds of files:

## 1. Topic Files (curated, searchable)

Named files that split long-term memory by topic:

- `work.md` — company/business context
- `deals.md` — active deals, contracts
- `travel.md` — trips, flights, hotels
- `personal.md` — personal preferences
- `infra.md` — machines, models, tools
- `archive.md` — completed items, past context

**Why topic files?** They're found via `memory_search` when relevant, NOT auto-loaded every session. This keeps your core `MEMORY.md` small and focused.

**When to promote to a topic file:**
- Something in MEMORY.md is getting too long (>15 lines on one topic)
- You find yourself updating the same section repeatedly
- Info is relevant sometimes but not every session

## 2. Daily Logs

`YYYY-MM-DD.md` files — one per day with raw context, decisions, conversations.

**What goes in daily logs:**
- What happened that day
- Decisions made
- Things learned
- Quick notes you might want later

**What DOESN'T:**
- Stable preferences → `MEMORY.md`
- Deep topic knowledge → topic file
- One-off thoughts that don't need persistence

## Workflow

1. **In the moment:** append to today's `YYYY-MM-DD.md`
2. **Periodically (heartbeat):** promote important learnings to MEMORY.md or a topic file
3. **Search via `memory_search`:** finds relevant context from any file without loading everything

## The Key Insight

Most "AI memory" systems fail because they either:
- Load everything (wastes context + costs)
- Load nothing (agent feels dumb)

The split-file approach loads a **small core** every session and **searches the rest on demand**. That's the whole trick.
