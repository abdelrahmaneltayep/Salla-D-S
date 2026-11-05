// Render a 1080x1920 HTML card to a transparent PNG.
// Usage: node render.js <in.html> <out.png>
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [inp, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.resolve(inp));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(150);
  await page.screenshot({ path: out, omitBackground: true });
  await browser.close();
  console.log('rendered', out);
})();
