# Manosh kit recovery notes (2026-11-05)

These files were recovered from session `session_01XVZrXVQNW7ARLqDMBhukoW`. The whole event log was read, from 2026-10-05 18:47 to 2026-11-05: 2,951 assistant/user events and 920 tool calls.

## How the files were rebuilt
1. **Seed: the original kit as uploaded.** On 2026-10-05 the user uploaded `Manosh.zip` and `BRANDKIT.md` from the Mac folder `/Users/a.eltayeb/Desktop/Mennatullah video editing pipeline/brandkits/Manosh/`.
   - The kit was untouched until 2026-10-26 16:58.
   - Event `9b8eef7d` (2026-10-26 16:58) printed `BRANDKIT.md` and `templates/subtitle_html.js` in full.
   - Event `da241bff` printed `watermark.html`.
   - Byte sizes match the originals exactly: BRANDKIT 6228, subtitle 1929, watermark 857.
2. **Replay: every later command, in order, in a sandbox.**
   - What ran: all Bash heredoc writes (`cat > f <<'EOF'`), Python patch scripts (`s.replace(old, new)`, `assert old in s`), `sed -i` edits, `cp` and Write/Edit calls.
   - What was blocked: network access, ffmpeg/node renders, git and curl were all stubbed.
   - Result: every patch whose anchor exists in its target file applied. The only asserting patch that failed (`3659dbb2`, subtitle `<bdi>` regex) also failed in the original session; its follow-up fix (`bd157302`) was applied.
   - Sed edits were checked by grepping for their new text. All were present. One `sed` on `storyboard_video.js` used a `\n` pattern that sed cannot match on a single line, so it changed nothing, as it would have in the original run.
3. **Verification against the log.** The final `BRANDKIT.md` has 202 lines. Its 16 `##` headings land on the same line numbers that event `49c1e288` printed on 2026-10-29 08:20 (line 12 "Color palette" through line 201 "Wordmark / handle"). Intermediate states also match the line numbers printed in the log (`2d6d2017`: lines 5/48/84/122; `78597388`: line 107; `ab8b8dbf`: lines 155–159).
4. **Nothing changed in the kit after 2026-10-29 08:20.** The last kit zip sent to the user was `Manosh_brandkit_2026-10-29.zip` (20.6 MB, SendUserFile `c55293d7`), so the recovered state equals that zip, minus binaries.

> Easiest full restore: the user still has the zips delivered in chat: `Manosh_brandkit_2026-10-26.zip`, `…-10-28.zip` and **`…-10-29.zip` (final)**. They are likely in `~/Downloads` on the Mac and contain everything, including `brand.css` with fonts and the SFX wavs. The original kit is also still in the Mac folder above.

## File by file
| Recovered file | Source | Complete? |
|---|---|---|
| `BRANDKIT.md` | Original (2026-08-29) plus patches `1b41d0fd`, `2d6d2017` (10-26), `78597388`, `ab8b8dbf` (10-28), `49c1e288` (10-29) | **Yes**, verified against logged line numbers |
| `templates/chips_html.js` | Created `2f6161c8` (10-26 16:58); Arabic/ﷺ patches `853d3272`, `18568398`; dark theme and other patches through 10-29 | Yes (replayed) |
| `templates/subtitle_html.js` | Original plus Amiri `.ar` (`853d3272`), `<bdi dir=rtl>` (`19d8711d`), phrase grouping (`bd157302`, 10-29 05:06) | Yes |
| `templates/watermark.html` | Original, printed 10-29 (`da241bff`) | Yes (857 bytes, matches) |
| `templates/watermark_dark.html` | Derived from watermark by `sed` (`f5b586f5`, 10-29 08:14) | Yes |
| `templates/story_panels.js`, `templates/paper_scene.py` | Copied from tools on 10-28 06:45 (`97a018c2`); brand.css path fixed (`78597388`) | Yes |
| `templates/hook_html.PARTIAL.js` | Only `head -50` was ever printed (10-05, `4c2bcdde`) | **Partial** (legacy template) |
| `motion/zoom_cuts.py` | `a465e5ab`; marked deprecated in `2d6d2017` (zoom cuts removed) | Yes |
| `audio/chips_sfx.py` | `a465e5ab`, then the typing-sound rewrite in `2d6d2017` | Yes |
| `audio/denoise_voice.sh` | Original, printed in full on 10-05 (`4c2bcdde`) | Yes |
| `audio/sfx/REGENERATE_SFX.sh` | Written during recovery from the exact ElevenLabs prompts and ffmpeg chains in the log (see below) | New helper |
| `storyboard/storyboard_base.py` | `tools/storyboard_base.py` (`41a2fcf5`), zoompan sign fix `4499cdcc`, copied in `e67a8f21` | Yes |
| `carousel/carousel.js` | `tools/carousel_full.js` (`080b3820`) plus sed `ff94d299`, `df764d74`, copied and path fixed in `e67a8f21` | Yes |
| `delivery/upload_drive.py` | `31c01bce` plus sed `0c6ca8a2` | Yes (secrets come only from env vars) |
| `examples/*.json` | Replayed generator scripts. `words_hijab.json` was checked against the sample printed in the log. | Likely exact |
| `build_css.PARTIAL.js` | Only `head -30` was printed (`9b8eef7d`) | **Partial**: the end (write brand.css and templates/brand.css) is missing |
| `tools/build_v8.py` | Created `99dee316` (10-26 17:22) plus 17 patches through 10-29 08:14 (`f5b586f5`, `light_bg` → watermark_dark) | Yes; parses, and has `chips_theme`, `light_bg`, wrap check `>120*S`, typing SFX |
| `tools/build_v7.py` | Write `be25496f` (10-26 04:11) plus patches. **build_v8 imports `sh, trim, probe_dur, load_wav, save_wav` from it.** | Yes |
| `tools/*` (others) | All tools written in the session (render.js, render_many.js, zip_words.py, story_panels.js, paper_scene.py, paper_full.py, parchment.py, storyboard_video.js, carousel*.js, chips_bounce/layout.js, …) | Yes (replayed). All `.py` files parse and all `.js` files pass `node --check`. |
| `history/` | BRANDKIT as uploaded (08-29), after chips (10-26), after scrolls and Drive (10-28), plus the 10-28 update preview | Reference only |

## Not recoverable from the log (never printed; binary or huge)
- `brand.css` and `templates/brand.css` (418,757 bytes each, base64 woff2 fonts). Get them from the original kit or the delivered zips, or regenerate with `build_css.js`.
- Fonts are npm `@fontsource` packages, not Google Fonts downloads. No font download happened in the session.

  | Family | Weight | Subset |
  |---|---|---|
  | aref-ruqaa | 700 | arabic |
  | reem-kufi | 700 | arabic |
  | amiri | 700 | arabic |
  | amiri | 400 | latin |
  | ibm-plex-sans-arabic | 400 and 700 | arabic |
  | nunito-sans | 600 and 700 | latin |
  | cormorant-garamond | 600 | latin |

  The path pattern is `node_modules/@fontsource/<pkg>/files/<pkg>-<subset>-<wt>-normal.woff2`. Nunito 800 and Cormorant italic are browser-synthesised, which is intentional per BRANDKIT.
- Original templates that were never printed: `endcard.html` (2457 bytes), `verse_html.js`, `badge.html`, `title_html.js`, `v11_title_html.js`, and the rest of `hook_html.js`. None was modified in the session, so the originals in Manosh.zip are current.
- Binary assets:
  - `audio/sfx/typing.wav`, `pop.wav`, `typing_peaks.json`, `scroll_open.wav`, `scroll_close.wav`
  - `assets/paper/layered_torn_page.webp`, from user-supplied paper reference `r4.webp`
  - `examples/word_chips_still.png`, `word_chips_preview.mp4`, `storyboard_scroll_still.png`
  - `kit2/sfx/*`
- Tool runtime setup: `cd tools && npm init -y && PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm i playwright@1.56`. Renders run with `NODE_PATH=<scratchpad>/tools/node_modules`.

## SFX: how they were made (ElevenLabs Sound Effects API, `POST /v1/sound-generation`)
All processing chains are reproduced in `audio/sfx/REGENERATE_SFX.sh`.

| Output | Made | Prompt | duration_seconds | prompt_influence |
|---|---|---|---|---|
| `typing.wav` | 10-26 04:43 | "soft quiet keyboard typing, a few gentle key clicks, close mic, no music" | 1.2 | 0.65 |
| `pop.wav` | 10-26 04:43 | "single soft bubble pop, short, clean, warm, UI sound, no music" | 0.5 | 0.65 |
| `paper_place.wav` (old "fold" look) | 10-26 04:08 | "newspaper clipping being placed down, light paper rustle and soft tap, no music" | 1.0 | 0.6 |
| `scroll_open.wav` | 10-27 18:53 | "Old parchment scroll being unrolled quickly, dry crisp paper rustle and crinkle, close-up foley, no music, no voice" | 1.3 | 0.6 |
| `scroll_close.wav` | 10-27 18:53 | "Old parchment scroll being rolled up and closed, dry paper rustling and crinkling, close-up foley, no music, no voice" | 1.3 | 0.6 |

Post-processing:
- **typing / pop:** `silenceremove` at both ends (−50 dB / −55 dB), high-pass (typing 200 Hz, pop 120 Hz), 4 ms fade-in, 60 ms tail fade, 48 kHz stereo, peak normalised to −3 dBFS, `pcm_s16le`.
- **paper_place:** same chain with a 120 Hz high-pass and 5 ms / 80 ms fades.
- **scroll_open / scroll_close:** `highpass=f=150,afade=t=in:d=0.02,afade=t=out:st=1.05:d=0.25`, then `volume=5.6dB` (open) or `volume=4.8dB` (close), 48 kHz stereo.
- **typing_peaks.json:** click peak times in typing.wav. Envelope = 96-sample moving average; threshold = 0.35 × max; 1,200-sample search window; 3,000-sample hold-off.

Mix levels (BRANDKIT "Sound design", implemented in `tools/build_v8.py`):

| Event | Sound | Level |
|---|---|---|
| Each hook chip | One 70 ms key click per letter, 35 ms apart (`LETTER=0.035`) | −19 dB |
| Key-word chip | Typing clicks plus a pop | −16 dB clicks, −24 dB pop |
| Scroll open | `scroll_open.wav` at scene start + 0.12 s | −9 dB |
| Scroll close | `scroll_close.wav` at scene end − 1.1 s | −10 dB |

No music anywhere.

Other ElevenLabs SFX made but not part of the final kit: `whoosh_a/b/c`, `settle_a/b/c`, `paper_a/c`, `end_a/b`, `swipe_a`, `impact_a` (10-26 04:07–04:43). The final kit uses no whoosh, swoosh or impact.

## Caveats
- `tools/build_v8.py` expects the scratchpad layout `<root>/tools`, `<root>/manosh/Manosh` and `<root>/kit2/sfx/{scroll_open,scroll_close,paper_place}.wav`.
- **Security:** the session history contains an ElevenLabs API key hard-coded in several Bash commands (10-09, 10-17, 10-26, 10-27). It is not copied into any recovered file, but the key should be rotated.
