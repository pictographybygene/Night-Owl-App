import streamlit as st

import urllib.parse

# --- MOBILE OPTIMIZATION & CONFIG ---

st.set_page_config(

    page_title="Night Owl v3",

    page_icon="🦉",

    layout="centered",

    initial_sidebar_state="collapsed"

)

# --- 3D GALAXY RENDERED UI (MOBILE STABLE) ---

st.markdown("""

    <style>

    /* Full Page Background */

    .stApp {

        background: radial-gradient(circle at center, #1b1133 0%, #050508 100%);

        color: #e0d5ff;

    }

    

    /* Neumorphic 3D Glass Cards */

    .glass-card {

        background: rgba(255, 255, 255, 0.05);

        border: 1px solid rgba(187, 134, 252, 0.3);

        border-radius: 20px;

        padding: 18px;

        margin-bottom: 15px;

        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);

        backdrop-filter: blur(8px);

        -webkit-backdrop-filter: blur(8px);

        text-align: center;

    }

    

    /* Visual separation for the scripture */

    .scripture-text {

        font-size: 1.1em;

        font-style: italic;

        color: #d1b3ff;

        margin-bottom: 5px;

    }

    

    /* 3D "Tactile" Buttons */

    .stButton > button {

        width: 100%;

        border-radius: 12px;

        height: 3.2em;

        background: linear-gradient(145deg, #bb86fc, #7c4dff);

        color: #ffffff !important;

        font-weight: bold;

        border: none;

        box-shadow: 0 4px 15px rgba(124, 77, 255, 0.4);

        text-transform: uppercase;

        letter-spacing: 1px;

    }

    

    /* Mobile-Specific Input Tweaks */

    .stTextArea textarea {

        background-color: rgba(0, 0, 0, 0.3) !important;

        border: 1px solid #bb86fc !important;

        color: white !important;

        border-radius: 10px !important;

    }

    

    .stSelectbox div[data-baseweb="select"] {

        background-color: rgba(0, 0, 0, 0.3) !important;

        border: 1px solid #bb86fc !important;

        border-radius: 10px !important;

    }

    </style>

    """, unsafe_allow_html=True)

# --- APP HEADER ---

st.markdown("<h1 style='text-align: center; color: #bb86fc; text-shadow: 0 0 10px #bb86fc;'>🦉 NIGHT OWL v3 # ", unsafe_allow_html=True)

st.markdown("""

    <div class="glass-card">

        <p class="scripture-text">"For I know the plans I have for you..."

        <b style="color: #bb86fc;">Jeremiah 29:11**

    

    """, unsafe_allow_html=True)

# --- INTERACTIVE TELEMETRY (ENERGY) ---

st.markdown("<p style='text-align: center; margin-bottom: 0px;'>⚡ ENERGY STATE", unsafe_allow_html=True)

mood = st.select_slider(

    "Mood Slider",

    options=["Exhausted", "Tired", "Steady", "Energetic", "Flirty"],

    label_visibility="collapsed"

)

# Render Assets based on state

if mood == "Flirty":

    st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKMGpxx6rD8tE40/giphy.gif", use_container_width=True)

    st.markdown("<h3 style='text-align: center; color: #bb86fc;'>✨ OPEN-WINGED OWL", unsafe_allow_html=True)

elif mood == "Exhausted":

    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzZ4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV5R8Bv1iU/giphy.gif", use_container_width=True)

    st.markdown("<h3 style='text-align: center;'>🌙 SLEEPY OWL", unsafe_allow_html=True)

else:

    st.image("[suspicious link removed]", use_container_width=True)

    st.markdown("<h3 style='text-align: center;'>🦉 OBSERVANT OWL", unsafe_allow_html=True)

# --- MISSION LOG ---

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.markdown("<h4 style='color: #bb86fc; margin-bottom: 10px;'>📝 MISSION LOG", unsafe_allow_html=True)

med_notes = st.text_area("Medications/Daily Notes", placeholder="Track NMN, vitamins, energy level...", label_visibility="collapsed")

clearblue = st.selectbox("📊 Clearblue Result", ["Not Taken", "Low", "High", "Peak"])

if st.button("💾 SAVE TO THE STARS"):

    st.balloons()

    st.success("TELEMETRY LOGGED!")

st.markdown('', unsafe_allow_html=True)

# --- QUICK SIGNAL (WHATSAPP) ---

msg = urllib.parse.quote("Hey Jaco, Nightingale needs a hand. 🦉")

whatsapp_url = f"https://wa.me/27845870789?text={msg}"

st.markdown(f"""

    <a href='{whatsapp_url}' target='_blank' style='text-decoration: none;'>

        <div style='

            width: 100%; 

            height: 60px; 

            background: linear-gradient(90deg, #25D366, #128C7E); 

            color: white; 

            border-radius: 15px; 

            display: flex; 

            justify-content: center; 

            align-items: center; 

            font-weight: 800;

            font-size: 1.1em;

            box-shadow: 0 4px 15px rgba(0,0,0,0.4);

            margin-top: 10px;'>

            SIGNAL JACO (WhatsApp)

        

    

    """, unsafe_allow_html=True)

```
