from pydantic import BaseModel


class FilmSchema(BaseModel):
    kinopoisk_id: str