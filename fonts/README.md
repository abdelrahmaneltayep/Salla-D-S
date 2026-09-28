# Fonts

**Ping AR + LT** is the only typeface in the system (Figma `Typography/Family/Font`, runtime `--font-main: "PingARLT"`).

| File | Weight | Figma style |
|---|---:|---|
| `PingARLT/PingAR+LT-Regular.otf` / `.woff2` | 400 | Regular |
| `PingARLT/PingAR+LT-Medium.otf` / `.woff2` | 500 | Medium |
| `PingARLT/PingAR+LT-Bold.otf` / `.woff2` | 700 | Bold |
| `PingARLT/PingAR+LT-Heavy.otf` / `.woff2` | 800 | Heavy (not used by the current text styles) |

`pingarlt.css` declares `@font-face` for both family names used across the system, so `tokens/tokens.css`
text styles (`"Ping AR + LT"`) and the Storybook runtime (`PingARLT`) resolve to the same files:

```html
<link rel="stylesheet" href="fonts/pingarlt.css" />
```

WOFF2 files were generated from the OTFs with fontTools; ship those on the web and keep the OTFs for design tools.
Production loads the same family from `https://cdn.salla.network/fonts/pingarlt.css`.

Ping AR + LT is a licensed commercial typeface; keep this repository private or confirm the license covers redistribution.
