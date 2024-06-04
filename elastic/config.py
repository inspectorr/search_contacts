from elasticsearch import Elasticsearch


def get_es_client() -> Elasticsearch:
    return Elasticsearch(
        hosts=["http://elasticsearch:9200"],
        http_auth=("elastic", "pass")
    )
