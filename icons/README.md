# Icons

Salla's icon set, extracted from the Figma library **Icons DS_V.1** (`figma/source/Icons_DS_V.1.fig`).
The library is a repackaged **Hugeicons Pro** set (Rounded type), so the names match Hugeicons
(`add-01`, `bubble-chat`, `shopping-cart-02`, …) and the merchant dashboard's Figma components
(`add-01-outline`, `add-01-filled`).

| Folder | Figma variant | Salla DS name | Count |
|---|---|---|---|
| `svg/outline/<name>.svg` | `Style=Stroke, Type=Rounded` | `<name>-outline` | 3,886 |
| `svg/filled/<name>.svg`  | `Style=Solid, Type=Rounded`  | `<name>-filled`  | 3,886 |

All icons are `24×24`, `viewBox="0 0 24 24"`, and use `fill="currentColor"` so they recolor with CSS
`color`. Stroke icons are shipped as filled outlines (Figma stores the outlined stroke geometry), so
no `stroke-width` is needed and rendering matches Figma exactly.

```html
<img src="icons/svg/outline/add-01.svg" width="20" height="20" alt="" />
<!-- or inline the SVG and set color: -->
<span style="color: var(--salla-icon-primary)"> …svg… </span>
```

## Files

- `manifest.json` — one entry per icon: name, Hugeicons category, keyword description (when the
  library has one), paths of both variants, and whether the name exists in the merchant DS Figma
  (`inSallaDS.filled` / `inSallaDS.outline`).
- `categories.json` — icon counts per Hugeicons category (59 categories).
- `figma-icon-names.json` — the 4,010 `Icons/Filled` + 4,004 `Icons/Outline` symbol names found on
  the *Main Components (Full)* page of **Merchant - Storybook DS** (see `docs/components/`).
- `flags.json` — the 265 `Flag/<country-code>` symbols in the merchant DS (not exported as SVG yet).

## Coverage vs. the merchant DS

| | Names in merchant DS | Present in this icon set | Missing |
|---|---:|---:|---:|
| Filled  | 4,010 | 3,853 | 157 |
| Outline | 4,003 | 3,846 | 157 |

The ~157 missing names (e.g. `activity-01`, `apple-vision-pro`, `arc-browser`, `campfire`) are newer
Hugeicons additions that exist in the merchant DS Figma but not in this `Icons DS_V.1` file; the DS
file also carries `Saudi-Riyal`. Re-export them from Figma (`download_assets` / SVG export on the
`Icons/Filled` and `Icons/Outline` frames) to close the gap. 31 icons in this file are not referenced
by the merchant DS (`1st-brecket*`, `3d-*`, `4k`, …).

## Regenerating

```bash
cd scripts/fig-decode && npm install
unzip -o ../../figma/source/Icons_DS_V.1.fig -d ../../figma/source   # yields canvas.fig
node decode.mjs ../../figma/source/canvas.fig ../../.fig-out
node validate.mjs ../../.fig-out
```

`decode.mjs` documents the `fig-kiwi` container (zstd-compressed kiwi message), the path-command
blob grammar and every rendering choice; `REPORT.md` next to it lists the known caveats (15 solid
icons that use white overlays instead of cut-outs, one stray instance in `transmission`).

## Licensing

Hugeicons Pro is a commercial icon library. Keep this repository private, or confirm Salla's
Hugeicons Pro license permits redistributing the SVG sources, before making it public.
