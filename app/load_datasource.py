from app.utils.vector_store import vector_store
from app.utils.loader import HTMLLoader
from app.utils.models import DataSource, Domains, Extraction
from typing import List, Dict

domain_strategy_map = {
    "PubMed": {
        "strategy": Extraction.WRAPPER,
        "kwargs": {"root_tag": {"tag": "div", "id": "abstract"}},
    },
    "FDA": {
        "strategy": Extraction.WRAPPER,
        "kwargs": {"root_tag": {"tag": "article", "id": "main-content"}},
    },
    "DrugBank": {
        "strategy": Extraction.WRAPPER,
        "kwargs": {"root_tag": {"tag": "div", "class": "drug-card"}},
    },
    "DailyMed": {
        "strategy": Extraction.TAG,
        "kwargs": {"unwanted_tags": ["p"], "tags_to_extract": ["header"]},
    },
}


def preprocess_urls(data: DataSource):
    preprocessed_data: Dict[Domains, List[str]] = {}
    for item in data:
        domain = item["domain"]
        url = item["url"]
        if domain in preprocessed_data:
            preprocessed_data[domain].append(url)
        else:
            preprocessed_data[domain] = [url]

    return preprocessed_data


def create_embeddings(data: DataSource):
    documents = []

    domain_urls = preprocess_urls(data)

    for [domain, urls] in domain_urls.items():
        value = domain_strategy_map[domain]
        loader = HTMLLoader(urls=urls, strategy=value["strategy"])
        docs = loader.load_and_split(**value["kwargs"])
        documents.extend(docs)

    vector_store.add_documents(documents=documents)
