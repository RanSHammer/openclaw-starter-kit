# Notion Integration — Setup Guide

Read and write Notion pages directly from your agent.

## Setup

### 1. Create an Internal Integration

1. Go to https://www.notion.so/my-integrations
2. Click **+ New integration**
3. Name it (e.g. "Alpha Agent")
4. Select your workspace
5. Set capabilities: **Read content**, **Update content**, **Insert content**
6. Click **Submit** → copy the **Internal Integration Token**

### 2. Store the API Key

```bash
mkdir -p ~/.config/notion
echo "secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" > ~/.config/notion/api_key
chmod 600 ~/.config/notion/api_key
```

### 3. Connect Pages to Your Integration

For each page/database you want the agent to access:

1. Open the page in Notion
2. Click **···** (top right) → **Connections**
3. Search for your integration name → **Confirm**

Without this step, the API returns 404 even if the key is valid.

## Making API Calls

All requests need two headers:

```
Authorization: Bearer <api_key>
Notion-Version: 2022-06-28
Content-Type: application/json
```

Note: The Notion-Version header is **required**. Omitting it causes errors.

### Read a Page

```bash
API_KEY=$(cat ~/.config/notion/api_key)
PAGE_ID="your-page-id-here"  # from the page URL

curl -s -H "Authorization: Bearer $API_KEY" \
     -H "Notion-Version: 2022-06-28" \
     "https://api.notion.com/v1/pages/$PAGE_ID"
```

### Read Page Blocks (the actual content)

```bash
curl -s -H "Authorization: Bearer $API_KEY" \
     -H "Notion-Version: 2022-06-28" \
     "https://api.notion.com/v1/blocks/$PAGE_ID/children"
```

### Create a New Page

```bash
curl -s -X POST \
  -H "Authorization: Bearer $API_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": { "page_id": "PARENT_PAGE_ID" },
    "properties": {
      "title": {
        "title": [{ "text": { "content": "My New Page" } }]
      }
    },
    "children": [
      {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
          "rich_text": [{ "text": { "content": "Hello from Alpha!" } }]
        }
      }
    ]
  }' \
  "https://api.notion.com/v1/pages"
```

### Append Content to an Existing Page

```bash
curl -s -X PATCH \
  -H "Authorization: Bearer $API_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{
    "children": [
      {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
          "rich_text": [{ "text": { "content": "Appended content here." } }]
        }
      }
    ]
  }' \
  "https://api.notion.com/v1/blocks/$PAGE_ID/children"
```

### Query a Database

```bash
DB_ID="your-database-id"
curl -s -X POST \
  -H "Authorization: Bearer $API_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{"filter": {}, "sorts": []}' \
  "https://api.notion.com/v1/databases/$DB_ID/query"
```

## Getting Page/Database IDs

From a Notion URL:
```
https://www.notion.so/My-Page-Title-f4655509875a43ecafd51e53f7d01c54
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                     This is the page ID (remove hyphens or keep them)
```

## Block Types Reference

Common block types for creating content:

| Type | Use |
|------|-----|
| `paragraph` | Regular text |
| `heading_1` / `heading_2` / `heading_3` | Headers |
| `bulleted_list_item` | Bullet point |
| `numbered_list_item` | Numbered list |
| `to_do` | Checkbox |
| `code` | Code block |
| `divider` | Horizontal line |
| `quote` | Block quote |
| `callout` | Highlighted callout box |

## Practical Use Cases

- **Log agent activity** — append daily summaries to a Notion log page
- **Read task databases** — pull open tasks into your agent's context
- **Create research pages** — save web research to Notion automatically
- **Update CRM entries** — write contact notes from your contacts/ directory
- **Morning brief archive** — save each morning briefing to Notion for reference

## Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| 401 Unauthorized | Bad API key | Re-check `~/.config/notion/api_key` |
| 404 Not Found | Page not connected | Add integration to the page (step 3) |
| 400 Bad Request | Missing Notion-Version header | Add the header |
| 403 Forbidden | Integration lacks capability | Check integration settings at notion.so/my-integrations |
