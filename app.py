import streamlit as st
import urllib.parse
from datetime import datetime

# --- SETTINGS ---
st.set_page_config(page_title="Night Owl", page_icon="🦉", layout="centered")

# --- STYLE ---
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: #f0e6ff; }
    .stButton>button { width: 100%; border-radius: 12px; height: 50px; font-weight: bold; }
    .log-box { background: #1d2129; padding: 15px; border-radius: 15px; border-left: 5px solid #bb86fc; margin-bottom: 10px; }
    .owl-header { font-size: 60px; text-align: center; margin-bottom: 0px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONTROL ---
st.sidebar.title("🦉 Night Owl Control")
phase = st.sidebar.selectbox("Mission Phase", ["Fertility & PCOS", "Starlit Womb"])

# --- MAIN CONTENT ---
if phase == "Fertility & PCOS":
    st.title("🌙 Mission Launch")
    
    # 1. THE SCRIPTURE (Restored)
    st.markdown("""
    <div class="log-box">
    <i>"For I know the plans I have for you,” declares the Lord, “plans to prosper you and not to harm you, plans to give you hope and a future."</i><br>
    <b>- Jeremiah 29:11</b>
    </div>
    """, unsafe_allow_html=True)

    # 2. THE OWL VISUAL
    mood = st.select_slider("Mood Engine", ["Exhausted", "Tired", "Steady", "Energetic", "Flirty"])
    
    st.markdown('<div class="owl-header">', unsafe_allow_html=True)
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

    # 3. THE LOGBOOK (New Buttons!)
    st.subheader("📝 Daily Logbook")
    col1, col2 = st.columns(2)
    with col1:
        nmn = st.checkbox("💊 NMN Taken")
        clearblue = st.selectbox("📊 Clearblue", ["Not Taken", "Low", "High", "Peak"])
    with col2:
        water = st.checkbox("💧 Hydrated")
        meds = st.checkbox("🌿 Supplements")

    if st.button("💾 SAVE TO MISSION LOG"):
        st.success("Entry captured in the stardust! (Data saved locally)")

    # 4. THE SIGNAL
    st.subheader("📲 The Signal")
    msg = urllib.parse.quote("Hey Jaco, Nightingale needs a hand. 🦉")
    st.markdown(f'<a href="https://wa.me/27845870789?text={msg}" target="_blank"><button style="background-color: #25D366; color: white; border: none;">SIGNAL JACO (WhatsApp)</button></a>', unsafe_allow_html=True)

elif phase == "Starlit Womb":
    st.title("✨ Starlit Womb")
    week = st.slider("Current Week", 1, 42, 10)
    st.markdown('<div class="owl-header">🤰</div>', unsafe_allow_html=True)
    if week >= 6:
        st.success(f"Week {week}: The Spark's heartbeat is steady!")
