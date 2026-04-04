import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

# 1. Basic Page Setup
st.set_page_config(page_title="Vijay Translator")

# 2. UI Styling
st.markdown("""
    <style>
    .stTextArea textarea { border: 2px solid #075E54 !important; border-radius: 10px; }
    .result-box { background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-left: 5px solid #2e7d32; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 विजय का ट्रांसलेटर")

# 3. Mode & Input
option = st.radio("अनुवाद चुनें:", ["Hindi to English", "English to Hindi"], horizontal=True)
user_input = st.text_area("यहाँ लिखें:", height=100)

# 4. Translation Logic
if st.button("Translate"):
    if user_input:
        src, dest = ('hi', 'en') if "Hindi" in option else ('en', 'hi')
        try:
            # Simple Translation
            translated = GoogleTranslator(source=src, target=dest).translate(user_input)
            
            # Sense Correction
            if "doing anything" in translated.lower() and "बात" in user_input:
                translated = translated.replace("doing anything", "talking")

            # Display Output
            st.markdown(f'<div class="result-box">{translated}</div>', unsafe_allow_html=True)
            
            # Share Option
            encoded_text = urllib.parse.quote(translated)
            st.markdown(f'''<a href="https://wa.me/?text={encoded_text}" target="_blank">
                <button style="width:100%; background-color:#25D366; color:white; border:none; padding:12px; border-radius:20px; font-weight:bold; cursor:pointer; margin-top:10px;">
                WhatsApp पर भेजें</button></a>''', unsafe_allow_html=True)
                
        except Exception:
            st.error("इंटरनेट धीमा है, कृपया फिर से बटन दबाएं।")
    else:
        st.warning("कुछ टाइप करें।")
