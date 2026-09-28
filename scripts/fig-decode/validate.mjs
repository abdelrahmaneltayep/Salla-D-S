import fs from 'fs'; import path from 'path'; import { XMLValidator } from 'fast-xml-parser';
const m = JSON.parse(fs.readFileSync('../manifest.json'));
let ok=0, bad=[], noPath=[], tinyPath=[]; const pathCounts={};
for (const e of m) {
  const s = fs.readFileSync(path.join('..', e.file), 'utf8');
  const v = XMLValidator.validate(s); if (v !== true) { bad.push([e.file, v.err?.msg]); continue; }
  const ds = [...s.matchAll(/ d="([^"]*)"/g)].map(x=>x[1]);
  if (!ds.length) noPath.push(e.file); else if (ds.every(d=>d.length<20)) tinyPath.push(e.file);
  ok++; pathCounts[ds.length]=(pathCounts[ds.length]||0)+1;
}
console.log(JSON.stringify({ total:m.length, wellFormed: ok, malformed: bad.slice(0,5), malformedCount: bad.length, noPath, tinyPath: tinyPath.slice(0,10), tinyCount: tinyPath.length, pathCounts }, null, 1));
