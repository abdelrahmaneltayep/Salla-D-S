// Reel-inspired Manosh hook layers -> transparent (or opaque page) PNG frames.
// Usage: node hook_anim2.js <variant 1-10> <out_dir> [scale=1] [fps=30] [dur=3.4]
// Variants: 1 kinetic slam, 2 text behind (layer only), 3 title card (page), 4 gravity drop,
// 5 comment bubble, 6 giant captions, 7 magazine cover (layer only), 8 pinned series title,
// 9 (pull-back: reuses pill pop layer), 10 screenplay page (page)
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [variant, outDir, scaleArg, fpsArg, durArg] = process.argv.slice(2);
const scale = Number(scaleArg || 1), fps = Number(fpsArg || 30), dur = Number(durArg || 3.4);
const css = 'file://' + path.resolve(__dirname, '../manosh/Manosh/templates/brand.css');
const bounce = 'cubic-bezier(.34,1.56,.64,1)', easeOut = 'cubic-bezier(.22,1,.36,1)';
const words = [["I'm", 1.83], ["free", 2.15], ["and", 3.11], ["I", 3.23], ["had", 3.43], ["freedom", 3.67],
               ["to", 4.27], ["wear", 4.51], ["my", 4.79], ["hijab", 5.03]];
const pages = [[0, 2, 1.80, 3.05], [2, 6, 3.08, 4.22], [6, 10, 4.25, 5.9]];
let body = '', style = '';
switch (variant) {
  case '1': {
    const W = [['FREE TO WEAR', 104, ''], ['ANYTHING…', 128, ''], ['EXCEPT', 104, ''], ['HIJAB?', 196, 'g']];
    body = `<div class="ks">${W.map(([t, s, g], i) => `<div class="w ${g}" style="font-size:${s}px;animation:slam .32s ${bounce} ${.15 + i * .3}s both">${t}</div>`).join('')}</div>`;
    style = `.ks{position:absolute;top:150px;left:0;right:0;text-align:center;font-family:'Nunito Sans';font-weight:800;color:var(--burgundy);line-height:.98;letter-spacing:-2px;}
      .w.g{color:var(--gold);-webkit-text-stroke:5px var(--burgundy);paint-order:stroke fill;}
      @keyframes slam{from{opacity:0;transform:scale(1.7)}to{opacity:1;transform:none}}`;
    break; }
  case '2':
    body = `<div class="sm">free to wear anything… except</div><div class="big">HIJAB</div>`;
    style = `.sm{position:absolute;top:430px;left:0;right:0;text-align:center;font-family:'Cormorant Garamond';font-weight:600;font-style:italic;font-size:62px;color:var(--burgundy);animation:up .5s ${easeOut} .15s both;}
      .big{position:absolute;top:500px;left:0;right:0;text-align:center;font-family:'Cormorant Garamond';font-weight:600;font-size:360px;line-height:1;letter-spacing:12px;color:var(--burgundy);animation:up .7s ${easeOut} .35s both;}
      @keyframes up{from{opacity:0;transform:translateY(70px)}to{opacity:1;transform:none}}`;
    break;
  case '3':
    body = `<div class="pg"><div class="mk">MENNATULLAH</div><div class="rl"></div>
      <div class="l" style="animation-delay:.2s">Free to wear</div><div class="l" style="animation-delay:.42s">anything…</div>
      <div class="l i" style="animation-delay:.64s">except <span>hijab?</span></div><div class="rl b"></div></div>`;
    style = `.pg{position:absolute;inset:0;background:var(--cream);text-align:center;padding-top:250px;}
      .mk{font-family:'Cormorant Garamond';font-weight:600;font-size:34px;letter-spacing:12px;color:var(--gold);animation:fd .4s linear .05s both;}
      .rl{width:90px;height:2px;background:rgba(201,162,100,.9);margin:26px auto 40px;animation:fd .4s linear .1s both;} .rl.b{margin-top:44px;}
      .l{font-family:'Cormorant Garamond';font-weight:600;font-size:118px;line-height:1.02;color:var(--burgundy);animation:up .55s ${easeOut} both;}
      .l.i{font-style:italic;} .l span{color:var(--terracotta);}
      @keyframes fd{from{opacity:0}to{opacity:1}} @keyframes up{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:none}}`;
    break;
  case '4': {
    const L = 'HIJAB?'.split('');
    body = `<div class="sm">free to wear anything… except</div><div class="gd">${L.map((c, i) => `<span class="${c === '?' ? 'q' : ''}" style="animation:grav .6s ${bounce} ${.45 + i * .1}s both">${c}</span>`).join('')}</div>`;
    style = `.sm{position:absolute;top:300px;left:0;right:0;text-align:center;font-family:'Cormorant Garamond';font-weight:600;font-style:italic;font-size:60px;color:var(--burgundy);animation:fd .4s linear .15s both;}
      .gd{position:absolute;top:370px;left:0;right:0;text-align:center;font-family:'Cormorant Garamond';font-weight:600;font-size:240px;line-height:1;color:var(--burgundy);letter-spacing:6px;}
      .gd span{display:inline-block;} .gd .q{color:var(--gold);}
      @keyframes fd{from{opacity:0}to{opacity:1}} @keyframes grav{from{transform:translateY(-520px)}to{transform:none}}`;
    break; }
  case '5': {
    const txt = 'Free to wear anything… except hijab?';
    body = `<div class="bub"><div class="av">M</div><div class="tx"><div class="nm">@mennatullah.mo</div>
      <div class="ty"><span>${txt}</span></div></div><div class="ht">♡</div></div>`;
    style = `.bub{position:absolute;top:250px;left:70px;right:70px;display:flex;align-items:center;gap:22px;background:#fff;border-radius:44px;padding:26px 32px;
        box-shadow:0 10px 30px rgba(30,15,20,.18);animation:pop .42s ${bounce} .15s both;transform-origin:left center;}
      .av{flex:none;width:84px;height:84px;border-radius:50%;background:var(--burgundy);color:var(--gold);font:800 44px 'Nunito Sans';display:flex;align-items:center;justify-content:center;}
      .tx{flex:1;min-width:0;} .nm{font:700 28px 'Nunito Sans';color:#8a7d80;margin-bottom:6px;}
      .ty{font:800 38px 'Nunito Sans';color:var(--burgundy);white-space:nowrap;overflow:hidden;}
      .ty span{display:inline-block;animation:type 1.3s steps(${txt.length}) .45s both;clip-path:inset(0 100% 0 0);}
      .ht{flex:none;font-size:46px;color:var(--terracotta);}
      @keyframes pop{0%{opacity:0;transform:scale(.4)}100%{opacity:1;transform:none}}
      @keyframes type{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}`;
    break; }
  case '6':
    body = pages.map(([a, b, s, e], pi) => `<div class="pg" style="animation:show ${(e - s).toFixed(2)}s linear ${s}s forwards">${words.slice(a, b).map(([w, t]) =>
      `<span class="w${w === 'free' || w === 'hijab' || w === 'freedom' ? ' k' : ''}" style="animation:wp .22s ${bounce} ${t}s both${w === 'free' || w === 'hijab' || w === 'freedom' ? '' : `, act .5s linear ${t}s both`}">${w.toUpperCase()}</span>`).join(' ')}</div>`).join('');
    style = `.pg{position:absolute;top:1180px;left:60px;right:60px;text-align:center;font-family:'Nunito Sans';font-weight:800;font-size:112px;line-height:1.06;letter-spacing:3px;word-spacing:14px;opacity:0;}
      .w{display:inline-block;color:var(--cream);-webkit-text-stroke:6px var(--burgundy);paint-order:stroke fill;} .w.k{color:var(--gold);}
      @keyframes show{0%{opacity:1}99.5%{opacity:1}100%{opacity:0}} @keyframes wp{from{opacity:0;transform:scale(.6)}to{opacity:1;transform:none}}
      @keyframes act{0%{color:var(--gold)}99%{color:var(--gold)}100%{color:var(--cream)}}`;
    break;
  case '7':
    body = `<div class="iss">ISSUE 05 · WOMEN IN ISLAM</div><div class="mast">MENNATULLAH</div>
      <div class="cl"><span class="c1">Free to wear anything…</span><br><span class="c2">except <span>hijab?</span></span></div>`;
    style = `.iss{position:absolute;top:612px;left:0;right:0;text-align:center;font:700 26px 'Nunito Sans';letter-spacing:6px;color:var(--terracotta);animation:fd .4s linear .2s both;}
      .mast{position:absolute;top:652px;left:0;right:0;text-align:center;font-family:'Cormorant Garamond';font-weight:600;font-size:132px;line-height:1;letter-spacing:2px;color:var(--burgundy);animation:dn .6s ${easeOut} .15s both;}
      .cl{position:absolute;top:1230px;left:70px;animation:fd .4s linear .7s both;} .c1,.c2{font:800 54px 'Nunito Sans';color:var(--cream);background:var(--burgundy);display:inline-block;padding:8px 20px 10px;border-radius:10px;}
      .c2{margin-top:12px;} .c2 span{color:var(--gold);}
      @keyframes fd{from{opacity:0}to{opacity:1}} @keyframes dn{from{opacity:0;transform:translateY(-80px)}to{opacity:1;transform:none}}`;
    break;
  case '8':
    body = `<div class="pin"><div class="ep">WOMEN IN ISLAM · 05</div><div class="t1">Free to wear anything…</div><div class="t2">except <span>hijab?</span></div></div>`;
    style = `.pin{position:absolute;top:150px;left:0;right:0;text-align:center;animation:dn .55s ${easeOut} .15s both;}
      .ep{font:700 28px 'Nunito Sans';letter-spacing:6px;color:var(--gold);margin-bottom:12px;}
      .t1,.t2{font:800 74px 'Nunito Sans';line-height:1.05;color:var(--burgundy);letter-spacing:-1px;} .t2 span{color:var(--terracotta);}
      @keyframes dn{from{opacity:0;transform:translateY(-60px)}to{opacity:1;transform:none}}`;
    break;
  case '10': {
    const L = [['INT. MENNATULLAH\'S ROOM — DAY', 'l', .15], ['MENNATULLAH', 'c', .75], ['(to camera)', 'c p', 1.05],
               ['Free to wear anything…', 'c d', 1.3], ['except <mark>hijab?</mark>', 'c d', 1.85]];
    body = `<div class="sp">${L.map(([t, c, d]) => { const n = t.replace(/<[^>]+>/g, '').length;
      return `<div class="${c}"><span style="animation:type ${(n * .028).toFixed(2)}s steps(${n}) ${d}s both">${t}</span></div>`; }).join('')}<div class="ct">CUT TO:</div></div>`;
    style = `.sp{position:absolute;inset:0;background:var(--cream);padding:430px 90px 0;font-family:'Courier New','Liberation Mono','DejaVu Sans Mono',monospace;font-size:44px;color:#3a2a2e;}
      .sp div{margin-bottom:26px;white-space:nowrap;} .sp .c{text-align:center;} .sp .p{color:#7d6d70;} .sp .l{margin-bottom:70px;}
      .sp span{display:inline-block;clip-path:inset(0 100% 0 0);} mark{background:rgba(201,124,90,.45);color:inherit;padding:0 6px;}
      .ct{text-align:right;margin-top:60px;animation:fd .2s linear 2.45s both;}
      @keyframes type{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}} @keyframes fd{from{opacity:0}to{opacity:1}}`;
    break; }
}
const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="${css}">
<style>body{width:1080px;height:1920px;margin:0;position:relative;overflow:hidden;}${style}</style></head><body>${body}</body></html>`;
(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const hp = path.join(outDir, 'hook.html'); fs.writeFileSync(hp, html);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: scale });
  await page.goto('file://' + path.resolve(hp)); await page.evaluate(() => document.fonts.ready);
  const n = Math.round(dur * fps);
  for (let f = 0; f <= n; f++) {
    await page.evaluate(ms => document.getAnimations().forEach(a => { a.pause(); a.currentTime = ms; }), f / fps * 1000);
    await page.screenshot({ path: path.join(outDir, `f_${String(f).padStart(4, '0')}.png`), omitBackground: true });
  }
  await browser.close(); console.log('variant', variant, n + 1, 'frames');
})();
