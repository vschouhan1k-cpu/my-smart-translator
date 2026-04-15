import streamlit as st
from googletrans import Translator
import urllib.parse

# 1. Page Setup
st.set_page_config(page_title="Vijay's Translator", layout="centered")

# 2. UI Styling
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; border-radius: 10px !important; border: 2px solid #075E54 !important; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #075E54 !important; color: white !important; height: 50px; font-weight: bold; }
    .translated-box { background-color: #e8f5e9; padding: 20px; border-radius: 10px; font-size: 20px; color: #1b5e20; border-left: 6px solid #2e7d32; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 विजय का स्मार्ट ट्रांसलेटर")

# 3. Mode Selection
mode = st.radio("Select Direction:", ["Hindi to English", "English to Hindi"], horizontal=True)

# 4. Input Area
user_input = st.text_area("यहाँ लिखें:", height=120)

# 5. New Logic using googletrans (Stable Version)
if st.button("Translate (अनुवाद करें)"):
    if user_input:
        translator = Translator()
        try:
            if mode == "Hindi to English":
                result = translator.translate(user_input, src='hi', dest='en')
                translated = result.text
                
                # 'Sense' Correction Logic
                if "doing anything" in translated.lower() and "बात" in user_input:
                    translated = translated.replace("doing anything", "talking")
            else:
                # English to Hindi Logic
                result = translator.translate(user_input, src='en', dest='hi')
                translated = result.text

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
                st.info("📋 Copy from here:")
                st.code(translated, language=None)
                
        except Exception as e:
            st.error("सर्वर लोड नहीं ले रहा, कृपया 2 सेकंड बाद दोबारा बटन दबाएं।")
    else:
        st.warning("कृपया कुछ टाइप करें।")

st.caption("Version 9.0 | Google-Engine Final")
