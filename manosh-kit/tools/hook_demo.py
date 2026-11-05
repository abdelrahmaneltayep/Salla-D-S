import subprocess, sys, os
S = "/tmp/claude-0/-home-user-Salla-D-S/eed706bf-056f-536c-90ab-beced86b9c6d/scratchpad/rec_work/replay2/x1/x2/x3/x4/D/scratchpad"
H = f"{S}/hook10"; SFX = f"{S}/kit2/sfx"
SRC = f"{S}/v6/src/source.mov"; VOICE = f"{S}/v6/work/voice_el.wav"
SEG = 3.4
names = {1: "Drop & settle", 2: "Stagger drop", 3: "Slide in", 4: "Pop", 5: "Type on",
         6: "Marker swipe", 7: "Gold punch", 8: "Focus pull", 9: "Band wipe", 10: "Mask rise"}
cues = {1: [("hook_whoosh", .10, -9), ("hook_land", .45, -10)],
        2: [("swoosh", .10, -12), ("hook_land", .45, -15), ("hook_land", .59, -15), ("hook_land", .73, -15)],
        3: [("swoosh", .12, -13), ("swoosh", .24, -15), ("swoosh", .36, -15)],
        4: [("pop", .15, -11), ("pop", .31, -11), ("pop", .47, -11)],
        5: [("typing", .15, -13), ("typing", .95, -13)],
        6: [("swipe", .15, -12), ("swipe", .37, -12), ("swipe", .59, -12)],
        7: [("whoosh_air", .10, -15), ("impact", .92, -9)],
        8: [("whoosh_air", .10, -10)],
        9: [("swoosh", .12, -10), ("whoosh_air", .48, -13)],
        10: [("swoosh", .12, -14), ("hook_land", .60, -16)]}
os.makedirs(f"{H}/seg", exist_ok=True)
# base clip once: first SEG seconds, 1080x1920 30fps, with voice
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC, "-i", VOICE, "-t", str(SEG), "-vf", "fps=30,scale=1080:1920,vignette=angle=PI/6",
                "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "2",
                f"{H}/seg/base.mov"], check=True)
for v in range(1, 11):
    ins = ["-i", f"{H}/seg/base.mov", "-framerate", "30", "-i", f"{H}/v{v}/f_%04d.png"]
    af = []; labels = ["[0:a]"]
    for k, (name, at, db) in enumerate(cues[v]):
        ins += ["-i", f"{SFX}/{name}.wav"]
        af.append(f"[{2 + k}:a]volume={db}dB,adelay={int(at * 1000)}|{int(at * 1000)}[s{k}]")
        labels.append(f"[s{k}]")
    fc = (f"[1:v]tpad=stop_mode=clone:stop_duration=2,format=rgba[h];[0:v][h]overlay=0:0:shortest=0:eof_action=repeat,"
          f"drawbox=x=40:y=60:w=520:h=96:color=0x4C2130@0.92:t=fill,"
          f"drawtext=text='{v}  {names[v]}':fontcolor=0xF3ECDF:fontsize=52:x=64:y=82,trim=0:{SEG},setpts=PTS-STARTPTS[v];"
          + ";".join(af) + (";" if af else "") + "".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,atrim=0:{SEG}[a]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    f"{H}/seg/opt{v:02d}.mp4"], check=True)
    print("segment", v, names[v])
open(f"{H}/seg/list.txt", "w").write("".join(f"file 'opt{v:02d}.mp4'\n" for v in range(1, 11)))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{H}/seg/list.txt",
                "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
                f"{H}/Manosh_hook_10_options.mp4"], check=True)
print("done")
