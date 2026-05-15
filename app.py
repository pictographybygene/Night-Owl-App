import streamlit as st
import random
import urllib.parse

# --- MOBILE SETUP ---
st.set_page_config(page_title="Night Owl", page_icon="🦉", layout="centered")

# --- GALAXY THEME ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                    linear-gradient(135deg, #2d1b4e 0%, #1a0b2e 100%);
        color: #f0e6ff;
    }
    .stButton>button { width: 100%; height: 60px; border-radius: 15px; background: #bb86fc; color: black; font-weight: bold; border: none; }
    .owl-container { text-align: center; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("🦉 Night Owl")
app_mode = st.sidebar.selectbox("Mission Phase", ["Fertility & PCOS", "Starlit Womb (3D)"])

# --- FERTILITY MODE ---
if app_mode == "Fertility & PCOS":
    st.title("🌙 Mission Launch")
    
    mood = st.select_slider("Mood Engine", ["Exhausted", "Tired", "Steady", "Energetic", "Flirty"])
    
    # THE OWL VISUALS
    st.markdown('<div class="owl-container">', unsafe_allow_html=True)
    if mood == "Flirty":
        st.header("✨ Open-Winged Owl")
        # This pulls a sparkling owl image
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKMGpxx6rD8tE40/giphy.gif", width=300)
        st.write("🦉 *Launch Active! Wings spread wide.*")
    elif mood in ["Exhausted", "Tired"]:
        st.header("🌙 Sleepy Owl")
        # This pulls a cozy, sleeping owl image
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzZ4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV5R8Bv1iU/giphy.gif", width=300)
        st.write("🦉 *Zzz... Time to recharge the Nightingale.*")
    else:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzZ4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKVUn7iM8FMEU24/giphy.gif", width=300)
    st.markdown('</div>', unsafe_allow_html=True)

    # THE SIGNAL
    st.subheader("📲 The Signal")
    msg = urllib.parse.quote("Hey love, Nightingale needs a hand (or a hug). 🦉")
    st.markdown(f'<a href="https://wa.me/27845870789?text={msg}" target="_blank"><button>SIGNAL JACO (WhatsApp)</button></a>', unsafe_allow_html=True)

# --- 3D WOMB MODE ---
elif app_mode == "Starlit Womb (3D)":
    st.title("✨ Starlit Womb")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzZ4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKVUn7iM8FMEU24/giphy.gif")
    st.info("The Spark is flickering in the stardust...")
    
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
