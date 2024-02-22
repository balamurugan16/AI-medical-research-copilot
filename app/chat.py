from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from app.utils.llm import build_llm
from app.utils.vector_store import build_retriever
from app.utils.memory import build_memory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain.prompts import PromptTemplate

chat_history = StreamlitChatMessageHistory(key="messages")


system_prompt_template = """
Your are an AI assistant who has access to multiple research articles and clinical trials
on certain diseases, drug trials with efficacy from reliable resources.

Your job is to retrieve the relevant information for the user's prompt based on the context

{context}

If the user is greeting you, greet him back politely.
If you don't know the answer, just say that you don't know.
If you know the answer, give the accurate answer in Markdown format!
"""

system_prompt = PromptTemplate(
    template=system_prompt_template, input_variables=["context"]
)


def build_chat():
    llm = build_llm()
    retriever = build_retriever()
    memory = build_memory(chat_history=chat_history)
    return ConversationalRetrievalChain.from_llm(
        memory=memory, retriever=retriever, llm=llm, verbose=True
    )
