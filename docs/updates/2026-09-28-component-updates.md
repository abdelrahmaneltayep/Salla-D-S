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

## Second batch (`others.zip`) — 28 exports

| Component | Exports (`figma/exports/…`) | Where | Design ↔ code notes |
|---|---|---|---|
| **Alertbox** | `alertbox/alertbox` | [alertbox.md](../components/alertbox.md), gallery → AlertBox | 6 variants (info, warning, success, danger, neutral, primary) × 2 types (**Inline** tinted background with a 3 px start border, **White** card with colored border) × title on/off × transparent. Icon ⓘ at the start, ✕ at the end. `s-alert-box` covers the themes and `layout="flat"`; the white-card type maps to the default layout on a white surface. |
| **Avatar** | `avatar/avatar`, `avatar-stack`, `avatar-with-text`, `avatar-placeholder-images`, `bank-placeholder-images` | [avatar.md](../components/avatar.md), gallery → Avatar | 6 sizes (xs…2xl) × circular/rectangular × variants: image, image-fallback, person icon, brand icon, "+24" counter, with a green online dot on circular ones. AvatarStack: overlapping/spaced × default/compact with a trailing "+24". Runtime `s-avatar` has `size xs–lg`, `layout circular/rounded`, `initials`, `icon`, `status`; the 2xl size and the stack are compositions. |
| **Accordion** | `accordion/accordion`, `accordion-header`, `accordion-icon` | gallery → Accordion | Header states: default (white, + in a mint circle), hover (underlined title), open (light-mint background, − icon), active (mint), disabled (gray). Maps to `s-accordion` / `s-accordion-group`. |
| **Toast** | `toast/toast` | gallery → Toast (Figma-only section) | New: success / danger / warning / info toasts with icon, title, message, ✕ and a colored progress bar along the bottom. No Storybook story; the runtime ships toastify variables (`--toastify-*`). |
| **Qty / Counter** | `qty/quantity`, `qty/counter`, `qty/quantity-hotreload` | [inputs.md](../components/inputs.md), gallery → Qty | Stepper with − / + , focus ring `#5196f3`, disabled, and a delete (trash) variant when the value is 1; compact and default sizes. Maps to `s-qty`. |
| **OTP** | `otp/single-digit` | gallery → OTP | Single-digit cell states (default, hover, pre-active, active, filled, error). Maps to `s-otp` / `s-otp-input`. |
| **Telephone input** | `tel-input/phone-input` | gallery → Telephone Input | Country flag + code selector at the start, 7 states, AR/EN. Maps to `s-tel-input`. |
| **Textarea** | `textarea/textarea` | gallery → Textarea | Plain and rich-text (toolbar) variants × states. Maps to `s-textarea` / `s-editor`. |
| **Inputs** | `input/text-input`, `search-input`, `input-with-image`, `input-with-button`, `input-counter`, `amount-input`, `email-input`, `password-input` | [inputs.md](../components/inputs.md), gallery → Input | Shared anatomy: leading icon, placeholder, trailing helper ("وصف مساعد") and language switch `AR ▾`; states default, hover, pre-active (underline), active (blue border `#5196f3`), filled, disabled, each with an error twin (red border). Password adds hidden/visible and a requirements checklist. All map to `s-input` (`type`, slots `start`/`end`, `hasError`, description). |
| **Select / Dropdown** | `select/dropdown-single`, `dropdown-multiple`, `basic-dropdown-single`, `basic-dropdown-multiple` | [drop-down-list.md](../components/drop-down-list.md), gallery → Select | Trigger states plus the open list: search field with a teal start-bar, options, the selected option in light mint with ✓, and an "أضف: خيار جديد" add-new row. Maps to `s-select` (`searchable`, `multiselect`, `addMissingItem`) and `s-dropdown`. |

## Files added

```
figma/exports/button/button.{svg,png}
figma/exports/tag/tag.{svg,png}
figma/exports/breadcrumb/breadcrumb.{svg,png}
figma/exports/checkbox/checkboxfield.{svg,png}
figma/exports/tabs/{radiotext-tabs,secondary-tabs-list,header-secondary-tabs,primary-tabs-list,header-primary-tabs}.{svg,png}
figma/exports/calendar/{calendar-time-date,time,time-item,date-item,big-calendar-items}.{svg,png}
figma/exports/table/table-states.{svg,png} + desktop-*.png / mobile-*.png (from Figma)
figma/exports/{alertbox,avatar,accordion,toast,qty,otp,tel-input,textarea,input,select}/*.{svg,png}   (second batch)
```
