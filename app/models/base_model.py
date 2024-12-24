from datetime import datetime
from sqlalchemy import DateTime, Integer, Column
from sqlalchemy.orm import Mapped, mapped_column


class BaseModel:
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    update_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
