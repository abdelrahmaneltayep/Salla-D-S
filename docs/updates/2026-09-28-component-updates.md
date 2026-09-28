# Component updates — 2026-09-28

Updated Figma exports were delivered for seven components (`Updates.zip`). They are filed under
`figma/exports/<component>/` (SVG + PNG), embedded in the component pages under `docs/components/`,
shown as "التصميم في Figma" reference cards at the top of each section of the live gallery
(`demo/components.html`), and, where the demos use the component, applied to `demo/index.html`.

The Figma page *Main Components (Full)* itself was re-read from the branch and is byte-identical to the
snapshot in `figma/snapshots/`, so the variant inventories in `docs/components/` are still current.
The one new component set found in the library is **RadioText tabs** (published 2026-09-02).

| # | Component | Export | Where it now lives | Design ↔ code notes |
|---|---|---|---|---|
| 1 | **Table** | `table/table-states.svg` (all 18 states, 1927×11474) + 11 state renders from Figma | [docs/components/table.md](../components/table.md), gallery → Table | The runtime `s-table` covers search, sort, selection, pagination, empty state and custom slots. The Figma set adds: a **tabs row** above the header (`Status=Tabs`), a **title row**, a **filter-chips row** with removable chips and "إلغاء", a **bulk-selection banner** ("تنبيه! تم تحديد العملاء الموجودين في هذه الصفحة… حدد كل العملاء (2467)"), a header **more-menu** (تحديث البيانات / تخصيص الجدول), a **sticky header on scroll**, and the **mobile card layout** (order card with checkbox, thumbnails, price, relative date, status pill, ⋯). These rows/cards are compositions around `s-table` (use `s-tabs-group`, `s-tag closable`, `s-alert-box`, `s-dropdown`); the mobile cards have no runtime counterpart yet. |
| 2 | **Tags** | `tag/tag.png` | [docs/components/status.md](../components/status.md), gallery → Tag | Figma defines 7 themes (default mint, secondary, transparent, danger, info, warning, success) × 2 appearances (filled, subtle/outlined). `s-tag` has the same themes plus `feature`, `white`, `mahally`; `outlined` maps to the Figma subtle row. Pill radius `9999px`, 28 px height. |
| 3 | **Tabs + header** | `tabs/radiotext-tabs.png`, `tabs/secondary-tabs-list.png`, `tabs/header-secondary-tabs.png`, `tabs/primary-tabs-list.png`, `tabs/header-primary-tabs.png` | [docs/components/header.md](../components/header.md), gallery → Tabs, `demo/index.html` header | **RadioText tabs** is a new chip-style segmented control (mint active chip, white or transparent container, scroll arrow when overflowing) — nearest runtime is `s-tabs-group theme="buttons"`. **Secondary Tabs List** = underlined text tabs (active bold `#004956` with 2 px underline; "••• المزيد" overflow) — matches `s-tabs-group theme="underline"` and the demo's subcategory row. Header primary tabs: default (white text on teal), hover (light gray pill), active (mint pill) — implemented in the demo header. |
| 4 | **Breadcrumb** | `breadcrumb/breadcrumb.png` | [docs/components/bread-crumb.md](../components/bread-crumb.md), gallery → Breadcrumbs, demo header | Separators are light chevrons (`#bbbbbb`, now applied in the demo), inactive items `#737373`, current item `#004956` medium; collapsed middle items render as "•••" (runtime: `s-breadcrumbs max-visible-items`). Desktop and mobile variants share the same layout with 56 px vs 16 px padding. |
| 5 | **Button** | `button/button.png` (full matrix, 3200 px) | [docs/components/button.md](../components/button.md), gallery → Button | 7 variants (primary mint, secondary/white, feature gold, danger, success, info, warning) × 4 appearances (default, outlined, link, link-auxiliary) × 5 states × 3 sizes (32/40/48) × 2 layouts (default, circular). `s-button` maps Variant→`theme`, `--outlined`→`outlined`, link appearances→`theme="transparent"`, Size→`size sm/md/lg`, Layout→`layout="circular"`. Loading state shows a spinner in place of the label at the same width. |
| 6 | **Calendar** | `calendar/calendar-time-date.png`, `time.png`, `big-calendar-items.png`, `date-item.png`, `time-item.png` | [docs/components/drop-down-list.md](../components/drop-down-list.md), gallery → Calendar | Month/year header with chevrons, Arabic weekday names, **today** in muted teal (`#7fb8c3`-ish, `--primary-200`), **selected** day in mint, adjacent-month days `#bbb`; a **time row** (hours `:` minutes + ص/م toggle) with hover/edit spinner states. Runtime `s-calendar` supports `type` (date / time / datetime), `is24Hr`, `inline`, ranges — the AM/PM segmented toggle is the visual to match. |
| 7 | **Checkbox** | `checkbox/checkboxfield.png` | [docs/components/check-box.md](../components/check-box.md), gallery → Checkbox | `checkboxfield` = 20 px box + label (with required `*`) + 12 px description; states default, disabled (`#bbb` text), **disabled-info** (ⓘ next to the label, muted description) and **disabled-info-tooltip** (dark tooltip "You chose X, you can't do Y" with a "Change your choice" link). Runtime `s-checkbox` has `label`, `desc`, `required`, `disabled`, `indeterminate`; the info icon + tooltip combination is composed with `s-tooltip`. |

## Files added

```
figma/exports/button/button.{svg,png}
figma/exports/tag/tag.{svg,png}
figma/exports/breadcrumb/breadcrumb.{svg,png}
figma/exports/checkbox/checkboxfield.{svg,png}
figma/exports/tabs/{radiotext-tabs,secondary-tabs-list,header-secondary-tabs,primary-tabs-list,header-primary-tabs}.{svg,png}
figma/exports/calendar/{calendar-time-date,time,time-item,date-item,big-calendar-items}.{svg,png}
figma/exports/table/table-states.{svg,png} + desktop-*.png / mobile-*.png (from Figma)
```
