let cards = [];
let order = [];
let idx = 0;

const LS_KEY = "nonverbal_cards_state_v1";

function saveState(){
  localStorage.setItem(LS_KEY, JSON.stringify({
    idx, order,
    shuffle: document.getElementById("shuffleToggle").checked
  }));
}
function loadState(){
  try{ return JSON.parse(localStorage.getItem(LS_KEY)||"null"); }catch{ return null; }
}
function shuffleArray(a){
  a = [...a];
  for(let i=a.length-1;i>0;i--){
    const j = Math.floor(Math.random()*(i+1));
    [a[i],a[j]]=[a[j],a[i]];
  }
  return a;
}
function setCounter(){ document.getElementById("counter").textContent = `${idx+1} / ${order.length}`; }
function typesetMath(){ if(window.MathJax?.typesetPromise){ MathJax.typesetPromise(); } }

function renderCard(){
  const c = cards[order[idx]];
  document.getElementById("topic").textContent = `【${c.topic}】`;
  document.getElementById("formula").innerHTML = `\\[ ${c.formula_latex} \\]`;
  document.getElementById("question").textContent = c.question;
  document.getElementById("answer").innerHTML = `\\( ${c.answer} \\)`;
  const hint = document.getElementById("hint");
  hint.textContent = c.hint || "";
  document.getElementById("answer").classList.add("hidden");
  hint.classList.add("hidden");
  setCounter(); typesetMath(); saveState();
}
function nextCard(){ idx=(idx+1)%order.length; renderCard(); }
function prevCard(){ idx=(idx-1+order.length)%order.length; renderCard(); }
function applyShuffle(checked){
  order = checked ? shuffleArray(order) : [...Array(cards.length).keys()];
  idx=0; renderCard();
}

async function init(){
  const res = await fetch("/api/cards");
  cards = (await res.json()).cards || [];
  order = [...Array(cards.length).keys()];

  const saved = loadState();
  if(saved?.order?.length===cards.length){
    order = saved.order; idx = Math.min(Math.max(saved.idx||0,0), order.length-1);
    document.getElementById("shuffleToggle").checked = !!saved.shuffle;
  }

  document.getElementById("nextBtn").addEventListener("click", nextCard);
  document.getElementById("prevBtn").addEventListener("click", prevCard);
  document.getElementById("toggleAnsBtn").addEventListener("click", ()=>document.getElementById("answer").classList.toggle("hidden"));
  document.getElementById("hintBtn").addEventListener("click", ()=>document.getElementById("hint").classList.toggle("hidden"));
  document.getElementById("shuffleToggle").addEventListener("change", e=>applyShuffle(e.target.checked));

  // スワイプ（片手操作）
  let startX=null;
  document.body.addEventListener("touchstart", e=>{ startX=e.changedTouches[0].clientX; }, {passive:true});
  document.body.addEventListener("touchend", e=>{
    if(startX===null) return;
    const dx=e.changedTouches[0].clientX-startX;
    if(dx>50) prevCard(); if(dx<-50) nextCard();
    startX=null;
  }, {passive:true});

  if (document.getElementById("shuffleToggle").checked) order = shuffleArray(order);
  renderCard();
}
init();
