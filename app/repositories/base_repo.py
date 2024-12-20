from abc import ABC, abstractmethod

from typing import Any

class BaseRepo(ABC):

    @abstractmethod
    async def get_details(self) -> Any:
        ...