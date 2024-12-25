from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import DuplicateException, SqlException
from app.models.user_model import User
from app.databases.user_db import user_db
from app.schemas.user_schema import UserSchema


class UserService:
    def __init__(self):
        self.db = user_db

    async def get_user(self, session: AsyncSession) -> UserSchema:
        user = await self.db.get(session=session)
        return user

    async def add_user(self, request: UserSchema, session: AsyncSession) -> None:
        user = User(username=request.username, password=request.password)
        try:
            await self.db.add(user=user, session=session)
        except SqlException as exc:
            raise DuplicateException(message=str(exc))


user_service = UserService()