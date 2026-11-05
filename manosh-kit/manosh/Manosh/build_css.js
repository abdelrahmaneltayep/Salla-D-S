// The remainder (closing the CSS string and writing brand.css + templates/brand.css) is missing.
// Build brand.css with base64-embedded woff2 fonts (bulletproof for headless render).
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const F = f => path.join(root, 'node_modules/@fontsource', f);

const faces = [
  ['Aref Ruqaa', 700, 'aref-ruqaa/files/aref-ruqaa-arabic-700-normal.woff2'],
  ['Reem Kufi', 700, 'reem-kufi/files/reem-kufi-arabic-700-normal.woff2'],
  ['Amiri', 700, 'amiri/files/amiri-arabic-700-normal.woff2'],
  ['Amiri', 400, 'amiri/files/amiri-latin-400-normal.woff2'],
  ['IBM Plex Sans Arabic', 400, 'ibm-plex-sans-arabic/files/ibm-plex-sans-arabic-arabic-400-normal.woff2'],
  ['IBM Plex Sans Arabic', 700, 'ibm-plex-sans-arabic/files/ibm-plex-sans-arabic-arabic-700-normal.woff2'],
  ['Nunito Sans', 600, 'nunito-sans/files/nunito-sans-latin-600-normal.woff2'],
  ['Nunito Sans', 700, 'nunito-sans/files/nunito-sans-latin-700-normal.woff2'],
  ['Cormorant Garamond', 600, 'cormorant-garamond/files/cormorant-garamond-latin-600-normal.woff2'],
];

let css = '/* Mennatullah brand fonts — base64 embedded woff2 */\n';
for (const [fam, wt, rel] of faces) {
  const b64 = fs.readFileSync(F(rel)).toString('base64');
  css += `@font-face{font-family:'${fam}';font-weight:${wt};font-style:normal;`
       + `font-display:block;src:url(data:font/woff2;base64,${b64}) format('woff2');}\n`;
}
css += `
:root{
  --burgundy:#4C2130; --cream:#F3ECDF; --terracotta:#C97C5A;
  --gold:#C9A264; --teal:#3B837E; --blush:#E8C9B4;
}
*{margin:0;padding:0;box-sizing:border-box;}
`;
// [RESTORED 2026-11-05] tail rewritten after recovery: write the stylesheet for the kit root and templates/.
fs.writeFileSync(path.join(__dirname, 'brand.css'), css);
fs.writeFileSync(path.join(__dirname, 'templates', 'brand.css'), css);
console.log('brand.css', css.length, 'bytes');
