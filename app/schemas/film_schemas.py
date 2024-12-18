from pydantic import BaseModel


class FilmResponseSchema(BaseModel):
    kinopoisk_Id: int
