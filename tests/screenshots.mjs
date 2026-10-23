import pkg from "file:///C:/Users/miraa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.js";
const { chromium } = pkg;
const browser = await chromium.launch();
for (const [width, height] of [[1440, 900], [768, 1024], [390, 844]]) {
  const page = await browser.newPage({ viewport: { width, height } });
  await page.goto("http://127.0.0.1:8000/demo");
  await page.waitForTimeout(2000);
  await page.screenshot({ path: `C:/Users/miraa/AppData/Local/Temp/opencode/kandor-${width}.png`, fullPage: true });
  await page.close();
}
await browser.close();
console.log("screenshots done");