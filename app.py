import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

# 1. Page Setup
st.set_page_config(page_title="Vijay's Smart Translator", layout="centered")

# 2. UI Styling (सुंदर और मोबाइल फ्रेंडली)
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; border-radius: 10px !important; border: 2px solid #075E54 !important; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #075E54; color: white; height: 50px; font-weight: bold; }
    .translated-box { background-color: #e8f5e9; padding: 20px; border-radius: 10px; font-size: 20px; color: #1b5e20; border-left: 6px solid #2e7d32; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 विजय का स्मार्ट ट्रांसलेटर")

# 3. Mode Selection (English to Hindi अब काम करेगा)
mode = st.radio("अनुवाद का प्रकार चुनें:", ["Hindi to English", "English to Hindi"], horizontal=True)

# 4. Input Area
user_input = st.text_area("यहाँ लिखें:", height=100)

# 5. Logic
if st.button("Translate (अनुवाद करें)"):
    if user_input:
        # भाषा का चुनाव
        if mode == "Hindi to English":
            src_lang, dest_lang = 'hi', 'en'
        else:
            src_lang, dest_lang = 'en', 'hi'
            
        try:
            # Translation
            translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(user_input)
            
            # Sense Correction (सिर्फ Hindi to English के लिए)
            if mode == "Hindi to English" and "doing anything" in translated.lower() and "बात" in user_input:
                translated = translated.replace("doing anything", "talking")

            # Result Display
            st.markdown(f'<div class="translated-box">{translated}</div>', unsafe_allow_html=True)
            
            # WhatsApp Share
            encoded_text = urllib.parse.quote(translated)
            st.markdown(f'''<a href="https://wa.me/?text={encoded_text}" target="_blank">
                <button style="width:100%; cursor:pointer; background-color:#25D366; color:white; border:none; padding:12px; border-radius:20px; font-weight:bold; margin-bottom:15px;">
                WhatsApp पर भेजें</button></a>''', unsafe_allow_html=True)
            
            # Copy Option (Simple & Safe Method)
            st.write("📋 **इसे यहाँ से कॉपी करें:**")
            st.code(translated, language=None)
            st.caption("ऊपर दिए गए बॉक्स के कोने में मौजूद 'Copy' आइकन पर क्लिक करें।")
                
        except Exception:
            st.error("कनेक्शन की समस्या है। कृपया दोबारा बटन दबाएं।")
    else:
        st.warning("कृपया कुछ टाइप करें।")

st.markdown("---")
st.caption("Stable Final Version | Hindi ↔ English")
