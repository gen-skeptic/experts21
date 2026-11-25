// Render assets/readme-banner.png (the README banner) from the Dautel Design System, in the same layout as gen-skeptic/experts.
// Usage: node tools/banner/render.js   (needs Playwright with Chromium)
const fs = require('fs'), path = require('path'), os = require('os');
const { chromium } = require('playwright');
const repo = path.resolve(__dirname, '..', '..');
const ds = path.join(repo, 'design-system');
(async () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'dio-banner-'));
  // Drop the Google Fonts @import so rendering uses the bundled web fonts offline.
  fs.writeFileSync(path.join(tmp, 'dautel.css'), fs.readFileSync(path.join(ds, 'dautel.css'), 'utf8').replace(/^@import.*$/m, ''));
  const html = fs.readFileSync(path.join(__dirname, 'banner.html'), 'utf8').replaceAll('{{DS}}', 'file://' + ds);
  fs.writeFileSync(path.join(tmp, 'banner.html'), html);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 420 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(tmp, 'banner.html'));
  await p.waitForTimeout(800);
  await p.screenshot({ path: path.join(repo, 'assets', 'readme-banner.png'), clip: { x: 0, y: 0, width: 1280, height: 420 } });
  await b.close();
  console.log('Wrote assets/readme-banner.png');
})();
