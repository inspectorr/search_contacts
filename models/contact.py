from sqlalchemy import Column, Integer, String

from database.config import Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    def __repr__(self):
        return f"Contact(id={self.id}, name={self.name})"
