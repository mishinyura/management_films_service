from pydantic import BaseModel
from uuid import UUID


class UserCreate(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    uuid: UUID
    username: str

    class Config:
        from_attributes = True
