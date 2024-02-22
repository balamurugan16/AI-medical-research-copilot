from enum import Enum


class Domains(Enum):
    PUBMED = "PubMed"
    DAILYMED = "DailyMed"
    DRUGBANK = "DrugBank"
    FDA = "FDA"


class Extraction(Enum):
    WRAPPER = "wrapper"
    TAG = "tag"


class DataSource:
    url: str
    domain: str
