#!/usr/bin/env python3
"""Manosh composite build for video 2 (Part 1) — native 4K (2160x3840) @ 60fps.

Cards are rendered at deviceScaleFactor 2 from the 1080x1920 templates, trimmed
to their visible bounding box, then overlaid with the brand-kit motion.
Usage: build.py [preview]   (preview = fast 1080p x264 for checking)
"""
import json, os, subprocess, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = f"{ROOT}/manosh/Manosh/templates"
B = f"{ROOT}/v2/build"
SRC = f"{ROOT}/v2/src2/source.mov"
VOICE = os.environ.get("VOICE", f"{ROOT}/v2/work/voice_df.wav")
S = 2                      # 1080-space -> 4K pixels
W, H, FPS = 2160, 3840, 60
PREVIEW = len(sys.argv) > 1 and sys.argv[1] == "preview"

HOOK = "Even if she's|a {{gold}}millionaire{{/gold}},|he still pays?"
HOOK_IN, HOOK_OUT = 0.30, 4.95          # hook fully gone by HOOK_OUT + 0.6

# (start, end, text) — times from word-level alignment of the original audio
SUBS = [
    (5.70, 6.60, "First,"),
    (6.69, 8.37, "Islam gives women"),
    (8.41, 9.09, "an absolute"),
    (9.13, 10.90, "{{gold}}financial independence{{/gold}}."),
    (10.98, 12.50, "Her money is for her."),
    (12.64, 14.83, "Invest, buy, sell,"),
    (14.87, 17.05, "no one has a say over it."),
    (17.31, 18.20, "Second,"),
    (18.27, 19.35, "the marriage gift,"),
    (19.39, 20.35, "which is the {{gold}}mahr{{/gold}},"),
    (20.39, 21.62, "is also for her."),
    (21.67, 22.95, "Not for her family"),
    (22.99, 24.45, "and not for the house."),
    (24.64, 25.55, "Third,"),
    (25.60, 27.88, "the man, religiously and legally,"),
    (27.92, 29.40, "is {{gold}}responsible{{/gold}} to pay"),
    (29.44, 31.08, "for everything in the house."),
    (31.14, 32.86, "The clothes, the food,"),
    (32.90, 33.95, "everything."),
    (34.08, 35.12, "So she is treated"),
    (35.16, 37.70, "as if she is a {{gold}}queen{{/gold}} in Islam."),
    (38.05, 39.05, "But there is something"),
    (39.09, 40.95, "that is called {{gold}}qiwamah{{/gold}}."),
    (41.03, 42.31, "Some people say that it's"),
    (42.35, 43.31, "a kind of control"),
    (43.35, 44.90, "from men over women."),
    (44.96, 46.65, "This is what we will discuss"),
    (46.69, 47.95, "in {{gold}}part two{{/gold}}."),
]

XF_OFF, XF_DUR, END_HOLD = 48.10, 0.7, 3.0   # endcard smoothup reveal
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
        out = f"{B}/Manosh_Part1_4K60_master.mp4"
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
