# MEMORY.md — Long-Term Memory (Core)

> **Topic files** (searchable via memory_search, not auto-injected):
> - `memory/work.md` — Company, products, GTM, key business context
> - `memory/deals.md` — Active deals, contracts, legal
> - `memory/travel.md` — Active/upcoming trips, flights, hotels
> - `memory/personal.md` — Personal preferences, purchases, family
> - `memory/infra.md` — Machines, models, tools, cron jobs, skills
> - `memory/archive.md` — Completed items (past trips, closed deals)

_This file is the **index + essence**. It stays loaded in every session._
_Topic files only load when `memory_search` returns them or when you explicitly reference them._
_Keep this file under ~200 lines. Everything else goes into topic files._

---

## About [User]
_(Fill in as you learn: name, role, company, timezone, key details)_

## Permissions
_(Hard boundaries your agent must respect)_
- Email: READ-ONLY (never send, reply, forward, archive)
- Calendar: read + create events
- Social: DRAFT-ONLY — never post without explicit approval

## Preferences & Corrections
_(Every time they correct you, log it here. These prevent repeat mistakes.)_
- When sending drafts to copy/paste, send ONLY the raw text — no "Here's the draft" preamble
- Keep responses short and concise by default; only go long when asked
- Web search = [preferred provider] ONLY

## Projects
_(Active projects, status, key decisions)_

## Key People
_(Main contacts with whom your agent interacts most. Detailed CRM in `contacts/`)_

## Silent Replies
When you have nothing useful to add in a group chat or heartbeat, respond with ONLY: `NO_REPLY`

**Rules:**
- Must be the ENTIRE message — nothing else
- Never append to actual replies
- Never wrap in markdown

---

_Keep this file lean. Topic files hold the details; this holds the essence._
