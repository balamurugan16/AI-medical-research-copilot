from langchain_core.documents import Document
from typing import List, Dict
from langchain_community.document_transformers import BeautifulSoupTransformer
from abc import ABC, abstractmethod


class ExtractionStrategy(ABC):
    @abstractmethod
    def extract_html(self, docs: List[Document], **kwargs):
        pass


class WrapperExtraction(ExtractionStrategy):
    def extract_html(self, docs: List[Document], root_tag: Dict[str, str]):
        from bs4 import BeautifulSoup

        for doc in docs:
            soup = BeautifulSoup(doc.page_content, "html.parser")
            element = None
            if "id" in root_tag:
                element = soup.find(root_tag["tag"], id=root_tag["id"])
            elif "class" in root_tag:
                element = soup.find(root_tag["tag"], class_=root_tag["class"])
            else:
                raise ValueError(
                    "Search criteria must contain 'id' or 'class_' property."
                )
            doc.page_content = element.get_text(strip=True, separator=" ")

        return docs


class TagsExtraction(ExtractionStrategy):
    def extract_html(
        self, docs: List[Document], unwanted_tags: List[str], tags_to_extract: List[str]
    ):
        transformer = BeautifulSoupTransformer()
        docs = transformer.transform_documents(
            documents=docs,
            unwanted_tags=unwanted_tags,
            tags_to_extract=tags_to_extract,
        )
        return docs
