from sqlalchemy import Column, Integer, String, DateTime, JSON

from database.config import Base


class ContactSearchLog(Base):
    __tablename__ = "contact_search_log"

    id = Column(Integer, primary_key=True, index=True)
    search_query = Column(String)
    search_result = Column(JSON)
    search_result_count = Column(Integer)
    # RequestMetadata
    timestamp = Column(DateTime)
    user_agent = Column(String, nullable=True)
    accept_language = Column(String, nullable=True)
    client_ip = Column(String, nullable=True)

    def __repr__(self):
        return f"ContactSearchLog(id={self.id}, search_query={self.search_query})"
