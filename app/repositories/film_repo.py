import aiohttp
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.film_schemas import FilmSchema
from app.repositories.base_repo import BaseRepo
from app.config import settings



class FilmRepo(BaseRepo):

    def __ini__(self):
        self.url=settings.kinopoisk.kinopoinsk_base_url
        self._api_key=settings.kinopoisk.kinopoinsk_api_key

    async def get_details(self, kinopoisk_id: int, session: AsyncSession) -> FilmSchema:
        headers = {'X-API-KEY': self._api_key}
        details = await session.get(
            session,
            f'{self.url}+{kinopoisk_id}',
            headers
        )
        return await details

film_repo = FilmRepo()