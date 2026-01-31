import streamlit as st
import requests
import json

BACKEND_URL = "http://127.0.0.1:8000/chat"
MODEL_NAME = "llama3.2"

st.set_page_config(
    page_title="🦙 Ollama Chatbot",
    page_icon="🦙",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("# 🦙 **Ollama Chatbot**")
with col2:
    st.markdown(f"**`{MODEL_NAME}`**")

st.divider()

# Chat History
for message in st.session_state.messages:
    with st.chat_message(
        message["role"], 
        avatar="👤" if message["role"] == "user" else "🦙"
    ):
        st.markdown(message["content"])

# Sidebar - UNIQUE KEYS!
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1, key="temp_slider_unique")
    
    st.divider()
    if st.button("🗑️ Clear Chat", use_container_width=True, key="clear_chat_unique"):
        st.session_state.messages = []
        st.rerun()

# Chat Input
if prompt := st.chat_input("Ask anything...", key="chat_input_unique"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("🦙 Thinking..."):
            try:
                response = requests.post(
                    BACKEND_URL,
                    json={"message": prompt, "temperature": temperature},
                    headers={"Content-Type": "application/json"},
                    timeout=60
                )
                
                if response.status_code == 200:
                    result = response.json()
                    st.markdown(result["response"])
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": result["response"]
                    })
                else:
                    st.error(f"❌ Backend Error: {response.status_code}")
                    
            except requests.exceptions.ConnectionError:
                st.error("❌ Backend not running!\n**Terminal 2:** `python main.py`")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

st.divider()
st.caption("🆓 Local AI - Ollama + FastAPI + Streamlit")