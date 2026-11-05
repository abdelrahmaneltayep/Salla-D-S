# Sound design for the word-chip style (LOCKED 2026-10-26) — no music.
# Typing sound on the hook chips: one key click per letter, 35 ms apart, starting when the chip appears
# (-19 dB; key words -16 dB), plus a soft pop under each key-word chip (-24 dB).
# Usage: python3 chips_sfx.py <voice_clean.wav> <words.json> <out.wav>
import json, os, subprocess, sys, wave
import numpy as np
voice_p, pages_p, out = sys.argv[1:4]
SFX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sfx"); SR = 48000
def load(p):
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", p, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"])
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
def trim(x, d, fade):
    x = x[:int(d * SR)].copy(); x[-int(fade * SR):] *= np.linspace(1, 0, int(fade * SR))[:, None]; return x
typ = load(f"{SFX}/typing.wav"); pop = trim(load(f"{SFX}/pop.wav"), .25, .08)
clicks = [trim(typ[max(0, int((p - .006) * SR)):], .07, .02) for p in json.load(open(f"{SFX}/typing_peaks.json"))]
mix = load(voice_p)
def add(c, t, db):
    at = int(t * SR); n = min(len(c), len(mix) - at)
    if n > 0: mix[at:at + n] += c[:n] * 10 ** (db / 20)
rng = np.random.default_rng(3); k = 0
for p in json.load(open(pages_p)):
    for w, t, *key in p["words"]:          # typing: one key click per letter, 35 ms apart
        kw = bool(key and key[0])
        for i in range(len(w)):
            add(clicks[k % len(clicks)] * rng.uniform(.8, 1.1), t + i * .035, -16 if kw else -19); k += 1
        if kw: add(pop, t, -24)
mix = np.clip(mix / max(1, np.abs(mix).max() / .95), -1, 1)
with wave.open(out, "wb") as wv:
    wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes((mix * 32767).astype(np.int16).tobytes())
print("voice + chip SFX ->", out)
