#!/usr/bin/env python3
"""Manosh composite build for video 5 (Part 4) — native 4K (2160x3840) @ 60fps.

Cards are rendered at deviceScaleFactor 2 from the 1080x1920 templates, trimmed
to their visible bounding box, then overlaid with the brand-kit motion.
Usage: build.py [preview]   (preview = fast 1080p x264 for checking)
"""
import json, os, subprocess, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = f"{ROOT}/manosh/Manosh/templates"
B = f"{ROOT}/v5/build"
SRC = f"{ROOT}/v5/src/source.mov"
VOICE = os.environ.get("VOICE", f"{ROOT}/v5/work/voice_original.wav")
S = 2                      # 1080-space -> 4K pixels
W, H, FPS = 2160, 3840, 60
PREVIEW = len(sys.argv) > 1 and sys.argv[1] == "preview"

HOOK = "Can women|{{gold}}work{{/gold}} in Islam?"
HOOK_IN, HOOK_OUT = 0.30, 2.95          # hook fully gone by HOOK_OUT + 0.6

# (start, end, text) — times from word-level alignment of the original audio
SUBS = [
    (3.62, 4.60, "Yes!"),
    (5.41, 6.50, "You are going to find"),
    (6.53, 8.20, "some {{gold}}female companions{{/gold}}"),
    (8.29, 10.05, "they were actually {{gold}}working{{/gold}},"),
    (10.15, 10.75, "during the time of"),
    (10.79, 12.95, "Prophet Muhammad,"),
    (12.99, 14.12, "or during the time of"),
    (14.15, 14.95, "Umar ibn al-Khattab"),
    (14.99, 16.50, "or Abu Bakr as-Siddiq."),
    (17.41, 19.15, "You're going to find someone"),
    (19.17, 20.45, "like Nusaybah bint Ka'b,"),
    (20.49, 21.60, "Umm Ammarah."),
    (21.70, 23.20, "She was {{gold}}fighting{{/gold}}"),
    (23.33, 25.20, "in the battle of Uhud."),
    (25.29, 26.80, "Not only that, but she was"),
    (26.85, 29.80, "protecting Prophet Muhammad"),
    (29.85, 30.45, "himself."),
    (30.56, 31.95, "So she was a {{gold}}soldier{{/gold}}."),
    (32.23, 33.60, "And you are going to find,"),
    (33.63, 34.45, "during the time of"),
    (34.47, 35.32, "Umar ibn al-Khattab,"),
    (35.35, 36.60, "radiyAllahu anhu,"),
    (36.71, 38.24, "he hired a woman"),
    (38.27, 39.48, "to take care of the {{gold}}market{{/gold}},"),
    (39.51, 40.92, "for buying and selling,"),
    (40.95, 42.10, "like a police."),
    (42.88, 44.70, "And also you are going to find"),
    (44.72, 45.48, "the wife of"),
    (45.52, 47.65, "Prophet Muhammad,"),
    (47.69, 49.30, "Aisha, radiyAllahu anha."),
    (49.35, 50.40, "Many of the companions"),
    (50.43, 52.20, "they go to ask for her {{gold}}advice{{/gold}}."),
    (52.42, 53.83, "Even Abu Bakr as-Siddiq"),
    (53.86, 55.03, "and Umar ibn al-Khattab,"),
    (55.06, 56.30, "when they became caliphs,"),
    (56.34, 58.23, "they go to ask for her advice"),
    (58.26, 58.95, "sometimes."),
    (59.49, 61.45, "So not only these three,"),
    (61.49, 63.58, "but you are going to find also"),
    (63.61, 64.95, "some companions"),
    (65.01, 65.93, "that were taking care"),
    (65.97, 66.85, "of soldiers."),
    (66.89, 68.10, "They were {{gold}}doctors{{/gold}}."),
    (69.03, 70.40, "Women were working"),
    (70.43, 71.03, "during the time of"),
    (71.07, 71.88, "Prophet Muhammad,"),
    (71.91, 72.60, "and during"),
    (72.63, 73.60, "the companions' time."),
    (73.73, 75.02, "So if it was wrong,"),
    (75.05, 76.40, "or it was {{gold}}haram{{/gold}},"),
    (76.64, 78.13, "Prophet Muhammad"),
    (78.16, 80.30, "was going to prevent them."),
    (80.83, 82.40, "So Islam here"),
    (82.43, 84.20, "is not calling women"),
    (84.77, 85.90, "not to work."),
    (85.99, 87.48, "It's calling them"),
    (87.51, 89.10, "to have {{gold}}peace{{/gold}} in their life."),
    (89.79, 91.92, "Don't run and push"),
    (91.95, 93.64, "yourself toward this kind"),
    (93.67, 95.90, "of battle in the society"),
    (96.65, 97.35, "to prove that"),
    (97.37, 98.70, "you are {{gold}}independent{{/gold}}."),
    (99.07, 100.30, "You are a woman,"),
    (100.42, 101.90, "and it's a kind of {{gold}}privilege{{/gold}}"),
    (101.94, 102.90, "you already have,"),
    (102.95, 104.40, "and Allah gave it to you."),
    (104.55, 105.50, "You have to be {{gold}}proud{{/gold}}"),
    (105.55, 106.60, "of being a woman,"),
    (106.72, 108.38, "with the same {{gold}}softness{{/gold}}"),
    (108.40, 109.20, "you have."),
    (109.51, 112.00, "Don't carry"),
    (112.07, 113.84, "the {{gold}}responsibility{{/gold}}"),
    (113.87, 115.60, "of financial life."),
    (116.03, 117.40, "It's not your job."),
]

XF_OFF, XF_DUR, END_HOLD = 117.55, 0.7, 3.0   # endcard smoothup reveal
TOTAL = XF_OFF + XF_DUR + END_HOLD


def sh(cmd, **kw):
    print("+", cmd if isinstance(cmd, str) else " ".join(cmd)[:300])
    subprocess.run(cmd, check=True, shell=isinstance(cmd, str), **kw)


def trim(png):
    """Crop to visible pixels (+pad); return (x, y) of the crop in the frame."""
    im = Image.open(png)
    x0, y0, x1, y1 = im.getbbox()
    pad = 8
    x0, y0 = max(0, x0 - pad), max(0, y0 - pad)
    x1, y1 = min(im.width, x1 + pad), min(im.height, y1 + pad)
    x0, y0 = x0 - x0 % 2, y0 - y0 % 2
    w, h = (x1 - x0) // 2 * 2, (y1 - y0) // 2 * 2
    im.crop((x0, y0, x0 + w, y0 + h)).save(png)
    return x0, y0


def render_cards():
    os.makedirs(B, exist_ok=True)
    pairs = []
    sh(["node", f"{T}/hook_html.js", f"{B}/hook.html", HOOK])
    pairs += [f"{B}/hook.html", f"{B}/hook.png"]
    for i, (_, _, txt) in enumerate(SUBS):
        sh(["node", f"{T}/subtitle_html.js", f"{B}/sub_{i:02d}.html", txt], stdout=subprocess.DEVNULL)
        pairs += [f"{B}/sub_{i:02d}.html", f"{B}/sub_{i:02d}.png"]
    pairs += [f"{T}/watermark.html", f"{B}/watermark.png", f"{T}/endcard.html", f"{B}/endcard.png"]
    env = dict(os.environ, NODE_PATH=f"{ROOT}/tools/node_modules")
    sh(["node", f"{ROOT}/tools/render_many.js", str(S), *pairs], env=env)
    pos = {"hook": trim(f"{B}/hook.png"), "watermark": trim(f"{B}/watermark.png")}
    for i in range(len(SUBS)):
        pos[f"sub_{i:02d}"] = trim(f"{B}/sub_{i:02d}.png")
    json.dump(pos, open(f"{B}/pos.json", "w"))
    return pos


def build(pos):
    inputs = ["-i", SRC]
    fc = []
    # base: autorotated 2160x3840, 60fps, gentle vignette like the reference look
    fc.append(f"[0:v]fps={FPS},scale={W}:{H}:flags=lanczos,setsar=1,format=yuv420p,"
              f"vignette=angle=PI/6,trim=0:{XF_OFF + XF_DUR},setpts=PTS-STARTPTS[v0]")
    idx, cur = 1, "v0"

    def add_img(png, start, dur, fade_in, fade_out, x_expr, y_expr, name):
        nonlocal idx, cur
        inputs.extend(["-framerate", str(FPS), "-loop", "1", "-t", f"{dur:.3f}", "-i", png])
        fc.append(f"[{idx}:v]format=rgba,fade=in:st=0:d={fade_in}:alpha=1,"
                  f"fade=out:st={dur - fade_out:.3f}:d={fade_out}:alpha=1,"
                  f"setpts=PTS-STARTPTS+{start:.3f}/TB[{name}]")
        fc.append(f"[{cur}][{name}]overlay=x='{x_expr}':y='{y_expr}':eval=frame:eof_action=pass[{name}o]")
        cur = f"{name}o"
        idx += 1

    # watermark: whole main section
    wx, wy = pos["watermark"]
    add_img(f"{B}/watermark.png", 0, XF_OFF + XF_DUR, 0.01, 0.01, wx, wy, "wm")

    # hook: drop from ~170px (x2) above rest with ease-out-back, 0.28s alpha in, 0.6s out
    hx, hy = pos["hook"]
    A, D, t0 = 170 * S, 0.55, HOOK_IN
    u = f"min(1,max(0,(t-{t0})/{D}))"
    ease = f"(1+2.70158*pow({u}-1,3)+1.70158*pow({u}-1,2))"
    add_img(f"{B}/hook.png", t0, HOOK_OUT + 0.6 - t0, 0.28, 0.6, hx, f"{hy}-{A}*(1-{ease})", "hk")

    # subtitles: 0.14s fade-in + 60px (x2) slide-up over 0.16s, 0.12s fade-out
    for i, (st, en, _) in enumerate(SUBS):
        sx, sy = pos[f"sub_{i:02d}"]
        st = st - 0.04
        p = f"min(1,(t-{st:.3f})/0.16)"
        add_img(f"{B}/sub_{i:02d}.png", st, en - st, 0.14, 0.12, sx,
                f"{sy}+{60 * S}*pow(1-{p},2)", f"s{i:02d}")

    # endcard + smoothup reveal
    inputs.extend(["-framerate", str(FPS), "-loop", "1", "-t", f"{XF_DUR + END_HOLD:.3f}", "-i", f"{B}/endcard.png"])
    fc.append(f"[{idx}:v]scale={W}:{H},format=yuv420p,setsar=1[ec]")
    fc.append(f"[{cur}]format=yuv420p[main]")
    fc.append(f"[main][ec]xfade=transition=smoothup:duration={XF_DUR}:offset={XF_OFF}[vout]")
    idx += 1

    # audio: studio-cleaned voice, fade under the reveal, silence tail
    inputs.extend(["-i", VOICE])
    fc.append(f"[{idx}:a]atrim=0:{XF_OFF + 0.3},afade=t=out:st={XF_OFF - 0.25}:d=0.55,"
              f"apad=whole_dur={TOTAL:.3f},atrim=0:{TOTAL:.3f}[aout]")

    graph = ";\n".join(fc)
    open(f"{B}/graph.txt", "w").write(graph)
    if PREVIEW:
        out = f"{B}/preview_1080.mp4"
        venc = ["-vf", "scale=1080:1920", "-c:v", "libx264", "-preset", "ultrafast", "-crf", "23", "-r", "30"]
        maps = ["-map", "[vpre]", "-map", "[aout]"]
        graph += ";\n[vout]scale=1080:1920,fps=30[vpre]"
        open(f"{B}/graph.txt", "w").write(graph)
        venc = ["-c:v", "libx264", "-preset", "ultrafast", "-crf", "23"]
    else:
        out = f"{B}/Manosh_Part4_4K60_master.mp4"
        maps = ["-map", "[vout]", "-map", "[aout]"]
        venc = ["-c:v", "libx265", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p",
                "-tag:v", "hvc1", "-x265-params", "log-level=error",
                "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
                "-r", str(FPS)]
    cmd = ["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex_script", f"{B}/graph.txt",
           *maps, *venc, "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-movflags", "+faststart",
           "-t", f"{TOTAL:.3f}", out]
    sh(cmd)
    print("OUT", out)


if __name__ == "__main__":
    pos = json.load(open(f"{B}/pos.json")) if os.path.exists(f"{B}/pos.json") and "--reuse" in sys.argv else render_cards()
    build(pos)
