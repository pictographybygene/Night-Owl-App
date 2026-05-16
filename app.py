import streamlit as st

import urllib.parse

# --- PAGE CONFIGURATION ---

st.set_page_config(

    page_title="Night Owl",

    page_icon="🦉",

    layout="centered",

    initial_sidebar_state="collapsed"

)

# --- THEME & STYLING (3D GALAXY RENDERINGS) ---

st.markdown("""

    <style>

    /* Galaxy Background with Depth */

    .stApp {

        background: radial-gradient(circle at center, #2d1b4e 0%, #090912 100%);

        color: #f0e6ff;

    }

    

    /* 3D Glassmorphism Card Effect */

    .nebula-card {

        background: rgba(255, 255, 255, 0.03);

        border: 2px solid rgba(187, 134, 252, 0.4);

        border-radius: 25px;

        padding: 25px;

        margin-bottom: 25px;

        text-align: center;

        backdrop-filter: blur(10px);

        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(187, 134, 252, 0.1);

    }

    

    /* Neumorphic 3D Buttons */

    .stButton>button {

        width: 100%;

        border-radius: 20px;

        height: 3.8em;

        background: linear-gradient(145deg, #bb86fc, #9965f4);

        color: #000000;

        font-weight: bold;

        border: none;

        box-shadow: 5px 5px 15px rgba(0,0,0,0.3), -2px -2px 10px rgba(255,255,255,0.05);

        transition: all 0.3s ease;

    }

    

    .stButton>button:hover {

        transform: translateY(-2px);

        box-shadow: 0 8px 20px rgba(153, 101, 244, 0.4);

        color: #ffffff;

    }

    

    /* 3D Input Fields */

    .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {

        background-color: rgba(255, 255, 255, 0.05) !important;

        border: 1px solid rgba(187, 134, 252, 0.3) !important;

        border-radius: 15px !important;

        color: #f0e6ff !important;

        box-shadow: inset 2px 2px 5px rgba(0,0,0,0.5);

    }

    

    .stSlider > div > div > div > div {

        background-color: #bb86fc;

    }

    </style>

    """, unsafe_allow_html=True)

# --- HEADER SECTION ---

st.markdown("<h1 style='text-align: center; color: #bb86fc; text-shadow: 0 0 15px #bb86fc;'>🦉 NIGHT OWL # ", unsafe_allow_html=True)

# --- SPIRITUAL COMPONENT (NEBULA CARD) ---

st.markdown("""

    <div class="nebula-card">

        <i style='font-size: 1.2em; opacity: 0.9;'>"For I know the plans I have for you..."_

        <b style='color: #bb86fc; font-size: 1.3em;'>Jeremiah 29:11**

    

    """, unsafe_allow_html=True)

# --- INTERACTIVE OWL INTERFACE ---

mood = st.select_slider("Energy Level", options=["Exhausted", "Tired", "Steady", "Energetic", "Flirty"])

# Logic for Dynamic Image Renderings

if mood == "Flirty":

    st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKMGpxx6rD8tE40/giphy.gif")

    st.markdown("<h3 style='text-align: center; color: #bb86fc;'>✨ Open-Winged Owl", unsafe_allow_html=True)

elif mood == "Exhausted":

    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzZ4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV5R8Bv1iU/giphy.gif")

    st.markdown("<h3 style='text-align: center;'>🌙 Sleepy Owl", unsafe_allow_html=True)

else:

    # High-quality Observant Owl Rendering

    st.image("[suspicious link removed]")

    st.markdown("<h3 style='text-align: center;'>🦉 Observant Owl", unsafe_allow_html=True)

# --- MISSION LOG (3D FORM SECTION) ---

with st.container():

    st.markdown('<div class="nebula-card">', unsafe_allow_html=True)

    st.subheader("📝 Mission Log")

    

    med_notes = st.text_area("Medications & Daily Notes", placeholder="Record NMN, supplements, and health data...")

    clearblue = st.selectbox("📊 Clearblue Result", ["Not Taken", "Low", "High", "Peak"])

    

    if st.button("💾 SAVE TO THE STARS"):

        st.balloons()

        st.success("Mission Log safely recorded in the galaxy!")

    st.markdown('', unsafe_allow_html=True)

# --- EMERGENCY SIGNAL (WHATSAPP 3D BUTTON) ---

msg = urllib.parse.quote("Hey Jaco, Nightingale needs a hand. 🦉")

whatsapp_url = f"https://wa.me/27845870789?text={msg}"

st.markdown(f"""

    <a href='{whatsapp_url}' target='_blank' style='text-decoration: none;'>

        <div style='

            width: 100%; 

            height: 65px; 

            background: linear-gradient(145deg, #25D366, #128C7E); 

            color: white; 

            border-radius: 20px; 

            display: flex; 

            justify-content: center; 

            align-items: center; 

            font-weight: bold;

            font-size: 1.2em;

            box-shadow: 0 10px 20px rgba(0,0,0,0.3);'>

            SIGNAL JACO (WhatsApp)

        

    

    """, unsafe_allow_html=True)

```
