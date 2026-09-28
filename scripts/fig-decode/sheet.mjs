import fs from 'fs'; import path from 'path'; import sharp from 'sharp';
const m = JSON.parse(fs.readFileSync('../manifest.json'));
const byFile = Object.fromEntries(m.map(e=>[e.file,e]));
const pick = [
 'svg/add-01/style=stroke-type=rounded.svg','svg/add-01/style=solid-type=rounded.svg',
 'svg/adobe-photoshop/style=stroke-type=rounded.svg','svg/adobe-photoshop/style=solid-type=rounded.svg',
 'svg/bubble-chat/style=stroke-type=rounded.svg','svg/bubble-chat/style=solid-type=rounded.svg',
 'svg/delivery-return-02/style=solid-type=rounded.svg','svg/time-schedule/style=solid-type=rounded.svg',
 'svg/transmission/style=stroke-type=rounded.svg','svg/disability-01/style=stroke-type=rounded.svg','svg/disability-01/style=solid-type=rounded.svg',
 'svg/maps-location-01/style=solid-type=rounded.svg','svg/wifi-disconnected-01/style=stroke-type=rounded.svg','svg/evil/style=stroke-type=rounded.svg',
 'svg/_internal/add-01/bulk-rounded.svg','svg/_internal/add-01/duotone-rounded.svg','svg/_internal/add-01/twotone-rounded.svg','svg/_internal/add-01/stroke-sharp.svg','svg/_internal/add-01/solid-sharp.svg',
 'svg/_internal/bubble-chat/bulk-rounded.svg','svg/_internal/bubble-chat/duotone-rounded.svg','svg/_internal/bubble-chat/twotone-rounded.svg',
 'svg/_standalone/tag.svg','svg/_standalone/star-square-3_121.svg','svg/_standalone/gitlab.svg','svg/_standalone/style=duotone-type=rounded.svg',
];
// plus random live ones
const live = m.filter(e=>!e.internal&&e.set); let seed=42; const rnd=()=>{seed=(seed*16807)%2147483647;return seed/2147483647;};
for (let i=0;i<22;i++) pick.push(live[Math.floor(rnd()*live.length)].file);
const CELL=96, COLS=8, PAD=8; const rows=Math.ceil(pick.length/COLS);
const comps=[]; const labels=[];
for (const [i,f] of pick.entries()) {
  const svg = fs.readFileSync(path.join('..',f),'utf8').replace('<svg ', '<svg color="#141b34" '); // currentColor -> dark navy
  const png = await sharp(Buffer.from(svg), {density: 72*CELL/24}).resize(CELL-2*PAD, CELL-2*PAD, {fit:'contain', background:{r:0,g:0,b:0,alpha:0}}).png().toBuffer();
  comps.push({input: png, left: (i%COLS)*CELL+PAD, top: Math.floor(i/COLS)*CELL+PAD});
  labels.push(`${i}: ${f} (${byFile[f].paths} paths)`);
}
// grid background
const grid = `<svg xmlns="http://www.w3.org/2000/svg" width="${COLS*CELL}" height="${rows*CELL}"><rect width="100%" height="100%" fill="#f4f4f5"/>${Array.from({length:COLS*rows},(_,i)=>`<rect x="${(i%COLS)*CELL+2}" y="${Math.floor(i/COLS)*CELL+2}" width="${CELL-4}" height="${CELL-4}" fill="#fff" stroke="#ddd"/><text x="${(i%COLS)*CELL+5}" y="${Math.floor(i/COLS)*CELL+12}" font-size="9" font-family="sans-serif" fill="#999">${i}</text>`).join('')}</svg>`;
await sharp(Buffer.from(grid)).composite(comps).png().toFile('contact-sheet.png');
// also a dark-background sheet for the white-fill check
const gridD = grid.replace('#f4f4f5','#1a1a1a').replace(/fill="#fff" stroke="#ddd"/g,'fill="#222" stroke="#444"');
const compsD=[]; for (const [i,f] of pick.entries()) { const svg = fs.readFileSync(path.join('..',f),'utf8').replace('<svg ', '<svg color="#ffffff" '); const png = await sharp(Buffer.from(svg), {density: 72*CELL/24}).resize(CELL-2*PAD, CELL-2*PAD, {fit:'contain', background:{r:0,g:0,b:0,alpha:0}}).png().toBuffer(); compsD.push({input:png, left:(i%COLS)*CELL+PAD, top:Math.floor(i/COLS)*CELL+PAD}); }
await sharp(Buffer.from(gridD)).composite(compsD).png().toFile('contact-sheet-dark.png');
fs.writeFileSync('contact-sheet-index.txt', labels.join('\n'));
console.log(labels.join('\n'));
