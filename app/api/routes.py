from fastapi import APIRouter
from app.api.login import router as login


api_router = APIRouter()
api_router.include_router(login)
