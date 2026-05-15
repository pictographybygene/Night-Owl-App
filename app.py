import streamlit as st
import urllib.parse

# --- GALAXY SETTINGS ---
st.set_page_config(page_title="Night Owl", page_icon="🦉")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                    linear-gradient(135deg, #2d1b4e 0%, #1a0b2e 100%);
        color: #f0e6ff;
    }
    .nebula-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid #bb86fc;
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🦉 NIGHT OWL")

# --- SCRIPTURE ---
st.markdown('<div class="nebula-card"><i>"For I know the plans I have for you..."</i><br><b>Jeremiah 29:11</b></div>', unsafe_allow_html=True)

# --- MOOD & OWL ---
mood = st.select_slider("Energy Level", ["Exhausted", "Tired", "Steady", "Energetic", "Flirty"])

if mood == "Flirty":
    st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKMGpxx6rD8tE40/giphy.gif")
    st.subheader("✨ Open-Winged Owl")
else:
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzZ4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV5R8Bv1iU/giphy.gif")
    st.subheader("🌙 Sleepy Owl")

# --- LOGBOOK ---
st.markdown('<div class="nebula-card">', unsafe_allow_html=True)
st.subheader("📝 Mission Log")
meds = st.text_area("Medications & Notes", placeholder="Type NMN, supplements, etc...")
cb = st.selectbox("📊 Clearblue Result", ["Not Taken", "Low", "High", "Peak"])
if st.button("SAVE TO THE STARS"):
    st.balloons()
    st.success("Mission Log Captured!")
st.markdown('</div>', unsafe_allow_html=True)

# --- SIGNAL ---
msg = urllib.parse.quote("Hey Jacob, Nightingale needs a hand. 🦉")
st.markdown(f'<a href="https://wa.me/27845870789?text={msg}" target="_blank"><button style="width:100%; height:55px; background:#25D366; color:white; border-radius:15px; border:none; font-weight:bold; font-size:18px;">SIGNAL JACOB (WhatsApp)</button></a>', unsafe_allow_html=True)
