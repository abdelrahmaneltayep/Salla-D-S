# OPT-IN ONLY — zoom cuts were removed from the Manosh kit on 2026-10-26 (frame stays steady).
# Zoom cuts on the VIDEO frame (kept for when a video explicitly asks for them).
# Hard cuts between a close-up and the wide shot, one per caption page:
# page 1 close, page 2 wide, page 3 close, ...; wide before the first page.
# Crops per frame from the full-res source with zoompan, holding the face at 46.9% of frame height.
# Usage: python3 zoom_cuts.py <source.mov> <words.json> <out.mp4> [--close 1.42] [--size 2160x3840] [--fps 60]
#        [--face-x 0.5] [--face-y 0.4375] [--dur seconds]
# words.json: same file as templates/chips_html.js. Output is video-only (CRF 12 intermediate for compositing).
import argparse, json, subprocess
ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("pages"); ap.add_argument("out")
ap.add_argument("--close", type=float, default=1.42); ap.add_argument("--size", default="2160x3840")
ap.add_argument("--fps", type=int, default=60); ap.add_argument("--face-x", type=float, default=.5)
ap.add_argument("--face-y", type=float, default=.4375); ap.add_argument("--dur", type=float)
a = ap.parse_args()
pages = json.load(open(a.pages))
dur = a.dur or pages[-1]["end"] + .2
st = [p["start"] for p in pages]; nxt = st[1:] + [dur + 1]
T = f"(in/{a.fps})"
terms = [f"between({T}\\,{s:.3f}\\,{n - 1e-3:.3f})*{a.close - 1:.3f}" for i, (s, n) in enumerate(zip(st, nxt)) if i % 2 == 0]
z = "1+" + "+".join(terms) if terms else "1"
x = f"min(max(0\\,{a.face_x}*iw-0.5*iw/zoom)\\,iw-iw/zoom)"
y = f"min(max(0\\,{a.face_y}*ih-0.46875*ih/zoom)\\,ih-ih/zoom)"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-t", str(dur), "-i", a.src, "-vf",
    f"fps={a.fps},zoompan=z='{z}':x='{x}':y='{y}':d=1:s={a.size}:fps={a.fps},setsar=1,format=yuv420p",
    "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "12", "-t", str(dur), a.out], check=True)
print("zoom-cut base ->", a.out)
