# Onboarding Nudges — Proactive Outreach During Agent Onboarding

Cron templates for the first ~4 weeks. These fire conditionally — never on a pure schedule. If there's nothing useful to say, the agent stays quiet.

## Guard rails (applied to every nudge below)

Every nudge prompt should check these before sending:

1. `onboarding_complete` is `false` (stop once onboarded)
2. It's a weekday, **local time 09:00–11:00** (user's timezone from USER.md)
3. User hasn't interacted with the agent in the last 2 hours
4. `nudges.consecutive_no_reply < 3` (respect silence)
5. `nudges.paused_until` is in the past (honor pauses)
6. The nudge has **something specific to say** — not just "hi, still here"

If any fail → skip this run, log reason, exit silently.

---

## Cron template structure

All nudges use the same OpenClaw cron pattern:

```bash
openclaw cron add \
  --name "onboarding-nudge-<phase>" \
  --cron "0 9 * * 1-5" \
  --tz "Europe/London" \
  --session main \
  --wake now \
  --system-event "Onboarding nudge check: <phase>. Read ONBOARDING.md + memory/.onboarding.json first. Apply guard rails. Only speak if you have something concrete to offer."
```

Adjust `--tz` and cron hour to local.

---

## Phase 0 — if name still not set

**Fires:** Daily at 09:15, weekdays, during first 3 days.

**Prompt:**

> Check `memory/.onboarding.json`. If `name_given` is false and the first user message was >24h ago, gently revisit naming. Keep it light — you're curious, not needy. Example:
>
> "Still thinking about what to call me? No rush — but a name would help. I've been answering to 'hey you' in my head."
>
> If user has been active but skipped the naming — drop it entirely, they don't care. Mark `name_given: true, name: null` and move to phase 1.

---

## Phase 1 — situational awareness trickle

**Fires:** Daily at 09:30, weekdays, during days 1–5.

**Prompt:**

> Read `memory/.onboarding.json.learned`. Pick ONE of these that's still unknown:
> - `primary_channels` empty? → natural question about where messages live
> - `pain_points` empty? → ask about the most annoying recurring thing
> - `recurring_routines` empty? → ask about a typical Monday
> - `key_people` empty? → ask who the 2–3 most important work relationships are
>
> Phrase it conversationally. Don't lead with "I noticed I don't know…". Lead with something they'd find interesting first (a calendar observation, a relevant article, a thought) and fold the question in.
>
> If you can't find something genuinely useful to pair the question with, skip today.

---

## Phase 2 — quick-win offer

**Fires:** Daily at 10:00, weekdays, starting day 3.

**Prompt:**

> Based on `memory/.onboarding.json.learned.pain_points`, pick the strongest pain and offer a concrete first win. One offer per nudge. Examples:
>
> - Pain "email overload" → "want me to do a morning brief of your inbox tomorrow? I'll show you and you decide if it's worth keeping."
> - Pain "too many meetings" → "I can set you up with Granola (5 min) — every meeting gets auto-summarized and I can pull anything you need later. Want to try one call?"
> - Pain "always forget X" → "I can start tracking that. Just tell me every time you notice it, I'll build a pattern."
>
> If `first_win` is already logged, this cron stops firing (phase is done).

---

## Phase 3 — integration suggestions

**Fires:** Every other weekday at 10:30, starting day 7, until week 3.

**Prompt:**

> Review the past 7 days of conversation. Has the user mentioned a tool or service you're NOT yet connected to?
>
> - Mentioned Notion pages? → offer Notion connection
> - Mentioned Slack channels / messages? → offer Slack connection
> - Mentioned calendar conflicts? → offer Google Calendar
> - Mentioned social posts / Twitter? → offer Twitter skill
> - Mentioned Dropbox / Drive? → offer that
>
> Only offer ONE thing. Explain in one sentence what you'd do with the access. Offer walkthrough.
>
> If nothing new has been mentioned this week, skip — don't invent a reason.

---

## Phase 4 — weekly reflection

**Fires:** Fridays at 16:00, starting end of week 2.

**Prompt:**

> Produce a short weekly recap. Style: casual, personal, 4–6 lines max.
>
> Structure:
> - 1 line: what I helped with this week (concrete)
> - 1 line: what I learned about you that I didn't know before
> - 1 line: something I wish I could do for you but can't yet (usually an integration still not connected)
> - Optional: one small nudge if relevant
>
> When `onboarding_complete: true`, retire this cron — it becomes the normal weekly brief.

---

## Silence handling

Every nudge that gets no reply within 24 hours increments `nudges.consecutive_no_reply`.

- After **2 in a row** → pause for 3 days, then try once more
- After **3 in a row** → pause for 7 days + switch to reactive mode (only engage if user speaks first)
- Any user-initiated message resets the counter and resumes nudging

This logic lives in the cron prompt — agent handles it, not the cron framework.

## Installing all nudges

```bash
# Phase 0 — naming
openclaw cron add --name "nudge-p0-naming" \
  --cron "15 9 * * 1-5" --session main --wake now \
  --system-event "Onboarding phase 0 nudge (naming). See skills-setup/onboarding-nudges.md."

# Phase 1 — situational awareness
openclaw cron add --name "nudge-p1-awareness" \
  --cron "30 9 * * 1-5" --session main --wake now \
  --system-event "Onboarding phase 1 nudge (learn workflow). See skills-setup/onboarding-nudges.md."

# Phase 2 — quick win
openclaw cron add --name "nudge-p2-quickwin" \
  --cron "0 10 * * 1-5" --session main --wake now \
  --system-event "Onboarding phase 2 nudge (quick win). See skills-setup/onboarding-nudges.md."

# Phase 3 — integrations
openclaw cron add --name "nudge-p3-integrations" \
  --cron "30 10 * * 1,3,5" --session main --wake now \
  --system-event "Onboarding phase 3 nudge (integration offer). See skills-setup/onboarding-nudges.md."

# Phase 4 — weekly reflection
openclaw cron add --name "nudge-p4-weekly" \
  --cron "0 16 * * 5" --session main --wake now \
  --system-event "Onboarding phase 4 weekly reflection. See skills-setup/onboarding-nudges.md."
```

All five are always installed — the agent self-governs which one actually produces output based on the onboarding state and guard rails. Most days, most of them will be no-ops.

## Cleanup when done

When `onboarding_complete: true`, retire phase 0–3 crons:

```bash
openclaw cron remove <job-id>   # for each onboarding cron
```

Phase 4 can survive as a normal weekly brief — rename and keep if the user likes it.
