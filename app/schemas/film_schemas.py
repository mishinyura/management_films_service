from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel


class ProductionStatus(str, Enum):
    POST_PRODUCTION = "POST_PRODUCTION"

class Type(str, Enum):
    FILM = "FILM"

class Country(BaseModel):
    country: str

class Genre(BaseModel):
    genre: str

class FilmSchema(BaseModel):
    kinopoiskId: int
    kinopoiskHDId: str
    imdbId: str
    nameRu: str
    nameEn: str
    nameOriginal: str
    posterUrl: str
    posterUrlPreview: str
    coverUrl: str
    logoUrl: str
    reviewsCount: int
    ratingGoodReview: float
    ratingGoodReviewVoteCount: int
    ratingKinopoisk: float
    ratingKinopoiskVoteCount: int
    ratingImdb: float
    ratingImdbVoteCount: int
    ratingFilmCritics: float
    ratingFilmCriticsVoteCount: int
    ratingAwait: float
    ratingAwaitCount: int
    ratingRfCritics: float
    ratingRfCriticsVoteCount: int
    webUrl: str
    year: int
    filmLength: int
    slogan: str
    description: str
    shortDescription: str
    editorAnnotation: str
    isTicketsAvailable: bool
    productionStatus: ProductionStatus
    type: Type
    ratingMpaa: str
    ratingAgeLimits: str
    hasImax: bool
    has3D: bool
    lastSync: datetime
    countries: List[Country]
    genres: List[Genre]
    startYear: int
    endYear: int
    serial: bool
    shortFilm: bool
    completed: bool

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
        }

