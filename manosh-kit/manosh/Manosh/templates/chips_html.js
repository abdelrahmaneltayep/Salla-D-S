// Word-chip captions (LOCKED caption + hook style, 2026-10-26) -> transparent PNG frame sequence.
// Each spoken word pops in as a rounded cream chip (burgundy Nunito Sans) at its spoken time;
// KEY words become italic Cormorant chips in cream text on burgundy / gold (alternating).
// Arabic words (and ﷺ) switch to Amiri. Chips sit centred at chest height; one line-group per page.
// Usage: node chips_html.js <words.json> <out_dir> [scale=1] [fps=30] [dur] [theme=light|dark]
// theme dark: on dark backdrops (storyboard video) burgundy key chips get a cream outline.
//   scale 2 + fps 60 for the 4K60 master (frames are 2160x3840).
// words.json: [{"start":s,"end":e,"words":[["and",t],["dressed",t,true],...]}, ...]   (true = key word)
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [pagesPath, outDir, scaleArg, fpsArg, durArg, themeArg] = process.argv.slice(2);
const pages = JSON.parse(fs.readFileSync(pagesPath, 'utf8'));
const scale = Number(scaleArg || 1), fps = Number(fpsArg || 30), dur = Number(durArg || pages.at(-1).end + .2);
const css = 'file://' + path.resolve(__dirname, 'brand.css');
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const AR = /[\u0600-\u06FF\uFB50-\uFDFF\uFE70-\uFEFF]/;   // Arabic incl. ligatures such as ﷺ
let nk = 0;
const chip = ([w, t, key]) => {
  const cls = key ? (nk++ % 2 ? 'chip kc g' : 'chip kc') : 'chip';
  return `<span class="${cls}${AR.test(w) ? ' ar' : ''}" style="animation:chip .16s cubic-bezier(.34,1.56,.64,1) ${t}s both">${esc(w)}</span>`;
};
const body = pages.map(p => `<div class="pg" style="animation:show ${(p.end - p.start).toFixed(3)}s linear ${p.start}s forwards">
  <div class="chips">${p.words.map(chip).join('')}</div></div>`).join('\n');
const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="${css}"><style>
 body{width:1080px;height:1920px;margin:0;position:relative;overflow:hidden;}
 .pg{position:absolute;inset:0;opacity:0;}
 .chips{position:absolute;left:70px;right:70px;top:1170px;display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:10px;}
 .chip{font:800 62px/1 'Nunito Sans';color:var(--burgundy);background:var(--cream);padding:9px 18px 12px;border-radius:16px;
   box-shadow:0 4px 14px rgba(76,33,48,.22);}
 .chip.kc{font:italic 700 78px/0.9 'Cormorant Garamond';color:var(--cream);background:var(--burgundy);padding:8px 20px 12px;}
 .chip.kc.g{background:var(--gold);text-shadow:0 2px 0 rgba(76,33,48,.3);}
 .chip.ar{font:700 60px/1.25 'Amiri';padding:0 18px 6px;} .chip.kc.ar{font:700 66px/1.25 'Amiri';padding:2px 22px 8px;}
 ${themeArg === 'dark' ? `.chip.kc{box-shadow:0 0 0 3px var(--cream),0 4px 14px rgba(0,0,0,.35);}` : ''}
 @keyframes show{0%{opacity:1}99.5%{opacity:1}100%{opacity:0}}
 @keyframes chip{from{opacity:0;transform:scale(.8)}to{opacity:1;transform:none}}
</style></head><body>${body}</body></html>`;
(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const hp = path.join(outDir, 'chips.html'); fs.writeFileSync(hp, html);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: scale });
  await page.goto('file://' + path.resolve(hp)); await page.evaluate(() => document.fonts.ready);
  const n = Math.round(dur * fps);
  for (let f = 0; f <= n; f++) {   // deterministic: seek every CSS animation to the frame time
    await page.evaluate(ms => document.getAnimations().forEach(a => { a.pause(); a.currentTime = ms; }), f / fps * 1000);
    await page.screenshot({ path: path.join(outDir, `f_${String(f).padStart(4, '0')}.png`), omitBackground: true });
  }
  await browser.close(); console.log('chips', n + 1, 'frames');
})();
