const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const cards = [
  { file: 'menu-card-instagram.html', name: 'ritus-kitchen-menu-instagram.png', width: 1080, height: 1080 },
  { file: 'menu-card-story.html', name: 'ritus-kitchen-menu-story.png', width: 1080, height: 1920 },
  { file: 'menu-card-google.html', name: 'ritus-kitchen-menu-google.png', width: 1200, height: 900 },
];

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();

  for (const card of cards) {
    const filePath = 'file://' + path.resolve(__dirname, card.file);
    await page.setViewport({ width: card.width, height: card.height, deviceScaleFactor: 2 });
    await page.goto(filePath, { waitUntil: 'networkidle0', timeout: 30000 });
    // Wait for fonts
    await page.evaluateHandle('document.fonts.ready');
    await page.screenshot({ path: card.name, fullPage: false });
    console.log('Created:', card.name);
  }

  await browser.close();
})();
