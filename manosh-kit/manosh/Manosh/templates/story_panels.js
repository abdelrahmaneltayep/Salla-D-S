// Storyboard illustration panels, top centre, one per story scene (Manosh kit frame + label).
// Usage: node story_panels.js <scenes.json> <img_dir> <out_dir> <windows.json> [scale] [fps] [look]
// look 'card' (default): cream frame + label.  look 'old': no frame/label — parchment PNG (tools/parchment.py) with a slow fade.
// look 'fold': parchment sheet (tools/paper_scene.py, pN.png + paper back bN.png) that arrives folded in thirds,
//   unfolds (right flap, then left), drifts slowly, and folds back up before it leaves.
// look 'roll': the same sheet as a scroll — two paper rolls start at the centre and roll outward to open it,
//   roll back in to close it; soft gloss + one light glint across the paper after it opens.
// look 'rollR': one roll, no shine — unrolls from the RIGHT edge (travels right->left), rolls up from the LEFT (travels left->right).
// look 'rollL': one roll, no shine, NO shadow — unrolls from the LEFT edge (travels left->right), rolls up from the RIGHT (travels right->left).
// scenes.json: [{"start","end","img":"p1.png","label":"Her mahr: Islam"}]; windows.json: [[t0,t1],...] absolute times to render.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [scenesPath, imgDir, outDir, winPath, scaleArg, fpsArg, lookArg] = process.argv.slice(2);
const OLD = lookArg === 'old', FOLD = lookArg === 'fold', ROLL = lookArg === 'roll', ROLLR = lookArg === 'rollR', ROLLL = lookArg === 'rollL';
const scenes = JSON.parse(fs.readFileSync(scenesPath, 'utf8')), wins = JSON.parse(fs.readFileSync(winPath, 'utf8'));
const scale = Number(scaleArg || 1), fps = Number(fpsArg || 30);
const css = 'file://' + path.resolve(__dirname, 'brand.css');
const body = scenes.map(s => {
  const d = s.end - s.start;
  if (ROLLL) {
    const img = `file://${path.resolve(imgDir, s.img)}`, back = `file://${path.resolve(imgDir, s.img.replace(/^p/, 'b'))}`;
    const at = x => (s.start + x).toFixed(3), bt = x => (s.end - x).toFixed(3);
    return `<div class="rwrap" style="animation:okb ${d.toFixed(3)}s linear ${s.start}s both">
      <div class="sheet ns" style="background-image:url('${img}');animation:lO 1.2s linear ${at(0)}s both, lC 1.2s linear ${bt(1.2)}s forwards"></div>
      <div class="roll ns" style="background-image:var(--shade),url('${back}');animation:l1O 1.2s linear ${at(0)}s both, l1C 1.2s linear ${bt(1.2)}s forwards"></div></div>`;
  }
  if (ROLLR) {
    const img = `file://${path.resolve(imgDir, s.img)}`, back = `file://${path.resolve(imgDir, s.img.replace(/^p/, 'b'))}`;
    const at = x => (s.start + x).toFixed(3), bt = x => (s.end - x).toFixed(3);
    return `<div class="rwrap" style="animation:okb ${d.toFixed(3)}s linear ${s.start}s both">
      <div class="sheet" style="background-image:url('${img}');animation:rO 1.2s linear ${at(0)}s both, rC 1.2s linear ${bt(1.2)}s forwards"></div>
      <div class="roll" style="background-image:var(--shade),url('${back}');animation:r1O 1.2s linear ${at(0)}s both, r1C 1.2s linear ${bt(1.2)}s forwards"></div></div>`;
  }
  if (ROLL) {
    const img = `file://${path.resolve(imgDir, s.img)}`, back = `file://${path.resolve(imgDir, s.img.replace(/^p/, 'b'))}`;
    const at = x => (s.start + x).toFixed(3), bt = x => (s.end - x).toFixed(3);
    const roll = side => `<div class="roll ${side}" style="background-image:var(--shade),url('${back}');
      animation:${side}O 1.1s linear ${at(0)}s both, ${side}C 1.15s linear ${bt(1.15)}s forwards"></div>`;
    return `<div class="rwrap" style="animation:okb ${d.toFixed(3)}s linear ${s.start}s both">
      <div class="sheet" style="background-image:url('${img}');animation:sO 1.1s linear ${at(0)}s both, sC 1.15s linear ${bt(1.15)}s forwards">
        <i class="gloss" style="-webkit-mask-image:url('${img}')"></i>
        <i class="glint" style="-webkit-mask-image:url('${img}');animation:glint 1.4s ease-in-out ${at(1.15)}s both"></i>
      </div>${roll('L')}${roll('R')}</div>`;
  }
  if (FOLD) {
    const front = `url('file://${path.resolve(imgDir, s.img)}')`, back = `url('file://${path.resolve(imgDir, s.img.replace(/^p/, 'b'))}')`;
    const at = x => (s.start + x).toFixed(3), bt = x => (s.end - x).toFixed(3);
    const face = (pos, bg, cls = '', sh = '') => `<div class="face ${cls}" style="background-image:${bg};background-position:${pos} 0"><i class="sh" style="${sh};-webkit-mask-image:${bg};-webkit-mask-size:300% 100%;-webkit-mask-position:${pos} 0;-webkit-mask-repeat:no-repeat"></i></div>`;
    const shade = (o, c) => `animation:shOpen .55s ease-in ${at(o)}s both, shClose .5s ease-out ${bt(c)}s forwards`;
    return `<div class="fwrap" style="animation:okb ${d.toFixed(3)}s linear ${s.start}s both">
     <div class="fold" style="animation:fin .3s ease-out ${at(0)}s both, fout .3s ease-in ${bt(.3)}s forwards">
      <div class="third mid">${face('50%', front)}</div>
      <div class="third left" style="animation:openL .55s cubic-bezier(.45,0,.25,1) ${at(.62)}s both, closeL .5s cubic-bezier(.6,0,.4,1) ${bt(1.25)}s forwards">
        ${face('0%', front, 'f', shade(.62, 1.25))}${face('100%', back, 'b', shade(.62, 1.25))}</div>
      <div class="third right" style="animation:openR .55s cubic-bezier(.45,0,.25,1) ${at(.22)}s both, closeR .5s cubic-bezier(.6,0,.4,1) ${bt(.8)}s forwards">
        ${face('100%', front, 'f', shade(.22, .8))}${face('0%', back, 'b', shade(.22, .8))}</div>
     </div></div>`;
  }
  if (OLD) return `<div class="old" style="animation:oin .9s ease-out ${s.start}s both, oout .6s ease-in ${(s.end - .6).toFixed(3)}s forwards">
    <img src="file://${path.resolve(imgDir, s.img)}" style="animation:okb ${d.toFixed(3)}s linear ${s.start}s both"></div>`;
  return `<div class="card" style="animation:cin .6s linear ${s.start}s both, cout .35s ease-in ${(s.end - .35).toFixed(3)}s forwards">
    <div class="pic"><img src="file://${path.resolve(imgDir, s.img)}" style="animation:kb ${d.toFixed(3)}s linear ${s.start}s both"></div>
    <div class="lab">${s.label}</div></div>`;
}).join('\n');
const html = `<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="${css}"><style>
 body{width:1080px;height:1920px;margin:0;position:relative;overflow:hidden;}
 .card{position:absolute;left:220px;top:56px;width:640px;opacity:0;transform-origin:50% 0;}
 .pic{width:640px;height:360px;border-radius:26px;overflow:hidden;border:8px solid var(--cream);box-sizing:border-box;
   box-shadow:0 10px 30px rgba(76,33,48,.28);background:var(--cream);}
 .pic img{width:100%;height:100%;object-fit:cover;transform-origin:50% 45%;}
 .lab{position:absolute;left:50%;top:330px;translate:-50% 0;white-space:nowrap;font:italic 700 50px/1 'Cormorant Garamond';color:var(--cream);
   background:var(--burgundy);padding:8px 24px 12px;border-radius:14px;box-shadow:0 4px 14px rgba(76,33,48,.25);}
 @keyframes cin{0%{opacity:0;transform:translateY(-40px) scale(.92);animation-timing-function:cubic-bezier(.22,1,.36,1)}
   60%{opacity:1;transform:scale(1.02);animation-timing-function:ease-in-out}100%{opacity:1;transform:none}}
 @keyframes cout{from{opacity:1;transform:none}to{opacity:0;transform:translateY(-24px) scale(.96)}}
 .old{position:absolute;left:170px;top:40px;width:740px;opacity:0;}
 .old img{width:100%;display:block;transform-origin:50% 50%;filter:drop-shadow(0 6px 12px rgba(40,25,15,.28));}
 @keyframes oin{from{opacity:0;transform:translateY(-14px) scale(.97)}to{opacity:1;transform:none}}
 @keyframes oout{from{opacity:1}to{opacity:0}}
 @keyframes okb{from{transform:scale(1)}to{transform:scale(1.04)}}
 /* roll (scroll) look: stage 760x471; rolls 56px wide, centre x = 380 */
 .rwrap{position:absolute;left:160px;top:36px;width:760px;height:471px;transform-origin:50% 50%;}
 .sheet{position:absolute;inset:0;background-size:100% 100%;isolation:isolate;filter:drop-shadow(0 8px 14px rgba(40,25,15,.3));}
 .gloss,.glint{position:absolute;inset:0;-webkit-mask-size:100% 100%;mix-blend-mode:screen;}
 .gloss{background:radial-gradient(ellipse 70% 60% at 32% 24%,rgba(255,248,228,.38),rgba(255,248,228,0) 70%),
   linear-gradient(160deg,rgba(255,250,235,.10),rgba(255,250,235,0) 45%);}
 .glint{background:linear-gradient(110deg,rgba(255,255,255,0) 40%,rgba(255,250,232,.72) 50%,rgba(255,255,255,0) 60%);background-size:260% 100%;}
 @keyframes glint{from{background-position:115% 0}to{background-position:-15% 0}}
 .roll{--shade:linear-gradient(90deg,rgba(45,25,10,.78) 0%,rgba(120,80,40,.18) 20%,rgba(255,246,222,.62) 40%,rgba(170,120,70,.12) 62%,rgba(45,25,10,.8) 100%);
   position:absolute;left:0;top:2%;width:56px;height:96%;border-radius:28px/12px;background-size:100% 100%,420px 100%;
   box-shadow:0 6px 12px rgba(40,25,15,.38);opacity:0;}
 @keyframes sO{0%,18%{clip-path:inset(-6% 50% -6% 50%);animation-timing-function:cubic-bezier(.45,0,.3,1)}92%,100%{clip-path:inset(-6% 0 -6% 0)}}
 @keyframes sC{0%,8%{clip-path:inset(-6% 0 -6% 0);animation-timing-function:cubic-bezier(.5,0,.4,1)}75%,100%{clip-path:inset(-6% 50% -6% 50%)}}
 @keyframes LO{0%{opacity:0;transform:translateX(324px) scaleY(.88)}18%{opacity:1;transform:translateX(324px);background-position:0 0,0 0;animation-timing-function:cubic-bezier(.45,0,.3,1)}
   92%{opacity:1;transform:translateX(-28px) scaleX(.16);background-position:0 0,420px 0}100%{opacity:0;transform:translateX(-28px) scaleX(.1)}}
 @keyframes RO{0%{opacity:0;transform:translateX(380px) scaleY(.88)}18%{opacity:1;transform:translateX(380px);background-position:0 0,0 0;animation-timing-function:cubic-bezier(.45,0,.3,1)}
   92%{opacity:1;transform:translateX(732px) scaleX(.16);background-position:0 0,-420px 0}100%{opacity:0;transform:translateX(732px) scaleX(.1)}}
 @keyframes LC{0%{opacity:0;transform:translateX(-28px) scaleX(.1)}8%{opacity:1;transform:translateX(-28px) scaleX(.16);background-position:0 0,420px 0;animation-timing-function:cubic-bezier(.5,0,.4,1)}
   75%{opacity:1;transform:translateX(324px);background-position:0 0,0 0}100%{opacity:0;transform:translateX(324px) scaleY(.88)}}
 @keyframes RC{0%{opacity:0;transform:translateX(732px) scaleX(.1)}8%{opacity:1;transform:translateX(732px) scaleX(.16);background-position:0 0,-420px 0;animation-timing-function:cubic-bezier(.5,0,.4,1)}
   75%{opacity:1;transform:translateX(380px);background-position:0 0,0 0}100%{opacity:0;transform:translateX(380px) scaleY(.88)}}
 /* rollR: single roll; open = reveal right->left, close = hide left->right */
 @keyframes rO{0%,12%{clip-path:inset(-6% 0 -6% 100%);animation-timing-function:cubic-bezier(.45,0,.3,1)}92%,100%{clip-path:inset(-6% 0 -6% 0)}}
 @keyframes rC{0%,8%{clip-path:inset(-6% 0 -6% 0);animation-timing-function:cubic-bezier(.5,0,.4,1)}88%,100%{clip-path:inset(-6% 0 -6% 100%)}}
 @keyframes r1O{0%{opacity:0;transform:translateX(732px) scaleY(.88)}12%{opacity:1;transform:translateX(732px);background-position:0 0,0 0;animation-timing-function:cubic-bezier(.45,0,.3,1)}
   92%{opacity:1;transform:translateX(-28px) scaleX(.2);background-position:0 0,640px 0}100%{opacity:0;transform:translateX(-28px) scaleX(.12)}}
 @keyframes r1C{0%{opacity:0;transform:translateX(-28px) scaleX(.12)}8%{opacity:1;transform:translateX(-28px) scaleX(.2);background-position:0 0,0 0;animation-timing-function:cubic-bezier(.5,0,.4,1)}
   88%{opacity:1;transform:translateX(732px);background-position:0 0,-640px 0}100%{opacity:0;transform:translateX(732px) scaleY(.88)}}
 /* rollL: single roll, no shadow; open = reveal left->right, close = hide right->left */
 .sheet.ns{filter:none;} .roll.ns{box-shadow:none;}
 @keyframes lO{0%,12%{clip-path:inset(-6% 100% -6% 0);animation-timing-function:cubic-bezier(.45,0,.3,1)}92%,100%{clip-path:inset(-6% 0 -6% 0)}}
 @keyframes lC{0%,8%{clip-path:inset(-6% 0 -6% 0);animation-timing-function:cubic-bezier(.5,0,.4,1)}88%,100%{clip-path:inset(-6% 100% -6% 0)}}
 @keyframes l1O{0%{opacity:0;transform:translateX(-28px) scaleY(.88)}12%{opacity:1;transform:translateX(-28px);background-position:0 0,0 0;animation-timing-function:cubic-bezier(.45,0,.3,1)}
   92%{opacity:1;transform:translateX(732px) scaleX(.2);background-position:0 0,-640px 0}100%{opacity:0;transform:translateX(732px) scaleX(.12)}}
 @keyframes l1C{0%{opacity:0;transform:translateX(732px) scaleX(.12)}8%{opacity:1;transform:translateX(732px) scaleX(.2);background-position:0 0,0 0;animation-timing-function:cubic-bezier(.5,0,.4,1)}
   88%{opacity:1;transform:translateX(-28px);background-position:0 0,640px 0}100%{opacity:0;transform:translateX(-28px) scaleY(.88)}}
 .fwrap{position:absolute;left:160px;top:36px;width:760px;height:471px;transform-origin:50% 50%;}
 .fold{position:absolute;inset:0;perspective:1800px;transform-style:preserve-3d;opacity:0;filter:drop-shadow(0 8px 14px rgba(40,25,15,.3));}
 .third{position:absolute;top:0;width:33.334%;height:100%;transform-style:preserve-3d;}
 .third.mid{left:33.333%;} .third.left{left:0;transform-origin:100% 50%;} .third.right{left:66.666%;transform-origin:0 50%;}
 .face{position:absolute;inset:0;background-size:300% 100%;background-repeat:no-repeat;backface-visibility:hidden;}
 .face.b{transform:rotateY(180deg);}
 .sh{position:absolute;inset:0;background:linear-gradient(90deg,rgba(40,22,10,.0),rgba(40,22,10,.35));opacity:0;}
 .left .sh{background:linear-gradient(270deg,rgba(40,22,10,.0),rgba(40,22,10,.35));}
 @keyframes shOpen{from{opacity:.9}to{opacity:0}} @keyframes shClose{from{opacity:0}to{opacity:.9}}
 @keyframes fin{from{opacity:0;transform:translateY(-24px) scale(.94)}to{opacity:1;transform:none}}
 @keyframes fout{from{opacity:1;transform:none}to{opacity:0;transform:translateY(-16px) scale(.95)}}
 @keyframes openL{from{transform:rotateY(178deg)}to{transform:rotateY(0)}}
 @keyframes closeL{from{transform:rotateY(0)}to{transform:rotateY(178deg)}}
 @keyframes openR{from{transform:translateZ(1px) rotateY(-176deg)}to{transform:rotateY(0)}}
 @keyframes closeR{from{transform:rotateY(0)}to{transform:translateZ(1px) rotateY(-176deg)}}
 @keyframes kb{from{transform:scale(1)}to{transform:scale(1.08)}}
</style></head><body>${body}</body></html>`;
(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const hp = path.join(outDir, 'panels.html'); fs.writeFileSync(hp, html);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: scale });
  await page.goto('file://' + path.resolve(hp)); await page.evaluate(() => document.fonts.ready);
  await page.waitForFunction(() => [...document.images].every(i => i.complete));
  let k = 0;
  for (const [t0, t1] of wins) {
    const n = Math.round((t1 - t0) * fps);
    for (let f = 0; f < n; f++) {
      await page.evaluate(ms => document.getAnimations().forEach(a => { a.pause(); a.currentTime = ms; }), (t0 + f / fps) * 1000);
      await page.screenshot({ path: path.join(outDir, `f_${String(k++).padStart(5, '0')}.png`), omitBackground: true });
    }
  }
  await browser.close(); console.log('panels', k, 'frames');
})();
