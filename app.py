import streamlit as st

import urllib.parse

# --- PAGE CONFIGURATION ---

st.set_page_config(

    page_title="Night Owl",

    page_icon="🦉",

    layout="centered",

    initial_sidebar_state="collapsed"

)

# --- THEME & STYLING (GALAXY THEME) ---

st.markdown("""

    <style>

    /* Galaxy Background */

    .stApp {

        background: radial-gradient(circle at center, #2d1b4e 0%, #090912 100%);

        color: #f0e6ff;

    }

    

    /* Glowing Nebula Card Interface */

    .nebula-card {

        background: rgba(255, 255, 255, 0.05);

        border: 2px solid #bb86fc;

        border-radius: 25px;

        padding: 25px;

        margin-bottom: 20px;

        text-align: center;

        box-shadow: 0 0 20px rgba(187, 134, 252, 0.3);

    }

    

    /* Visual Buttons & Controls */

    .stButton>button {

        width: 100%;

        border-radius: 20px;

        height: 3.5em;

        background: linear-gradient(90deg, #bb86fc, #9965f4);

        color: #000000;

        font-weight: bold;

        border: none;

        box-shadow: 0 4px 15px rgba(153, 101, 244, 0.4);

    }

    

    .stSlider > div > div > div > div {

        background-color: #bb86fc;

    }

    

    /* 3D Model Effect for Inputs */

    .stTextArea textarea, .stSelectbox div {

        background-color: rgba(255, 255, 255, 0.07) !important;

        border: 1px solid #bb86fc !important;

        border-radius: 15px !important;

    }

    </style>

    """, unsafe_allow_html=True)

# --- HEADER ---

st.markdown("<h1 style='text-align: center; color: #bb86fc; text-shadow: 0 0 10px #bb86fc;'>🦉 NIGHT OWL # ", unsafe_allow_html=True)

# --- MAIN INTERFACE CARD ---

with st.container():

    st.markdown('<div class="nebula-card">', unsafe_allow_html=True)

    

    # Scripture Header

    st.markdown("""

        <i style='font-size: 1.2em;'>"For I know the plans I have for you..."_

        <b style='color: #bb86fc;'>Jeremiah 29:11**

        <hr style='border: 0.5px solid rgba(187, 134, 252, 0.2); margin: 20px 0;'>

    """, unsafe_allow_html=True)

    

    # Mission Log Subheader

    st.subheader("📝 Mission Log")

    # --- ANIMATED OWL & ENERGY SLIDER ---

    mood = st.select_slider("Energy Level", options=["Exhausted", "Tired", "Steady", "Energetic", "Flirty"])

    if mood == "Flirty":

        # ANIMATED OWL: Open wings

        st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKMGpxx6rD8tE40/giphy.gif")

        st.markdown("<h3 style='color: #bb86fc;'>✨ Open-Winged Owl", unsafe_allow_html=True)

    elif mood == "Exhausted":

        # ANIMATED OWL: Sleepy

        st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzZ4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV5R8Bv1iU/giphy.gif")

        st.markdown("🌙 Sleepy Owl", unsafe_allow_html=True)

    else:

        # Standard Animated Owl

        st.image("[suspicious link removed]")

        st.subheader("🦉 Observant Owl")

    # --- 3D-STYLED INPUT FIELDS ---

    med_notes = st.text_area("Medications & Daily Notes", placeholder="Record NMN, supplements, etc...")

    clearblue = st.selectbox("📊 Clearblue Result", ["Not Taken", "Low", "High", "Peak"])

    # SAVE BUTTON

    if st.button("💾 SAVE TO THE STARS"):

        st.balloons()

        st.success("Mission Log saved to the galaxy!")

    st.markdown('', unsafe_allow_html=True)

# --- EMERGENCY SIGNAL (WhatsApp Button) ---

msg = urllib.parse.quote("Hey Jaco, Nightingale needs a hand. 🦉")

whatsapp_url = f"https://wa.me/27845870789?text={msg}"

st.markdown(f"""

    <a href='{whatsapp_url}' target='_blank' style='text-decoration: none;'>

        <div style='

            width: 100%; 

            height: 60px; 

            background: #25D366; 

            color: white; 

            border-radius: 20px; 

            display: flex; 

            justify-content: center; 

            align-items: center; 

            font-weight: bold;

            font-size: 1.2em;

            box-shadow: 0 4px 15px rgba(0,0,0,0.4);'>

            SIGNAL JACO (WhatsApp)

        

    

""", unsafe_allow_html=True)

```
