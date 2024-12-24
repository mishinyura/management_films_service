from uuid import UUID, uuid4
from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as U_UUID

from app.db import Base
from app.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    # uuid: Mapped[UUID] = mapped_column(U_UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True)
    username = Column(String(256), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    # films: Mapped[int] = mapped_column(String(256), ForeignKey('films.film_id'), nullable=False)

    def __repr__(self):
        return (
            # f"UUID(user_id={self.uuid!r}, "
            f"username={self.username!r}, "
            # f"films={self.films!r}, "
        )

    def __str__(self):
        return (
            # f"UUID(user_id={self.uuid!r}, "
            f"username={self.username!r}, "
            # f"films={self.films!r}, "
        )
