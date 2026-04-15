import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

# 1. Page Setup
st.set_page_config(page_title="Vijay's App", layout="centered")

# 2. Styling
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; border-radius: 10px !important; border: 2px solid #075E54 !important; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #075E54 !important; color: white !important; height: 50px; font-weight: bold; }
    .translated-box { background-color: #e8f5e9; padding: 20px; border-radius: 10px; font-size: 20px; color: #1b5e20; border-left: 6px solid #2e7d32; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 विजय का स्मार्ट ट्रांसलेटर")

# 3. Selection
mode = st.radio("अनुवाद का प्रकार:", ["Hindi to English", "English to Hindi"], horizontal=True)
user_input = st.text_area("यहाँ लिखें:", height=120)

# 4. Corrected Logic using deep-translator
if st.button("Translate"):
    if user_input:
        try:
            # यहाँ हमने कोड्स को 'hi' और 'en' पर फिक्स किया है
            if mode == "Hindi to English":
                translated = GoogleTranslator(source='hi', target='en').translate(user_input)
                # Sense Correction
                if "doing anything" in translated.lower() and "बात" in user_input:
                    translated = translated.replace("doing anything", "talking")
            else:
                # English to Hindi (Fixed to prevent "Pronunciation" error)
                translated = GoogleTranslator(source='en', target='hi').translate(user_input)

            # Display
            st.markdown(f'<div class="translated-box">{translated}</div>', unsafe_allow_html=True)
            
            # Action Buttons
            col1, col2 = st.columns(2)
            with col1:
                encoded_text = urllib.parse.quote(translated)
                st.markdown(f'''<a href="https://wa.me/?text={encoded_text}" target="_blank">
                    <button style="width:100%; cursor:pointer; background-color:#25D366; color:white; border:none; padding:12px; border-radius:20px; font-weight:bold;">
                    WhatsApp</button></a>''', unsafe_allow_html=True)
            with col2:
                st.info("📋 Copy Text:")
                st.code(translated, language=None)
                
        except Exception as e:
            st.error("कनेक्शन की समस्या है। कृपया फिर से बटन दबाएँ।")
    else:
        st.warning("कृपया कुछ लिखें।")

st.caption("Version 10.0 | Python 3.14 Compatible")
