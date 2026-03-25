# Subagents — Parallel Work & Multi-Model Workflows

Spawn parallel agents to do work simultaneously, then consolidate their results.

## Why Subagents?

Some tasks are naturally parallel:
- Research 3 topics at once instead of waiting for each
- Run expensive analysis on a cheaper model in the background
- Use GPT for web research + Opus for synthesis
- Process a batch of items without blocking your main session

## How It Works

OpenClaw supports spawning subagents via the session system. Each subagent:
- Gets its own context and model
- Runs independently (won't see your main session history)
- Reports back to you when done (push-based — no polling needed)

## Spawning a Subagent

In your cron or heartbeat prompts, you can instruct your agent to spawn subagents:

```
Spawn 3 parallel research subagents:
  1. Model: gpt-5.4 — Research [Topic A]. Return: 3-paragraph summary + 5 sources.
  2. Model: gpt-5.4 — Research [Topic B]. Return: 3-paragraph summary + 5 sources.
  3. Model: claude-opus-4-6 — Research [Topic C]. Return: 3-paragraph summary + 5 sources.

Wait for all 3 to complete (timeout: 120 seconds).
Consolidate results into a single report.
Send to [channel].
```

## Model Assignment Strategy

| Task | Best Model | Why |
|------|-----------|-----|
| Web research, fact-finding | GPT-5.4 | Strong search + reasoning |
| Long-form writing, synthesis | Claude Opus 4 | Best prose, nuanced |
| Simple data extraction | Claude Sonnet 4 | Fast + cheap |
| Local/private analysis | Qwen 3.5 397B (Ollama) | Free, no data leaves machine |
| Code generation | GPT-5.4 or Opus 4 | Both excellent |

## Example: Weekly Intelligence Brief

```
Spawn 4 research subagents simultaneously:

Subagent 1 (gpt-5.4):
  Search for [industry] news from the past 7 days.
  Return top 5 developments with sources.

Subagent 2 (gpt-5.4):
  Search for mentions of [company/project] on Twitter and news.
  Return sentiment summary + notable mentions.

Subagent 3 (claude-sonnet-4-6):
  Check GitHub for new repos/issues in [relevant repos].
  Return summary of activity.

Subagent 4 (claude-sonnet-4-6):
  Fetch prices for [crypto/stocks] and compare to last week.
  Return: current prices, % change, notable movements.

After all complete:
  Synthesize into a weekly brief (use claude-opus-4-6 for synthesis).
  Send formatted report to [channel].
```

## Consolidating Results

When subagents return:

```
You will receive results from 3 subagents.
Once all are in, combine them:
1. Start with executive summary (3 sentences)
2. Section per subagent's findings
3. End with "Key Actions" — 3 concrete things to do this week

Format: markdown headers, no walls of text, use bullets.
```

## Timeout Handling

Subagents can time out on slow tasks. Handle it gracefully:

```
If a subagent doesn't respond within 90 seconds:
- Mark that section as "⏳ Pending — check later"
- Continue with available results
- Don't fail the whole report over one slow subagent
```

## Local Subagents with Qwen (Ollama)

For private data or zero-cost analysis:

```bash
# Make sure Ollama is running
ollama serve &
ollama pull qwen3.5:397b  # or smaller: qwen2.5:7b for speed

# In OpenClaw config, add:
# model: ollama/qwen3.5
```

Use Qwen for:
- Processing personal files/documents locally
- Analysis that shouldn't leave your machine
- High-volume tasks where you don't want API costs
- Overnight batch jobs

## State Between Subagents

Subagents are stateless — they don't share memory. If Subagent 2 needs output from Subagent 1, you have two options:

1. **Sequential with handoff** — pass Subagent 1's output as context to Subagent 2
2. **File-based** — Subagent 1 writes to `/tmp/research-a.md`, Subagent 2 reads it

```
Subagent 1: Research [Topic A]. Save results to /tmp/research-a.md.

Subagent 2: Read /tmp/research-a.md. Use it as context. Now research [Topic B] and how it relates to Topic A.
```

## Practical Tips

- **Don't over-parallelize** — 3-5 subagents is usually the sweet spot
- **Give clear return formats** — "Return: 3 bullet points" beats "summarize it"
- **Cheaper models for extraction, expensive for synthesis** — Sonnet reads, Opus writes
- **Log subagent results** — write them to daily memory file for future reference
- **Test before scheduling** — run the subagent workflow manually before adding it to cron
