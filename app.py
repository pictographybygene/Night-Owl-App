import streamlit as st
import urllib.parse

# --- THE NEBULA THEME ---
st.set_page_config(page_title="Night Owl", page_icon="🦉", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(10, 10, 26, 0.95), rgba(10, 10, 26, 0.95)), 
                    url('https://www.transparenttextures.com/patterns/stardust.png'),
                    linear-gradient(180deg, #2D1B4E 0%, #1A0B2E 100%);
        color: #E0D5FF;
    }
    .nebula-card {
        background: rgba(45, 27, 78, 0.6);
        border: 2px solid #BB86FC;
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 0 15px rgba(187, 134, 252, 0.2);
    }
    .stButton>button {
        background: linear-gradient(45deg, #6200EE, #BB86FC);
        color: white;
        border-radius: 30px;
        height: 55px;
        font-weight: bold;
        border: none;
    }
    .signal-btn {
        background-color: #25D366;
        color: white;
        padding: 18px;
        border-radius: 30px;
        text-align: center;
        font-weight: bold;
        text-decoration: none;
        display: block;
        margin-top: 10px;
    }
    h1, h2, h3 { color: #F0E6FF !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🦉 NIGHT OWL</h1>", unsafe_allow_html=True)

# 1. SCRIPTURE CARD
st.markdown("""
<div class="nebula-card">
    <p style="font-size: 19px; font-style: italic; line-height: 1.5;">
        "For I know the plans I have for you,” declares the Lord, “plans to prosper you and not to harm you, plans to give you hope and a future."
    </p>
    <p style="color: #BB86FC; font-weight: bold;">— Jeremiah 29:11</p>
</div>
""", unsafe_allow_html=True)

# 2. MOOD ENGINE
mood = st.select_slider("How is the Nightingale today?", ["Exhausted", "Tired", "Steady", "Energetic", "Flirty"])
st.markdown('<div style="text-align:center; font-size:90px; padding:10px;">', unsafe_allow_html=True)
if mood == "Flirty":
    st.write("✨🦉✨")
    st.subheader("Open-Winged Owl")
    st.caption("Mission Status: Peak Launch Active!")
elif mood in ["Exhausted", "Tired"]:
    st.write("😴🦉💤")
    st.subheader("Sleepy Owl")
    st.caption("Quiet night. Recharging the soul.")
else:
    st.write("👀🦉👀")
    st.subheader("Steady Owl")
    st.caption("Clear skies and steady wings.")
st.markdown('</div>', unsafe_allow_html=True)

# 3. MISSION TRACKING (Mockup Style)
st.markdown('<div class="nebula-card">', unsafe_allow_html=True)
st.subheader("📝 Mission Logbook")
c1, c2 = st.columns(2)
with c1:
    st.checkbox("💊 NMN Taken")
    st.checkbox("📊 Clearblue Peak")
with c2:
    st.checkbox("💧 Hydrated")
    st.checkbox("🌿 Supplements")

if st.button("SAVE TO THE STARS"):
    st.balloons()
    st.success("Entry captured in the nebula!")
st.markdown('</div>', unsafe_allow_html=True)

# 4. THE SIGNAL
st.subheader("📲 The Signal")
msg = urllib.parse.quote("Hey Jaco, Nightingale needs a hand. 🦉")
st.markdown(f'<a href="https://wa.me/27845870789?text={msg}" class="signal-btn">SIGNAL JACO (WhatsApp)</a>', unsafe_allow_html=True)
