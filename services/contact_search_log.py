from database.config import SessionLocal
from models.contact_search_log import ContactSearchLog
from api.metadata import RequestMetadata


def create_contact_search_log(
    search_query: str,
    search_result: str,
    search_metadata: RequestMetadata
) -> None:
    session = SessionLocal()
    new_log = ContactSearchLog(
        search_query=search_query,
        search_result=search_result,
        search_result_count=len(search_result),
        **search_metadata
    )
    session.add(new_log)
    session.commit()
    session.close()
