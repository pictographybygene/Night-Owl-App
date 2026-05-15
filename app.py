import streamlit as st

import urllib.parse



# --- PAGE CONFIGURATION ---

st.set_page_config(

    page_title="Night Owl",

    page_icon="🦉",

    layout="centered",

    initial_sidebar_state="collapsed"

)



# --- THEME & STYLING ---

st.markdown("""

    <style>

    .stApp {

        background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), 

                    linear-gradient(135deg, #2d1b4e 0%, #090912 100%);

        color: #f0e6ff;

    }

    .nebula-card {

        background: rgba(255, 255, 255, 0.05);

        border: 1px solid #bb86fc;

        border-radius: 20px;

        padding: 20px;

        margin-bottom: 20px;

        text-align: center;

        box-shadow: 0 4px 15px rgba(187, 134, 252, 0.2);

    }

    .stSlider > div > div > div > div {

        background-color: #bb86fc;

    }

    /* Buttons */

    .stButton>button {

        width: 100%;

        border-radius: 15px;

        height: 3em;

        background-color: #bb86fc;

        color: #000000;

        font-weight: bold;

        border: none;

    }

    .stButton>button:hover {

        background-color: #9965f4;

        color: #ffffff;

    }

    </style>

    """, unsafe_allow_html=True)



# --- HEADER SECTION ---

st.markdown("<h1 style='text-align: center;'>🦉 NIGHT OWL</h1>", unsafe_allow_html=True)



# --- SCRIPTURE / MOCK-UP COMPONENT ---

st.markdown("""

    <div class="nebula-card">

        <i style='font-size: 1.1em;'>"For I know the plans I have for you..."</i><br>

        <b style='color: #bb86fc;'>Jeremiah 29:11</b>

    </div>

    """, unsafe_allow_html=True)



# --- ENERGY LEVEL & OWL ---

mood = st.select_slider("Energy Level", options=["Exhausted", "Tired", "Steady", "Energetic", "Flirty"])



if mood == "Flirty":

    # GIF for Open-Winged Owl

    st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKMGpxx6rD8tE40/giphy.gif")

    st.subheader("✨ Open-Winged Owl")

else:

    # GIF for Sleepy Owl

    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzZ4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV5R8Bv1iU/giphy.gif")

    st.subheader("🌙 Sleepy Owl")



# --- MISSION LOG SECTION ---

st.markdown('<div class="nebula-card">', unsafe_allow_html=True)

st.subheader("📝 Mission Log")



med_notes = st.text_area("Medications & Daily Notes", placeholder="Type NMN, supplements, etc...", help="Record your daily intake and observations here.")

clearblue = st.selectbox("📊 Clearblue Result", ["Not Taken", "Low", "High", "Peak"])



if st.button("💾 SAVE TO THE STARS"):

    # Here you would typically add logic to save to a database or file

    st.balloons()

    st.success("Mission Log saved successfully!")



st.markdown('</div>', unsafe_allow_html=True)



# --- EMERGENCY / SIGNAL SECTION ---

st.markdown("--- ")

msg = urllib.parse.quote("Hey Jaco, Nightingale needs a hand. 🦉")

# WhatsApp link for South Africa number provided in screenshots

whatsapp_url = f"https://wa.me/27845870789?text={msg}"



st.markdown(f"""

    <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">

        <div style="

            width: 100%; 

            height: 55px; 

            background: #25D366; 

            color: white; 

            border-radius: 15px; 

            display: flex; 

            justify-content: center; 

            align-items: center; 

            font-weight: bold;

            font-size: 1.1em;

            cursor: pointer;

            box-shadow: 0 4px 10px rgba(0,0,0,0.3);">

            SIGNAL JACO (WhatsApp)

        </div>

    </a>

    """, unsafe_allow_html=True)



