import fs from 'fs'; import zlib from 'zlib'; import * as fzstd from 'fzstd';
import { decodeBinarySchema, compileSchema } from 'kiwi-schema';
const buf = fs.readFileSync('../../fig/canvas.fig');
let off = 12; const chunks=[];
while (off < buf.length) { const len = buf.readUInt32LE(off); off+=4; chunks.push(buf.subarray(off, off+len)); off+=len; }
const schema = decodeBinarySchema(new Uint8Array(zlib.inflateRawSync(chunks[0])));
const msg = compileSchema(schema).decodeMessage(new Uint8Array(Buffer.from(fzstd.decompress(chunks[1]))));
const key = g => `${g.sessionID}:${g.localID}`;
const byId = new Map(msg.nodeChanges.map(n=>[key(n.guid), n]));
const children = new Map(); for (const n of msg.nodeChanges) if (n.parentIndex) { const k=key(n.parentIndex.guid); if(!children.has(k)) children.set(k,[]); children.get(k).push(n); }
const dump=(n,d=0)=>{ console.log(' '.repeat(d*2)+n.type+' "'+n.name+'" vis='+n.visible+' size='+JSON.stringify(n.size)+' fg='+(n.fillGeometry||[]).length+' sg='+(n.strokeGeometry||[]).length+' t=['+[n.transform?.m00,n.transform?.m01,n.transform?.m02,n.transform?.m10,n.transform?.m11,n.transform?.m12].map(v=>+v?.toFixed(2)).join(',')+']'+(n.symbolData?' sym='+key(n.symbolData.symbolID):'')); for (const c of children.get(key(n.guid))||[]) dump(c,d+1); };
for (const setName of process.argv.slice(2)) { const sg = msg.nodeChanges.find(n=>n.isStateGroup&&n.name===setName); console.log('=== '+setName+' desc='+sg.symbolDescription); for (const s of children.get(key(sg.guid))) dump(s); }
