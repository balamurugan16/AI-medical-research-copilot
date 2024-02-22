from langchain.memory import ConversationBufferMemory
from langchain_core.chat_history import BaseChatMessageHistory

from langchain_community.chat_message_histories import StreamlitChatMessageHistory


def build_memory(chat_history: BaseChatMessageHistory):
    return ConversationBufferMemory(
        chat_memory=chat_history,
        memory_key="messages",
        return_messages=True,
        input_key="question",
    )
