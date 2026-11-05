// Reference-inspired Manosh captions (5 options), rendered as two transparent layers:
//   back  = giant key word (composited BEHIND the person), front = word captions.
// Usage: node caption_ref.js <option 1-5> <back|front> <pages.json> <out_dir> [fps] [dur]
// pages.json: [{"start","end","small":[[w,t,hl?],...],"big":[w,t,hl?]}]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [opt, layer, pagesPath, outDir, fpsArg, durArg] = process.argv.slice(2);
const pages = JSON.parse(fs.readFileSync(pagesPath, 'utf8'));
const fps = Number(fpsArg || 30), dur = Number(durArg || pages.at(-1).end + .2), o = Number(opt);
const css = 'file://' + path.resolve(__dirname, '../manosh/Manosh/templates/brand.css');
const LETTER = 0.035;
const words = p => [...p.small.map(([w, t, h]) => ({ w, t, h: !!h, k: false })), { w: p.big[0], t: p.big[1], h: !!p.big[2], k: true }];
const pgAnim = p => o == 3   // 3 dissolves between lines, the rest hard-swap
  ? `animation:fin .22s linear ${p.start}s both, fout .25s linear ${(p.end - .05).toFixed(3)}s forwards`
  : `animation:show ${(p.end - p.start).toFixed(3)}s linear ${p.start}s forwards`;
let nk = 0;
const typed = (w, t, n = w.length) => `<span class="ty" style="animation:type ${(n * LETTER).toFixed(3)}s steps(${n}) ${t}s both">${w}</span>`;
const back = p => {
  const [w, t] = p.big;
  if (o == 1) return `<div class="giant g1"><span style="animation:rise .32s cubic-bezier(.22,1,.36,1) ${t}s both">${w}</span></div>`;
  if (o == 3) return `<div class="giant g3"><span style="animation:fin .35s linear ${t}s both">${w}</span></div>`;
  if (o == 5) return `<div class="giant g1"><span style="animation:fin .01s linear ${t}s both">${typed(w, t)}</span></div>`;
  return '';
};
const front = p => {
  const ws = words(p);
  if (o == 1) return `<div class="tags">` + ws.map(x => `<span class="tag${x.k ? ' k' : ''}" style="animation:fin .12s linear ${x.t}s both">${x.w}</span>`).join('') + `</div>`;
  if (o == 2) return `<div class="line">` + ws.map(x => x.k
      ? `<span class="kw" style="animation:ghost .22s linear ${x.t}s both;--d:${(x.t + .12).toFixed(3)}s">${x.w}</span>`
      : `<span class="sw" style="animation:ghost .22s linear ${x.t}s both">${x.w}</span>`).join(' ') + `</div>`;
  if (o == 3) return `<div class="serif">` + ws.filter(x => !x.k).map(x => `<span style="animation:fin .2s linear ${x.t}s both">${x.w}</span>`).join(' ') + `</div>`;
  if (o == 4 || o == 5) return `<div class="chips c${o}">` + ws.map(x => `<span class="chip${x.k || x.h ? (nk++ % 2 ? ' kc g' : ' kc') : ''}" style="animation:chip .16s cubic-bezier(.34,1.56,.64,1) ${x.t}s both">${x.w}</span>`).join('') + `</div>`;
  return '';
};
const body = pages.map(p => `<div class="pg" style="${pgAnim(p)}">${layer == 'back' ? back(p) : front(p)}</div>`).join('\n');
const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="${css}"><style>
 body{width:1080px;height:1920px;margin:0;position:relative;overflow:hidden;}
 .pg{position:absolute;inset:0;opacity:0;}
 /* giant key word, sits behind her head (bottom edge ~ head top) */
 .giant{position:absolute;left:0;right:0;bottom:${1920 - 790}px;text-align:center;white-space:nowrap;}
 .giant span{display:inline-block;}
 .g1{font:900 420px/0.8 'Nunito Sans';color:var(--burgundy);text-transform:uppercase;letter-spacing:-.03em;}
 .g3{font:600 360px/0.85 'Cormorant Garamond';color:var(--gold);letter-spacing:-.01em;text-shadow:0 3px 0 rgba(76,33,48,.22);}
 /* 1: square word tags, lower left */
 .tags{position:absolute;left:64px;width:780px;top:1380px;display:flex;flex-wrap:wrap;gap:12px;}
 .tag{font:800 46px/1 'Nunito Sans';letter-spacing:4px;text-transform:uppercase;color:var(--burgundy);background:var(--cream);
   padding:10px 14px 8px;border-radius:5px;box-shadow:0 3px 10px rgba(0,0,0,.18);}
 .tag.k{background:var(--burgundy);color:var(--cream);}
 /* 2: minimal line, italic serif keyword with gold underline */
 .line{position:absolute;left:40px;right:40px;top:470px;text-align:center;font:800 84px/1.2 'Nunito Sans';color:var(--burgundy);}
 .sw,.kw{display:inline-block;} .kw{position:relative;font:italic 700 132px/1 'Cormorant Garamond';margin-left:.08em;}
 .kw:after{content:'';position:absolute;left:4%;right:2%;bottom:-2px;height:7px;border-radius:4px;background:var(--gold);transform-origin:left;
   animation:uline .3s cubic-bezier(.22,1,.36,1) var(--d) both;}
 /* 3: small serif words at chest height */
 .serif{position:absolute;left:40px;right:40px;top:1190px;text-align:center;font:700 100px/1.1 'Cormorant Garamond';color:var(--burgundy);
   text-shadow:0 0 22px var(--cream),0 0 10px var(--cream),0 0 4px var(--cream);}
 .serif span{display:inline-block;}
 /* 4/5: rounded word chips, keyword chips in italic serif on burgundy / gold */
 .chips{position:absolute;left:70px;right:70px;display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:10px 10px;}
 .c4{top:1170px;} .c5{top:1330px;}
 .chip{font:800 62px/1 'Nunito Sans';color:var(--burgundy);background:var(--cream);padding:9px 18px 12px;border-radius:16px;box-shadow:0 4px 14px rgba(76,33,48,.22);}
 .chip.kc{font:italic 700 78px/0.9 'Cormorant Garamond';color:var(--cream);background:var(--burgundy);padding:8px 20px 12px;}
 .chip.kc.g{background:var(--gold);text-shadow:0 2px 0 rgba(76,33,48,.3);}
 .ty{display:inline-block;clip-path:inset(-30% 100% -30% 0);}
 @keyframes show{0%{opacity:1}99.5%{opacity:1}100%{opacity:0}}
 @keyframes fin{from{opacity:0}to{opacity:1}} @keyframes fout{from{opacity:1}to{opacity:0}}
 @keyframes ghost{from{opacity:0;filter:blur(6px)}to{opacity:1;filter:none}}
 @keyframes rise{from{opacity:0;transform:translateY(70px)}to{opacity:1;transform:none}}
 @keyframes uline{from{transform:scaleX(0)}to{transform:scaleX(1)}}
 @keyframes chip{from{opacity:0;transform:scale(.8)}to{opacity:1;transform:none}}
 @keyframes type{from{clip-path:inset(-30% 100% -30% 0)}to{clip-path:inset(-30% -5% -30% 0)}}
</style></head><body>${body}</body></html>`;
(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const hp = path.join(outDir, 'cap.html'); fs.writeFileSync(hp, html);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.resolve(hp)); await page.evaluate(() => document.fonts.ready);
  await page.evaluate(() => document.querySelectorAll('.giant span:not(.ty)').forEach(el => {   // fit giant word to the frame
    let fs = parseFloat(getComputedStyle(el).fontSize);
    while (el.scrollWidth > 1010 && fs > 120) { fs -= 6; el.style.fontSize = fs + 'px'; }
  }));
  const n = Math.round(dur * fps);
  for (let f = 0; f <= n; f++) {
    await page.evaluate(ms => document.getAnimations().forEach(a => { a.pause(); a.currentTime = ms; }), f / fps * 1000);
    await page.screenshot({ path: path.join(outDir, `f_${String(f).padStart(4, '0')}.png`), omitBackground: true });
  }
  await browser.close(); console.log('opt', opt, layer, n + 1, 'frames');
})();
