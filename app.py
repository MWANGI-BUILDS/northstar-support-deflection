<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Northstar Support — Deflection Assistant</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap');
  :root{
    --paper:#F6F3EC;
    --panel:#FFFFFF;
    --ink:#151A23;
    --ink-soft:#5B6270;
    --line:#E4DFD3;
    --amber:#C9862A;
    --amber-soft:#F2E2C8;
    --navy:#151A23;
    --ok:#3E7A55;
    --warn:#B5502E;
    --mono: 'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
    --display: 'Space Grotesk', 'Segoe UI', sans-serif;
    --body: 'Inter', 'Segoe UI', sans-serif;
  }
  *{box-sizing:border-box;}
  body{
    margin:0; background:var(--paper); color:var(--ink);
    font-family:var(--body); min-height:100vh;
    display:flex; align-items:center; justify-content:center; padding:32px 16px;
  }
  .app{
    width:100%; max-width:960px; background:var(--panel);
    border:1px solid var(--line); border-radius:14px; overflow:hidden;
    box-shadow:0 1px 2px rgba(21,26,35,.04);
    display:grid; grid-template-columns:220px 1fr;
    min-height:640px;
  }
  @media(max-width:720px){ .app{grid-template-columns:1fr;} .side{display:none;} }

  .side{
    background:var(--navy); color:var(--paper); padding:24px 20px;
    display:flex; flex-direction:column; gap:22px;
  }
  .brand{display:flex; align-items:center; gap:8px;}
  .brand .mark{width:16px;height:16px;position:relative;flex:none;}
  .brand .mark::before{content:"";position:absolute;inset:0;background:var(--amber);
    clip-path:polygon(50% 0%,61% 39%,100% 50%,61% 61%,50% 100%,39% 61%,0% 50%,39% 39%);}
  .brand span{font-family:var(--display); font-weight:600; font-size:15px; letter-spacing:.01em;}
  .side .tag{font-size:11.5px; color:#9AA3B2; line-height:1.5;}
  .side .status{margin-top:auto; font-size:11px; color:#8892A0; border-top:1px solid #2A3140; padding-top:14px; line-height:1.7;}
  .side .status b{color:var(--amber); font-weight:600;}

  .main{display:flex; flex-direction:column; height:100%;}
  .header{padding:18px 22px; border-bottom:1px solid var(--line); display:flex; align-items:center; justify-content:space-between;}
  .header h1{font-family:var(--display); font-size:16px; margin:0; font-weight:600;}
  .header p{margin:2px 0 0; font-size:12px; color:var(--ink-soft);}
  .dot{width:7px;height:7px;border-radius:50%;background:var(--ok); display:inline-block; margin-right:6px;}

  .thread{flex:1; overflow-y:auto; padding:20px 22px; display:flex; flex-direction:column; gap:14px;}
  .msg{max-width:78%; padding:11px 14px; border-radius:12px; font-size:13.5px; line-height:1.55;}
  .msg.bot{background:var(--amber-soft); color:var(--ink); border-bottom-left-radius:3px; align-self:flex-start;}
  .msg.user{background:var(--navy); color:var(--paper); border-bottom-right-radius:3px; align-self:flex-end;}
  .msg.bot .k{font-family:var(--mono); background:rgba(21,26,35,.06); padding:1px 5px; border-radius:4px; font-size:12px;}

  .chips{display:flex; flex-wrap:wrap; gap:8px; align-self:flex-start; max-width:88%; margin-top:-4px;}
  .chip{
    font-family:var(--body); font-size:12.5px; font-weight:500; color:var(--navy);
    background:var(--panel); border:1px solid var(--line); padding:8px 13px;
    border-radius:20px; cursor:pointer; transition:border-color .15s, transform .1s;
  }
  .chip:hover{border-color:var(--amber); transform:translateY(-1px);}

  .composer{border-top:1px solid var(--line); padding:14px 22px; display:flex; gap:10px;}
  .composer input{
    flex:1; border:1px solid var(--line); border-radius:9px; padding:10px 12px;
    font-family:var(--body); font-size:13.5px; background:var(--paper); color:var(--ink);
  }
  .composer input:focus{outline:none; border-color:var(--amber);}
  .composer button{
    background:var(--navy); color:var(--paper); border:none; border-radius:9px;
    padding:0 18px; font-family:var(--body); font-weight:600; font-size:13px; cursor:pointer;
  }
  .composer button:hover{background:#232B3A;}

  .trail{padding:8px 22px 14px; font-family:var(--mono); font-size:10.5px; color:var(--ink-soft); border-top:1px solid var(--line); display:flex; align-items:center; gap:6px; flex-wrap:wrap;}
  .trail b{color:var(--ink); font-weight:500;}
  .trail .node{background:var(--paper); border:1px solid var(--line); padding:2px 7px; border-radius:5px;}
  .trail .arrow{color:#C7C1B2;}
</style>
</head>
<body>

<div class="app">
  <div class="side">
    <div class="brand"><div class="mark"></div><span>Northstar Support</span></div>
    <div class="tag">Deflection MVP — resolves order status, returns &amp; refunds, and stock questions before they become tickets.</div>
    <div class="status">
      <b>Coverage</b><br>
      Order Status · Returns &amp; Refunds · Stock Availability<br><br>
      <b>Build</b><br>
      Prototype — Day 2–5 sprint
    </div>
  </div>

  <div class="main">
    <div class="header">
      <div>
        <h1>Ask Northstar</h1>
        <p><span class="dot"></span>Answers in seconds, no ticket needed</p>
      </div>
    </div>
    <div class="thread" id="thread"></div>
    <div class="trail" id="trail"><b>Path:</b></div>
    <div class="composer">
      <input id="freeInput" type="text" placeholder="Ask me anything — an order #, a product, or just say hi…" />
      <button onclick="handleFreeText()">Send</button>
    </div>
  </div>
</div>

<script>
/* ---------- Mock data (stand-ins for Northstar's real systems) ---------- */
const ORDERS = {
  "NS-10234": {item:"Trailhead Jacket",        status:"shipped",    carrier:"UPS",   eta:"Aug 13",                    tracking:"1Z999AA10123456784", placed:"Aug 8"},
  "NS-10250": {item:"Aurora Sneaker",          status:"processing", carrier:null,    eta:"Aug 15 (pending fulfillment)", tracking:null,              placed:"Aug 10"},
  "NS-10199": {item:"Summit Backpack",         status:"delayed",    carrier:"FedEx", eta:"Aug 16 (was Aug 12)",       tracking:"7712994410",         placed:"Aug 5"},
  "NS-10088": {item:"Ridge Fleece Pullover",   status:"delivered",  carrier:"UPS",   eta:"Delivered Aug 9",           tracking:"1Z999AA10998877665", placed:"Aug 2"},
  "NS-10301": {item:"Alpine Trekking Poles",   status:"shipped",    carrier:"USPS",  eta:"Aug 14",                    tracking:"9405511899223344556", placed:"Aug 9"},
  "NS-10315": {item:"Cascade Water Bottle",    status:"processing", carrier:null,    eta:"Aug 16 (pending fulfillment)", tracking:null,              placed:"Aug 11"},
  "NS-10327": {item:"Compass Wool Beanie",     status:"delayed",    carrier:"UPS",   eta:"Aug 18 (was Aug 14)",       tracking:"1Z999AA10556677889", placed:"Aug 6"},
  "NS-10340": {item:"Thermal Base Layer",      status:"delivered",  carrier:"FedEx", eta:"Delivered Aug 10",          tracking:"7712994499",         placed:"Aug 3"},
  "NS-10356": {item:"Trailhead Jacket",        status:"processing", carrier:null,    eta:"Aug 17 (pending fulfillment)", tracking:null,              placed:"Aug 12"},
  "NS-10362": {item:"Aurora Sneaker",          status:"delivered",  carrier:"UPS",   eta:"Delivered Aug 11",          tracking:"1Z999AA10334455667", placed:"Aug 4"},
  "NS-10378": {item:"Summit Backpack",         status:"shipped",    carrier:"USPS",  eta:"Aug 15",                    tracking:"9405511899667788990", placed:"Aug 10"},
  "NS-10390": {item:"Cascade Water Bottle",    status:"delivered",  carrier:"FedEx", eta:"Delivered Aug 12",          tracking:"7712994512",         placed:"Aug 7"}
};
const RETURN_POLICY = {windowDays:30, nonReturnable:["final sale","gift card","personal care"]};
const INVENTORY = {
  "trailhead jacket": {"S":0,"M":3,"L":0,"XL":5, restock:"Aug 20"},
  "aurora sneaker": {"S":2,"M":0,"L":1,"XL":0, restock:"Aug 18"},
  "summit backpack": {"S":8,"M":8,"L":8,"XL":8, restock:null},
  "ridge fleece pullover": {"S":4,"M":12,"L":0,"XL":7, restock:"Aug 22"},
  "alpine trekking poles": {"STANDARD":18,"PRO CARBON":0, restock:"Aug 28"},
  "cascade water bottle": {"20OZ":30,"32OZ":14, restock:null},
  "compass wool beanie": {"CHARCOAL":9,"OATMEAL":0,"FOREST GREEN":2, restock:"Sept 05"},
  "thermal base layer": {"S":0,"M":10,"L":6, restock:"Aug 19"}
};
// Reverse index so order lookups and stock lookups can inform each other (e.g. "is my jacket back in stock")
const PRODUCT_TO_ORDERS = {};
Object.entries(ORDERS).forEach(([id,o])=>{
  const k = o.item.toLowerCase();
  (PRODUCT_TO_ORDERS[k] = PRODUCT_TO_ORDERS[k] || []).push(id);
});

/* ---------- Chat engine ---------- */
const thread = document.getElementById('thread');
const trailEl = document.getElementById('trail');
let path = [];
// Remembers what the customer was just talking about, so follow-ups like
// "what about a Medium" or "when will it ship" don't need to repeat the whole question.
let state = { lastProduct:null, lastOrderId:null };

function titleCase(s){ return s.replace(/\b\w/g, c=>c.toUpperCase()); }

// Finds which variant of a product (S/M/L/XL, or odd ones like "PRO CARBON", "20OZ") a message refers to.
function findVariantKey(item, text){
  const keys = Object.keys(item).filter(k=>k!=='restock');
  const sorted = keys.slice().sort((a,b)=>b.length-a.length); // longer/more specific keys win
  for(const k of sorted){
    if(/^[a-z]{1,3}$/i.test(k)){
      if(new RegExp(`\\b${k}\\b`,'i').test(text)) return k;
    } else {
      const norm = s => s.toLowerCase().replace(/[^a-z0-9]/g,'');
      if(norm(text).includes(norm(k))) return k;
    }
  }
  return null;
}

function say(text, who='bot'){
  const d = document.createElement('div');
  d.className = 'msg ' + who;
  d.innerHTML = text;
  thread.appendChild(d);
  thread.scrollTop = thread.scrollHeight;
}
function chips(options){
  const wrap = document.createElement('div');
  wrap.className = 'chips';
  options.forEach(([label, fn])=>{
    const b = document.createElement('button');
    b.className = 'chip'; b.textContent = label;
    b.onclick = ()=>{ wrap.remove(); say(label,'user'); fn(); };
    wrap.appendChild(b);
  });
  thread.appendChild(wrap);
  thread.scrollTop = thread.scrollHeight;
}
function mark(node){
  path.push(node);
  trailEl.innerHTML = '<b>Path:</b> ' + path.map(p=>`<span class="node">${p}</span>`).join('<span class="arrow">→</span>');
}
function resetPath(){ path=[]; trailEl.innerHTML = '<b>Path:</b>'; }

function humanChip(){
  chips([["Talk to a human", ()=>{ say("Got it — I'll hand this to a support agent with everything above attached. Ticket <span class='k'>#deflect-escalated</span> created.", 'bot'); mark('escalate:human'); }]]);
}

/* ---- Root menu ---- */
function showMenu(){
  resetPath();
  say("Hi! I'm the Northstar assistant. What can I help with?");
  mark('root');
  chips([
    ["Where's my order?", startOrderStatus],
    ["Return or refund", startReturns],
    ["Is this back in stock?", startStock]
  ]);
}

/* ---- Flow 1: Order status ---- */
function startOrderStatus(){
  mark('order-status');
  say("Sure — what's your order number? It looks like <span class='k'>NS-10234</span>.");
}
function lookupOrder(id){
  const orderId = id.toUpperCase();
  const o = ORDERS[orderId];
  mark('order-lookup:'+orderId);
  if(!o){
    say(`I can't find order <span class='k'>${id}</span>. Double check the number, or I can loop in a human.`);
    humanChip();
    return;
  }
  state.lastOrderId = orderId;
  state.lastProduct = o.item;
  const lines = {
    processing: `Order <span class='k'>${orderId}</span> (<b>${o.item}</b>) is <b>being prepared</b>. Estimated ship date: ${o.eta}.`,
    shipped: `Order <span class='k'>${orderId}</span> (<b>${o.item}</b>) has <b>shipped</b> via ${o.carrier}. Tracking: <span class='k'>${o.tracking}</span>. Estimated arrival: ${o.eta}.`,
    delayed: `Order <span class='k'>${orderId}</span> (<b>${o.item}</b>) is <b>running late</b> via ${o.carrier} — new estimate ${o.eta}. Sorry about that.`,
    delivered: `Order <span class='k'>${orderId}</span> (<b>${o.item}</b>) shows as <b>delivered</b> (${o.eta}) via ${o.carrier}.`
  };
  say(lines[o.status]);
  mark('resolved:'+o.status);
  chips([["That answers it, thanks", showMenu], ["Still an issue — talk to a human", ()=>{humanChip();}]]);
}

/* ---- Flow 2: Returns & refunds ---- */
function startReturns(){
  mark('returns');
  say("What's the item category? This determines eligibility.");
  chips([
    ["Apparel / general item", ()=>askReturnWindow("general")],
    ["Electronics", ()=>askReturnWindow("electronics")],
    ["Final sale / gift card", ()=>{
      mark('category:non-returnable');
      say("Items marked final sale or gift cards aren't eligible for return under Northstar's policy.");
      chips([["Understood", showMenu], ["I think this is a mistake — talk to a human", ()=>{humanChip();}]]);
    }]
  ]);
}
function askReturnWindow(category){
  mark('category:'+category);
  say("How many days ago did you receive it?");
  chips([
    ["Within 30 days", ()=>returnResult(category, true)],
    ["More than 30 days", ()=>returnResult(category, false)]
  ]);
}
function returnResult(category, withinWindow){
  mark(withinWindow ? 'eligible' : 'window-expired');
  if(withinWindow){
    say(`Good news — that's eligible for a return. Refunds post to your original payment method <b>5–7 business days</b> after we receive the item. I'll email you a prepaid label.`);
    chips([["Got it, thanks", showMenu]]);
  } else {
    say(`That's outside Northstar's ${RETURN_POLICY.windowDays}-day return window, so I can't auto-approve it. A human can review exceptions case-by-case.`);
    humanChip();
  }
}

/* ---- Flow 3: Stock availability ---- */
function startStock(){
  mark('stock');
  say("Which product are you asking about?");
  chips(Object.keys(INVENTORY).map(k=>[titleCase(k), ()=>lookupStock(titleCase(k))]));
}
function lookupStock(name, variant){
  const key = name.toLowerCase().trim();
  const item = INVENTORY[key];
  mark('stock-lookup:'+key);
  if(!item){
    say(`I don't have a product called <span class='k'>${name}</span> in the catalog. Check the spelling, or I can bring in a human.`);
    humanChip();
    return;
  }
  state.lastProduct = titleCase(key);
  const variantKeys = Object.keys(item).filter(k=>k!=='restock');
  if(!variant){
    say(`Which option for the <b>${titleCase(name)}</b>? (${variantKeys.join(' / ')})`);
    chips(variantKeys.map(v=>[v, ()=>lookupStock(name, v)]));
    return;
  }
  const matchKey = variantKeys.find(k=>k.toLowerCase()===variant.toLowerCase()) || findVariantKey(item, variant);
  if(!matchKey){
    say(`I don't see "${variant}" as an option for the <b>${titleCase(name)}</b> — choices are ${variantKeys.join(' / ')}.`);
    chips(variantKeys.map(v=>[v, ()=>lookupStock(name, v)]));
    return;
  }
  const qty = item[matchKey];
  mark('variant:'+matchKey);
  if(qty > 0){
    say(`Yes — <b>${titleCase(name)} (${matchKey})</b> is in stock, ${qty} left.`);
    mark('resolved:in-stock');
  } else {
    const alt = Object.entries(item).filter(([k,v])=>k!=='restock' && v>0).map(([k])=>k);
    say(`<b>${titleCase(name)} (${matchKey})</b> is currently out of stock.` +
        (item.restock ? ` Restock expected ${item.restock}.` : ` No restock date yet.`) +
        (alt.length ? ` Available now in: ${alt.join(', ')}.` : ``));
    mark('resolved:out-of-stock');
  }
  const relatedOrders = PRODUCT_TO_ORDERS[key];
  chips([
    ["That helps, thanks", showMenu],
    ["Notify me / talk to a human", ()=>{humanChip();}],
    ...(relatedOrders ? [["Check my order for this item", ()=>lookupOrder(relatedOrders[0])]] : [])
  ]);
}
// Answers casual "when's it back" / "is it in stock" questions without forcing the click-through picker.
function productRestockSummary(name){
  const key = name.toLowerCase().trim();
  const item = INVENTORY[key];
  if(!item) return false;
  mark('restock-query:'+key);
  const variantKeys = Object.keys(item).filter(k=>k!=='restock');
  const inStock = variantKeys.filter(v=>item[v] > 0);
  const oos = variantKeys.filter(v=>item[v] === 0);
  let msg = `<b>${titleCase(name)}</b>: `;
  if(oos.length === 0){
    msg += `everything's currently in stock (${variantKeys.map(v=>`${v}: ${item[v]}`).join(', ')}).`;
  } else {
    msg += `${oos.join(', ')} ${oos.length>1?'are':'is'} currently out of stock` +
           (item.restock ? `, expected back ${item.restock}.` : `, no restock date yet.`);
    if(inStock.length) msg += ` ${inStock.join(', ')} still available now.`;
  }
  say(msg);
  mark('resolved:restock-summary');
  chips([
    ["Check a specific size/option", ()=>lookupStock(titleCase(name))],
    ["That helps, thanks", showMenu],
    ["Notify me / talk to a human", ()=>{humanChip();}]
  ]);
  return true;
}

/* ---- Free-text router (keyword + intent matching with light conversational memory, not full NLP) ---- */
function handleFreeText(){
  const input = document.getElementById('freeInput');
  const raw = input.value.trim();
  if(!raw) return;
  say(raw, 'user');
  input.value = '';
  const lower = raw.toLowerCase();

  // --- Small talk / social intents first, so the bot doesn't misroute "hi" or "thanks" ---
  if(/^\s*(hi|hello|hey|good (morning|afternoon|evening))\b/.test(lower)){
    mark('greeting');
    say("Hey there! I can help with order status, returns/refunds, or stock questions — what's up?");
    chips([["Order status", startOrderStatus],["Returns & refunds", startReturns],["Stock availability", startStock]]);
    return;
  }
  if(/thank(s| you)|appreciate it|cheers/.test(lower)){
    mark('thanks');
    say("You're welcome! Anything else I can help with?");
    chips([["Order status", startOrderStatus],["Returns & refunds", startReturns],["Stock availability", startStock],["No, that's all", ()=>{ mark('session-end'); say("Great — have a good one! 👋"); }]]);
    return;
  }
  if(/\b(bye|goodbye|that'?s all|no more questions|i'?m (good|done))\b/.test(lower)){
    mark('session-end');
    say("Sounds good — have a great day! 👋");
    return;
  }
  if(/\b(human|agent|representative|real person|speak to someone)\b/.test(lower)){
    mark('free-text→human');
    say("Of course — connecting you now.");
    humanChip();
    return;
  }
  if(/\b(damaged|broken|defective|wrong item|missing item|never arrived|lost package)\b/.test(lower)){
    mark('free-text→damage-claim');
    say("I'm sorry to hear that — that's not something I can resolve automatically, but I want to get it in front of a person fast.");
    humanChip();
    return;
  }

  // --- Explicit order number anywhere in the message ---
  const upper = raw.toUpperCase().replace(/\bNS\s?(\d{5})\b/, 'NS-$1'); // normalize "NS10234" / "NS 10234" -> "NS-10234"
  const orderMatch = upper.match(/NS-\d{5}/);
  if(orderMatch){ mark('free-text→order-status'); lookupOrder(orderMatch[0]); return; }

  // --- Product mentioned by name ---
  const productHit = Object.keys(INVENTORY).find(p => lower.includes(p));
  if(productHit){
    if(/restock|back in stock|when.*(back|available)/.test(lower)){
      mark('free-text→restock-summary');
      productRestockSummary(productHit);
      return;
    }
    const item = INVENTORY[productHit];
    const variantHit = findVariantKey(item, lower);
    mark('free-text→stock');
    lookupStock(titleCase(productHit), variantHit);
    return;
  }

  // --- Context follow-up: no product named this turn, but we were just talking about one ---
  if(state.lastProduct && INVENTORY[state.lastProduct.toLowerCase()]){
    const item = INVENTORY[state.lastProduct.toLowerCase()];
    const variantHit = findVariantKey(item, lower);
    if(variantHit){
      mark('free-text→followup-variant');
      lookupStock(state.lastProduct, variantHit);
      return;
    }
    if(/restock|back in stock/.test(lower)){
      mark('free-text→followup-restock');
      productRestockSummary(state.lastProduct);
      return;
    }
  }
  // --- Context follow-up: we were just talking about an order ---
  if(state.lastOrderId && /track|tracking|when.*(arrive|ship|come)/.test(lower)){
    mark('free-text→followup-order');
    lookupOrder(state.lastOrderId);
    return;
  }

  // --- Topic-level keywords (no specific product/order named) ---
  if(/return|refund|exchange|send.*back/.test(lower)){ mark('free-text→returns'); startReturns(); return; }
  if(/stock|available|size|inventory|carry/.test(lower)){ mark('free-text→stock'); startStock(); return; }
  if(/order|ship|track|deliver|package|where.*(is|my)/.test(lower)){ mark('free-text→order-status'); startOrderStatus(); return; }

  mark('free-text→unmatched');
  say("I didn't quite catch that — pick a topic below and I'll take it from there.");
  chips([
    ["Order status", startOrderStatus],
    ["Returns & refunds", startReturns],
    ["Stock availability", startStock]
  ]);
}
document.getElementById('freeInput').addEventListener('keydown', e=>{ if(e.key==='Enter') handleFreeText(); });

showMenu();
</script>
</body>
</html>