# Salla Design System

The merchant-dashboard design system of [Salla](https://salla.sa), moved out of Figma and Storybook
into a versioned repository: **design tokens**, **icons**, **illustrations**, a full **component
inventory** with variant properties, and **reference markup/specs** for the core components.

Sources of truth (this repo is a snapshot of them, dated 2026-09-28):

| Source | Where | What we took |
|---|---|---|
| Figma library **Merchant - Storybook DS** | file `zuGhoKg2BaBIYUreKuSBGY`, component page on branch `dnmyqzYKK9dUJjVHuIWMDS` (*Main Components (Full)*, node `27713:61`) | variables → tokens, component inventory, section screenshots, design-to-code specs |
| Figma library **Icons DS_V.1** | `figma/source/Icons_DS_V.1.fig` (uploaded export) | 3,886 icons × 2 styles as SVG |
| Storybook (Twilight web components) | <https://dashboard-ui-components.pages.dev/> | *not captured yet* — see [Storybook](#storybook) |

## Layout

```
tokens/        tokens.json (DTCG), tokens.css (--salla-* custom properties), tokens.flat.json, tailwind.preset.cjs
icons/         svg/outline/*.svg, svg/filled/*.svg, manifest.json, categories.json, flags.json, figma-icon-names.json
illustrations/ png/ renders of the 20 empty-state illustrations (+ node ids to re-export as SVG)
docs/          foundations.md, components/ (one page per Figma section), specs/ (design-to-code reference), images/
figma/         variables.json (merged Figma variables), components.json (inventory), snapshots/ (raw dumps), source/ (.fig)
storybook/     placeholder + sync script target
scripts/       build_tokens.mjs, build_inventory.py, sync_storybook.mjs, fig-decode/ (the .fig → SVG decoder)
```

## Tokens

`figma/variables.json` is the merged output of the Figma variable definitions used across every
section of the component page (300 variables). `scripts/build_tokens.mjs` turns it into:

- `tokens/tokens.css` — `--salla-<path>` custom properties (colors, spacing, radius, typography, shadows).
- `tokens/tokens.json` — nested DTCG-style tokens (`$type`, `$value`, Figma name in `$extensions`).
- `tokens/tailwind.preset.cjs` — a Tailwind preset (`colors`, `spacing`, `borderRadius`, `fontSize`, `boxShadow`, `fontFamily`).

Key values: primary `#004956`, secondary (mint) `#a4ffe5`, danger `#f55157`, success `#00af6c`,
info `#5196f3`, warning `#ffaf44`, font **Ping AR + LT** (400/500/700), text sizes 10/12/14/16/18/20/24,
radius 2/4/8/9999, spacing 2–56 px. Full tables: [docs/foundations.md](docs/foundations.md).

Note the Figma names are kept verbatim, typos included (`seconadry`, `Descreptive`), because the
reference code from Figma references them as CSS variables. Two collections overlap
(`spacing/*` vs `Spacing/Sizes/*`, `radius/*` vs `Radius/Sizes/*`); `radius/md` is `4` in most
sections and `8` in Loader/Status (recorded in `figma/snapshots/variables/conflicts.txt`).

```css
@import "salla-design-system/tokens/tokens.css";
.btn-primary { background: var(--salla-background-secondary-seconadry); color: var(--salla-text-primary-primary); border-radius: var(--salla-radius-xl); }
```

## Components

[docs/components/README.md](docs/components/README.md) indexes the 28 sections / 118 component sets /
~1,900 variants of the Figma page, each with its variant properties, node ids, Figma links and a
screenshot. Highlights:

| Section | Component sets | Notes |
|---|---|---|
| Button | 441 variants | Variant × Appearance (default/outlined/link/link-auxiliary) × State × Size (32/40/48) × Layout |
| Inputs | 27 sets | text, textarea (rich text), amount, email, password, phone, counter, dropdown single/multiple, search, upload… |
| Table | 41 sets | cells (Header, Name, Amount, Status, Actions, …), mobile rows, header/footer, bulk edit, edit sheet |
| Alertbox / Status / Toggle / Checkbox / Radio / Avatar / Breadcrumb / Steps / Side menu / More Menu / Drop Down List / Loader / Header | — | see the index |

[docs/specs/](docs/specs/README.md) holds the design-to-code reference (Tailwind-flavoured markup +
token table) returned by Figma for one representative variant of each core component.

## Icons

3,886 Hugeicons-Pro-based icons in two styles, `icons/svg/outline/<name>.svg` and
`icons/svg/filled/<name>.svg`, all 24×24 and `currentColor`. See [icons/README.md](icons/README.md)
for the manifest, the coverage check against the Figma DS names (3,853 / 4,010 matched) and licensing.

## Illustrations

20 empty-state illustrations (PNG renders + Figma node ids), see [illustrations/README.md](illustrations/README.md).

## Storybook

The Storybook host was blocked from the environment that assembled this repo, so no story markup is
included yet. Run `node scripts/sync_storybook.mjs` from a machine that can reach it to capture the
rendered HTML of every story into `storybook/`.

## Regenerating

```bash
npm run build            # tokens + inventory docs
node scripts/build_tokens.mjs
python3 scripts/build_inventory.py
```

To refresh from Figma: re-run `get_variable_defs` per section (see `figma/snapshots/variables/`) and
`get_metadata` on node `27713:61` (see `figma/snapshots/main-components.xml`), then rebuild.

## License / ownership

All assets are Salla's. The icon set derives from Hugeicons Pro (commercial); keep the repository
private unless the license permits redistribution.
