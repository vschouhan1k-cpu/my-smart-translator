import streamlit as st
from deep_translator import MyMemoryTranslator
import urllib.parse

# 1. Page Configuration
st.set_page_config(page_title="Smart Hindi Translator", layout="centered")

# 2. UI Styling
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; border-radius: 10px !important; background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #075E54; color: white; height: 45px; font-weight: bold; }
    .translated-box { background-color: #e8f5e9; padding: 20px; border-radius: 10px; font-size: 20px; color: #1b5e20; border: 1px solid #c8e6c9; margin-bottom: 10px; }
    div[data-testid="stCopyButton"] button { width: 100% !important; background-color: #607d8b !important; color: white !important; border-radius: 20px !important; height: 45px !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 Smart Hindi-English App")

# 3. Mode Selection
option = st.radio("अनुवाद का प्रकार चुनें:", ["Hindi to English", "English to Hindi"], horizontal=True)

# 4. Input Area
user_input = st.text_area("यहाँ लिखें:", placeholder="उदा: आज तो बात ही नहीं कर रही हो", height=120)

if user_input:
    st.caption(f"Characters: {len(user_input)}")

# 5. Logic using MyMemory (Better for Conversational Hindi)
if st.button("Translate (अनुवाद करें)"):
    if user_input:
        # MyMemory uses language codes like 'hi-IN' and 'en-GB'
        src, dest = ('hi-IN', 'en-GB') if option == "Hindi to English" else ('en-GB', 'hi-IN')
        try:
            # Using MyMemoryTranslator for better sense
            translated = MyMemoryTranslator(source=src, target=dest).translate(user_input)
            
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
            st.error("Connection error. Please try again.")
    else:
        st.warning("कृपया पहले कुछ लिखें।")

st.markdown("---")
st.caption("Developed by Vijay | MyMemory Engine v3.0")
