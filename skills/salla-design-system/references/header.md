# Header — app shell (Figma component `Header`, node 15895:36794)

Source of truth: `figma/exports/header/header.svg` in the Salla-D-S repo (carries both frames), implemented 1:1 in
`demo/header.css` + `demo/index.html`, and inlined into `assets/prototype-template.html` of this skill.
Colors are the Figma semantic tokens (`--salla-*`), fallbacks are the hex values below.

## Title bar (`.hd-top`)

| Item | Spec |
|---|---|
| Bar | `#004956` (`background/primary/primary`), **92 px** high, **64 px** side gutters. ≤1200 px: **88 px**, **24 px** gutters |
| Logo | `salla` wordmark `#A4FFE5`, 95.4 × 40, at the start (right in RTL) |
| Primary tabs | 40 px pills, radius **12**, padding 8, gap 4 between 24 px icon and 16 px/24 px text (weight 500), 8 px between tabs. Hover `rgba(255,255,255,.08)`. **Active**: `#A4FFE5` fill, `#004956` text, weight 700. First item is the hamburger "الكل" (20 px icon) |
| Tools (from the end) | account → settings → bell → messages → apps grid → search → setup ring. 24 px icons, stroke `#F4F4F4`, 16 px gaps |
| Setup ring | 38 px white disc, 30 px ring: `#EEEEEE` track, `#00AF6C` progress arc (2/7), 10 px `#00AF6C` label |
| Account | 48 px photo avatar with 1 px `#EEEEEE` border · name 14 px `#F8F8F8` over a 23 px "جديد" pill (1 px `#DBFFF6` stroke, radius 140, 12 px text) · 16 px chevron. 8 px gaps, 8 px inline padding |
| ≤1200 px | name + tag hidden; search, apps and messages fold into a **⋯** button placed between the avatar and settings |

## Subcategory bar (`.hd-sub`)

| Item | Spec |
|---|---|
| Bar | white, **64 px**, 12 px vertical padding, same gutters as above, 1 px `#EEEEEE` bottom border |
| Secondary tabs | 40 px, 16 px/24 px text, padding 8 × 2, 16 px gap. Inactive `#666` weight 500; **active** `#004956` weight 700 with a **2 px `#004956` underline** |
| Help | 32 px **rounded square** (radius 12), 1 px `#A4FFE5` border, white fill, 16 px `?` icon `#004956` — outermost at the end |
| مشمر (AI assistant) | 98 × 32 pill, radius 12, `#E6FFF9` fill, **1 px angular-gradient border** `#FFE895 → #FFAF83 → #E4BC8F → #2CF2C7 → #92F0FF`, 16 px chevron `#004956`, 12 px `#333` label, 18 px gradient disc with a sparkle. 8 px from the help button |

Below the bars, screens add the breadcrumb row (`.hd-crumbs`, 8 px × gutter padding, `#737373` items, `#BBBBBB` chevrons,
current item `#004956`) and the page-title row (`.hd-title`, 24 px/32 px bold `#004956` + action buttons).

## Usage

- Copy `<header>…</header>` and the `.hd-*` styles from `assets/prototype-template.html`; the icons are an inline
  `<symbol>` sprite (`<use href="#i-<hugeicon-name>">`) so the file stays self-contained.
- Change only: the active primary tab, the secondary tab labels, the breadcrumb, the page title and its buttons.
- Keep the DOM order — in RTL the first child renders at the right, which is how the Figma frame is laid out.
