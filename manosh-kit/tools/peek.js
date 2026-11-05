const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ channel: 'chromium' }); const p = await b.newPage({ viewport: { width: 1200, height: 800 } });
  await p.goto(process.argv[2], { waitUntil: 'domcontentloaded', timeout: 45000 }); await p.waitForTimeout(3000);
  console.log('URL:', p.url()); console.log('TITLE:', await p.title());
  await p.screenshot({ path: process.argv[3] }); await b.close();
})();
