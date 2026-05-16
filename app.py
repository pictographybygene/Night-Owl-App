import streamlit as st

import urllib.parse

# 1. SETUP

st.set_page_config(page_title='Night Owl v5', page_icon='🦉')

# 2. INJECTED STYLE ENGINE (Single quotes only to prevent runtime parsing errors)

st.markdown('<style>.stApp { background: #090912; color: #f0e6ff; } .nebula-card { background: rgba(255, 255, 255, 0.05); border: 2px solid #bb86fc; border-radius: 20px; padding: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.5); } .stButton>button { width: 100%; border-radius: 15px; height: 3.5em; background: linear-gradient(135deg, #bb86fc, #9965f4); color: black !important; font-weight: bold; }</style>', unsafe_allow_html=True)

# 3. HEADER & BANNER CARDS

st.markdown('<div class="nebula-card"><h1 style="color: #bb86fc; margin: 0;">🦉 NIGHT OWL v5 # ', unsafe_allow_html=True)

st.markdown('<div class="nebula-card"><p style="font-size: 1.1em; font-style: italic; margin-bottom: 5px;">"For I know the plans I have for you..."**Jeremiah 29:11**', unsafe_allow_html=True)

# 4. SLIDER FOR ENERGY

st.write('### ⚡ Energy Level')

mood = st.select_slider('Status Meter', options=['Exhausted', 'Tired', 'Steady', 'Energetic', 'Flirty'], label_visibility='collapsed')

# 5. OWL IMAGES

if mood == 'Flirty':

    st.image('https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6Z3B6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKMGpxx6rD8tE40/giphy.gif', use_container_width=True)

    st.markdown('<h3 style="text-align: center; color: #bb86fc;">✨ Open-Winged Owl', unsafe_allow_html=True)

elif mood == 'Exhausted':

    st.image('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzZ4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeWV4eXJyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTfuxV5R8Bv1iU/giphy.gif', use_container_width=True)

    st.markdown('<h3 style="text-align: center; color: #a3a3c2;">🌙 Sleepy Owl', unsafe_allow_html=True)

else:

    st.image('[suspicious link removed]', use_container_width=True)

    st.markdown('<h3 style="text-align: center; color: #bb86fc;">🦉 Observant Owl', unsafe_allow_html=True)

# 6. MISSION LOG CONTAINER

st.markdown('<div class="nebula-card">', unsafe_allow_html=True)

st.write('### 📝 Mission Log')

med_notes = st.text_area('Logs', placeholder='NMN, vitamins, notes...', label_visibility='collapsed')

clearblue = st.selectbox('📊 Clearblue Result', ['Not Taken', 'Low', 'High', 'Peak'])

if st.button('💾 SAVE DATA'):

    st.balloons()

    st.success('Telemetry logged!')

st.markdown('', unsafe_allow_html=True)

# 7. WHATSAPP LINK

msg = urllib.parse.quote('Hey Jaco, Nightingale needs a hand. 🦉')

whatsapp_url = 'https://wa.me/27845870789?text=' + msg

st.markdown('<a href="' + whatsapp_url + '" target="_blank" style="text-decoration: none;"><div style="background: linear-gradient(90deg, #25D366, #128C7E); color: white; padding: 18px; border-radius: 15px; text-align: center; font-weight: bold; font-size: 1.2em; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">SIGNAL JACO (WhatsApp)', unsafe_allow_html=True)

```
