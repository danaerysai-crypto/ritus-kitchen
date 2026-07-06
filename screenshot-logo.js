const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  const filePath = 'file://' + path.resolve(__dirname, 'logo-regenerate.html');
  await page.setViewport({ width: 1200, height: 1200, deviceScaleFactor: 3 });
  await page.goto(filePath, { waitUntil: 'networkidle0', timeout: 30000 });
  await page.evaluateHandle('document.fonts.ready');
  await page.screenshot({ path: 'images/logo-ritus-kitchen-regenerated.png', fullPage: false });
  console.log('Created: images/logo-ritus-kitchen-regenerated.png');
  await browser.close();
})();
