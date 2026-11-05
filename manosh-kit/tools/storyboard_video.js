// Storyboard video base (voice-only version): illustrations on paper over a burgundy backdrop,
// slow drift on each, soft cross-dissolve between scenes. Captions/chips/voice are added by build_v8.py.
// Usage: node storyboard_video.js <scenes.json> <img_dir> <out_dir> <dur> [scale] [fps]
// scenes.json: [{"start","end","img"}]  (consecutive; each scene's image is a paper_scene.py PNG)
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [scenesPath, imgDir, outDir, durArg, scaleArg, fpsArg] = process.argv.slice(2);
const scenes = JSON.parse(fs.readFileSync(scenesPath, 'utf8'));
const extra = [];
const dur = Number(durArg), scale = Number(scaleArg || 1), fps = Number(fpsArg || 30), XF = .6;
const body = scenes.map((s, i) => {
  const a = Math.max(0, s.start - (i ? XF / 2 : 0)), b = s.end + XF / 2, d = b - a, dir = i % 2 ? -1 : 1;
  return `<img src="file://${path.resolve(imgDir, s.img)}" style="--dx:${dir * 18}px;animation:fade ${d.toFixed(3)}s linear ${a.toFixed(3)}s both,drift ${d.toFixed(3)}s linear ${a.toFixed(3)}s both;--fi:${((i ? XF : .5) / d * 100).toFixed(2)}%;--fo:${(100 - XF / d * 100).toFixed(2)}%">`;
}).join('\n');
const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><style>
 body{margin:0;width:1080px;height:1920px;overflow:hidden;
   background:radial-gradient(ellipse 85% 55% at 50% 33%,#5d2a3b 0%,#4C2130 58%,#36161f 100%);}
 img{position:absolute;left:40px;top:300px;width:1000px;opacity:0;transform-origin:50% 50%;}
 @keyframes fade{0%{opacity:0}var(--fi){opacity:1}}
 @keyframes drift{from{transform:scale(1.0) translateX(0)}to{transform:scale(1.06) translateX(var(--dx))}}
</style></head><body>${body}</body></html>`;
(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  // CSS vars can't drive keyframe offsets, so expand per-scene fade keyframes inline
  let h = html, k = 0;
  h = h.replace(/animation:fade ([\d.]+)s linear ([\d.]+)s both,drift ([\d.]+)s linear ([\d.]+)s both;--fi:([\d.]+)%;--fo:([\d.]+)%/g,
    (m, d, a, d2, a2, fi, fo) => { const n = `f${k++}`; h += ''; extra.push(`@keyframes ${n}{0%{opacity:0}${fi}%{opacity:1}${fo}%{opacity:1}100%{opacity:0}}`);
      return `animation:${n} ${d}s linear ${a}s both,drift ${d2}s linear ${a2}s both`; });
  h = h.replace('</style>', extra.join('\n') + '</style>');
  const hp = path.join(outDir, 'sb.html'); fs.writeFileSync(hp, h);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: scale });
  await page.goto('file://' + path.resolve(hp)); await page.waitForFunction(() => [...document.images].every(i => i.complete));
  const n = Math.round(dur * fps);
  for (let f = 0; f < n; f++) {
    await page.evaluate(ms => document.getAnimations().forEach(a => { a.pause(); a.currentTime = ms; }), f / fps * 1000);
    await page.screenshot({ path: path.join(outDir, `f_${String(f).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 92 });
  }
  await browser.close(); console.log('storyboard frames', n);
})();
