// Render an animated Manosh hook (same layout as templates/hook_html.js) to a
// transparent PNG frame sequence. Animations are CSS; frames are captured by
// seeking every animation to t, so output is deterministic.
// Usage: node hook_anim.js <variant 1-10> "<line1>|<line2>|<line3>" <out_dir> [scale=1] [fps=30] [dur=2.2]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [variant, rawLines, outDir, scaleArg, fpsArg, durArg] = process.argv.slice(2);
const scale = Number(scaleArg || 1), fps = Number(fpsArg || 30), dur = Number(durArg || 2.2);
const css = 'file://' + path.resolve(__dirname, '../manosh/Manosh/templates/brand.css');
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const fmt = s => esc(s).replace(/\{\{gold\}\}/g, '<span class="hl">').replace(/\{\{\/gold\}\}/g, '</span>');
const lines = String(rawLines).split('|').map(s => s.trim()).filter(Boolean);
const stagger = ['one', 'two', 'three', 'four'];
const D0 = 0.15;                                   // hook start (s)
const bounce = 'cubic-bezier(.34,1.56,.64,1)';     // ease-out-back
const easeOut = 'cubic-bezier(.22,1,.36,1)';

// per-variant CSS; ${i} = line index for staggered delays
const V = {
  1: { name: 'Drop & settle', hook: `animation:drop .55s ${bounce} ${D0}s both, fade .28s linear ${D0}s both;` },
  2: { name: 'Stagger drop', row: i => `animation:dropS .5s ${bounce} ${D0 + i * .14}s both, fade .2s linear ${D0 + i * .14}s both;` },
  3: { name: 'Slide in', row: i => `animation:slideL .5s ${bounce} ${D0 + i * .12}s both;` },
  4: { name: 'Pop', row: i => `transform-origin:left center;animation:pop .42s ${bounce} ${D0 + i * .16}s both;` },
  5: { name: 'Type on', blk: (i, n) => `animation:type ${(n * .045).toFixed(2)}s steps(${n}) ${D0 + i * .5}s both;` },
  6: { name: 'Marker swipe', swipe: true },
  7: { name: 'Gold punch', row: i => `animation:fade .22s linear ${D0 + i * .08}s both;`, punch: true },
  8: { name: 'Focus pull', hook: `animation:focus .6s ${easeOut} ${D0}s both;` },
  9: { name: 'Band wipe', band: true },
  10: { name: 'Mask rise', mask: true },
}[variant];

let rows = lines.map((ln, i) => {
  const n = ln.replace(/\{\{\/?gold\}\}/g, '').length;
  const rowStyle = V.row ? V.row(i) : '';
  let blkStyle = V.blk ? V.blk(i, n) : '';
  let inner = fmt(ln);
  if (V.swipe) {
    const d = D0 + i * .22;
    return `<div class="row ${stagger[i]}"><span class="blk sw" style="--d:${d}s"><i class="bg"></i><span class="tx">${inner}</span></span></div>`;
  }
  if (V.mask) {
    const d = D0 + i * .11;
    return `<div class="row ${stagger[i]} mk"><span class="blk" style="animation:rise .5s ${easeOut} ${d}s both;">${inner}</span></div>`;
  }
  return `<div class="row ${stagger[i]}" style="${rowStyle}"><span class="blk" style="${blkStyle}">${inner}</span></div>`;
}).join('\n');

const last = D0 + (lines.length - 1) * .2 + .5;
const stripDelay = { 5: D0 + lines.length * .5, 6: D0 + lines.length * .22 + .2, 9: D0 + .45 }[variant] ?? last;
const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="${css}">
<style>
 body{width:1080px;height:1920px;position:relative;margin:0;overflow:hidden;}
 .hook{position:absolute;top:1040px;left:80px;right:80px;display:flex;flex-direction:column;align-items:flex-start;${V.hook || ''}}
 .row{display:flex;}
 .blk{position:relative;display:inline-block;font-family:'Nunito Sans';font-weight:800;color:var(--cream);font-size:76px;line-height:1.0;
   letter-spacing:-.5px;background:var(--burgundy);padding:14px 28px 16px;border-radius:12px;border:1.5px solid rgba(76,33,48,.14);}
 .blk .hl{color:var(--gold);display:inline-block;}
 .row + .row{margin-top:14px;} .row.two{margin-left:52px;} .row.three{margin-left:26px;} .row.four{margin-left:60px;}
 .strip{display:flex;align-items:center;gap:18px;margin-top:40px;margin-left:6px;animation:fade .35s linear ${stripDelay}s both;}
 .rule{width:64px;height:2px;background:rgba(201,162,100,.85);}
 .brand{font-family:'Nunito Sans';font-weight:700;color:var(--cream);font-size:26px;letter-spacing:2px;text-transform:uppercase;text-shadow:0 2px 6px rgba(0,0,0,.45);}
 /* marker swipe */
 .sw{background:none;border-color:transparent;} .sw .bg{position:absolute;inset:0;border-radius:12px;background:var(--burgundy);transform-origin:left center;
   animation:swipe .32s ${easeOut} var(--d) both;} .sw .tx{position:relative;animation:fade .2s linear calc(var(--d) + .16s) both;}
 /* mask rise */
 .mk{overflow:hidden;padding:0 0 2px;border-radius:12px;}
 /* band wipe */
 .band{position:absolute;top:1020px;left:0;width:1080px;height:420px;background:var(--burgundy);animation:bandIn .26s ${easeOut} ${D0}s both, bandOut .34s cubic-bezier(.64,0,.78,0) ${D0 + .36}s both;}
 .band:after{content:'';position:absolute;left:0;right:0;top:50%;height:2px;background:rgba(201,162,100,.85);}
 ${V.band ? `.hook{animation:fade .01s linear ${D0 + .3}s both;}` : ''}
 ${V.punch ? `.hl{animation:punch .5s ${bounce} ${D0 + .75}s both;}` : ''}
 @keyframes fade{from{opacity:0}to{opacity:1}}
 @keyframes drop{from{transform:translateY(-170px)}to{transform:none}}
 @keyframes dropS{from{transform:translateY(-64px)}to{transform:none}}
 @keyframes slideL{from{transform:translateX(-1100px)}to{transform:none}}
 @keyframes pop{0%{transform:scale(.3);opacity:0}60%{opacity:1}100%{transform:scale(1);opacity:1}}
 @keyframes type{from{clip-path:inset(0 100% 0 0 round 12px)}to{clip-path:inset(0 0 0 0 round 12px)}}
 @keyframes swipe{from{transform:scaleX(0)}to{transform:scaleX(1)}}
 @keyframes focus{from{opacity:0;filter:blur(22px);transform:scale(1.14)}to{opacity:1;filter:blur(0);transform:none}}
 @keyframes bandIn{from{transform:translateX(-101%)}to{transform:none}}
 @keyframes bandOut{from{transform:none}to{transform:translateX(101%)}}
 @keyframes rise{from{transform:translateY(105%)}to{transform:none}}
 @keyframes punch{0%{transform:scale(1);color:var(--cream)}45%{transform:scale(1.32);color:var(--gold)}100%{transform:scale(1);color:var(--gold)}}
</style></head><body>
${V.band ? '<div class="band"></div>' : ''}
<div class="hook">${rows}
<div class="strip"><span class="rule"></span><span class="brand">@mennatullah.mo</span></div></div></body></html>`;

(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const htmlPath = path.join(outDir, 'hook.html');
  fs.writeFileSync(htmlPath, html);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: scale });
  await page.goto('file://' + path.resolve(htmlPath));
  await page.evaluate(() => document.fonts.ready);
  const n = Math.round(dur * fps);
  for (let f = 0; f <= n; f++) {
    const ms = (f / fps) * 1000;
    await page.evaluate(ms => document.getAnimations().forEach(a => { a.pause(); a.currentTime = ms; }), ms);
    await page.screenshot({ path: path.join(outDir, `f_${String(f).padStart(4, '0')}.png`), omitBackground: true });
  }
  await browser.close();
  console.log(V.name, n + 1, 'frames');
})();
