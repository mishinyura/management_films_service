from fastapi import APIRouter
from app.api.login import router as login
from app.api.films_api import films_router


api_router = APIRouter()
api_router.include_router(login)

ROUTES = {
    "/films": films_router,
}
