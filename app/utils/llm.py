import os
from langchain_openai import AzureChatOpenAI


def build_llm():
    model = os.environ["OPENAI_MODEL"]
    azure_deployment = os.environ["OPENAI_DEPLOYMENT"]
    azure_endpoint = os.environ["OPENAI_ENDPOINT"]

    return AzureChatOpenAI(
        model=model,
        temperature=0,
        azure_deployment=azure_deployment,
        azure_endpoint=azure_endpoint,
    )
