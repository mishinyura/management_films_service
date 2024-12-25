from sqlalchemy import Column, Integer, String
from app.core.db import Base
from app.models.base_model import BaseModel


class User(BaseModel, Base):
    __tablename__ = "users"

    username = Column(String, nullable=False)
    password = Column(String, nullable=False)