import requests
import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()
st.set_page_config(page_title="Elysia AI", layout="wide")
st.markdown(
    """
<style>
/* Page background - Luxury Black */
body, .stApp, .main, .block-container {
    background-color: #010101;  /* deep black */
    color: #FFFFFF;              /* default text white */
}

/* Sidebar background (optional) */
.css-1d391kg {
    background-color: #010101;
}

/* Scrollbar styling for dark luxury */
::-webkit-scrollbar {
    width: 6px;
}

::-webkit-scrollbar-track {
    background: #111111;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: #555555;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #888888;
}
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
    background: linear-gradient(135deg, #18453B, #1F6A55); /* dark green gradient */
    color: white;
    padding: 18px 18px;
    border-radius: 18px 18px 18px 4px;
    margin-right: auto;
    margin-bottom: 9px;
    max-width: 40%;
    box-shadow: 0 4px 15px rgba(255, 255, 255, 0.1), 0 8px 25px rgba(255, 255, 255, 0.09);
    position: relative;
    word-wrap: break-word;
}

/* AI bubble - RIGHT side */
.ai-bubble {
    background: linear-gradient(135deg, #1B2C3B, #345A70); /* dark blue gradient */
    color: white;
    padding: 18px 18px;
    border-radius: 18px 18px 4px 18px;
    margin-left: auto;
    margin-bottom: 25px;
    max-width: 40%;
    box-shadow: 0 4px 15px rgba(255, 255, 255, 0.12), 0 8px 25px rgba(255, 255, 255, 0.06);
    position: relative;
    word-wrap: break-word;
}

/* Optional: glow effect for realism */
.user-bubble:hover, .ai-bubble:hover {
    box-shadow: 0 6px 20px rgba(255, 255, 255, 0.2), 0 12px 40px rgba(255, 255, 255, 0.08);
    transition: all 0.3s ease;
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
/* Typing animation */
.typing {
    display: inline-block;
    width: 20px;
    text-align: left;
}

.typing::after {
    content: "...";
    animation: typingDots 1.2s infinite steps(3);
}

@keyframes typingDots {
    0% { content: ""; }
    33% { content: "."; }
    66% { content: ".."; }
    100% { content: "..."; }
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
    "<p style='text-align:center; font-size:18px; color: #666;'>Your personal therapy assistant 🤍 <br/> developed by <a  href='https://ismailkhandev.vercel.app'  style='color:#666;'   >ismail khan</a> </p>",
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
    
    # --- SHOW ANIMATED TYPING INDICATOR ---
    typing_placeholder = st.empty()
    typing_placeholder.markdown(
        "<div class='ai-bubble'><span class='typing'></span></div>",
        unsafe_allow_html=True
    )

    json_data = st.session_state.chat_history[-8:]
    res = requests.post(
        os.getenv("BACKEND_URL"),
        json=json_data,
        headers={"Content-Type": "application/json"},
    )

    # --- REMOVE TYPING INDICATOR ---
    typing_placeholder.empty()
    if res.status_code != 200 : 
        st.error("Error occured please try again later.")
    else:
        st.session_state.chat_history.append({"role": "assistant", "content": res.json()})
    st.rerun()
