from pydantic import BaseModel


class FilmResponseSchema(BaseModel):
    kinopoisk_id: str
