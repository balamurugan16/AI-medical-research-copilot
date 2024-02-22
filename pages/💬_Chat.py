import streamlit as st
from app.chat import build_chat, chat_history

avatars = {"human": "user", "ai": "assistant"}


def clear_messages():
    chat_history.clear()
    chat_history.add_ai_message(message="How may I assist you today?")


chat = build_chat()

st.set_page_config(page_title="💬 Chat")
st.sidebar.button("Clear Chat History", on_click=clear_messages)

if len(chat_history.messages) == 0:
    clear_messages()


for _, message in enumerate(chat_history.messages):
    avatar = avatars[message.type]
    with st.chat_message(avatar):
        st.write(message.content)


if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.spinner("Ai is thinking"):
        response = chat(
            inputs={"question": prompt, "chat_history": chat_history.messages}
        )
        st.chat_message("assistant").write(response["answer"])
