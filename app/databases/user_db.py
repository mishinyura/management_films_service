from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.core.exceptions import SqlException
from app.models.user_model import User
from app.databases.base_db import BaseDB
from app.schemas.user_schema import UserSchema


class UserDB(BaseDB):
    async def get(self, user_id: int, session: AsyncSession) -> UserSchema:
        result = await session.execute(select(User).where(User.id == user_id))
        print('RESS: ', result)
        return result

    # async def get_all(self, session: AsyncSession) -> list[UserSchema]:
    #     result = await session.execute(select(User))
    #     return [
    #         UserSchema.model_validate(user) for user in result.scalars().all()
    #     ]

    async def add(self, user: User, session: AsyncSession) -> None:
        try:
            session.add(user)
            await session.commit()
        except SQLAlchemyError as exc:
            await session.rollback()
            raise SqlException(message=str(exc))


user_db = UserDB()