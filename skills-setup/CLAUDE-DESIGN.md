# Claude Design — AI-Generated Presentations, Landing Pages, One-Pagers

Claude Design (by Anthropic Labs, launched April 2026) turns a prompt + brand context into a real rendered design — not a template. It produces HTML you can deploy, or PPTX for slides. Dramatically better output quality than Gamma / Stitch for brand-aware work.

## Access

- URL: https://claude.ai/design
- Requires Claude Pro or Max subscription (already included if you have Claude)
- Browser-based — no install, no API

## Workflow

1. Go to claude.ai/design
2. Create a new project
3. Paste a well-structured prompt (more on this below)
4. Drop in design context files (logos, brand zip, DESIGN.md)
5. Let Claude Design generate
6. Iterate via chat: "make section 3 punchier", "tighten the hero"
7. Export as HTML, PPTX, or share link

## Writing a great prompt

The most important rule: **explain what the thing IS and WHAT IT NEEDS TO DO — let Claude Design decide how to design it.**

Bad:
```
Make slides with dark background and gold text about my company.
```

Good:
```
Create a 10-slide presentation titled "Company Roadshow May 2026"
for a 10-minute pitch at investor meetings.

What the company is:
[2-paragraph company description]

Slide structure:
1. Title — hook + byline
2. What we are — big facts
3. Product pillars — 4 of them
4. ...

Audience: institutional investors in Asia
Tone: confident, quantitative, premium

Content to include:
- [key stats]
- [must-mention facts]
```

Tell Claude Design the story — let it make design decisions from scratch. You'll be surprised.

## Pairing with DESIGN.md

If you have a `DESIGN.md` for your brand (see `DESIGN-SYSTEMS.md`), drop it in as context. Claude Design will:

- Pick up brand colors
- Use your fonts
- Apply your component recipes
- Follow your do/don't list

Without a DESIGN.md, Claude Design will invent a system. It usually picks tasteful defaults, but it won't match your actual brand.

## Output formats

- **HTML** — production-ready, deploy to Netlify/Vercel in one click
- **PPTX** — editable in PowerPoint/Keynote
- **Share link** — teammates-only (within your Anthropic workspace)

## When to use Claude Design vs alternatives

| Task | Tool |
|---|---|
| Quick slides, internal | Gamma (faster, less polished) |
| Production landing page | Claude Design |
| Brand-critical deck | Claude Design with DESIGN.md |
| Iterating with a team | Google Slides (sharing + comments) |
| Quick artifact / prototype | Stitch (Google's equivalent) |

## Limitations

- Browser-only — can't automate from API (yet)
- Share links only work for people in your workspace
- Complex animations / interactivity need hand-editing the HTML after

## Hosting the output (optional)

If you want a public URL for the generated HTML:

```bash
# One-time: install Netlify CLI
brew install netlify-cli

# Deploy
cd /path/to/generated/html
netlify deploy --create-site my-site-name --dir . --prod

# Later, redeploy
netlify deploy --prod --dir .
```

Output: `https://my-site-name.netlify.app` — works on mobile, shareable with anyone.

Add custom domain via Netlify's domain panel (either point DNS at Netlify or just use their subdomain).

## Pro tip: the two-step workflow

1. **First pass:** tight content prompt, no design instructions. See what Claude Design does.
2. **Second pass:** iterate via chat on specifics ("make it less corporate", "add a stats section", "tighten this slide").

Don't over-specify upfront. The tool is much better than you at design — give it room.
