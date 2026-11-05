// Plain typed captions with kit-colour blocks on SOME words (flag 3rd element true)
// and zoom cuts on the TEXT (style n uses zoom mode n; the video frame stays still).
// placed above centre. Usage: node caption_type3.js <style 1-5> <pages.json> <out_dir> [scale] [fps] [dur]
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
// highlight block per style (only on flagged words)
// highlight blocks alternate burgundy / gold, cream text (only on flagged words)
const H = `.w.h{background:var(--burgundy);color:var(--cream);} .w.h.g{background:var(--gold);text-shadow:0 3px 0 rgba(76,33,48,.28);}` +
  (style == 4 ? ` .w.h,.w.h.g{background:none;} .w.h:before{content:'';position:absolute;inset:0;border-radius:inherit;background:var(--burgundy);z-index:-1;
      transform-origin:left center;animation:swipe .2s cubic-bezier(.22,1,.36,1) var(--d) both;} .w.h.g:before{background:var(--gold);}` : '');
let nh = 0;
// zoom points [t, scale]; equal times = hard cut. Modes:
// 1 punch: caption cuts to 1.15 when the big word lands   2 snap: big word slams in from 2.4x
// 3 pull-back: each page enters at 1.35x and settles       4 step: every word cuts the caption up a notch
// 5 pulse: highlighted words cut to 1.25x for .3s then cut back
const ease = (t0, z0, z1, d) => [...Array(9)].map((_, i) => [t0 + d * i / 8, z1 + (z0 - z1) * Math.pow(1 - i / 8, 3)]);
const zoomPts = p => {
  const s = p.start, b = p.big[1], E = p.end;
  if (style == 1) return [[s, 1], [b, 1], [b, 1.15], [E, 1.15]];
  if (style == 3) return [...ease(s, 1.35, 1, .35), [E, 1]];
  if (style == 4) { const pts = [[s, 1]]; let z = 1;
    p.small.slice(1).forEach(([, t]) => { pts.push([t, z], [t, z += .04]); });
    pts.push([b, z], [b, z += .1], [E, z]); return pts; }
  return [[s, 1], [E, 1]];
};
const maxZ = { 1: 1.15, 4: 1.26, 5: 1.25 }[style] || 1;
let kf = '';
const zAnim = (p, i) => {
  const d = p.end - p.start, pts = zoomPts(p);
  kf += `@keyframes z${i}{` + pts.map(([t, z], j) => `${(Math.min(100, (t - p.start) / d * 100) + (j && t === pts[j - 1][0] ? .001 : 0)).toFixed(3)}%{transform:scale(${z.toFixed(4)})}`).join('') + '}\n';
  return `animation:z${i} ${d.toFixed(3)}s linear ${p.start}s both`;
};
const wAnim = (w, t, h, cls) => {
  const td = w.length * LETTER;
  if (style == 2 && cls == 'b') return `animation:snap .16s cubic-bezier(.22,1,.36,1) ${t}s both`;
  if (style == 5 && h) return `animation:pop .2s cubic-bezier(.34,1.56,.64,1) ${t}s both, pulse .3s step-end ${(t + td).toFixed(3)}s forwards`;
  return `animation:pop .2s cubic-bezier(.34,1.56,.64,1) ${t}s both`;
};
const typed = (w, t, cls, h) => `<span class="w ${cls}${h ? (nh++ % 2 ? ' h g' : ' h') : ''}" style="--d:${t}s;${wAnim(w, t, h, cls)}"><span class="ty" style="animation:type ${(w.length * LETTER).toFixed(3)}s steps(${w.length}) ${t}s both">${w}</span></span>`;
const body = pages.map((p, i) => `<div class="pg" style="animation:show ${(p.end - p.start).toFixed(3)}s linear ${p.start}s forwards">
 <div class="zm" style="${zAnim(p, i)}">
  <div class="sl">${p.small.map(([w, t, h]) => typed(w, t, 's', h)).join(' ')}</div>
  <div class="bl">${typed(p.big[0], p.big[1], 'b', p.big[2])}</div></div></div>`).join('');
const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="${css}"><style>
 body{width:1080px;height:1920px;margin:0;position:relative;overflow:hidden;}
 .pg{position:absolute;top:210px;left:40px;right:40px;text-align:center;opacity:0;}
 .sl{line-height:1.05;} .bl{line-height:.92;margin-top:4px;white-space:nowrap;}
 .w{display:inline-block;position:relative;z-index:0;} .w.s{${S.sm}margin:0 .14em;} .w.b{${S.bg}}
 .w.b{transform-origin:50% 8%;}
 .w.s.h{padding:.02em .2em .06em;border-radius:14px;} .w.b.h{padding:.04em .16em .02em;border-radius:26px;margin-top:10px;}
 ${H}
 .ty{display:inline-block;clip-path:inset(-30% 100% -30% 0);}
 @keyframes show{0%{opacity:1}99.5%{opacity:1}100%{opacity:0}}
 @keyframes pop{from{opacity:0;transform:scale(.85)}to{opacity:1;transform:none}}
 .zm{transform-origin:50% 60%;}
 ${kf}
 @keyframes snap{from{opacity:0;transform:scale(2.4)}to{opacity:1;transform:none}}
 @keyframes pulse{0%{transform:scale(1.25)}100%{transform:none}}
 @keyframes swipe{from{transform:scaleX(0)}to{transform:scaleX(1)}}
 @keyframes type{from{clip-path:inset(-30% 100% -30% 0)}to{clip-path:inset(-30% -5% -30% 0)}}
</style></head><body>${body}</body></html>`;
(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const hp = path.join(outDir, 'cap.html'); fs.writeFileSync(hp, html);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: scale });
  await page.goto('file://' + path.resolve(hp)); await page.evaluate(() => document.fonts.ready);
  // fit each BIG word to the frame width
  await page.evaluate(W => document.querySelectorAll('.w.b').forEach(el => {
    let fs = parseFloat(getComputedStyle(el).fontSize);
    while (el.scrollWidth > W && fs > 80) { fs -= 4; el.style.fontSize = fs + 'px'; }
  }), 1000 / maxZ);
  const n = Math.round(dur * fps);
  for (let f = 0; f <= n; f++) {
    await page.evaluate(ms => document.getAnimations().forEach(a => { a.pause(); a.currentTime = ms; }), f / fps * 1000);
    await page.screenshot({ path: path.join(outDir, `f_${String(f).padStart(4, '0')}.png`), omitBackground: true });
  }
  await browser.close(); console.log('style', style, n + 1, 'frames');
})();
