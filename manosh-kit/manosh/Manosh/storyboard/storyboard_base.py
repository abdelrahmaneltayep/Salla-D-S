# Full-frame vertical storyboard base video: each scene image (paper_full.py output) gets a slow
# push-in / drift (alternating), scenes cross-dissolve. Captions, chips, voice are added by build_v8.py.
# Usage: python3 storyboard_base.py <scenes.json> <img_dir> <out.mp4> [W=1080] [H=1920] [fps=30]
# scenes.json: [{"start","end","img"}] consecutive, covering the whole voice.
import json, subprocess, sys
scenes_p, img_dir, out = sys.argv[1:4]
W, H, FPS = (int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])) if len(sys.argv) > 6 else (1080, 1920, 30)
XF = 0.6
sc = json.load(open(scenes_p))
inputs, fc = [], []
for i, s in enumerate(sc):
    d = s["end"] - s["start"] + (XF if i < len(sc) - 1 else 0)
    n = int(round(d * FPS)) + 1
    inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{d:.3f}", "-i", f"{img_dir}/{s['img']}"]
    z = f"1+0.07*on/{n}"                                                   # slow push-in, 1.00 -> 1.07
    x = f"(iw-iw/zoom)/2+({-1 if i % 2 else 1})*(iw-iw/zoom)*0.25*on/{n}"  # gentle drift, alternating side
    fc.append(f"[{i}:v]scale={W * 2}:{H * 2}:flags=lanczos,zoompan=z='{z}':x='{x}':y='(ih-ih/zoom)*0.45':d=1:"
              f"s={W}x{H}:fps={FPS},trim=0:{d:.3f},setpts=PTS-STARTPTS,format=yuv420p[s{i}]")
cur, t = "s0", sc[0]["end"] - sc[0]["start"]
for i in range(1, len(sc)):
    fc.append(f"[{cur}][s{i}]xfade=transition=fade:duration={XF}:offset={t:.3f}[x{i}]")
    cur = f"x{i}"; t += sc[i]["end"] - sc[i]["start"]
open(out + ".graph.txt", "w").write(";\n".join(fc))
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex_script", out + ".graph.txt", "-map", f"[{cur}]",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "14", "-pix_fmt", "yuv420p", out], check=True)
print("storyboard base ->", out, f"{t:.2f}s")
