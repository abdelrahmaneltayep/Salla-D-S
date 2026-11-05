# Full-frame vertical storyboard: drawing (kit tritone) sunk into a full-bleed paper texture, 1080x1920 (x scale).
# Usage: python3 paper_full.py <paper_scan> <drawing.png> <out.png> [tone=C2AE98] [scale=1]
import sys
import numpy as np
from PIL import Image, ImageFilter
paper_p, draw_p, out = sys.argv[1:4]
tone = sys.argv[4] if len(sys.argv) > 4 else "C2AE98"; S = float(sys.argv[5]) if len(sys.argv) > 5 else 1
W, H = int(1080 * S), int(1920 * S)

def cover(im, w, h):
    r = max(w / im.width, h / im.height); im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))

def blur(a, r):
    return np.asarray(Image.fromarray(np.clip(a * 255, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(r)), np.float32) / 255

P = np.asarray(cover(Image.open(paper_p).convert("RGB"), W, H), np.float32) / 255
tgt = np.array([int(tone[i:i + 2], 16) for i in (0, 2, 4)], np.float32) / 255
P = np.clip(P * (tgt / np.median(P.reshape(-1, 3), axis=0)), 0, 1) * .97
d = np.asarray(cover(Image.open(draw_p).convert("RGB"), W, H), np.float32) / 255
d = np.clip(d / np.percentile(d, 97, axis=(0, 1)), 0, 1)
lum = d @ np.array([.3, .59, .11], np.float32)
stops = np.array([[.18, .07, .11], [.30, .13, .19], [.79, .49, .35], [.95, .93, .87], [1, 1, 1]], np.float32)
pos = np.array([0, .22, .55, .85, 1], np.float32)
d = np.stack([np.interp(lum, pos, stops[:, c]) for c in range(3)], -1)          # kit tritone
d = np.clip(d / np.percentile(d, 88, axis=(0, 1)), 0, 1) ** 1.35
l2 = (d @ np.array([.3, .59, .11], np.float32))[..., None]
ch = np.clip((d.max(-1) - d.min(-1))[..., None] * 5 - .15, 0, 1); d = l2 * (1 - ch) + d * ch
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
m = int(30 * S); fade = np.zeros((H, W), np.float32); fade[m:H - m, m:W - m] = 1; fade = blur(fade, 40 * S)
img = P * (1 - (1 - d) * (fade[..., None] * .92))
vig = 1 - .22 * np.clip(((xx / W - .5) ** 2 * 2.2 + (yy / H - .5) ** 2 * 1.6), 0, 1)   # gentle aged vignette
Image.fromarray((np.clip(img * vig[..., None], 0, 1) * 255).astype(np.uint8)).save(out)
print("full-frame storyboard ->", out)
