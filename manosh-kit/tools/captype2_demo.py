# 5 plain-caption options, each with its own zoom-cut style, + typing clicks.
import json, subprocess, numpy as np, wave
S = "/tmp/claude-0/-home-user-Salla-D-S/eed706bf-056f-536c-90ab-beced86b9c6d/scratchpad/rec_work/replay2/x1/x2/x3/x4/D/scratchpad"
C = f"{S}/captype2"; SR = 48000; DUR = 11.2
pages = json.load(open(f"{C}/pages.json"))
st = [p["start"] for p in pages]; bg = [p["big"][1] for p in pages]
nxt = st[1:] + [DUR + 1]
def seg(a, b, f): return f"between(t\\,{a:.3f}\\,{b:.3f})*({f})"
def zexpr(o):
    terms = []
    for i, (s, b, n) in enumerate(zip(st, bg, nxt)):
        n = n - 1e-3
        if o == 1: terms.append(seg(b, n, ".15"))
        if o == 2 and i % 2: terms.append(seg(s, n, ".12"))
        if o == 3: terms.append(seg(s, n, f".08*(t-{s:.3f})/{n - s:.3f}"))
        if o == 4: terms.append(seg(b, n, f".2*(1-pow(1-min(1\\,(t-{b:.3f})/.12)\\,3))"))
        if o == 5: terms.append(seg(s, n, f".18*pow(1-min(1\\,(t-{s:.3f})/.5)\\,3)"))
    return "1+" + "+".join(terms)
punch_times = {1: bg, 4: bg, 5: st}
def load(p):
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", p, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"])
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
typ = load(f"{S}/kit2/sfx/typing.wav"); imp = load(f"{S}/kit2/sfx/impact.wav")[:int(.5 * SR)]
imp[-int(.15 * SR):] *= np.linspace(1, 0, int(.15 * SR))[:, None]
clicks = []
for p in json.load(open(f"{S}/kit2/typing_peaks.json")):
    a = max(0, int((p - .006) * SR)); c = typ[a:a + int(.07 * SR)].copy()
    c[-int(.02 * SR):] *= np.linspace(1, 0, int(.02 * SR))[:, None]; clicks.append(c)
voice = load(f"{S}/v6/work/voice_el.wav")[:int(DUR * SR)]
def add(mix, c, t, db):
    at = int(t * SR); n = min(len(c), len(mix) - at); mix[at:at + n] += c[:n] * 10 ** (db / 20)
def audio(o):
    mix = voice.copy(); rng = np.random.default_rng(3); k = 0
    for p in pages:
        for w, t, db in [(w, t, -19) for w, t in p["small"]] + [(p["big"][0], p["big"][1], -15)]:
            for i in range(len(w)):
                add(mix, clicks[k % len(clicks)] * rng.uniform(.8, 1.1), t + i * .035, db); k += 1
    for t in punch_times.get(o, []): add(mix, imp, t, -21)
    mix = np.clip(mix / max(1, np.abs(mix).max() / .95), -1, 1)
    out = f"{C}/audio_{o}.wav"
    with wave.open(out, "wb") as wv:
        wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes((mix * 32767).astype(np.int16).tobytes())
    return out
names = {1: "1  Punch on big word", 2: "2  Alternate cut", 3: "3  Slow push", 4: "4  Snap zoom", 5: "5  Pull-back per page"}
segs = []
for o in range(1, 6):
    z = zexpr(o); out = f"{C}/seg_{o}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-t", str(DUR), "-i", f"{S}/v6/src/source.mov", "-framerate", "30", "-i", f"{C}/s{o}/f_%04d.png",
        "-i", audio(o), "-filter_complex",
        f"[0:v]fps=30,scale=w='2*trunc(1080*({z})/2)':h='2*trunc(1920*({z})/2)':eval=frame:flags=lanczos,"
        f"crop=1080:1920:x='0.49*(iw-ow)':y='0.40*(ih-oh)',setsar=1,vignette=angle=PI/6[b];"
        f"[b][1:v]overlay=0:0:eof_action=repeat,drawbox=x=40:y=1770:w=700:h=96:color=0x4C2130@0.92:t=fill,"
        f"drawtext=text='{names[o]}':fontcolor=0xF3ECDF:fontsize=50:x=64:y=1793,trim=0:{DUR},format=yuv420p[v]",
        "-map", "[v]", "-map", "2:a", "-r", "30", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-t", str(DUR), out], check=True)
    segs.append(out); print("seg", o)
open(f"{C}/list.txt", "w").write("".join(f"file '{p}'\n" for p in segs))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{C}/list.txt", "-c:v", "libx264", "-preset", "medium", "-crf", "21",
    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", f"{C}/Manosh_plain_captions_5options.mp4"], check=True)
print("done")
