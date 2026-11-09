// Manosh Instagram carousel (1080x1350, 4:5) from a story video.
// Usage: node carousel.js <slides.json> <img_dir> <out_dir>
// slides.json: [{"kind":"cover"|"story"|"text"|"end", "kicker","title","body","img","n"}]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [slidesPath, imgDir, outDir] = process.argv.slice(2);
const slides = JSON.parse(fs.readFileSync(slidesPath, 'utf8'));
const css = 'file://' + path.resolve(__dirname, '../manosh/Manosh/templates/brand.css');
const AR = /([؀-ۿﭐ-﷿ﹰ-﻿]+(?:\s+[؀-ۿﭐ-﷿ﹰ-﻿]+)*)/g;
const fmt = s => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;')
  .replace(/\{\{gold\}\}/g, '<span class="hl">').replace(/\{\{\/gold\}\}/g, '</span>')
  .replace(AR, '<bdi class="ar" dir="rtl">$1</bdi>');
const img = s => s.img ? `<img class="pap" src="file://${path.resolve(imgDir, s.img)}">` : '';
const total = slides.length;
const body = (s, i) => {
  const dots = `<div class="dots">${slides.map((_, j) => `<i class="${j === i ? 'on' : ''}"></i>`).join('')}</div>`;
  const handle = `<div class="handle"><span class="star">✦</span>@mennatullah.mo</div>`;
  if (s.kind === 'cover') return `<section class="cover">${img(s)}<div class="txt"><div class="kick">${fmt(s.kicker)}</div>
    <h1>${fmt(s.title)}</h1><div class="sub">${fmt(s.body)}</div></div><div class="swipe">Swipe <span>→</span></div>${handle}</section>`;
  if (s.kind === 'end') return `<section class="end">${img(s)}<div class="quote">${fmt(s.title)}</div><div class="sub">${fmt(s.body)}</div>
    <div class="cta">Follow for more stories of the Sahabiyat</div>${handle}${dots}</section>`;
  return `<section class="story ${s.img ? '' : 'noimg'}"><div class="num">${String(i).padStart(2, '0')}</div>${img(s)}
    <div class="txt"><div class="kick">${fmt(s.kicker)}</div><h2>${fmt(s.title)}</h2><p>${fmt(s.body)}</p></div>${handle}${dots}</section>`;
};
const html = s => `<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="${css}"><style>
 body{margin:0;width:1080px;height:1350px;overflow:hidden;background:var(--burgundy);}
 section{position:relative;width:1080px;height:1350px;box-sizing:border-box;overflow:hidden;
   background:radial-gradient(ellipse 90% 70% at 50% 35%,#5d2a3b 0%,var(--burgundy) 60%,#3a1824 100%);color:var(--cream);}
 .pap{position:absolute;left:70px;width:940px;filter:none;}
 .ar{font-family:'Amiri';font-weight:700;white-space:nowrap;}
 .hl{color:var(--gold);}
 .handle{position:absolute;left:0;right:0;bottom:44px;text-align:center;font:700 24px 'Nunito Sans';letter-spacing:4px;color:var(--gold);}
 .handle .star{margin-right:10px;}
 .dots{position:absolute;right:70px;bottom:52px;display:flex;gap:8px;} .dots i{width:10px;height:10px;border-radius:50%;background:rgba(243,236,223,.3);} .dots i.on{background:var(--gold);}
 .cover .pap{top:90px;} .cover .txt{position:absolute;left:80px;right:80px;top:740px;text-align:center;}
 .kick{font:700 26px 'Nunito Sans';letter-spacing:5px;text-transform:uppercase;color:var(--gold);}
 h1{margin:18px 0 0;font:600 104px/1 'Cormorant Garamond';color:var(--cream);}
 .cover .sub{margin-top:26px;font:italic 600 44px/1.25 'Cormorant Garamond';color:var(--cream);opacity:.92;}
 .swipe{position:absolute;right:80px;bottom:110px;font:700 28px 'Nunito Sans';color:var(--cream);opacity:.85;} .swipe span{color:var(--gold);}
 .story .num{position:absolute;left:80px;top:64px;font:600 64px 'Cormorant Garamond';color:var(--gold);opacity:.9;}
 .story .pap{top:160px;} .story .txt{position:absolute;left:90px;right:90px;top:780px;}
 .story h2{margin:14px 0 0;font:600 66px/1.08 'Cormorant Garamond';color:var(--cream);}
 .story p{margin:24px 0 0;font:600 34px/1.45 'Nunito Sans';color:rgba(243,236,223,.9);}
 .story.noimg .txt{top:360px;} .story.noimg h2{font-size:84px;} .story.noimg p{font-size:40px;}
 .end .pap{top:90px;opacity:.95;} .end .quote{position:absolute;left:90px;right:90px;top:760px;text-align:center;font:italic 600 62px/1.15 'Cormorant Garamond';}
 .end .sub{position:absolute;left:90px;right:90px;top:1010px;text-align:center;font:600 30px/1.4 'Nunito Sans';opacity:.85;}
 .end .cta{position:absolute;left:0;right:0;top:1150px;text-align:center;}
 .end .cta{display:block;margin:0 auto;width:fit-content;left:50%;translate:-50% 0;font:800 30px 'Nunito Sans';color:var(--burgundy);background:var(--gold);padding:14px 30px;border-radius:14px;white-space:nowrap;}
</style></head><body>${s}</body></html>`;
(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch(); const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (let i = 0; i < slides.length; i++) {
    const hp = path.join(outDir, `slide_${i + 1}.html`); fs.writeFileSync(hp, html(body(slides[i], i)));
    await page.goto('file://' + path.resolve(hp)); await page.evaluate(() => document.fonts.ready);
    await page.waitForFunction(() => [...document.images].every(im => im.complete));
    await page.screenshot({ path: path.join(outDir, `Manosh_carousel_${String(i + 1).padStart(2, '0')}.png`) });
  }
  await browser.close(); console.log('slides', slides.length);
})();
