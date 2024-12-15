from uuid import UUID, uuid4
from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as U_UUID
from datetime import datetime

from app.db import Base


class User(Base):
    __tablename__ = 'users'

    uuid:               Mapped[UUID] = mapped_column(U_UUID(as_uuid=True), primary_key=True, default=uuid4)
    username:           Mapped[str] = mapped_column(String(256), nullable=False, unique=True)
    created_at:         Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())
    hashed_password:    Mapped[bool] = mapped_column(String(256), nullable=False)
