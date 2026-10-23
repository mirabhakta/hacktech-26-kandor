DEMO_HTML = r"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1.0" />
  <title>Kandor safety review</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap" rel="stylesheet" />
  <style>
    :root {
      --frame: #edf1f0;
      --sheet: #ffffff;
      --edge: #e2e8e7;
      --text: #14201f;
      --muted: #5b6a6a;
      --accent: #0f766e;
      --accent-soft: #e5f4f1;
      --safe: #176b55;
      --safe-soft: #e8f5ef;
      --warn: #8a5a00;
      --warn-soft: #fdf3dd;
      --danger: #a4322b;
      --danger-soft: #fdecea;
      --evidence: #b7791f;
      --sans: "Manrope", system-ui, sans-serif;
      --display: "Fraunces", Georgia, serif;
    }
    * { box-sizing: border-box; }
    html, body { height: 100%; }
    body { margin: 0; background: var(--frame); color: var(--text); font-family: var(--sans); font-size: 14px; line-height: 1.5; }
    button, textarea, select { font: inherit; }
    .app { height: 100vh; height: 100dvh; display: grid; grid-template-rows: 48px auto 1fr; }
    .topbar {
      display: flex; align-items: center; justify-content: space-between; gap: 16px;
      padding: 0 20px; background: var(--frame);
    }
    .brand { display: flex; align-items: center; gap: 10px; min-width: 0; }
    .brand-mark {
      width: 28px; height: 28px; border-radius: 8px; background: var(--accent); color: #fff;
      display: grid; place-items: center; font-family: var(--display); font-weight: 700; font-size: 16px;
    }
    .brand h1 { margin: 0; font-family: var(--display); font-size: 20px; line-height: 1.1; letter-spacing: -.02em; font-weight: 700; }
    .brand p { margin: 0; color: var(--muted); font-size: 12px; }
    .synthetic-note { color: var(--muted); font-size: 12px; text-align: right; }
    .viewtabs { display: none; gap: 6px; padding: 0 12px 8px; background: var(--frame); }
    .viewtabs button {
      flex: 1; border: 0; background: transparent; border-radius: 8px; padding: 9px 6px;
      font-size: 13px; font-weight: 700; color: var(--muted); cursor: pointer;
    }
    .viewtabs button.is-active { background: var(--accent-soft); color: var(--accent); }
    .viewtabs button:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
    .sheet {
      background: var(--sheet); border: 1px solid var(--edge); border-radius: 16px;
      margin: 0 8px 8px 8px; min-height: 0;
      display: grid; grid-template-columns: 280px minmax(0, 1fr) 360px;
    }
    .panel { min-width: 0; min-height: 0; display: flex; flex-direction: column; }
    .inbox-panel { border-right: 1px solid var(--edge); }
    .insights-panel { border-left: 1px solid var(--edge); background: #fbfdfc; border-radius: 0 16px 16px 0; }
    .panel-header { padding: 14px 16px 10px; }
    .panel-title { margin: 0; font-size: 14px; font-weight: 700; }
    .panel-subtitle { color: var(--muted); font-size: 12px; margin-top: 2px; }
    .conversation-list { overflow-y: auto; padding: 4px 8px 12px; }
    .conversation {
      width: 100%; border: 0; background: transparent; border-radius: 10px; padding: 10px 12px 10px 10px;
      display: grid; grid-template-columns: 36px minmax(0, 1fr) auto; gap: 10px; align-items: start;
      text-align: left; cursor: pointer; color: inherit; position: relative;
    }
    .conversation:hover { background: #f2f6f5; }
    .conversation:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
    .conversation.is-active { background: var(--accent-soft); }
    .conversation.is-active::before {
      content: ""; position: absolute; left: 0; top: 10px; bottom: 10px; width: 2px;
      background: var(--accent); border-radius: 2px;
    }
    .avatar {
      width: 36px; height: 36px; border-radius: 10px; display: grid; place-items: center;
      color: #fff; font-size: 12px; font-weight: 700;
    }
    .conversation-name { font-size: 14px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .conversation-preview { color: var(--muted); font-size: 13px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin-top: 1px; }
    .conversation-time { color: var(--muted); font-size: 11px; white-space: nowrap; }
    .chat-panel { min-width: 0; }
    .chat-header { padding: 14px 18px 10px; display: flex; align-items: center; gap: 12px; }
    .chat-name { font-size: 15px; font-weight: 700; }
    .chat-subtitle { color: var(--muted); font-size: 12px; }
    .chat-scroll { flex: 1; overflow-y: auto; padding: 6px 18px 18px; background: #f7faf9; }
    .day-divider { display: flex; align-items: center; gap: 12px; color: var(--muted); font-size: 11px; margin: 8px 0 16px; }
    .day-divider::before, .day-divider::after { content: ""; height: 1px; background: var(--edge); flex: 1; }
    .message-row { display: flex; gap: 10px; margin: 10px 0; align-items: flex-end; }
    .message-row.outgoing { flex-direction: row-reverse; }
    .message-avatar { width: 26px; height: 26px; border-radius: 8px; display: grid; place-items: center; font-size: 10px; font-weight: 700; color: #fff; flex: 0 0 auto; }
    .message-stack { max-width: min(70%, 560px); display: flex; flex-direction: column; gap: 4px; }
    .outgoing .message-stack { align-items: flex-end; }
    .bubble {
      padding: 10px 13px; border-radius: 14px; background: var(--sheet); border: 1px solid var(--edge);
      font-size: 14px; line-height: 1.45; word-break: break-word;
    }
    .outgoing .bubble { background: var(--accent); border-color: var(--accent); color: #fff; border-bottom-right-radius: 5px; }
    .incoming .bubble { border-bottom-left-radius: 5px; }
    .bubble.has-evidence { border-left: 3px solid var(--evidence); }
    .outgoing .bubble.has-evidence { border-left-color: var(--accent); border-right: 3px solid var(--evidence); }
    .bubble.flash { outline: 2px solid var(--evidence); outline-offset: 2px; }
    .message-meta { color: var(--muted); font-size: 11px; padding: 0 4px; }
    .composer { padding: 12px 18px 14px; background: var(--sheet); border-top: 1px solid var(--edge); border-radius: 0 0 0 0; }
    .composer-row { display: flex; gap: 10px; align-items: flex-end; }
    .composer textarea {
      flex: 1; min-height: 44px; max-height: 120px; resize: vertical; border: 1px solid var(--edge);
      border-radius: 10px; padding: 11px 12px; background: #f7faf9; color: var(--text);
    }
    .composer textarea:focus { outline: 2px solid var(--accent); outline-offset: 1px; }
    .button {
      border: 0; border-radius: 9px; padding: 10px 14px; background: var(--accent); color: #fff;
      font-weight: 700; font-size: 13px; cursor: pointer; white-space: nowrap;
    }
    .button.secondary { background: #eef3f2; color: var(--text); }
    .button:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
    .composer-actions { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin-top: 8px; }
    .select { border: 1px solid var(--edge); border-radius: 9px; padding: 9px 10px; background: var(--sheet); color: var(--text); font-size: 13px; }
    .scan-status { margin-top: 8px; min-height: 18px; color: var(--muted); font-size: 12px; }
    .insights-scroll { flex: 1; overflow-y: auto; padding: 0 16px 16px; display: flex; flex-direction: column; gap: 14px; }
    .insight-state { padding: 12px 14px; border-radius: 10px; background: #eef3f2; font-size: 13px; }
    .insight-state.safe { background: var(--safe-soft); color: var(--safe); }
    .insight-state.warning { background: var(--danger-soft); color: var(--danger); }
    .insight-state.error { background: var(--danger-soft); color: var(--danger); }
    #resultPill {
      display: inline-block; padding: 4px 10px; border-radius: 999px;
      font-size: 12px; font-weight: 700; background: #eef3f2; color: var(--muted);
    }
    #resultPill.pill-risk { background: var(--danger-soft); color: var(--danger); }
    #resultPill.pill-safe { background: var(--safe-soft); color: var(--safe); }
    .risk-block { display: flex; flex-direction: column; gap: 4px; }
    .risk-level { font-family: var(--display); font-size: 30px; line-height: 1.05; letter-spacing: -.02em; font-weight: 700; }
    .risk-caption { color: var(--muted); font-size: 12px; }
    .insight-label { font-size: 12px; font-weight: 700; color: var(--muted); margin-bottom: 6px; }
    .signal-list { display: flex; flex-wrap: wrap; gap: 6px; }
    .signal { padding: 6px 9px; border-radius: 999px; background: var(--warn-soft); color: var(--warn); font-size: 12px; font-weight: 700; }
    .guidance { color: var(--text); font-size: 13px; line-height: 1.55; }
    .evidence-list { display: flex; flex-direction: column; gap: 8px; }
    .evidence-card {
      width: 100%; text-align: left; border-radius: 10px; padding: 11px 12px;
      background: #f2f6f5; border: 0; cursor: pointer; color: var(--text); font-size: 13px;
    }
    .evidence-card:hover { background: var(--accent-soft); }
    .evidence-card:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
    .evidence-card strong { display: block; font-size: 13px; margin-bottom: 4px; }
    .evidence-card p { margin: 4px 0 0; color: var(--muted); font-size: 12px; line-height: 1.45; }
    .limitations { color: var(--muted); font-size: 11px; line-height: 1.5; }
    @media (max-width: 1100px) {
      .sheet { grid-template-columns: 240px minmax(0, 1fr) 320px; }
    }
    @media (max-width: 1023px) {
      .app { grid-template-rows: 48px auto 1fr; }
      .viewtabs { display: flex; }
      .sheet { grid-template-columns: minmax(0, 1fr); overflow: hidden; }
      .panel { display: none; overflow: hidden; }
      .panel.is-visible { display: flex; }
      .inbox-panel, .insights-panel { border: 0; border-radius: 16px; }
      .conversation-list, .chat-scroll, .insights-scroll { flex: 1; }
      .synthetic-note { display: none; }
      .message-stack { max-width: 82%; }
    }
  </style>
</head>
<body>
  <div class="app">
    <header class="topbar">
      <div class="brand">
        <div class="brand-mark" aria-hidden="true">K</div>
        <div>
          <h1>Kandor safety review</h1>
          <p>Synthetic conversation workspace</p>
        </div>
      </div>
      <div class="synthetic-note">All conversations are synthetic.<br />No real messages are used.</div>
    </header>

    <nav class="viewtabs" aria-label="Views">
      <button type="button" data-view="inbox-panel">Conversations</button>
      <button type="button" data-view="chat-panel" class="is-active">Messages</button>
      <button type="button" data-view="insights-panel">Insights</button>
    </nav>

    <main class="sheet">
      <aside class="panel inbox-panel is-visible" aria-labelledby="conversations-title">
        <div class="panel-header">
          <h2 class="panel-title" id="conversations-title">Conversations</h2>
          <div class="panel-subtitle">Demo inbox</div>
        </div>
        <div class="conversation-list" id="inboxList" role="list"></div>
      </aside>

      <section class="panel chat-panel is-visible" aria-labelledby="chat-title">
        <div class="chat-header">
          <div class="avatar" id="activeAvatar" aria-hidden="true">s9</div>
          <div>
            <div class="chat-name" id="chat-title"><span id="activeName">stranger_92</span></div>
            <div class="chat-subtitle" id="activeSub">Grooming-pattern example</div>
          </div>
        </div>
        <div class="chat-scroll" id="thread" role="log" aria-live="polite" aria-label="Conversation messages"></div>
        <div class="composer">
          <div class="composer-row">
            <textarea id="messageInput" placeholder="Add a synthetic message..." aria-label="Message"></textarea>
            <button class="button" type="button" id="addMessage">Send</button>
          </div>
          <div class="composer-actions">
            <select id="speakerSelect" class="select" aria-label="Send as">
              <option value="adult">Other person</option>
              <option value="child">You</option>
            </select>
            <button class="button secondary" type="button" id="resetChat">Reset</button>
            <button class="button secondary" type="button" id="analyzeNow">Analyze now</button>
          </div>
          <div class="scan-status" id="scanStatus" role="status">Ready.</div>
        </div>
      </section>

      <aside class="panel insights-panel" aria-labelledby="insights-title">
        <div class="panel-header">
          <h2 class="panel-title" id="insights-title">Kandor insights</h2>
          <span id="resultPill">Idle</span>
        </div>
        <div class="insights-scroll">
          <div class="insight-state" id="analysisStatus" role="status">Select a conversation to review its patterns.</div>
          <div class="risk-block">
            <div class="risk-level" id="riskLevel">Not reviewed</div>
            <div class="risk-caption" id="riskCaption">Kandor will summarize concerns when analysis completes.</div>
          </div>
          <div>
            <div class="insight-label">Analysis basis</div>
            <div class="guidance" id="mode">Rule-based analysis. No paid model is used.</div>
          </div>
          <div>
            <div class="insight-label">Recommended next step</div>
            <div class="guidance" id="action">No action needed yet.</div>
          </div>
          <div>
            <div class="insight-label">Detected signals</div>
            <div class="signal-list" id="threats"></div>
          </div>
          <div>
            <div class="insight-label">Why this matters</div>
            <div class="guidance" id="evaluation"></div>
          </div>
          <div>
            <div class="insight-label">Message evidence</div>
            <div class="evidence-list" id="flagged"></div>
          </div>
          <div class="risk-caption" id="scoreNote"></div>
          <div class="risk-caption" id="danger" hidden></div>
          <div class="limitations">
            Rule-based analysis is heuristic, not clinically validated. It can miss harmful behavior or flag ordinary phrases. Scores are not calibrated probabilities.
          </div>
        </div>
      </aside>
    </main>
  </div>

  <script>
    const threads = {
      stranger: {
        name: "stranger_92", initials: "s9", color: "#0f766e", subtitle: "Grooming-pattern example",
        messages: [
          { speaker: "adult", text: "You seem really mature for your age. Do not tell your parents we talk, okay?", time: "9:12 AM" },
          { speaker: "child", text: "Why not? They usually check my messages.", time: "9:13 AM" },
          { speaker: "adult", text: "They would not understand our connection. Move to WhatsApp and send me your address so I can mail you a surprise.", time: "9:14 AM" },
          { speaker: "child", text: "I do have WhatsApp. What kind of surprise?", time: "9:15 AM" }
        ]
      },
      alex: {
        name: "alex", initials: "AX", color: "#b43d34", subtitle: "Harassment example",
        messages: [
          { speaker: "adult", text: "You are worthless and nobody wants you.", time: "8:42 AM" },
          { speaker: "child", text: "Please stop.", time: "8:43 AM" },
          { speaker: "adult", text: "Everyone hates you.", time: "8:43 AM" }
        ]
      },
      sam: {
        name: "sam", initials: "SP", color: "#b46a2b", subtitle: "Personal-information request",
        messages: [
          { speaker: "adult", text: "Where do you live and what school do you go to?", time: "Yesterday" },
          { speaker: "child", text: "Why?", time: "Yesterday" },
          { speaker: "adult", text: "Send me your address so I can visit.", time: "Yesterday" }
        ]
      },
      mia: {
        name: "mia.creates", initials: "MC", color: "#a04f78", subtitle: "Low-risk conversation",
        messages: [
          { speaker: "adult", text: "Still on for the museum tomorrow?", time: "7:30 PM" },
          { speaker: "child", text: "Yep! 2pm at the main entrance", time: "7:31 PM" },
          { speaker: "adult", text: "haha see you tmrw then", time: "7:32 PM" }
        ]
      },
      jordan: {
        name: "jordan.lee", initials: "JL", color: "#3f6f8f", subtitle: "Ambiguous conversation",
        messages: [
          { speaker: "adult", text: "What are you wearing to the party?", time: "Mon" },
          { speaker: "child", text: "Just jeans and a hoodie.", time: "Mon" },
          { speaker: "adult", text: "Cool, see you there.", time: "Mon" }
        ]
      },
      snack: {
        name: "the_snack_squad", initials: "S", color: "#8a7040", subtitle: "Group chat",
        messages: [
          { speaker: "adult", text: "whos bringing chips", time: "Sun" },
          { speaker: "child", text: "I can grab 2 bags", time: "Sun" }
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
    const viewtabs = document.querySelector(".viewtabs");

    let currentId = "stranger";
    let currentMessages = [];
    let lastSignature = "";
    let scanTimer = null;
    let scanning = false;
    let latestFlaggedTexts = new Set();

    function normalizeText(value) { return String(value || "").replace(/\s+/g, " ").trim(); }
    function speakerClass(speaker) { return speaker === "child" ? "outgoing" : "incoming"; }
    function nowLabel() { return "Just now"; }
    function riskLevel(danger) {
      if (danger >= 80) return "Severe concern";
      if (danger >= 60) return "High concern";
      if (danger >= 40) return "Moderate concern";
      if (danger > 0) return "Low concern";
      return "No strong concern";
    }
    function riskCaption(danger) {
      if (danger >= 80) return "Several strong patterns suggest the conversation needs immediate attention.";
      if (danger >= 60) return "Multiple concerning patterns are present in this conversation.";
      if (danger >= 40) return "Some concerning patterns are present and deserve attention.";
      if (danger > 0) return "A minor pattern was noticed, but the overall conversation is low concern.";
      return "No strong concerning pattern was detected in this synthetic conversation.";
    }
    function actionLabel(action) {
      const labels = { none: "No action needed.", monitor: "Continue monitoring the conversation.", warn_user: "Warn the person at risk.", block_and_alert_guardian: "Block the contact and alert a guardian." };
      return labels[action] || "Continue monitoring the conversation.";
    }
    function signalLabel(signal) {
      const labels = { GROOMING: "Trust grooming", SEXUAL_CONTENT: "Sexual content", PII_SOLICITATION: "Personal information request", PLATFORM_MIGRATION: "Move off-platform", THREATS_COERCION: "Threats or coercion", SELF_HARM_CONTENT: "Self-harm content", HATE_HARASSMENT: "Harassment", FINANCIAL_SCAM: "Financial scam", OBFUSCATION: "Hidden language" };
      return labels[signal] || signal;
    }

    function renderMessages() {
      thread.replaceChildren();
      const divider = document.createElement("div");
      divider.className = "day-divider";
      divider.textContent = "Today";
      thread.appendChild(divider);
      currentMessages.forEach((message, index) => {
        const row = document.createElement("div");
        row.className = "message-row " + speakerClass(message.speaker);
        const avatar = document.createElement("div");
        avatar.className = "message-avatar";
        avatar.style.background = message.speaker === "child" ? "#38525a" : (threads[currentId]?.color || "#0f766e");
        avatar.textContent = message.speaker === "child" ? "You" : (threads[currentId]?.initials || "?");
        const stack = document.createElement("div");
        stack.className = "message-stack";
        const bubble = document.createElement("div");
        bubble.className = "bubble" + (latestFlaggedTexts.has(normalizeText(message.text)) ? " has-evidence" : "");
        bubble.textContent = message.text;
        bubble.id = "msg-" + index;
        const meta = document.createElement("div");
        meta.className = "message-meta";
        meta.textContent = (message.speaker === "child" ? "You" : threads[currentId]?.name || "Other") + " · " + (message.time || nowLabel());
        stack.appendChild(bubble);
        stack.appendChild(meta);
        row.appendChild(avatar);
        row.appendChild(stack);
        thread.appendChild(row);
      });
      thread.scrollTop = thread.scrollHeight;
    }

    function signature() {
      return JSON.stringify({ id: currentId, messages: currentMessages.map(message => ({ speaker: message.speaker, text: message.text })) });
    }

    function scanPayload() {
      return currentMessages.slice(-24).map(message => ({ speaker: message.speaker, text: message.text }));
    }

    function renderResult(result) {
      const danger = Number(result?.danger_rating || 0);
      latestFlaggedTexts = new Set((Array.isArray(result?.flagged_messages) ? result.flagged_messages : []).map(item => normalizeText(item?.text)));
      const pill = document.getElementById("resultPill");
      pill.textContent = danger >= 40 ? riskLevel(danger) : (danger > 0 ? riskLevel(danger) : "No strong concern");
      pill.className = danger >= 40 ? "pill-risk" : "pill-safe";
      pill.id = "resultPill";
      document.getElementById("riskLevel").textContent = riskLevel(danger);
      document.getElementById("riskCaption").textContent = riskCaption(danger);
      document.getElementById("danger").textContent = danger;
      document.getElementById("scoreNote").textContent = "Heuristic score " + danger + " of 100. This is not a calibrated probability.";
      document.getElementById("mode").textContent = result?.fallback_used ? "Rule-based analysis. No paid model is used." : "Model-assisted analysis.";
      document.getElementById("action").textContent = actionLabel(result?.recommended_action || "none");
      const threats = Array.isArray(result?.threats_detected) ? result.threats_detected : [];
      const threatsEl = document.getElementById("threats");
      threatsEl.replaceChildren();
      if (!threats.length) {
        const empty = document.createElement("div");
        empty.className = "risk-caption";
        empty.textContent = "No concerning signals detected.";
        threatsEl.appendChild(empty);
      } else {
        for (const signal of threats) {
          const chip = document.createElement("span");
          chip.className = "signal";
          chip.textContent = signalLabel(signal);
          threatsEl.appendChild(chip);
        }
      }
      document.getElementById("evaluation").textContent = result?.fallback_used
        ? "Kandor's built-in rules matched wording and patterns in this conversation that are often associated with risk. A person should review the flagged messages above."
        : (result?.evaluation || "");
      const flagged = Array.isArray(result?.flagged_messages) ? result.flagged_messages : [];
      const flaggedEl = document.getElementById("flagged");
      flaggedEl.replaceChildren();
      if (flagged.length) {
        flagged.forEach((item) => {
          const card = document.createElement("button");
          card.type = "button";
          card.className = "evidence-card";
          const title = document.createElement("strong");
          const who = item.speaker === "child" ? "You" : (item.speaker === "adult" || item.speaker === "sender" ? "Other person" : (item.speaker || "Unknown"));
          title.textContent = who + ": " + (item.text || "");
          card.appendChild(title);
          const why = document.createElement("p");
          why.textContent = "Why it matters: " + (((item.reasons || []).map(signalLabel).join(", ")) || "No reason provided");
          card.appendChild(why);
          const matched = document.createElement("p");
          matched.textContent = "Flagged wording: " + (((item.phrases || []).join(" | ")) || "None");
          card.appendChild(matched);
          card.addEventListener("click", () => {
            const target = normalizeText(item.text);
            const index = currentMessages.findIndex(message => normalizeText(message.text) === target);
            if (index < 0) return;
            const bubble = document.getElementById("msg-" + index);
            if (!bubble) return;
            bubble.scrollIntoView({ block: "center", behavior: "smooth" });
            bubble.classList.add("flash");
            setTimeout(() => bubble.classList.remove("flash"), 1600);
          });
          flaggedEl.appendChild(card);
        });
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
        empty.className = "risk-caption";
        empty.textContent = "No message-level evidence was returned.";
        flaggedEl.appendChild(empty);
      }
      const status = document.getElementById("analysisStatus");
      status.className = "insight-state " + (danger >= 40 ? "warning" : "safe");
      status.textContent = danger >= 40
        ? "Kandor found a concerning pattern in this synthetic conversation."
        : "No strong concerning pattern was detected in this synthetic conversation.";
      renderMessages();
    }

    function renderFailure(message) {
      latestFlaggedTexts = new Set();
      const pill = document.getElementById("resultPill");
      pill.textContent = "Analysis failed";
      pill.className = "";
      pill.id = "resultPill";
      document.getElementById("riskLevel").textContent = "Analysis unavailable";
      document.getElementById("riskCaption").textContent = "No safety conclusion was produced.";
      document.getElementById("danger").textContent = "-";
      document.getElementById("scoreNote").textContent = "";
      document.getElementById("mode").textContent = "Unavailable";
      document.getElementById("action").textContent = "Try the analysis again.";
      const threatsEl = document.getElementById("threats");
      threatsEl.replaceChildren();
      const none = document.createElement("div");
      none.className = "risk-caption";
      none.textContent = "No signals reported.";
      threatsEl.appendChild(none);
      document.getElementById("evaluation").textContent = "";
      const flaggedEl = document.getElementById("flagged");
      flaggedEl.replaceChildren();
      const failed = document.createElement("div");
      failed.className = "risk-caption";
      failed.textContent = "Analysis failed. Kandor did not mark this conversation as safe.";
      flaggedEl.appendChild(failed);
      const status = document.getElementById("analysisStatus");
      status.className = "insight-state error";
      status.textContent = message || "Analysis failed. No safety conclusion was produced.";
      renderMessages();
    }

    async function scan(force) {
      if (!currentMessages.length) { scanStatus.textContent = "No messages to analyze."; return; }
      const currentSignature = signature();
      if (!force && currentSignature === lastSignature) { scanStatus.textContent = "No changes since the last scan."; return; }
      lastSignature = currentSignature;
      scanning = true;
      scanStatus.textContent = "Analyzing conversation...";
      const status = document.getElementById("analysisStatus");
      status.className = "insight-state";
      status.textContent = "Analyzing synthetic conversation...";
      try {
        const response = await fetch("/v1/evaluate", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ platform: "demo", messages: scanPayload() })
        });
        if (!response.ok) throw new Error("Backend returned HTTP " + response.status);
        renderResult(await response.json());
        scanStatus.textContent = "Analysis updated.";
      } catch (error) {
        renderFailure("Analysis failed: " + (error?.message || "network error") + ". Kandor did not mark this conversation as safe.");
        scanStatus.textContent = "Analysis failed.";
      } finally { scanning = false; }
    }

    function scheduleScan() { if (scanTimer) clearTimeout(scanTimer); scanTimer = setTimeout(() => scan(false), 650); }

    function setActiveConversation(id) {
      currentId = id;
      for (const button of inboxList.querySelectorAll(".conversation")) button.classList.toggle("is-active", button.getAttribute("data-id") === id);
      const conversation = threads[id];
      activeName.textContent = conversation.name;
      activeSub.textContent = conversation.subtitle;
      activeAvatar.textContent = conversation.initials;
      activeAvatar.style.background = conversation.color;
      currentMessages = conversation.messages.map(message => ({ ...message }));
      lastSignature = "";
      latestFlaggedTexts = new Set();
      renderMessages();
      messageInput.value = "";
      document.getElementById("analysisStatus").className = "insight-state";
      document.getElementById("analysisStatus").textContent = "Analyzing synthetic conversation...";
      scan(true);
    }

    function setMobileView(viewClass) {
      for (const panel of document.querySelectorAll(".sheet .panel")) panel.classList.toggle("is-visible", panel.classList.contains(viewClass));
      for (const button of viewtabs.querySelectorAll("button")) button.classList.toggle("is-active", button.getAttribute("data-view") === viewClass);
    }
    viewtabs.addEventListener("click", event => {
      const button = event.target.closest("button[data-view]");
      if (button) setMobileView(button.getAttribute("data-view"));
    });

    for (const id of Object.keys(threads)) {
      const conversation = threads[id];
      const button = document.createElement("button");
      button.type = "button";
      button.className = "conversation";
      button.setAttribute("data-id", id);
      button.setAttribute("role", "listitem");
      const avatar = document.createElement("div");
      avatar.className = "avatar";
      avatar.style.background = conversation.color;
      avatar.textContent = conversation.initials;
      const meta = document.createElement("div");
      const name = document.createElement("div");
      name.className = "conversation-name";
      name.textContent = conversation.name;
      const preview = document.createElement("div");
      preview.className = "conversation-preview";
      preview.textContent = conversation.messages[conversation.messages.length - 1]?.text || "";
      meta.appendChild(name);
      meta.appendChild(preview);
      const time = document.createElement("div");
      time.className = "conversation-time";
      time.textContent = conversation.messages[conversation.messages.length - 1]?.time || "Demo";
      button.appendChild(avatar);
      button.appendChild(meta);
      button.appendChild(time);
      button.addEventListener("click", () => {
        setActiveConversation(id);
        if (window.matchMedia("(max-width: 1023px)").matches) setMobileView("chat-panel");
      });
      inboxList.appendChild(button);
    }

    addButton.addEventListener("click", () => {
      const text = messageInput.value.trim();
      if (!text) return;
      currentMessages.push({ speaker: speakerSelect.value, text, time: nowLabel() });
      renderMessages();
      messageInput.value = "";
      scheduleScan();
    });
    messageInput.addEventListener("keydown", event => { if ((event.ctrlKey || event.metaKey) && event.key === "Enter") addButton.click(); });
    resetButton.addEventListener("click", () => { latestFlaggedTexts = new Set(); setActiveConversation(currentId); });
    analyzeButton.addEventListener("click", () => scan(true));

    const observer = new MutationObserver(() => { if (!scanning) scheduleScan(); });
    observer.observe(thread, { childList: true, subtree: true, characterData: true });

    setActiveConversation("stranger");
    if (window.matchMedia("(max-width: 1023px)").matches) setMobileView("chat-panel");
  </script>
</body>
</html>
"""