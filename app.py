import streamlit as st
import urllib.parse

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Night Owl",
    page_icon="🦉",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. THEME & NEBULA STYLING
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
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 3.5em;
        background: linear-gradient(135deg, #bb86fc, #9965f4);
        color: black !important;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background: #9965f4;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER SECTION
st.markdown("<h1 style='text-align: center; color: #bb86fc;'>🦉 NIGHT OWL</h1>", unsafe_allow_html=True)

# 4. SCRIPTURE CARD
st.markdown("""
    <div class="nebula-card">
        <i style='font-size: 1.1em;'>\"For I know the plans I have for you...\"</i><br>
        <b style='color: #bb86fc;'>Jeremiah 29:11</b>
    </div>
    """, unsafe_allow_html=True)

# 5. ENERGY LEVEL SLIDER & OWL IMAGES
st.write("### ⚡ Energy Level")
mood = st.select_slider("Status Meter", options=["Exhausted", "Tired", "Steady", "Energetic", "Flirty"], label_visibility="collapsed")

if mood == "Flirty":
    st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKMGpxx6rD8tE40/giphy.gif", use_container_width=True)
    st.markdown("<h3 style='text-align: center; color: #bb86fc;'>✨ Open-Winged Owl</h3>", unsafe_allow_html=True)
elif mood == "Exhausted":
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzZ4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV5R8Bv1iU/giphy.gif", use_container_width=True)
    st.markdown("<h3 style='text-align: center; color: #a3a3c2;'>🌙 Sleepy Owl</h3>", unsafe_allow_html=True)
else:
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnc1bm96Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6Z3R6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/m8pEQT5C26D5u/giphy.gif", use_container_width=True)
    st.markdown("<h3 style='text-align: center; color: #bb86fc;'>🦉 Observant Owl</h3>", unsafe_allow_html=True)

# 6. MISSION LOG
st.markdown('<div class="nebula-card">', unsafe_allow_html=True)
st.write("### 📝 Mission Log")
med_notes = st.text_area("Logs", placeholder="Track NMN, supplements, daily notes...", label_visibility="collapsed")
clearblue = st.selectbox("📊 Clearblue Result", ["Not Taken", "Low", "High", "Peak"])

if st.button("💾 SAVE DATA"):
    st.balloons()
    st.success("Telemetry logged successfully!")
st.markdown('</div>', unsafe_allow_html=True)

# 7. COMMUNICATIONS LINK (SIGNAL JACO)
msg = urllib.parse.quote("Hey Jaco, Nightingale needs a hand. 🦉")
whatsapp_url = "https://wa.me/27845870789?text=" + msg

st.markdown(f"""
    <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
        <div style="
            background: linear-gradient(90deg, #25D366, #128C7E); 
            color: white; 
            padding: 18px; 
            border-radius: 15px; 
            text-align: center; 
            font-weight: bold; 
            font-size: 1.2em; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
            SIGNAL JACO (WhatsApp)
        </div>
    </a>
    """, unsafe_allow_html=True)
    
