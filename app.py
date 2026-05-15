import streamlit as st
import urllib.parse

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Night Owl",
    page_icon="🦉",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- THEME & STYLING (APP INTERFACE FOCUS) ---
st.markdown("""
    <style>
    /* Force a dark galaxy background and hide default headers to make it feel like an App */
    [data-testid="stHeader"] {background: rgba(0,0,0,0);}
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                    linear-gradient(135deg, #1a0b2e 0%, #090912 100%);
        color: #f0e6ff;
    }
    
    /* Neon Nebula Card Style */
    .nebula-card {
        background: rgba(255, 255, 255, 0.03);
        border: 2px solid #bb86fc;
        border-radius: 25px;
        padding: 25px;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 0 20px rgba(187, 134, 252, 0.3);
    }
    
    /* App-style Navigation Buttons */
    .nav-button {
        background: #bb86fc;
        color: black !important;
        padding: 15px;
        border-radius: 20px;
        text-decoration: none;
        display: block;
        margin: 10px 0;
        font-weight: bold;
        text-align: center;
        box-shadow: 0 4px 15px rgba(187, 134, 252, 0.4);
    }
    
    /* Styled Inputs */
    .stTextArea textarea, .stSelectbox div {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-radius: 15px !important;
        color: white !important;
    }
    
    .stSlider > div > div > div > div { background-color: #bb86fc; }
    
    /* Hide Streamlit Menu for "App" feel */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- LOGIN / SECURITY ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #bb86fc;'>🔒 NIGHT OWL ACCESS</h1>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="nebula-card">', unsafe_allow_html=True)
        user = st.text_input("Identify Yourself", placeholder="Username")
        password = st.text_input("Star-Key", type="password", placeholder="Password")
        if st.button("ENTER GALAXY"):
            # Simple check for Jaco or User
            if password == "Nightingale2026": 
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Access Denied. Check your Star-Key.")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- MAIN MENU LOGIC ---
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# --- SIDEBAR MENU (Modern App Style) ---
with st.sidebar:
    st.markdown("<h2 style='color: #bb86fc;'>🦉 Menu</h2>", unsafe_allow_html=True)
    if st.button("🌌 Home View"): st.session_state.page = "Home"
    if st.button("📝 Log Entry"): st.session_state.page = "Log"
    if st.button("📊 Progress"): st.session_state.page = "Stats"
    st.markdown("---")
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

# --- PAGE 1: HOME ---
if st.session_state.page == "Home":
    st.markdown("<h1 style='text-align: center; color: #bb86fc; text-shadow: 0 0 15px #bb86fc;'>🦉 NIGHT OWL</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="nebula-card">
            <i style='font-size: 1.2em; color: #f0e6ff;'>"For I know the plans I have for you..."</i><br>
            <b style='color: #bb86fc; font-size: 1.1em;'>Jeremiah 29:11</b>
        </div>
        """, unsafe_allow_html=True)

    mood = st.select_slider("Current Energy Level", options=["Exhausted", "Tired", "Steady", "Energetic", "Flirty"])

    if mood == "Flirty":
        st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKMGpxx6rD8tE40/giphy.gif")
        st.markdown("<h3 style='text-align: center; color: #bb86fc;'>✨ Open-Winged Owl</h3>", unsafe_allow_html=True)
    else:
        st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzZ4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV5R8Bv1iU/giphy.gif")
        st.markdown("<h3 style='text-align: center; color: #f0e6ff;'>🌙 Sleepy Owl</h3>", unsafe_allow_html=True)

    # Big "Action" Button to go to Log
    if st.button("➕ LOG YOUR DAY"):
        st.session_state.page = "Log"
        st.rerun()

# --- PAGE 2: LOG ENTRY ---
elif st.session_state.page == "Log":
    st.markdown("<h2 style='color: #bb86fc;'>📝 Mission Log</h2>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="nebula-card">', unsafe_allow_html=True)
        meds = st.text_area("Medications & Supplements", placeholder="NMN, Vit D, etc...")
        notes = st.text_area("Observations", placeholder="How are we feeling?")
        cb = st.selectbox("📊 Clearblue Result", ["Not Taken", "Low", "High", "Peak"])
        
        if st.button("💾 SAVE TO THE STARS"):
            st.balloons()
            st.success("Entry captured in the galaxy!")
            st.session_state.page = "Home"
        st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("⬅ BACK"): 
        st.session_state.page = "Home"
        st.rerun()

# --- FOOTER SIGNAL (Always visible) ---
st.markdown("---")
msg = urllib.parse.quote("Hey Jaco, Nightingale needs a hand. 🦉")
whatsapp_url = f"https://wa.me/27845870789?text={msg}"

st.markdown(f"""
    <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
        <div style="
            width: 100%; 
            height: 60px; 
            background: #25D366; 
            color: white; 
            border-radius: 20px; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            font-weight: bold;
            font-size: 1.1em;
            box-shadow: 0 4px 15px rgba(0,0,0,0.4);">
            SIGNAL JACO (WhatsApp)
        </div>
    </a>
    """, unsafe_allow_html=True)
