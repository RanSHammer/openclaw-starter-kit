# Computer Use — Screen, Keyboard & Mouse Control

Let your agent see your screen and optionally take actions on it (click, type, scroll). macOS-native stack, no Docker, no VMs.

## Why Computer Use

- Verify UI state before taking action ("is the form saved?")
- Extract data from apps that don't have APIs
- Automate repetitive Mac tasks
- Drive web apps that resist normal automation

## Philosophy (Safety)

Computer use is powerful. The safety rule this kit recommends:

> **Always ask before touching the screen.**

Your agent announces the action (`"I'm about to click X at (Y,Z) — OK?"`), waits for `yes`, then acts. No automation without a human-in-the-loop checkpoint.

Set this expectation in `SOUL.md`:

```
## Computer Use Protocol
Before clicking, typing, or scrolling on the Mac:
1. Take a screenshot
2. Describe what you see and what you want to do
3. Ask Ran "OK to proceed?"
4. Only act after explicit approval
```

## Install the toolkit

```bash
# Native macOS mouse/keyboard control
brew install cliclick

# Full browser automation (real Chromium)
npm install -g playwright
npx playwright install chromium

# OCR (optional, for reading text from screenshots)
brew install tesseract

# Screen recording/video (usually already installed)
brew install ffmpeg
```

macOS built-ins you already have:
- `screencapture` — take a screenshot of screen/window/region

## Grant permissions

macOS will prompt when your agent first uses these:

1. **Accessibility** (for cliclick) — System Settings → Privacy & Security → Accessibility → add your terminal / OpenClaw
2. **Screen Recording** (for screencapture) — System Settings → Privacy & Security → Screen Recording → add your terminal / OpenClaw

Test both work with a safe read-only call:

```bash
cliclick p           # prints current cursor position
screencapture -x /tmp/test.png && ls -la /tmp/test.png
```

## Common recipes

### Take a screenshot + describe

```bash
screencapture -x /tmp/screen.png
```

Then your agent passes the file to the image/vision tool for description.

### Move the mouse (no click)

```bash
cliclick m:500,300
```

### Click at coordinates

```bash
cliclick c:500,300    # single click
cliclick dc:500,300   # double click
cliclick rc:500,300   # right click
```

### Type text

```bash
cliclick t:"Hello world"
```

### Keyboard shortcut

```bash
cliclick kd:cmd t:"a" ku:cmd   # Cmd+A (select all)
```

### Drive a browser end-to-end (Playwright)

For anything more complex than a click, use Playwright. A small Node script can open a real Chromium, navigate, fill forms, extract data, and take screenshots — much more reliable than cliclick for web apps.

## Alternatives (not installed by default)

- **Claude Cowork** (Anthropic) — visual agent that uses your Mac; set up via Claude desktop app
- **OpenAI computer use** — via the API
- **Astropad Workbench** — iPhone/iPad remote control of your Mac (not really agent-facing, but useful)

These are session-based tools. The lightweight `cliclick` + `screencapture` stack is better when you want your persistent agent to just "check on something" or "click the save button" without spinning up a whole session.

## When NOT to use computer use

- When an API exists — always prefer API
- For headless/unattended work — computer use requires the screen to be awake
- For sensitive actions (banking, medical portals) — do it yourself

## What to add to your workspace

After installing, add this to `memory/infra.md`:

```markdown
## Computer Use
- Accessibility permission: granted
- Screen Recording permission: granted
- Tools: cliclick, playwright, screencapture, tesseract
- Safety rule: always ask before clicking/typing
```
