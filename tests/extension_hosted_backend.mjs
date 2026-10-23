import pkg from "file:///C:/Users/miraa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.js";
const { chromium } = pkg;
import fs from "node:fs";

const EXT = "C:/Users/miraa/Downloads/hacktech-26-kandor/Frontend";
const userDataDir = "C:/Users/miraa/AppData/Local/Temp/opencode/kandor-hosted-profile";
// clean profile
fs.rmSync(userDataDir, { recursive: true, force: true });

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

// Wait for service worker and point extension at hosted backend.
let sw = null;
for (let i = 0; i < 50; i++) {
  const workers = context.serviceWorkers();
  if (workers.length) { sw = workers[0]; break; }
  await new Promise(r => setTimeout(r, 200));
}
if (!sw) throw new Error("No service worker");
await sw.evaluate(async () => {
  await chrome.storage.sync.set({
    hacktechSafetySettings: {
      enabled: true,
      backendBaseUrl: "https://kandor-backend.onrender.com",
      scanIntervalMinutes: 1,
      warningThreshold: 40,
    },
  });
});
console.log("Service worker:", sw.url());

const page = await context.newPage();
page.on("console", m => console.log("PAGE:", m.text()));
if (sw) sw.on("console", m => console.log("SW:", m.text()));
await page.goto("http://127.0.0.1:8000/demo");
await page.waitForTimeout(12000);
const banner = await page.$("#hacktech-safety-banner");
console.log("banner present:", !!banner);
if (banner) console.log(await banner.innerText());

// popup status check
const popup = await context.newPage();
// find extension id from service worker url
const extId = sw.url().match(/chrome-extension:\/\/([^/]+)/)?.[1];
console.log("extId:", extId);
await popup.goto(`chrome-extension://${extId}/popup.html`);
await popup.waitForTimeout(3000);
console.log("popup result pill:", await popup.textContent("#resultPill"));
const stored = await sw.evaluate(async () => chrome.storage.local.get("hacktechSafetyTabResults"));
console.log("stored results:", JSON.stringify(stored).slice(0,300));

await context.close();
console.log("HOSTED_BACKEND_TEST_DONE");