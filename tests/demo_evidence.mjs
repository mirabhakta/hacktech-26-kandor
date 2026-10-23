import pkg from "file:///C:/Users/miraa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.js";
const { chromium } = pkg;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await page.goto("http://127.0.0.1:8000/demo");
await page.waitForFunction(
  () => document.querySelector("#danger")?.textContent && document.querySelector("#danger").textContent !== "-",
  { timeout: 10000 },
);

// Click the first evidence card and verify the linked message highlights + receives focus.
await page.click("#flagged .evidence-card");
await page.waitForTimeout(600);
const flashCount = await page.evaluate(() => document.querySelectorAll(".bubble.flash").length);
console.log("flashed bubbles:", flashCount);
if (flashCount !== 1) throw new Error("Expected exactly one highlighted message");

const focusedIsBubble = await page.evaluate(() =>
  document.activeElement && document.activeElement.classList.contains("bubble"),
);
console.log("focus on bubble:", focusedIsBubble);
if (!focusedIsBubble) throw new Error("Expected keyboard focus on the highlighted message");

// Highlight clears after a short delay.
await page.waitForTimeout(1500);
const flashAfter = await page.evaluate(() => document.querySelectorAll(".bubble.flash").length);
console.log("flashed bubbles after delay:", flashAfter);
if (flashAfter !== 0) throw new Error("Expected highlight to clear");

await browser.close();
console.log("DEMO_EVIDENCE_PASS");
