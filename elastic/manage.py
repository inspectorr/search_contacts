from elastic.config import get_es_client
from elastic.contacts_index import (
    create_contacts_index,
    add_data_to_contacts_index,
    drop_contacts_index,
)


def create_indices():
    create_contacts_index(get_es_client())


def add_data_to_indices():
    add_data_to_contacts_index(get_es_client())


def drop_indices():
    drop_contacts_index(get_es_client())


if __name__ == "__main__":
    create_indices()
    add_data_to_indices()
