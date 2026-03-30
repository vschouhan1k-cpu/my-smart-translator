import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse
import streamlit.components.v1 as components

# Page Setup
st.set_page_config(page_title="Hindi Translator", layout="centered")

# Custom CSS for UI
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; border-radius: 10px !important; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #075E54; color: white; height: 45px; }
    .translated-text { background-color: #e8f5e9; padding: 20px; border-radius: 10px; font-size: 20px; color: #1b5e20; border: 1px solid #c8e6c9; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 Smart Hindi-English App")

# Language Selection
option = st.radio("Translate from:", ["Hindi to English", "English to Hindi"], horizontal=True)

# Input Area
user_input = st.text_area("यहाँ लिखें:", placeholder="उदा: मैं घर पहुँच गया हूँ", height=100)

# Character Count
if user_input:
    st.caption(f"Characters: {len(user_input)}")

# Translate Button (ताकि सिर्फ Enter/Click पर काम करे)
if st.button("Translate (अनुवाद करें)"):
    if user_input:
        src, dest = ('hi', 'en') if option == "Hindi to English" else ('en', 'hi')
        try:
            translated = GoogleTranslator(source=src, target=dest).translate(user_input)
            
            # Displaying only the translated text (बिना "Result:" शब्द के)
            st.markdown(f'<div class="translated-text">{translated}</div>', unsafe_allow_html=True)
            
            # Action Buttons
            col1, col2 = st.columns(2)
            
            with col1:
                # WhatsApp Share
                encoded_text = urllib.parse.quote(translated)
                st.markdown(f'''<a href="https://wa.me/?text={encoded_text}" target="_blank">
                    <button style="width:100%; cursor:pointer; background-color:#25D366; color:white; border:none; padding:10px; border-radius:20px;">
                    WhatsApp</button></a>''', unsafe_allow_html=True)
            
            with col2:
                # JavaScript based Copy to Clipboard Button
                copy_js = f"""
                <script>
                function copyToClipboard() {{
                    const text = "{translated}";
                    navigator.clipboard.writeText(text).then(() => {{
                        alert("Copied to Clipboard!");
                    }});
                }}
                </script>
                <button onclick="copyToClipboard()" style="width:100%; cursor:pointer; background-color:#607d8b; color:white; border:none; padding:10px; border-radius:20px;">
                Copy to Clipboard</button>
                """
                components.html(copy_js, height=50)
                
        except Exception as e:
            st.error("Connection error. Please try again.")
    else:
        st.warning("कृपया पहले कुछ लिखें।")

st.markdown("---")
st.caption("Developed by Vijay | Version 2.0")