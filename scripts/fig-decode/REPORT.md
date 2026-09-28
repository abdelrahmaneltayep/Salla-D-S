# Icons DS_V.1 (`264ae0b3-Icons_DS_V.1.fig`) — SVG extraction report

Re-run: `cd icons-out/tools && node decode.mjs [../../fig/canvas.fig] [../]`
(deps already installed in `icons-out/tools/node_modules`: `kiwi-schema`, `fzstd`; `sharp` + `fast-xml-parser` only for the checks).
Helper scripts: `tools/validate.mjs` (XML + path-data check over every SVG), `tools/sheet.mjs` (contact sheets),
`tools/inspect.mjs <set-name>` (dump a component set's node tree), `tools/summary.json` (machine-readable stats from the last run).

## File format (what was actually found)

* Container: `fig-kiwi` magic, `uint32 version = 106`, then 2 length-prefixed chunks (`uint32 LE length` + bytes).
  * Chunk 0 (28,377 B) = kiwi binary schema, **raw deflate** (`zlib.inflateRawSync`), inflates to 70,742 B.
  * Chunk 1 (20.4 MB) = kiwi `Message`, **zstd** (magic `28 B5 2F FD`; decoded with the npm `fzstd` package), inflates to 73.6 MB.
* Decoded with `kiwi-schema`: `decodeBinarySchema` -> `compileSchema(...).decodeMessage`. Message has `nodeChanges` (156,745 nodes) and `blobs` (70,432).
* Node types: SYMBOL 27,241 · FRAME 31,539 · VECTOR 87,587 · BOOLEAN_OPERATION 3,545 · ELLIPSE 2,354 · ROUNDED_RECTANGLE 159 · TEXT 4,251 · INSTANCE 57 · CANVAS 3 · DOCUMENT 1 · VARIABLE_SET 3 · VARIABLE 5.
* Geometry blob encoding verified empirically on all 105,735 `fillGeometry`/`strokeGeometry` references (0 failures):
  `uint8 cmd` + float32-LE coords, `0=Z`, `1=M (x y)`, `2=L (x y)`, `3=Q (4 floats)`, `4=C (6 floats)`; every blob length is consistent with that grammar.
* `windingRule` values seen: `NONZERO`, `ODD` (-> `fill-rule="evenodd"`).
* Transforms: `transform {m00 m01 m02 m10 m11 m12}` relative to the parent (`x' = m00*x + m01*y + m02`). Composed down the tree and baked into path coordinates (3 decimals); the SYMBOL's own transform (its position on the canvas) is dropped so the icon sits at `0 0 W H`.
* Sibling z-order comes from `parentIndex.position` (fractional-index string); children are sorted by it before rendering.
* Descriptions: component sets and some symbols carry `description` (HTML, e.g. `<p>message, chat…</p>`) and `symbolDescription` (plain text). The plain text is used; the variant's own description wins, else the set's.
* Variant props live in `name` (`"Style=Stroke, Type=Rounded"`) and structurally in `variantPropSpecs` / the set's `componentPropDefs` (JSON string) and `stateGroupPropertyValueOrders`.
* Component sets are `FRAME` nodes with `isStateGroup: true`; their children are the `SYMBOL` variants.

## Pages / canvases

| Canvas | internalOnly | top-level children | SYMBOLs |
|---|---|---|---|
| `❖ Hugeicons Pro` | no | 138 (136 category FRAMEs + 2 stray INSTANCEs) | 7,772 |
| `Internal Only Canvas` | yes (hidden) | 19,495 | 19,469 |
| `Cover` | no | 1 (cover frame; text/instances only) | 0 |

The library is a re-packaged **Hugeicons Pro** set: 59 named category frames (Arrows, Business and finance, Communications, Edit Formatting, E-Commerce, Islamic, …; the remaining 77 top-level frames are unnamed `Frame`s with loose vectors, no components).

## Components

* **3,886 component sets** (all directly inside category frames), all with exactly **2 variants** → **7,772 live symbols**.
  * Variant properties observed: `Style = Stroke | Solid` (3,886 each), `Type = Rounded` (all). Every symbol is `24×24`.
  * `Style=Stroke` icons: 1.5 px black strokes, round caps/joins; `Style=Solid`: filled `#141B34` shapes (often via a color variable "Dark").
* **19,430 deleted-from-library symbols** on the hidden `Internal Only Canvas`, named `<icon>/<Style>/<Type>` and carrying `ancestorPathBeforeDeletion` (pointing back at the same category frame / component set). They are the five other Hugeicons styles that were removed from the published set but kept in the file:
  `Twotone/Rounded`, `Duotone/Rounded`, `Bulk/Rounded`, `Stroke/Sharp`, `Solid/Sharp` — 3,886 each, one per live icon.
  Exported under `svg/_internal/<icon>/<style>-<type>.svg` and flagged `"internal": true` in the manifest.
* **39 standalone symbols** (no component-set parent) also on the internal canvas: remote-library backing symbols (`componentKey` / `sourceLibraryKey` set) used by INSTANCEs on the Cover page and the "E-Commerce" header (a `tag` badge, `gitlab`, several `star*/favourite*/thumbs-*` from other libraries, and 7 unnamed `Style=…` variants). Exported under `svg/_standalone/` (guid-suffixed when names collide).
* Descriptions: 1,418 sets and 937 symbols have a description (keywords such as `message, chat, communicate, talk, comment`). Internal deleted symbols have none.

## Output

* `icons-out/svg/<set>/<variant>.svg` — 7,772 live icons (e.g. `svg/add-01/style=stroke-type=rounded.svg`, `svg/add-01/style=solid-type=rounded.svg`).
* `icons-out/svg/_internal/<set>/<style>-<type>.svg` — 19,430 deleted-style icons (e.g. `svg/_internal/add-01/bulk-rounded.svg`).
* `icons-out/svg/_standalone/*.svg` — 39.
* `icons-out/manifest.json` — 27,241 entries: `{ set, variant, name, width, height, file, description, category, properties{Style,Type}, internal, paths, guid, componentKey? }`.
  Total 27,241 SVGs, 166 MB on disk (du; small files on 4 KB blocks), manifest 9.5 MB.

### Rendering choices

* Stroke icons are emitted as **filled outlines from `strokeGeometry`** (Figma stores the stroke already outlined with the correct caps/joins), so no stroke attributes are needed and rendering is exact. Fill icons use `fillGeometry`. The raw `vectorData.vectorNetworkBlob` (editable centerline) was not decoded.
* Every solid paint with relative luminance < 0.05 and max channel < 0.32 (`#000000`, `#141B34`, `#2A353D` …) becomes `fill="currentColor"`, so icons recolor via CSS `color`. Other colors are kept verbatim: only 49 paths in the whole set — `#ffffff` ×46, `#d4d7e0` ×2, `#0bbc5c` ×1.
* Node and paint opacity are multiplied into `fill-opacity` (used by Duotone/Bulk styles: 0.4 fills; a few 0.25 paints).
* `BOOLEAN_OPERATION` nodes render their own pre-computed result geometry and skip their children (all 3,545 have geometry). `ELLIPSE`/`ROUNDED_RECTANGLE` use their `fillGeometry`/`strokeGeometry` like vectors.
* Hidden nodes (`visible: false`) are skipped: 13 nodes in total (e.g. an unused hidden `elements` frame in `wifi-disconnected-01` Stroke, a hidden `Union` in `maps-location-01` Solid, a hidden ellipse in `evil` Stroke).
* INSTANCE nodes inside symbols (9 across all symbols; `transmission`, `disability-01`, `tag`, plus the internal copies) are inlined by rendering the master symbol's children; overrides are ignored.
* Frames' "clip content" is not applied (`frameMaskDisabled`); no masks, gradients, images or effects exist inside any symbol (all 26,532 paints are `SOLID`).

### Sanity checks

* `tools/validate.mjs`: all 27,241 SVGs are well-formed XML; **none is empty** (min 1 path, max 18, mode 2); no degenerate path data.
* `tools/sheet.mjs` rasterized 48 icons with `sharp` (librsvg) on a light and a dark background (`tools/contact-sheet.png`, `tools/contact-sheet-dark.png`, index in `tools/contact-sheet-index.txt`). Visually checked: `add-01`, `adobe-photoshop`, `bubble-chat` (Stroke + Solid + Bulk/Duotone/Twotone/Sharp), `disability-01`, `maps-location-01`, `wifi-disconnected-01`, `evil`, `cpu`, `garbage-truck`, `medal-01`, `sun-cloud-little-snow-02`, etc. All look like the expected Hugeicons glyphs, correctly oriented (the source uses double vertical flips — `m11 = -1` on both the `elements` frame and its vectors — which compose back to upright), correctly positioned inside the 24×24 box, and recolor correctly through `currentColor`.

### Known issues / honest caveats

1. **Stray content in the source**: `svg/transmission/style=stroke-type=rounded.svg` contains an extra `file-validation` instance that the Figma component itself holds at offset (20,20); it renders as a small sliver in the bottom-right corner, exactly as in Figma. Not a decoder bug, but the icon is "wrong" as designed.
2. **White overlays instead of cut-outs** in 15 live Solid icons (`align-key-object, archer, crane, cursor-edit-01, delivery-return-02, disability-02, drag-04, file-zip, hand-sanitizer, hanging-clock, hockey, hot-air-balloon, left-triangle, mail-edit-01, time-schedule`) and 20 internal ones: the designer drew `#ffffff` shapes on top of the dark fill instead of subtracting. They are kept as `fill="#ffffff"` (per spec), so on a dark background with `color: white` the detail disappears. Fixing would require converting those paths to boolean cut-outs.
3. **TEXT is not rendered** (no glyph outlines in the file). It only affects `svg/_standalone/tag.svg` (a "New" badge from another library) — no icon contains text.
4. `_standalone/` symbols are other-library backing components, not part of this icon set; some are visually incomplete without their text/overrides (e.g. `tag.svg` is just a green dot).
5. Internal deleted symbols (`_internal/`) are *historical* — they were removed from the published library and may lag the live Stroke/Solid designs; their `description` is empty.
6. Duotone/Bulk styles rely on `fill-opacity` (0.4); when placed over non-white backgrounds they blend as Figma would.
