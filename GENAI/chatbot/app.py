import streamlit as st
from code import generate_response

# =========================
# Page Configuration
# =========================
st.set_page_config(
    page_title="Blog Assistant Chatbot",
    page_icon="📝",
    layout="centered"
)

# =========================
# Title
# =========================
st.title("📝 Blog Assistant Chatbot")
st.write("AI-powered chatbot using Gemini GenAI API")

# =========================
# Session State
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# Display Chat History
# =========================
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =========================
# User Input
# =========================
user_input = st.chat_input("Ask anything about blogging...")

# =========================
# Chat Processing
# =========================
if user_input:

    # Store User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display User Message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate Bot Response
    with st.spinner("Generating response..."):

        response = generate_response(user_input)

    # Store Bot Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # Display Bot Response
    with st.chat_message("assistant"):
        st.markdown(response)