import uvicorn
import asyncio
from fastapi import FastAPI
from app.core.app import get_app
from app.core.config import settings
from app.core.db import create_tables
from app.core.logger import setup_logger


def run_api_app() -> None:
    setup_logger()
    app = get_app()
    app.mount(settings.app.app_mount, app)
    asyncio.run(create_tables())
    uvicorn.run(
        app, host=settings.app.app_host, port=settings.app.app_port, log_config=None
    )
