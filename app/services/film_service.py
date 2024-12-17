from app.schemas.film_schemas import FilmSchema
from app.config import settings


api_key = settings.app.app_api_key

if not api_key:
    raise ValueError("API_KEY is not set")


class FilmService:

    def __init__(self):
        pass

    async def get_film_by_name(self, name: str) -> FilmSchema:
        # вход в кинопоиск
        pass

    async def get_film_details(self):
        # вход в кинопоиск
        pass
        


film_service = FilmService()