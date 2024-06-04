import logging

from fastapi import APIRouter, BackgroundTasks, HTTPException, Request

from api.metadata import get_request_metadata
from services.contact import search_contacts_elastic
from services.contact_search_log import create_contact_search_log

router = APIRouter()

logger = logging.getLogger(__name__)  # todo: set up logging + more logs

# todo sql fallback


@router.get("/search/")
def search_contacts(
    request: Request,
    search_query: str,
    background_tasks: BackgroundTasks
):
    try:
        contacts = search_contacts_elastic(search_query)
        background_tasks.add_task(
            create_contact_search_log,
            search_query,
            contacts,
            get_request_metadata(request)
        )
        return {"result": contacts}
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Error!")
