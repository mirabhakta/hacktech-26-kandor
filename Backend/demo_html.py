DEMO_HTML = r"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1.0" />
  <title>Kandor synthetic messaging demo</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,500;9..144,700&display=swap" rel="stylesheet" />
  <style>
    :root {
      --ig-bg:#fafafa; --ig-surface:#fff; --ig-line:#dbdbdb; --ig-incoming:#efefef;
      --ig-outgoing1:#3797f0; --ig-outgoing2:#6b4eff; --ig-text:#262626; --ig-sub:#8e8e8e;
      --kandor:#4f46e5;
    }
    * { box-sizing:border-box; }
    body { margin:0; font-family:Inter,system-ui,sans-serif; background:linear-gradient(135deg,#eff6ff,#eef2ff 45%,#faf5ff); color:var(--ig-text); }
    .page { min-height:100vh; padding:16px; }
    .shell { max-width:1180px; margin:0 auto; display:grid; grid-template-columns:300px minmax(0,1fr) 360px; gap:16px; }
    @media (max-width:1000px){ .shell { grid-template-columns:1fr; } }
    .card { background:rgba(255,255,255,.72); border:1px solid rgba(255,255,255,.6); border-radius:20px; box-shadow:0 20px 50px -12px rgba(99,102,241,.18); backdrop-filter:blur(16px); overflow:hidden; }
    .inbox { min-height:560px; display:flex; flex-direction:column; }
    .inbox-top { padding:12px 14px; border-bottom:1px solid var(--ig-line); display:flex; align-items:center; justify-content:space-between; }
    .wordmark { font-weight:700; display:flex; align-items:center; gap:8px; }
    .logo { width:28px;height:28px;border-radius:8px;background:linear-gradient(135deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888); color:#fff;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:800; }
    .conv { width:100%; border:none; background:#fff; text-align:left; padding:10px 14px; display:flex; gap:12px; cursor:pointer; border-bottom:1px solid #fafafa; }
    .conv:hover { background:#fafafa; }
    .conv.is-active { background:#efefef; }
    .avatar { width:44px;height:44px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;color:#fff;font-size:.75rem;font-weight:600; }
    .conv-body { min-width:0; flex:1; }
    .conv-top { display:flex; justify-content:space-between; gap:8px; margin-bottom:2px; }
    .conv-name { font-weight:600; font-size:.88rem; }
    .conv-time { font-size:.7rem; color:var(--ig-sub); }
    .conv-preview { font-size:.78rem; color:var(--ig-sub); white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
    .thread-card { display:flex; flex-direction:column; min-height:560px; }
    .thread-top { padding:10px 16px; border-bottom:1px solid var(--ig-line); display:flex; align-items:center; gap:10px; }
    .thread { flex:1; padding:16px 20px; background:var(--ig-bg); overflow-y:auto; display:flex; flex-direction:column; gap:4px; }
    .msg { max-width:72%; padding:10px 14px; border-radius:18px; line-height:1.45; font-size:.9rem; word-wrap:break-word; }
    .msg.adult { align-self:flex-start; background:var(--ig-incoming); border-radius:18px 18px 18px 4px; }
    .msg.child { align-self:flex-end; color:#fff; background:linear-gradient(130deg,var(--ig-outgoing1),var(--ig-outgoing2)); border-radius:18px 18px 4px 18px; }
    .composer { padding:12px 16px; border-top:1px solid var(--ig-line); background:#fff; }
    .composer textarea { width:100%; min-height:64px; resize:vertical; border-radius:20px; border:1px solid var(--ig-line); background:#fafafa; padding:10px 14px; font:inherit; font-size:.88rem; }
    .controls { display:flex; flex-wrap:wrap; gap:8px; margin-top:8px; align-items:center; }
    select, button { border:none; border-radius:8px; padding:8px 12px; font:inherit; font-size:.82rem; font-weight:600; cursor:pointer; }
    select { background:#fff; border:1px solid var(--ig-line); }
    button { background:#0095f6; color:#fff; }
    button.secondary { background:#efefef; color:#262626; }
    .analysis { padding:16px; display:flex; flex-direction:column; gap:10px; }
    .analysis h2 { margin:0; font-family:Fraunces,serif; font-size:1.4rem; background:linear-gradient(135deg,#111827,#4b5563); -webkit-background-clip:text; background-clip:text; color:transparent; }
    .pill { display:inline-flex; align-items:center; padding:5px 10px; border-radius:999px; font-size:11px; font-weight:700; margin:4px 6px 0 0; }
    .pillRisk { background:#fee2e2; color:#b91c1c; border:1px solid #fecaca; }
    .pillSafe { background:#dcfce7; color:#15803d; border:1px solid #bbf7d0; }
    .muted { color:var(--ig-sub); font-size:.85rem; line-height:1.5; }
    .flagged { display:flex; flex-direction:column; gap:8px; max-height:260px; overflow:auto; }
    .flag { padding:10px 12px; border-radius:12px; background:rgba(255,255,255,.55); border:1px solid rgba(255,255,255,.5); }
    .chip { display:inline-flex; margin:3px 5px 0 0; padding:4px 8px; border-radius:999px; background:#fee2e2; color:#b91c1c; font-size:11px; font-weight:600; border:1px solid #fecaca; }
    .banner { padding:10px 12px; border-radius:12px; background:linear-gradient(135deg,#eff6ff,#eef2ff); border:1px solid #dbeafe; }
    .error { background:#fef2f2; border-color:#fecaca; color:#991b1b; }
    .footer { grid-column:1 / -1; font-size:.8rem; color:var(--ig-sub); line-height:1.5; }
    .status { font-size:.8rem; color:var(--ig-sub); }
  </style>
</head>
<body>
  <div class="page">
    <div class="shell">
      <aside class="card inbox">
        <div class="inbox-top">
          <div class="wordmark"><div class="logo">IB</div>Instabam</div>
          <span class="muted">Synthetic demo</span>
        </div>
        <div id="inboxList"></div>
      </aside>

      <section class="card thread-card">
        <div class="thread-top">
          <div class="avatar" id="activeAvatar">s9</div>
          <div>
            <div style="font-weight:600" id="activeName">stranger_92</div>
            <div class="muted" id="activeSub">Synthetic conversation</div>
          </div>
        </div>
        <div class="thread" id="thread"></div>
        <div class="composer">
          <textarea id="messageInput" placeholder="Message..." aria-label="Message"></textarea>
          <div class="controls">
            <select id="speakerSelect" aria-label="Send as">
              <option value="adult">Other person (left)</option>
              <option value="child">You (right)</option>
            </select>
            <button type="button" id="addMessage">Send</button>
            <button type="button" id="resetChat" class="secondary">Reset thread</button>
            <button type="button" id="analyzeNow" class="secondary">Analyze now</button>
          </div>
          <div class="status" id="scanStatus">Ready.</div>
        </div>
      </section>

      <aside class="card analysis">
        <h2>Kandor analysis</h2>
        <div id="analysisStatus" class="banner">Select or edit a conversation to begin.</div>
        <div id="resultPill" class="pill pillSafe">Idle</div>
        <div><b>Danger rating:</b> <span id="danger">-</span></div>
        <div><b>Confidence:</b> <span id="confidence">-</span> <span class="muted">(heuristic, not calibrated)</span></div>
        <div><b>Analysis mode:</b> <span id="mode">-</span></div>
        <div><b>Recommended action:</b> <span id="action">-</span></div>
        <div><b>Detected signals:</b> <span id="threats">None</span></div>
        <div class="muted" id="evaluation"></div>
        <div><b>Message evidence</b></div>
        <div class="flagged" id="flagged"></div>
      </aside>

      <div class="footer">
        Synthetic conversations only. Kandor is not clinically validated and may produce false positives or false negatives. Rule-based fallback results are labeled separately from model output. No Chrome extension is required for this demo.
      </div>
    </div>
  </div>

  <script>
    const threads = {
      stranger: {
        name:"stranger_92", initials:"s9", grad:"linear-gradient(135deg,#6366f1,#8b5cf6)", sub:"Synthetic grooming-pattern example",
        messages:[
          {speaker:"adult", text:"You seem really mature for your age. Do not tell your parents we talk, okay?"},
          {speaker:"child", text:"Why not? They usually check my messages."},
          {speaker:"adult", text:"They would not understand our connection. Move to WhatsApp and send me your address so I can mail you a surprise."},
          {speaker:"child", text:"I do have WhatsApp. What kind of surprise?"}
        ]
      },
      alex: {
        name:"alex", initials:"AX", grad:"linear-gradient(135deg,#ef4444,#dc2626)", sub:"Synthetic harassment example",
        messages:[
          {speaker:"adult", text:"You are worthless and nobody wants you."},
          {speaker:"child", text:"Please stop."},
          {speaker:"adult", text:"Everyone hates you."}
        ]
      },
      sam: {
        name:"sam", initials:"SP", grad:"linear-gradient(135deg,#f59e0b,#ea580c)", sub:"Synthetic personal-information request",
        messages:[
          {speaker:"adult", text:"Where do you live and what school do you go to?"},
          {speaker:"child", text:"Why?"},
          {speaker:"adult", text:"Send me your address so I can visit."}
        ]
      },
      mia: {
        name:"mia.creates", initials:"MC", grad:"linear-gradient(135deg,#ec4899,#f43f5e)", sub:"Synthetic low-risk conversation",
        messages:[
          {speaker:"adult", text:"Still on for the museum tomorrow?"},
          {speaker:"child", text:"Yep! 2pm at the main entrance"},
          {speaker:"adult", text:"haha see you tmrw then"}
        ]
      },
      jordan: {
        name:"jordan.lee", initials:"JL", grad:"linear-gradient(135deg,#14b8a6,#0d9488)", sub:"Synthetic ambiguous conversation",
        messages:[
          {speaker:"adult", text:"What are you wearing to the party?"},
          {speaker:"child", text:"Just jeans and a hoodie."},
          {speaker:"adult", text:"Cool, see you there."}
        ]
      },
      snack: {
        name:"the_snack_squad", initials:"S", grad:"linear-gradient(135deg,#f59e0b,#ea580c)", sub:"Synthetic group chat",
        messages:[
          {speaker:"adult", text:"whos bringing chips"},
          {speaker:"child", text:"I can grab 2 bags"}
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

    function speakerClass(speaker){ return speaker === "child" ? "child" : "adult"; }
    function normalizeText(v){ return String(v||"").replace(/\s+/g," ").trim(); }

    function getBaselineMessages(){ return (threads[currentId]?.messages || []).map(m => ({...m})); }

    function renderMessages(messages){
      thread.innerHTML = "";
      for (const m of messages){
        const bubble = document.createElement("div");
        bubble.className = "msg " + speakerClass(m.speaker);
        bubble.textContent = m.text;
        thread.appendChild(bubble);
      }
      thread.scrollTop = thread.scrollHeight;
    }

    function extractMessages(){
      const out = [];
      for (const bubble of thread.querySelectorAll(".msg")){
        const speaker = bubble.classList.contains("child") ? "child" : "adult";
        const text = normalizeText(bubble.textContent);
        if (text) out.push({speaker, text});
      }
      return out.slice(-24);
    }

    function signature(messages){
      return JSON.stringify({id:currentId, messages:messages.map(m=>({speaker:m.speaker,text:m.text}))});
    }

    function threatLabel(t){
      const labels = {GROOMING:"Trust grooming", SEXUAL_CONTENT:"Sexual content", PII_SOLICITATION:"Personal info request", PLATFORM_MIGRATION:"Move off-platform", THREATS_COERCION:"Threats or coercion", SELF_HARM_CONTENT:"Self-harm content", HATE_HARASSMENT:"Harassment", FINANCIAL_SCAM:"Financial scam", OBFUSCATION:"Hidden language"};
      return labels[t] || t;
    }

    function renderResult(result){
      const danger = Number(result?.danger_rating || 0);
      const confidence = Number(result?.confidence_score ?? result?.confidence ?? 0);
      document.getElementById("resultPill").textContent = danger >= 40 ? "Risk " + danger : (danger > 0 ? "Monitor " + danger : "Clear");
      document.getElementById("resultPill").className = "pill " + (danger >= 40 ? "pillRisk" : "pillSafe");
      document.getElementById("danger").textContent = danger;
      document.getElementById("confidence").textContent = confidence;
      document.getElementById("mode").textContent = result?.fallback_used ? "Fallback (rules only)" : (result?.analysis_provider || "unknown");
      document.getElementById("action").textContent = result?.recommended_action || "none";
      const threats = Array.isArray(result?.threats_detected) ? result.threats_detected : [];
      document.getElementById("threats").innerHTML = threats.length ? threats.map(t=>'<span class="chip">'+threatLabel(t)+'</span>').join("") : "None";
      document.getElementById("evaluation").textContent = result?.evaluation || "";
      const flagged = Array.isArray(result?.flagged_messages) ? result.flagged_messages : [];
      const flaggedEl = document.getElementById("flagged");
      flaggedEl.innerHTML = "";
      if (flagged.length){
        for (const item of flagged){
          const div = document.createElement("div");
          div.className = "flag";
          div.innerHTML = "<div><b>" + (item.speaker || "unknown") + ":</b> " + (item.text || "") + "</div><div class='muted' style='margin-top:4px'>Reasons: " + ((item.reasons||[]).map(threatLabel).join(", ") || "None") + "</div><div class='muted' style='margin-top:4px'>Matched: " + ((item.phrases||[]).join(" | ") || "None") + "</div>";
          flaggedEl.appendChild(div);
        }
      } else if (result?.highest_risk_message){
        const div = document.createElement("div");
        div.className = "flag";
        div.innerHTML = "<div><b>Highest-risk excerpt</b></div><div style='margin-top:6px'>" + result.highest_risk_message + "</div>";
        flaggedEl.appendChild(div);
      } else {
        flaggedEl.innerHTML = "<div class='muted'>No message-level evidence returned.</div>";
      }
      document.getElementById("analysisStatus").className = "banner";
      document.getElementById("analysisStatus").textContent = danger >= 40 ? "Kandor detected a concerning pattern in this synthetic conversation." : "No strong concerning pattern detected in this synthetic conversation.";
    }

    function renderFailure(message){
      document.getElementById("resultPill").textContent = "Failed";
      document.getElementById("resultPill").className = "pill pillRisk";
      document.getElementById("danger").textContent = "-";
      document.getElementById("confidence").textContent = "-";
      document.getElementById("mode").textContent = "Unavailable";
      document.getElementById("action").textContent = "No conclusion";
      document.getElementById("threats").innerHTML = "None";
      document.getElementById("evaluation").textContent = "";
      document.getElementById("flagged").innerHTML = "<div class='muted'>Analysis failed. Kandor did not mark this conversation as safe.</div>";
      const status = document.getElementById("analysisStatus");
      status.className = "banner error";
      status.textContent = message || "Analysis failed. No safety conclusion was produced.";
    }

    async function scan(force){
      const messages = extractMessages();
      if (!messages.length){ scanStatus.textContent = "No messages to analyze."; return; }
      const sig = signature(messages);
      if (!force && sig === lastSignature){ scanStatus.textContent = "No changes since last scan."; return; }
      lastSignature = sig;
      scanning = true;
      scanStatus.textContent = "Analyzing conversation...";
      document.getElementById("analysisStatus").className = "banner";
      document.getElementById("analysisStatus").textContent = "Analyzing synthetic conversation...";
      try {
        const response = await fetch("/v1/evaluate", {
          method:"POST",
          headers:{"Content-Type":"application/json"},
          body: JSON.stringify({platform:"demo", messages})
        });
        if (!response.ok) throw new Error("Backend returned HTTP " + response.status);
        const result = await response.json();
        renderResult(result);
        scanStatus.textContent = "Analysis updated.";
      } catch (err) {
        renderFailure("Analysis failed: " + (err?.message || "network error") + ". Kandor did not mark this conversation as safe.");
        scanStatus.textContent = "Analysis failed.";
      } finally {
        scanning = false;
      }
    }

    function scheduleScan(){ if (scanTimer) clearTimeout(scanTimer); scanTimer = setTimeout(()=>scan(false), 700); }

    function setActiveInbox(id){
      currentId = id;
      for (const btn of inboxList.querySelectorAll(".conv")) btn.classList.toggle("is-active", btn.getAttribute("data-id") === id);
      const meta = threads[id];
      activeName.textContent = meta.name;
      activeSub.textContent = meta.sub;
      activeAvatar.textContent = meta.initials;
      activeAvatar.style.background = meta.grad;
      lastSignature = "";
      document.getElementById("analysisStatus").className = "banner";
      document.getElementById("analysisStatus").textContent = "Analyzing synthetic conversation...";
      renderMessages(getBaselineMessages());
      messageInput.value = "";
      scan(true);
    }

    for (const id of Object.keys(threads)){
      const meta = threads[id];
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "conv";
      btn.setAttribute("data-id", id);
      btn.innerHTML = '<div class="avatar" style="background:'+meta.grad+'">'+meta.initials+'</div><div class="conv-body"><div class="conv-top"><span class="conv-name">'+meta.name+'</span><span class="conv-time">demo</span></div><div class="conv-preview">'+(meta.messages[meta.messages.length-1]?.text || "")+'</div></div>';
      btn.addEventListener("click", ()=>setActiveInbox(id));
      inboxList.appendChild(btn);
    }

    addButton.addEventListener("click", ()=>{
      const text = messageInput.value.trim();
      if (!text) return;
      const bubble = document.createElement("div");
      bubble.className = "msg " + speakerClass(speakerSelect.value);
      bubble.textContent = text;
      thread.appendChild(bubble);
      messageInput.value = "";
      thread.scrollTop = thread.scrollHeight;
      scheduleScan();
    });

    messageInput.addEventListener("keydown", (event)=>{ if ((event.ctrlKey || event.metaKey) && event.key === "Enter") addButton.click(); });

    resetButton.addEventListener("click", ()=>{ renderMessages(getBaselineMessages()); lastSignature=""; scan(true); });

    analyzeButton.addEventListener("click", ()=>scan(true));

    const observer = new MutationObserver(()=>{ if (!scanning) scheduleScan(); });
    observer.observe(thread, {childList:true, subtree:true, characterData:true});

    setActiveInbox("stranger");
  </script>
</body>
</html>
"""