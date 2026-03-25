# GitHub Workflows — gh CLI Setup

PRs, forks, issues, and directory submissions — all from your agent.

## Setup

### 1. Install gh CLI

```bash
# macOS
brew install gh

# Ubuntu/Debian
sudo apt install gh
```

### 2. Authenticate

```bash
gh auth login
# Choose: GitHub.com → HTTPS → Login with a web browser
# Follow the URL, paste the one-time code
```

Verify it worked:
```bash
gh auth status
```

### 3. Configure Git Identity

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

## Core Operations

### Fork a Repo

```bash
gh repo fork owner/repo-name --clone --remote
# This forks, clones locally, and sets upstream remote in one command
```

### Create a Branch

```bash
cd repo-name
git checkout -b my-feature-branch
```

### Open a PR

```bash
# After committing your changes:
gh pr create \
  --title "Add: something useful" \
  --body "Description of what this adds and why" \
  --base main
```

### Check PR Status / CI

```bash
gh pr status          # your open PRs
gh pr checks          # CI status on current branch
gh run list           # recent workflow runs
gh run view <id>      # details of a specific run
```

### Review PR Comments

```bash
gh pr view --comments  # see all comments on current PR
```

## Submitting to Awesome Lists

Awesome lists (and similar directories) follow a consistent pattern:

```bash
# 1. Fork the awesome list
gh repo fork sindresorhus/awesome --clone --remote

# 2. Create a branch
cd awesome
git checkout -b add-my-project

# 3. Edit the README.md to add your entry
# (Follow the existing format exactly)

# 4. Commit
git add README.md
git commit -m "Add [Your Project] to [Section]"
git push origin add-my-project

# 5. Open PR
gh pr create \
  --title "Add [Your Project]" \
  --body "Short description. Follows contribution guidelines." \
  --base main
```

**Format rules for awesome list PRs:**
- Match the exact formatting of existing entries
- Alphabetical order within sections (most lists require this)
- One entry per PR
- Description: start with capital, no period at end (usually)

## Bot PR Conventions

When your agent submits PRs on your behalf, use clear bot markers so maintainers can process them quickly:

```bash
gh pr create \
  --title "🤖🤖🤖 Add [Project] to [Section]" \
  --body "$(cat << 'EOF'
🤖 **Automated PR** — submitted by AI agent on behalf of @YourHandle

## What this adds

[Your project/entry]

## Why it belongs here

[1-2 sentence justification]

## Checklist
- [x] Follows contribution guidelines
- [x] Alphabetically ordered
- [x] Link works
- [x] No duplicate exists

*Questions? Ping @YourHandle — happy to review manually.*
EOF
)"
```

The `🤖🤖🤖` prefix is a community convention on some lists for automated submissions that request fast-track review.

## Monitoring Your PRs

```bash
# List all your open PRs across repos
gh pr list --author @me --state open

# Check a specific PR
gh pr view https://github.com/owner/repo/pull/123

# Watch for CI to pass
gh pr checks --watch
```

## Issue Workflows

```bash
# Create an issue
gh issue create --title "Bug: X doesn't work" --body "Steps to reproduce..."

# Comment on an issue
gh issue comment 42 --body "I can reproduce this on macOS 14.3"

# Close an issue with a comment
gh issue close 42 --comment "Fixed in #45"
```

## Agent Workflow Example

When your agent handles a GitHub submission autonomously:

```
1. Fork the target repo
2. Clone locally
3. Make the edit (README, config, etc.)
4. Commit with a clear message
5. Push to fork
6. Open PR with 🤖🤖🤖 prefix + full description
7. Report back: "PR opened at [URL]. CI shows [status]."
8. Monitor with `gh pr checks` — alert you if it fails
```

## Useful Shortcuts

```bash
gh repo view             # view current repo in browser
gh browse                # open current repo in browser
gh browse --branch main  # specific branch
gh api /repos/:owner/:repo/contents/README.md  # read a file via API
```

## Tips

- **One fork, many branches** — fork once, create a new branch for each PR
- **Always check existing PRs first** — `gh pr list --repo owner/repo` to avoid duplicates
- **Read CONTRIBUTING.md** — failing to follow it is the #1 reason PRs get closed
- **Squash before PR** — clean commit history makes maintainers happy: `git rebase -i HEAD~3`
- **Labels** — some repos label bot PRs. Ask: `gh label list` to see what's available
