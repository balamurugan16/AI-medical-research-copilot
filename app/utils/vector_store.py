from app.utils.embeddings import embeddings
from langchain_community.vectorstores.chroma import Chroma
import os

persist_directory = os.environ["CHROMA_PERSIST_DIRECTORY"]

vector_store = Chroma(
    persist_directory=persist_directory, embedding_function=embeddings
)


def build_retriever():
    return vector_store.as_retriever()
