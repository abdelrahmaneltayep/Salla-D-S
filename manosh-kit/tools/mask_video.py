# Person matte for a whole video: reads frames from ffmpeg, writes a grey matte video (white = person).
# Usage: mask_video.py <in.mp4> <out_matte.mkv> <model.tflite>
import sys, subprocess, numpy as np
from PIL import Image, ImageFilter
from ai_edge_litert.interpreter import Interpreter
src, out, model = sys.argv[1:4]; W, H = 1080, 1920
it = Interpreter(model_path=model); it.allocate_tensors()
ii, oi = it.get_input_details()[0]["index"], it.get_output_details()[0]["index"]
rd = subprocess.Popen(["ffmpeg", "-v", "error", "-i", src, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
wr = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "gray", "-s", f"{W}x{H}", "-r", "30", "-i", "-",
                       "-c:v", "ffv1", "-pix_fmt", "gray", out], stdin=subprocess.PIPE)
prev = None; n = 0
while True:
    buf = rd.stdout.read(W * H * 3)
    if len(buf) < W * H * 3: break
    im = Image.frombuffer("RGB", (W, H), buf)
    x = np.asarray(im.resize((256, 256), Image.BILINEAR), np.float32)[None] / 255.0
    it.set_tensor(ii, x); it.invoke(); y = it.get_tensor(oi)[0]
    if y.min() < 0 or y.max() > 1.001 or abs(y.sum(-1).mean() - 1) > 0.05:
        e = np.exp(y - y.max(-1, keepdims=True)); y = e / e.sum(-1, keepdims=True)
    person = 1.0 - y[..., 0]
    if prev is not None and np.abs(person - prev).mean() < .08: person = .6 * person + .4 * prev   # smooth, but not across cuts
    prev = person
    a = np.clip((person - .25) / .5, 0, 1)
    m = Image.fromarray((a * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(2))
    wr.stdin.write(m.tobytes()); n += 1
wr.stdin.close(); wr.wait(); print("matte frames", n)
