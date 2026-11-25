---
name: dautel-brand
description: "Apply the Dautel brand to anything visual or written for the firm: the voice rules (\"we\", sentence case, no emoji, no hype, no fake metrics, privacy lock), the right theme (Dautel for the firm's own sites; Catppuccin for software, demos, social and customer work; the client's own brand when it has one), the role color tokens and their meanings, JetBrains Mono and Manrope, shapes, the Terminal Monogram logo rules and accessibility. Use for any website, app, slide, document, graphic, thumbnail or video."
---

# Dautel brand and design system

*Marketing skill for the DIO expert team.* Apply the Dautel Design System and company voice to any site, app, document, slide, graphic or video.

## When to use

Anything visual or published: sites, apps, slides, documents, social graphics, thumbnails, video graphics. The design system files are in `design-system/` (copied from gen-skeptic/dautel_brand); `design-system/BRAND.md` is the full rule set and `design-system/index.html` the reference page.

## Voice

- Company copy says **"we"**; "I" only in Erich's own founder posts and personal portfolio pages.
- Plain, confident and specific; **sentence case** for headlines and buttons; **no emoji, no hype, no fake metrics**, no decorative status. Status shown must be real.
- Section titles are short noun phrases with the terminal prompt: `>_ Selected systems`.
- **Privacy lock:** never publish a street address, personal phone, personal email or a resume with contact details.

## Which theme

| Where | Theme |
| --- | --- |
| The firm's own sites: dautel.io, home.dautel.cloud, its landing and campaign pages | **Dautel** (`data-theme="dautel"`) |
| Software, examples and demos, social graphics and video, customer sites | **Catppuccin**: Mocha by default; Macchiato, Frappé or Latte when there's a reason |
| A client with its own brand | **The client's brand**, without the Dautel mark |
| A client without a brand | Catppuccin, the client's name in mono, no Dautel mark |

## In code

- Load `design-system/dautel.css` once and set `data-theme` on `<html>`.
- Style only with role tokens: `var(--ink)`, `var(--ink-soft)`, `var(--surface)`, `var(--surface-strong)`, `var(--text)`, `var(--muted)`, `var(--quiet)`, `var(--rule)`, `var(--blue)`, `var(--mint)`, `var(--lavender)`, `var(--peach)`, `var(--danger)`. **Never hard-code hex values or other fonts.**
- Type and components: `.display`, `.lead`, `.section-title`, `.label`, `.micro`; `.button.button-primary`, `.section-heading`, `.panel`, `.panel-cut`, `.topology-node`, `.topology-status`, `.contact-form`, `.dot-grid`, `.container`.

## Color meaning (one accent per element)

- **blue:** primary action, the `>_` prompt, focus, Agents.
- **mint:** live or healthy status, secondary action, success, Infrastructure.
- **lavender:** the descriptor, Operations.
- **peach:** contact actions only.
- **danger:** errors, always with a word.

## Type and shape

- **JetBrains Mono** (the Nerd Font where installed) for navigation, controls, labels and short headings; **Manrope** for prose. Section titles start with a blue `>_`.
- Small radii only, **no pills**; 12px clipped corners on feature panels; 1px hairlines; dot and line grids drawn, never washed. **No shadows, gradients, glow or glassmorphism.**
- Motion: 160ms color and small lifts; `prefers-reduced-motion` turns it off.

## Logo

- The Terminal Monogram files in `design-system/logos/`, used as provided, on `ink` or another approved dark surface; lockup 220px or wider, mark 24px or larger; alt text "Dautel Intelligent Operations".
- Never stretch, rotate, outline, recolor, add effects, or place it on a busy image. Never on customer work that has its own brand.

## Accessibility

WCAG 2.1 AA contrast (keep `quiet` for icons and large text only), a visible blue focus ring with 4px offset, full keyboard paths. Latte's green and peach are under 3:1 on its base: use them only as fills or outlines beside words in `text`.

## Non-web media

Slides, video, images and print use the palette values of the right theme from `dautel.css`, the same fonts and the same shape rules. `quality-reviewer` fails branded work that breaks these rules.

## Used by

`content-marketing`, `web-developer-designer`, `trainer-curriculum`, `ux-ui-designer`, `full-stack-developer`, `mobile-developer`, `technical-writer`, `marketing-director`, `social-media-manager`, `youtube-producer`, `video-editor`, `graphic-designer`, `community-manager`, `paid-ads-specialist`, `podcast-webinar-producer`, `quality-reviewer`.
