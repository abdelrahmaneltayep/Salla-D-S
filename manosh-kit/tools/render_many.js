// Render many 1080x1920 HTML cards to transparent PNGs at a device scale factor.
// Usage: node render_many.js <scale> <in1.html> <out1.png> [<in2.html> <out2.png> ...]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [scale, ...pairs] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: Number(scale) });
  for (let i = 0; i < pairs.length; i += 2) {
    await page.goto('file://' + path.resolve(pairs[i]));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(80);
    await page.screenshot({ path: pairs[i + 1], omitBackground: true });
  }
  await browser.close();
  console.log('rendered', pairs.length / 2);
})();
