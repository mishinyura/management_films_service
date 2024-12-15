from datetime import datetime
from sqlalchemy import Column, DateTime, Integer


class BaseModel:
    id = Column(Integer, primary_key=True)
    update_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )
