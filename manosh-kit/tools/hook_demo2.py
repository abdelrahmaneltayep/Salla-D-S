import subprocess, os
S = "/tmp/claude-0/-home-user-Salla-D-S/eed706bf-056f-536c-90ab-beced86b9c6d/scratchpad/rec_work/replay2/x1/x2/x3/x4/D/scratchpad"
B = f"{S}/hook10b"; SFX = f"{S}/kit2/sfx"; SEGD = f"{B}/seg"; os.makedirs(SEGD, exist_ok=True)
SRC = f"{S}/v6/src/source.mov"; VOICE = f"{S}/v6/work/voice_el.wav"
def run(a): subprocess.run(a, check=True)
for name, d in [("base34", 3.4), ("base59", 5.9)]:
    run(["ffmpeg", "-v", "error", "-y", "-i", SRC, "-i", VOICE, "-t", str(d), "-vf", "fps=30,scale=1080:1920,vignette=angle=PI/6",
         "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "2", f"{SEGD}/{name}.mov"])
seq = lambda d: ["-framerate", "30", "-i", f"{d}/f_%04d.png"]
FG = seq(f"{B}/fg")
opts = {
 1: ("Kinetic slam", "base34", seq(f"{B}/L1"), "[0:v][1:v]overlay=0:0[v]", [("impact", .17, -15), ("impact", .47, -15), ("impact", .77, -15), ("impact", 1.07, -9)]),
 2: ("Text behind her", "base34", seq(f"{B}/L2") + FG, "[2:v]crop=1080:1150:0:0[fg];[0:v][1:v]overlay=0:0[a];[a][fg]overlay=0:0[v]", [("whoosh_air", .15, -12), ("impact", .45, -12)]),
 3: ("Title card dive", "base34", seq(f"{B}/L3"),
     "[0:v]format=rgba,scale=w='2*trunc(540*if(lt(t,1.6),0.42,if(lt(t,2.2),0.42+0.58*(1-pow(1-(t-1.6)/0.6,3)),1)))':h='2*trunc(960*if(lt(t,1.6),0.42,if(lt(t,2.2),0.42+0.58*(1-pow(1-(t-1.6)/0.6,3)),1)))':eval=frame,"
     "fade=in:st=1.35:d=0.15:alpha=1[sv];[1:v]format=rgba[pg];[pg][sv]overlay=x='(W-w)/2':y='if(lt(t,1.6),1350,if(lt(t,2.2),1350-390*(1-pow(1-(t-1.6)/0.6,3)),960))-h/2':eval=frame:enable='gte(t,1.35)'[v]",
     [("whoosh_air", .10, -15), ("swoosh", 1.55, -9)]),
 4: ("Gravity drop", "base34", seq(f"{B}/L4"), "[0:v][1:v]overlay=0:0[v]", [("pop", .80 + i * .1, -16) for i in range(6)] + [("hook_land", 1.32, -11)]),
 5: ("Comment bubble", "base34", seq(f"{B}/L5"), "[0:v][1:v]overlay=0:0[v]", [("pop", .20, -10), ("typing", .45, -13), ("typing", 1.15, -15)]),
 6: ("Giant captions", "base59", seq(f"{B}/L6"), "[0:v][1:v]overlay=0:0[v]", [("pop", 2.15, -14), ("pop", 3.67, -14), ("pop", 5.03, -11)]),
 7: ("Magazine cover", "base34", seq(f"{B}/L7") + FG, "[2:v]crop=1080:1100:0:0[fg];[0:v][1:v]overlay=0:0[a];[a][fg]overlay=0:0[v]", [("swoosh", .15, -12), ("pop", .75, -14)]),
 8: ("Pinned title", "base34", seq(f"{B}/L8"), "[0:v][1:v]overlay=0:0[v]", [("swoosh", .15, -12)]),
 9: ("Pull-back reveal", "base34", seq(f"{S}/hook10/v4"),
     "[0:v]scale=w='2*trunc(540*if(lt(t,0.15),1.35,if(lt(t,1.05),1.35-0.35*(1-pow(1-(t-0.15)/0.9,3)),1)))':h='2*trunc(960*if(lt(t,0.15),1.35,if(lt(t,1.05),1.35-0.35*(1-pow(1-(t-0.15)/0.9,3)),1)))':eval=frame,"
     "crop=1080:1920:x='0.49*(iw-ow)':y='0.40*(ih-oh)'[z];[1:v]setpts=PTS+0.6/TB[h];[z][h]overlay=0:0:eof_action=repeat[v]",
     [("whoosh_air", .10, -10), ("pop", .75, -13), ("pop", .91, -13), ("pop", 1.07, -13)]),
 10: ("Screenplay page", "base34", seq(f"{B}/L10"), "[1:v]format=rgba[pg];[0:v][pg]overlay=0:0:enable='lt(t,2.6)'[v]",
      [("typing", .15, -13), ("typing", .80, -14), ("typing", 1.35, -13), ("swoosh", 2.55, -10)]),
}
files = []
for k, (label, base, ins, vgraph, cues) in opts.items():
    nin = 1 + ins.count("-i")
    args = ["-i", f"{SEGD}/{base}.mov", *ins]
    af, labs = [], ["[0:a]"]
    for j, (n, at, db) in enumerate(cues):
        args += ["-i", f"{SFX}/{n}.wav"]
        af.append(f"[{nin + j}:a]volume={db}dB,adelay={int(at * 1000)}|{int(at * 1000)}[s{j}]"); labs.append(f"[s{j}]")
    dur = 5.9 if base == "base59" else 3.4
    fc = (vgraph.replace("[v]", "[v0]", 1) if vgraph.endswith("[v]") else vgraph)
    fc = vgraph[:-3] + "[v0];" + f"[v0]drawbox=x=40:y=1770:w=600:h=96:color=0x4C2130@0.92:t=fill,drawtext=text='{k}  {label}':fontcolor=0xF3ECDF:fontsize=52:x=64:y=1792,trim=0:{dur},setpts=PTS-STARTPTS,format=yuv420p[v];" \
         + ";".join(af) + ";" + "".join(labs) + f"amix=inputs={len(labs)}:normalize=0:duration=first,atrim=0:{dur}[a]"
    out = f"{SEGD}/opt{k:02d}.mp4"
    run(["ffmpeg", "-v", "error", "-y", *args, "-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-r", "30",
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", out])
    files.append(out); print("segment", k, label)
open(f"{SEGD}/list.txt", "w").write("".join(f"file '{f}'\n" for f in files))
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{SEGD}/list.txt", "-c:v", "libx264", "-preset", "medium",
     "-crf", "21", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", f"{B}/Manosh_hook_10_options_reel_inspired.mp4"])
print("done")
