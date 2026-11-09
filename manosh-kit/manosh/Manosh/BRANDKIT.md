# Brand Kit — Manosh

Snapshot of the Mennatullah (منّة الله) visual identity as shipped in the
"Duaa When Suffering Pain Or Hardship" video (Mannon-layout Manosh look).
Updated 2026-11-06 (NEW: cinematic storyboard video — hybrid Kling 2.5 animation, see **Cinematic storyboard video**; hijab rule added to the storyboard art). 2026-11-05: scrolls now show the storyboard art in its ORIGINAL colours, same look as the storyboard video; kit restored after a workspace reset). Earlier, 2026-10-29: storyboard art style locked; storyboard video + carousel added; Drive delivery step; storyboard scrolls added; word-chip hook with typing sound, no bounce; no zoom cuts). The card generators in `templates/` are the source of truth
for this look; the older Deliverable-#15 generators still live under `scripts/`.

**Applying the kit** = brand cards/subtitles/motion (below) **plus** the
mandatory audio pass (**Audio treatment** section). "Apply Manosh brand kit"
always includes removing the background noise from the voice track.

**"Apply Manosh brand kit" = 3 deliverables (LOCKED 2026-11-06, the user's standing instruction):**
1. **Main video** — Menna's footage with the full kit (ElevenLabs voice clean-up, typing hook, pill subtitles, storyboard scrolls above her, watermark, endcard), 1080p preview ≤30 MiB.
2. **Cinematic storyboard video** — the hybrid animated storyboard (see **Cinematic storyboard video**), Menna's voice.
3. **Instagram carousel** — 7 slides + `caption.txt` (folder + zip).

The **regular (non-animated) storyboard video** is made **only when the user asks for it**. Video captions (Instagram/TikTok) and the 4K60 master also only on request.

## Color palette
Defined in `build_css.js` `:root` and compiled into `brand.css`.

| Token         | Hex       | Usage                                              |
|---------------|-----------|----------------------------------------------------|
| `--burgundy`  | `#4C2130` | Primary text, wordmark, endcard strip, scrim       |
| `--cream`     | `#F3ECDF` | Card backgrounds, endcard field, handle-on-photo   |
| `--terracotta`| `#C97C5A` | Accent square, highlights, kickers, diamond        |
| `--gold`      | `#C9A264` | Keyword highlights (`{{gold}}`), dividers, stars    |
| `--teal`      | `#3B837E` | Zellige stars, badge English text                   |
| `--blush`     | `#E8C9B4` | Zellige stars, soft accents                         |

## Fonts (base64 woff2, embedded in brand.css)
| Family                | Weight | Role                                             |
|-----------------------|--------|--------------------------------------------------|
| Aref Ruqaa            | 700    | Arabic wordmark (منّة الله) on endcard            |
| Reem Kufi             | 700    | Arabic kicker / badge Arabic                     |
| Amiri                 | 400/700| Verse-card Arabic (Qur'an text)                  |
| IBM Plex Sans Arabic  | 400/700| Arabic body / utility                            |
| Nunito Sans           | 600/700| Subtitles, English translation, handle, headline |
| Cormorant Garamond    | 600    | Latin wordmark subline (MENNATULLAH)             |

## Templates (in `templates/`)
| File                | Anchor            | Purpose                                             |
|---------------------|-------------------|-----------------------------------------------------|
| `chips_html.js`     | top:1170px, centered | **Locked caption + hook style (2026-10-26).** Word chips; see **Captions — Word chips**. Usage: `node chips_html.js <words.json> <out_dir> [scale] [fps] [dur]` |
| `story_panels.js`   | top centre (y=36) | **Storyboard scrolls (2026-10-28).** See **Storyboard scrolls**. Usage: `node story_panels.js <scenes.json> <img_dir> <out_dir> <windows.json> [scale] [fps] rollL` |
| `paper_scene.py`    | —                 | Puts a drawing on the paper (tritone colour, paper recolour, torn edges). Usage: `python3 paper_scene.py <paper> <drawing.png|blank> <out.png> [flip] kit 0.97 C2AE98` |
| `hook_html.js`      | top:1040px, left  | **Primary hook.** Staggered burgundy pills, cream Nunito Sans 800, sentence case, `{{gold}}` word → gold. Aged-gold rule + `@mennatullah.mo` strip. No shadow. Usage: `node hook_html.js <out> "<line1>|<line2>|<line3>" ["<handle>"]` |
| `subtitle_html.js`  | top:1300px, centered | **Primary subtitle.** One spoken chunk on a solid cream pill, burgundy Nunito Sans 700, `{{gold}}` word → terracotta. No shadow. Usage: `node subtitle_html.js <out> "<text>"` |
| `verse_html.js`     | bottom (bottom:300)| Verse card: Amiri Arabic + Nunito English + ref     |
| `endcard.html`      | full frame        | Closing card: accent-square wordmark + zellige strip |
| `watermark.html`    | y=1645, centered  | @mennatullah.mo gold-star handle overlay               |
| `badge.html`        | top, centered     | "آية للقلب · A VERSE FOR THE HEART" badge (optional) |
| `title_html.js`     | (legacy)          | Original hook/title card generator                  |
| `v11_title_html.js` | (legacy)          | Deliverable-#11 hook card, teal-star kicker         |

## Captions — Word chips (LOCKED 2026-10-26)
The approved hook: chips over the opening spoken lines (option #4 of the reference-inspired set), with the typing sound.
Each spoken word appears **at the moment it is said** as its own chip; a page (one short line-group)
clears when the next page starts.

| Element | Spec |
|---------|------|
| Word chip | `--cream` fill, `--burgundy` Nunito Sans 800 62px, padding 9/18/12px, radius 16px, shadow `0 4px 14px rgba(76,33,48,.22)` |
| Key-word chip | Cormorant Garamond italic 700 78px, `--cream` text; fill alternates `--burgundy` → `--gold` (gold adds a `0 2px 0 rgba(76,33,48,.3)` text shadow) |
| Arabic | any Arabic word or ligature (e.g. ﷺ, قوامة, مسلمة) switches to **Amiri** automatically — in chips and in `subtitle_html.js` pills |
| Layout | centred block, 70px side margins, top 1170px (chest height), wraps, 10px gaps |
| Entrance | pop: scale .8 → 1 + fade, 0.16s, `cubic-bezier(.34,1.56,.64,1)` (ease-out-back) |
| Key words | the main word of each line + 1–2 meaningful words per video (e.g. *freedom*, *hijab*, *fully*, *Muslim*); never every word |

Input `words.json` (word times from transcription, `true` = key word):
`[{"start":5.87,"end":7.45,"words":[["and",5.89],["to",6.01],["be",6.13],["fully",6.37,true],["dressed",6.81,true]]}]`
Example: `examples/words_hijab.json`, still: `examples/word_chips_still.png`, clip: `examples/word_chips_preview.mp4`.
Fonts: `brand.css` embeds Nunito Sans 600/700 and Cormorant 600 only; 800 and italic are browser-synthesised,
exactly as approved — don't swap in other weights.
The pill subtitle (`subtitle_html.js`) stays the default for the rest of the video unless chips are asked for throughout.

## Storyboard art style (LOCKED 2026-10-29 — every storyboard)
All storyboard illustrations — scrolls, storyboard video, carousel — use this one style, **in its original
colours** (no tritone recolour, no paper overlay on full-frame art). Reference: `examples/storyboard_video/style_reference.jpg`.

| Element | Spec |
|---------|------|
| Look | classic film-storyboard **pencil sketch**: graphite lines + soft **burgundy & gold watercolour washes** on warm cream paper; light, airy, sun-washed |
| Generator | ElevenLabs image, `gpt-image-2`; set **aspect_ratio 9:16, resolution 2K** for full-frame (default is 16:9 — always change it) |
| **Islamic rules** | all figures **faceless** (smooth blank face); the Prophet ﷺ is **never drawn**; modest dress; **every woman in a proper hijab — no hair visible at all** (hairline, temples, ears, neck covered). **Abaya always reaches the ground — no legs, shins or ankles visible** (2026-11-06: a feet-and-footprints close-up showed her shins; prompt low shots with *the abaya falls to the ground, only the tips of her sandals show*). Zoom-check every head before building |
| History | 7th-century setting — **no domes, no minarets**; the early Masjid = mud-brick walls + palm-trunk pillars + palm-frond roof |
| Composition | main action in the **upper two-thirds**; lower third calmer, lighter paper for captions |
| Prompt core | `Vertical 9:16 portrait composition, one single full-frame illustration, no borders, no text. Classic film storyboard pencil sketch, graphite lines with soft burgundy and gold watercolor wash accents on warm cream paper. 7th-century Arabia/Madinah… HIJAB RULE: every woman wears a proper Islamic hijab, a fitted underscarf with the hijab wrapped snugly around the face, completely covering ALL hair including the hairline at the forehead and temples, the ears and the neck, the khimar falling over the chest; absolutely no hair visible on any woman. All people faceless (no eyes, nose or mouth, smooth blank face area), modestly dressed. No domes, no minarets. Main action in the upper two-thirds; the lower third calmer, lighter paper for captions.` (say *cream hijab*, never *headscarf*) |
| Cost | ~267 credits per 9:16 2K image; generate **1 variation per scene** — always pass `generations_count: 1` (deterministic nodes such as Voice Isolator default to 4 takes) |
| Look check (2026-11-05) | The approved look is the **light, airy** one: sun-washed cream paper, soft burgundy & gold washes, clear graphite lines (e.g. the Umm Kulthum storyboard video). **No style-reference image** by default. A darker "Ash-Shifa'-style" variant (dense hatching, aged stained paper) is possible with `examples/storyboard_video/style_reference.jpg` wired in as a reference (~502 credits/image), only when asked |

(The Storyboard **scrolls** below keep their paper/scroll treatment; the art inside them follows this style.)

## Storyboard video — Menna's voice only (2026-10-29)
A second version of a story video: her footage is replaced by **full-frame vertical illustrations** (one per story beat,
~8–14 s each, 10–12 scenes for a 2-min story), with her **ElevenLabs-cleaned voice**.

| Element | Spec |
|---------|------|
| Scenes | `scenes.json` `[{"start","end","img"}]`, consecutive, covering the whole voice (example: `examples/storyboard_video/scenes_ashshifa.json`) |
| Motion | `storyboard/storyboard_base.py`: slow push-in 1.00→1.07 + gentle sideways drift (alternating), 0.6 s cross-dissolve |
| Overlays | same as the main video: typing hook chips, pill subtitles, endcard — via `build_v8`-style compose with `src` = storyboard base |
| Watermark | **`templates/watermark_dark.html`** (burgundy handle) — the cream one disappears on the light art |
| Delivery | 1080p preview + 4K60 master, same as the main video |

## Cinematic storyboard video — hybrid animation (LOCKED 2026-11-06)
The storyboard video can be made to feel like a **real film**: the key moments are **animated with AI** (characters walk,
gesture and act; cloaks and dust move; the camera dollies), the rest of the scenes get **cinematic camera moves** — all in
the same pencil-and-watercolour storyboard look. First made for Safiyya bint Abdul-Muttalib (IMG_6052).

| Element | Spec |
|---------|------|
| Approach | **Hybrid**: animate the **6–9 key moments** (hook, the main action beats, the ending); every other scene is a still with a camera move. Fully animating a 3-min story would cost ~77k credits — more than a month of the plan |
| Model | **Kling 2.5 Turbo** (`kling-2.5-turbo`) — chosen 2026-11-06 over Runway Gen-4 Turbo (Runway barely moved the characters and smeared the crowd). Image-to-video from the scene's 9:16 storyboard image (`connect_from` the image node → `start_frame`) |
| Settings | `aspect_ratio: 9:16`, `duration_secs: 5`, `cfg_scale: 0.5`; **1 generation per clip** (`generations_count: 1`). Output 1080×1920, 24 fps, ~5 s |
| Cost | **~2,121 credits per 5-s clip** (10-s = double). Hybrid 3-min video ≈ 9 clips ≈ 19k credits; a 1-min story ≈ 5–6 clips ≈ 11–13k. Runway Gen-4 Turbo is ~1,515/clip (720p) if credits are tight |
| Prompt core | `Hand-drawn pencil and watercolor storyboard animation on warm cream paper, visible graphite lines with a subtle hand-drawn line boil, cinematic.` + **one clear action** (who moves, how, what the wind/dust/light does) + **one camera move** (slow push-in / tracking / arc / crane / pan) + `Faces stay smooth blank faceless shapes; her hijab keeps fully covering her hair.` |
| Negative prompt | `face, eyes, nose, mouth, facial features, visible hair, hair strands, bare legs, ankles, lifted hem, blood, gore, text, letters, watermark, photorealistic, 3D render, color photo` (+ `weapon, sword, fighting, red stains` for conflict scenes) |
| Islamic rules in motion | Same as the art: faceless, hijab fully covering, **the Prophet ﷺ never drawn or animated**. Violence is never shown: show the *before* (she grips the pole and strides to the gate) and the *after* (the enemies retreat) — no strike, no blood, no fallen body |
| QC (every clip) | Contact-sheet 5–6 frames, then zoom on every head at 2–3 timestamps: no face appearing when a character turns, no hair slipping from a hijab, no hem lifting to show legs or ankles when she walks or the wind blows. Watch for red watercolour on walls near a conflict — run `tools/tone_down_red.py` on the PNG/clip. A clip that breaks a rule is regenerated (costs again) — never shipped |
| Assembly | `storyboard/storyboard_hybrid.py <scenes.json> <img_dir> <out.mp4>` — scenes.json entries: stills `{"start","end","img","move"}` with `move` ∈ push / pull / left / right / up / down (ease-in-out, cycles if omitted); animated `{"start","end","img","video","lead"}`. A clip is slowed ≤1.25× with motion interpolation to 30 fps; `lead` = seconds of the still (a gentle pull-out that lands exactly on the clip's first frame) **before** the clip starts, so the action lands on the line that describes it; after the clip, its last frame holds with a slow push-in. 0.6 s cross-dissolves |
| Timing | Re-cut scenes so each clip starts on its line (e.g. *"She carried a kind of a stick"* → the pole clip; *"Once the disbelievers see this"* → the retreat clip) |
| Overlays / delivery | Unchanged: build_v8 compose with `src` = the hybrid base (typing hook, pill subtitles, `watermark_dark`, endcard), 1080p preview ≤30 MiB (two-pass), 4K60 on request. Voice only — no music |
| Workflow | 1) storyboard images as usual → 2) pick the key moments → 3) (new video type or model) **test 2 clips first** → 4) generate the rest (one run, `generations_count: 1`) → 5) QC → 6) `storyboard_hybrid.py` → 7) build |

## Instagram carousel (2026-10-29)
`node carousel/carousel.js <slides.json> <img_dir> <out_dir>` → 1080×1350 (4:5) PNGs, one per slide.
- 7 slides: **cover** (kicker + name + one-line role, "Swipe →") · **5 story slides** (numbered burgundy tag, kicker, Cormorant title with one terracotta key word, 1–2 sentence Nunito body) · **end** (her closing line as a quote + "Follow for more stories of the Sahabiyat").
- Each slide = a **full-bleed storyboard illustration** (same images as the storyboard video), text on a soft cream fade at the bottom, burgundy text, @mennatullah.mo + page dots.
- Arabic honorifics (رضي الله عنها / ﷺ) in Amiri, kept on one line. Example: `examples/storyboard_video/slides_ashshifa.json`, `carousel_cover.jpg`.

## Storyboard scrolls (optional — story videos, LOCKED 2026-10-28)
For story content (sahabiyat, seerah, history). Not every scene: only **3–5 key story moments**,
each on screen while Menna narrates that part. The talking parts in between stay clean.

| Element | Spec |
|---------|------|
| Illustration | Per the **Storyboard art style** above — the **same look as the storyboard video** (one 2×2 sheet, 4 panels, crop each, or a 16:9 crop of a storyboard scene) |
| **Islamic rule** | All figures **faceless**. The Prophet ﷺ is **never drawn** — scenes show only the companion's own moments. Every woman in a **proper hijab, no hair visible** (same HIJAB RULE sentence in the sheet prompt) |
| Colour | **Original colours** of the storyboard art (burgundy, gold, ochre, sunset) blended into the paper — `paper_scene.py … orig` (updated 2026-11-05; replaces the earlier Kit tritone `… kit`) |
| Paper | **Layered torn page** (`assets/paper/layered_torn_page.png`, aged with warm tea-stains and darker edges) recoloured to **`#C2AE98`** (a little darker than the wall), darken 0.97; flip it per scene (none / hv / h / v) so edges don't repeat |
| Frame / title / shadow / shine | **None** |
| Position / size | top centre, 760×471 at x=160, y=36 (1080×1920 space) — above her head |
| Open | scroll **unrolls from the LEFT** (roll travels left → right), 1.2 s |
| On screen | very slow drift, scale 1.00 → 1.04 |
| Close | scroll **rolls up from the RIGHT** (roll travels right → left), 1.2 s, ends exactly at the scene's end |
| Sound | `audio/sfx/scroll_open.wav` at start+0.12 s (−9 dB), `scroll_close.wav` at end−1.1 s (−10 dB) |

Files per scene: `pN.png` (drawing on paper) + `bN.png` (`paper_scene.py … blank`, the roll's paper back).
`scenes.json`: `[{"start":28.9,"end":47.9,"img":"p2.png","label":"Her mahr: Islam"}]` — label is for reference only, never shown.
Example: `examples/scenes_ummsulaym.json`, `examples/storyboard_scroll_preview.mp4`, `examples/storyboard_scroll_still.png`.

## Recurring motif
Zellige eight-point star (two overlaid squares, one rotated 45°) in teal / gold / cream / blush.
Aged-gold hairline frames on cards. Terracotta rounded-square accent behind the wordmark.
Cards are flat (drop shadows removed) — depth comes from the solid fill + hairline border only.

## Motion (applied at composite time in ffmpeg, not baked into the PNGs)
Cards render static/transparent; the entrance/exit motion is layered in the composite build
(see `work/vid_manosh/build.py`).

| Element   | Entrance                                                        | Exit                     |
|-----------|-----------------------------------------------------------------|--------------------------|
| Hook      | **Drop from top + settle** — falls in from ~170px above rest, overshoots and eases back (ease-out-back on overlay `y`), with a 0.28s alpha fade-in | 0.6s alpha fade-out      |
| Subtitle  | Pop-in: 0.14s alpha fade-in + 60px slide-up over 0.16s          | 0.12s alpha fade-out     |
| Verse     | 0.4s alpha fade-in, shown across each recitation window          | 0.45–0.5s alpha fade-out |
| Endcard   | `xfade=smoothup` reveal over the final ~0.7s                     | —                        |
| Word chips| per-word pop (baked into the chip frames by `chips_html.js`) — **no bounce** | hard swap at page change |
| Storyboard scroll | unroll from left, 1.2 s (`story_panels.js` look `rollL`) | roll up from right, 1.2 s |
| Video frame | **Steady, full frame — no zoom cuts, no jump cuts** (both removed per creator, 2026-10-26). `motion/zoom_cuts.py` is kept only as an opt-in tool; don't use it unless asked. | — |

Ease-out-back used for the hook: `E(u) = 1 + 2.70158·(u−1)³ + 1.70158·(u−1)²`, `u = (t−t0)/D`;
overlay offset `= A·(1−E(u))` moves the box from `A`→0 with a slight overshoot, then settles.

## Audio treatment (mandatory — "remove noise background")
Every Manosh video runs the creator's voice through a gentle background-noise
removal pass **before** compositing. This is part of the brand kit: applying the
kit always includes this step. It preserves the original voice (no AI
re-synthesis, no gating of quiet onsets) so the opening word survives and the
timbre stays natural.

Canonical script: `audio/denoise_voice.sh` (mirrors `scripts/denoise_voice.sh`).
Usage: `denoise_voice.sh <input_media> <voice_clean.wav>`

Chain (ffmpeg `-af`):
| Stage | Filter | Purpose |
|-------|--------|---------|
| 1 | `highpass=f=80` | cut sub-80Hz room rumble / handling noise |
| 2 | `afftdn=nr=12:nf=-25:nt=w` | gentle broadband FFT spectral denoise, white-noise tracking; `nr` kept modest so speech is untouched |
| 3 | `loudnorm=I=-16:TP=-1.5:LRA=11` | broadcast loudness target for the whole pipeline |
| 4 | `aresample=48000` | pipeline sample rate |

Output: `pcm_s16le`, 2ch, 48000 Hz. The composite build then uses this
`voice_clean.wav` as its audio source (afade-out + acrossfade to silence tail).

## Sound design (no music)
`audio/chips_sfx.py <voice_clean.wav> <words.json> <out.wav>` mixes onto the cleaned voice:
| Event | Sound | Level |
|-------|-------|-------|
| each hook chip | **typing**: one key click per letter, 35 ms apart, starting when the chip appears (`sfx/typing.wav`, keystrokes picked via `typing_peaks.json`) | −19 dB |
| key-word chip  | typing clicks at −16 dB + soft `sfx/pop.wav` | −16 dB + −24 dB |
| storyboard scroll opens | `sfx/scroll_open.wav` (parchment unrolling) | −9 dB |
| storyboard scroll closes | `sfx/scroll_close.wav` (parchment rolling up) | −10 dB |
Never add music under the voice.

## Word-chip build recipe (4K60 master)
1. Clean voice with the **ElevenLabs Voice Isolator** → `voice_clean.wav`; transcribe word times → `words.json`
   (the opening lines = the hook, ~10 s), mark 1 key word per line.
2. `node templates/chips_html.js words.json chips/ 2 60` (2× scale = 2160×3840 frames).
3. `python3 audio/chips_sfx.py voice_clean.wav words.json mix.wav` (typing sound on the hook).
4. ffmpeg: source scaled to 2160×3840 @ 60 (steady, no zoom) `[base][chips]overlay=0:0:eof_action=pass`,
   then pill subtitles (`subtitle_html.js`) for the rest of the video, watermark, smoothup endcard → HEVC 4K60 with `mix.wav`.
6. *(Story videos, optional)* storyboard scrolls: pick 3–5 moments → generate the 2×2 pencil sheet (faceless, no Prophet ﷺ)
   → `paper_scene.py … orig 0.97 C2AE98` (original colours, paper `#C2AE98`) for pN/bN → `story_panels.js … 2 60 rollL` per scene →
   overlay above the chips at each scene's start; mix the scroll sounds into `mix.wav`.

## Delivery (every video)
1. **1080p preview → Google Drive (always):** upload `<name>_preview_1080.mp4` to the **Mennatullah** folder
   https://drive.google.com/drive/folders/1K_kdbWRYsrqFZ95Gz4v7vnR5XigQQb4B
   with `python3 delivery/upload_drive.py <preview.mp4>` and share the Drive link.
   Needs env vars `GDRIVE_CLIENT_ID`, `GDRIVE_CLIENT_SECRET`, `GDRIVE_REFRESH_TOKEN` (OAuth, Drive scope) — never pasted in chat.
2. Also send the preview in chat (≤ 30 MiB; two-pass encode if larger).
3. **4K60 master on request:** full quality split into 24 MB parts + the `cat` join command (with the part-count check and MD5).

## Build
`node build_css.js` re-embeds the fonts and regenerates `brand.css`.
Templates link `brand.css` relatively and render via `scripts/render.js` (Playwright, 1080×1920, transparent).

## Wordmark / handle
Wordmark: منّة الله · Latin: MENNATULLAH · Handle: @mennatullah.mo (Instagram username; changed from @MENNATULLAH on 2026-11-09)

## Restore log (2026-11-05)
The cloud workspace was reset and the kit was rebuilt from this session's history. What differs from the 2026-10-29 zip:
- `brand.css`: regenerated with `build_css.js` from today's `@fontsource` packages (`npm i @fontsource/{aref-ruqaa,reem-kufi,amiri,ibm-plex-sans-arabic,nunito-sans,cormorant-garamond}` in the folder above the kit), 418,722 bytes vs 418,757 originally.
- `templates/endcard.html`: rebuilt from a delivered endcard frame (Aref Ruqaa wordmark on the terracotta square, Cormorant MENNATULLAH, gold rule, handle, zellige band).
- `audio/sfx/*`: regenerated with ElevenLabs Sound Effects from the original prompts (`REGENERATE_SFX.sh`); new takes, same recipe.
- `assets/paper/layered_torn_page.png`: **replacement** paper (gpt-image-2 sheet `layered_torn_page_clean.png` + procedural warm tea-stains and darker edges to match the Ash-Shifa' scrolls). The creator's original `r4.webp` was lost; swap it back in if it turns up.
- Storyboard style reference restored as `examples/storyboard_video/style_reference*.jpg` (frames from the Ash-Shifa' storyboard video). Optional, for the darker variant only: wire **one** into the gpt-image-2 node (~502 credits/image vs ~267 without; 3 references ~927/image). The default light look uses none.
- `endcard.html`, `verse_html.js`, `badge.html`, `title_html.js` originals were not recoverable; only `endcard.html` is rebuilt.
- Tools live beside the kit: `tools/` (build_v8.py etc.). Layout expected by build_v8.py: `<root>/tools`, `<root>/manosh/Manosh`, `<root>/kit2/sfx` (scroll sounds).
