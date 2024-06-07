import logging

from api.metadata import RequestMetadata
from database.config import SessionLocal
from models.contact_search_log import ContactSearchLog


logger = logging.getLogger(__name__)


def create_contact_search_log(
    search_query: str,
    search_result: str,
    search_result_count: int,
    search_metadata: RequestMetadata
) -> None:
    session = SessionLocal()
    new_log = ContactSearchLog(
        search_query=search_query,
        search_result=search_result,
        search_result_count=search_result_count,
        **search_metadata
    )
    session.add(new_log)
    session.commit()
    logger.info('Contact search log created %r', new_log)
    session.close()
