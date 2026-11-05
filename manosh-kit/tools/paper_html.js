// Render the inserted photo as a "paper" card at top-center (1080x1920, transparent).
// Usage: node paper_html.js <out.html> <style 1-5> <photo path> [title]
const fs = require('fs'), path = require('path');
const [out, style, photo, rawTitle] = process.argv.slice(2);
const title = String(rawTitle || '').replace(/&/g,'&amp;').replace(/</g,'&lt;');
const css = 'file://' + path.resolve(__dirname, '../manosh/Manosh/templates/brand.css');
const img = 'file://' + path.resolve(photo);
let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
function torn(amp = 1.4, n = 46) {           // jagged polygon in % units
  const p = [], j = () => (rnd() * amp).toFixed(2);
  for (let i = 0; i <= n; i++) p.push(`${(i * 100 / n).toFixed(2)}% ${j()}%`);
  for (let i = 0; i <= n; i++) p.push(`${(100 - j()).toFixed(2)}% ${(i * 100 / n).toFixed(2)}%`);
  for (let i = n; i >= 0; i--) p.push(`${(i * 100 / n).toFixed(2)}% ${(100 - j()).toFixed(2)}%`);
  for (let i = n; i >= 0; i--) p.push(`${j()}% ${(i * 100 / n).toFixed(2)}%`);
  return `polygon(${p.join(',')})`;
}
const grain = `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .3  0 0 0 0 .25  0 0 0 0 .2  0 0 0 .22 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")`;
const crumple = `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='600' height='600'><filter id='c'><feTurbulence type='fractalNoise' baseFrequency='.012' numOctaves='4' seed='3'/><feDiffuseLighting lighting-color='white' surfaceScale='2.2'><feDistantLight azimuth='45' elevation='55'/></feDiffuseLighting><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -.5 0 0 0 .5'/></filter><rect width='100%' height='100%' filter='url(%23c)'/></svg>")`;
const S = {
1: { // Polaroid + washi tape
 wrap: 'transform:rotate(-3deg);filter:drop-shadow(0 16px 22px rgba(30,15,20,.30));',
 card: `background:#fbf8f2;padding:22px 22px 18px;`,
 post: `<div class="t t1">${title}</div>`,
 extra: `<div class="tape" style="left:50%;top:-26px;transform:translateX(-50%) rotate(3deg);width:190px;height:52px;background:rgba(201,124,90,.62);"></div>` },
2: { // Torn paper sheet
 wrap: 'transform:rotate(2deg);filter:drop-shadow(0 14px 18px rgba(30,15,20,.28));',
 card: `background:var(--cream);padding:30px 34px 36px;clip-path:${torn(1.6)};`, extra: '',
 pre: `<div class="t t2">${title}</div>` },
3: { // Newspaper clipping
 wrap: 'transform:rotate(-2deg);filter:drop-shadow(0 12px 16px rgba(30,15,20,.25));',
 card: `background:#ece3cf;padding:30px 30px 26px;clip-path:${torn(1.1, 60)};`,
 pre: `<div class="rule"></div><div class="t t3">${title}</div><div class="rule thin"></div>`,
 post: `<div class="bars"><i style="width:96%"></i><i style="width:64%"></i></div>`,
 imgcss: 'filter:grayscale(.55) contrast(1.05) sepia(.18);' },
4: { // Scrapbook: crumpled paper + corner tapes
 wrap: 'transform:rotate(1.5deg);filter:drop-shadow(0 14px 20px rgba(30,15,20,.28));',
 card: `background:#f7f1e6;padding:18px 18px 14px;`, crumple: true,
 post: `<div class="t t4">${title}</div>`,
 extra: `<div class="tape" style="left:-34px;top:-8px;transform:rotate(-38deg);width:150px;height:44px;background:rgba(232,217,185,.85);"></div>
         <div class="tape" style="right:-34px;top:-8px;transform:rotate(38deg);width:150px;height:44px;background:rgba(232,217,185,.85);"></div>` },
5: { // Brand pinned card: cream + aged-gold hairline + burgundy pin
 wrap: 'transform:rotate(-1.5deg);filter:drop-shadow(0 10px 14px rgba(30,15,20,.22));',
 card: `background:var(--cream);padding:24px;outline:1.5px solid rgba(201,162,100,.9);outline-offset:-11px;`,
 extra: `<div class="pin"></div>`,
 post: `<div class="t5rule"></div><div class="t t5">${title}</div>` },
}[style];
const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="${css}">
<style>
 body{width:1080px;height:1920px;margin:0;position:relative;}
 .wrap{position:absolute;top:80px;left:50%;width:520px;margin-left:-260px;${S.wrap}}
 .card{position:relative;${S.card}}
 .card:after{content:'';position:absolute;inset:0;background:${S.crumple ? crumple + ',' : ''}${grain};pointer-events:none;mix-blend-mode:multiply;}
 .card img{display:block;width:100%;${S.imgcss || ''}}
 .tape{position:absolute;z-index:3;box-shadow:0 1px 2px rgba(0,0,0,.12);}
 .rule{height:4px;border-top:2px solid #4a4038;border-bottom:1px solid #4a4038;margin:0 0 14px;}
 .bars{margin:12px 0;}.bars i{display:block;height:9px;background:rgba(60,50,42,.35);margin:7px 0;border-radius:2px;}
 .t{font-family:'Nunito Sans';text-align:center;}
 .t1{font-weight:800;color:var(--burgundy);font-size:40px;padding:18px 0 4px;}
 .t2{font-weight:800;color:var(--burgundy);font-size:42px;padding:0 0 18px;}
 .t3{font-family:'Cormorant Garamond';font-weight:600;color:#2b241f;font-size:40px;line-height:1;text-transform:uppercase;letter-spacing:.5px;white-space:nowrap;padding:6px 0 4px;}
 .rule.thin{height:0;border-bottom:none;margin:8px 0 16px;}
 .t4{font-weight:800;color:var(--burgundy);font-size:38px;padding:14px 0 2px;}
 .t5rule{width:64px;height:2px;background:rgba(201,162,100,.9);margin:18px auto 10px;}
 .t5{font-weight:800;color:var(--burgundy);font-size:38px;padding:0 0 6px;}
 .pin{position:absolute;z-index:3;left:50%;top:-14px;width:34px;height:34px;margin-left:-17px;border-radius:50%;
   background:radial-gradient(circle at 35% 30%,#a5566c 0,#4C2130 55%,#2e1019 100%);box-shadow:0 4px 6px rgba(0,0,0,.35);}
</style></head><body><div class="wrap">${S.extra || ''}<div class="card">${S.pre || ''}<img src="${img}">${S.post || ''}</div></div></body></html>`;
fs.writeFileSync(out, html); console.log('wrote', out);
