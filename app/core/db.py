from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import settings


engine = create_async_engine(url=settings.db.db_url, echo=True, poolclass=NullPool)

async_session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=True
)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session():
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    pass