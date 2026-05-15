import streamlit as st
import urllib.parse

# --- MOBILE SETUP ---
st.set_page_config(page_title="Night Owl", page_icon="🦉", layout="centered")

# --- GALAXY THEME ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        background-image: radial-gradient(circle at top, #2d1b4e 0%, #0e1117 100%);
        color: #f0e6ff;
    }
    .stButton>button { width: 100%; height: 60px; border-radius: 15px; background: #25D366; color: white; font-weight: bold; border: none; }
    .owl-display { text-align: center; font-size: 80px; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("🦉 Night Owl Control")
app_mode = st.sidebar.selectbox("Mission Phase", ["Fertility & PCOS", "Starlit Womb"])

# --- FERTILITY MODE ---
if app_mode == "Fertility & PCOS":
    st.title("🌙 Mission Launch")
    
    mood = st.select_slider("Mood Engine", ["Exhausted", "Tired", "Steady", "Energetic", "Flirty"])
    
    # THE OWL VISUALS (Using high-quality Emoji Art for 100% reliability on mobile)
    st.markdown('<div class="owl-display">', unsafe_allow_html=True)
    if mood == "Flirty":
        st.header("✨ Open-Winged Owl")
        st.write("✨ 🦉 ✨")
        st.write("*Launch Active! Wings spread wide.*")
    elif mood in ["Exhausted", "Tired"]:
        st.header("🌙 Sleepy Owl")
        st.write("😴 🦉 💤")
        st.write("*Zzz... Quiet night, Nightingale.*")
    else:
        st.write("👀 🦉 👀")
        st.write("*Steady and alert.*")
    st.markdown('</div>', unsafe_allow_html=True)

    # THE SIGNAL
    st.subheader("📲 The Signal")
    # Using the name Jacob (Jaco) as confirmed
    msg = urllib.parse.quote("Hey Jaco, Nightingale needs a hand. 🦉")
    st.markdown(f'<a href="https://wa.me/27845870789?text={msg}" target="_blank"><button>SIGNAL JACO (WhatsApp)</button></a>', unsafe_allow_html=True)

# --- WOMB MODE ---
elif app_mode == "Starlit Womb":
    st.title("✨ Starlit Womb")
    week = st.slider("Week", 1, 40, 10)
    st.markdown('<div class="owl-display">✨🤰✨</div>', unsafe_allow_html=True)
    if week >= 6:
        st.success(f"Week {week}: Heartbeat Active in the Stardust! ❤️")
        
