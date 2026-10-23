import pkg from "file:///C:/Users/miraa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.js";
const { chromium } = pkg;

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto("http://127.0.0.1:8000/demo");

async function waitForAnalysis() {
  await page.waitForFunction(() => document.querySelector("#danger")?.textContent && document.querySelector("#danger").textContent !== "-", { timeout: 10000 });
}

// Select grooming conversation and verify signals.
await page.click('[data-id="stranger"]');
await waitForAnalysis();
let danger = await page.textContent("#danger");
let threats = await page.textContent("#threats");
console.log("stranger danger:", danger, "threats:", threats);
if (Number(danger) < 70) throw new Error("Expected high risk for grooming scenario");
if (!threats.includes("Trust grooming")) throw new Error("Expected grooming signal");

// Add a new message and verify analysis updates.
const beforeDanger = danger;
await page.fill("#messageInput", "Please do not tell anyone about this.");
await page.click("#addMessage");
await page.waitForTimeout(1500);
await waitForAnalysis();
danger = await page.textContent("#danger");
console.log("after add danger:", danger);
if (Number(danger) < 70) throw new Error("Expected high risk after adding concerning message");

// Add a second message and verify earlier messages are kept.
await page.fill("#messageInput", "Do not tell anyone about this either.");
await page.click("#addMessage");
await page.waitForTimeout(1500);
const threadText = await page.textContent("#thread");
if (!threadText.includes("Please do not tell anyone about this.")) throw new Error("First added message was lost");
if (!threadText.includes("Do not tell anyone about this either.")) throw new Error("Second added message missing");

// Switch to safe conversation and verify warnings clear.
await page.click('[data-id="mia"]');
await page.waitForFunction(() => Number(document.querySelector("#danger").textContent) < 40, { timeout: 10000 });
danger = await page.textContent("#danger");
const status = await page.textContent("#analysisStatus");
console.log("mia danger:", danger, "status:", status);
if (Number(danger) >= 40) throw new Error("Expected low risk for safe conversation");
if (!status.includes("No strong")) throw new Error("Expected safe status");

// Simulate backend failure and ensure not shown as safe.
await page.route("**/v1/evaluate", route => route.fulfill({ status: 500, body: "boom" }));
await page.click('[data-id="stranger"]');
await page.waitForTimeout(2000);
const pill = await page.textContent("#resultPill");
const failureStatus = await page.textContent("#analysisStatus");
console.log("failure pill:", pill, "status:", failureStatus);
if (!pill.includes("Analysis failed")) throw new Error("Failure was not shown as failed");
if (!failureStatus.includes("Analysis failed")) throw new Error("Failure status was not shown");

await browser.close();
console.log("DEMO_FLOW_PASS");