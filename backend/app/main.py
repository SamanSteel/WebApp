# Third Library
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.search import router as search_router
from sqlalchemy import create_engine

base_url_path = "/api"

app = FastAPI(title="WareHouse API", docs_url=base_url_path + "/docs")
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(search_router, prefix=base_url_path + "/search")


@app.get("/api")
def get_version():

    engine = create_engine("postgresql://shijar:shijar@15101367@@localhost/postgres")
    with engine.connect() as conn:
        pass
    engine.dialect.server_version_info
