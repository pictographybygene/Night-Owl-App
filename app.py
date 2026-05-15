import streamlit as st
import urllib.parse

# --- THE NEBULA THEME ---
st.set_page_config(page_title="Night Owl", page_icon="🦉", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(10, 10, 26, 0.9), rgba(10, 10, 26, 0.9)), 
                    url('https://www.transparenttextures.com/patterns/stardust.png'),
                    linear-gradient(180deg, #2D1B4E 0%, #1A0B2E 100%);
        color: #E0D5FF;
    }
    .nebula-card {
        background: rgba(45, 27, 78, 0.5);
        border: 2px solid #BB86FC;
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 20px;
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(45deg, #6200EE, #BB86FC);
        color: white;
        border-radius: 25px;
        height: 50px;
        font-weight: bold;
        border: none;
    }
    .signal-btn {
        background-color: #25D366;
        color: white;
        padding: 15px;
        border-radius: 25px;
        text-align: center;
        font-weight: bold;
        text-decoration: none;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>🦉 NIGHT OWL</h1>", unsafe_allow_html=True)

# SCRIPTURE
st.markdown("""
<div class="nebula-card">
    <p style="font-size: 18px; font-style: italic;">"For I know the plans I have for you..."</p>
    <p><b>Jeremiah 29:11</b></p>
</div>
""", unsafe_allow_html=True)

# MOOD OWL
mood = st.select_slider("Energy Level", ["Exhausted", "Tired", "Steady", "Energetic", "Flirty"])
st.markdown('<div style="text-align:center; font-size:80px; padding:10px;">', unsafe_allow_html=True)
if mood == "Flirty":
    st.write("✨🦉✨")
    st.subheader("Open-Winged Owl")
elif mood in ["Exhausted", "Tired"]:
    st.write("😴🦉💤")
    st.subheader("Sleepy Owl")
else:
    st.write("👀🦉👀")
    st.subheader("Steady Owl")
st.markdown('</div>', unsafe_allow_html=True)

# LOGGING
st.markdown('<div class="nebula-card">', unsafe_allow_html=True)
st.subheader("📝 Mission Tracking")
c1, c2 = st.columns(2)
with c1:
    st.checkbox("💊 NMN Taken")
    st.checkbox("📊 Clearblue Peak")
with c2:
    st.checkbox("💧 Hydrated")
    st.checkbox("🌿 Supplements")
if st.button("SAVE TO THE STARS"):
    st.balloons()
st.markdown('</div>', unsafe_allow_html=True)

# THE SIGNAL
st.subheader("📲 The Signal")
msg = urllib.parse.quote("Hey Jaco, Nightingale needs a hand. 🦉")
st.markdown(f'<a href="https://wa.me/27845870789?text={msg}" class="signal-btn">SIGNAL JACO (WhatsApp)</a>', unsafe_allow_html=True)
