from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.film_repo import film_repo
from app.schemas.film_schemas import FilmSchema





if not api_key:
    raise ValueError("API_KEY is not set")


class FilmService:

    def __init__(self):
        self.repo = film_repo
    
    async def get_film_details(self, kinopoisk_id, session: AsyncSession) -> FilmSchema:
        details = await self.repo.get_details(session=session, kinopoisk_id=kinopoisk_id)
        return details
        


film_service = FilmService()