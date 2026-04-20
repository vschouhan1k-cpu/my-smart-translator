import streamlit as st
import google.generativeai as genai
import urllib.parse

# 1. Page Config
st.set_page_config(page_title="Vijay's AI Translator", layout="centered")

# 2. Security Setup (API Key को सुरक्षित तरीके से पढ़ना)
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception:
    st.error("कृपया Streamlit Secrets में API Key सेट करें।")

# 3. Styling
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; border-radius: 10px !important; border: 2px solid #075E54 !important; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #075E54 !important; color: white !important; height: 50px; font-weight: bold; }
    .translated-box { background-color: #e8f5e9; padding: 20px; border-radius: 10px; font-size: 20px; color: #1b5e20; border-left: 6px solid #2e7d32; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 विजय का AI ट्रांसलेटर")
st.write("यह सिर्फ शब्दों को नहीं, आपकी भावनाओं (Sense) को समझता है।")

# 4. Input Area
mode = st.radio("Mode चुनें:", ["Hindi to English", "English to Hindi"], horizontal=True)
user_input = st.text_area("यहाँ लिखें (Hinglish भी चलेगा):", height=120, placeholder="उदा: आज तो बात ही नहीं कर रही हो")

# 5. AI Translation Logic
if st.button("AI Translate"):
    if user_input:
        with st.spinner('AI गहराई से सोच रहा है...'):
            try:
                # AI को विशेष निर्देश देना ताकि 'Sense' सही आए
                prompt = f"Act as a professional translator. Translate this text from {mode}: '{user_input}'. If it's Hinglish, treat it as Hindi. Focus on the actual human meaning (context) rather than literal word-to-word translation. Output ONLY the translated text."
                
                response = model.generate_content(prompt)
                translated = response.text.strip()

                # Result Display
                st.markdown(f'<div class="translated-box">{translated}</div>', unsafe_allow_html=True)
                
                # WhatsApp & Copy
                encoded_text = urllib.parse.quote(translated)
                st.markdown(f'''<a href="https://wa.me/?text={encoded_text}" target="_blank">
                    <button style="width:100%; cursor:pointer; background-color:#25D366; color:white; border:none; padding:12px; border-radius:20px; font-weight:bold; margin-bottom:10px;">
                    WhatsApp पर भेजें</button></a>''', unsafe_allow_html=True)
                
                st.info("📋 Copy Text:")
                st.code(translated, language=None)
                
            except Exception as e:
                st.error("अभी AI काम नहीं कर पा रहा। कृपया अपनी API Key चेक करें।")
    else:
        st.warning("भाई, पहले कुछ लिखो तो सही!")
