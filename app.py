import streamlit as st
import google.generativeai as genai
import urllib.parse

st.set_page_config(page_title="Vijay's AI Translator", layout="centered")

# --- सुरक्षा और चाबी की जाँच ---
if "GEMINI_API_KEY" not in st.secrets:
    st.error("❌ एरर: Secrets में 'GEMINI_API_KEY' नहीं मिली!")
    st.stop()

try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    # सबसे लेटेस्ट 'Flash' मॉडल जो 404 नहीं देगा
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"❌ API लोड करने में दिक्कत: {e}")

# --- UI और Styling ---
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; border-radius: 10px !important; border: 2px solid #075E54 !important; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #075E54 !important; color: white !important; height: 50px; font-weight: bold; }
    .translated-box { background-color: #e8f5e9; padding: 20px; border-radius: 10px; font-size: 20px; color: #1b5e20; border-left: 6px solid #2e7d32; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 विजय का AI ट्रांसलेटर")

mode = st.radio("अनुवाद चुनें:", ["Hindi to English", "English to Hindi"], horizontal=True)
user_input = st.text_area("यहाँ लिखें (जैसे: आज तो बात ही नहीं कर रही हो):", height=120)

if st.button("AI Translate"):
    if user_input:
        with st.spinner('AI गहराई से सोच रहा है...'):
            try:
                # AI को स्पष्ट निर्देश
                prompt = f"Professional translation for {mode}: '{user_input}'. Meaning and context matter. Output only translated text."
                response = model.generate_content(prompt)
                translated = response.text.strip()
                
                st.markdown(f'<div class="translated-box">{translated}</div>', unsafe_allow_html=True)
                
                # WhatsApp Button
                encoded_text = urllib.parse.quote(translated)
                st.markdown(f'''<a href="https://wa.me/?text={encoded_text}" target="_blank">
                    <button style="width:100%; cursor:pointer; background-color:#25D366; color:white; border:none; padding:12px; border-radius:20px; font-weight:bold;">
                    WhatsApp पर भेजें</button></a>''', unsafe_allow_html=True)
                
                st.info("📋 Copy Text:")
                st.code(translated, language=None)
                
            except Exception as e:
                st.error(f"AI Error: {e}")
    else:
        st.warning("कृपया कुछ टाइप करें।")
