import pkg from "file:///C:/Users/miraa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.js";
const { chromium } = pkg;
import fs from "node:fs";
import path from "node:path";

const browser = await chromium.launch();
const page = await browser.newPage();
const html = fs.readFileSync("C:/Users/miraa/Downloads/hacktech-26-kandor/tests/instagram_fixture.html", "utf8");
await page.setContent(html, { waitUntil: "domcontentloaded" });

// Polyfill chrome runtime for content script initialization.
await page.addInitScript(() => {
  window.chrome = { runtime: { sendMessage: () => {}, lastError: null }, storage: { local: { get: (_k, cb) => cb({}), set: () => {} }, sync: { get: (_k, cb) => cb({}) } } };
});

await page.addScriptTag({ path: "C:/Users/miraa/Downloads/hacktech-26-kandor/Frontend/constants.js" });
await page.addScriptTag({ path: "C:/Users/miraa/Downloads/hacktech-26-kandor/Frontend/content.js" });

// Wait for script initialization.
await page.waitForTimeout(500);
const messages = await page.evaluate(() => (typeof extractInstagramMessages === "function" ? extractInstagramMessages() : null));
console.log("EXTRACTED:", JSON.stringify(messages, null, 2));
await browser.close();