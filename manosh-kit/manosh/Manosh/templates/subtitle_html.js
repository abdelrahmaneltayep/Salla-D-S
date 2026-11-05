// Generate a spoken-word subtitle overlay HTML (1080x1920, transparent) —
// Manosh identity, Mannon layout.
// Structure borrowed from the Mannon brand (CapCut/podcast single solid
// highlight pill, bold dark text) recolored to Manosh: one short spoken chunk on
// a solid warm-GOLD pill with bold BURGUNDY text (Nunito Sans 700). Lower third,
// centered. Motion (pop/fade) is added at composite time in ffmpeg.
// Usage: node subtitle_html.js <out.html> "<text with {{gold}}word{{/gold}}>"
const fs = require('fs');
const path = require('path');
const [outPath, rawText] = process.argv.slice(2);
const cssHref = 'file://' + path.resolve(__dirname, 'brand.css');

const esc = s => String(s)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
// escape first, then re-enable the emphasis markers (terracotta on gold)
const text = esc(rawText)
  .replace(/\{\{gold\}\}/g, '<span class="hl">')
  .replace(/\{\{\/gold\}\}/g, '</span>')
  // Arabic runs (e.g. ﷺ) render in Amiri — Nunito Sans has no Arabic glyphs
  .replace(/[؀-ۿﭐ-﷿ﹰ-﻿]+(?:\s+[؀-ۿﭐ-﷿ﹰ-﻿]+)*/g, m => `<bdi class="ar" dir="rtl">${m}</bdi>`);

const html = `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="${cssHref}">
<style>
  /* SUBTITLE — one spoken chunk on a solid GOLD pill, bold BURGUNDY text.
     Lower third, centered. Transparent alpha render. */
  body{width:1080px;height:1920px;position:relative;margin:0;}
  .sub{position:absolute;top:1300px;left:70px;right:70px;
    display:flex;justify-content:center;text-align:center;}
  .cap{display:inline-block;max-width:820px;
    background:var(--cream);
    padding:14px 30px 16px;border-radius:14px;
    border:1.5px solid rgba(76,33,48,.14);}
  .cap .t{font-family:'Nunito Sans';font-weight:700;color:var(--burgundy);
    font-size:52px;line-height:1.16;letter-spacing:.2px;}
  .cap .t .hl{color:var(--terracotta);}
  .cap .t .ar{font-family:'Amiri';font-weight:700;font-size:.95em;}
</style></head>
<body>
  <div class="sub">
    <div class="cap"><span class="t">${text}</span></div>
  </div>
</body></html>`;

fs.writeFileSync(outPath, html);
console.log('wrote', outPath);
