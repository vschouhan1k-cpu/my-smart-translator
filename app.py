import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse
import time

# 1. Page Configuration
st.set_page_config(page_title="Vijay's Smart Translator", layout="centered")

# 2. UI Styling
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; border-radius: 10px !important; border: 2px solid #075E54 !important; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #075E54; color: white; height: 50px; font-weight: bold; font-size: 18px; }
    .translated-box { background-color: #e8f5e9; padding: 20px; border-radius: 10px; font-size: 20px; color: #1b5e20; border-left: 6px solid #2e7d32; margin-bottom: 10px; }
    /* Simple Copy styling */
    .copy-instruction { font-size: 14px; color: #666; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 विजय का स्मार्ट ट्रांसलेटर")

# 3. Mode Selection
option = st.radio("Mode चुनें:", ["Hindi to English", "English to Hindi"], horizontal=True)

# 4. Input Area
user_input = st.text_area("यहाँ लिखें:", placeholder="उदा: आज तो बात ही नहीं कर रही हो", height=120)

# 5. Stable Logic
if st.button("Translate (अनुवाद करें)"):
    if user_input:
        src, dest = ('hi', 'en') if option == "Hindi to English" else ('en', 'hi')
        
        translated = ""
        success = False
        
        with st.spinner('अनुवाद हो रहा है...'):
            for i in range(3):
                try:
                    translated = GoogleTranslator(source=src, target=dest).translate(user_input)
                    # Sense Correction logic
                    if "doing anything" in translated.lower() and "बात" in user_input:
                        translated = translated.replace("doing anything", "talking")
                    success = True
                    break
                except:
                    time.sleep(1)
                    continue

        if success:
            st.markdown(f'<div class="translated-box">{translated}</div>', unsafe_allow_html=True)
            
            # Action Buttons
            col1, col2 = st.columns(2)
            with col1:
                encoded_text = urllib.parse.quote(translated)
                st.markdown(f'''<a href="https://wa.me/?text={encoded_text}" target="_blank">
                    <button style="width:100%; cursor:pointer; background-color:#25D366; color:white; border:none; padding:12px; border-radius:20px; font-weight:bold;">
                    WhatsApp</button></a>''', unsafe_allow_html=True)
            
            with col2:
                # Error-free Copy Method: st.code का उपयोग (यह हर वर्जन पर काम करता है और वन-क्लिक कॉपी देता है)
                st.info("नीचे से टेक्स्ट कॉपी करें:")
                st.code(translated, language=None)
        else:
            st.error("सर्वर में समस्या है, कृपया 10 सेकंड बाद कोशिश करें।")
    else:
        st.warning("कुछ लिखें भाई!")

st.markdown("---")
st.caption("Version 6.0 | Error-Free Version")
