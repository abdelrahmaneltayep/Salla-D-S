# Cut the person out of each frame (RGBA, transparent background) using the
# MediaPipe selfie_multiclass_256x256 model on the LiteRT runtime.
# Usage: person_mask.py <frames_dir> <out_dir> <model>
import sys, os, glob, numpy as np
from PIL import Image, ImageFilter
from ai_edge_litert.interpreter import Interpreter
src, out, model = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
it = Interpreter(model_path=model); it.allocate_tensors()
ii, oi = it.get_input_details()[0]["index"], it.get_output_details()[0]["index"]
prev = None
for p in sorted(glob.glob(f"{src}/*.png")):
    im = Image.open(p).convert("RGB")
    x = np.asarray(im.resize((256, 256), Image.BILINEAR), np.float32)[None] / 255.0
    it.set_tensor(ii, x); it.invoke()
    y = it.get_tensor(oi)[0]
    if y.min() < 0 or y.max() > 1.001 or abs(y.sum(-1).mean() - 1) > 0.05:   # logits -> softmax
        e = np.exp(y - y.max(-1, keepdims=True)); y = e / e.sum(-1, keepdims=True)
    person = 1.0 - y[..., 0]
    if prev is not None:
        person = 0.6 * person + 0.4 * prev          # light temporal smoothing against flicker
    prev = person
    a = np.clip((person - 0.25) / 0.5, 0, 1)
    am = Image.fromarray((a * 255).astype(np.uint8)).resize(im.size, Image.BICUBIC).filter(ImageFilter.GaussianBlur(2))
    rgba = im.copy(); rgba.putalpha(am)
    rgba.save(f"{out}/{os.path.basename(p)}")
print("masked", len(glob.glob(f"{out}/*.png")))
