from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String

from app.models.base_model import BaseModel
from app.db import Base

class User(Base, BaseModel):
    __tablename__ = 'users'

    username = Column(String(255), nullable=False)