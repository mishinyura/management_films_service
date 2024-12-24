import uvicorn
from fastapi import FastAPI, APIRouter
from app.app import get_app
from app.config import settings


def run_api_app() -> None:
    app = get_app()
    app.mount(settings.app.app_mount, app)
    uvicorn.run(
        app,
        host=settings.app.app_host,
        port=settings.app.app_port,
        log_config=None,
        reload=True
    )
