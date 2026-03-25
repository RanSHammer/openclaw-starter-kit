# Browser Automation — OpenClaw Built-In

OpenClaw includes a built-in headless browser (powered by browser-use). No extra setup needed — just start using it.

## Basic Operations

```
# Start a browser session / navigate
browser_navigate(url="https://example.com")

# Take a snapshot (DOM tree — use for decisions)
browser_snapshot()

# Take a screenshot (visual — use for sending to user)
browser_screenshot()

# Click an element (use ref from snapshot)
browser_click(ref="f2e3a")

# Type into a field
browser_type(ref="f2e1b", text="hello world")

# Wait for page to settle
browser_wait(ms=1000)
```

## The Golden Rule

> **Always snapshot before clicking.**

The snapshot gives you `ref` IDs for every interactive element. Never guess at element selectors — get them from the snapshot.

```
# Wrong ❌
browser_click(selector="#submit-btn")

# Right ✅
snapshot = browser_snapshot()
# Find ref for submit button in snapshot → e.g. "f2e9c"
browser_click(ref="f2e9c")
```

## Common Use Cases

### Filling a Form
```
browser_navigate(url="https://someform.com/apply")
browser_snapshot()  # get refs
browser_click(ref="f2e1a")  # click name field
browser_type(ref="f2e1a", text="Jane Smith")
browser_click(ref="f2e1b")  # click email field
browser_type(ref="f2e1b", text="jane@example.com")
browser_snapshot()  # verify before submitting
browser_click(ref="f2e9f")  # submit
```

### Taking a Screenshot for the User
```
browser_navigate(url="https://dashboard.example.com")
browser_wait(ms=2000)  # let it load
screenshot = browser_screenshot()
# Send screenshot via message tool to your channel
```

### Submitting to a Directory / Awesome List
```
browser_navigate(url="https://directory.example.com/submit")
browser_snapshot()
# Fill in fields, attach links, submit
```

## Key Tips

1. **Dismiss popups first.** Cookie banners, consent modals, chat widgets — snapshot shows them. Click dismiss/accept before doing anything else.

2. **Use `targetId` to stay in the same tab.** If the browser returns a `targetId`, pass it to subsequent calls to avoid opening new tabs.

3. **Snapshot vs Screenshot:**
   - `snapshot` = DOM tree with refs → use for navigation decisions
   - `screenshot` = visual image → use for "show me what you see"

4. **iFrames need inner refs.** If a form is inside an iframe, the refs are inside the iframe's context. Snapshot will show this.

5. **Wait after navigation.** Dynamic pages (React, SPAs) need a beat to render. Use `browser_wait(ms=1500)` after navigating.

6. **Multi-step flows:** Keep a variable holding the `targetId` so you're not spawning a new browser for each step.

## What Works Well

- Web form submissions
- Sign-up flows
- Taking "proof" screenshots
- Submitting to directories and awesome lists
- Basic web scraping when Lightpanda isn't enough
- Checking if a site is down or has changed

## What Doesn't Work Well

- Sites with heavy bot detection (Cloudflare, reCAPTCHA, hCaptcha)
- File downloads (use `fetch` or `curl` instead)
- Browser extensions or desktop apps
- Login flows using passkeys / WebAuthn

## See Also

- `TOOLS.md` → Browser automation tips & SevenRooms iframe notes
- `GITHUB.md` → Submitting PRs to GitHub repos (gh CLI is better than browser for this)
