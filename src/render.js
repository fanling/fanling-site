const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const [,, inp, out, shots] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1056, height: 816 } });
  await p.goto('file://' + require('path').resolve(inp));
  await p.evaluate(() => document.fonts.ready);
  if (out) await p.pdf({ path: out, preferCSSPageSize: true, printBackground: true });
  if (shots) {
    const n = await p.$$eval('.pg', e => e.length);
    for (let i = 0; i < n; i++) { const el = (await p.$$('.pg'))[i]; await el.screenshot({ path: `${shots}/p${String(i+1).padStart(2,'0')}.png` }); }
  }
  await b.close();
})();
