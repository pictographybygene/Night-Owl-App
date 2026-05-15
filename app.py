import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random
import urllib.parse

# --- MOBILE SETUP ---
st.set_page_config(page_title="Night Owl", page_icon="🦉", layout="centered")

# --- GALAXY THEME ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                    url('https://www.transparenttextures.com/patterns/stardust.png'),
                    linear-gradient(135deg, #2d1b4e 0%, #1a0b2e 100%);
        color: #f0e6ff;
    }
    .stButton>button { width: 100%; height: 60px; border-radius: 15px; background: #bb86fc; color: black; font-weight: bold; border: none; }
    .metric-card { background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 15px; border-left: 4px solid #bb86fc; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR & BIBLE VERSES ---
st.sidebar.title("🦉 Night Owl")
VERSES = [
    "Isaiah 40:31 - Hope in the Lord and renew your strength.",
    "Psalm 139:13 - You knit me together in my mother’s womb.",
    "Philippians 4:13 - I can do all things through Christ.",
    "Proverbs 31:25 - She is clothed with strength and dignity."
]
st.sidebar.info(f"📖 {random.choice(VERSES)}")
app_mode = st.sidebar.selectbox("Mission Phase", ["Fertility & PCOS", "Starlit Womb (3D)", "Nursery Hub"])

# --- FERTILITY MODE ---
if app_mode == "Fertility & PCOS":
    st.title("🌙 Mission Launch")
    mood = st.select_slider("Mood Engine", ["Exhausted", "Tired", "Steady", "Energetic", "Flirty"])
    
    if mood == "Flirty":
        st.header("✨ Open-Winged Owl")
        st.write("🦉 *Launch Active! Wings spread wide.*")
    elif mood in ["Exhausted", "Tired"]:
        st.header("🌙 Sleepy Owl")
        st.write("🦉 *Zzz... Quiet night, Nightingale.*")
    
    st.markdown('<div class="metric-card"><b>Cycle Status:</b> CD 4 - Clean Slate</div>', unsafe_allow_html=True)
    
    # THE JACO SIGNAL
    st.subheader("📲 The Signal")
    msg = urllib.parse.quote("Hey love, Nightingale needs a hand (or a hug). 🦉")
    st.markdown(f'<a href="https://wa.me/27845870789?text={msg}" target="_blank"><button style="width:100%; height:50px; border-radius:10px; background:#25D366; color:white; border:none; cursor:pointer;">SIGNAL JACO (WhatsApp)</button></a>', unsafe_allow_html=True)

# --- 3D WOMB MODE ---
elif app_mode == "Starlit Womb (3D)":
    st.title("✨ Starlit Womb")
    week = st.slider("Week", 4, 12, 5)
    st.subheader(f"Week {week}: The Spark")
    if week >= 5: st.success("💓 Heartbeat Active in the Stardust!")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzZ4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKMGpxx6rD8tE40/giphy.gif")
