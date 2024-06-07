from elasticsearch import Elasticsearch


es_client = Elasticsearch(
    hosts=["http://elasticsearch:9200"],
    http_auth=("elastic", "pass")
)


def get_es_client() -> Elasticsearch:
    return es_client
