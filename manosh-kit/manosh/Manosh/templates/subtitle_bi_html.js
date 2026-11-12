// Bilingual subtitle overlay (1080x1920, transparent): English pill on top, Arabic pill directly below.
// Same Manosh look as subtitle_html.js (cream pill, burgundy text, {{gold}} -> terracotta).
// Usage: node subtitle_bi_html.js <out.html> "<english with {{gold}}..>" "<arabic with {{gold}}..>"
const fs = require('fs');
const path = require('path');
const [outPath, rawEn, rawAr] = process.argv.slice(2);
const cssHref = 'file://' + path.resolve(__dirname, 'brand.css');

const esc = s => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const gold = s => s.replace(/\{\{gold\}\}/g, '<span class="hl">').replace(/\{\{\/gold\}\}/g, '</span>');
const en = gold(esc(rawEn))
  .replace(/[؀-ۿﭐ-﷿ﹰ-﻿]+(?:\s+[؀-ۿﭐ-﷿ﹰ-﻿]+)*/g, m => `<bdi class="ar" dir="rtl">${m}</bdi>`);
const ar = gold(esc(rawAr));

const html = `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="${cssHref}">
<style>
  body{width:1080px;height:1920px;position:relative;margin:0;}
  .sub{position:absolute;top:1270px;left:60px;right:60px;
    display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center;}
  .cap{display:inline-block;max-width:880px;background:var(--cream);
    padding:12px 30px 14px;border-radius:14px;border:1.5px solid rgba(76,33,48,.14);}
  .en{font-family:'Nunito Sans';font-weight:700;color:var(--burgundy);font-size:50px;line-height:1.16;letter-spacing:.2px;}
  .en .ar{font-family:'Amiri';font-weight:700;font-size:.95em;}
  .arl{font-family:'IBM Plex Sans Arabic','Amiri';font-weight:700;color:var(--burgundy);font-size:46px;line-height:1.35;}
  .hl{color:var(--terracotta);}
</style></head>
<body>
  <div class="sub">
    <div class="cap"><span class="en">${en}</span></div>
    ${ar ? `<div class="cap" dir="rtl"><span class="arl">${ar}</span></div>` : ''}
  </div>
</body></html>`;
fs.writeFileSync(outPath, html);
console.log('wrote', outPath);
