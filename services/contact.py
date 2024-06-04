from typing import TypedDict

from elastic.config import get_es_client


class ContactSearchResult(TypedDict):
    id: int
    name: str


def search_contacts_elastic(
    search_query: str,
    fuzziness: int = 1
) -> list[ContactSearchResult]:
    es = get_es_client()
    response = es.search(
        index="contacts-index",
        body={
            "query": {
                "fuzzy": {
                    "name": {
                        "value": search_query,
                        "fuzziness": fuzziness
                    }
                }
            }
        }
    )
    return [
        {
            "id": hit["_source"]["id"],
            "name": hit["_source"]["name"]
        }
        for hit in response['hits']['hits']
    ]
