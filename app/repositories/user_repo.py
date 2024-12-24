from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user_schemas import UserSchema
from app.models.user_model import User


class UserRepo(BaseModel):
    async def get_user(self, session: AsyncSession) -> UserSchema:
        result = await session.execute(select(User))
        return result

    async def add(self, session: AsyncSession, user: User) -> None:
        session.add(user)
        await session.commit()


user_repo = UserRepo()