#!/usr/bin/env bash
# [RECOVERED 2026-11-05] Rebuilds the Manosh kit SFX exactly as they were made in the session
# (ElevenLabs Sound Effects API + ffmpeg post-processing). The original .wav/.mp3 files were lost;
# ElevenLabs generations are not deterministic, so re-running gives new takes with the same prompts.
#
# Kit files produced (Manosh/audio/sfx/): typing.wav, pop.wav, typing_peaks.json, scroll_open.wav, scroll_close.wav
# Extra files build_v8.py reads from <scratchpad>/kit2/sfx/: scroll_open.wav, scroll_close.wav, paper_place.wav
#
# Needs ELEVENLABS_API_KEY in the environment (never hard-code it). Costs ElevenLabs credits.
# Usage: ELEVENLABS_API_KEY=... bash REGENERATE_SFX.sh [out_dir]
set -euo pipefail
O="${1:-$(dirname "$0")}"; RAW="$O/raw"; mkdir -p "$O" "$RAW"
: "${ELEVENLABS_API_KEY:?set ELEVENLABS_API_KEY}"

gen(){  # name, prompt, duration_seconds (0.5..30), prompt_influence
  curl -sS -o "$RAW/$1.mp3" -w "$1 %{http_code}\n" -X POST https://api.elevenlabs.io/v1/sound-generation \
    -H "xi-api-key: $ELEVENLABS_API_KEY" -H "Content-Type: application/json" \
    -d "{\"text\":\"$2\",\"duration_seconds\":$3,\"prompt_influence\":$4}"
}

# --- 2026-10-26 04:43 (prompt_influence 0.65) -> pop.wav, typing.wav ---
gen pop_a  "single soft bubble pop, short, clean, warm, UI sound, no music" 0.5 0.65
gen type_a "soft quiet keyboard typing, a few gentle key clicks, close mic, no music" 1.2 0.65
# --- 2026-10-26 04:08 (prompt_influence 0.6) -> paper_place.wav (used by the old "fold" storyboard look) ---
gen paper_b "newspaper clipping being placed down, light paper rustle and soft tap, no music" 1.0 0.6
# --- 2026-10-27 18:53 (prompt_influence 0.6) -> scroll_open.wav / scroll_close.wav (roll / rollL / rollR looks) ---
gen scroll_open  "Old parchment scroll being unrolled quickly, dry crisp paper rustle and crinkle, close-up foley, no music, no voice" 1.3 0.6
gen scroll_close "Old parchment scroll being rolled up and closed, dry paper rustling and crinkling, close-up foley, no music, no voice" 1.3 0.6

# Trim leading/trailing silence, high-pass, tiny fades, 48 kHz stereo, normalise peak to -3 dBFS.
p(){  # raw_name out_name extra_filter fade_in fade_tail
  ffmpeg -v error -y -i "$RAW/$1.mp3" -af "silenceremove=start_periods=1:start_threshold=-50dB,$3,afade=t=in:d=$4,areverse,silenceremove=start_periods=1:start_threshold=-55dB,afade=t=in:d=$5,areverse,aresample=48000" -ac 2 "$O/tmp.wav"
  pk=$(ffmpeg -v error -i "$O/tmp.wav" -af "astats=metadata=1:reset=0,ametadata=print:key=lavfi.astats.Overall.Peak_level:file=-" -f null - 2>/dev/null | tail -1 | sed 's/.*=//')
  g=$(python3 -c "print(-3-($pk))")
  ffmpeg -v error -y -i "$O/tmp.wav" -af "volume=${g}dB" -c:a pcm_s16le "$O/$2.wav"; rm -f "$O/tmp.wav"
}
p pop_a   pop         "highpass=f=120" 0.004 0.06
p type_a  typing      "highpass=f=200" 0.004 0.06
p paper_b paper_place "highpass=f=120" 0.005 0.08

# Scroll sounds (final version, 2026-10-27 18:53:43): high-pass, fades, fixed gain.
ffmpeg -v error -y -i "$RAW/scroll_open.mp3"  -af "highpass=f=150,afade=t=in:d=0.02,afade=t=out:st=1.05:d=0.25,volume=5.6dB" -ar 48000 -ac 2 "$O/scroll_open.wav"
ffmpeg -v error -y -i "$RAW/scroll_close.mp3" -af "highpass=f=150,afade=t=in:d=0.02,afade=t=out:st=1.05:d=0.25,volume=4.8dB" -ar 48000 -ac 2 "$O/scroll_close.wav"

# typing_peaks.json: times (s) of the individual key clicks inside typing.wav (2026-10-26 05:08).
# build_v8.py / chips_sfx.py cut one 70 ms click starting 6 ms before each peak.
python3 - "$O" <<'EOF'
import json, subprocess, sys, numpy as np
O = sys.argv[1]; sr = 48000
a = np.frombuffer(subprocess.check_output(["ffmpeg", "-v", "error", "-i", f"{O}/typing.wav", "-ac", "1", "-f", "f32le", "-"]), np.float32)
env = np.convolve(np.abs(a), np.ones(96) / 96, "same"); thr = env.max() * 0.35; peaks = []; i = 0
while i < len(env):
    if env[i] > thr: j = i + int(np.argmax(env[i:i + 1200])); peaks.append(j); i = j + 3000
    else: i += 1
json.dump([p / sr for p in peaks], open(f"{O}/typing_peaks.json", "w")); print("click peaks:", [round(p / sr, 3) for p in peaks])
EOF
echo "done -> $O (copy scroll_*.wav and paper_place.wav to <scratchpad>/kit2/sfx/ for build_v8.py)"
