// Word-chip hook with 5 "bounce bigger/smaller" variants (Manosh kit chips look).
// Usage: node chips_bounce.js <mode 1-5> <words.json> <out_dir> [scale] [fps] [dur]
// 1 elastic pop · 2 jelly drop · 3 active word grows · 4 ripple on every new word · 5 breathing + big key word
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [modeArg, pagesPath, outDir, scaleArg, fpsArg, durArg] = process.argv.slice(2);
const mode = Number(modeArg), pages = JSON.parse(fs.readFileSync(pagesPath, 'utf8'));
const scale = Number(scaleArg || 1), fps = Number(fpsArg || 30), dur = Number(durArg || pages.at(-1).end + .2);
const css = 'file://' + path.resolve(__dirname, '../manosh/Manosh/templates/brand.css');
const AR = /[؀-ۿﭐ-﷿ﹰ-﻿]/;
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
const OUT = 'cubic-bezier(.22,1,.36,1)', INOUT = 'cubic-bezier(.45,0,.55,1)';
let kfs = '', id = 0, nk = 0;
// keyframes from [time(s), scale, opacity?] points; each segment eased
const kf = (pts, ease = INOUT) => {
  const name = `k${id++}`, D = pts.at(-1)[0] || .01;
  kfs += `@keyframes ${name}{` + pts.map(([t, s, o]) => `${(t / D * 100).toFixed(3)}%{transform:scale(${s});${o !== undefined ? `opacity:${o};` : ''}animation-timing-function:${ease}}`).join('') + '}\n';
  return [name, D];
};
const chip = (w, t, key, p, j) => {
  const ws = p.words, later = ws.slice(j + 1).map(x => x[1]);
  const cls = (key ? (nk++ % 2 ? 'chip kc g' : 'chip kc') : 'chip') + (AR.test(w) ? ' ar' : '');
  let a = '', b = '';                         // a = outer (bounce) animation, b = inner chip animation
  if (mode == 1) {
    const [n, D] = kf([[0, 0, 0], [.2, 1.28, 1], [.31, .88], [.42, 1.07], [.52, .97], [.6, 1]]);
    a = `animation:${n} ${D}s linear ${t}s both`;
  } else if (mode == 2) {
    a = `animation:jelly .55s linear ${t}s both`;
  } else if (mode == 3) {
    const nxt = later.length ? later[0] : Math.min(t + .8, p.end - .1);
    const h = Math.max(.2, nxt - t);
    const [n, D] = kf([[0, .6, 0], [.12, 1.22, 1], [h, 1.22], [h + .16, .94], [h + .26, 1]]);
    a = `animation:${n} ${D}s linear ${t}s both`;
  } else if (mode == 4) {
    const pts = [[0, .5, 0], [.16, 1.15, 1], [.3, .96], [.38, 1]];
    later.forEach(u => { const r = u - t; pts.push([r, 1], [r + .09, 1.13], [r + .2, .97], [r + .26, 1]); });
    const [n, D] = kf(pts);
    a = `animation:${n} ${D}s linear ${t}s both`;
  } else if (mode == 5) {
    const [n, D] = key ? kf([[0, 0, 0], [.22, 1.45, 1], [.36, .9], [.48, 1.08], [.58, 1]])
                       : kf([[0, .5, 0], [.14, 1.12, 1], [.24, 1]]);
    a = `animation:${n} ${D}s linear ${t}s both`;
    b = `animation:breathe .9s ${INOUT} ${(t + D).toFixed(3)}s infinite`;
  }
  return `<span class="wrap" style="${a}"><span class="${cls}" style="${b}">${esc(w)}</span></span>`;
};
const body = pages.map(p => `<div class="pg" style="animation:show ${(p.end - p.start).toFixed(3)}s linear ${p.start}s forwards">
  <div class="chips">${p.words.map(([w, t, key], j) => chip(w, t, key, p, j)).join('')}</div></div>`).join('\n');
const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="${css}"><style>
 body{width:1080px;height:1920px;margin:0;position:relative;overflow:hidden;}
 .pg{position:absolute;inset:0;opacity:0;}
 .chips{position:absolute;left:70px;right:70px;top:1170px;display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:10px;}
 .wrap{display:inline-block;transform-origin:50% 60%;}
 .chip{display:inline-block;font:800 62px/1 'Nunito Sans';color:var(--burgundy);background:var(--cream);padding:9px 18px 12px;border-radius:16px;
   box-shadow:0 4px 14px rgba(76,33,48,.22);}
 .chip.kc{font:italic 700 78px/0.9 'Cormorant Garamond';color:var(--cream);background:var(--burgundy);padding:8px 20px 12px;}
 .chip.kc.g{background:var(--gold);text-shadow:0 2px 0 rgba(76,33,48,.3);}
 .chip.ar{font:700 60px/1.25 'Amiri';padding:0 18px 6px;} .chip.kc.ar{font:700 66px/1.25 'Amiri';padding:2px 22px 8px;}
 @keyframes show{0%{opacity:1}99.5%{opacity:1}100%{opacity:0}}
 @keyframes jelly{0%{opacity:0;transform:translateY(-90px) scale(.85,1.15)}38%{opacity:1;transform:translateY(0) scale(1.28,.76)}
   58%{transform:scale(.9,1.12)}76%{transform:scale(1.07,.95)}90%{transform:scale(.98,1.02)}100%{transform:none}}
 @keyframes breathe{0%,100%{transform:scale(1)}50%{transform:scale(1.07)}}
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
  await browser.close(); console.log('mode', mode, n + 1, 'frames');
})();
