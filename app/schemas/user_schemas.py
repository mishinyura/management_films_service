from pydantic import BaseModel
from sqlalchemy.orm import Mapped
from uuid import UUID


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: UUID
    username: str

    class Config:
        from_attributes = True


class UserSchema(BaseModel):
    # uuid: Mapped[UUID]
    username: str
    password: str
    # film_id: Mapped[int]