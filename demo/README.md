# Screen demo — إدارة الطلبات (orders list ↔ detail)

`index.html` composes a full merchant-dashboard screen from the design system:

- **Header**: top bar (logo, primary nav with the active mint pill, tools cluster, setup ring, store switcher), secondary tab row with the section CTA (`s-button theme="secondary"`), breadcrumb (`s-breadcrumbs`).
- **Body**: search bar (`s-input` + filter button), the three-column list ↔ detail layout from [docs/patterns.md](../docs/patterns.md) — status rail, grouped order list (`s-checkbox` rows, selected row tint), detail panel with action bar (`s-dropdown`, `s-button`), `s-alert-box`, order/customer card (`s-avatar`, `s-tag`), payment, shipping, products table and a footer with `s-toggle` and actions.
- **Floating chips**: support bubble and activity-log button.

It loads the real Twilight runtime from the repo (`storybook/static/admin-ui.esm.js` + `styles.css`), so every `s-*` element is the production web component, and the semantic Figma tokens from `tokens/tokens.css` drive the shell layout (`--salla-background-primary-primary`, `--salla-radius-xl`, …). Icons are inlined from `icons/svg/outline/`.

![demo](../docs/images/demo-orders.png)

## Run

```bash
npx serve .            # from the repository root, then open http://localhost:3000/demo/
# or: python3 -m http.server 8080  →  http://localhost:8080/demo/
```

Fonts (PingARLT, Hugeicons font) load from `cdn.salla.network` as in production; the checkbox tick,
alert close ✕ and dropdown chevrons inside the components use that icon font.

## Adapting

Copy the `<header>` / `.subnav` block for any section, swap the tabs, and drop any pattern from
`docs/patterns.md` into `<main class="page">`. Component attributes are documented per component in
`docs/storybook/` (e.g. [button](../docs/storybook/button.md), [tag](../docs/storybook/tag.md)).
