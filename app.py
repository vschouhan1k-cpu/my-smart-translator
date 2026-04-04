import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

# 1. Page Setup
st.set_page_config(page_title="Vijay Translator", layout="centered")

# 2. UI Styling (Only Basic CSS)
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; border-radius: 10px !important; border: 2px solid #075E54 !important; }
    .translated-box { background-color: #e8f5e9; padding: 20px; border-radius: 10px; font-size: 20px; color: #1b5e20; border-left: 6px solid #2e7d32; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 ट्रांसलेटर")

# 3. Input
option = st.radio("Select Mode:", ["Hindi to English", "English to Hindi"], horizontal=True)
user_input = st.text_area("यहाँ लिखें:", height=100)

# 4. Simple Logic (No Retry Loops, No Complex Functions)
if st.button("Translate (अनुवाद करें)"):
    if user_input:
        src, dest = ('hi', 'en') if "Hindi" in option else ('en', 'hi')
        try:
            # Basic Translation
            translated = GoogleTranslator(source=src, target=dest).translate(user_input)
            
            # Smart Sense Fix
            if "doing anything" in translated.lower() and "बात" in user_input:
                translated = translated.replace("doing anything", "talking")

            # 5. Result Display
            st.markdown(f'<div class="translated-box">{translated}</div>', unsafe_allow_html=True)
            
            # 6. Action Buttons (Direct Markdown)
            encoded_text = urllib.parse.quote(translated)
            
            # WhatsApp Button
            st.markdown(f'''<a href="https://wa.me/?text={encoded_text}" target="_blank">
                <button style="width:100%; cursor:pointer; background-color:#25D366; color:white; border:none; padding:12px; border-radius:20px; font-weight:bold; margin-bottom:10px;">
                WhatsApp पर भेजें</button></a>''', unsafe_allow_html=True)
            
            # Simple Copy Method
            st.info("टेक्स्ट कॉपी करने के लिए इसे दबाकर रखें (Long press to copy):")
            st.write(translated)
                
        except Exception as e:
            st.error("Connection Error. Please try again.")
    else:
        st.warning("Please enter text.")

st.caption("Stable Version 7.0")
