import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

st.set_page_config(page_title="Vijay's Smart Translator", layout="centered")

st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; border-radius: 10px !important; border: 2px solid #075E54 !important; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #075E54 !important; color: white !important; height: 50px; font-weight: bold; }
    .translated-box { background-color: #e8f5e9; padding: 20px; border-radius: 10px; font-size: 20px; color: #1b5e20; border-left: 6px solid #2e7d32; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 विजय का स्मार्ट ट्रांसलेटर")

# Mode Selection
mode = st.radio("अनुवाद का प्रकार चुनें:", ["Hindi to English", "English to Hindi"], horizontal=True)

# Input Area
user_input = st.text_area("यहाँ लिखें:", height=120, placeholder="यहाँ टाइप करें...")

if st.button("Translate (अनुवाद करें)"):
    if user_input:
        # पक्के कोड्स: 'hi' (Hindi) और 'en' (English)
        s_lang = 'hi' if mode == "Hindi to English" else 'en'
        d_lang = 'en' if mode == "Hindi to English" else 'hi'
            
        try:
            translated = GoogleTranslator(source=s_lang, target=d_lang).translate(user_input)
            
            # Smart Correction for colloquial Hindi
            if mode == "Hindi to English" and "doing anything" in translated.lower() and "बात" in user_input:
                translated = translated.replace("doing anything", "talking")

            # Result Display
            st.markdown(f'<div class="translated-box">{translated}</div>', unsafe_allow_html=True)
            
            # WhatsApp Share
            encoded_text = urllib.parse.quote(translated)
            st.markdown(f'''<a href="https://wa.me/?text={encoded_text}" target="_blank">
                <button style="width:100%; cursor:pointer; background-color:#25D366; color:white; border:none; padding:12px; border-radius:20px; font-weight:bold; margin-bottom:15px;">
                WhatsApp पर भेजें</button></a>''', unsafe_allow_html=True)
            
            # Improved Copy Option
            st.info("📋 नीचे से टेक्स्ट कॉपी करें:")
            st.code(translated, language=None)
                
        except Exception as e:
            st.error("कनेक्शन एरर। कृपया दोबारा कोशिश करें।")
    else:
        st.warning("कृपया कुछ टाइप करें।")

st.caption("Version 8.0 | Fixed Language Logic")
