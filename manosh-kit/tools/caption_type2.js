// Plain typed captions (no border/background), small words + one BIG word per page,
// placed above centre. Usage: node caption_type2.js <style 1-5> <pages.json> <out_dir> [scale] [fps] [dur]
// pages.json: [{"start","end","small":[[w,t],...],"big":[w,t]}]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [style, pagesPath, outDir, scaleArg, fpsArg, durArg] = process.argv.slice(2);
const pages = JSON.parse(fs.readFileSync(pagesPath, 'utf8'));
const scale = Number(scaleArg || 1), fps = Number(fpsArg || 30), dur = Number(durArg || pages.at(-1).end + .2);
const LETTER = 0.035;
const css = 'file://' + path.resolve(__dirname, '../manosh/Manosh/templates/brand.css');
const S = {
  1: { sm: `font:800 76px 'Nunito Sans';color:var(--burgundy);`,
       bg: `font:800 230px 'Nunito Sans';color:var(--burgundy);text-transform:uppercase;letter-spacing:-4px;` },
  2: { sm: `font:800 72px 'Nunito Sans';color:var(--burgundy);`,
       bg: `font:800 230px 'Nunito Sans';color:var(--terracotta);text-transform:uppercase;letter-spacing:-4px;` },
  3: { sm: `font:italic 600 92px 'Cormorant Garamond';color:var(--burgundy);`,
       bg: `font:600 250px 'Cormorant Garamond';color:var(--burgundy);text-transform:uppercase;letter-spacing:2px;` },
  4: { sm: `font:700 64px 'Nunito Sans';color:var(--terracotta);text-transform:uppercase;letter-spacing:8px;`,
       bg: `font:800 230px 'Nunito Sans';color:var(--burgundy);text-transform:uppercase;letter-spacing:-4px;` },
  5: { sm: `font:italic 600 90px 'Cormorant Garamond';color:var(--burgundy);`,
       bg: `font:800 220px 'Nunito Sans';color:var(--terracotta);text-transform:uppercase;letter-spacing:-3px;` },
}[style];
const typed = (w, t, cls) => `<span class="w ${cls}" style="animation:pop .2s cubic-bezier(.34,1.56,.64,1) ${t}s both"><span class="ty" style="animation:type ${(w.length * LETTER).toFixed(3)}s steps(${w.length}) ${t}s both">${w}</span></span>`;
const body = pages.map(p => `<div class="pg" style="animation:show ${(p.end - p.start).toFixed(3)}s linear ${p.start}s forwards">
  <div class="sl">${p.small.map(([w, t]) => typed(w, t, 's')).join(' ')}</div>
  <div class="bl">${typed(p.big[0], p.big[1], 'b')}</div></div>`).join('');
const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="${css}"><style>
 body{width:1080px;height:1920px;margin:0;position:relative;overflow:hidden;}
 .pg{position:absolute;top:210px;left:40px;right:40px;text-align:center;opacity:0;}
 .sl{line-height:1.05;} .bl{line-height:.92;margin-top:4px;white-space:nowrap;}
 .w{display:inline-block;} .w.s{${S.sm}margin:0 .14em;} .w.b{${S.bg}}
 .ty{display:inline-block;clip-path:inset(-30% 100% -30% 0);}
 @keyframes show{0%{opacity:1}99.5%{opacity:1}100%{opacity:0}}
 @keyframes pop{from{opacity:0;transform:scale(.85)}to{opacity:1;transform:none}}
 @keyframes type{from{clip-path:inset(-30% 100% -30% 0)}to{clip-path:inset(-30% -5% -30% 0)}}
</style></head><body>${body}</body></html>`;
(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const hp = path.join(outDir, 'cap.html'); fs.writeFileSync(hp, html);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: scale });
  await page.goto('file://' + path.resolve(hp)); await page.evaluate(() => document.fonts.ready);
  // fit each BIG word to the frame width
  await page.evaluate(() => document.querySelectorAll('.w.b').forEach(el => {
    let fs = parseFloat(getComputedStyle(el).fontSize);
    while (el.scrollWidth > 1000 && fs > 80) { fs -= 4; el.style.fontSize = fs + 'px'; }
  }));
  const n = Math.round(dur * fps);
  for (let f = 0; f <= n; f++) {
    await page.evaluate(ms => document.getAnimations().forEach(a => { a.pause(); a.currentTime = ms; }), f / fps * 1000);
    await page.screenshot({ path: path.join(outDir, `f_${String(f).padStart(4, '0')}.png`), omitBackground: true });
  }
  await browser.close(); console.log('style', style, n + 1, 'frames');
})();
