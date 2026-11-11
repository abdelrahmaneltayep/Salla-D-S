#!/usr/bin/env python3
"""Manosh build — brand kit 2026-10-26: word-chip hook (opening lines), cream pill subtitles,
video zoom cuts (close-up <-> wide at every caption line), chip SFX, watermark, smoothup endcard.
No jump cuts, no music. Native 4K (2160x3840) @ 60fps, or a 1080p30 preview.

Usage: build_v8.py <config.json> [preview]
Config: src, voice, out_dir, out_name, pages (chips words.json format), subs [[start,end,text]],
        close (zoom factor), face_x, face_y (face centre as fraction of frame), zoom (bool, default true),
        story {scenes, img_dir, look} (optional storyboard panels, top centre, rendered by tools/story_panels.js).
"""
import json, os, subprocess, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_v7 import sh, trim, probe_dur, load_wav, save_wav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K = f"{ROOT}/manosh/Manosh"; T = f"{K}/templates"
SR = 48000
XF_DUR, END_HOLD, TAIL = 0.7, 3.0, 0.5
LETTER = 0.035          # typing click spacing
SUB_BLOCK_MIN = 2.2      # after the hook, framing changes at most every ~2 s (at subtitle starts)


def chip_sfx(mix, pages):
    sfx = f"{K}/audio/sfx"
    def tr(x, d, f):
        x = x[:int(d * SR)].copy(); x[-int(f * SR):] *= np.linspace(1, 0, int(f * SR))[:, None]; return x
    typ = load_wav(f"{sfx}/typing.wav"); pop = tr(load_wav(f"{sfx}/pop.wav"), .25, .08)
    clicks = [tr(typ[max(0, int((p - .006) * SR)):], .07, .02) for p in json.load(open(f"{sfx}/typing_peaks.json"))]
    def add(c, t, db):
        at = int(t * SR); n = min(len(c), len(mix) - at)
        if n > 0: mix[at:at + n] += c[:n] * 10 ** (db / 20)
    rng = np.random.default_rng(3); k = 0
    for p in pages:
        for w, t, *key in p["words"]:          # typing: one key click per letter, 35 ms apart
            kw = bool(key and key[0])
            for i in range(len(w)):
                add(clicks[k % len(clicks)] * rng.uniform(.8, 1.1), t + i * LETTER, -16 if kw else -19); k += 1
            if kw: add(pop, t, -24)


def main():
    cfg = json.load(open(sys.argv[1]))
    preview = len(sys.argv) > 2 and sys.argv[2] == "preview"
    S, FPS = (1, 30) if preview else (2, 60)
    W, H = 1080 * S, 1920 * S
    B = cfg["out_dir"] + ("/preview" if preview else "/master"); os.makedirs(B, exist_ok=True)
    src_dur = probe_dur(cfg["src"])
    pages, subs = cfg["pages"], [list(s) for s in cfg["subs"]]
    end = min(src_dur - 0.05, subs[-1][1] + TAIL + XF_DUR)
    xf_off = end - XF_DUR; total = xf_off + XF_DUR + END_HOLD
    for i in range(len(subs) - 1):
        subs[i][1] = min(max(subs[i][1], subs[i][0] + 0.45), subs[i + 1][0] - 0.02)

    # ---- zoom-cut framing: every chip page, then subtitle starts spaced >= SUB_BLOCK_MIN -------------
    marks = [0.0] + [p["start"] for p in pages[1:]]
    for a, _, _ in subs:
        if a - marks[-1] >= SUB_BLOCK_MIN and end - a >= SUB_BLOCK_MIN:
            marks.append(a)
    marks.append(end + 1)
    tt = f"(in/{FPS})"
    zterms = [f"between({tt}\\,{marks[k]:.3f}\\,{marks[k + 1] - 1e-3:.3f})*{cfg['close'] - 1:.3f}"
              for k in range(len(marks) - 1) if k % 2 == 0]
    Z = "1+" + "+".join(zterms)
    fx, fy = cfg["face_x"], cfg["face_y"]
    print("framing blocks:", len(marks) - 1)

    # ---- cards ---------------------------------------------------------------------------------------
    pairs = []
    subs_ar = cfg.get("subs_ar")    # optional: Arabic line per sub, shown in a second pill below the English
    if subs_ar:
        assert len(subs_ar) == len(subs), f"subs_ar has {len(subs_ar)} lines, subs has {len(subs)}"
    for i, (_, _, txt) in enumerate(subs):
        if subs_ar:
            sh(["node", f"{T}/subtitle_bi_html.js", f"{B}/sub_{i:02d}.html", txt, subs_ar[i]], stdout=subprocess.DEVNULL)
        else:
            sh(["node", f"{T}/subtitle_html.js", f"{B}/sub_{i:02d}.html", txt], stdout=subprocess.DEVNULL)
        pairs += [f"{B}/sub_{i:02d}.html", f"{B}/sub_{i:02d}.png"]
    wm = "watermark_dark.html" if cfg.get("light_bg") else "watermark.html"   # light_bg: storyboard videos
    pairs += [f"{T}/{wm}", f"{B}/watermark.png", f"{T}/endcard.html", f"{B}/endcard.png"]
    env = dict(os.environ, NODE_PATH=f"{ROOT}/tools/node_modules")
    sh(["node", f"{ROOT}/tools/render_many.js", str(S), *pairs], env=env)
    story = cfg.get("story")
    scenes = json.load(open(story["scenes"])) if story else []
    pos = {"watermark": trim(f"{B}/watermark.png")}
    for i in range(len(subs)):
        pos[f"sub_{i:02d}"] = trim(f"{B}/sub_{i:02d}.png")
        if pos[f"sub_{i:02d}"][3] > (240 if subs_ar else 120) * S:    # one line ~95 px (two pills ~200); more = wrapped
            print(f"WARNING sub {i} wraps to two lines: {subs[i][2]}")
    json.dump(pages, open(f"{B}/words.json", "w"), ensure_ascii=False)
    chip_dur = pages[-1]["end"] + 0.1
    sh(["node", f"{T}/chips_html.js", f"{B}/words.json", f"{B}/chips", str(S), str(FPS), f"{chip_dur:.2f}",
        cfg.get("chips_theme", "light")], env=env)
    for k, sc in enumerate(scenes):          # one frame sequence per storyboard scene
        json.dump([[sc["start"], sc["end"]]], open(f"{B}/story_win_{k}.json", "w"))
        sh(["node", f"{ROOT}/tools/story_panels.js", story["scenes"], story["img_dir"], f"{B}/story_{k}",
            f"{B}/story_win_{k}.json", str(S), str(FPS), story.get("look", "card")], env=env)

    # ---- audio ---------------------------------------------------------------------------------------
    v = load_wav(cfg["voice"])
    mix = np.zeros((int(total * SR), 2), np.float32)
    n = min(len(v), int((xf_off + 0.3) * SR)); vv = v[:n].copy()
    fo = int(0.55 * SR); st = max(0, int((xf_off - 0.25) * SR))
    vv[st:st + fo] *= np.linspace(1, 0, len(vv[st:st + fo]))[:, None]; vv[st + fo:] = 0
    mix[:n] += vv
    chip_sfx(mix, pages)
    if story and story.get("look") in ("fold", "roll", "rollR", "rollL"):   # paper sound as the sheet opens / closes
        def put(snd, t, db):
            at = int(t * SR); n = min(len(snd), len(mix) - at)
            if n > 0: mix[at:at + n] += snd[:n] * 10 ** (db / 20)
        if story["look"].startswith("roll"):     # parchment scroll unrolling / rolling up (ElevenLabs SFX)
            sopen, sclose = load_wav(f"{ROOT}/kit2/sfx/scroll_open.wav"), load_wav(f"{ROOT}/kit2/sfx/scroll_close.wav")
            for sc in scenes:
                put(sopen, sc["start"] + .12, -9); put(sclose, sc["end"] - 1.1, -10)
        else:
            paper = load_wav(f"{ROOT}/kit2/sfx/paper_place.wav")[:int(.7 * SR)].copy()
            paper[-int(.2 * SR):] *= np.linspace(1, 0, int(.2 * SR))[:, None]
            for sc in scenes:
                for t, db in [(sc["start"] + .22, -19), (sc["start"] + .62, -20), (sc["end"] - 1.25, -21), (sc["end"] - .8, -21)]:
                    put(paper, t, db)
    peak = np.abs(mix).max()
    if peak > 0.94: mix *= 0.94 / peak
    save_wav(f"{B}/audio_mix.wav", mix)

    # ---- video graph -----------------------------------------------------------------------------------
    inputs = ["-t", f"{end:.3f}", "-i", cfg["src"], "-framerate", str(FPS), "-i", f"{B}/chips/f_%04d.png"]
    frame = (f"zoompan=z='{Z}':x='min(max(0\\,{fx}*iw-0.5*iw/zoom)\\,iw-iw/zoom)'"
             f":y='min(max(0\\,{fy}*ih-0.46875*ih/zoom)\\,ih-ih/zoom)':d=1:s={W}x{H}:fps={FPS}"
             if cfg.get("zoom", True) else f"scale={W}:{H}:flags=lanczos")
    fc = [f"[0:v]fps={FPS},{frame},setsar=1,format=yuv420p,"
          f"vignette=angle=PI/6,trim=0:{end:.3f},setpts=PTS-STARTPTS[v0]"]
    idx, cur = 2, "v0"

    def add_img(png, start, dur, fi, fo, x, y, name):
        nonlocal idx, cur
        inputs.extend(["-framerate", str(FPS), "-loop", "1", "-t", f"{dur:.3f}", "-i", png])
        fc.append(f"[{idx}:v]format=rgba,fade=in:st=0:d={fi}:alpha=1,"
                  f"fade=out:st={dur - fo:.3f}:d={fo}:alpha=1,setpts=PTS-STARTPTS+{start:.3f}/TB[{name}]")
        fc.append(f"[{cur}][{name}]overlay=x='{x}':y='{y}':eval=frame:eof_action=pass[{name}o]")
        cur = f"{name}o"; idx += 1

    wx, wy, _, _ = pos["watermark"]
    add_img(f"{B}/watermark.png", 0, end, 0.01, 0.01, wx, wy, "wm")
    fc.append(f"[{cur}][1:v]overlay=0:0:eof_action=pass[chp]"); cur = "chp"
    for k, sc in enumerate(scenes):
        inputs.extend(["-framerate", str(FPS), "-i", f"{B}/story_{k}/f_%05d.png"])
        fc.append(f"[{idx}:v]setpts=PTS-STARTPTS+{sc['start']:.3f}/TB[sb{k}]")
        fc.append(f"[{cur}][sb{k}]overlay=0:0:eof_action=pass[sbo{k}]"); cur = f"sbo{k}"; idx += 1
    for i, (s0, s1, _) in enumerate(subs):
        sx, sy, _, _ = pos[f"sub_{i:02d}"]
        s0 -= 0.04
        p = f"min(1,(t-{s0:.3f})/0.16)"
        add_img(f"{B}/sub_{i:02d}.png", s0, s1 - s0, 0.14, 0.12, sx, f"{sy}+{60 * S}*pow(1-{p},2)", f"s{i:02d}")
    inputs.extend(["-framerate", str(FPS), "-loop", "1", "-t", f"{XF_DUR + END_HOLD:.3f}", "-i", f"{B}/endcard.png"])
    fc.append(f"[{idx}:v]scale={W}:{H},format=yuv420p,setsar=1[ec]")
    fc.append(f"[{cur}]format=yuv420p[main]")
    fc.append(f"[main][ec]xfade=transition=smoothup:duration={XF_DUR}:offset={xf_off:.3f}[vout]")
    idx += 1
    inputs.extend(["-i", f"{B}/audio_mix.wav"])
    if preview:
        out = f"{B}/{cfg['out_name']}_preview_1080.mp4"
        venc = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "22"]
    else:
        out = f"{B}/{cfg['out_name']}_4K60_master.mp4"
        venc = ["-c:v", "libx265", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", "-tag:v", "hvc1",
                "-x265-params", "log-level=error", "-color_primaries", "bt709", "-color_trc", "bt709",
                "-colorspace", "bt709", "-r", str(FPS)]
    open(f"{B}/graph.txt", "w").write(";\n".join(fc))
    sh(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex_script", f"{B}/graph.txt",
        "-map", "[vout]", "-map", f"{idx}:a", *venc, "-c:a", "aac", "-b:a", "320k",
        "-movflags", "+faststart", "-t", f"{total:.3f}", out])
    json.dump({"marks": marks, "subs": subs, "xf_off": xf_off, "total": total}, open(f"{B}/timeline.json", "w"), indent=1)
    print("OUT", out)


if __name__ == "__main__":
    main()
