import uvicorn
from fastapi import FastAPI
from app.app import get_app
from app.config import settings
from app.api.routes import api_router


def run_app():
    app = FastAPI(docs_url='/docs')
    app.include_router(api_router, prefix='')
    app.mount(settings.app.app_mount, get_app())
    uvicorn.run(
        app,
        host=settings.app.app_host,
        port=settings.app.app_port,
        log_config=None,
    )

