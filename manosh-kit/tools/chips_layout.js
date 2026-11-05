// Word-chip hook, little bounce, chips placed in different layouts (not side by side).
// Usage: node chips_layout.js <layout 1-5> <words.json> <out_dir> [scale] [fps] [dur]
// 1 column · 2 staircase · 3 zigzag · 4 sticker scatter (tilted) · 5 rising stack (new word at the bottom pushes the rest up)
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [lArg, pagesPath, outDir, scaleArg, fpsArg, durArg] = process.argv.slice(2);
const L = Number(lArg), pages = JSON.parse(fs.readFileSync(pagesPath, 'utf8'));
const scale = Number(scaleArg || 1), fps = Number(fpsArg || 30), dur = Number(durArg || pages.at(-1).end + .2);
const css = 'file://' + path.resolve(__dirname, '../manosh/Manosh/templates/brand.css');
const AR = /[؀-ۿﭐ-﷿ﹰ-﻿]/;
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
const STEP = 96;                                   // vertical spacing between chips
const SCATTER = [[310, 1010, -5], [770, 1090, 4], [360, 1250, 3], [740, 1350, -4]];
let kfs = '', id = 0, nk = 0;
const place = (j, n) => {                          // centre x, top y, tilt (deg)
  if (L == 1) return [540, 1050 + j * STEP, 0];
  if (L == 2) return [330 + j * 140, 1040 + j * STEP, 0];
  if (L == 3) return [j % 2 ? 710 : 370, 1040 + j * STEP, 0];
  if (L == 4) return SCATTER[j % 4];
  return [540, 1360, 0];                           // 5: all start at the bottom slot
};
const chip = (w, t, key, p, j) => {
  const n = p.words.length, [x, y, r] = place(j, n);
  const cls = (key ? (nk++ % 2 ? 'chip kc g' : 'chip kc') : 'chip') + (AR.test(w) ? ' ar' : '');
  let move = '';
  if (L == 5) {                                    // each later word pushes this chip up one slot
    const later = p.words.slice(j + 1).map(q => q[1] - t);
    if (later.length) {
      const name = `m${id++}`, D = later.at(-1) + .22;
      const pts = [[0, 0]]; later.forEach((u, k) => pts.push([u, -k * STEP], [u + .22, -(k + 1) * STEP]));
      kfs += `@keyframes ${name}{` + pts.map(([tt, dy]) => `${(tt / D * 100).toFixed(3)}%{transform:translateY(${dy}px);animation-timing-function:cubic-bezier(.22,1,.36,1)}`).join('') + '}\n';
      move = `animation:${name} ${D.toFixed(3)}s linear ${t}s both;`;
    }
  }
  return `<span class="slot" style="left:${x}px;top:${y}px;${move}"><span class="tilt" style="transform:rotate(${r}deg)">` +
         `<span class="${cls}" style="animation:lb .34s linear ${t}s both">${esc(w)}</span></span></span>`;
};
const body = pages.map(p => `<div class="pg" style="animation:show ${(p.end - p.start).toFixed(3)}s linear ${p.start}s forwards">
  ${p.words.map(([w, t, key], j) => chip(w, t, key, p, j)).join('')}</div>`).join('\n');
const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="${css}"><style>
 body{width:1080px;height:1920px;margin:0;position:relative;overflow:hidden;}
 .pg{position:absolute;inset:0;opacity:0;}
 .slot{position:absolute;width:0;height:0;} .tilt{position:absolute;left:0;top:0;transform-origin:0 0;}
 .chip{position:absolute;left:0;top:0;translate:-50% 0;white-space:nowrap;display:inline-block;font:800 62px/1 'Nunito Sans';color:var(--burgundy);
   background:var(--cream);padding:9px 18px 12px;border-radius:16px;box-shadow:0 4px 14px rgba(76,33,48,.22);transform-origin:50% 60%;}
 .chip.kc{font:italic 700 78px/0.9 'Cormorant Garamond';color:var(--cream);background:var(--burgundy);padding:8px 20px 12px;}
 .chip.kc.g{background:var(--gold);text-shadow:0 2px 0 rgba(76,33,48,.3);}
 .chip.ar{font:700 60px/1.25 'Amiri';padding:0 18px 6px;} .chip.kc.ar{font:700 66px/1.25 'Amiri';padding:2px 22px 8px;}
 @keyframes show{0%{opacity:1}99.5%{opacity:1}100%{opacity:0}}
 /* little bounce: small overshoot only */
 @keyframes lb{0%{opacity:0;transform:translateY(14px) scale(.82);animation-timing-function:cubic-bezier(.22,1,.36,1)}
   55%{opacity:1;transform:scale(1.06);animation-timing-function:ease-in-out}78%{transform:scale(.98)}100%{transform:none}}
 ${kfs}
</style></head><body>${body}</body></html>`;
(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const hp = path.join(outDir, 'chips.html'); fs.writeFileSync(hp, html);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: scale });
  await page.goto('file://' + path.resolve(hp)); await page.evaluate(() => document.fonts.ready);
  const n = Math.round(dur * fps);
  for (let f = 0; f <= n; f++) {
    await page.evaluate(ms => document.getAnimations().forEach(a => { a.pause(); a.currentTime = ms; }), f / fps * 1000);
    await page.screenshot({ path: path.join(outDir, `f_${String(f).padStart(4, '0')}.png`), omitBackground: true });
  }
  await browser.close(); console.log('layout', L, n + 1, 'frames');
})();
