#!/usr/bin/env python3
"""Manosh composite build for video 4 (Part 3) — native 4K (2160x3840) @ 60fps.

Cards are rendered at deviceScaleFactor 2 from the 1080x1920 templates, trimmed
to their visible bounding box, then overlaid with the brand-kit motion.
Usage: build.py [preview]   (preview = fast 1080p x264 for checking)
"""
import json, os, subprocess, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = f"{ROOT}/manosh/Manosh/templates"
B = f"{ROOT}/v4/build"
SRC = f"{ROOT}/v4/src/source.mov"
VOICE = os.environ.get("VOICE", f"{ROOT}/v4/work/voice_original.wav")
S = 2                      # 1080-space -> 4K pixels
W, H, FPS = 2160, 3840, 60
PREVIEW = len(sys.argv) > 1 and sys.argv[1] == "preview"

HOOK = "What if equality|is {{gold}}unfair{{/gold}}|to women?"
HOOK_IN, HOOK_OUT = 0.30, 10.65          # hook fully gone by HOOK_OUT + 0.6

# (start, end, text) — times from word-level alignment of the original audio
SUBS = [
    (11.52, 12.90, "Let me give an example."),
    (12.99, 14.50, "If I asked men and women"),
    (14.55, 15.40, "to carry the same"),
    (15.43, 17.10, "heavy {{gold}}backpack{{/gold}},"),
    (17.60, 18.95, "regardless of their strengths"),
    (19.00, 20.40, "or their natural role,"),
    (20.65, 21.60, "{{gold}}unfair{{/gold}}."),
    (22.02, 23.46, "{{gold}}Equity{{/gold}} actually means"),
    (23.50, 25.00, "I give each person"),
    (25.02, 25.85, "what they need,"),
    (25.90, 27.22, "and this is what Islam"),
    (27.26, 28.30, "is calling for."),
    (28.55, 30.68, "Islam is not calling"),
    (30.72, 32.15, "for a kind of"),
    (32.20, 33.60, "{{gold}}blind equality{{/gold}} for women."),
    (33.73, 35.12, "Because if we did,"),
    (35.17, 37.05, "it means women are going to"),
    (37.12, 38.88, "carry the burden of this life,"),
    (38.92, 41.10, "including the {{gold}}financial anxiety{{/gold}},"),
    (41.22, 42.90, "and at the same time,"),
    (43.14, 44.60, "somehow carrying"),
    (44.67, 47.10, "the unique emotional"),
    (47.15, 48.25, "and physical load"),
    (48.32, 50.90, "of building a home"),
    (51.01, 52.10, "with children."),
    (52.90, 54.30, "It's not fair,"),
    (54.34, 55.75, "it's not freedom."),
    (55.84, 57.95, "It's a kind of {{gold}}burnout{{/gold}} for her."),
    (58.50, 60.42, "So does it mean that Islam"),
    (60.46, 61.78, "prevents women"),
    (61.82, 62.75, "from {{gold}}working{{/gold}}?"),
    (63.65, 65.40, "It's not true."),
    (65.60, 66.28, "But this is what"),
    (66.32, 67.24, "we will discuss"),
    (67.28, 68.40, "in the {{gold}}next video{{/gold}}."),
]

XF_OFF, XF_DUR, END_HOLD = 68.55, 0.7, 3.0   # endcard smoothup reveal
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
        out = f"{B}/Manosh_Part3_4K60_master.mp4"
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
