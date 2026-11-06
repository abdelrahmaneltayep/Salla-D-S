# Tone down red/burgundy watercolour patches that could read as blood (e.g. stains on a wall next to a fight).
# Works on a PNG or an MP4 (frame by frame). Shifts red hues to the wall's ochre and lowers their saturation.
# Usage: python3 tone_down_red.py <in.png|in.mp4> <out.png|out.mp4>
# Only use it on scenes where no burgundy clothing should stay red (it recolours ALL saturated reds).
import subprocess, sys
import numpy as np
from PIL import Image

src, dst = sys.argv[1:3]


def fix(im):
    hsv = np.array(im.convert("HSV")).astype(float)
    h, s = hsv[..., 0] * 360 / 255, hsv[..., 1] / 255
    m = ((h < 20) | (h > 320)) & (s > 0.18)
    hsv[..., 0] = np.where(m, 36 * 255 / 360, hsv[..., 0])
    hsv[..., 1] = np.where(m, hsv[..., 1] * 0.55, hsv[..., 1])
    hsv[..., 2] = np.where(m, np.minimum(255, hsv[..., 2] * 1.08), hsv[..., 2])
    return Image.fromarray(hsv.astype("uint8"), "HSV").convert("RGB")


if src.lower().endswith(".png"):
    fix(Image.open(src).convert("RGB")).save(dst)
    sys.exit(0)
probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height,r_frame_rate",
                        "-of", "csv=p=0", src], capture_output=True, text=True).stdout.strip().split(",")
W, H, R = int(probe[0]), int(probe[1]), probe[2]
dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", src, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", R, "-i", "-",
                        "-c:v", "libx264", "-crf", "14", "-preset", "medium", "-pix_fmt", "yuv420p", dst], stdin=subprocess.PIPE)
while True:
    b = dec.stdout.read(W * H * 3)
    if len(b) < W * H * 3:
        break
    enc.stdin.write(fix(Image.frombytes("RGB", (W, H), b)).tobytes())
enc.stdin.close(); enc.wait()
