# Storyboard drawing on a real parchment sheet (reference scan), horizontal, background removed,
# sepia ink sinking into the paper, faint tri-fold creases. Output: transparent RGBA PNG.
# Usage: python3 paper_scene.py <paper_scan> <drawing.png|blank> <out.png> [flip: none|h|v|hv] [tint]   ('blank' = paper back)
# [darken] multiplies the paper (e.g. 0.9 = a little darker beige). A red wax seal on the paper is kept on top of the ink.
# tint: sepia (default) | soft (light colour) | wash (watercolour) | select (only gold + burgundy in colour)
#       | orig (original colours of the drawing, 2026-11-05) | kit (tritone: burgundy -> terracotta -> cream) | illum (dark ink + gold-leaf accents, like a manuscript)
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps
paper_p, draw_p, out = sys.argv[1:4]; flip = sys.argv[4] if len(sys.argv) > 4 else "none"
tint = sys.argv[5] if len(sys.argv) > 5 else "sepia"
darken = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0   # <1 = deeper beige paper
tone = sys.argv[7] if len(sys.argv) > 7 else None          # e.g. D2C0AC: recolour the paper so its median becomes this colour (texture kept)
W, H = 1500, 930

def blur(a, r):
    return np.asarray(Image.fromarray(np.clip(a * 255, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(r)), np.float32) / 255

# --- paper: landscape, white studio background flood-filled away from the borders ------------------------
pap = Image.open(paper_p).convert("RGB").rotate(90, expand=True)
if "h" in flip: pap = ImageOps.mirror(pap)
if "v" in flip: pap = ImageOps.flip(pap)
a = np.asarray(pap, np.int16)
white = ((a.min(-1) > 236) * 255).astype(np.uint8)
m = Image.fromarray(white, "L").copy(); w0, h0 = m.size   # copy: floodfill needs a writable image
for seed in [(0, 0), (w0 - 1, 0), (0, h0 - 1), (w0 - 1, h0 - 1), (w0 // 2, 0), (w0 // 2, h0 - 1), (0, h0 // 2), (w0 - 1, h0 // 2)]:
    if m.getpixel(seed) == 255: ImageDraw.floodfill(m, seed, 128)
bg = (np.asarray(m) == 128).astype(np.float32)
alpha = 1 - bg
pap = pap.resize((W, H), Image.LANCZOS)
alpha = np.asarray(Image.fromarray((alpha * 255).astype(np.uint8)).resize((W, H), Image.LANCZOS), np.float32) / 255
alpha = blur(np.clip((alpha - .35) / .4, 0, 1), .8)                    # clean, slightly soft torn edge
P = np.asarray(pap, np.float32) / 255
if tone:
    tgt = np.array([int(tone[i:i + 2], 16) for i in (0, 2, 4)], np.float32) / 255
    med = np.median(P[alpha > .9], axis=0)
    P = np.clip(P * (tgt / np.maximum(med, 1e-3)), 0, 1)
P = P * darken
# --- drawing as sepia ink, multiplied into the paper, fading out before the torn edge ---------------------
dr = Image.new("RGB", (64, 64), "white") if draw_p == "blank" else Image.open(draw_p).convert("RGB")
iw, ih = int(W * .80), int(H * .76)
d = np.asarray(dr.resize((iw, ih), Image.LANCZOS), np.float32) / 255
if tint != "sepia":                              # white-balance: the drawing's own paper -> neutral white
    d = np.clip(d / np.percentile(d, 97, axis=(0, 1)), 0, 1)
lum = d @ np.array([.3, .59, .11], np.float32)
sep = np.stack([lum ** .92, lum ** 1.02, lum ** 1.22], -1)

def sat(x, k):                                   # scale saturation around luminance
    l = (x @ np.array([.3, .59, .11], np.float32))[..., None]
    return np.clip(l + (x - l) * k, 0, 1)

def hue_mask(x):                                 # gold and burgundy/red areas of the original wash
    mx, mn = x.max(-1), x.min(-1); c = mx - mn + 1e-6
    r, g, b = x[..., 0], x[..., 1], x[..., 2]
    h = np.where(mx == r, ((g - b) / c) % 6, np.where(mx == g, (b - r) / c + 2, (r - g) / c + 4)) * 60
    sv = c / (mx + 1e-6)
    gold = (h > 25) & (h < 62) & (sv > .18); red = ((h > 320) | (h < 22)) & (sv > .14)
    return gold, red

if tint == "sepia":  d = .3 * d + .7 * sep
elif tint == "soft": d = sat(.6 * d + .4 * sep, 1.3)
elif tint == "wash": d = sat(.9 * d + .1 * sep, 1.55)
elif tint == "orig": d = sat(d, 1.2)                 # original colours (storyboard art style), as generated
elif tint == "kit":                              # gradient map in the Manosh palette
    stops = np.array([[.18, .07, .11], [.30, .13, .19], [.79, .49, .35], [.95, .93, .87], [1, 1, 1]], np.float32)
    pos = np.array([0, .22, .55, .85, 1], np.float32)
    d = np.stack([np.interp(lum, pos, stops[:, c]) for c in range(3)], -1)
elif tint == "illum":                            # iron-gall ink, gold leaf where the wash was gold
    gold, _ = hue_mask(d)
    m = np.asarray(Image.fromarray((gold * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2.5)), np.float32)[..., None] / 255
    ink = 1 - (1 - lum[..., None]) * (1 - np.array([.16, .12, .10], np.float32))
    goldleaf = np.clip(np.array([.86, .66, .28], np.float32) * (.55 + .6 * lum[..., None]), 0, 1)
    m = m * .8                                   # keep the gold a touch softer
    d = ink * (1 - m) + goldleaf * m
elif tint == "select":
    gold, red = hue_mask(d)
    m = np.asarray(Image.fromarray(((gold | red) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2.5)), np.float32)[..., None] / 255
    d = sep * (1 - m) + sat(d, 1.5) * m
if tint == "orig":                               # keep the warm sky/sand washes: only near-white paper -> white
    d = np.clip(d / np.percentile(d, 99.5, axis=(0, 1)), 0, 1) ** 1.15
else:
    d = (np.clip(d / np.percentile(d, 97, axis=(0, 1)), 0, 1) if tint == "sepia"
         else np.clip(d / np.percentile(d, 88, axis=(0, 1)), 0, 1)) ** 1.35   # drawing paper -> pure white, ink contrast kept
if tint not in ("sepia", "orig"):   # grey (hue-neutral) hatching so it takes the paper's own colour; keep colour only where the drawing has it
    lumd = (d @ np.array([.3, .59, .11], np.float32))[..., None]
    chroma = np.clip((d.max(-1) - d.min(-1))[..., None] * 5 - .15, 0, 1)
    d = lumd * (1 - chroma) + d * chroma
ink = np.ones((H, W, 3), np.float32); oy, ox = (H - ih) // 2, (W - iw) // 2
ink[oy:oy + ih, ox:ox + iw] = d
fade = np.zeros((H, W), np.float32); fade[oy + 70:oy + ih - 70, ox + 70:ox + iw - 70] = 1
fade = blur(fade, 70)
ink = 1 - (1 - ink) * (fade[..., None] * .92)
img = P * ink
# --- keep a red wax seal (if the paper has one) above the ink -------------------------------------------------
r_, g_, b_ = P[..., 0] / max(darken, 1e-3), P[..., 1] / max(darken, 1e-3), P[..., 2] / max(darken, 1e-3)
seal = ((r_ > .42) & (g_ < .33) & (b_ < .33) & (r_ - g_ > .22)).astype(np.float32)
if seal.mean() > .0005:
    seal = blur(np.asarray(Image.fromarray((seal * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(7)), np.float32) / 255, 2)
    img = img * (1 - seal[..., None]) + (P / max(darken, 1e-3)) * seal[..., None]
# --- faint tri-fold creases (the sheet was folded in thirds) -------------------------------------------------
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
for cx in (W / 3, 2 * W / 3):
    dline = xx - cx
    img *= (1 - .10 * np.exp(-(dline / 2.2) ** 2))[..., None]              # crease shadow
    img = np.minimum(1, img * (1 + .06 * np.exp(-((dline - 4) / 3) ** 2))[..., None])  # highlight beside it
rgba = np.dstack([np.clip(img, 0, 1), alpha]) * 255
Image.fromarray(rgba.astype(np.uint8), "RGBA").save(out)
print("paper scene ->", out)
