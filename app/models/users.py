from uuid import UUID, uuid4
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as U_UUID

from app.db import Base


class User(Base):
    __tablename__ = 'users'

    uuid: Mapped[UUID] = mapped_column(U_UUID(as_uuid=True), primary_key=True, default=uuid4)
    username: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)
    password: Mapped[bool] = mapped_column(String(256), nullable=False)
