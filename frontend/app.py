import streamlit as st
import requests

st.set_page_config(page_title="ChatPDF AI", layout="wide")

# 🎨 ---- COOL BACKGROUND CSS ----
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}
/* Chat bubbles */
[data-testid="stChatMessage"] {
    background: rgba(255, 255, 255, 0.08);
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    backdrop-filter: blur(10px);
}
/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(10px);
}
/* Input */
textarea {
    background-color: rgba(255,255,255,0.1) !important;
    color: white !important;
}
/* Buttons */
button {
    border-radius: 10px !important;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white !important;
}
/* Title glow */
h1 {
    text-align: center;
    text-shadow: 0px 0px 15px rgba(0, 200, 255, 0.8);
}
</style>
""", unsafe_allow_html=True)

# 📂 ---- SIDEBAR ----
with st.sidebar:
    st.title("📄 ChatPDF AI")
    st.markdown("Upload a PDF and chat with it 🤖")
    file = st.file_uploader("Upload PDF", type=["pdf"])
    if file is not None:
        with st.spinner("Processing PDF..."):
            try:
                res = requests.post(
                    "http://localhost:8000/upload",
                    files={"file": file}
                )
                if res.status_code == 200:
                    st.success("✅ PDF processed!")
                else:
                    st.error("❌ Upload failed")
                    st.write(res.text)
            except Exception as e:
                st.error(f"Error: {e}")
    st.markdown("---")
    st.caption("Built with ❤️ using RAG + Ollama")

# 💬 ---- MAIN CHAT ----
st.title("💬 Chat with your PDF")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask something from your PDF...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤖"):
            try:
                res = requests.get(
                    "http://localhost:8000/ask",
                    params={"q": user_input}
                )
                if res.status_code == 200:
                    answer = res.json().get("answer", "No response")
                else:
                    answer = "❌ Server error"
                    st.write(res.text)
            except Exception as e:
                answer = f"Error: {e}"
        st.markdown(answer)
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })