# Design Systems — DESIGN.md for AI Design Tools

Encode your brand once as a `DESIGN.md` file, and every AI design tool (Claude Design, Stitch, Cursor, etc.) will output on-brand work from that single source of truth.

## Why

Without a design system file, every time you ask an AI to make a deck, landing page, or one-pager, you have to re-explain:

- Our brand colors are…
- The font is…
- We use this gradient for hero moments…
- Never use these cliches…

Repeating this per-session wastes tokens and produces inconsistent output. `DESIGN.md` is the fix — it's a markdown spec ([from Google Labs / Stitch](https://github.com/google-labs-code/design-md)) that any participating tool reads and applies.

## Architecture

```
design-systems/
├── company-one/
│   └── DESIGN.md
├── company-two/
│   └── DESIGN.md
└── personal/
    └── DESIGN.md
```

One folder per brand. Drag the `DESIGN.md` into the AI design tool as context — it handles the rest.

## What goes in a DESIGN.md

At minimum:

1. **Brand voice** — tone, do/don't list for writing
2. **Color palette** — primary, secondary, semantic colors with hex codes
3. **Gradients** — named gradient recipes if you use them
4. **Typography** — font families + type scale
5. **Spacing** — your grid/scale (e.g. 8-point grid)
6. **Shape** — border radii, shadows
7. **Components** — buttons, cards, section labels (how they look, when to use)
8. **Imagery rules** — what kind of photos/illustrations/icons to use

Optionally:
- Motion (easings, durations)
- Dark mode tokens
- Accessibility targets
- AI tool guidance section (anything weird you've learned)

## How to build one

**Option 1: From existing Figma**
1. Export color tokens and typography from Figma
2. Describe components in plain language
3. Format as markdown following the sections above

**Option 2: Have the AI do it**
1. Share your Figma link with Claude Design
2. Ask: "Generate a DESIGN.md for this brand system"
3. Review, refine, save

**Option 3: Distill from an existing brand guideline PDF**
1. Extract the text from the PDF
2. Paste it into Claude with: "Convert this into a DESIGN.md following the spec at github.com/google-labs-code/design-md"

## How AI tools use it

Tools with native DESIGN.md support: Stitch (Google), Claude Design (newer versions), some IDE AI features.

For tools that don't natively parse it: just paste the file as context in the prompt. LLMs do the right thing with it.

## Example structure

```markdown
# Acme Inc. — Design System

## Brand Identity
Voice: confident, technical, premium. No hype. No emoji in marketing.

## Tokens

### Colors
- Primary: #3346F2
- Accent: #DC8AE0
- Background: #F6F6F6

### Typography
- Primary font: Montserrat 300-900
- Secondary: Raleway 300-800
- Type scale: 12 / 14 / 16 / 18 / 21 / 26 / 42 / 56 / 64 / 84 / 96 / 125

### Spacing
8-point grid: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128

## Components
### Primary button
- Background: var(--primary)
- Text: white
- Radius: 8px
- Padding: 12px 24px

## Do & Don't
✅ Use one dominant gradient per viewport
❌ Never use pure black — use #070707 instead
```

## Maintenance

- Review quarterly with the designer/brand owner
- Add new components as they appear
- Update when rebranding
- Keep it under 500 lines — split if it grows beyond that

## The payoff

Once installed, every deck, landing page, one-pager, pitch, or graphic you ask an AI to make — it looks like your brand. No per-session rexplaining. No inconsistency. No lazy defaults.
