import pkg from "file:///C:/Users/miraa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.js";
const { chromium } = pkg;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
await page.goto("http://127.0.0.1:8000/demo");
await page.waitForFunction(
  () => document.querySelector("#danger")?.textContent && document.querySelector("#danger").textContent !== "-",
  { timeout: 10000 },
);

async function dotHidden() {
  return page.evaluate(() => document.getElementById("insightsDot").hidden);
}

// stranger_92 is concerning -> dot visible
console.log("dot hidden (stranger):", await dotHidden());
if (await dotHidden()) throw new Error("Risk indicator should show for the concerning conversation");

// switch to safe conversation -> dot clears (open the inbox tab first on small screens)
await page.click('.viewtabs button[data-view="inbox-panel"]');
await page.click('[data-id="mia"]');
await page.waitForFunction(() => Number(document.querySelector("#danger").textContent) < 40, { timeout: 10000 });
console.log("dot hidden (mia):", await dotHidden());
if (!(await dotHidden())) throw new Error("Risk indicator should clear for the safe conversation");

// switch back -> dot returns
await page.click('.viewtabs button[data-view="inbox-panel"]');
await page.click('[data-id="stranger"]');
await page.waitForFunction(() => Number(document.querySelector("#danger").textContent) >= 40, { timeout: 10000 });
console.log("dot hidden (stranger again):", await dotHidden());
if (await dotHidden()) throw new Error("Risk indicator should return for the concerning conversation");

await browser.close();
console.log("DEMO_RISK_DOT_PASS");
