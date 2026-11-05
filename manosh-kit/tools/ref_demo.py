# Compose the 5 reference-inspired options: base (zoom cuts) -> giant word -> person cut-out -> front captions; + SFX.
import json, subprocess, numpy as np, wave, os
S = "/tmp/claude-0/-home-user-Salla-D-S/eed706bf-056f-536c-90ab-beced86b9c6d/scratchpad/rec_work/replay2/x1/x2/x3/x4/D/scratchpad"
C = f"{S}/captype2"; R = f"{C}/R"; SR = 48000; DUR = 11.2
pages = json.load(open(f"{C}/pages3.json"))
def load(p):
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", p, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"])
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
def trim(x, d, fade):
    x = x[:int(d * SR)].copy(); x[-int(fade * SR):] *= np.linspace(1, 0, int(fade * SR))[:, None]; return x
typ = load(f"{S}/kit2/sfx/typing.wav"); imp = trim(load(f"{S}/kit2/sfx/impact.wav"), .5, .15)
swo = trim(load(f"{S}/kit2/sfx/swoosh.wav"), .45, .15); pop = trim(load(f"{S}/kit2/sfx/pop.wav"), .25, .08)
clicks = [trim(typ[max(0, int((p - .006) * SR)):], .07, .02) for p in json.load(open(f"{S}/kit2/typing_peaks.json"))]
voice = load(f"{S}/v6/work/voice_el.wav")[:int(DUR * SR)]
def add(mix, c, t, db):
    at = int(t * SR); n = min(len(c), len(mix) - at); mix[at:at + n] += c[:n] * 10 ** (db / 20)
def audio(o):
    mix = voice.copy(); rng = np.random.default_rng(3); k = 0
    for p in pages:
        for w, t, *_ in p["small"]:                       # one key click per word as it appears
            add(mix, clicks[k % len(clicks)] * rng.uniform(.8, 1.1), t, -19 if o != 4 else -21); k += 1
            if o == 4: add(mix, pop, t, -27)
        w, t = p["big"][:2]
        if o == 1: add(mix, imp, t, -20)
        if o == 2: add(mix, clicks[k % len(clicks)], t, -16); k += 1
        if o == 3: add(mix, swo, t - .08, -23)
        if o == 4: add(mix, pop, t, -21)
        if o == 5:
            for i in range(len(w)): add(mix, clicks[k % len(clicks)] * rng.uniform(.8, 1.1), t + i * .035, -15); k += 1
    mix = np.clip(mix / max(1, np.abs(mix).max() / .95), -1, 1)
    out = f"{C}/ra_{o}.wav"
    with wave.open(out, "wb") as wv:
        wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes((mix * 32767).astype(np.int16).tobytes())
    return out
names = {1: "1  Giant word + tags", 2: "2  Underline keyword", 3: "3  Editorial serif", 4: "4  Word chips", 5: "5  Chips + typed giant"}
segs = []
for o in range(1, 6):
    out = f"{C}/rseg_{o}.mp4"; hasb = os.path.isdir(f"{R}/o{o}_back")
    inp = ["-i", f"{C}/rb_{o}.mp4"]
    if hasb: inp += ["-framerate", "30", "-i", f"{R}/o{o}_back/f_%04d.png", "-i", f"{C}/rm_{o}.mkv"]
    inp += ["-framerate", "30", "-i", f"{R}/o{o}_front/f_%04d.png", "-i", audio(o)]
    fi = 3 if hasb else 1
    fc = (f"[0:v]split[v0][v1];[v0][1:v]overlay=0:0:eof_action=repeat[b1];[2:v]format=gray[m];[v1][m]alphamerge[pp];[b1][pp]overlay=0:0[b2];"
          if hasb else "[0:v]null[b2];")
    fc += (f"[b2][{fi}:v]overlay=0:0:eof_action=repeat,drawbox=x=40:y=1770:w=760:h=96:color=0x4C2130@0.92:t=fill,"
           f"drawtext=text='{names[o]}':fontcolor=0xF3ECDF:fontsize=50:x=64:y=1793,trim=0:{DUR},format=yuv420p[v]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", fc, "-map", "[v]", "-map", f"{fi + 1}:a", "-r", "30",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-t", str(DUR), out], check=True)
    segs.append(out); print("seg", o, flush=True)
open(f"{C}/rlist.txt", "w").write("".join(f"file '{p}'\n" for p in segs))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{C}/rlist.txt", "-c:v", "libx264", "-preset", "medium", "-crf", "23",
    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", f"{C}/Manosh_ref_inspired_5options.mp4"], check=True)
print("done")
