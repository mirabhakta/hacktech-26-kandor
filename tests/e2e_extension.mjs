import pkg from "file:///C:/Users/miraa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.js";
const { chromium } = pkg;
import path from "node:path";

const EXT = "C:/Users/miraa/Downloads/hacktech-26-kandor/Frontend";
const userDataDir = "C:/Users/miraa/AppData/Local/Temp/opencode/kandor-e2e-profile2";

const context = await chromium.launchPersistentContext(userDataDir, {
  executablePath: "C:/Users/miraa/.cache/ms-playwright/chromium-1248/chrome-win64/chrome.exe",
  headless: false,
  args: [
    `--disable-extensions-except=${EXT}`,
    `--load-extension=${EXT}`,
    "--no-first-run",
    "--no-default-browser-check",
  ],
});

const page = await context.newPage();
page.on("console", (msg) => console.log("PAGE:", msg.text()));
context.on("page", (p) => console.log("NEW PAGE:", p.url()));
await page.goto("http://127.0.0.1:8000/demo");
await page.waitForTimeout(3000);
console.log("backgroundPages:", context.backgroundPages().map(p=>p.url()));
await page.waitForTimeout(9000);
const banner = await page.$("#hacktech-safety-banner");
console.log("banner present:", !!banner);
if (banner) {
  console.log("FALLBACK_USED:", (await page.evaluate(() => window.__kandorLastResult?.fallback_used)));
console.log(await banner.innerText());
}
await page.screenshot({ path: "C:/Users/miraa/AppData/Local/Temp/opencode/kandor-e2e.png", fullPage: true });
await context.close();
console.log("done");