# Zoomed base clips (wide <-> close-up hard cuts on the face) + person mattes for the 5 reference-inspired options.
import json, subprocess, sys
S = "/tmp/claude-0/-home-user-Salla-D-S/eed706bf-056f-536c-90ab-beced86b9c6d/scratchpad/rec_work/replay2/x1/x2/x3/x4/D/scratchpad"
C = f"{S}/captype2"; DUR = 11.2
pages = json.load(open(f"{C}/pages3.json"))
st = [p["start"] for p in pages]; bg = [p["big"][1] for p in pages]; nxt = st[1:] + [DUR + 1]
def seg(a, b, f): return f"between(in/30\\,{a:.3f}\\,{b - 1e-3:.3f})*({f})"
def zoom(o):
    t = []
    for i, (s, b, n) in enumerate(zip(st, bg, nxt)):
        if o == 1: t.append(seg(b, n, ".42"))                      # wide, cut to close-up on the key word
        if o == 2 and i % 2: t.append(seg(s, n, ".35"))            # alternate wide / close per line
        if o == 3 and not i % 2: t.append(seg(s, n, ".3"))         # alternate close / wide per line
        if o == 4 and not i % 2: t.append(seg(s, n, ".42"))        # starts close, then wide
        if o == 5: t.append(seg(s, n, ".12" if not i % 2 else "0") + "+" + seg(b, n, ".3"))   # medium/wide + punch on key word
    return "1+" + "+".join(t)
for o in map(int, sys.argv[1:] or range(1, 6)):
    z = zoom(o); base = f"{C}/rb_{o}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-t", str(DUR), "-i", f"{S}/v6/src/source.mov", "-vf",
        # zoompan crops per frame from the full-res source; face (x=.5, y=.4375 of frame) held at y=900/1920 when zoomed
        f"fps=30,zoompan=z='{z}':x='iw/2-iw/zoom/2':y='min(max(0\\,0.4375*ih-0.46875*ih/zoom)\\,ih-ih/zoom)':d=1:s=1080x1920:fps=30,"
        f"setsar=1,vignette=angle=PI/6,format=yuv420p",
        "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "12", "-t", str(DUR), base], check=True)
    if o in (1, 3, 5):
        subprocess.run(["python3", f"{S}/tools/mask_video.py", base, f"{C}/rm_{o}.mkv", f"{S}/models/seg/selfie_multiclass.tflite"], check=True)
    print("base", o, flush=True)
