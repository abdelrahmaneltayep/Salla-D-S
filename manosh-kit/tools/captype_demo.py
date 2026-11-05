import json, subprocess, numpy as np, wave, os
S = "/tmp/claude-0/-home-user-Salla-D-S/eed706bf-056f-536c-90ab-beced86b9c6d/scratchpad/rec_work/replay2/x1/x2/x3/x4/D/scratchpad"
C = f"{S}/captype"; SR = 48000; DUR = 11.2
def load(p):
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", p, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"])
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
typ = load(f"{S}/kit2/sfx/typing.wav")
peaks = json.load(open(f"{S}/kit2/typing_peaks.json"))
clicks = []
for p in peaks:
    a = max(0, int((p - .006) * SR)); c = typ[a:a + int(.07 * SR)].copy()
    c[-int(.02 * SR):] *= np.linspace(1, 0, int(.02 * SR))[:, None]; clicks.append(c)
voice = load(f"{S}/v6/work/voice_el.wav")[:int(DUR * SR)]
mix = voice.copy()
rng = np.random.default_rng(3); k = 0
for pg in json.load(open(f"{C}/pages.json")):
    for w, t, key in pg["words"]:
        for i in range(len(w)):
            at = int((t + i * .035) * SR); c = clicks[k % len(clicks)]; k += 1
            g = 10 ** ((-16 if key else -19) / 20) * rng.uniform(.8, 1.1)
            mix[at:at + len(c)] += c[:len(mix) - at] * g
mix = np.clip(mix / max(1, np.abs(mix).max() / .95), -1, 1)
with wave.open(f"{C}/audio.wav", "wb") as wv:
    wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes((mix * 32767).astype(np.int16).tobytes())
names = {"A": "A  Burgundy blocks", "B": "B  Bold outline", "C": "C  Cream + terracotta"}
segs = []
for st in "ABC":
    out = f"{C}/seg_{st}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-t", str(DUR), "-i", f"{S}/v6/src/source.mov", "-framerate", "30", "-i", f"{C}/{st}/f_%04d.png",
        "-i", f"{C}/audio.wav", "-filter_complex",
        f"[0:v]fps=30,scale=1080:1920,vignette=angle=PI/6[b];[b][1:v]overlay=0:0:eof_action=repeat,drawbox=x=40:y=1770:w=640:h=96:color=0x4C2130@0.92:t=fill,"
        f"drawtext=text='{names[st]}':fontcolor=0xF3ECDF:fontsize=52:x=64:y=1792,trim=0:{DUR},format=yuv420p[v]",
        "-map", "[v]", "-map", "2:a", "-r", "30", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-t", str(DUR), out], check=True)
    segs.append(out)
open(f"{C}/list.txt", "w").write("".join(f"file '{p}'\n" for p in segs))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{C}/list.txt", "-c:v", "libx264", "-preset", "medium", "-crf", "21",
    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", f"{C}/Manosh_giant_typed_captions_3styles.mp4"], check=True)
print("done")
