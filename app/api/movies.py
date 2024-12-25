from fastapi import APIRouter, Depends, HTTPException
from app.models.users import User
from app.services.auth import get_current_user
from app.services.kinopoisk_api import KinopoiskClient, get_kinopoisk_client
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_session
from app.models.users import UserFilm
from sqlalchemy import select, delete
from loguru import logger

movies_router = APIRouter(prefix="/movies", tags=["movies"])


@movies_router.get("/search")
async def search_movies(
    query: str,
    current_user: User = Depends(get_current_user),
    kinopoisk_client: KinopoiskClient = Depends(get_kinopoisk_client),
):
    logger.info(f"Поиск фильмов: запрос '{query}' от пользователя {current_user.username}")
    try:
        result = await kinopoisk_client.search_movies(query)
        logger.success(f"Поиск фильмов: успешно для запроса '{query}'")
        return result
    except Exception as e:
        logger.error(f"Поиск фильмов: ошибка для запроса '{query}' - {str(e)}")
        raise HTTPException(status_code=500, detail="Ошибка при поиске фильмов")


@movies_router.get("/{kinopoisk_id}")
async def get_movie_details(
    kinopoisk_id: int,
    current_user: User = Depends(get_current_user),
    kinopoisk_client: KinopoiskClient = Depends(get_kinopoisk_client),
):
    logger.info(f"Получение деталей фильма: ID {kinopoisk_id} от пользователя {current_user.username}")
    try:
        result = await kinopoisk_client.get_movie_details(kinopoisk_id)
        logger.success(f"Получение деталей фильма: успешно для ID {kinopoisk_id}")
        return result
    except Exception as e:
        logger.error(f"Получение деталей фильма: ошибка для ID {kinopoisk_id} - {str(e)}")
        raise HTTPException(status_code=500, detail="Ошибка при получении деталей фильма")


@movies_router.post("/favorites")
async def add_to_favorites(
    kinopoisk_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_session),
):
    logger.info(f"Добавление в избранное: фильм ID {kinopoisk_id} от пользователя {current_user.username}")
    try:
        existing_film = await db.execute(
            select(UserFilm).where(UserFilm.user_uuid == current_user.uuid, UserFilm.film_id == kinopoisk_id)
        )
        if existing_film.scalar():
            logger.warning(f"Добавление в избранное: фильм ID {kinopoisk_id} уже в избранном")
            raise HTTPException(status_code=400, detail="Фильм уже в избранном")

        new_film = UserFilm(user_uuid=current_user.uuid, film_id=kinopoisk_id)
        db.add(new_film)
        await db.commit()
        logger.success(f"Добавление в избранное: успешно для фильма ID {kinopoisk_id}")
        return {"message": "Фильм добавлен в избранное"}
    except Exception as e:
        logger.error(f"Добавление в избранное: ошибка для фильма ID {kinopoisk_id} - {str(e)}")
        raise HTTPException(status_code=500, detail="Ошибка при добавлении в избранное")


@movies_router.delete("/favorites/{kinopoisk_id}")
async def remove_from_favorites(
    kinopoisk_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_session),
):
    logger.info(f"Удаление из избранного: фильм ID {kinopoisk_id} от пользователя {current_user.username}")
    try:
        result = await db.execute(
            delete(UserFilm).where(UserFilm.user_uuid == current_user.uuid, UserFilm.film_id == kinopoisk_id)
        )
        if result.rowcount == 0:
            logger.warning(f"Удаление из избранного: фильм ID {kinopoisk_id} не найден")
            raise HTTPException(status_code=404, detail="Фильм не найден в избранном")

        await db.commit()
        logger.success(f"Удаление из избранного: успешно для фильма ID {kinopoisk_id}")
        return {"message": "Фильм удален из избранного"}
    except Exception as e:
        logger.error(f"Удаление из избранного: ошибка для фильма ID {kinopoisk_id} - {str(e)}")
        raise HTTPException(status_code=500, detail="Ошибка при удалении из избранного")


@movies_router.get("/favorites")
async def get_favorites(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_session),
    kinopoisk_client: KinopoiskClient = Depends(get_kinopoisk_client),
):
    logger.info(f"Получение избранных фильмов: запрос от пользователя {current_user.username}")
    try:
        result = await db.execute(select(UserFilm).where(UserFilm.user_uuid == current_user.uuid))
        user_films = result.scalars().all()

        favorites = []
        for film in user_films:
            details = await kinopoisk_client.get_movie_details(film.film_id)
            favorites.append(details)

        logger.success(f"Получение избранных фильмов: успешно для пользователя {current_user.username}")
        return favorites
    except Exception as e:
        logger.error(f"Получение избранных фильмов: ошибка для пользователя {current_user.username} - {str(e)}")
        raise HTTPException(status_code=500, detail="Ошибка при получении избранных фильмов")