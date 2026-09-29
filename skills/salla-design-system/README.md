# salla-design-system skill — header update (2026-09-29)

Drop-in files for the `salla-design-system` skill so its prototype shell matches the Figma **Header**
component (the same header that `demo/index.html` and `demo/components.html` in this repo render).

```
skills/salla-design-system/
├── assets/prototype-template.html   replaces the skill's assets/prototype-template.html
└── references/header.md             new reference: measured header spec + usage rules
```

## Install

1. Copy `assets/prototype-template.html` over the skill's file of the same name.
2. Copy `references/header.md` into the skill's `references/`.
3. In `SKILL.md`, Shape 1 step 1, replace the app-shell description with:

   > Read `assets/prototype-template.html` and use it as the starting shell. It carries the **Figma Header
   > component** (92 px teal title bar with the mint active-tab pill, setup ring, icon cluster and photo
   > avatar; 64 px subcategory bar with underlined tabs, the rounded-square help button and the gradient
   > "مشمر" pill; breadcrumb and page-title rows) with its ≤1200 px variant, plus the list-detail layout —
   > fork this rather than building from scratch. Specs in `references/header.md`.

The template is self-contained (icons inlined as an SVG sprite, avatar as a data URI) and loads the Twilight
runtime + PingARLT from the CDN, as the skill's `_runtime.html` does. For offline use point the four
`<link>`/`<script>` tags at `storybook/static/` and `fonts/pingarlt.css` from this repo.
