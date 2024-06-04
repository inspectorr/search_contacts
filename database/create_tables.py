from database.config import engine, Base
from models import *


def migrate():
    Base.metadata.create_all(bind=engine)
    print("Tables created")


if __name__ == "__main__":
    migrate()
