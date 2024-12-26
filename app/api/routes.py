from fastapi import APIRouter

from app.api.login import login_router
from app.api.movies import movies_router
from loguru import logger
from app.logger import logger as app_logger

api_router = APIRouter()
api_router.include_router(login_router)
api_router.include_router(movies_router)
logger.info("Приложение запущено")