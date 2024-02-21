from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from utils.models import llm, embeddings
from langchain_community.vectorstores.chroma import Chroma
import time


template = """
I want you to act as an assistant who will analyze several clinical and drug research papers,
and provide a detailed summary about the subject that is being asked for. The context will
provided from various sources like PubMed, Drug bank, Dailymed, and FDA. It will contain
abstract about a disease, its causes, symptoms, preventive measures. Along with that
drug trials will also be available with its efficacy on the disease.

With this context, You have to analyze the following aspects.
1. Symptoms for the disease
2. Key findings from the clinical and drug trials.
3. What are the current drugs available for the disease and their efficacy
4. What is the treatment for the disease?

After analysing you have to give me a summary with 3 subsections
1. A Complete summary about the subject (the disease and the drugs)
2. Main outcomes and measures (from the related research articles)
3. Study design of background
Your summarization should be informative and about 1000 words

If you don't know the answer, just say that you don't know.
You don't need to provide the citations for the articles.
Don't give any answer outside the information that is not provided in the context.
Give the answer in Markdown format.

Subject: {subject}
Context: {context}
"""

db = Chroma(persist_directory="embeddings", embedding_function=embeddings)


def summarize(prompt: str, question: str) -> str:
    related_docs = db.similarity_search(question, k=50)
    print(prompt)
    prompt = PromptTemplate(template=prompt, input_variables=["subject", "context"])
    chain = load_summarize_chain(
        llm,
        chain_type="stuff",
        verbose=True,
        prompt=prompt,
        document_variable_name="context",
    )
    output = chain.invoke({"input_documents": related_docs, "subject": question})
    summary = output["output_text"]
    current_epoch_time = int(time.time())
    with open(f"output_cache/summary_{current_epoch_time}.md", "w") as file:
        file.write(summary)
    return summary
