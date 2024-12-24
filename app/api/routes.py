from fastapi import APIRouter
from app.api.login import login_router

api_router = APIRouter()
api_router.include_router(login_router)
