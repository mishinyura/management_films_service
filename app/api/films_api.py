from fileinput import filename
from fastapi import APIRouter
from starlette.responses import Response
from starlette.status import HTTP_404_NOT_FOUND

from app.schemas.film_schemas import FilmResponseSchema
from app.services.film_service import film_service


films_router = APIRouter(tags=["films"])


# Ищет фильмы по названию, используя эндпойнт:
# GET /api/v2.1/films/search-by-keyword
@films_router.get("films/search-by-keyword", response_model=FilmResponseSchema | None)
async def get_film(film_name: str):
    film = await film_service.get_film_by_name(film_name)
    if not film:
        return Response(status_code=HTTP_404_NOT_FOUND)
    return film


# Получает подробную информацию о фильме по его Kinopoisk ID, используя эндпойнт:
# GET /api/v2.2/films/{kinopoisk_id}
@films_router.get("films/kinopoisk_id", response_model=FilmResponseSchema | None)
async def get_details(kinopoisk_id: str):
    details = await film_service.get_film_details(kinopoisk_id)
    if not details:
        return Response(status_code=HTTP_404_NOT_FOUND)
    return details
