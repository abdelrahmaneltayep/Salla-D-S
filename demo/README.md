# Screen demo — إدارة الطلبات (orders list ↔ detail)

`index.html` composes a full merchant-dashboard screen from the design system:

- **Header**: a 1:1 build of the Figma **Header** component (`figma/exports/header/`, spec in `docs/specs/header.md`): the 92 px title bar (real Salla logo, primary tabs with the mint active pill, setup ring 2/7, action icons, avatar + name + "جديد" tag), the 64 px subcategory row (secondary tabs, "مشمر" gradient pill, help-centre button), the breadcrumb row and the page-title row with its buttons.
- **Body**: search bar (`s-input` + filter button), the three-column list ↔ detail layout from [docs/patterns.md](../docs/patterns.md) — status rail, grouped order list (`s-checkbox` rows, selected row tint), detail panel with action bar (`s-dropdown`, `s-button`), `s-alert-box`, order/customer card (`s-avatar`, `s-tag`), payment, shipping, products table and a footer with `s-toggle` and actions.
- **Floating chips**: support bubble and activity-log button.

It loads the real Twilight runtime from the repo (`storybook/static/admin-ui.esm.js` + `styles.css`), so every `s-*` element is the production web component, and the semantic Figma tokens from `tokens/tokens.css` drive the shell layout (`--salla-background-primary-primary`, `--salla-radius-xl`, …). Icons are inlined from `icons/svg/outline/`.

![demo](../docs/images/demo-orders.png)

## Run

```bash
npx serve .            # from the repository root, then open http://localhost:3000/demo/
# or: python3 -m http.server 8080  →  http://localhost:8080/demo/
```

The typeface loads from `fonts/pingarlt.css` (Ping AR + LT, in the repo). The Hugeicons icon font still
loads from `cdn.salla.network`; the checkbox tick, alert close ✕ and dropdown chevrons inside the
components use it.

## Adapting

Copy the `<header>` / `.subnav` block for any section, swap the tabs, and drop any pattern from
`docs/patterns.md` into `<main class="page">`. Component attributes are documented per component in
`docs/storybook/` (e.g. [button](../docs/storybook/button.md), [tag](../docs/storybook/tag.md)).
