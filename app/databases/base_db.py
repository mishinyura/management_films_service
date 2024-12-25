from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any


class BaseDB(ABC):
    @abstractmethod
    async def get(self) -> Any:
        pass

    @abstractmethod
    async def add(self, batch: Any) -> None:
        pass