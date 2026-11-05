import sys, json, wave, numpy as np, sherpa_onnx as so
M="models/sherpa-onnx-zipformer-gigaspeech-2023-12-12/"
segs=json.load(open(sys.argv[1]))
with wave.open(sys.argv[2]) as f:
    a=np.frombuffer(f.readframes(f.getnframes()),dtype=np.int16).astype(np.float32)/32768
rec=so.OfflineRecognizer.from_transducer(encoder=M+"encoder-epoch-30-avg-1.int8.onnx",decoder=M+"decoder-epoch-30-avg-1.int8.onnx",
  joiner=M+"joiner-epoch-30-avg-1.int8.onnx",tokens=M+"tokens.txt",num_threads=4,decoding_method="modified_beam_search")
words=[]
for sg in segs:
    s0=max(0,sg["start"]-0.15); s1=sg["end"]+0.15
    st=rec.create_stream(); st.accept_waveform(16000,a[int(s0*16000):int(s1*16000)]); rec.decode_stream(st)
    r=st.result; cur=None
    for tok,t in zip(r.tokens,r.timestamps):
        if tok.startswith(" ") or tok.startswith("▁") or cur is None:
            if cur: words.append(cur)
            cur={"w":tok.replace("▁","").strip(),"s":round(s0+t,2)}
        else: cur["w"]+=tok
    if cur: words.append(cur)
    print(f"[{sg['start']:.2f}] "+" ".join(f"{w['w'].lower()}@{w['s']:.2f}" for w in words if w['s']>=s0-0.01 and w['s']<=s1))
json.dump(words,open(sys.argv[3],"w"),indent=0)
