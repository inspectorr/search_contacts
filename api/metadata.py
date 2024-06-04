from typing import TypedDict
from datetime import datetime
from fastapi import Request


class RequestMetadata(TypedDict):
    timestamp: float
    user_agent: str
    accept_language: str
    client_ip: str


def get_request_metadata(request: Request) -> RequestMetadata:
    request_time = datetime.now()
    user_agent = request.headers.get('User-Agent')
    accept_language = request.headers.get('Accept-Language')
    client_ip = request.client.host if request.client else None

    return {
        "timestamp": request_time,
        "user_agent": user_agent,
        "accept_language": accept_language,
        "client_ip": client_ip,
    }
