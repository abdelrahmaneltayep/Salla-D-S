# Manosh brand kit (Mennatullah videos)

Backup of the Manosh video brand kit and its build tools, restored on 2026-11-05 after a workspace reset.

- `manosh/Manosh/` — the kit: `BRANDKIT.md` (spec + restore log), templates, brand.css (fonts embedded), SFX, paper, carousel, storyboard.
- `manosh/package.json` — `@fontsource` fonts used by `build_css.js` (`cd manosh && npm i && node Manosh/build_css.js`).
- `tools/` — builders (`build_v8.py` main/storyboard video, `storyboard_base.py`, `story_panels.js`, `paper_scene.py`, `render_many.js`, …).
- `MENNA_VOICE_AND_TONE.md` — voice & tone guide for scripts.

To use in a fresh session: copy `tools/` and `manosh/` into a working root, symlink Playwright into `tools/node_modules`, and copy
`manosh/Manosh/audio/sfx/scroll_*.wav` to `<root>/kit2/sfx/`.
