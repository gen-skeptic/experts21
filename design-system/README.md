# Dautel Design System (copy)

A copy of the `Dautel_style/` folder of [gen-skeptic/dautel_brand](https://github.com/gen-skeptic/dautel_brand), the canonical source. Change the design system there first, then copy it here. The agents use it through the `dautel-brand` skill, and the web app in `web/` uses its tokens and fonts.

| Path | What |
| --- | --- |
| [`BRAND.md`](BRAND.md) | Brand rules: identity, voice, color, type, shape, motion, icons, components |
| [`dautel.css`](dautel.css) | The stylesheet: five themes (Catppuccin Mocha default, Macchiato, Frappé, Latte, Dautel), fonts, base styles, components |
| [`index.html`](index.html) | Example page using the stylesheet, logo and favicon |
| [`logos/`](logos/) | Terminal Monogram logo, mark and favicon (SVG) |
| [`fonts/web/`](fonts/web/) | Manrope and JetBrains Mono web fonts plus `fonts.css`, for offline projects |

## How the firm uses the themes

| Where | Theme |
| --- | --- |
| The firm's own sites: dautel.io, home.dautel.cloud, its landing and campaign pages | **Dautel** (`data-theme="dautel"`) |
| Software, examples and demos, social graphics and video, customer sites (and this repository's web app) | **Catppuccin** (Mocha unless there's a reason to pick another) |
| A client with its own brand | The client's brand, without the Dautel mark |

Company copy says "we"; `BRAND.md`'s first-person "I" applies only to Erich's own founder posts and portfolio pages.

## Fonts on this laptop (Omarchy / Arch Linux)

The installable JetBrainsMono Nerd Font (16 styles, 38 MB) is left out of this copy. Omarchy already ships JetBrainsMono Nerd Font as its default font. On any other Arch Linux setup, install it from the official repositories:

```bash
sudo pacman -S ttf-jetbrains-mono-nerd
```

Fonts are under the SIL Open Font License (`fonts/web/LICENSE-*.txt`). The logos are the property of Dautel Intelligent Operations.
