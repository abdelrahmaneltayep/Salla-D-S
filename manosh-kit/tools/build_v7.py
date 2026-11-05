#!/usr/bin/env python3
"""Manosh v2 build — jump cuts, punch-in reframing, push-in drift, photo-card
tilt-settle and hook sound effects, on top of the v1 kit (cards, subtitles,
watermark, endcard). Native 4K (2160x3840) @ 60fps.

Usage: build_v7.py <config.json> [preview]

Config keys: src, voice, out_dir, out_name, hook, subs [[start,end,text]...],
segments [[start,end]...] (speech, original timeline), and optional
paper {style, photo, title, in, out}, cuts (bool, default true),
sfx (bool, default true), reframe (bool, default true: punch-in framing). All times are on the ORIGINAL timeline; the build
remaps them onto the cut timeline.
"""
import json, math, os, subprocess, sys, wave
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = f"{ROOT}/manosh/Manosh/templates"
SFX = f"{ROOT}/kit2/sfx"
S = 2
W, H, FPS, SR = 2160, 3840, 60, 48000

# Cut / motion tuning
GAP_MIN = 0.30          # silence left between phrases after padding; longer is cut
PAD_IN, PAD_OUT = 0.08, 0.16
BLOCK_MIN = 2.0         # shortest framing block (wide <-> punch-in alternates per phrase)
LEAD_IN = 0.90          # silence kept before the first word (hook drops here)
PUNCH = 1.12            # punch-in scale on alternating segments
DRIFT = 0.035           # slow push-in across each wide segment
FACE_X, FACE_Y = 0.49, 0.443   # face centre (fraction of frame) for reframing
XF_DUR, END_HOLD = 0.7, 3.0


def sh(cmd, **kw):
    print("+", " ".join(cmd)[:240])
    subprocess.run(cmd, check=True, **kw)


def trim(png):
    im = Image.open(png)
    x0, y0, x1, y1 = im.getbbox()
    pad = 8
    x0, y0 = max(0, x0 - pad), max(0, y0 - pad)
    x1, y1 = min(im.width, x1 + pad), min(im.height, y1 + pad)
    x0, y0 = x0 - x0 % 2, y0 - y0 % 2
    w, h = (x1 - x0) // 2 * 2, (y1 - y0) // 2 * 2
    im.crop((x0, y0, x0 + w, y0 + h)).save(png)
    return x0, y0, w, h


def probe_dur(path):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", path]).decode())


def keep_intervals(segs, src_dur, cuts=True):
    if not cuts:
        return [(0.0, src_dur)]
    iv = [[max(0.0, a - PAD_IN), min(src_dur, b + PAD_OUT)] for a, b in segs]
    iv[0][0] = max(0.0, segs[0][0] - LEAD_IN)
    merged = [iv[0]]
    for a, b in iv[1:]:
        if a - merged[-1][1] < GAP_MIN:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])
    merged[-1][1] = min(src_dur - 0.05, merged[-1][1] + XF_DUR)   # room for the endcard dissolve
    return [tuple(m) for m in merged]


class Timeline:
    def __init__(self, iv):
        self.iv, self.new = iv, []
        acc = 0.0
        for a, b in iv:
            self.new.append(acc)
            acc += b - a
        self.total = acc

    def map(self, t, side="start"):
        """Original time -> cut time. Times inside a removed gap snap to the
        next kept frame (side=start) or the previous one (side=end)."""
        for (a, b), n in zip(self.iv, self.new):
            if a <= t <= b:
                return n + (t - a)
            if t < a:
                return n if side == "start" else max(0.0, n - 0.001)
        return self.total


def load_wav(path):
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", path, "-ac", "2", "-ar", str(SR),
                                   "-f", "f32le", "-"])
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()


def save_wav(path, x):
    x = np.clip(x, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())


def build_audio(cfg, tl, hook_in, paper_in, xf_off, total, out):
    voice = load_wav(cfg["voice"])
    fade = int(0.008 * SR)
    parts = []
    for a, b in tl.iv:
        seg = voice[int(a * SR):int(b * SR)].copy()
        ramp = np.linspace(0, 1, fade)[:, None]
        seg[:fade] *= ramp; seg[-fade:] *= ramp[::-1]
        parts.append(seg)
    v = np.concatenate(parts)
    mix = np.zeros((int(total * SR) + SR, 2), np.float32)
    n = min(len(v), int((xf_off + 0.3) * SR))
    v = v[:n].copy()
    fo = int(0.55 * SR); st = max(0, int((xf_off - 0.25) * SR))
    v[st:st + fo] *= np.linspace(1, 0, min(fo, len(v) - st))[:, None]
    v[st + fo:] = 0
    mix[:n] += v
    if cfg.get("sfx", True):
        cues = [("hook_whoosh.wav", hook_in - 0.05, -9),
                ("hook_land.wav", hook_in + 0.30, -10),
                ("end_reveal.wav", xf_off - 0.10, -11)]
        if paper_in is not None:
            cues.append(("paper_place.wav", paper_in + 0.20, -8))
        for name, at, db in cues:
            s = load_wav(f"{SFX}/{name}") * (10 ** (db / 20))
            i = int(max(0, at) * SR)
            mix[i:i + len(s)] += s[:len(mix) - i]
    mix = mix[:int(total * SR)]
    peak = np.abs(mix).max()
    if peak > 0.94:
        mix *= 0.94 / peak
    save_wav(out, mix)


def main():
    cfg = json.load(open(sys.argv[1]))
    preview = len(sys.argv) > 2 and sys.argv[2] == "preview"
    B = cfg["out_dir"]; os.makedirs(B, exist_ok=True)
    src_dur = probe_dur(cfg["src"])
    tl = Timeline(keep_intervals(cfg["segments"], src_dur, cfg.get("cuts", True)))
    removed = src_dur - tl.total
    print(f"segments kept: {len(tl.iv)}  cut time: {removed:.2f}s  new length: {tl.total:.2f}s")

    xf_off = tl.total - XF_DUR
    total = xf_off + XF_DUR + END_HOLD
    hook_in = 0.15
    first_word = tl.map(cfg["segments"][0][0])
    hook_out = tl.map(cfg.get("hook_out", cfg["segments"][0][1]), "end")

    subs = []
    for a, b, txt in cfg["subs"]:
        na, nb = tl.map(a), tl.map(b, "end")
        subs.append([na, max(nb, na + 0.45), txt])
    for i in range(len(subs) - 1):
        subs[i][1] = min(subs[i][1], subs[i + 1][0] - 0.02)
    paper = cfg.get("paper")
    p_in = p_out = None
    if paper:
        p_in, p_out = tl.map(paper["in"]), tl.map(paper["out"], "end")

    # ---- cards -----------------------------------------------------------------
    pairs = []
    sh(["node", f"{T}/hook_html.js", f"{B}/hook.html", cfg["hook"]], stdout=subprocess.DEVNULL)
    pairs += [f"{B}/hook.html", f"{B}/hook.png"]
    for i, (_, _, txt) in enumerate(subs):
        sh(["node", f"{T}/subtitle_html.js", f"{B}/sub_{i:02d}.html", txt], stdout=subprocess.DEVNULL)
        pairs += [f"{B}/sub_{i:02d}.html", f"{B}/sub_{i:02d}.png"]
    if paper:
        sh(["node", f"{ROOT}/tools/paper_html.js", f"{B}/paper.html", str(paper["style"]), paper["photo"],
            paper.get("title", "")], stdout=subprocess.DEVNULL)
        pairs += [f"{B}/paper.html", f"{B}/paper.png"]
    pairs += [f"{T}/watermark.html", f"{B}/watermark.png", f"{T}/endcard.html", f"{B}/endcard.png"]
    sh(["node", f"{ROOT}/tools/render_many.js", str(S), *pairs], env=dict(os.environ, NODE_PATH=f"{ROOT}/tools/node_modules"))
    pos = {k: trim(f"{B}/{k}.png") for k in ["hook", "watermark"] + (["paper"] if paper else [])}
    for i in range(len(subs)):
        pos[f"sub_{i:02d}"] = trim(f"{B}/sub_{i:02d}.png")

    # ---- audio -------------------------------------------------------------------
    build_audio(cfg, tl, hook_in, p_in, xf_off, total, f"{B}/audio_mix.wav")

    # ---- video graph ----------------------------------------------------------------
    sel = "+".join(f"between(t,{a:.4f},{b:.4f})" for a, b in tl.iv)
    # framing blocks: change framing at phrase starts (and at every jump cut), >= BLOCK_MIN long
    marks = sorted(set([round(n, 3) for n in tl.new] +
                       [round(max(0.0, tl.map(a) - PAD_IN), 3) for a, _ in cfg["segments"]]))
    blocks = [0.0]
    for m in marks:
        if m - blocks[-1] >= BLOCK_MIN and tl.total - m >= BLOCK_MIN:
            blocks.append(m)
    blocks.append(tl.total + 1)
    print("framing blocks:", len(blocks) - 1)
    zterms = []
    for k in range(len(blocks) - 1):
        n, L = blocks[k], blocks[k + 1] - blocks[k]
        z = f"{PUNCH}" if k % 2 else f"(1+{DRIFT}*(t-{n:.4f})/{L:.4f})"
        zterms.append(f"gte(t,{n:.4f})*lt(t,{n + L:.4f})*{z}")
    Z = f"max(1,({'+'.join(zterms)}))"
    inputs = ["-i", cfg["src"]]
    reframe = (f"scale=w='2*trunc({W}*{Z}/2)':h='2*trunc({H}*{Z}/2)':eval=frame:flags=bicubic,"
               f"crop={W}:{H}:x='{FACE_X}*(iw-ow)':y='{FACE_Y}*(ih-oh)',") if cfg.get("reframe", True) else ""
    fc = [f"[0:v]fps={FPS},scale={W}:{H}:flags=lanczos,setsar=1,select='{sel}',setpts=N/{FPS}/TB,"
          f"{reframe}format=yuv420p,"
          f"vignette=angle=PI/6,trim=0:{xf_off + XF_DUR:.3f},setpts=PTS-STARTPTS[v0]"]
    idx, cur = 1, "v0"

    def add_img(png, start, dur, fi, fo, x, y, name, pre=""):
        nonlocal idx, cur
        inputs.extend(["-framerate", str(FPS), "-loop", "1", "-t", f"{dur:.3f}", "-i", png])
        fc.append(f"[{idx}:v]format=rgba,{pre}fade=in:st=0:d={fi}:alpha=1,"
                  f"fade=out:st={dur - fo:.3f}:d={fo}:alpha=1,setpts=PTS-STARTPTS+{start:.3f}/TB[{name}]")
        fc.append(f"[{cur}][{name}]overlay=x='{x}':y='{y}':eval=frame:eof_action=pass[{name}o]")
        cur = f"{name}o"; idx += 1

    wx, wy, _, _ = pos["watermark"]
    add_img(f"{B}/watermark.png", 0, xf_off + XF_DUR, 0.01, 0.01, wx, wy, "wm")
    hx, hy, _, _ = pos["hook"]
    u = f"min(1,max(0,(t-{hook_in})/0.55))"
    ease = f"(1+2.70158*pow({u}-1,3)+1.70158*pow({u}-1,2))"
    add_img(f"{B}/hook.png", hook_in, hook_out + 0.6 - hook_in, 0.28, 0.6, hx, f"{hy}-{170 * S}*(1-{ease})", "hk")
    if paper:
        px, py, pw, ph = pos["paper"]
        D = int(math.ceil(math.hypot(pw, ph) / 2) * 2)
        lu = "min(1,t/0.6)"   # card-local time (before setpts shift)
        lease = f"(1+2.70158*pow({lu}-1,3)+1.70158*pow({lu}-1,2))"
        rot = f"rotate=a='-6*PI/180*(1-{lease})':ow={D}:oh={D}:c=none,"
        pu = f"min(1,max(0,(t-{p_in:.3f})/0.6))"
        pease = f"(1+2.70158*pow({pu}-1,3)+1.70158*pow({pu}-1,2))"
        add_img(f"{B}/paper.png", p_in, p_out - p_in, 0.30, 0.45, px - (D - pw) // 2,
                f"{py - (D - ph) // 2}-{120 * S}*(1-{pease})", "pp", pre=rot)
    for i, (st, en, _) in enumerate(subs):
        sx, sy, _, _ = pos[f"sub_{i:02d}"]
        st -= 0.04
        p = f"min(1,(t-{st:.3f})/0.16)"
        add_img(f"{B}/sub_{i:02d}.png", st, en - st, 0.14, 0.12, sx, f"{sy}+{60 * S}*pow(1-{p},2)", f"s{i:02d}")
    inputs.extend(["-framerate", str(FPS), "-loop", "1", "-t", f"{XF_DUR + END_HOLD:.3f}", "-i", f"{B}/endcard.png"])
    fc.append(f"[{idx}:v]scale={W}:{H},format=yuv420p,setsar=1[ec]")
    fc.append(f"[{cur}]format=yuv420p[main]")
    fc.append(f"[main][ec]xfade=transition=smoothup:duration={XF_DUR}:offset={xf_off:.3f}[vout]")
    idx += 1
    inputs.extend(["-i", f"{B}/audio_mix.wav"])
    if preview:
        fc.append("[vout]scale=1080:1920,fps=30[vfin]")
        out = f"{B}/{cfg['out_name']}_preview_1080.mp4"
        venc = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "22"]
    else:
        fc.append("[vout]null[vfin]")
        out = f"{B}/{cfg['out_name']}_4K60_master.mp4"
        venc = ["-c:v", "libx265", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", "-tag:v", "hvc1",
                "-x265-params", "log-level=error", "-color_primaries", "bt709", "-color_trc", "bt709",
                "-colorspace", "bt709", "-r", str(FPS)]
    open(f"{B}/graph.txt", "w").write(";\n".join(fc))
    sh(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex_script", f"{B}/graph.txt",
        "-map", "[vfin]", "-map", f"{idx}:a", *venc, "-c:a", "aac", "-b:a", "320k",
        "-movflags", "+faststart", "-t", f"{total:.3f}", out])
    json.dump({"intervals": tl.iv, "subs": subs, "hook_out": hook_out, "paper": [p_in, p_out],
               "xf_off": xf_off, "total": total, "removed": removed}, open(f"{B}/timeline.json", "w"), indent=1)
    print("OUT", out)


if __name__ == "__main__":
    main()
