// [RECOVERY NOTE] Only the first 50 lines of the original hook_html.js (2836 bytes) were ever printed
// in the session (2026-10-05). The rest is missing; the full file is in the original Manosh.zip on the Mac.
// Generate a full-frame (1080x1920, transparent) opening HOOK card for the
// Mennatullah shorts — Manosh identity, Mannon layout.
// Structure borrowed from the Mannon brand (#فنجان-style staggered solid
// highlight blocks) but recolored to Manosh: warm-GOLD pills with bold BURGUNDY
// text (Nunito Sans 700), an aged-gold hairline strip + @mennatullah.mo beneath.
// Lower-middle. Rendered to PNG via render.js (alpha).
// Usage: node hook_html.js <out.html> "<line1>|<line2>|<line3>" ["<handle>"]
const fs = require('fs');
const path = require('path');
const [outPath, rawLines, handleArg] = process.argv.slice(2);
const cssHref = 'file://' + path.resolve(__dirname, 'brand.css');

const esc = s => String(s)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
// {{gold}}..{{/gold}} lets one word deepen to burgundy-on-gold emphasis.
const fmt = s => esc(s)
  .replace(/\{\{gold\}\}/g, '<span class="hl">')
  .replace(/\{\{\/gold\}\}/g, '</span>');

const lines = String(rawLines || '').split('|').map(s => s.trim()).filter(Boolean);
const handle = esc(handleArg || '@mennatullah.mo');
const stagger = ['one', 'two', 'three', 'four'];
const rows = lines.map((ln, i) =>
  `<div class="row ${stagger[i] || ''}"><span class="blk">${fmt(ln)}</span></div>`
).join('\n    ');

const html = `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="${cssHref}">
<style>
  /* HOOK — staggered solid GOLD blocks, bold BURGUNDY text. Lower-middle.
     Aged-gold hairline + brand strip beneath. Transparent alpha render. */
  body{width:1080px;height:1920px;position:relative;margin:0;}
  .hook{position:absolute;top:1040px;left:80px;right:80px;
    display:flex;flex-direction:column;align-items:flex-start;}
  .row{display:flex;}
  .blk{font-family:'Nunito Sans';font-weight:800;color:var(--cream);
    font-size:76px;line-height:1.0;letter-spacing:-.5px;text-transform:none;
    background:var(--burgundy);padding:14px 28px 16px;border-radius:12px;
    border:1.5px solid rgba(76,33,48,.14);}
  .blk .hl{color:var(--gold);}
  .row + .row{margin-top:14px;}
  .row.two{margin-left:52px;}
  .row.three{margin-left:26px;}
  .row.four{margin-left:60px;}
  /* aged-gold rule + wordmark handle strip */
  .strip{display:flex;align-items:center;gap:18px;margin-top:40px;margin-left:6px;}
  .rule{width:64px;height:2px;background:rgba(201,162,100,.85);}
  .brand{font-family:'Nunito Sans';font-weight:700;color:var(--cream);
    font-size:26px;letter-spacing:2px;text-transform:uppercase;
    text-shadow:0 2px 6px rgba(0,0,0,.45);}
