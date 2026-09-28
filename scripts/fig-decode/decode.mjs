// decode.mjs — extract every SYMBOL (component) from a Figma .fig (fig-kiwi) as SVG + manifest.
// Usage: node decode.mjs [path/to/canvas.fig] [outDir]
import fs from 'fs'; import path from 'path'; import zlib from 'zlib'; import * as fzstd from 'fzstd';
import { decodeBinarySchema, compileSchema } from 'kiwi-schema';

const FIG = process.argv[2] || path.resolve('../../fig/canvas.fig');
const OUT = process.argv[3] || path.resolve('..');
const SVG_DIR = path.join(OUT, 'svg');

// ---------- 1. container: "fig-kiwi" + uint32 version + [uint32 len + bytes]* ----------
const buf = fs.readFileSync(FIG);
if (buf.subarray(0, 8).toString() !== 'fig-kiwi') throw new Error('not a fig-kiwi file');
const version = buf.readUInt32LE(8);
let off = 12; const chunks = [];
while (off < buf.length) { const len = buf.readUInt32LE(off); off += 4; chunks.push(buf.subarray(off, off + len)); off += len; }
const inflate = (c) => {
  if (c[0] === 0x28 && c[1] === 0xb5 && c[2] === 0x2f && c[3] === 0xfd) return Buffer.from(fzstd.decompress(c));
  try { return zlib.inflateRawSync(c); } catch { return zlib.inflateSync(c); }
};
const schemaBytes = inflate(chunks[0]);
const msgBytes = inflate(chunks[1]);
const schema = decodeBinarySchema(new Uint8Array(schemaBytes));
const msg = compileSchema(schema).decodeMessage(new Uint8Array(msgBytes));

// ---------- 2. node tree ----------
const key = g => `${g.sessionID}:${g.localID}`;
const nodes = msg.nodeChanges;
const byId = new Map(nodes.map(n => [key(n.guid), n]));
const children = new Map();
for (const n of nodes) if (n.parentIndex) { const k = key(n.parentIndex.guid); if (!children.has(k)) children.set(k, []); children.get(k).push(n); }
// Figma orders siblings by parentIndex.position (fractional-index string); sort so z-order is right.
for (const arr of children.values()) arr.sort((a, b) => (a.parentIndex.position < b.parentIndex.position ? -1 : a.parentIndex.position > b.parentIndex.position ? 1 : 0));
const kids = n => children.get(key(n.guid)) || [];
const parentOf = n => n.parentIndex ? byId.get(key(n.parentIndex.guid)) : null;
const canvasOf = n => { let c = n; while (c) { if (c.type === 'CANVAS') return c; c = parentOf(c); } return null; };

// ---------- 3. geometry blob -> SVG path data ----------
// blob = sequence of [uint8 cmd][float32 LE coords...]; 0=Z 1=M(2) 2=L(2) 3=Q(4) 4=C(6)
const CMD = { 0: ['Z', 0], 1: ['M', 1], 2: ['L', 1], 3: ['Q', 2], 4: ['C', 3] };
const fmt = v => { const s = (Math.round(v * 1000) / 1000).toString(); return s === '-0' ? '0' : s; };
function blobToPath(idx, m) {
  const b = msg.blobs[idx].bytes; const dv = new DataView(b.buffer, b.byteOffset, b.byteLength);
  let i = 0; const out = [];
  while (i < b.length) {
    const c = CMD[b[i]]; if (!c) throw new Error(`unknown path cmd ${b[i]} in blob ${idx}`); i++;
    const parts = [c[0]];
    for (let p = 0; p < c[1]; p++) {
      const x = dv.getFloat32(i, true), y = dv.getFloat32(i + 4, true); i += 8;
      parts.push(fmt(m[0] * x + m[1] * y + m[2]), fmt(m[3] * x + m[4] * y + m[5]));
    }
    out.push(parts[0] + parts.slice(1).join(' '));
  }
  return out.join('');
}
// affine: [m00 m01 m02 m10 m11 m12]; x' = m00*x + m01*y + m02
const mul = (a, b) => [a[0] * b[0] + a[1] * b[3], a[0] * b[1] + a[1] * b[4], a[0] * b[2] + a[1] * b[5] + a[2],
                       a[3] * b[0] + a[4] * b[3], a[3] * b[1] + a[4] * b[4], a[3] * b[2] + a[4] * b[5] + a[5]];
const T = n => n.transform ? [n.transform.m00, n.transform.m01, n.transform.m02, n.transform.m10, n.transform.m11, n.transform.m12] : [1, 0, 0, 0, 1, 0];
const IDENT = [1, 0, 0, 0, 1, 0];

// ---------- 4. paints ----------
const hex = c => '#' + [c.r, c.g, c.b].map(v => Math.round(Math.max(0, Math.min(1, v)) * 255).toString(16).padStart(2, '0')).join('');
const lin = v => v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
const isDark = c => (0.2126 * lin(c.r) + 0.7152 * lin(c.g) + 0.0722 * lin(c.b)) < 0.05 && Math.max(c.r, c.g, c.b) < 0.32;
// returns {color, opacity} for the first visible solid paint, or null
function paint(paints) {
  const p = (paints || []).find(p => p.visible !== false && p.type === 'SOLID' && (p.opacity ?? 1) > 0);
  if (!p) { if ((paints || []).some(p => p.visible !== false && p.type !== 'SOLID')) stats.nonSolidPaints++; return null; }
  const a = (p.opacity ?? 1) * (p.color.a ?? 1);
  return { color: isDark(p.color) ? 'currentColor' : hex(p.color), opacity: a, raw: hex(p.color) };
}

// ---------- 5. render a symbol ----------
const stats = { symbols: 0, emptySvg: [], hiddenSkipped: 0, instancesInlined: 0, nonSolidPaints: 0, booleanNoGeometry: 0, unknownTypes: {}, colorsKept: {}, unresolvedInstances: [] };
function renderNode(n, m, out, depth, opacity) {
  if (n.visible === false) { stats.hiddenSkipped++; return; }
  const M = depth === 0 ? IDENT : mul(m, T(n));            // symbol's own transform (canvas position) is dropped
  const op = opacity * (n.opacity ?? 1);
  const emit = (geos, pnt) => {
    if (!geos || !geos.length || !pnt) return;
    for (const g of geos) {
      const d = blobToPath(g.commandsBlob, M); if (!d) continue;
      const a = op * pnt.opacity;
      out.push(`<path d="${d}" fill="${pnt.color}"${g.windingRule === 'ODD' ? ' fill-rule="evenodd"' : ''}${a < 1 ? ` fill-opacity="${fmt(a)}"` : ''}/>`);
      if (pnt.color !== 'currentColor') stats.colorsKept[pnt.color] = (stats.colorsKept[pnt.color] || 0) + 1;
    }
  };
  switch (n.type) {
    case 'SYMBOL': case 'FRAME': case 'GROUP':
      if (depth > 0) { emit(n.fillGeometry, paint(n.fillPaints)); emit(n.strokeGeometry, paint(n.strokePaints)); }
      for (const c of kids(n)) renderNode(c, M, out, depth + 1, op);
      break;
    case 'BOOLEAN_OPERATION':
      if ((n.fillGeometry?.length) || (n.strokeGeometry?.length)) { emit(n.fillGeometry, paint(n.fillPaints)); emit(n.strokeGeometry, paint(n.strokePaints)); }
      else { stats.booleanNoGeometry++; for (const c of kids(n)) renderNode(c, M, out, depth + 1, op); }
      break;
    case 'VECTOR': case 'ELLIPSE': case 'RECTANGLE': case 'ROUNDED_RECTANGLE': case 'STAR': case 'LINE': case 'REGULAR_POLYGON':
      emit(n.fillGeometry, paint(n.fillPaints)); emit(n.strokeGeometry, paint(n.strokePaints));
      break;
    case 'INSTANCE': {
      // inline the master symbol's children (overrides ignored; only 3 such nodes exist in this file)
      const master = n.symbolData?.symbolID && byId.get(key(n.symbolData.symbolID));
      if (master) { stats.instancesInlined++; for (const c of kids(master)) renderNode(c, M, out, depth + 1, op); }
      else stats.unresolvedInstances.push(n.name);
      break;
    }
    case 'TEXT': stats.unknownTypes.TEXT = (stats.unknownTypes.TEXT || 0) + 1; break; // no glyph outlines in file
    default: stats.unknownTypes[n.type] = (stats.unknownTypes[n.type] || 0) + 1;
  }
}
function symbolToSvg(sym) {
  const w = sym.size?.x ?? 24, h = sym.size?.y ?? 24; const out = [];
  renderNode(sym, IDENT, out, 0, 1);
  return { svg: `<svg xmlns="http://www.w3.org/2000/svg" width="${fmt(w)}" height="${fmt(h)}" viewBox="0 0 ${fmt(w)} ${fmt(h)}">\n${out.map(p => '  ' + p).join('\n')}\n</svg>\n`, paths: out.length, w, h };
}

// ---------- 6. collect symbols ----------
const safe = s => (s || '').toLowerCase().replace(/[\/]+/g, '-').replace(/\s+/g, '-').replace(/[^a-z0-9._=-]/g, '').replace(/-+/g, '-').replace(/^[-.]+|[-.]+$/g, '') || 'unnamed';
const stripHtml = s => s ? s.replace(/<[^>]+>/g, '').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').trim() : '';
const desc = n => n.symbolDescription || stripHtml(n.description) || '';
const canvases = nodes.filter(n => n.type === 'CANVAS');
const symbols = nodes.filter(n => n.type === 'SYMBOL');
const stateGroups = nodes.filter(n => n.isStateGroup);
const manifest = []; const used = new Set();
const variantProps = {};
for (const sym of symbols) {
  const parent = parentOf(sym); const canvas = canvasOf(sym);
  let set, variant, category = null, internal = false, dir;
  const props = {};
  if (parent?.isStateGroup) {
    set = parent.name; variant = sym.name; category = parentOf(parent)?.type === 'FRAME' ? parentOf(parent).name : null;
    for (const part of sym.name.split(',')) { const [k, v] = part.split('=').map(s => s?.trim()); if (k && v) { props[k] = v; (variantProps[k] ||= {})[v] = ((variantProps[k] ||= {})[v] || 0) + 1; } }
    dir = safe(set);
  } else if (canvas?.internalOnly && sym.name.includes('/') && sym.ancestorPathBeforeDeletion) {
    // deleted-from-library symbols kept in the "Internal Only Canvas": "<icon>/<Style>/<Type>"
    const segs = sym.name.split('/'); set = segs[0]; variant = segs.slice(1).join('/'); internal = true;
    if (segs.length === 3) { props.Style = segs[1]; props.Type = segs[2]; }
    const cat = sym.ancestorPathBeforeDeletion.map(g => byId.get(key(g))).find(a => a && a.type === 'FRAME' && !a.isStateGroup);
    category = cat?.name || null;
    dir = path.join('_internal', safe(set));
  } else {
    set = null; variant = sym.name; internal = !!canvas?.internalOnly; dir = '_standalone';
  }
  let base = safe(variant); let file = path.join(dir, base + '.svg'); let i = 2;
  while (used.has(file)) file = path.join(dir, `${base}-${key(sym.guid).replace(':', '_')}.svg`), i++;
  used.add(file);
  const { svg, paths, w, h } = symbolToSvg(sym);
  fs.mkdirSync(path.join(SVG_DIR, dir), { recursive: true });
  fs.writeFileSync(path.join(SVG_DIR, file), svg);
  stats.symbols++;
  if (paths === 0) stats.emptySvg.push({ file, name: sym.name, set });
  const entry = { set, variant, name: set || sym.name, width: w, height: h, file: 'svg/' + file.split(path.sep).join('/'), description: desc(sym) || (parent?.isStateGroup ? desc(parent) : '') };
  entry.category = category; entry.properties = props; entry.internal = internal; entry.paths = paths; entry.guid = key(sym.guid);
  if (sym.componentKey) entry.componentKey = sym.componentKey;
  manifest.push(entry);
}
manifest.sort((a, b) => (a.internal - b.internal) || (a.file < b.file ? -1 : 1));
fs.writeFileSync(path.join(OUT, 'manifest.json'), JSON.stringify(manifest, null, 1));

const summary = {
  figVersion: version, chunks: chunks.length, schemaBytes: schemaBytes.length, messageBytes: msgBytes.length,
  nodeChanges: nodes.length, blobs: msg.blobs.length,
  canvases: canvases.map(c => ({ name: c.name, internalOnly: !!c.internalOnly, topLevelChildren: kids(c).length, symbols: symbols.filter(s => canvasOf(s) === c).length })),
  nodeTypes: nodes.reduce((a, n) => (a[n.type] = (a[n.type] || 0) + 1, a), {}),
  componentSets: stateGroups.length, categoryFrames: [...new Set(stateGroups.map(g => parentOf(g)?.name))].length,
  setsWithDescription: stateGroups.filter(desc).length, symbolsWithOwnDescription: symbols.filter(desc).length,
  liveSymbols: manifest.filter(m => !m.internal && m.set).length, internalDeletedSymbols: manifest.filter(m => m.internal && m.set).length, standalone: manifest.filter(m => !m.set).length,
  variantProps, stats,
};
fs.writeFileSync(path.join(OUT, 'tools', 'summary.json'), JSON.stringify(summary, null, 1));
console.log(JSON.stringify(summary, null, 1));
