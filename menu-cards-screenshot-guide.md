# Ritu's Kitchen — How to Screenshot Menu Cards for Google / Instagram

Created 3 ready-to-render menu cards:

| File | Size | Best For |
|------|------|----------|
| `menu-card-instagram.html` | 1080 × 1080 | Instagram feed post, WhatsApp status, Google Business Profile photo |
| `menu-card-story.html` | 1080 × 1920 | Instagram Stories, Reels cover, WhatsApp status |
| `menu-card-google.html` | 1200 × 900 | Google Business Profile "Menu" photo, website banner, flyer |

---

## Method 1: Screenshot from Browser (Easiest)

1. Open any of the HTML files in Chrome
2. Press **F11** for full screen
3. Zoom to fit:
   - **Instagram card (1080×1080):** zoom out until whole card visible (usually 75% or 67%)
   - **Story card (1080×1920):** zoom out until full card visible (usually 50%)
   - **Google card (1200×900):** zoom to 75% or 80%
4. Screenshot the card area using Windows Snipping Tool or Snip & Sketch
5. Save as **PNG**

---

## Method 2: High-Quality PNG via Puppeteer

### Step 1: Install Puppeteer globally

```bash
npm install -g puppeteer
```

### Step 2: Run screenshot script

Save this as `screenshot-menu.js` in the `ritus-kitchen/` folder:

```javascript
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
    await page.setViewport({ width: card.width, height: card.height });
    await page.goto(filePath, { waitUntil: 'networkidle0' });
    await page.screenshot({ path: card.name, fullPage: false });
    console.log('Created:', card.name);
  }

  await browser.close();
})();
```

### Step 3: Run it

```bash
cd /c/Users/Admin/Desktop/projects/ritus-kitchen
node screenshot-menu.js
```

This creates 3 PNGs:
- `ritus-kitchen-menu-instagram.png`
- `ritus-kitchen-menu-story.png`
- `ritus-kitchen-menu-google.png`

---

## Where to Upload

| Platform | Upload Which File | Where |
|----------|-------------------|-------|
| **Google Business Profile** | `ritus-kitchen-menu-google.png` | Photos → Add photos → Menu / Products |
| **Instagram Feed** | `ritus-kitchen-menu-instagram.png` | New post |
| **Instagram Story** | `ritus-kitchen-menu-story.png` | New story |
| **WhatsApp Status** | Either story or instagram |
| **Website banner** | `ritus-kitchen-menu-google.png` | Can be added to `index.html` |
| **Printed flyer** | `ritus-kitchen-menu-google.png` | Highest resolution |

---

## Pro Tips

- Google Business Profile photos should be **720 × 720 px minimum**, ideally **1080 × 1080 px or larger**
- Instagram feed: **1080 × 1080**
- Instagram story: **1080 × 1920**
- Use PNG for sharpest text, JPG for smaller file size
- Keep text large enough to read on a phone screen

---

## Want Me to Generate the PNGs?

I can install Puppeteer and run the screenshot script. This takes ~2 minutes.

**Say "generate PNGs"** and I'll do it.
