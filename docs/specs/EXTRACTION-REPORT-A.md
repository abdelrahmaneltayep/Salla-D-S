# REPORT-A — Figma design-to-code extraction (Salla D-S, file `dnmyqzYKK9dUJjVHuIWMDS`)

Date: 2026-09-28. All output in this `specs/` folder. `/home/user/Salla-D-S` untouched.

## Succeeded (10/10)

| Slug | Node | Result |
|---|---|---|
| button-primary-lg | 14526:107537 | Full code + tokens + text style + 2 SVG icons |
| checkbox | 12411:21810 | Full code + tokens + 1 SVG (tick) |
| radio | 12459:14981 | Code returned, but Figma flattened the whole radio to a single SVG — no tokens surfaced |
| toggle | 12411:21836 | Code returned, but flattened to a single SVG (39x24) — no tokens surfaced |
| status-badge | 15342:59964 | Full code (Status + BaseStatusIndicator) + tokens + text style; no assets |
| alertbox | 15375:52053 | Full code (incl. optional button/link/close) + tokens + 2 text styles + 2 SVG icons |
| loading-indicator | 27716:13238 | Code returned, flattened to a single SVG (88x88) — no tokens surfaced |
| avatar | 15368:1124 | Full code + tokens + 1 PNG placeholder |
| breadcrumb | 15392:76150 | Full code (Breadcrumb + BreadcrumbItem) + tokens + text style + 1 SVG |
| header | 15895:36794 | Full code (Header + PrimaryTabsListDashboardOnly, all optional sections) + tokens + 5 text styles + 7 component descriptions + 16 assets |

## Failed / skipped

- None failed. No response was flagged "sparse" or "too large", so no child-node follow-ups or saved-file reads were needed.
- Button component set parent (14526:107536) was NOT queried, per instructions (only the ten listed nodes were fetched). Its keywords/description came back inside the button and header responses and are recorded there.
- Asset downloads intentionally skipped (proxy blocks figma.com asset URLs). All asset references are written as `figma-asset:<basename>` placeholders; the real prefix was `https://www.figma.com/api/mcp/asset/<uuid>/` (7-day expiry).

## Setup notes

- `ReadMcpResourceTool` was not available in this session; the required `skill://figma/figma-design-to-code/SKILL.md` was loaded via `mcp__Figma__get_figma_skill` instead, before any `get_design_context` call.
- All calls used clientFrameworks=unknown, clientLanguages=html,css, skillNames=resource:figma-design-to-code, excludeScreenshot=true.

## Observations useful for implementation

- Token naming is inconsistent in the file: both slash-style (`--spacing/3xs`, `--spacing/sizes/sm`) and hyphen-style (`--spacing-4xl`, `--spacing-xs`, `--spacing-7xl`) appear, sometimes with different values for similar names (`--spacing/7xl`=56px vs `--spacing-7xl`=24px). "seconadry" and "Descreptive" typos are in the actual token names.
- Font is `Ping AR + LT` (Regular 400 / Medium 500 / Bold 700) everywhere; sizes xs 12/16, sm 14/20, md 16/24, 2xl 24/32.
- Core colours: primary `#004956`, secondary/mint `#a4ffe5` (hover `#dbfff6`), info `#5196f3`/`#ecf3fe`/`#cbe0fb`/`#204374`, warning `#d18f36`/`#fff9eb`/`#8f5f22`, success `#008c56`, gray-lighter `#737373`, border-default `#eee`.
