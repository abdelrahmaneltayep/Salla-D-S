# 5 options: highlight blocks on some words + zoom cuts on the TEXT (video frame static) + typing clicks.
import json, subprocess, numpy as np, wave
S = "/tmp/claude-0/-home-user-Salla-D-S/eed706bf-056f-536c-90ab-beced86b9c6d/scratchpad/rec_work/replay2/x1/x2/x3/x4/D/scratchpad"
C = f"{S}/captype2"; SR = 48000; DUR = 11.2
pages = json.load(open(f"{C}/pages3.json"))
def load(p):
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", p, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"])
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
def trim(x, d, fade):
    x = x[:int(d * SR)].copy(); x[-int(fade * SR):] *= np.linspace(1, 0, int(fade * SR))[:, None]; return x
typ = load(f"{S}/kit2/sfx/typing.wav"); imp = trim(load(f"{S}/kit2/sfx/impact.wav"), .5, .15)
swo = trim(load(f"{S}/kit2/sfx/swoosh.wav"), .45, .15)
clicks = [trim(typ[max(0, int((p - .006) * SR)):], .07, .02) for p in json.load(open(f"{S}/kit2/typing_peaks.json"))]
voice = load(f"{S}/v6/work/voice_el.wav")[:int(DUR * SR)]
def add(mix, c, t, db):
    at = int(t * SR); n = min(len(c), len(mix) - at); mix[at:at + n] += c[:n] * 10 ** (db / 20)
words = lambda p: [(w, t, len(r) > 2) for w, t, *r in p["small"]] + [(p["big"][0], p["big"][1], len(p["big"]) > 2)]
cues = {1: [(p["big"][1], imp, -21) for p in pages], 2: [(p["big"][1], imp, -19) for p in pages],
        3: [(p["start"], swo, -24) for p in pages], 4: [(p["big"][1], imp, -21) for p in pages],
        5: [(t + len(w) * .035, imp, -20) for p in pages for w, t, h in words(p) if h]}
def audio(o):
    mix = voice.copy(); rng = np.random.default_rng(3); k = 0
    for p in pages:
        for j, (w, t, h) in enumerate(words(p)):
            db = -15 if h else (-16 if w == p["big"][0] and t == p["big"][1] else -19)
            for i in range(len(w)):
                add(mix, clicks[k % len(clicks)] * rng.uniform(.8, 1.1), t + i * .035, db); k += 1
    for t, c, db in cues[o]: add(mix, c, t, db)
    mix = np.clip(mix / max(1, np.abs(mix).max() / .95), -1, 1)
    out = f"{C}/audio3_{o}.wav"
    with wave.open(out, "wb") as wv:
        wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes((mix * 32767).astype(np.int16).tobytes())
    return out
names = {1: "1  Punch cut", 2: "2  Snap-in word", 3: "3  Pull-back", 4: "4  Step cuts", 5: "5  Pulse on highlight"}
segs = []
for o in range(1, 6):
    out = f"{C}/seg3_{o}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-t", str(DUR), "-i", f"{S}/v6/src/source.mov", "-framerate", "30", "-i", f"{C}/h{o}/f_%04d.png",
        "-i", audio(o), "-filter_complex",
        f"[0:v]fps=30,scale=1080:1920,setsar=1,vignette=angle=PI/6[b];"
        f"[b][1:v]overlay=0:0:eof_action=repeat,drawbox=x=40:y=1770:w=700:h=96:color=0x4C2130@0.92:t=fill,"
        f"drawtext=text='{names[o]}':fontcolor=0xF3ECDF:fontsize=50:x=64:y=1793,trim=0:{DUR},format=yuv420p[v]",
        "-map", "[v]", "-map", "2:a", "-r", "30", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-t", str(DUR), out], check=True)
    segs.append(out); print("seg", o)
open(f"{C}/list3.txt", "w").write("".join(f"file '{p}'\n" for p in segs))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{C}/list3.txt", "-c:v", "libx264", "-preset", "medium", "-crf", "23",
    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", f"{C}/Manosh_highlight_text_zoomcuts_5options.mp4"], check=True)
print("done")
