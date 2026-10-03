const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const [,, file, out, w, scheme] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: +w, height: 900 }, colorScheme: scheme || 'light' });
  await p.goto('file://' + require('path').resolve(file)); await p.waitForTimeout(1500);
  const sw = await p.evaluate(() => document.documentElement.scrollWidth);
  console.log(file, 'scrollWidth', sw, 'viewport', w);
  await p.screenshot({ path: out, fullPage: true }); await b.close();
})();
