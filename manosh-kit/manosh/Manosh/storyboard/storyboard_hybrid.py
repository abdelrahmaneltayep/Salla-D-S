# Hybrid storyboard base video: animated AI clips for key moments + cinematic camera moves on the stills.
# Usage: python3 storyboard_hybrid.py <scenes.json> <img_dir> <out.mp4> [W=1080] [H=1920] [fps=30]
# scenes.json: [{"start","end","img", "video"?: path, "move"?: push|pull|up|down|left|right}]
#   video: an animated clip (any size, any length). It is scaled/cropped to fill WxH. If it is shorter than
#          the scene it is slowed down (max 1.6x slower) and then holds on its last frame.
#   move:  camera move for stills (default cycles push, left, up, pull, right, down).
import json, subprocess, sys
scenes_p, img_dir, out = sys.argv[1:4]
W, H, FPS = (int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])) if len(sys.argv) > 6 else (1080, 1920, 30)
XF = 0.6
CYCLE = ["push", "left", "up", "pull", "right", "down"]
sc = json.load(open(scenes_p))


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                                capture_output=True, text=True).stdout.strip())


inputs, fc = [], []
for i, s in enumerate(sc):
    d = s["end"] - s["start"] + (XF if i < len(sc) - 1 else 0)
    n = int(round(d * FPS)) + 1
    if s.get("video"):
        # optional "lead": seconds of the still (a gentle pull-out that lands exactly on the clip's first frame)
        lead = float(s.get("lead", 0))
        vd = dur(s["video"])
        rest = d - lead
        slow = min(1.25, max(1.0, rest / vd))     # gentle slow-down only; motion-interpolated to FPS
        c = min(vd * slow, rest)
        last = out + f".last{i}.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.1", "-i", s["video"], "-frames:v", "1", "-update", "1", last], check=True)
        parts = []
        if lead > 0.05:
            li0 = sum(1 for a in inputs if a == "-i")
            inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{lead + 0.2:.3f}", "-i", f"{img_dir}/{s['img']}"]
            nl = int(round(lead * FPS)) + 1
            fc.append(f"[{li0}:v]scale={W * 2}:{H * 2}:force_original_aspect_ratio=increase:flags=lanczos,crop={W * 2}:{H * 2},"
                      f"zoompan=z='1.06-0.06*(0.5-0.5*cos(PI*on/{nl}))':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':d=1:s={W}x{H}:fps={FPS},"
                      f"trim=0:{lead:.3f},setpts=PTS-STARTPTS,format=yuv420p,fps={FPS},settb=1/{FPS}[l{i}]")
            parts.append(f"[l{i}]")
        vi = sum(1 for a in inputs if a == "-i")
        inputs += ["-i", s["video"]]
        fc.append(f"[{vi}:v]scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},"
                  f"setpts={slow:.4f}*(PTS-STARTPTS),minterpolate=fps={FPS}:mi_mode=mci:mc_mode=aobmc:vsbmc=1,"
                  f"trim=0:{c:.3f},setpts=PTS-STARTPTS,format=yuv420p,fps={FPS},settb=1/{FPS}[v{i}]")
        parts.append(f"[v{i}]")
        tl = rest - c
        if tl > 0.05:
            ti = sum(1 for a in inputs if a == "-i")
            inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{tl + 0.2:.3f}", "-i", last]
            nn = int(round(tl * FPS)) + 1
            fc.append(f"[{ti}:v]scale={W * 2}:{H * 2}:force_original_aspect_ratio=increase:flags=lanczos,crop={W * 2}:{H * 2},"
                      f"zoompan=z='1+0.05*on/{nn}':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)*0.45':d=1:s={W}x{H}:fps={FPS},"
                      f"trim=0:{tl:.3f},setpts=PTS-STARTPTS,format=yuv420p,fps={FPS},settb=1/{FPS}[t{i}]")
            parts.append(f"[t{i}]")
        fc.append(f"{''.join(parts)}concat=n={len(parts)}:v=1:a=0,trim=0:{d:.3f},setpts=PTS-STARTPTS,fps={FPS},settb=1/{FPS}[s{i}]")
        continue
    mv = s.get("move", CYCLE[i % len(CYCLE)])
    ii = sum(1 for a in inputs if a == "-i")
    inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{d:.3f}", "-i", f"{img_dir}/{s['img']}"]
    p = f"(on/{n})"
    ease = f"(0.5-0.5*cos(PI*{p}))"                      # ease-in-out
    if mv == "pull":
        z = f"1.12-0.12*{ease}"
    elif mv == "push":
        z = f"1+0.12*{ease}"
    else:
        z = "1.10"
    cx, cy = "(iw-iw/zoom)/2", "(ih-ih/zoom)*0.45"
    if mv == "left":
        cx = f"(iw-iw/zoom)*(0.85-0.7*{ease})"
    elif mv == "right":
        cx = f"(iw-iw/zoom)*(0.15+0.7*{ease})"
    elif mv == "up":
        cy = f"(ih-ih/zoom)*(0.85-0.7*{ease})"
    elif mv == "down":
        cy = f"(ih-ih/zoom)*(0.10+0.7*{ease})"
    fc.append(f"[{ii}:v]scale={W * 2}:{H * 2}:flags=lanczos,zoompan=z='{z}':x='{cx}':y='{cy}':d=1:"
              f"s={W}x{H}:fps={FPS},trim=0:{d:.3f},setpts=PTS-STARTPTS,format=yuv420p"
                  f",fps={FPS},settb=1/{FPS}[s{i}]")
cur, t = "s0", sc[0]["end"] - sc[0]["start"]
for i in range(1, len(sc)):
    fc.append(f"[{cur}][s{i}]xfade=transition=fade:duration={XF}:offset={t:.3f}[x{i}]")
    cur = f"x{i}"; t += sc[i]["end"] - sc[i]["start"]
open(out + ".graph.txt", "w").write(";\n".join(fc))
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex_script", out + ".graph.txt", "-map", f"[{cur}]",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "14", "-pix_fmt", "yuv420p", out], check=True)
print("storyboard hybrid ->", out, f"{t:.2f}s")
