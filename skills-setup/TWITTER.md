# Twitter/X Integration — Setup Guide

Post, reply, search, and like tweets from your agent.

## Setup

### 1. Create a Twitter Developer App

1. Go to https://developer.x.com/en/portal/dashboard
2. Apply for a developer account if you don't have one
3. Create a new **App** (or use an existing project)
4. Under **User authentication settings**, enable:
   - **OAuth 1.0a** (needed for posting as yourself)
   - Permissions: **Read and Write**
   - App type: **Web App** (use a dummy callback URL if needed)
5. Generate your keys under **Keys and Tokens**

### 2. Store Your Keys

```bash
mkdir -p ~/.config/twitter
cat > ~/.config/twitter/credentials.json << 'EOF'
{
  "api_key": "your_api_key_here",
  "api_secret": "your_api_secret_here",
  "access_token": "your_access_token_here",
  "access_token_secret": "your_access_token_secret_here",
  "bearer_token": "your_bearer_token_here"
}
EOF
chmod 600 ~/.config/twitter/credentials.json
```

### 3. Test It

```bash
# Quick test — get your own profile
BEARER=$(cat ~/.config/twitter/credentials.json | python3 -c "import sys,json; print(json.load(sys.stdin)['bearer_token'])")
curl -H "Authorization: Bearer $BEARER" \
  "https://api.twitter.com/2/users/me"
```

## Skill Setup

Install the twitter skill if you haven't:
```bash
clawhub install twitter
```

Then configure your handle in `SOUL.md` or the skill's config so the agent knows which account to use.

## Core Operations

### Post a Tweet

**Always draft first, post only on approval.**

```
# Agent workflow:
1. Draft tweet options (2-3 variants)
2. Send drafts to user via message tool
3. Wait for "post #2" or explicit approval
4. Then post
```

Never auto-post. One bad tweet > zero good tweets.

### Reply to a Tweet

```
# Include the tweet ID you're replying to
POST /2/tweets
{
  "text": "Great point! Here's my take...",
  "reply": { "in_reply_to_tweet_id": "1234567890" }
}
```

### Search Tweets

```
GET /2/tweets/search/recent?query=<your_query>&max_results=10
```

Good for:
- Monitoring brand mentions
- Finding engagement opportunities
- Researching trending topics in your niche

### Like a Tweet

```
POST /2/users/:id/likes
{ "tweet_id": "1234567890" }
```

## Content Strategy

Good agents don't just blast content — they participate.

### Tweet Mix (rough guide)
- **40% Thought leadership** — your take on industry news
- **30% Engagement** — replies, quotes, joining conversations
- **20% Brand/project updates** — announcements, milestones
- **10% Personal/behind the scenes** — humanizes the account

### Drafting Good Tweets

When asked to draft tweets, your agent should:

1. **Search first** — look at what's trending in your niche
2. **Reference real things** — link to articles, quote specific numbers
3. **Give options** — different vibes, different lengths
4. **Flag character count** — Twitter limit is 280 chars

### Prompt for Tweet Drafts

```
Search Twitter for trending topics in [topic].
Find 2-3 recent tweets with high engagement about [topic].
Draft 3 tweet options:
  A) Thought leadership take (strong opinion, no hedging)
  B) Question/engagement bait (invites replies)
  C) Project/brand angle (relevant mention without being spammy)

Format each with:
- The tweet text (count chars)
- Suggested time to post
- Accounts to @ mention or threads to join

Send as drafts. Do NOT post until approved.
```

## Cron Integration

```json
{
  "name": "tweet-suggestions",
  "schedule": "0 9,15 * * *",
  "prompt": "Draft 2 tweet suggestions for @YourHandle on [topic]. Send to [channel] for approval. Never auto-post.",
  "model": "claude-sonnet-4-6"
}
```

## Rate Limits (Free Tier)

| Action | Limit |
|--------|-------|
| Post tweets | 50/day |
| Search | 60 requests/15 min |
| Read tweets | 15 requests/15 min |
| Likes | 50/day |

Free tier is enough for 1 person's account. If you hit limits, spread posts across the day.

## Common Mistakes

- **Auto-posting** — always require human approval first
- **Posting duplicates** — track what you've already posted in a state file
- **Ignoring rate limits** — the API will 429 you if you search too aggressively in cron jobs
- **Forgetting context** — a reply without reading the thread looks dumb. Always fetch the thread first.
