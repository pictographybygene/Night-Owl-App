import streamlit as st
import urllib.parse

st.set_page_config(page_title="Night Owl", page_icon="🦉")

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
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🦉 NIGHT OWL</h1>", unsafe_allow_html=True)

st.markdown('<div class="nebula-card"><i>"For I know the plans I have for you..."</i><br><b>Jeremiah 29:11</b></div>', unsafe_allow_html=True)
mood = st.select_slider("Energy Level", ["Exhausted", "Tired", "Steady", "Energetic", "Flirty"])

if mood == "Flirty":
    st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKMGpxx6rD8tE40/giphy.gif")
    st.subheader("✨ Open-Winged Owl")
else:
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzZ4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV5R8Bv1iU/giphy.gif")
    st.subheader("🌙 Sleepy Owl")

st.markdown('<div class="nebula-card">', unsafe_allow_html=True)
st.subheader("📝 Mission Log")
med_notes = st.text_area("Medications & Daily Notes", placeholder="Type NMN, supplements, etc...")
clearblue = st.selectbox("📊 Clearblue Result", ["Not Taken", "Low", "High", "Peak"])

if st.button("💾 SAVE TO THE STARS"):
    st.balloons()
st.markdown('</div>', unsafe_allow_html=True)

msg = urllib.parse.quote("Hey Jaco, Nightingale needs a hand. 🦉")
st.markdown(f'<a href="https://wa.me/27845870789?text={msg}" target="_blank"><button style="width:100%; height:55px; background:#25D366; color:white; border-radius:15px; border:none; font-weight:bold;">SIGNAL JACO (WhatsApp)</button></a>', unsafe_allow_html=True)
