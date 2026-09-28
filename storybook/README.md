# Storybook

- `static/` — the complete static build of <https://dashboard-ui-components.pages.dev/> (Storybook 8.6.18, `@storybook/html-webpack5`,
  Stencil `admin-ui` web components, compiled Tailwind `styles.css`). Serve it with any static file server, e.g.
  `npx serve storybook/static`, and browse it offline.
- `captures/` — output of `scripts/capture_storybook.mjs`: `stories.json` (id, title, args, argTypes, tags rendered, files) and
  `stories/<component>/<story>.html|.png` for every story.
- `components.json` — the per-component API distilled from the captures (`scripts/build_storybook_docs.py`).

The human-readable version lives in [`docs/storybook/`](../docs/storybook/README.md).

Component tags shipped by the runtime (`admin-ui.esm.js`): s-accordion, s-accordion-group, s-alert-box, s-alert-box-action,
s-avatar, s-breadcrumbs, s-button, s-buttons-group, s-calendar, s-checkbox, s-click-outside, s-color-picker,
s-draggable-container, s-draggable-item, s-dropdown, s-editor (+ -desc, -preview, -toolbar), s-field, s-form, s-icon,
s-icon-picker, s-input, s-lingual-field, s-list-item, s-loader, s-maps, s-modal (+ -body, -footer, -head), s-otp, s-otp-input,
s-overlay, s-panel (+ -body, -head), s-placeholder, s-progress-bar, s-qty, s-radio, s-range-slider, s-rate, s-select,
s-skeleton and page skeletons (s-action-bar-skeleton, s-article-skeleton, s-box-skeleton, s-breadcrumb-skeleton,
s-cart-skeleton, s-checkout-skeleton, s-header-skeleton, s-home-page-skeleton, s-iframe-page-skeleton, s-items-list-skeleton,
s-list-entry-skeleton, s-list-skeleton, s-quick-filters-skeleton, s-resource-page-skeleton, s-sections-page-skeleton,
s-settings-skeleton, s-table-skeleton, s-widget-skeleton), s-tab-body, s-tab-head, s-tabs-group, s-table, s-tag, s-tags,
s-tel-input, s-textarea, s-toggle, s-tooltip, s-tooltip-action, s-uploader.
