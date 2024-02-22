from langchain_community.document_loaders.base import BaseLoader
from langchain_core.documents import Document
from typing import Iterator, List, cast, Any
from langchain.text_splitter import RecursiveCharacterTextSplitter, TextSplitter
from app.utils.models import Extraction
from app.utils.strategies import TagsExtraction, WrapperExtraction


class HTMLLoader(BaseLoader):
    def __init__(self, urls: List[str], strategy: Extraction):
        if strategy == Extraction.WRAPPER:
            self.strategy = WrapperExtraction()
        else:
            self.strategy = TagsExtraction()
        self.urls = urls
        try:
            import requests
        except ImportError:
            raise ImportError("Requests module is required for HTMLLoader")
        self.text_splitter = RecursiveCharacterTextSplitter.from_language(
            language="html", chunk_size=1000, chunk_overlap=0
        )

    def get_html_data(self, url: str) -> str:
        import requests

        data = requests.get(url)
        return data.text

    def load_and_split(
        self, text_splitter: TextSplitter | None = None, **kwargs
    ) -> List[Document]:
        html = self.load()
        docs = self.strategy.extract_html(html, **kwargs)
        return self.text_splitter.split_documents(docs)

    def load(self) -> List[Document]:
        return list(self.lazy_load())

    def lazy_load(self) -> Iterator[Document]:
        for url in self.urls:
            page_content = self.get_html_data(url)
            metadata = {"source": url}
            yield Document(page_content=page_content, metadata=metadata)


def get_navigable_strings(element: Any) -> Iterator[str]:
    """Get all navigable strings from a BeautifulSoup element.

    Args:
        element: A BeautifulSoup element.

    Returns:
        A generator of strings.
    """

    from bs4 import NavigableString, Tag

    for child in cast(Tag, element).children:
        if isinstance(child, Tag):
            yield from get_navigable_strings(child)
        elif isinstance(child, NavigableString):
            if (element.name == "a") and (href := element.get("href")):
                yield f"{child.strip()} ({href})"
            else:
                yield child.strip()
