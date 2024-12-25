import json
from http.client import HTTPException

from fastapi import APIRouter, Depends
from starlette.responses import Response
from starlette.status import *
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.base_model import BaseModel
from app.models.user_model import User
# from app.schemas.film_schemas import FilmSchema
from app.core.config import settings
# from app.services.film_services import film_services

# from app.services.payment_service import payment_service
from app.core.db import get_session
# from app.exceptions import DuplicateException


films_router = APIRouter(tags=["films"])


@films_router.get("/search")
def get_films():
    return "OK"


@films_router.get("/{film_id}")
async def get_film_info_by_film_id(film_id: int):
    pass
    # film_info = await film_services.get_film_info_by_film_id(film_id)
    #
    # return Response(
    #     status_code=HTTP_200_OK,
    #     content=json.dumps(film_info, ensure_ascii=False, indent=4),
    # )


@films_router.post("/favourites/{film_id}")
async def add_film_to_favourites(
    film_id: int,
    session: AsyncSession = Depends(get_session),
    user_id: str = settings.kp.kinopoinsk_api_key,
):
    pass
    # try:
    #     film_info = await film_services.add_film(film_id, user_id, session)
    # except Exception as error:
    #     return Response(status_code=HTTP_400_BAD_REQUEST, content=str(error))
    #
    # return Response(
    #     status_code=201,
    #     content=json.dumps(
    #         {"message": "Film has been added to favourites"},
    #         ensure_ascii=False,
    #         indent=4,
    #     ),
    # )


@films_router.get("/favourites/films")
async def get_favourite_films(
    user_id: str = settings.kp.kinopoinsk_api_key,
    session: AsyncSession = Depends(get_session),
):
    pass
    # try:
    #     favourite_films = await film_services.get_favourite_films(user_id, session)
    # except Exception as error:
    #     return Response(status_code=HTTP_400_BAD_REQUEST, content=str(error))
    # return Response(
    #     status_code=HTTP_200_OK,
    #     content=json.dumps(favourite_films, ensure_ascii=False, indent=4),
    # )


@films_router.delete("/favourites/{film_id}")
async def delete_film_from_favourites(
    film_id: int,
    session: AsyncSession = Depends(get_session),
    user_id: str = settings.kp.kinopoinsk_api_key,
):
    pass
    # try:
    #     film_info = await film_services.delete_film_from_favourites(
    #         user_id, film_id, session
    #     )
    # except Exception as error:
    #     return Response(status_code=HTTP_400_BAD_REQUEST, content=str(error))
    # return Response(status_code=HTTP_204_NO_CONTENT)
