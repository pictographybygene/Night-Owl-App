import streamlit as st

st.set_page_config(
    page_title="Night Owl",
    page_icon="🦉",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Orbitron:wght@700&display=swap');

html, body, .stApp {
    background: #0d0118 !important;
    color: #f0e6ff;
    font-family: 'Nunito', sans-serif;
}
.stApp::before {
    content: '';
    position: fixed; inset: 0;
    background-image:
        radial-gradient(1px 1px at 7%  11%, rgba(255,255,255,0.9) 0%, transparent 100%),
        radial-gradient(1px 1px at 19% 43%, rgba(204,153,255,0.8) 0%, transparent 100%),
        radial-gradient(1px 1px at 34%  8%, rgba(255,255,255,0.7) 0%, transparent 100%),
        radial-gradient(1px 1px at 52% 67%, rgba(255,255,255,0.8) 0%, transparent 100%),
        radial-gradient(1px 1px at 65% 22%, rgba(204,153,255,0.7) 0%, transparent 100%),
        radial-gradient(1px 1px at 81% 53%, rgba(255,255,255,0.9) 0%, transparent 100%),
        radial-gradient(2px 2px at 90% 78%, rgba(187,134,252,0.8) 0%, transparent 100%),
        radial-gradient(2px 2px at 13% 83%, rgba(255,255,255,0.7) 0%, transparent 100%),
        radial-gradient(1px 1px at 58% 38%, rgba(204,153,255,0.9) 0%, transparent 100%),
        radial-gradient(1px 1px at 43% 55%, rgba(255,255,255,0.7) 0%, transparent 100%),
        radial-gradient(1px 1px at 27% 71%, rgba(187,134,252,0.5) 0%, transparent 100%);
    pointer-events: none; z-index: 0;
    animation: twinkle 8s ease-in-out infinite alternate;
}
@keyframes twinkle { 0%{opacity:.5} 100%{opacity:1} }

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#130a2a 0%,#0d0118 100%) !important;
    border-right: 1px solid rgba(187,134,252,0.15) !important;
}
section[data-testid="stSidebar"] * { color:#e8d9ff !important; }

/* ── App Cards ── */
.app-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(187,134,252,0.2);
    border-radius: 22px; padding:20px; margin-bottom:14px;
}
/* ── Hero Banner ── */
.hero-banner {
    background: linear-gradient(135deg,#6b21a8 0%,#9333ea 50%,#c026d3 100%);
    border-radius: 26px; padding:28px 24px 22px;
    margin-bottom:16px; text-align:center;
    box-shadow: 0 8px 32px rgba(147,51,234,0.4);
    position:relative; overflow:hidden;
}
.hero-banner::after {
    content:''; position:absolute; top:-40%; right:-20%;
    width:200px; height:200px;
    background:rgba(255,255,255,0.06); border-radius:50%;
}
.hero-day { font-size:3.5em; font-weight:900; color:#fff; line-height:1; margin:8px 0 4px; }
.hero-subtitle { font-size:1em; color:rgba(255,255,255,0.8); font-weight:600; }
.hero-phase {
    display:inline-block; background:rgba(255,255,255,0.2);
    border-radius:20px; padding:4px 14px; font-size:0.82em;
    color:#fff; font-weight:700; margin-top:8px; letter-spacing:0.06em;
}
.fertility-badge {
    position:absolute; top:20px; right:20px;
    background:rgba(255,255,255,0.15); border-radius:16px; padding:8px 12px; text-align:center;
}
.fertility-pct { font-size:1.4em; font-weight:900; color:#fff; }
.fertility-lbl { font-size:0.65em; color:rgba(255,255,255,0.75); display:block; letter-spacing:0.05em; }
/* ── Calendar strip ── */
.cal-strip {
    display:flex; justify-content:space-between; align-items:center;
    background:rgba(255,255,255,0.05); border:1px solid rgba(187,134,252,0.18);
    border-radius:18px; padding:12px 14px; margin-bottom:16px; gap:4px;
}
.cal-day { display:flex; flex-direction:column; align-items:center; gap:5px; flex:1; }
.cal-day-name { font-size:0.65em; font-weight:700; color:#7c5cbf; text-transform:uppercase; letter-spacing:0.04em; }
.cal-day-num {
    width:34px; height:34px; display:flex; align-items:center; justify-content:center;
    border-radius:50%; font-size:0.9em; font-weight:800; color:#c4b0e8;
}
.cal-day-num.today  { background:linear-gradient(135deg,#9333ea,#c026d3); color:#fff; box-shadow:0 2px 10px rgba(147,51,234,0.5); }
.cal-day-num.period { background:rgba(236,72,153,0.25); color:#f472b6; }
.cal-dot { width:6px; height:6px; border-radius:50%; background:transparent; }
.cal-dot.period  { background:#f472b6; }
.cal-dot.today   { background:#a855f7; }
.cal-dot.fertile { background:#fbbf24; }
/* ── Section label ── */
.section-lbl { font-size:1.05em; font-weight:800; color:#d8b4fe; margin:18px 0 10px; }
/* ── Chips ── */
.chip-grid { display:flex; flex-wrap:wrap; gap:8px; margin-bottom:6px; }
.chip {
    display:inline-flex; align-items:center; gap:6px;
    background:rgba(255,255,255,0.07); border:1.5px solid rgba(187,134,252,0.25);
    border-radius:50px; padding:7px 14px;
    font-family:'Nunito',sans-serif; font-size:0.88em; font-weight:700; color:#c4b0e8;
    cursor:pointer; white-space:nowrap;
}
.chip.selected { background:linear-gradient(135deg,rgba(147,51,234,0.5),rgba(192,38,211,0.4)); border-color:#a855f7; color:#fff; box-shadow:0 2px 10px rgba(147,51,234,0.35); }
.chip.red      { background:rgba(244,63,94,0.2); border-color:#f43f5e; color:#fda4af; }
/* ── Insight cards ── */
.insight-row { display:flex; gap:12px; overflow-x:auto; padding-bottom:6px; scrollbar-width:none; }
.insight-row::-webkit-scrollbar { display:none; }
.insight-card {
    min-width:140px; background:rgba(255,255,255,0.06); border:1px solid rgba(187,134,252,0.2);
    border-radius:18px; padding:14px; flex-shrink:0; font-size:0.82em; color:#c4b0e8; font-weight:600; line-height:1.4;
}
.insight-card .ic-emoji { font-size:1.5em; margin-bottom:6px; display:block; }
/* ── Buttons ── */
.stButton > button {
    width:100%; border-radius:50px !important; height:3.2em;
    background:linear-gradient(135deg,#9333ea 0%,#c026d3 100%) !important;
    color:#fff !important; font-family:'Nunito',sans-serif !important;
    font-weight:800 !important; font-size:1em !important; letter-spacing:0.04em;
    border:none !important; box-shadow:0 4px 18px rgba(147,51,234,0.4);
    transition:all 0.2s ease;
}
.stButton > button:hover { transform:translateY(-2px); box-shadow:0 8px 28px rgba(147,51,234,0.55) !important; }
/* ── Inputs ── */
.stTextArea textarea, .stTextInput input, .stSelectbox [data-baseweb="select"]>div {
    background:rgba(255,255,255,0.06) !important; border:1.5px solid rgba(187,134,252,0.3) !important;
    border-radius:16px !important; color:#f0e6ff !important; font-family:'Nunito',sans-serif !important;
}
.stSlider [role="slider"] { background-color:#a855f7 !important; }
/* ── Log entries ── */
.log-entry { background:rgba(147,51,234,0.08); border-left:3px solid #a855f7; border-radius:0 14px 14px 0; padding:10px 15px; margin-bottom:10px; font-size:0.9em; color:#d8b4fe; }
.log-date { font-weight:800; color:#a855f7; font-size:0.8em; letter-spacing:0.06em; text-transform:uppercase; }
/* ── WhatsApp ── */
.wa-button {
    display:block; background:linear-gradient(90deg,#25D366,#128C7E); color:#fff !important;
    padding:17px 24px; border-radius:50px; text-align:center;
    font-family:'Nunito',sans-serif; font-weight:800; font-size:1.05em;
    text-decoration:none !important; box-shadow:0 4px 18px rgba(37,211,102,0.3); transition:all 0.2s;
}
.wa-button:hover { transform:translateY(-2px); box-shadow:0 8px 28px rgba(37,211,102,0.45); }
/* ── Womb ── */
.womb-egg {
    width:220px; height:270px;
    background:radial-gradient(ellipse at 40% 35%,rgba(120,70,200,0.5) 0%,rgba(30,10,60,0.9) 60%,rgba(10,5,20,0.97) 100%);
    border-radius:50% 50% 45% 45% / 55% 55% 45% 45%;
    border:1.5px solid rgba(187,134,252,0.35);
    box-shadow:0 0 40px rgba(147,51,234,0.3),inset 0 0 30px rgba(147,51,234,0.08);
    margin:0 auto; display:flex; align-items:center; justify-content:center;
    position:relative; animation:womb-glow 4s ease-in-out infinite;
}
@keyframes womb-glow {
    0%,100%{box-shadow:0 0 40px rgba(147,51,234,0.3),inset 0 0 30px rgba(147,51,234,0.08)}
    50%    {box-shadow:0 0 65px rgba(147,51,234,0.5),inset 0 0 40px rgba(147,51,234,0.14)}
}
.womb-baby { font-size:3.5em; animation:float-baby 5s ease-in-out infinite; filter:drop-shadow(0 0 14px rgba(187,134,252,0.8)); }
@keyframes float-baby { 0%,100%{transform:translateY(0) rotate(-3deg)} 50%{transform:translateY(-12px) rotate(3deg)} }
.heartbeat-dot { width:12px;height:12px;background:#f43f5e;border-radius:50%;display:inline-block;animation:hb 1s ease-in-out infinite;box-shadow:0 0 10px #f43f5e;margin-right:6px;vertical-align:middle; }
@keyframes hb { 0%,100%{transform:scale(1)} 14%{transform:scale(1.4)} 28%{transform:scale(1)} 42%{transform:scale(1.25)} 70%{transform:scale(1)} }
/* ── Owl animations ── */
.owl-sleepy    {font-size:5em;display:inline-block;animation:nod 3s ease-in-out infinite;filter:drop-shadow(0 0 14px #555599)}
.owl-tired     {font-size:5em;display:inline-block;animation:tired-bob 4s ease-in-out infinite;filter:drop-shadow(0 0 12px #7755aa)}
.owl-steady    {font-size:5em;display:inline-block;animation:steady-p 2.8s ease-in-out infinite;filter:drop-shadow(0 0 16px #a855f7)}
.owl-energetic {font-size:5em;display:inline-block;animation:bounce .65s cubic-bezier(.36,.07,.19,.97) infinite alternate;filter:drop-shadow(0 0 20px #fbbf24)}
.owl-flirty    {font-size:5.5em;display:inline-block;animation:flirty 1.8s ease-in-out infinite;filter:drop-shadow(0 0 28px #f472b6)}
@keyframes nod       {0%,100%{transform:rotate(0) translateY(0)}40%{transform:rotate(-10deg) translateY(5px)}70%{transform:rotate(6deg) translateY(2px)}}
@keyframes tired-bob {0%,100%{transform:translateY(0);opacity:1}50%{transform:translateY(-7px);opacity:.7}}
@keyframes steady-p  {0%,100%{transform:scale(1);filter:drop-shadow(0 0 12px #a855f7)}50%{transform:scale(1.08);filter:drop-shadow(0 0 26px #c084fc)}}
@keyframes bounce    {0%{transform:translateY(0) rotate(-5deg)}100%{transform:translateY(-20px) rotate(5deg)}}
@keyframes flirty    {0%{transform:rotate(-14deg) scale(1)}25%{transform:rotate(14deg) scale(1.14)}50%{transform:rotate(-9deg) scale(1)}75%{transform:rotate(9deg) scale(1.1)}100%{transform:rotate(-14deg) scale(1)}}
/* ── Prog bar ── */
.prog-bar-wrap { background:rgba(255,255,255,0.08);border-radius:20px;height:10px;overflow:hidden;border:1px solid rgba(187,134,252,0.15);margin:10px 0; }
.prog-bar-fill { height:100%;border-radius:20px;background:linear-gradient(90deg,#7c3aed,#a855f7,#f472b6);box-shadow:0 0 8px rgba(168,85,247,0.5); }
#MainMenu,footer,header{visibility:hidden}
div[data-testid="stDecoration"]{display:none}
.block-container{padding-top:1rem !important;padding-bottom:2rem !important}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style='text-align:center;padding:22px 0 14px;'>
        <div style='font-size:2.6em;'>🦉</div>
        <div style='font-family:Nunito,sans-serif;font-weight:900;font-size:1.15em;color:#d8b4fe;margin-top:6px;'>Night Owl</div>
        <div style='font-size:0.68em;color:#4c2a7a;letter-spacing:0.1em;font-family:Orbitron,sans-serif;margin-top:2px;'>✦ SUITE ✦</div>
    </div>
    <hr style='border-color:rgba(187,134,252,0.15);margin:0 0 16px;'>
    """, unsafe_allow_html=True)

    page = st.radio("nav", [
        "🌸  Today",
        "📝  Daily Log",
        "🌌  Womb Tracker",
        "📡  Signal Jaco",
    ], label_visibility="collapsed")

    st.markdown("""
    <hr style='border-color:rgba(187,134,252,0.1);margin:20px 0 12px;'>
    <div style='font-size:0.72em;color:#3d1f6a;text-align:center;font-family:Nunito,sans-serif;font-weight:700;'>
        Made with 💜 for Nightingale
    </div>
    """, unsafe_allow_html=True)

if page == "🌸  Today":
    from pages_logic.today import render
    render()
elif page == "📝  Daily Log":
    from pages_logic.daily_log import render
    render()
elif page == "🌌  Womb Tracker":
    from pages_logic.womb_visualizer import render
    render()
elif page == "📡  Signal Jaco":
    from pages_logic.signal_jaco import render
    render()
  
