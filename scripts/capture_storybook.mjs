// Render every story of a static Storybook build offline and capture markup, args/argTypes and a screenshot.
// usage: node scripts/capture_storybook.mjs storybook/static storybook/captures   (needs `npm i playwright`; uses the Chromium at /opt/pw-browsers/chromium or set CHROMIUM=path)
import fs from 'node:fs'; import path from 'node:path'; import http from 'node:http';
import { chromium } from 'playwright';
const [,, STATIC, OUT] = process.argv;
const MIME = { '.html':'text/html', '.js':'text/javascript', '.mjs':'text/javascript', '.css':'text/css', '.json':'application/json', '.svg':'image/svg+xml', '.woff2':'font/woff2', '.woff':'font/woff', '.png':'image/png', '.jpg':'image/jpeg', '.ttf':'font/ttf', '.map':'application/json' };
const server = http.createServer((req, res) => {
  const p = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  let f = path.join(STATIC, p === '/' ? 'index.html' : p);
  if (!fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'content-type': MIME[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
});
await new Promise(r => server.listen(0, '127.0.0.1', r));
const base = `http://127.0.0.1:${server.address().port}`;
const index = JSON.parse(fs.readFileSync(path.join(STATIC, 'index.json'), 'utf8'));
const stories = Object.values(index.entries).filter(e => e.type === 'story');
const slug = s => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const browser = await chromium.launch({ executablePath: process.env.CHROMIUM || "/opt/pw-browsers/chromium" });
const page = await browser.newPage({ viewport: { width: 1200, height: 800 } });
page.on('pageerror', e => {});
const results = [];
let i = 0;
for (const e of stories) {
  i++;
  const url = `${base}/iframe.html?id=${e.id}&viewMode=story`;
  const rec = { id: e.id, title: e.title, name: e.name, importPath: e.importPath };
  try {
    await page.goto(url, { waitUntil: 'load', timeout: 30000 });
    await page.waitForFunction(() => document.querySelector('#storybook-root') && document.querySelector('#storybook-root').children.length > 0, null, { timeout: 15000 }).catch(() => {});
    await page.waitForTimeout(600);
    const info = await page.evaluate(async (id) => {
      const out = {};
      try {
        const preview = window.__STORYBOOK_PREVIEW__;
        const story = await preview.storyStore.loadStory({ storyId: id });
        out.component = story.component?.name || story.parameters?.component || null;
        out.args = story.initialArgs;
        out.argTypes = Object.fromEntries(Object.entries(story.argTypes || {}).map(([k, v]) => [k, { name: v.name, description: v.description, type: v.type, control: v.control, options: v.options, table: v.table, defaultValue: v.defaultValue }]));
        out.description = story.parameters?.docs?.description || null;
        out.componentDescription = story.parameters?.docs?.description?.component || null;
        out.tags = story.tags;
      } catch (err) { out.storeError = String(err); }
      const root = document.querySelector('#storybook-root');
      out.html = root ? root.innerHTML : '';
      out.tags_used = [...new Set([...document.querySelectorAll('#storybook-root *')].map(n => n.tagName.toLowerCase()).filter(t => t.startsWith('s-')))];
      return out;
    }, e.id);
    Object.assign(rec, info);
    const dir = path.join(OUT, 'stories', slug(e.title.replace(/^Components\//, '')));
    fs.mkdirSync(dir, { recursive: true });
    const fileBase = path.join(dir, slug(e.name));
    fs.writeFileSync(fileBase + '.html', `<!-- ${e.title} / ${e.name} (${e.id}) -->\n${(info.html || '').trim()}\n`);
    try {
      const root = page.locator('#storybook-root');
      await root.screenshot({ path: fileBase + '.png', timeout: 10000 });
    } catch (err) { await page.screenshot({ path: fileBase + '.png' }).catch(() => {}); }
    rec.htmlFile = path.relative(OUT, fileBase + '.html'); rec.pngFile = path.relative(OUT, fileBase + '.png');
    delete rec.html;
  } catch (err) { rec.error = String(err); }
  results.push(rec);
  if (i % 25 === 0) console.log(`${i}/${stories.length}`);
}
await browser.close(); server.close();
fs.writeFileSync(path.join(OUT, 'stories.json'), JSON.stringify(results, null, 1));
console.log('done', results.length, 'errors', results.filter(r => r.error).length);
