import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

# 1. Page Configuration
st.set_page_config(page_title="Smart Hindi Translator", layout="centered")

# 2. UI Styling
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; border-radius: 10px !important; background-color: #ffffff; border: 2px solid #075E54 !important; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #075E54; color: white; height: 50px; font-weight: bold; font-size: 18px; }
    .translated-box { background-color: #e8f5e9; padding: 20px; border-radius: 10px; font-size: 20px; color: #1b5e20; border-left: 6px solid #2e7d32; margin-bottom: 10px; font-family: sans-serif; }
    div[data-testid="stCopyButton"] button { width: 100% !important; background-color: #607d8b !important; color: white !important; border-radius: 20px !important; height: 45px !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 विजय का स्मार्ट ट्रांसलेटर")
st.write("अशुद्ध हिंदी का शुद्ध English अनुवाद")

# 3. Mode Selection
option = st.radio("Mode चुनें:", ["Hindi to English", "English to Hindi"], horizontal=True)

# 4. Input Area
user_input = st.text_area("यहाँ लिखें (Write here):", placeholder="उदा: आज तो बात ही नहीं कर रही हो", height=120)

if user_input:
    st.caption(f"Characters: {len(user_input)}")

# 5. Stable Logic (Google Engine - Improved)
if st.button("Translate (अभी अनुवाद करें)"):
    if user_input:
        src, dest = ('hi', 'en') if option == "Hindi to English" else ('en', 'hi')
        try:
            # हम Google का इस्तेमाल करेंगे पर 'Sense' के साथ
            translated = GoogleTranslator(source=src, target=dest).translate(user_input)
            
            # अगर अनुवाद में "doing anything" आ रहा है, तो उसे 'talking' से सुधारने की कोशिश (Smart logic)
            if "doing anything" in translated.lower() and "बात" in user_input:
                 translated = translated.replace("doing anything", "talking")

            # Display Result
            st.markdown(f'<div class="translated-box">{translated}</div>', unsafe_allow_html=True)
            
            # Action Buttons
            col1, col2 = st.columns(2)
            with col1:
                encoded_text = urllib.parse.quote(translated)
                st.markdown(f'''<a href="https://wa.me/?text={encoded_text}" target="_blank">
                    <button style="width:100%; cursor:pointer; background-color:#25D366; color:white; border:none; padding:12px; border-radius:20px; font-weight:bold;">
                    WhatsApp</button></a>''', unsafe_allow_html=True)
            with col2:
                st.copy_button(label="📋 Copy Text", data=translated)
                
        except Exception as e:
            st.error("सर्वर थोड़ा बिजी है, कृपया 2 सेकंड बाद फिर दबाएँ।")
    else:
        st.warning("भाई, पहले कुछ लिखो तो सही!")

st.markdown("---")
st.caption("Version 4.0 | Fast & Reliable")
