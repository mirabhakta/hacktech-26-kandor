DEMO_HTML = r"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1.0" />
  <title>Kandor Safety Demo</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style>
    :root {
      --bg: #f6f7f9;
      --surface: #ffffff;
      --surface-muted: #f2f4f7;
      --border: #e3e7ec;
      --text: #111827;
      --muted: #667085;
      --accent: #4f46e5;
      --accent-soft: #eef2ff;
      --safe: #027a48;
      --safe-soft: #ecfdf3;
      --warn: #b54708;
      --warn-soft: #fffaeb;
      --danger: #b42318;
      --danger-soft: #fef3f2;
      --neutral: #475467;
      --neutral-soft: #f2f4f7;
      --radius: 16px;
      --shadow: 0 18px 45px -24px rgba(16, 24, 40, .18);
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--text);
      background: var(--bg);
      line-height: 1.5;
    }
    a { color: var(--accent); }
    .skip-link {
      position: absolute;
      left: 12px;
      top: -40px;
      background: var(--surface);
      color: var(--text);
      padding: 8px 12px;
      border-radius: 8px;
      z-index: 100;
    }
    .skip-link:focus { top: 12px; }
    header {
      padding: 28px 20px 18px;
      max-width: 1240px;
      margin: 0 auto;
    }
    .brand-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .brand-mark {
      width: 40px;
      height: 40px;
      border-radius: 12px;
      background: linear-gradient(135deg, #4f46e5, #7c3aed);
      color: #fff;
      display: grid;
      place-items: center;
      font-family: "Fraunces", serif;
      font-size: 20px;
      font-weight: 700;
    }
    .brand-name {
      font-family: "Fraunces", serif;
      font-size: 24px;
      font-weight: 700;
      letter-spacing: -0.02em;
    }
    .brand-caption {
      color: var(--muted);
      font-size: 14px;
    }
    .disclosure {
      max-width: 760px;
      margin-top: 18px;
      padding: 12px 14px;
      border-radius: 12px;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--muted);
      font-size: 13px;
    }
    main {
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 20px 40px;
      display: grid;
      grid-template-columns: 250px minmax(0, 1fr) 360px;
      gap: 20px;
      align-items: start;
    }
    @media (max-width: 1080px) {
      main { grid-template-columns: 1fr 360px; }
      .conversations { grid-column: 1 / -1; }
    }
    @media (max-width: 760px) {
      main { grid-template-columns: 1fr; padding: 0 14px 32px; }
      header { padding: 22px 14px 14px; }
    }
    .panel {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      overflow: hidden;
    }
    .panel-header {
      padding: 16px 18px;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }
    .panel-title {
      margin: 0;
      font-size: 15px;
      font-weight: 700;
    }
    .panel-body { padding: 16px 18px; }
    .conversations {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    @media (max-width: 1080px) {
      .conversations {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      }
    }
    .conversation-button {
      width: 100%;
      border: 1px solid var(--border);
      background: var(--surface);
      border-radius: 12px;
      padding: 12px;
      text-align: left;
      cursor: pointer;
      display: flex;
      gap: 10px;
      align-items: center;
      transition: border-color 140ms ease, background 140ms ease, transform 140ms ease;
    }
    .conversation-button:hover { border-color: #c7d0db; }
    .conversation-button:focus-visible { outline: 3px solid #c7d2fe; outline-offset: 2px; }
    .conversation-button.is-active { border-color: var(--accent); background: var(--accent-soft); }
    .avatar {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      color: #fff;
      display: grid;
      place-items: center;
      font-size: 13px;
      font-weight: 700;
      flex: 0 0 auto;
    }
    .conversation-meta { min-width: 0; }
    .conversation-name { font-weight: 600; font-size: 14px; }
    .conversation-preview {
      color: var(--muted);
      font-size: 13px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .chat-panel { display: flex; flex-direction: column; min-height: 620px; }
    .chat-header {
      padding: 16px 18px;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .chat-title { font-weight: 700; font-size: 16px; }
    .chat-subtitle { color: var(--muted); font-size: 13px; }
    .chat {
      flex: 1;
      padding: 20px;
      background: var(--surface-muted);
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 10px;
      min-height: 360px;
    }
    .message {
      max-width: 78%;
      padding: 11px 14px;
      border-radius: 16px;
      font-size: 15px;
      line-height: 1.45;
      word-wrap: break-word;
    }
    .message.other {
      align-self: flex-start;
      background: var(--surface);
      border: 1px solid var(--border);
      border-bottom-left-radius: 6px;
    }
    .message.you {
      align-self: flex-end;
      background: var(--accent);
      color: #fff;
      border-bottom-right-radius: 6px;
    }
    .composer {
      padding: 16px 18px;
      border-top: 1px solid var(--border);
      background: var(--surface);
    }
    .composer textarea {
      width: 100%;
      min-height: 76px;
      resize: vertical;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 12px 14px;
      font: inherit;
      font-size: 15px;
      background: var(--surface-muted);
    }
    .composer textarea:focus { outline: 3px solid #c7d2fe; border-color: var(--accent); }
    .controls {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 10px;
      align-items: center;
    }
    .button {
      border: 0;
      border-radius: 10px;
      padding: 9px 14px;
      font: inherit;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      background: var(--accent);
      color: #fff;
      transition: transform 120ms ease, opacity 120ms ease;
    }
    .button:hover { opacity: .92; }
    .button:focus-visible { outline: 3px solid #c7d2fe; outline-offset: 2px; }
    .button.secondary {
      background: var(--surface);
      color: var(--text);
      border: 1px solid var(--border);
    }
    .button:disabled { opacity: .55; cursor: not-allowed; }
    .status {
      margin-top: 10px;
      color: var(--muted);
      font-size: 13px;
      min-height: 18px;
    }
    .analysis {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .analysis-state {
      padding: 12px 14px;
      border-radius: 12px;
      font-size: 14px;
      border: 1px solid var(--border);
      background: var(--surface-muted);
    }
    .analysis-state.warning { background: var(--danger-soft); border-color: #fecdca; color: var(--danger); }
    .analysis-state.safe { background: var(--safe-soft); border-color: #abefc6; color: var(--safe); }
    .analysis-state.error { background: var(--danger-soft); border-color: #fecdca; color: var(--danger); }
    .risk-level {
      font-family: "Fraunces", serif;
      font-size: 34px;
      font-weight: 700;
      letter-spacing: -0.03em;
      line-height: 1;
    }
    .risk-meta { color: var(--muted); font-size: 13px; margin-top: 6px; }
    .pill {
      display: inline-flex;
      align-items: center;
      padding: 5px 10px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      margin: 4px 6px 0 0;
    }
    .pill-risk { background: var(--danger-soft); color: var(--danger); }
    .pill-safe { background: var(--safe-soft); color: var(--safe); }
    .pill-neutral { background: var(--neutral-soft); color: var(--neutral); }
    .signals {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }
    .signal {
      padding: 6px 10px;
      border-radius: 999px;
      background: var(--warn-soft);
      color: var(--warn);
      font-size: 13px;
      font-weight: 600;
      border: 1px solid #fedf89;
    }
    .evidence {
      display: flex;
      flex-direction: column;
      gap: 10px;
      max-height: 300px;
      overflow: auto;
      padding-right: 2px;
    }
    .evidence-card {
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 12px;
      background: var(--surface);
    }
    .evidence-card strong { font-size: 14px; }
    .evidence-card p { margin: 6px 0 0; color: var(--muted); font-size: 13px; }
    .empty { color: var(--muted); font-size: 14px; }
    .footer {
      grid-column: 1 / -1;
      color: var(--muted);
      font-size: 13px;
      padding-top: 8px;
    }
    @media (prefers-reduced-motion: reduce) {
      * { transition: none !important; animation: none !important; }
    }
  </style>
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to main content</a>
  <header>
    <div class="brand-row">
      <div class="brand">
        <div class="brand-mark" aria-hidden="true">K</div>
        <div>
          <div class="brand-name">Kandor</div>
          <div class="brand-caption">Synthetic conversation safety demo</div>
        </div>
      </div>
      <div class="brand-caption">No Chrome extension required</div>
    </div>
    <div class="disclosure">
      This demo uses synthetic conversations only. Kandor is not clinically validated and may produce false positives or false negatives. Rule-based fallback results are labeled separately from model-based analysis.
    </div>
  </header>

  <main id="main-content">
    <section class="panel conversations" aria-labelledby="conversations-title">
      <div class="panel-header">
        <h2 class="panel-title" id="conversations-title">Conversations</h2>
      </div>
      <div class="panel-body" id="inboxList" role="list"></div>
    </section>

    <section class="panel chat-panel" aria-labelledby="chat-title">
      <div class="chat-header">
        <div class="avatar" id="activeAvatar" aria-hidden="true">s9</div>
        <div>
          <div class="chat-title" id="activeName">stranger_92</div>
          <div class="chat-subtitle" id="activeSub">Synthetic grooming-pattern example</div>
        </div>
      </div>
      <div class="chat" id="thread" role="log" aria-live="polite" aria-label="Conversation messages"></div>
      <div class="composer">
        <label for="messageInput" class="brand-caption">Add a message to this synthetic conversation</label>
        <textarea id="messageInput" placeholder="Type a message..." aria-label="Message"></textarea>
        <div class="controls">
          <select id="speakerSelect" aria-label="Send as">
            <option value="adult">Other person</option>
            <option value="child">You</option>
          </select>
          <button class="button" type="button" id="addMessage">Send</button>
          <button class="button secondary" type="button" id="resetChat">Reset</button>
          <button class="button secondary" type="button" id="analyzeNow">Analyze now</button>
        </div>
        <div class="status" id="scanStatus" role="status">Ready.</div>
      </div>
    </section>

    <section class="panel analysis" aria-labelledby="analysis-title">
      <div class="panel-header">
        <h2 class="panel-title" id="analysis-title">Kandor safety review</h2>
        <span class="pill pill-neutral" id="resultPill">Idle</span>
      </div>
      <div class="panel-body analysis">
        <div class="analysis-state" id="analysisStatus" role="status">Select or edit a conversation to begin.</div>
        <div>
          <div class="risk-level" id="riskLevel">-</div>
          <div class="risk-meta">Danger rating: <span id="danger">-</span> / 100. Confidence: <span id="confidence">-</span>% (heuristic, not calibrated).</div>
        </div>
        <div>
          <strong>Analysis mode</strong>
          <div class="risk-meta" id="mode">-</div>
        </div>
        <div>
          <strong>Recommended next step</strong>
          <div class="risk-meta" id="action">-</div>
        </div>
        <div>
          <strong>Detected signals</strong>
          <div class="signals" id="threats"></div>
        </div>
        <div class="risk-meta" id="evaluation"></div>
        <div>
          <strong>Message evidence</strong>
          <div class="evidence" id="flagged"></div>
        </div>
      </div>
    </section>

    <div class="footer">
      Synthetic conversations only. Kandor is not clinically validated and may produce false positives or false negatives.
    </div>
  </main>

  <script>
    const threads = {
      stranger: {
        name: "stranger_92", initials: "s9", color: "#4f46e5", subtitle: "Synthetic grooming-pattern example",
        messages: [
          { speaker: "adult", text: "You seem really mature for your age. Do not tell your parents we talk, okay?" },
          { speaker: "child", text: "Why not? They usually check my messages." },
          { speaker: "adult", text: "They would not understand our connection. Move to WhatsApp and send me your address so I can mail you a surprise." },
          { speaker: "child", text: "I do have WhatsApp. What kind of surprise?" }
        ]
      },
      alex: {
        name: "alex", initials: "AX", color: "#dc2626", subtitle: "Synthetic harassment example",
        messages: [
          { speaker: "adult", text: "You are worthless and nobody wants you." },
          { speaker: "child", text: "Please stop." },
          { speaker: "adult", text: "Everyone hates you." }
        ]
      },
      sam: {
        name: "sam", initials: "SP", color: "#ea580c", subtitle: "Synthetic personal-information request",
        messages: [
          { speaker: "adult", text: "Where do you live and what school do you go to?" },
          { speaker: "child", text: "Why?" },
          { speaker: "adult", text: "Send me your address so I can visit." }
        ]
      },
      mia: {
        name: "mia.creates", initials: "MC", color: "#db2777", subtitle: "Synthetic low-risk conversation",
        messages: [
          { speaker: "adult", text: "Still on for the museum tomorrow?" },
          { speaker: "child", text: "Yep! 2pm at the main entrance" },
          { speaker: "adult", text: "haha see you tmrw then" }
        ]
      },
      jordan: {
        name: "jordan.lee", initials: "JL", color: "#0f766e", subtitle: "Synthetic ambiguous conversation",
        messages: [
          { speaker: "adult", text: "What are you wearing to the party?" },
          { speaker: "child", text: "Just jeans and a hoodie." },
          { speaker: "adult", text: "Cool, see you there." }
        ]
      },
      snack: {
        name: "the_snack_squad", initials: "S", color: "#d97706", subtitle: "Synthetic group chat",
        messages: [
          { speaker: "adult", text: "whos bringing chips" },
          { speaker: "child", text: "I can grab 2 bags" }
        ]
      }
    };

    const inboxList = document.getElementById("inboxList");
    const thread = document.getElementById("thread");
    const activeName = document.getElementById("activeName");
    const activeSub = document.getElementById("activeSub");
    const activeAvatar = document.getElementById("activeAvatar");
    const messageInput = document.getElementById("messageInput");
    const speakerSelect = document.getElementById("speakerSelect");
    const addButton = document.getElementById("addMessage");
    const resetButton = document.getElementById("resetChat");
    const analyzeButton = document.getElementById("analyzeNow");
    const scanStatus = document.getElementById("scanStatus");

    let currentId = "stranger";
    let lastSignature = "";
    let scanTimer = null;
    let scanning = false;

    function normalizeText(value) { return String(value || "").replace(/\s+/g, " ").trim(); }
    function speakerClass(speaker) { return speaker === "child" ? "you" : "other"; }
    function riskLevel(danger) {
      if (danger >= 80) return "Severe";
      if (danger >= 60) return "High";
      if (danger >= 40) return "Moderate";
      if (danger > 0) return "Low";
      return "None detected";
    }
    function actionLabel(action) {
      const labels = { none: "No action needed", monitor: "Monitor the conversation", warn_user: "Warn the person at risk", block_and_alert_guardian: "Block and alert a guardian" };
      return labels[action] || action || "Monitor";
    }
    function signalLabel(signal) {
      const labels = { GROOMING: "Trust grooming", SEXUAL_CONTENT: "Sexual content", PII_SOLICITATION: "Personal information request", PLATFORM_MIGRATION: "Move off-platform", THREATS_COERCION: "Threats or coercion", SELF_HARM_CONTENT: "Self-harm content", HATE_HARASSMENT: "Harassment", FINANCIAL_SCAM: "Financial scam", OBFUSCATION: "Hidden language" };
      return labels[signal] || signal;
    }

    function getBaselineMessages() { return (threads[currentId]?.messages || []).map(message => ({ ...message })); }

    function renderMessages(messages) {
      thread.replaceChildren();
      for (const message of messages) {
        const bubble = document.createElement("div");
        bubble.className = "message " + speakerClass(message.speaker);
        bubble.textContent = message.text;
        thread.appendChild(bubble);
      }
      thread.scrollTop = thread.scrollHeight;
    }

    function extractMessages() {
      const messages = [];
      for (const bubble of thread.querySelectorAll(".message")) {
        const speaker = bubble.classList.contains("you") ? "child" : "adult";
        const text = normalizeText(bubble.textContent);
        if (text) messages.push({ speaker, text });
      }
      return messages.slice(-24);
    }

    function signature(messages) {
      return JSON.stringify({ id: currentId, messages: messages.map(message => ({ speaker: message.speaker, text: message.text })) });
    }

    function renderResult(result) {
      const danger = Number(result?.danger_rating || 0);
      const confidence = Number(result?.confidence_score ?? result?.confidence ?? 0);
      const level = riskLevel(danger);
      const pill = document.getElementById("resultPill");
      pill.textContent = danger > 0 ? level + " risk" : "No risk detected";
      pill.className = "pill " + (danger >= 40 ? "pill-risk" : "pill-safe");
      document.getElementById("riskLevel").textContent = level;
      document.getElementById("danger").textContent = danger;
      document.getElementById("confidence").textContent = confidence;
      document.getElementById("mode").textContent = result?.fallback_used ? "Rule-based fallback" : (result?.analysis_provider || "Model analysis");
      document.getElementById("action").textContent = actionLabel(result?.recommended_action || "none");
      const threats = Array.isArray(result?.threats_detected) ? result.threats_detected : [];
      const threatsEl = document.getElementById("threats");
      threatsEl.replaceChildren();
      if (!threats.length) {
        const none = document.createElement("div");
        none.className = "empty";
        none.textContent = "No concerning signals detected.";
        threatsEl.appendChild(none);
      } else {
        for (const signal of threats) {
          const chip = document.createElement("span");
          chip.className = "signal";
          chip.textContent = signalLabel(signal);
          threatsEl.appendChild(chip);
        }
      }
      document.getElementById("evaluation").textContent = result?.evaluation || "";
      const flagged = Array.isArray(result?.flagged_messages) ? result.flagged_messages : [];
      const flaggedEl = document.getElementById("flagged");
      flaggedEl.replaceChildren();
      if (flagged.length) {
        for (const item of flagged) {
          const card = document.createElement("article");
          card.className = "evidence-card";
          const title = document.createElement("strong");
          title.textContent = (item.speaker || "unknown") + ": " + (item.text || "");
          card.appendChild(title);
          const reasons = document.createElement("p");
          reasons.textContent = "Why it matters: " + (((item.reasons || []).map(signalLabel).join(", ")) || "No reason provided");
          card.appendChild(reasons);
          const matched = document.createElement("p");
          matched.textContent = "Matched phrases: " + (((item.phrases || []).join(" | ")) || "None");
          card.appendChild(matched);
          flaggedEl.appendChild(card);
        }
      } else if (result?.highest_risk_message) {
        const card = document.createElement("article");
        card.className = "evidence-card";
        const title = document.createElement("strong");
        title.textContent = "Highest-risk excerpt";
        card.appendChild(title);
        const body = document.createElement("p");
        body.textContent = result.highest_risk_message;
        card.appendChild(body);
        flaggedEl.appendChild(card);
      } else {
        const empty = document.createElement("div");
        empty.className = "empty";
        empty.textContent = "No message-level evidence was returned.";
        flaggedEl.appendChild(empty);
      }
      const status = document.getElementById("analysisStatus");
      status.className = "analysis-state " + (danger >= 40 ? "warning" : "safe");
      status.textContent = danger >= 40
        ? "Kandor found a concerning pattern in this synthetic conversation."
        : "No strong concerning pattern was detected in this synthetic conversation.";
    }

    function renderFailure(message) {
      const pill = document.getElementById("resultPill");
      pill.textContent = "Analysis failed";
      pill.className = "pill pill-risk";
      document.getElementById("riskLevel").textContent = "Unavailable";
      document.getElementById("danger").textContent = "-";
      document.getElementById("confidence").textContent = "-";
      document.getElementById("mode").textContent = "Unavailable";
      document.getElementById("action").textContent = "No conclusion reached";
      const threatsEl = document.getElementById("threats");
      threatsEl.replaceChildren();
      const none = document.createElement("div");
      none.className = "empty";
      none.textContent = "No signals reported.";
      threatsEl.appendChild(none);
      document.getElementById("evaluation").textContent = "";
      const flaggedEl = document.getElementById("flagged");
      flaggedEl.replaceChildren();
      const failed = document.createElement("div");
      failed.className = "empty";
      failed.textContent = "Analysis failed. Kandor did not mark this conversation as safe.";
      flaggedEl.appendChild(failed);
      const status = document.getElementById("analysisStatus");
      status.className = "analysis-state error";
      status.textContent = message || "Analysis failed. No safety conclusion was produced.";
    }

    async function scan(force) {
      const messages = extractMessages();
      if (!messages.length) {
        scanStatus.textContent = "No messages to analyze.";
        return;
      }
      const currentSignature = signature(messages);
      if (!force && currentSignature === lastSignature) {
        scanStatus.textContent = "No changes since the last scan.";
        return;
      }
      lastSignature = currentSignature;
      scanning = true;
      scanStatus.textContent = "Analyzing conversation...";
      const status = document.getElementById("analysisStatus");
      status.className = "analysis-state";
      status.textContent = "Analyzing synthetic conversation...";
      try {
        const response = await fetch("/v1/evaluate", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ platform: "demo", messages })
        });
        if (!response.ok) throw new Error("Backend returned HTTP " + response.status);
        renderResult(await response.json());
        scanStatus.textContent = "Analysis updated.";
      } catch (error) {
        renderFailure("Analysis failed: " + (error?.message || "network error") + ". Kandor did not mark this conversation as safe.");
        scanStatus.textContent = "Analysis failed.";
      } finally {
        scanning = false;
      }
    }

    function scheduleScan() {
      if (scanTimer) clearTimeout(scanTimer);
      scanTimer = setTimeout(() => scan(false), 650);
    }

    function setActiveConversation(id) {
      currentId = id;
      for (const button of inboxList.querySelectorAll(".conversation-button")) {
        button.classList.toggle("is-active", button.getAttribute("data-id") === id);
      }
      const conversation = threads[id];
      activeName.textContent = conversation.name;
      activeSub.textContent = conversation.subtitle;
      activeAvatar.textContent = conversation.initials;
      activeAvatar.style.background = conversation.color;
      lastSignature = "";
      renderMessages(getBaselineMessages());
      messageInput.value = "";
      document.getElementById("analysisStatus").className = "analysis-state";
      document.getElementById("analysisStatus").textContent = "Analyzing synthetic conversation...";
      scan(true);
    }

    for (const id of Object.keys(threads)) {
      const conversation = threads[id];
      const button = document.createElement("button");
      button.type = "button";
      button.className = "conversation-button";
      button.setAttribute("data-id", id);
      button.setAttribute("role", "listitem");
      const avatar = document.createElement("div");
      avatar.className = "avatar";
      avatar.style.background = conversation.color;
      avatar.textContent = conversation.initials;
      const meta = document.createElement("div");
      meta.className = "conversation-meta";
      const name = document.createElement("div");
      name.className = "conversation-name";
      name.textContent = conversation.name;
      const preview = document.createElement("div");
      preview.className = "conversation-preview";
      preview.textContent = conversation.messages[conversation.messages.length - 1]?.text || "";
      meta.appendChild(name);
      meta.appendChild(preview);
      button.appendChild(avatar);
      button.appendChild(meta);
      button.addEventListener("click", () => setActiveConversation(id));
      inboxList.appendChild(button);
    }

    addButton.addEventListener("click", () => {
      const text = messageInput.value.trim();
      if (!text) return;
      const bubble = document.createElement("div");
      bubble.className = "message " + speakerClass(speakerSelect.value);
      bubble.textContent = text;
      thread.appendChild(bubble);
      messageInput.value = "";
      thread.scrollTop = thread.scrollHeight;
      scheduleScan();
    });

    messageInput.addEventListener("keydown", event => {
      if ((event.ctrlKey || event.metaKey) && event.key === "Enter") addButton.click();
    });

    resetButton.addEventListener("click", () => {
      renderMessages(getBaselineMessages());
      lastSignature = "";
      scan(true);
    });

    analyzeButton.addEventListener("click", () => scan(true));

    const observer = new MutationObserver(() => {
      if (!scanning) scheduleScan();
    });
    observer.observe(thread, { childList: true, subtree: true, characterData: true });

    setActiveConversation("stranger");
  </script>
</body>
</html>
"""