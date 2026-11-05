# Turn a storyboard panel into a drawing on old paper: aged parchment, sepia ink, drawing fading into the
# paper margin, torn/deckled transparent edges with a darkened (burnt) rim. No frame, no label.
# Usage: python3 parchment.py <in.png> <out.png> [seed]
import sys
import numpy as np
from PIL import Image, ImageFilter
src, out = sys.argv[1:3]; seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
rng = np.random.default_rng(seed)
W, H = 1400, 772

def fbm(octaves, base):
    acc = np.zeros((H, W), np.float32); amp, tot = 1.0, 0.0
    for o in range(octaves):
        n = base * 2 ** o
        g = rng.random((max(2, n * H // W), n)).astype(np.float32)
        acc += amp * np.asarray(Image.fromarray((g * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC), np.float32) / 255
        tot += amp; amp *= .5
    return acc / tot

def blur(a, r):
    return np.asarray(Image.fromarray(np.clip(a * 255, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(r)), np.float32) / 255

yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
u, v = (xx / W - .5) * 2, (yy / H - .5) * 2
# --- parchment -----------------------------------------------------------------------------------------
blot = fbm(5, 3)                                     # large uneven toning
fib = rng.normal(0, 1, (H, W)).astype(np.float32)    # paper fibre grain
fib = blur((fib * .5 + .5).clip(0, 1), .8) - .5
edge_dark = np.clip((np.maximum(np.abs(u) ** 3, np.abs(v) ** 3)), 0, 1)
paper = np.stack([np.full((H, W), c, np.float32) for c in (231, 212, 172)], -1) / 255
tone = 1 - .16 * (blot - .5) * 2 - .22 * edge_dark - .05 * fib
paper *= tone[..., None]
for _ in range(5):                                   # faint stains
    cx, cy, r = rng.uniform(.1, .9) * W, rng.uniform(.1, .9) * H, rng.uniform(40, 140)
    ring = np.exp(-((np.hypot(xx - cx, yy - cy) - r) / (r * .08)) ** 2) * .07
    paper *= (1 - ring[..., None] * np.array([.6, .9, 1.3]))
# --- drawing as sepia ink, fading into the paper margin -----------------------------------------------------
im = Image.open(src).convert("RGB").resize((int(W * .9), int(H * .9)), Image.LANCZOS)
d = np.asarray(im, np.float32) / 255
lum = d @ np.array([.3, .59, .11], np.float32)
sep = np.stack([lum ** .95, lum ** 1.05, lum ** 1.25], -1)           # sepia toning
d = .35 * d + .65 * sep                                              # keep a trace of the burgundy/gold washes
d = d / np.maximum(d.max(axis=(0, 1)), 1e-3) * 1.0
canvas = np.ones((H, W, 3), np.float32); oy, ox = (H - d.shape[0]) // 2, (W - d.shape[1]) // 2
canvas[oy:oy + d.shape[0], ox:ox + d.shape[1]] = d
fade = np.zeros((H, W), np.float32); fade[oy:oy + d.shape[0], ox:ox + d.shape[1]] = 1
fade = blur(fade, 26) * (1 - .25 * fbm(3, 4))                        # soft, uneven vignette into the paper
ink = 1 - (1 - canvas) * fade[..., None]
img = paper * ink                                                    # multiply: ink sits in the paper
# --- torn / deckled edge with burnt rim ----------------------------------------------------------------------
n1, n2 = fbm(6, 6), fbm(4, 24)
dist = 1 - np.maximum(np.abs(u) ** 8 + 0 * v, np.abs(v) ** 8)        # 1 inside, 0 at border
dist = np.minimum(1 - np.abs(u) ** 1, 1 - np.abs(v) ** 1)            # linear distance to nearest side
edge = dist - .035 - .05 * (n1 - .5) - .025 * (n2 - .5)
alpha = np.clip(edge / .006, 0, 1)
burn = np.clip(1 - edge / .05, 0, 1) * alpha
img *= (1 - .45 * burn[..., None] * np.array([.8, 1, 1.15]))
alpha = blur(alpha, .7)
rgba = np.dstack([np.clip(img, 0, 1), alpha]) * 255
Image.fromarray(rgba.astype(np.uint8), "RGBA").save(out)
print("parchment ->", out)
