from typing import TypedDict

from elasticsearch_dsl import Search, Q

from elastic.config import get_es_client


class ContactSearchResult(TypedDict):
    id: int
    name: str


def search_contacts_elastic(
    search_query: str
) -> (list[ContactSearchResult], int):
    """
    Найти контакты в индексе эластика.
    Поисковая строка допускает 0-2 опечатки в зависимости от длины.

    Args:
        search_query (str): запрос

    Returns:
        list[ContactSearchResult]: список контактов (первые 10, todo пагинация)
        int: общее количество контактов
    """
    search = Search(using=get_es_client(), index="contacts-index")

    search_query = search_query.strip().lower()
    query = Q(
        'bool',
        should=[
            Q(
                'prefix',
                name__keyword={'value': search_query, 'boost': 2},
            ),
            Q(
                'match',
                name={'query': search_query, 'fuzziness': 'AUTO', 'boost': 1}
            )
        ]
    )

    response = search.query(query).execute()

    contacts = [{"id": hit.id, "name": hit.name} for hit in response]
    total_contacts = response.hits.total.value

    return contacts, total_contacts
