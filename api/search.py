import logging

from fastapi import APIRouter, BackgroundTasks, HTTPException, Request

from api.metadata import get_request_metadata
from services.contact import search_contacts_elastic
from services.contact_search_log import create_contact_search_log

router = APIRouter()

logger = logging.getLogger(__name__)


MAX_QUERY_LENGTH = 30


@router.get("/search/")
def search_contacts(
    request: Request,
    search_query: str,
    background_tasks: BackgroundTasks
):
    if not search_query:
        raise HTTPException(status_code=400, detail="Search query is empty")
    if len(search_query) > MAX_QUERY_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Search query is longer than {MAX_QUERY_LENGTH} characters"
        )
    try:
        contacts, total_contacts = search_contacts_elastic(search_query)
        background_tasks.add_task(
            func=create_contact_search_log,
            search_query=search_query,
            search_result=contacts,
            search_result_count=total_contacts,
            search_metadata=get_request_metadata(request)
        )
        return {"result": contacts}
    except Exception as e:
        logger.error('Error searching contacts: %s', e, exc_info=True)
        raise HTTPException(status_code=503, detail="Service Unavailable")
