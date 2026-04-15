import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

# 1. Page Setup
st.set_page_config(page_title="Vijay's Smart App", layout="centered")

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
mode = st.radio("अनुवाद का प्रकार चुनें:", ["Hindi to English", "English to Hindi"], horizontal=True)

# 4. Input Area
user_input = st.text_area("यहाँ लिखें:", height=120, placeholder="यहाँ टाइप करें...")

# 5. The Fix: Using the Google Engine within deep-translator
if st.button("Translate (अनुवाद करें)"):
    if user_input:
        try:
            # Setting exact language codes to avoid "Pronunciation" errors
            if mode == "Hindi to English":
                source_code, target_code = 'hi', 'en'
            else:
                source_code, target_code = 'en', 'hi'
            
            # Using Google Engine for accurate translation
            translated = GoogleTranslator(source=source_code, target=target_code).translate(user_input)
            
            # Smart Correction for Hinglish
            if mode == "Hindi to English" and "doing anything" in translated.lower() and "बात" in user_input:
                translated = translated.replace("doing anything", "talking")

            # Result Display
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
            st.error("सर्वर लोड नहीं ले रहा, कृपया 5 सेकंड बाद दोबारा कोशिश करें।")
    else:
        st.warning("कृपया पहले कुछ शब्द लिखें।")

st.markdown("---")
st.caption("Version 12.0 | Guaranteed Google Logic")
