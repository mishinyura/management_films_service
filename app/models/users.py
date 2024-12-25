from uuid import UUID, uuid4
from sqlalchemy import DateTime, String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy.dialects.postgresql import UUID as U_UUID
from datetime import datetime

from app.db import Base


class BaseUsers(DeclarativeBase):
    __abstract__ = True
    __table_args__ = {
        'schema': 'service'
    }
    pass


class User(BaseUsers):
    __tablename__ = 'users'

    uuid:               Mapped[UUID] = mapped_column(U_UUID(as_uuid=True), primary_key=True, default=uuid4)
    username:           Mapped[str] = mapped_column(String(256), nullable=False, unique=True)
    created_at:         Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())
    hashed_password:    Mapped[bool] = mapped_column(String(256), nullable=False)
    films:              Mapped[list['UserFilm']] = relationship(back_populates='user')


class UserFilm(BaseUsers):
    __tablename__ = 'user_films'
    user_uuid:    Mapped[UUID] = mapped_column(U_UUID(as_uuid=True), ForeignKey('service.users.uuid',
                                               ondelete='CASCADE'), primary_key=True)
    film_id:      Mapped[int] = mapped_column(Integer, primary_key=True)

    user:         Mapped['User'] = relationship(back_populates='films')

