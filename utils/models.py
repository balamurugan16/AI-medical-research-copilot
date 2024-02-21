import os
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings

load_dotenv()

model = os.environ["OPENAI_MODEL"]
azure_deployment = os.environ["OPENAI_DEPLOYMENT"]
azure_endpoint = os.environ["OPENAI_ENDPOINT"]

embedding_deployment = os.environ["OPENAI_EMBEDDING_DEPLOYMENT"]
embedding_model = os.environ["OPENAI_EMBEDDING_MODEL"]

llm = AzureChatOpenAI(
    model=model,
    temperature=0,
    azure_deployment=azure_deployment,
    azure_endpoint=azure_endpoint,
)

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=azure_endpoint,
    deployment=embedding_deployment,
    model=embedding_model,
)
