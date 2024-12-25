import aiohttp
from fastapi import HTTPException
from app.config import settings
from fastapi import Depends

KINOPOISK_API_URL = "https://kinopoiskapiunofficial.tech"
API_KEY = settings.app.api_key


class KinopoiskClient:
    def __init__(self):
        self.session = aiohttp.ClientSession(headers={"X-API-KEY": API_KEY})

    async def close(self):
        await self.session.close()

    async def search_movies(self, query: str):
        url = f"{KINOPOISK_API_URL}/api/v2.1/films/search-by-keyword"
        params = {"keyword": query, "page": 1}
        async with self.session.get(url, params=params) as response:
            if response.status != 200:
                raise HTTPException(status_code=response.status, detail="Ошибка при запросе к Кинопоиску")
            return await response.json()

    async def get_movie_details(self, kinopoisk_id: int):
        url = f"{KINOPOISK_API_URL}/api/v2.2/films/{kinopoisk_id}"
        async with self.session.get(url) as response:
            if response.status != 200:
                raise HTTPException(status_code=response.status, detail="Ошибка при запросе к Кинопоиску")
            return await response.json()


async def get_kinopoisk_client():
    client = KinopoiskClient()
    try:
        yield client
    finally:
        await client.close()
