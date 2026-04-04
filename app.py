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
    div[data-testid="stCopyButton"] button { width: 100% !important; background-color: #607d8b !important; color: white !important; border-radius: 20px !important; height: 45px !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 विजय का स्मार्ट ट्रांसलेटर")

# 3. Mode Selection
option = st.radio("Mode चुनें:", ["Hindi to English", "English to Hindi"], horizontal=True)

# 4. Input Area
user_input = st.text_area("यहाँ लिखें:", placeholder="उदा: आज तो बात ही नहीं कर रही हो", height=120)

if user_input:
    st.caption(f"Characters: {len(user_input)}")

# 5. Stable Logic with Auto-Retry
if st.button("Translate (अनुवाद करें)"):
    if user_input:
        src, dest = ('hi', 'en') if option == "Hindi to English" else ('en', 'hi')
        
        # Retry Logic: 3 बार कोशिश करेगा
        translated = ""
        success = False
        
        with st.spinner('अनुवाद हो रहा है... कृपया रुकें'):
            for i in range(3):
                try:
                    translated = GoogleTranslator(source=src, target=dest).translate(user_input)
                    
                    # 'Sense' Correction (हमारा खास फीचर)
                    if "doing anything" in translated.lower() and "बात" in user_input:
                        translated = translated.replace("doing anything", "talking")
                    
                    success = True
                    break # अगर सफल हुआ तो लूप से बाहर आ जाओ
                except Exception:
                    time.sleep(1) # 1 सेकंड इंतज़ार करके फिर कोशिश करेगा
                    continue

        if success:
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
        else:
            st.error("माफी चाहता हूँ, Google का सर्वर अभी जवाब नहीं दे रहा। कृपया 10 सेकंड बाद फिर कोशिश करें।")
    else:
        st.warning("भाई, पहले कुछ लिखो तो सही!")

st.markdown("---")
st.caption("Version 5.0 | High Stability")
