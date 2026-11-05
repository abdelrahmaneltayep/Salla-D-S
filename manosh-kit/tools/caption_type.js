// Giant typed captions (Manosh) -> transparent PNG frames.
// Each word types on letter by letter at its spoken time; pages swap at page boundaries.
// Usage: node caption_type.js <style A|B|C> <pages.json> <out_dir> [scale=1] [fps=30] [dur]
// pages.json: [{"start":s,"end":e,"words":[["FREE",t,keyword?],...]}, ...]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [style, pagesPath, outDir, scaleArg, fpsArg, durArg] = process.argv.slice(2);
const pages = JSON.parse(fs.readFileSync(pagesPath, 'utf8'));
const scale = Number(scaleArg || 1), fps = Number(fpsArg || 30);
const dur = Number(durArg || pages[pages.length - 1].end + .2);
const LETTER = 0.035;
const css = 'file://' + path.resolve(__dirname, '../manosh/Manosh/templates/brand.css');
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const ST = {
  // A: burgundy word blocks, keyword = burgundy on gold block
  A: `.w{background:var(--burgundy);color:var(--cream);padding:4px 22px 10px;border-radius:16px;}
      .w.k{background:var(--gold);color:var(--burgundy);}`,
  // B: cream letters, heavy burgundy outline + hard drop, keyword gold
  B: `.w{color:var(--cream);-webkit-text-stroke:14px var(--burgundy);paint-order:stroke fill;text-shadow:0 12px 0 var(--burgundy);letter-spacing:6px;margin:0 10px;}
      .w.k{color:var(--gold);}`,
  // C: burgundy letters on cream blocks, keyword cream on terracotta block
  C: `.w{background:var(--cream);color:var(--burgundy);padding:4px 22px 10px;border-radius:16px;}
      .w.k{background:var(--terracotta);color:var(--cream);}`,
}[style];
const body = pages.map(p => `<div class="pg" style="animation:show ${(p.end - p.start).toFixed(3)}s linear ${p.start}s forwards">` +
  p.words.map(([w, t, k]) => `<span class="w${k ? ' k' : ''}" style="animation:pop .18s cubic-bezier(.34,1.56,.64,1) ${t}s both"><span class="ty" style="animation:type ${(w.length * LETTER).toFixed(3)}s steps(${w.length}) ${t}s both">${esc(w)}</span></span>`).join(' ') +
  `</div>`).join('');
const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="${css}"><style>
 body{width:1080px;height:1920px;margin:0;position:relative;overflow:hidden;}
 .pg{position:absolute;top:1080px;left:40px;right:40px;display:flex;flex-wrap:wrap;justify-content:center;align-content:flex-start;gap:18px 20px;opacity:0;
   font-family:'Nunito Sans';font-weight:800;font-size:148px;line-height:1.04;letter-spacing:-1px;text-transform:uppercase;}
 .w{display:inline-block;}
 .ty{display:inline-block;clip-path:inset(-20% 100% -20% 0);}
 ${ST}
 @keyframes show{0%{opacity:1}99.5%{opacity:1}100%{opacity:0}}
 @keyframes pop{from{opacity:0;transform:scale(.82)}to{opacity:1;transform:none}}
 @keyframes type{from{clip-path:inset(-20% 100% -20% 0)}to{clip-path:inset(-20% -5% -20% 0)}}
</style></head><body>${body}</body></html>`;
(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const hp = path.join(outDir, 'cap.html'); fs.writeFileSync(hp, html);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: scale });
  await page.goto('file://' + path.resolve(hp)); await page.evaluate(() => document.fonts.ready);
  const n = Math.round(dur * fps);
  for (let f = 0; f <= n; f++) {
    await page.evaluate(ms => document.getAnimations().forEach(a => { a.pause(); a.currentTime = ms; }), f / fps * 1000);
    await page.screenshot({ path: path.join(outDir, `f_${String(f).padStart(4, '0')}.png`), omitBackground: true });
  }
  await browser.close(); console.log('style', style, n + 1, 'frames');
})();
