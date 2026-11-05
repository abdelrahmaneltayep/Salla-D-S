#!/usr/bin/env bash
# Gentle background-noise reduction that PRESERVES the creator's original voice.
# Unlike isolate_voice.sh (ElevenLabs AI Voice Isolator), this does NOT
# re-synthesise/colour the voice and does NOT gate out quiet onsets -- so the
# opening word survives and the timbre stays natural.
# Chain: highpass rumble cut -> FFT spectral denoise (afftdn) -> loudnorm.
# Usage: denoise_voice.sh <input_media> <out_clean.wav>
set -euo pipefail
export PATH="/opt/homebrew/bin:/usr/bin:/bin:$PATH"

IN="$1"; OUT="$2"

# 1) highpass=f=80      -> remove sub-80Hz room rumble/handling noise
# 2) afftdn nr=12 nf=-25 nt=w -> gentle broadband denoise, white-noise tracking;
#                        nr (noise reduction) kept modest so speech is untouched.
# 3) loudnorm           -> broadcast target, matches the rest of the pipeline.
ffmpeg -y -v error -i "$IN" -vn \
  -af "highpass=f=80,afftdn=nr=12:nf=-25:nt=w,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000" \
  -ac 2 -ar 48000 -c:a pcm_s16le "$OUT"

echo "=== denoised voice (original preserved): $OUT ==="
ffprobe -v error -show_entries stream=codec_name,sample_rate,channels,duration \
  -of default=nw=1 "$OUT"
