import requests
import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()
st.set_page_config(page_title="Elysia AI", layout="wide")
st.markdown(
    """
<style>
/* Main chat container */
.chat-container {
    max-height: 500px;
    overflow-y: auto;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e0e0e0;
    background-color: #f8f9fa;
    margin-bottom: 20px;
}

/* Chat message container */
.chat-box {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

/* User bubble - LEFT side */
.user-bubble {
background: linear-gradient(218deg,rgba(31, 31, 31, 1) 0%, rgba(31, 37, 64, 0.71) 0%);
    color: white;
    padding: 18px 18px;
    border-radius: 18px 18px 18px 4px;
    margin-right: auto;
    margin-bottom: 9px;
    max-width: 40%;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    position: relative;
    word-wrap: break-word;
}

/* AI bubble - RIGHT side */
.ai-bubble {
background: linear-gradient(218deg,rgba(31, 31, 31, 1) 0%, rgba(16, 36, 19, 0.71) 0%);
    color: white;
    padding: 18px 18px;
    border-radius: 18px 18px 4px 18px;
    margin-left: auto;
    margin-bottom: 25px;
    max-width: 40%;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    position: relative;
    word-wrap: break-word;
}

/* Responsive design for mobile */
@media (max-width: 768px) {
    .user-bubble, .ai-bubble {
        max-width: 85%;
    }
    
    .chat-container {
        max-height: 40px;
        padding: 15px;
    }
}

/* Scrollbar styling */
.chat-container::-webkit-scrollbar {
    width: 6px;
}

.chat-container::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 10px;
}

.chat-container::-webkit-scrollbar-thumb {
    background: #c1c1c1;
    border-radius: 10px;
}

.chat-container::-webkit-scrollbar-thumb:hover {
    background: #a8a8a8;
}

/* Message animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.user-bubble, .ai-bubble {
    animation: fadeIn 0.3s ease-in;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<h1 style='text-align:center; color: white;'>Elysia AI</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align:center; font-size:18px; color: #666;'>Your personal therapy assistant 🤍</p>",
    unsafe_allow_html=True,
)
st.divider()
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(
            f"<div class='user-bubble'>{chat['content']}</div>", unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='ai-bubble'>{chat['content']}</div>", unsafe_allow_html=True
        )

st.markdown("</div></div>", unsafe_allow_html=True)

user_input = st.chat_input("Type your message...", key="chat_input")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    json_data = st.session_state.chat_history[-4:]
    res = requests.post(
        os.getenv("BACKEND_URL"),
        json=json_data,
        headers={"Content-Type": "application/json"},
    )

    st.session_state.chat_history.append({"role": "assistant", "content": res.json()})
    st.rerun()
