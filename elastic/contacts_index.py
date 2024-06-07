from elasticsearch import Elasticsearch

from database.config import SessionLocal
from models.contact import Contact

# todo base class for creation/deletion/adding data manager


def create_contacts_index(es: Elasticsearch):
    if es.indices.exists(index="contacts-index"):
        print("Index contacts-index already exists")
        return
    es.indices.create(index="contacts-index", body={
        "settings": {
            "analysis": {
                "analyzer": {
                    "edge_ngram_analyzer": {
                        "type": "custom",
                        "tokenizer": "edge_ngram_tokenizer",
                        "filter": ["lowercase"]
                    }
                },
                "tokenizer": {
                    "edge_ngram_tokenizer": {
                        "type": "edge_ngram",
                        "min_gram": 1,
                        "max_gram": 10,
                        "token_chars": ["letter", "digit"]
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "text",
                    "analyzer": "edge_ngram_analyzer",
                    "fields": {
                        "keyword": {
                            "type": "keyword"
                        }
                    }
                }
            }
        }
    })
    print("Index contacts-index created")


def add_data_to_contacts_index(es: Elasticsearch):
    session = SessionLocal()
    contacts = session.query(Contact).all()

    for contact in contacts:
        document = {
            "id": contact.id,
            "name": contact.name
        }
        es.index(index="contacts-index", id=contact.id, document=document)

    print("Data added to contacts-index")


def drop_contacts_index(es: Elasticsearch):
    es.indices.delete(index="contacts-index")
    print("Index contacts-index deleted")
