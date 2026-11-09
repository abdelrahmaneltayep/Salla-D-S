// Manosh Instagram carousel, full-frame storyboard style (1080x1350, 4:5).
// Each slide = a full-bleed illustration on paper (paper_full.py output, cropped from the top), text set
// directly on the lighter lower paper in burgundy. Usage: node carousel_full.js <slides.json> <img_dir> <out_dir>
// slides.json: [{"kind":"cover"|"story"|"end","img","kicker","title","body"}]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [slidesPath, imgDir, outDir] = process.argv.slice(2);
const slides = JSON.parse(fs.readFileSync(slidesPath, 'utf8'));
const css = 'file://' + path.resolve(__dirname, '../manosh/Manosh/templates/brand.css');
const AR = /([؀-ۿﭐ-﷿ﹰ-﻿]+(?:\s+[؀-ۿﭐ-﷿ﹰ-﻿]+)*)/g;
const fmt = s => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;')
  .replace(/\{\{gold\}\}/g, '<span class="hl">').replace(/\{\{\/gold\}\}/g, '</span>')
  .replace(AR, '<bdi class="ar" dir="rtl">$1</bdi>');
const page = (s, i) => {
  const dots = `<div class="dots">${slides.map((_, j) => `<i class="${j === i ? 'on' : ''}"></i>`).join('')}</div>`;
  const handle = `<div class="handle"><span>✦</span> @mennatullah.mo</div>`;
  const inner = s.kind === 'cover'
    ? `<div class="txt cov"><div class="kick">${fmt(s.kicker)}</div><h1>${fmt(s.title)}</h1><div class="sub">${fmt(s.body)}</div></div><div class="swipe">Swipe →</div>`
    : s.kind === 'end'
    ? `<div class="txt end"><div class="quote">${fmt(s.title)}</div><div class="sub">${fmt(s.body)}</div><div class="cta">Follow for more stories of the Sahabiyat</div></div>`
    : `<div class="num">${String(i).padStart(2, '0')}</div><div class="txt"><div class="kick">${fmt(s.kicker)}</div><h2>${fmt(s.title)}</h2><p>${fmt(s.body)}</p></div>`;
  return `<section><img class="bg" src="file://${path.resolve(imgDir, s.img)}"><div class="veil"></div>${inner}${handle}${s.kind !== 'cover' ? dots : ''}</section>`;
};
const html = body => `<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="${css}"><style>
 body{margin:0;width:1080px;height:1350px;overflow:hidden;}
 section{position:relative;width:1080px;height:1350px;overflow:hidden;color:var(--burgundy);}
 .bg{position:absolute;left:0;top:-40px;width:1080px;height:1920px;object-fit:cover;}
 .veil{position:absolute;left:0;right:0;bottom:0;height:720px;
   background:linear-gradient(180deg,rgba(243,234,214,0) 0%,rgba(243,234,214,.88) 34%,rgba(243,234,214,.96) 100%);}
 .ar{font-family:'Amiri';font-weight:700;white-space:nowrap;} .hl{color:var(--terracotta);}
 .txt{position:absolute;left:80px;right:80px;bottom:150px;}
 .kick{font:800 25px 'Nunito Sans';letter-spacing:5px;text-transform:uppercase;color:#a35a3c;}
 h1{margin:14px 0 0;font:600 104px/0.98 'Cormorant Garamond';} h2{margin:12px 0 0;font:600 66px/1.05 'Cormorant Garamond';}
 p{margin:20px 0 0;font:600 32px/1.45 'Nunito Sans';color:#3d1a26;}
 .cov{text-align:center;} .cov .sub{margin-top:18px;font:italic 600 44px/1.2 'Cormorant Garamond';}
 .swipe{position:absolute;right:80px;bottom:70px;font:800 26px 'Nunito Sans';color:var(--burgundy);}
 .num{position:absolute;left:62px;top:44px;font:600 50px/1 'Cormorant Garamond';color:var(--cream);background:var(--burgundy);padding:8px 16px 12px;border-radius:12px;}
 .end{text-align:center;} .end .quote{font:italic 600 60px/1.12 'Cormorant Garamond';} .end .sub{margin-top:20px;font:700 28px 'Nunito Sans';}
 .end .cta{display:inline-block;margin-top:26px;font:800 28px 'Nunito Sans';color:var(--cream);background:var(--burgundy);padding:14px 30px;border-radius:14px;white-space:nowrap;}
 .handle{position:absolute;left:0;right:0;bottom:56px;text-align:center;font:800 23px 'Nunito Sans';letter-spacing:4px;color:var(--burgundy);} .handle span{color:var(--gold);}
 .dots{position:absolute;right:80px;bottom:64px;display:flex;gap:8px;} .dots i{width:10px;height:10px;border-radius:50%;background:rgba(76,33,48,.25);} .dots i.on{background:var(--burgundy);}
</style></head><body>${body}</body></html>`;
(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch(); const pg = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (let i = 0; i < slides.length; i++) {
    const hp = path.join(outDir, `slide_${i + 1}.html`); fs.writeFileSync(hp, html(page(slides[i], i)));
    await pg.goto('file://' + path.resolve(hp)); await pg.evaluate(() => document.fonts.ready);
    await pg.waitForFunction(() => [...document.images].every(im => im.complete));
    await pg.screenshot({ path: path.join(outDir, `Manosh_carousel_${String(i + 1).padStart(2, '0')}.png`) });
  }
  await browser.close(); console.log('slides', slides.length);
})();
