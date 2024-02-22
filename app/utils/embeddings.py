import os
from langchain_openai import AzureOpenAIEmbeddings

azure_endpoint = os.environ["OPENAI_ENDPOINT"]
deployment = os.environ["OPENAI_EMBEDDING_DEPLOYMENT"]
model = os.environ["OPENAI_EMBEDDING_MODEL"]

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=azure_endpoint,
    deployment=deployment,
    model=model,
)
