import json, sys
from faster_whisper import WhisperModel
m = WhisperModel(sys.argv[2] if len(sys.argv)>2 else "medium", device="cpu", compute_type="int8", cpu_threads=4)
segs, info = m.transcribe(sys.argv[1], word_timestamps=True, vad_filter=False, beam_size=5)
print("lang", info.language, info.language_probability, file=sys.stderr)
out=[]
for s in segs:
    out.append({"start":s.start,"end":s.end,"text":s.text,"words":[{"w":w.word,"s":w.start,"e":w.end} for w in s.words]})
    print(f"[{s.start:6.2f}-{s.end:6.2f}] {s.text}", file=sys.stderr)
json.dump(out, open(sys.argv[3] if len(sys.argv)>3 else "work/transcript.json","w"), ensure_ascii=False, indent=1)
