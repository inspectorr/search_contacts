import logging

from fastapi import FastAPI

from api.search import router as search_router

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

app = FastAPI()
app.include_router(search_router)
