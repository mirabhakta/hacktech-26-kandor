import pkg from "file:///C:/Users/miraa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.js";
const { chromium } = pkg;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
await page.goto("http://127.0.0.1:8000/demo");
await page.waitForTimeout(2500);

async function visible(selector) {
  return page.evaluate((sel) => {
    const el = document.querySelector(sel);
    if (!el) return false;
    const style = getComputedStyle(el);
    return style.display !== "none" && el.offsetParent !== null;
  }, selector);
}

console.log("chat visible:", await visible(".chat-panel"));
console.log("inbox visible:", await visible(".inbox-panel"));
console.log("insights visible:", await visible(".insights-panel"));
if (!(await visible(".chat-panel"))) throw new Error("Messages view should be visible on load");
if (await visible(".inbox-panel")) throw new Error("Inbox should be hidden on load");
if (await visible(".insights-panel")) throw new Error("Insights should be hidden on load");

await page.click('.viewtabs button[data-view="insights-panel"]');
await page.waitForTimeout(500);
if (!(await visible(".insights-panel"))) throw new Error("Insights should show after tab tap");
if (await visible(".chat-panel")) throw new Error("Messages should hide after tab tap");

await page.click('.viewtabs button[data-view="inbox-panel"]');
await page.waitForTimeout(500);
if (!(await visible(".inbox-panel"))) throw new Error("Inbox should show after tab tap");

await browser.close();
console.log("DEMO_TABS_PASS");