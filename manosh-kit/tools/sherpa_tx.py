import sys, json, wave, numpy as np, sherpa_onnx as so
M="models/sherpa-onnx-whisper-medium/"
wav, lang, out = sys.argv[1], sys.argv[2], sys.argv[3]
with wave.open(wav) as f:
    a = np.frombuffer(f.readframes(f.getnframes()), dtype=np.int16).astype(np.float32)/32768
sr=16000
rec = so.OfflineRecognizer.from_whisper(encoder=M+"medium-encoder.int8.onnx", decoder=M+"medium-decoder.int8.onnx",
    tokens=M+"medium-tokens.txt", language=lang, task="transcribe", num_threads=4)
cfg = so.VadModelConfig(); cfg.silero_vad.model="models/silero_vad.onnx"
cfg.silero_vad.min_silence_duration=float(sys.argv[4]) if len(sys.argv)>4 else 0.25
cfg.silero_vad.min_speech_duration=0.2; cfg.silero_vad.max_speech_duration=12; cfg.sample_rate=sr
vad = so.VoiceActivityDetector(cfg, buffer_size_in_seconds=60)
ws=cfg.silero_vad.window_size; segs=[]
for i in range(0,len(a),ws):
    vad.accept_waveform(a[i:i+ws])
    while not vad.empty():
        segs.append((vad.front.start, np.array(vad.front.samples))); vad.pop()
vad.flush()
while not vad.empty():
    segs.append((vad.front.start, np.array(vad.front.samples))); vad.pop()
res=[]
for st, s in segs:
    stream=rec.create_stream(); stream.accept_waveform(sr, s); rec.decode_stream(stream)
    t0=st/sr; t1=t0+len(s)/sr; txt=stream.result.text.strip()
    res.append({"start":round(t0,2),"end":round(t1,2),"text":txt}); print(f"[{t0:6.2f}-{t1:6.2f}] {txt}")
json.dump(res, open(out,"w"), ensure_ascii=False, indent=1)
